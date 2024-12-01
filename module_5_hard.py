from time import sleep

class User:
    def __init__(self, nickname, password, age ):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now =0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return self.videos

    def log_in(self, nickname, password ):
        for i in self.users:
            if nickname in i and password in i:
                self.current_user = nickname

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname :
                print(f'"Пользователь {nickname} уже существует"')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, word):
        list_videos = []
        for i in self.videos:
            if word.upper() in i.title.upper():
                list_videos.append(i.title)
        return list_videos

    def watch_video(self, name_video):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in self.videos:
            if i.title == name_video:
                if self.current_user.age.__lt__(18):
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for j in range(1, i.duration + 1):
                    sleep(1)
                    if j.__eq__(i.duration):
                        print('Конец видео')
                    else:
                        print(j, end=' ')
                i.duration = 0

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


