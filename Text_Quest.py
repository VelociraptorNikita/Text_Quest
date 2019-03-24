class GameObject:
    class_name = ''
    desc = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + '\n' + self.desc

    def listen(self, value):
        return


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = 'Гоблин'
        self._desc = 'Отвратительное создание'
        self.health = 3
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'У него рана на колене'
        elif self.health == 1:
            health_line = 'Его левая рука отсечена'
        elif self.health <= 0:
            health_line = 'Он мёртв'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

    def listen(self, value):
        if value == ['пошёл', 'на', 'хуй']:
            return 'Гоблин сказал "сам пошёл на хуй"'
        else:
            return 'А в ответ тишина'


def hit(noun):
    first_noun = noun[0].title()
    if first_noun in GameObject.objects:
        thing = GameObject.objects[first_noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = 'Вы убили гоблина'
            else:
                msg = 'Вы ранили гоблина'
        else:
            msg = 'Здесь нет {}'.format(first_noun)
        return msg


def examine(noun):
    first_noun = noun[0].title()
    if first_noun in GameObject.objects:
        print('хуй')
        return GameObject.objects[first_noun].get_desc()
    else:
        return 'Здесь нет {}'.format(first_noun)


def get_input():
    command = input(': ').split()
    verb_word = command[0].lower()
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print('Неизвестное слово "{}"'.format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1:]
        print(verb(noun_word))
    else:
        print('Что {}?'.format(verb_word))


def say(noun):
    return 'Вы сказали "{}"'.format(' '.join(noun)) + '\n' #+ GameObject.objects.values().listen(noun)


verb_dict = {
    'сказать': say,
    'изучить': examine,
    'атаковать': hit,
}

goblin = Goblin('Гоблин')
goblin.desc = 'Он пьян'
print('Перед вами повляется Гоблин.')
while True:
    get_input()
