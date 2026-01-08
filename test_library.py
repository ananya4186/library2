from library_repo.library import library_details

def test_library_details_output():
    expected = (
        "Book_id : 1001\n"
        "Book_title : Wings of Fire\n"
        "Author_name : Dr. Abdul Kalam\n"
        "Year_of_publication : 19/02/2014\n"
    )

    result = library_details(
        1001,
        "Wings of Fire",
        "Dr. Abdul Kalam",
        "19/02/2014"
    )

    assert result == expected
