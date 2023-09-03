import setuptools

with open("README.md", "r", encoding="utf-8") as f:  #README as you can publish in pypi as package but here as local package
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "amitabh-srivastava"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "amitabh.student20@gmail.com"
#this will look for init in all folders then install as local package


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)