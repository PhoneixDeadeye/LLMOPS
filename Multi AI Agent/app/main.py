import subprocess
import threading
import time
import os

from dotenv import load_dotenv
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

load_dotenv()

def run_backend():
    try:
        logger.info("Starting backend server...")
        # Set environment for subprocess
        env = os.environ.copy()
        env['PYTHONPATH'] = os.getcwd()
        
        backend_process = subprocess.Popen(
            ["python", "-m", "uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        logger.info("Backend server started successfully")
        return backend_process
    except Exception as e:
        logger.error(f"Problem with backend service: {e}")
        raise CustomException("Failed to start Backend") from e

def run_frontend():
    try:
        logger.info("Starting frontend server...")
        # Set environment for subprocess
        env = os.environ.copy()
        env['PYTHONPATH'] = os.getcwd()
        
        frontend_process = subprocess.Popen(
            ["streamlit", "run", "app/frontend/ui.py"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        logger.info("Frontend server started successfully")
        return frontend_process
    except Exception as e:
        logger.error(f"Problem with Frontend service: {e}")
        raise CustomException("Failed to start Frontend") from e

if __name__ == "__main__":
    try:
        # Start backend
        backend_process = run_backend()
        time.sleep(3)  # Wait for backend to start
        
        # Check backend startup
        if backend_process.poll() is None:
            logger.info("Backend process is running")
        else:
            logger.error("Backend process failed to start")
            stdout, stderr = backend_process.communicate()
            logger.error(f"Backend stdout: {stdout}")
            logger.error(f"Backend stderr: {stderr}")

        # Start frontend  
        frontend_process = run_frontend()
        time.sleep(2)  # Wait for frontend to start
        
        # Check frontend startup
        if frontend_process.poll() is None:
            logger.info("Frontend process is running")
        else:
            logger.error("Frontend process failed to start")
            stdout, stderr = frontend_process.communicate()
            logger.error(f"Frontend stdout: {stdout}")
            logger.error(f"Frontend stderr: {stderr}")

        logger.info("Both servers started. Backend: http://127.0.0.1:9999, Frontend: http://localhost:8501")

        # Keep main thread alive and monitor processes
        try:
            while True:
                # Check if processes are still running
                if backend_process.poll() is not None:
                    logger.error("Backend process has stopped unexpectedly")
                    stdout, stderr = backend_process.communicate()
                    logger.error(f"Backend stdout: {stdout}")
                    logger.error(f"Backend stderr: {stderr}")
                    break
                if frontend_process.poll() is not None:
                    logger.error("Frontend process has stopped unexpectedly")
                    stdout, stderr = frontend_process.communicate()
                    logger.error(f"Frontend stdout: {stdout}")
                    logger.error(f"Frontend stderr: {stderr}")
                    break
                time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Shutting down servers...")
            backend_process.terminate()
            frontend_process.terminate()

    except CustomException as e:
        logger.exception(f"CustomException occurred: {str(e)}")