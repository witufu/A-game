import random
import sys
print("Давным давно все расы были вместе, но наступули темные времена...\n Ты один из исторически рожденных героев, которые должны победить зло.")
print("Добро пожаловать в мой 'Бар', дружище! Для начала игры тебе нужно выбрать класс:\n Но помни, они уникальны, твой выбор нельзя изменить, у каждого класса свое оружие.")
print("1. Воин\n2. Стрелок\n3. Маг")
chs = int(input("Выберите класс: "))
if chs == 1:
    print("Ваш класс - Воин")
elif chs == 2:
    print("Ваш класс - Стрелок")
elif chs == 3:
    print("Ваш класс - Маг")
else:
    print("Некорректный выбор класса.")
    sys.exit()


class Weapon:
    def __init__(self, name, damage, special_damage, mana_cost):
        self.name = name
        self.damage = damage
        self.special_damage = special_damage
        self.mana_cost = mana_cost


class Game:
    def __init__(self):
        if chs == 1:
            self.weapons = [
                Weapon("Медный меч", damage=random.randint(20, 65), special_damage=random.randint(30, 85), mana_cost=15),
                Weapon("Экскалибур", damage=random.randint(100, 200), special_damage=random.randint(300, 600), mana_cost=50),
                Weapon("Ледяной меч", damage=random.randint(50, 90), special_damage=random.randint(100, 250), mana_cost=17),
                Weapon("Мурамаса", damage=random.randint(100, 150), special_damage=random.randint(100, 400), mana_cost=16),
                Weapon("Грань ночи", damage=random.randint(120, 150), special_damage=random.randint(108, 125), mana_cost=23)
            ]
        elif chs == 2:
            self.weapons = [
                Weapon("Ледяной лук", damage=random.randint(68, 116), special_damage=random.randint(45, 120), mana_cost=75),
                Weapon("Пчелиный улей", damage=random.randint(69, 110), special_damage=random.randint(70, 110), mana_cost=90),
                Weapon("Деревянный лук", damage=random.randint(50, 123), special_damage=random.randint(70, 120), mana_cost=40),
                Weapon("Адский лук", damage=random.randint(80, 130), special_damage=random.randint(66, 130), mana_cost=70),
                Weapon("Лук демона", damage=random.randint(78, 140), special_damage=random.randint(70, 140), mana_cost=92)
            ]
        elif chs == 3:
            self.weapons = [
                Weapon("Книга Черепа", damage=random.randint(68, 120), special_damage=random.randint(73, 110), mana_cost=90),
                Weapon("Книга Воды", damage=random.randint(54, 130), special_damage=random.randint(70, 144), mana_cost=70),
                Weapon("Книга пламени", damage=random.randint(66, 127), special_damage=random.randint(88, 150),  mana_cost=100),
                Weapon("Демоническая книга", damage=random.randint(52, 126), special_damage=random.randint(80, 152), mana_cost=85),
                Weapon("Книга Кристалов", damage=random.randint(56, 101), special_damage=random.randint(66, 124), mana_cost=80),
            ]

        if chs == 1:
            self.player = Player("Воин", health=1000, mana=150)
        elif chs == 2:
            self.player = Player("Стрелок", health=600, mana=250)
        elif chs == 3:
            self.player = Player("Маг", health=450, mana=500)

        self.enemies = [
            Enemy("Гоблин", health=1500, mana=200, damage=random.randint(1, 25), special_damage=80, mana_cost=50),
            Enemy("Глава Людоедов(Пудж)", health=5000, mana=200, damage=random.randint(20, 65), special_damage=100, mana_cost=120)
        ]

    def run(self):
        print("Добро пожаловать на хакатон по программированию на Python!")
        self.player.choose_weapon(self.weapons)
        battle_count = 0
        for enemy in self.enemies:
            battle = Battle(self.player, enemy)
            battle.start()
            battle_count += 1
            if battle_count < len(self.enemies):
                print("\nМежду сражениями вы находите возможность восстановиться.")
                self.player.restore(health=300, mana=200)
                print(
                    f"Ваше состояние: Жизни {self.player.health}/{self.player.max_health}, Мана {self.player.mana}/{self.player.max_mana}")
        print("\nПоздравляем! Вы победили всех противников!")


