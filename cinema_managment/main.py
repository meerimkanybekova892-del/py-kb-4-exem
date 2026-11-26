from moves import add_movie, show_movies, delete_movie


movies = []
halls = []
sessions = []
bookings = []


def main():
    while True:
        print("\n===== CINEMA MANAGEMENT =====")
        print("1. Добавить фильм")
        print("2. Показать фильмы")
        print("3. Удалить фильм")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            show_movies(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "0":
            print("Программа завершена!")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()
