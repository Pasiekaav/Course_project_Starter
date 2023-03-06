"""
Створіть разважальний чат-бот на Python. Даний бот може рекомендувати фільми, музику, ігри за жанрами, анекдоти, цікаві

історії, а також надати можливість пограти в гру. За бажанням можете додати додаткові можливості.

Вимоги:

1. Вихідний код має бути розміщений на github або іншому подібному сервісі.

2. Створіть архітектуру застосунку використовуючи функції.

3. У чат-боті обов'язково має бути передбачене меню.

4. Декомпозиція та композиція.

5. Використання додаткових модулів/бібліотек(pyjokes, art, emoji, prettytable, tqdm, fabulous, colorama, termcolor).

6. Додайте зв'язок викликів функцій між собою.

7. Реалізуйте 1 або декілька ігор(«Камінь-ножиці-папір», «Поле-чудес», «Вгадай число», тощо).

8. Протестуйте чат-бот на працездатність.

9. Наприкінці надайте можливість тестування колегам.

10. Кожний колега, маючи доступ до вашого репозиторію, який розташований на віддаленому сервері, повинен клонувати

ваш проект на свій ПК, додати хоча б 1 додаткову функцію, протестувати(ОБОВ’ЯЗКОВО!) код на працездатність та

надіслати зміни назад.
"""
import time
import emoji
import pyjokes
from prettytable import PrettyTable
from tqdm import tqdm
from termcolor import colored
from art import text2art
import random
import os


def recommend_movies(genre):
    table = PrettyTable()
    table.field_names = ["Title", "Year", "Rating"]
    if genre == "1":
        table.add_row(["Borat Subsequent Moviefilm", 2020, 7.0])
        table.add_row(["The Big Sick", 2017, 7.5])
        table.add_row(["The Nice Guys", 2016, 7.4])
        table.add_row(["Deadpool", 2016, 8.0])
        table.add_row(["The Grand Budapest Hotel", 2014, 8.1])
        table.add_row(["The Hangover", 2009, 7.7])
    elif genre == "2":
        table.add_row(["Moonlight", 2016, 7.4])
        table.add_row(["La La Land", 2016, 8.0])
        table.add_row(["Manchester by the Sea", 2016, 7.8])
        table.add_row(["The Dark Knight", 2008, 9.0])
        table.add_row(["The Shawshank Redemption", 1994, 9.3])
        table.add_row(["The Godfather", 1972, 9.2])
    elif genre == "3":
        table.add_row(["Mission: Impossible - Fallout", 2018, 7.7])
        table.add_row(["John Wick: Chapter 2", 2017, 7.5])
        table.add_row(["Deadpool", 2016, 8.0])
        table.add_row(["Mad Max: Fury Road", 2015, 8.1])
        table.add_row(["John Wick", 2014, 7.4])
        table.add_row(["The Matrix", 1999, 8.7])
    else:
        return f'Invalid choice'
    for _ in tqdm(range(100), mininterval=0.01, unit='Mb', desc="Loading: "):
        time.sleep(0.01)
    print(table)


def recommend_music(genre):
    table = PrettyTable()
    table.field_names = ["Artist", "Album", "Year", "Genre"]
    if genre == "1":
        table.add_row(["Foo Fighters", "Medicine at Midnight", 2021, "Rock"])
        table.add_row(["The War on Drugs", "A Deeper Understanding", 2017, "Rock"])
        table.add_row(["Muse", "Simulation Theory", 2018, "Rock"])
        table.add_row(["Tame Impala", "Currents", 2015, "Rock"])
        table.add_row(["Queens of the Stone Age", "Villains", 2017, "Rock"])
    elif genre == "2":
        table.add_row(["Taylor Swift", "Folklore", 2020, "Pop"])
        table.add_row(["Harry Styles", "Fine Line", 2019, "Pop"])
        table.add_row(["Ariana Grande", "Thank U, Next", 2019, "Pop"])
        table.add_row(["Dua Lipa", "Dua Lipa", 2017, "Pop"])
        table.add_row(["The Weeknd", "After Hours", 2020, "Pop"])
    elif genre == "3":
        table.add_row(["Kanye West", "The Life of Pablo", 2016, "Hip Hop"])
        table.add_row(["J. Cole", "4 Your Eyez Only", 2016, "Hip Hop"])
        table.add_row(["Tyler, The Creator", "Igor", 2019, "Hip Hop"])
        table.add_row(["Kendrick Lamar", "To Pimp a Butterfly", 2015, "Hip Hop"])
        table.add_row(["Travis Scott", "Astroworld", 2018, "Hip Hop"])
    elif genre == "4":
        table.add_row(["Daft Punk", "Random Access Memories", 2013, "Electronic"])
        table.add_row(["Justice", "Woman Worldwide", 2018, "Electronic"])
        table.add_row(["Disclosure", "Settle", 2013, "Electronic"])
        table.add_row(["The Chemical Brothers", "No Geography", 2019, "Electronic"])
        table.add_row(["Rufus Du Sol", "Bloom", 2016, "Electronic"])
    elif genre == "5":
        table.add_row(["Ghost", "Prequelle", 2018, "Metal"])
        table.add_row(["Mastodon", "Emperor of Sand", 2017, "Metal"])
        table.add_row(["Opeth", "Sorceress", 2016, "Metal"])
        table.add_row(["Gojira", "Magma", 2016, "Metal"])
        table.add_row(["Deafheaven", "New Bermuda", 2015, "Metal"])
    else:
        return f'Invalid choice'
    for _ in tqdm(range(100), mininterval=0.01, unit='Mb', desc="Loading: "):
        time.sleep(0.01)
    print(f"Here are some recommended {genre} albums:\n{table}\n")


