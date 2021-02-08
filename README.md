# Udacity-DevOps-Azure-Project-2
Udacity-DevOps-Azure-Project-1

badges for this branch
----------------------

![Python application test with Github Actions](https://github.com/jfcb853/Udacity-DevOps-Azure-Project-2/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg?branch=hello-github-actions)

## CI with GitHub Actions

* Enable Github Actions

* Replace yml code

> Replace the python-app.yml code with the following scaffolding code.

```sh
name: Python application test with Github Actions

on: 
  push:
    branches:
      - '*'

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
```

* Verify Remote Tests pass

* save the badge and put on the README.md


