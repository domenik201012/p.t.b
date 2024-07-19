from random import randint
import requests
from datetime import datetime,timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.hp = 100
        self.power = 20
        self.last_feed_time = datetime.now()
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code ==200:
          data = response.json()
          return data["sprites"]["other"]["home"]["front_default"]
        else:
            return "фото не доступно"


    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, здоровье: {self.hp}, сила: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            shans = randint(1,5)
            if shans == 1:
                return 'волшебник применил шит'

        if enemy.hp>self.power:
            enemy.hp -= self.power
            return f"сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}"

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  






class Wizard(Pokemon):
    def attack(self, enemy):
        return super().attack(enemy)







class Fighter(Pokemon):
     def attack(self, enemy):
         super_power=randint(5, 15)
         self.power += super_power
         super().attack(enemy)
         self.power -= super_power
         return f'результат: боец применил супер атаку силой: {super_power}'
     



