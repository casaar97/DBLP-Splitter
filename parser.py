#!/usr/bin/python3

from lxml import etree
from lxml.etree import XMLSyntaxError
from time import time
import sys
import os



def clearTagText(child):

    if('&' in str(child.text)):
        child.text = str(child.text).replace("&", "and")

    if('\"' in str(child.text)):
        child.text = str(child.text).replace('\"', "")

    if('<' in str(child.text)):
        child.text = str(child.text).replace('<', "&lt;")

    if('>' in str(child.text)):
        child.text = str(child.text).replace('>', "&gt;")

    if(str(child.tag) == "title"):
        if(str(child.text) == "null"):
            child.text = str(child.text).replace("null", "invalid")
        if(str(child.text) == ""):
            child.text = str(child.text).replace("", "invalid")

    return child


start_time = time()

source = sys.argv[1]
dtd = etree.DTD(file=sys.argv[2])  # read DTD

# Numero de records por fichero xml y autores/editores por tsv

threshold = 100000

records_per_xml = threshold
authors_per_tsv = threshold
editors_per_tsv = threshold

# Contadores para el numero de records y los orcid

count_author_orcid = 0
count_editor_orcid = 0
count_orcid = 0

count_records = 0
count_articles = 0
count_phdthesis = 0
count_inproceedings = 0
count_proceedings = 0
count_book = 0
count_incollection = 0
count_mastersthesis = 0
count_www = 0

# Contadores para los xml y tsv

author_orcid_number = 0
editor_orcid_number = 0

article_number = 0
phdthesis_number = 0
inproceedings_number = 0
proceedings_number = 0
book_number = 0
incollection_number = 0
mastersthesis_number = 0
www_number = 0


# Definicion de los ficheros de los orcid

author_orcid_xml_name = "parser_output/authors_orcid/author_orcid"
editor_orcid_xml_name = "parser_output/editors_orcid/editor_orcid"

author_orcid_xml = open( author_orcid_xml_name + "0.xml", "w")
author_orcid_xml.write("<authors>\n")

editor_orcid_xml = open( editor_orcid_xml_name + "0.xml", "w")
editor_orcid_xml.write("<editors>\n")



#Nombre de los ficheros xml

article_xml_name = "parser_output/articles/article"

book_xml_name = "parser_output/books/book"

phdthesis_xml_name = "parser_output/phdthesis/phdthesis"

inproceedings_xml_name = "parser_output/inproceedings/inproceedings"

proceedings_xml_name = "parser_output/proceedings/proceedings"

incollection_xml_name = "parser_output/incollections/incollection"

mastersthesis_xml_name = "parser_output/mastersthesis/mastersthesis"

# Apertura de los diferentes ficheros correspondientes a cada record

articles_xml = open(article_xml_name + "0.xml", "w")
articles_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
articles_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
articles_xml.write("<dblp>\n")

phdthesis_xml = open(phdthesis_xml_name + "0.xml", "w")
phdthesis_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
phdthesis_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
phdthesis_xml.write("<dblp>\n")

inproceedings_xml = open(inproceedings_xml_name + "0.xml", "w")
inproceedings_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
inproceedings_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
inproceedings_xml.write("<dblp>\n")

proceedings_xml = open(proceedings_xml_name + "0.xml", "w")
proceedings_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
proceedings_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
proceedings_xml.write("<dblp>\n")

book_xml = open(book_xml_name + "0.xml", "w")
book_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
book_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
book_xml.write("<dblp>\n")

incollection_xml = open(incollection_xml_name + "0.xml", "w")
incollection_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
incollection_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
incollection_xml.write("<dblp>\n")

mastersthesis_xml = open(mastersthesis_xml_name + "0.xml", "w")
mastersthesis_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
mastersthesis_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
mastersthesis_xml.write("<dblp>\n")


