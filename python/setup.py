from setuptools import setup, find_packages

setup(
    name="rebuff",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["langchain>=0.0.100", "pydantic>=1", "requests<3,>=2"],
    extras_require={
        "dev": [
            "pytest",
            "black>=23.0,<24",
            "flake8>=6.0,<7",
            "isort>=5.0,<6",
            "mypy>=1.0,<2",
        ],
    },
    test_suite="tests",
)
