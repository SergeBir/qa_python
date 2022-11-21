from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #проверяем в методе __init__, что books_rating имеет тип dict
    def test_type_of_books_rating_dict_true(self):
        collector = BooksCollector()
        assert type(collector.books_rating) == dict

    # проверяем в методе __init__, что favorites имеет тип list
    def test_type_of_favorites_list_true(self):
        collector = BooksCollector()
        assert type(collector.favorites) == list

    #проверяем, что одну книгу нельзя добавить дважды
    def test_check_book_cannot_be_twice_true(self):
        collector = BooksCollector()

        # пробуем добавить одну книгу дважды
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавилась именно одна
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1

    # проверяем, что нельзя выставить рейтинг книге, которой нет в списке
    def test_check_books_outside_list_have_not_rating_true(self):
        collector = BooksCollector()
        assert collector.set_book_rating('1984', 5) == None

    # проверяем, что нельзя выставить рейтинг книге меньше 1
    def test_check_rating_cannot_be_less_than_one_true(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # устанавливаем рейтинг меньше 1
        collector.set_book_rating('Гордость и предубеждение и зомби', -1)
        # проверяем, что рейтинг не может быть меньше 1
        assert collector.books_rating['Гордость и предубеждение и зомби'] > 0

    # проверяем, что нельзя выставить рейтинг книге больше 10
    def test_check_rating_cannot_be_more_than_ten_true(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # устанавливаем рейтинг больше 10
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        # проверяем, что рейтинг не может быть больще 10
        assert collector.books_rating['Гордость и предубеждение и зомби'] <= 10

    # проверяем, что у не добавленной книги нет рейтинга.
    def test_check_not_added_book_has_not_rating_true(self):
        collector = BooksCollector()
        try:
            assert collector.books_rating['Книга не добавлена'] == KeyError
        except:
            print("Ошибка! Хоть книга и не добавлена, у нее есть рейтинг")

    # проверка добавления книги в избранное
    def test_check_add_book_to_favorites_true(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Новая книга')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Новая книга')
        assert 'Новая книга' in collector.favorites

    #Проверка, что нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_check_cannot_add_book_to_favorites_outside_dict_true(self):
        collector = BooksCollector()
        # добавляем книгу в избранное сразу
        collector.add_book_in_favorites('Книга')
        assert len(collector.favorites) == 0

    # Проверка удаления книги из избранного.
    def test_check_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Новейшая книга')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Новейшая книга')
        # Удаляем книгу из избранного
        collector.delete_book_from_favorites('Новейшая книга')
        assert len(collector.favorites) == 0