# iterate through nodes
for event, element in etree.iterparse(source, load_dtd=True):

    """
    ARTICLES
    """

    if(element.tag == "article"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            articles_xml.write("\n<article mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    articles_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            articles_xml.write("</article>\n")

            count_articles += 1
            count_records += 1

            check = int(count_articles/records_per_xml)

            if(article_number < check):

                article_number = check
                articles_xml.write("</dblp>")
                articles_xml.close()
                articles_xml = open(article_xml_name +
                                    str(article_number) + ".xml", "w")
                articles_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                articles_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                articles_xml.write("<dblp>\n")

            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

    """
    PHDTHESIS
    """

    if(element.tag == "phdthesis"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            phdthesis_xml.write("\n<phdthesis mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    phdthesis_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            phdthesis_xml.write("</phdthesis>\n")

            count_phdthesis += 1
            count_records += 1

            check = int(count_phdthesis/records_per_xml)

            if(phdthesis_number < check):

                phdthesis_number = check
                phdthesis_xml.write("</dblp>")
                phdthesis_xml.close()
                phdthesis_xml = open(
                    phdthesis_xml_name + str(phdthesis_number) + ".xml", "w")
                phdthesis_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                phdthesis_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                phdthesis_xml.write("<dblp>\n")

            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

    """
    INPROCEEDINGS
    """

    if(element.tag == "inproceedings"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            inproceedings_xml.write("\n<inproceedings mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    inproceedings_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            inproceedings_xml.write("</inproceedings>\n")

            count_inproceedings += 1
            count_records += 1

            check = int(count_inproceedings/records_per_xml)

            if(inproceedings_number < check):

                inproceedings_number = check
                inproceedings_xml.write("</dblp>")
                inproceedings_xml.close()
                inproceedings_xml = open(
                    inproceedings_xml_name + str(inproceedings_number) + ".xml", "w")
                inproceedings_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                inproceedings_xml.write(
                    "<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                inproceedings_xml.write("<dblp>\n")

            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

    """
    PROCEEDINGS
    """

    if(element.tag == "proceedings"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            proceedings_xml.write("\n<proceedings mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    proceedings_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "editor"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        editor_orcid_xml.write("<editor name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_editor_orcid += 1

            proceedings_xml.write("</proceedings>\n")

            count_proceedings += 1
            count_records += 1

            check = int(count_proceedings/records_per_xml)

            if(proceedings_number < check):

                proceedings_number = check
                proceedings_xml.write("</dblp>")
                proceedings_xml.close()
                proceedings_xml = open(
                proceedings_xml_name + str(proceedings_number) + ".xml", "w")
                proceedings_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                proceedings_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                proceedings_xml.write("<dblp>\n")

            orcid_check = int(count_editor_orcid/editors_per_tsv)
            
            if(editor_orcid_number < orcid_check):
                editor_orcid_number = orcid_check
                print(editor_orcid_number)
                editor_orcid_xml.write("</editors>")
                editor_orcid_xml.close()
                editor_orcid_xml = open(editor_orcid_xml_name + str(editor_orcid_number) + ".xml", "w")
                editor_orcid_xml.write("<editors>\n")

    """
    BOOK
    """

    if(element.tag == "book"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            book_xml.write("\n<book mdate=\"" + element.attrib.get('mdate') +
                           "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    book_xml.write("<" + str(child.tag) + ">" +
                                   str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            book_xml.write("</book>\n")

            count_book += 1
            count_records += 1

            check = int(count_book/records_per_xml)

            if(book_number < check):

                book_number = check
                book_xml.write("</dblp>")
                book_xml.close()
                book_xml = open(book_xml_name + str(book_number) + ".xml", "w")
                book_xml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                book_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                book_xml.write("<dblp>\n")

            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

    """
    INCOLLECTION
    """

    if(element.tag == "incollection"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            incollection_xml.write("\n<incollection mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    incollection_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            incollection_xml.write("</incollection>\n")

            count_incollection += 1
            count_records += 1

            check = int(count_incollection/records_per_xml)

            if(incollection_number < check):

                incollection_number = check
                incollection_xml.write("</dblp>")
                incollection_xml.close()
                incollection_xml = open(
                    incollection_xml_name + str(incollection_number) + ".xml", "w")
                incollection_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                incollection_xml.write("<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                incollection_xml.write("<dblp>\n")

            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

    """
    MASTERSTHESIS
    """

    if(element.tag == "mastersthesis"):
        if str(element.attrib.get('mdate')) != "None" and str(element.attrib.get('key')) != "None":
            mastersthesis_xml.write("\n<mastersthesis mdate=\"" + element.attrib.get(
                'mdate') + "\" key=\"" + element.attrib.get('key') + "\">\n")

            for child in element:

                child = clearTagText(child)

                if(child.text != "\n"):
                    mastersthesis_xml.write(
                        "<" + str(child.tag) + ">" + str(child.text) + "</" + str(child.tag) + ">\n")

                if(child.tag == "author"):
                    if(str(child.attrib.get('orcid')) != "None"):
                        author_orcid_xml.write("<author name=" + "\"" + str(child.text) +"\"" + " orcid=" + "\"" + str(child.attrib.get('orcid')) + "\"" + ">\n")
                        count_orcid += 1
                        count_author_orcid += 1

            mastersthesis_xml.write("</mastersthesis>\n")

            count_mastersthesis += 1
            count_records += 1

            check = int(count_mastersthesis/records_per_xml)

            if(mastersthesis_number < check):

                mastersthesis_number = check
                mastersthesis_xml.write("</dblp>")
                mastersthesis_xml.close()
                mastersthesis_xml = open(
                    mastersthesis_xml_name + str(mastersthesis_number) + ".xml", "w")
                mastersthesis_xml.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                mastersthesis_xml.write(
                    "<!DOCTYPE dblp SYSTEM \"dblp.dtd\">\n")
                mastersthesis_xml.write("<dblp>\n")
            
            orcid_check = int(count_author_orcid/authors_per_tsv)

            if(author_orcid_number < orcid_check):
                author_orcid_number = orcid_check
                author_orcid_xml.write("</authors>")
                author_orcid_xml.close()
                author_orcid_xml = open(author_orcid_xml_name + str(author_orcid_number) + ".xml", "w")
                author_orcid_xml.write("<authors>\n")

element.clear()

#Terminacion de los ficheros correspondientes a authors y editors y cierre de los mismos

author_orcid_xml.write("</authors>")
author_orcid_xml.close()

editor_orcid_xml.write("</editors>")
editor_orcid_xml.close()

# Terminacion de los ficheros correspondientes a cada record
articles_xml.write("</dblp>")
phdthesis_xml.write("</dblp>")
inproceedings_xml.write("</dblp>")
proceedings_xml.write("</dblp>")
book_xml.write("</dblp>")
incollection_xml.write("</dblp>")
mastersthesis_xml.write("</dblp>")

# Cerramos los ficheros correspondientes a cada record
articles_xml.close()
phdthesis_xml.close()
inproceedings_xml.close()
proceedings_xml.close()
book_xml.close()
incollection_xml.close()
mastersthesis_xml.close()
# www_xml.close()

finish_time = time()

minutes = (finish_time - start_time)/60
seconds = (finish_time - start_time) % 60

total_time = str(minutes) + " minutes and " + str(seconds) + " seconds"

print(count_editor_orcid)


print("There have been found " + str(count_records) + " records:\n")
print("\t\t\t" "+" + str(count_articles) + " articles " +
      "({0:.2f})".format((count_articles/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_phdthesis) + " phdthesis " +
      "({0:.2f})".format((count_phdthesis/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_inproceedings) + " inproceedings " +
      "({0:.2f})".format((count_inproceedings/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_proceedings) + " proceedings " +
      "({0:.2f})".format((count_proceedings/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_book) + " books " +
      "({0:.2f})".format((count_book/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_incollection) + " incollections " +
      "({0:.2f})".format((count_incollection/count_records)*100) + "%")
print("\t\t\t" "+" + str(count_mastersthesis) + " mastersthesis " +
      "({0:.2f})".format((count_mastersthesis/count_records)*100) + "%")

print("\n")
print("There have been found " + str(count_orcid) + " orcids")
print("\n")
print("Total time: " + total_time)
