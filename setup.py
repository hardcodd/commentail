from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="commentail",
    version="0.1.0",
    description="Wagtail comment system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hardcodd/commentail",
    author="Alex Hardcodd",
    # author_email=""
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="wagtail, comments, comment system, django, wagtail comments",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.8,<4",
    install_requires=[
        "Django>=5.1,<5.2",
        "wagtail>=6.4,<6.5",
    ],
    project_urls={
        "Bug Reports": "https:/github.com/hardcodd/commentail/issues",
        # "Funding": "https://boosty.to/hardcodd",
        # "Say Thanks!": "https://saythanks.io/to/hardcodd",
        "Source": "https://github/com/hardcodd/commentail",
    },
)
