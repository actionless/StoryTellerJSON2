#!/bin/sh
set -ue
test -d gh-pages || git clone git@github.com:actionless/StoryTellerJSON2.git -b gh-pages gh-pages
cd gh-pages
rm -r *
cp -pr ../gh-pages-index.html ./index.html
cp -pr ../output ../docs ./
