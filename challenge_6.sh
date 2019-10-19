#!bin/bash
for x in `ls`; do cat $x | grep -v nothing; done;
grep -nr . -e 'comments'; #46145