class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.max_health = health
        self.health = health
        self.mana = mana
        self.max_mana = mana
        self.mana = mana

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} получает {amount} урона. Остаток жизней: {self.health}/{self.max_health}")

    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        else:
            print(f"У {self.name} недостаточно маны!")
            return False

    def restore(self, health=0, mana=0):
        self.health = min(self.health + health, self.max_health)
        self.mana = min(self.mana + mana, self.max_mana)


class Player(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)
        self.max_health = health

    def choose_weapon(self, weapons):
        print("Выберите оружие:")
        for idx, weapon in enumerate(weapons, start=1):
            print(
                f"{idx}. {weapon.name} (Базовый урон: {weapon.damage}, Спец. атака: {weapon.special_damage} (манакост: {weapon.mana_cost}))")
        while True:
            choice = input("Введите номер оружия: ")
            if choice.isdigit() and 1 <= int(choice) <= len(weapons):
                self.weapon = weapons[int(choice) - 1]
                print(f"Вы выбрали {self.weapon.name}!")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

    def attack(self, target):
        print(f"{self.name} атакует {target.name} обычной атакой оружием {self.weapon.name}.")
        target.take_damage(self.weapon.damage)

    def special_attack(self, target):
        if self.use_mana(self.weapon.mana_cost):
            print(f"{self.name} использует специальную атаку оружием {self.weapon.name}!")
            target.take_damage(self.weapon.special_damage)
        else:
            print("Специальная атака не выполнена из-за недостатка маны.")

    def heal(self):
        heal_amount = 150
        mana_amount = 50
        self.restore(mana= mana_amount)
        self.restore(health=heal_amount)
        print(f"{self.name} использует хил и восстанавливает {heal_amount} HP!","также получает 150 MN!")


class Enemy(Character):
    def __init__(self, name, health, mana, damage, special_damage, mana_cost):
        super().__init__(name, health, mana)
        self.damage = damage
        self.special_damage = special_damage
        self.mana_cost = mana_cost

    def attack(self, target):
        if self.mana >= self.mana_cost and random.choice([True, False]):
            self.use_mana(self.mana_cost)
            print(f"{self.name} применяет специальную атаку!")
            target.take_damage(self.special_damage)
        else:
            print(f"{self.name} атакует обычной атакой!")
            target.take_damage(self.damage)


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"\nНачинается сражение: {self.player.name} против {self.enemy.name}!")
        turn = 0
        while self.player.is_alive() and self.enemy.is_alive():
            print("\n--------------------")
            print(f"Ход {turn + 1}")
            self.player_turn()
            if not self.enemy.is_alive():
                print(f"{self.enemy.name} побежден!")
                if self.enemy.name == "Гоблин":
                    print(f"Поздравляю, ты получил ачивку:\n Глава Гоблинов")
                elif self.enemy.name == "Глава Людоедов(Пудж)":
                    print(f"Поздравляю, ты получил ачивку:\n Глава Людоедов, ТЫ СИЛЬНЕЙШИЙ!!!")
                break
            self.enemy_turn()
            if not self.player.is_alive():
                print("Вы проиграли!")
                sys.exit()
            turn += 1

    def player_turn(self):
        print(
            f"\nВаш ход. {self.player.name}: Жизни {self.player.health}/{self.player.max_health}, Мана {self.player.mana}/{self.player.max_mana}")
        print("Доступные действия:")
        print("1. Обычная атака")
        print("2. Специальная атака")
        print("3. Хилка")
        while True:
            choice = input("Введите номер действия: ")
            if choice == "1":
                self.player.attack(self.enemy)
                break
            elif choice == "2":
                self.player.special_attack(self.enemy)
                break
            elif choice == "3":
                self.player.heal()  # Call the heal method
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def enemy_turn(self):
        print(f"\nХод противника: {self.enemy.name}")
        self.enemy.attack(self.player)

if __name__ == "__main__":
    game = Game()
    game.run()