# TODO Найдите количество книг, которое можно разместить на дискете



size_in_bytes = 1.44 * 1024 * 1024
size_of_book = 4 * 25 * 50 * 100
count_of_books = size_in_bytes // size_of_book

print("Количество книг, помещающихся на дискету:", count_of_books)
