#!/bin/bash

name=$(basename $(pwd))
git archive \
    --format zip \
    --prefix "$name/" \
    -o $name.zip \
    HEAD
