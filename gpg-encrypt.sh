#!/bin/bash

rm -f sharing.log
rm -f *-input.txt
python3 sharing.py -s -k key.log -m 3 -x 5 > sharing.log

grep "^1-*" sharing.log > robin-input.txt
cat robin-input.txt
grep "^2-*" sharing.log > mia-input.txt
cat mia-input.txt
grep "^3-*" sharing.log > roay-input.txt
cat roay-input.txt
grep "^4-*" sharing.log > jetqe-input.txt
cat jetqe-input.txt
grep "^5-*" sharing.log > thorb-input.txt
cat thorb-input.txt

cat robin-input.txt | gpg --encrypt --armor --recipient robin@exin.one
cat mia-input.txt | gpg --encrypt --armor --recipient mia@exin.one
cat roay-input.txt | gpg --encrypt --armor --recipient roay@exin.one
cat jetqe-input.txt | gpg --encrypt --armor --recipient jetqe@exin.one
cat thorb-input.txt | gpg --encrypt --armor --recipient thorb@exin.one

rm -f sharing.log
rm -f *-input.txt

rm -f key.log
