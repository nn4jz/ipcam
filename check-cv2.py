import sys
import importlib.util
import os

def get_current_environment():
    """
    Detects the current Python environment (virtualenv, conda, or system).
    """
    # Check for virtualenv or venv
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        env_type = "Virtualenv/Venv"
        env_path = sys.prefix
    # Check for conda
    elif os.environ.get('CONDA_DEFAULT_ENV'):
        env_type = f"Conda ({os.environ['CONDA_DEFAULT_ENV']})"
        env_path = sys.prefix
    else:
        env_type = "System Python"
        env_path = sys.prefix

    return env_type, env_path

def is_module_installed(module_name):
    """
    Checks if a Python module is installed in the current environment.
    """
    return importlib.util.find_spec(module_name) is not None

if __name__ == "__main__":
    env_type, env_path = get_current_environment()
    print(f"Environment Type: {env_type}")
    print(f"Environment Path: {env_path}")
    print(f"Python Executable: {sys.executable}")

    if is_module_installed("cv2"):
        import cv2
        print(f"✅ OpenCV (cv2) is installed. Version: {cv2.__version__}")
    else:
        print("❌ OpenCV (cv2) is NOT installed in this environment.")
