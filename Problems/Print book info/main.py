def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author != None and year != None:
        print('"' + title + '" was written by ' + author + " in " + year)
    elif author != None:
        print('"' + title + '" was written by ' + author)
    elif year != None:
        print('"' + title + '" was written in ' + year)
    else:
        print('"' + title + '"')
    pass
