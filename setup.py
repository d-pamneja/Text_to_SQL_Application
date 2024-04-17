from setuptools import find_packages, setup 

setup(
    name="Text to SQL LLM Application",
    version="0.0.1",
    author="Dhruv Pamneja",
    author_email="dpamneja@gmail.com",
    install_requires = ["google-generativeai","streamlit","python-dotenv"],
    packages=find_packages()
)