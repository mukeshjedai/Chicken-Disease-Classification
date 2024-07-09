import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="cnnclassifier",  # lowercase package name
    version="0.1.0",       # Start with a non-zero version
    author="mukeshjedai",
    author_email="mukeshbcc56@gmail.com",
    description="A Python package for CNN-based classification", 
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url="https://github.com/mukeshjedai/Chicken-Disease-Classification",
    project_urls={
        "Bug Tracker": "https://github.com/mukeshjedai/Chicken-Disease-Classification/issues",
    },
    classifiers=[           # Optional, but recommended for classification
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or the appropriate license
        "Operating System :: OS Independent",      # if your package is
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",  # Specify minimum Python version
    install_requires=[        # List any dependencies your package needs
        "numpy",
        "tensorflow",       # or the deep learning framework you use
    ],
)
