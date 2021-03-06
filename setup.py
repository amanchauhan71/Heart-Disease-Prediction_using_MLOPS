from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    description="Solving heart disease problem and creating monitoring or managing system",
    long_description=long_description,
    url="https://github.com/amanchauhan71/simple-dvc-project",
    author_email="amanchauhan7172@gmail.com",
    packages=["src"],
    license="GNU",
    python_requires=">=3.6",
    install_requires= [
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)