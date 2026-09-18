name: Build APK

on:
  push:
    branches: [ master, main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Buildozer and Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y libtool pkg-config autoconf automake libffi-dev ccache gettext
        pip install --upgrade pip
        pip install buildozer cython==0.29.36 virtualenv

    - name: Build Android APK with Buildozer
      uses: ActionKit/buildozer-action@v1
      with:
        buildozer_version: 'stable'
        command: 'buildozer -v android debug'
        repository_path: '.'

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk
