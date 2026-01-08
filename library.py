def library_details(bookid, book_title, author_name, year_of_publication):
    return (
        f"Book_id : {bookid}\n"
        f"Book_title : {book_title}\n"
        f"Author_name : {author_name}\n"
        f"Year_of_publication : {year_of_publication}\n"
    )

if __name__ == "__main__":
    bookid = 1001
    book_title = "Wings of Fire"
    author_name = "Dr. Abdul Kalam"
    year_of_publication = "19/02/2014"

    print(library_details(bookid, book_title, author_name, year_of_publication))
