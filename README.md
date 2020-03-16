# DBLP-Splitter

REQUIREMENTS

- Python3
- lxml (Python3) -> https://lxml.de/installation.html

GUIDE

- Use chmod u+x parser.sh (only first time you use it) to grant permissions in order to execute it
- Download DBLP files from: https://dblp.uni-trier.de/xml/ (The .gz and .dtd files)
- Unzip the .gz file and you will get dblp.xml
- Run ./parser.sh dblp.xml dblp.dtd
- You will find a new directory called parser_output where all the new files will be generated

EXAMPLE

In case you place the dblp.xml and dblp.dtd file in the same directory that parser.sh:

- ./parser.sh dblp.xml dblp.dtd

In case you place the files into another directory just run the following:

- ./parser.sh path_to_dblp.xml path_to_dblp.dtd
