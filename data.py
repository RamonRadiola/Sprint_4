book_names = ['Бегущий по лезвию 2049', 'Чужой', 'Таинственная река', 'Анастасия', 'Евротур', 'Такси', 'Форрест Гамп']
genre_names = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии', 'Комедии', 'Приключения']

book_genre_dict = {}
for i in range(0, len(book_names)):
    book_genre_dict[book_names[i]] = genre_names[i]

