from setuptools import setup, find_packages

setup(
    name="dnd-firefly",
    version="0.4.0",
    packages=find_packages(),
    keywords = [firefly,visualization, astronomy,images, fits, parquet, votable, csv, tsv],
    author="Emmanuel Joliet",
    author_email="ejoliet@caltech.edu",
    description="Programmatically drag-and-drop in IRSA Viewer (Firefly) tool via Upload feature",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ejoliet/dnd-firefly.git",
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',        
        'Source': 'https://github.com/ejoliet/dnd-firefly.git',
        'Tracker': 'https://github.com/ejoliet/dnd-firefly/issues',
        'Say Thanks!': 'https://buymeacoffee.com/Red2Green',
    },
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  # Minimum Python version
    entry_points={
        "console_scripts": [
            "dnd_firefly=app.dnd_firefly:main",
        ],
    },
)
