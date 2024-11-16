# Drag-n-Drop files to Firefly programmatically

## Reqs

Make an environment, install deps or update existing `requirements.txt` file:

```bash
pip install -r requirements.txt 
```

## Build the Package:
Run the following command to build the package, update version in `setup.py` before published to pypi.

```bash
python -m build
```
## Install the Package:

Install the package on macOS or Windows.
```bash
pip install dist/dnd_firefly-0.4.0-py3-none-any.whl
```

## Run

Example:

```bash
python dnd_firefly.py ~/Downloads/WISE-allwise_p3as_psd-Cone_100asec.tbl
```