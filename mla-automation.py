import datetime

type_of_article = input("What type of article is this ( Electronic ): ")
author = input("What is the author's name: ")
title = input("What is the paper's title: ")
source = input("Where was the article sourced from ( Like New York Times, etc ): ")
datePublished = input("When was the paper published ( MM/DD/YY ): ")
articleURL = input("Url for article: ")

if type_of_article == "Electronic":
    #Working on formatting article inputs
    split_author1 = author.split(" ")
    split_author1.insert(1, ', ')
    split_author = ''.join(split_author1)
    formatted_title = "\"{}\".".format(title)
    formatted_date = datePublished.split("/")
    converted_date = datetime.datetime(int(formatted_date[2]), int(formatted_date[0]), int(formatted_date[1]))
    month = converted_date.strftime("%B")
    day = converted_date.strftime("%m")
    year = converted_date.strftime("%Y")
    fullformat = "{}. {} {}, {} {} {}, {}. Accessed [ insert date ]".format(split_author, formatted_title,source, day, month, year, articleURL )
    print(fullformat)

