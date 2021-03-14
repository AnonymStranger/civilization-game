
import time
class Player:
    global money
    money = 10000
    global people
    people = 100
    global warriors
    warriors = 0
    global workers
    workers = 0
    global traders
    traders = 0
    global freePeople
    freePeople = people - warriors - traders - workers
    global wood
    wood = 0
    global stone
    stone = 0
    global buildings
    buildings = 0
    global temples
    temples = 0
    global food
    food = 500
    global water
    water = 1000
    def __init__(self, nickname, kingdName):
        
        self.nickname = nickname
        self.kingdName = kingdName
    
    def timer(timeout):#Отсчитывает время и затем выполняет какую-нибудь функцию
        time.sleep(timeout)
    def showPlayerInfo(self):
        print('---------------------------------')
        print(f'|age:                        {self.age}|')
        print(f'|name:                  {self.nickname}|')
        print(f'|kingdom:              {self.kingdName}|')
        print('---------------------------------')
    def showAllResourses(self):
        global freePeople        
        print('---------------------------------')
        print(f'|money: {money}')
        print(f'|people: {people}')
        print('|warriors:', warriors)
        print('|workers:', workers)
        print('|traders')
        print('|free people:', freePeople)
        print('|wood:', wood,)
        print('|stone:', stone)
        print('|buildings:', buildings)
        print('|temples:', temples)
        print('|food:', food)
        print('|water:', water)
        print('---------------------------------')
    def showCommands(self):
        print('Type quit to finish the game.')
        print('Type showPlayerInfo to look at your profile info.')
        print('Type showAllResourses to look at your kingdom resourses')
        print('Type tutorial to see the tutorial.')
    def processRequest(self):
        while True:
            request = input('Enter a command: ')
            if request == 'showMyInfo':
               Player.showPlayerInfo(self)
               continue
            elif request == 'showAllResourses':
               Player.showAllResourses(self)
               continue
            elif request == 'showCommands':
                Player.showCommands(self)
                continue
            elif request == 'tutorial':
                Narrator.tutorial(self)
                continue
            elif request == 'quit':
                print('Goodbye!')
                break
            elif request == 'changePeople':
                amount = int(input('Enter the amount of people: '))
                print('Workers - 1/Traders - 2/Warriors - 3')
                if people >= amount:
                   Player.changePeople(self, amount)
                else:
                    print(f'Not enough people. Your current amount of people is {people}')
                continue
            elif request == 'build':
                Player.build()
                continue
            else:
               print('Incorrect request.')
    def changePeople(self, amount):
        global freePeople
        global warriors
        global workers
        global traders
        while True:
             typeWorkers = int(input('Enter the number of people you want to change to: '))
             if typeWorkers == 1:
                workers += amount
                freePeople = freePeople - amount
                print('Sucessfully changed.')
                break
             elif typeWorkers == 2:
                traders += amount
                freePeople = freePeople - amount
                print('Sucessfully changed.')
                break
             elif typeWorkers == 3:
                warriors += amount
                freePeople = freePeople - amount
                print('Sucessfully changed.')
                break
             else:
                print('Incorrect input.Enter the number of type of people you want to change to.')
                continue
    def build():
        building = input('Enter the type of building: ')
        if building == 'hut':
           print('Please wait...')
           print('for 20 seconds')
           Player.timer(20)
           print('Successfully built.')
           global buildings
           buildings += 1
        elif building == 'defence-tower':
            print('Please wait...')
            print('for 10 seconds.')
            Player.timer(10)
            buildings += 1
class Narrator:
    def __init__(self):
        self.self = self
    def tutorial(self):
        print('Welcome to Human Civilization text game!')
        print('Here you will rule your territory from a primeval family to modern nation.')
        print('First you start with small amount of people and you will need workers to build a hut for them.')    
        print('Type changePeople to make 20 people workers. and then type quit')
        Player.processRequest(self)
        print('Great!')
        print('Now enter build, to build a hut.')
        print('Now print \'hut\'')
        Player.processRequest(self)
        print('Perfetto!')
        print('Now your people have a place to sleep on!.Now we must...')
        Player.timer(2)
        print('Oh no!The neighboring tribe is going to attack us!')
        print('Build a defence tower! Type of building: defence-tower.Immideatly!')
        Player.processRequest(self)
        print('Nice!')
        
        
def main():
    nickname = input('Enter your nickname: ')
    kingdName = input("Enter your kingdom name: ")
    print('To see all availiable commands type showCommands')
    player = Player(nickname, kingdName)
    player.processRequest()
main()