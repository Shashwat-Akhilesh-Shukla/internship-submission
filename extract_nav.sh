#!/bin/bash

curl -s "https://www.amfiindia.com/spages/NAVAll.txt" | \
awk -F ';' '
    BEGIN { OFS="\t" }
    NF == 6 && $1 ~ /^[0-9]+$/ {
        print $4, $5
    }
' > scheme_nav.tsv
