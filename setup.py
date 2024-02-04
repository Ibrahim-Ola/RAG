
from setuptools import setup, find_packages

PROJNAME = "rag-with-langchain"
DESCRIPTION = "An introduction to Retrieval Augmented Generation (RAG) using LangChain."
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
MAINTAINER = "Ibrahim Olalekan Alabi"
MAINTAINER_EMAIL = "ibrahimolalekana@u.boisestate.edu"
URL = "https://github.com/Ibrahim-Ola/RAG.git"
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/Ibrahim-Ola/RAG/issues",
    "Documentation": "https://github.com/Ibrahim-Ola/RAG/blob/main/README.md",
    "Source Code": "https://github.com/Ibrahim-Ola/RAG",
}
VERSION = "0.0.1"
LICENSE = "MIT"
PYTHON_REQUIRES = ">=3.9"

def setup_package():
    metadata = dict(
        name=PROJNAME,
        version=VERSION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        url=URL,
        project_urls=PROJECT_URLS,
        license=LICENSE,
        python_requires=PYTHON_REQUIRES,
        packages=find_packages(),
        install_requires=[
            "torch==2.1.2",
            "langchain==0.1.1",
            "chromadb==0.4.22",
            "accelerate==0.26.1",
            "transformers==4.36.2",
            "python-dotenv==1.0.0",
            "bitsandbytes==0.42.0",
            "sentence-transformers==2.3.1"
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            # "Environment :: GPU :: NVIDIA CUDA",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Education",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        keywords=[
            "RAG",
            "LLM",
            "LangChain",
            "NLP",
            "Deep Learning",
            "AI",
            "Machine Learning",
            "Artificial Intelligence",
        ],
    )

    setup(**metadata)

if __name__ == "__main__":
    setup_package()
    print("Setup Complete.")