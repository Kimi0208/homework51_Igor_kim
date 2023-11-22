from random import randint


class CatDB:
    name = None
    age = 1
    hunger_level = 40
    mood_level = 40
    is_sleeping = False
    cat_photo = '/static/img/cat.jpg'

    @classmethod
    def to_dict(cls):
        return {'name': cls.name, 'age': cls.age, 'hunger_level': cls.check_characteristic(cls.hunger_level),
                'mood_level': cls.check_characteristic(cls.mood_level), 'cat_photo': cls.cat_photo}

    @classmethod
    def choose_action(cls, action):
        if action == 'play':
            cls.play_cat()
        elif action == 'sleep':
            cls.sleep()
        elif action == 'feed':
            cls.feed_cat()

    @classmethod
    def feed_cat(cls):
        print(cls.hunger_level)
        if not cls.is_sleeping:
            if cls.hunger_level <= 100:
                cls.hunger_level += 15
                cls.mood_level += 5
            elif cls.hunger_level > 100:
                cls.mood_level -= 30

    @classmethod
    def play_cat(cls):
        angry = randint(1, 3)
        if not cls.is_sleeping:
            if angry != 1:
                cls.mood_level += 15
                cls.hunger_level -= 10
            else:
                cls.mood_level = 0
        elif cls.is_sleeping:
            if angry != 1:
                cls.is_sleeping = False
                cls.mood_level -= 5
            else:
                cls.mood_level = 0

    @classmethod
    def sleep(cls):
        cls.is_sleeping = True

    @classmethod
    def check_characteristic(cls, characteristic):
        if characteristic > 100:
            return 100
        elif characteristic < 0:
            return 0
        else:
            return characteristic
