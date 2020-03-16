#!/bin/bash


if [ $# -ne 2 ];
  then
    echo "You need to run the script in that way: ./parser.sh dblp.xml dblp.dtd"
    exit 0
  else
    echo ""
    if [ -d $i ];
      then
        rm -rf "parser_output"
        mkdir "parser_output"
      else
        mkdir "parser_output"
    fi

    ## declare an array variable

    declare -a arr=("articles" "books" "proceedings" "inproceedings" "phdthesis" "mastersthesis" "incollections" "authors_orcid" "editors_orcid")

    ## now loop through the above array
    for i in "${arr[@]}"
    do
        
        mkdir "parser_output/$i"
        cp "parser_input/dblp.dtd" "parser_output/$i"
        echo "parser_output/$i directory has been created"
        echo ""
      
    done

    python3 parser.py parser_input/$1 parser_input/$2

fi
