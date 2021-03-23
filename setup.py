import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

GITHUB_URL = "https://github.com/plasmatic1/sampleproject"

setuptools.setup(
    name="solution-downloader", # Replace with your own username
    version="0.0.1",
    author="plasmatic1",
    author_email="moses@mosesxu.net",
    description="Downloader for competitive programming solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    project_urls={
        "Bug Tracker": GITHUB_URL + '/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
