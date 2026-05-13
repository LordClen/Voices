#!/bin/sh
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPT_PATH=$(dirname "$SCRIPT")

PYTHONHOME=/home/clen/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu
export PYTHONHOME
NUITKA_PYTHONPATH="/home/clen/Documentos/PythonProjects/voices:/home/clen/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12:/home/clen/.local/share/uv/python/cpython-3.12-linux-x86_64-gnu/lib/python3.12/lib-dynload:/home/clen/Documentos/PythonProjects/voices/.venv/lib/python3.12/site-packages"
export NUITKA_PYTHONPATH
PYTHONPATH="/home/clen/Documentos/PythonProjects/voices:/home/clen/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12:/home/clen/.local/share/uv/python/cpython-3.12-linux-x86_64-gnu/lib/python3.12/lib-dynload:/home/clen/Documentos/PythonProjects/voices/.venv/lib/python3.12/site-packages"
export PYTHONPATH

"$SCRIPT_PATH/voices.bin" $@

