#!/bin/bash -i
source $HOME/.bashrc

rm -rf public
mkdir public
cp -R static/* public

python src/main.py
cd public && python3 -m http.server 8888