def recommend_games(genre):
    table = PrettyTable()
    table.field_names = ["Name", "Year", "Rating"]
    if genre == "1":
        table.add_row(["Grand Theft Auto V", 2015, 9.0])
        table.add_row(["Red Dead Redemption 2", 2018, 9.5])
        table.add_row(["Horizon Zero Dawn", 2017, 8.7])
        table.add_row(["DOOM Eternal", 2020, 8.8])
        table.add_row(["God of War", 2018, 9.3])
    elif genre == "2":
        table.add_row(["The Legend of Zelda: Breath of the Wild", 2017, 9.5])
        table.add_row(["Uncharted 4: A Thief\'s End", 2016, 9.0])
        table.add_row(["Assassin\'s Creed Odyssey", 2018, 8.9])
        table.add_row(["The Witcher 3: Wild Hunt", 2015, 9.5])
        table.add_row(["Shadow of the Colossus", 2018, 9.2])
    elif genre == "3":
        table.add_row(["Dark Souls III", 2016, 9.1])
        table.add_row(["Bloodborne", 2015, 9.0])
        table.add_row(["Divinity: Original Sin II", 2017, 9.3])
        table.add_row(["Fallout 4", 2015, 8.8])
        table.add_row(["Mass Effect: Andromeda", 2017, 7.7])
    elif genre == "4":
        table.add_row(["Sid Meier\'s Civilization VI", 2016, 9.0])
        table.add_row(["Starcraft II", 2015, 8.8])
        table.add_row(["Total War: Warhammer II", 2017, 8.9])
        table.add_row(["Age of Empires II: Definitive Edition", 2019, 8.7])
        table.add_row(["XCOM 2", 2016, 9.2])
    elif genre == "5":
        table.add_row(["The Sims 4", 2014, 7.5])
        table.add_row(["Cities: Skylines", 2015, 9.0])
        table.add_row(["Planet Coaster", 2016, 8.3])
        table.add_row(["Euro Truck Simulator 2", 2012, 8.6])
        table.add_row(["Farming Simulator 19", 2018, 7.4])
    else:
        return f'Invalid choice'
    for _ in tqdm(range(100), mininterval=0.01, unit='Mb', desc="Loading: "):
        time.sleep(0.01)
    print(f"Here are some recommended {genre} games:\n{table}\n")


def tell_joke():
    jokes = pyjokes.get_jokes()
    print(random.choice(jokes))


def play_games():
    def play_rps():
        options = ['rock', 'paper', 'scissors']
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)

        print(f"\nYou chose {player_choice}, and the computer chose {computer_choice}.\n")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == 'rock' and computer_choice == 'scissors':
            print("You win!")
        elif player_choice == 'paper' and computer_choice == 'rock':
            print("You win!")
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print("You win!")
        else:
            print("You lose!")

    def play_hangman():
        words = ['python', 'computer', 'programming', 'algorithm', 'variable']
        word = random.choice(words).lower()
        word_letters = set(word)
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        used_letters = set()
        lives = 6

        while len(word_letters) > 0 and lives > 0:
            print(' '.join([letter if letter in used_letters else '-' for letter in word]))
            print(f"Lives left: {lives}")

            user_letter = input("Guess a letter: ").lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives -= 1
                    print("Letter is not in word.")
            elif user_letter in used_letters:
                print("You have already guessed that letter. Please try again.")
            else:
                print("Invalid character. Please try again.")

        if lives == 0:
            print(f"Sorry, you died. The word was {word}.")
        else:
            print(f"Congratulations! You guessed the word {word}!")

    def play_gtn():
        number = random.randint(1, 100)
        attempts = 0

        while True:
            while True:
                guess = input("Guess a number between 1 and 100: ")
                if guess.isnumeric():
                    guess = int(guess)
                    break
                print('Input only Integer!')
            attempts += 1
            if guess == number:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts!")
                break
            elif guess < number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        print("Thanks for playing!")

    games = ["Rock, Paper, Scissors", "Hangman", "Guess the Number"]
    print("Let's play a game! Here's a list of games to choose from:")
    for i, game in enumerate(games):
        print(f"{i+1}. {game}")
    choice = input("Enter the number of the game you want to play: ")
    if choice == "1":
        while True:
            play_rps()
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != 'y':
                break
    elif choice == "2":
        while True:
            play_hangman()
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != 'y':
                break
        print("Thanks for playing!")
    elif choice == "3":
        while True:
            play_gtn()
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != 'y':
                break
        print("Thanks for playing!")
    else:
        print("Invalid choice")


