./env/scripts/activate.ps1

if ($args[0] -eq '-dist') {
    python setup.py sdist bdist_wheel
    python -m twine upload --skip-existing dist/*
} else {
    ./docs/make clean
    ./docs/make html
}
