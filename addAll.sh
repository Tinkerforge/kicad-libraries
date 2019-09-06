#!/bin/sh
cd scripts
git add *.emp
cd ..
git add *.mod
git add *.lib
git add *.mdc
git add *.kicad_mod
find . -name "*.wrl" -exec git add {} \;
find . -name "*.step" -exec git add {} \;
find . -name "*.FCStd" -exec git add {} \;