def tell_story():
    story = ["In World War II, a young American soldier named Desmond Doss refused to carry a weapon into battle \n"
             "because of his religious beliefs. Despite being ridiculed by his fellow soldiers, he proved his \n"
             "bravery by saving the lives of dozens of wounded soldiers, all while unarmed.",
             "In the early days of personal computing, Apple co-founder Steve Wozniak built a device called the \n"
             "'Blue Box' that could hack into the phone system and make free long-distance calls. He and his friend \n"
             "Steve Jobs sold the Blue Boxes for hundreds of dollars, which helped fund the development of the first \n"
             "Apple computer.",
             "In the 1980s, a hacker named Kevin Mitnick gained notoriety for breaking into computer systems at \n"
             "companies like IBM and Motorola. He was eventually caught and sentenced to several years in prison, \n"
             "but his exploits helped expose weaknesses in computer security that are still being addressed toda",
             "In 2016, Google's DeepMind developed a machine learning algorithm called AlphaGo that was able to beat \n"
             "the world champion at the game of Go, a complex board game with more possible positions than there are \n"
             "atoms in the universe. AlphaGo's success showed the potential for AI to tackle difficult problems that \n"
             "were once thought to be the exclusive domain of human intelligence.",
             "In 2020, a group of researchers used AI to analyze satellite images of the Amazon rainforest and \n"
             "identify areas that were at risk of deforestation. The system was able to predict areas that were \n"
             "likely to be cleared for agriculture or mining, allowing conservationists to take action to protect \n"
             "these vital ecosystems.",
             "In 2018, an AI system developed by OpenAI called GPT-2 was able to generate realistic-looking news \n"
             "articles, essays, and even poetry. The system was so good that OpenAI initially decided not to release \n"
             "it to the public for fear that it could be used to spread fake news or propaganda."]
    print(random.choice(story))


def display_menu():
    while True:
        os.system('cls')
        print(colored(text2art("Chat  Bot!"), "green"))
        print(emoji.emojize(":robot: Hi there! I'm a chatbot and I can help you with the following:\n"))
        print(emoji.emojize("1. :movie_camera: Recommend Movies\n2. :musical_note: Recommend Music\n"
                            "3. :video_game: Recommend a Game\n4. :joystick: Play a Game\n"
                            "5. :upside-down_face: Tell me a Joke\n6. :books: Share an Interesting Story\n"
                            "7. :stop_button: Exit"))
        choice = input(emoji.emojize("Input Your choise::backhand_index_pointing_right: "))
        match choice:
            case '1':
                os.system('cls')
                while True:
                    print("List of available movies genres:\n1. Action\n2. Comedy\n3. Drama")
                    film_list = ['1', '2', '3']
                    choice1 = input('What genre of movies do you like?(1..3): ')
                    if choice1 in film_list:
                        recommend_movies(choice)
                        if input("Do you want to choose another genre of movies?(y/n): ").lower() == "n":
                            break
                    else:
                        print('Invalid choice')

            case '2':
                os.system('cls')
                while True:
                    print("List of available genres:\n1. Rock\n2. Pop\n3. Hip hop\n4. Electronic\n5. Metal")
                    music_list = ['1', '2', '3', '4', '5']
                    choice2 = input('What genre of music do you prefer?(1..5): ')
                    if choice2 in music_list:
                        recommend_music(choice2)
                        if input("Do you want to choose another genre?(y/n): ").lower() == "n":
                            break
                    else:
                        print('Invalid choice')
            case '3':
                os.system('cls')
                while True:
                    print("List of available genres of games:\n1. Action\n2. Adventure\n3. RPG"
                          "\n4. Strategy\n5. Simulation")
                    game_list = ['1', '2', '3', '4', '5']
                    choice3 = input('What genre of games do you prefer?(1..5): ')
                    if choice3 in game_list:
                        recommend_games(choice3)
                        if input("Do you want to choose another genre of game?(y/n): ").lower() == "n":
                            break
                    else:
                        print('Invalid choice')
            case '4':
                os.system('cls')
                play_games()
            case '5':
                os.system('cls')
                while True:
                    print()
                    tell_joke()
                    print()
                    if input("Do you want another joke?(y/n): ").lower() == "n":
                        break
            case '6':
                os.system('cls')
                print()
                while True:
                    tell_story()
                    print()
                    if input("Do you want another story?(y/n): ").lower() == "n":
                        break
            case '7':
                os.system('cls')
                print('Have a good day!')
                break
            case _:
                print('Invalid choice')


if __name__ == '__main__':
    display_menu()
