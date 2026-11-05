class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def show(self):
        print(self.name + " (цена: " + str(self.value) + ")")


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        if len(self.items) == 0:
            print("инвентарь пуст.")
        for item in self.items:
            item.show()

    def sort(self):
        n = len(self.items)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.items[j].value > self.items[j + 1].value:
                    temp = self.items[j]
                    self.items[j] = self.items[j + 1]
                    self.items[j + 1] = temp


class Player:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.alive = True
        self.inventory = Inventory()

    def go_to_start(self):
        self.row = 0
        self.col = 0


class Room:
    def __init__(self):
        self.items = []
        self.is_wall = False
        self.visited = False

    def enter(self, player):
        print("вы вошли в комнату.")
        for item in self.items:
            print("здесь лежит: " + item.name)

    def take_items(self, player):
        if len(self.items) == 0:
            print("здесь нечего брать.")
        for item in self.items:
            player.inventory.add(item)
            print("вы взяли: " + item.name)
        self.items = []


class Wall(Room):
    def __init__(self):
        Room.__init__(self)
        self.is_wall = True


class TrapRoom(Room):
    def enter(self, player):
        print("щёлк! это ловушка! вас телепортировало в начало лабиринта.")
        player.go_to_start()


class MonsterRoom(Room):
    def enter(self, player):
        print("в комнате притаился монстр! он набросился на вас...")
        player.alive = False


class ExitRoom(Room):
    def enter(self, player):
        print("вы нашли выход из лабиринта!")


class Game:

    def __init__(self):
        plan = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 0, 2, 0, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 3, 1, 0],
            [1, 1, 0, 0, 0, 4],
        ]

        self.rooms = []

        for row in plan:
            room_row = []
            for code in row:
                room_row.append(self.create_room(code))
            self.rooms.append(room_row)
        self.player = Player()
        self.rooms[0][0].visited = True

        self.rooms[0][1].items.append(Item("Ключ", 15))
        self.rooms[2][0].items.append(Item("Факел", 10))
        self.rooms[3][0].items.append(Item("Монета", 50))

    def create_room(self, code):
        if code == 1:
            return Wall()
        if code == 2:
            return TrapRoom()
        if code == 3:
            return MonsterRoom()
        if code == 4:
            return ExitRoom()
        return Room()

    def move(self, key):
        d_row = 0
        d_col = 0

        if key == "7":
            d_row = -1
            d_col = -1
        elif key == "8":
            d_row = -1
        elif key == "9":
            d_row = -1
            d_col = 1
        elif key == "4":
            d_col = -1
        elif key == "6":
            d_col = 1
        elif key == "1":
            d_row = 1
            d_col = -1
        elif key == "2":
            d_row = 1
        elif key == "3":
            d_row = 1
            d_col = 1

        new_row = self.player.row + d_row
        new_col = self.player.col + d_col

        if new_row < 0 or new_row >= len(self.rooms) or new_col < 0 or new_col >= len(self.rooms[0]):
            print("там граница лабиринта.")
            return
        room = self.rooms[new_row][new_col]
        if room.is_wall:
            print("там стена.")
            return

        self.player.row = new_row
        self.player.col = new_col
        room.visited = True
        room.enter(self.player)

    def show_map(self):
        print("карта (P - вы, # - стена, . - посещено, ? - неизвестно):")
        for i in range(len(self.rooms)):
            line = ""
            for j in range(len(self.rooms[i])):
                room = self.rooms[i][j]
                if i == self.player.row and j == self.player.col:
                    line = line + "P "
                elif room.is_wall:
                    line = line + "# "
                elif room.visited:
                    line = line + ". "
                else:
                    line = line + "? "
            print(line)

    def run(self):
        print("=== лабиринт ===")
        print("вы стоите в точке (0, 0). найдите выход и не попадитесь монстру!")
        print("цифры двигают вас в 8 сторон:")
        print("  7 8 9")
        print("  4   6")
        print("  1 2 3")
        print("команды: взять, инвентарь, сортировать (по цене), выход")
        print("после каждого хода показывается карта.")
        print("")
        self.show_map()

        while self.player.alive:
            room = self.rooms[self.player.row][self.player.col]
            if isinstance(room, ExitRoom):
                break
            print("")
            print("позиция: (" + str(self.player.row) + ", " + str(self.player.col) + ")")
            command = input("ваш ход: ").strip().lower()

            if command in ["1", "2", "3", "4", "6", "7", "8", "9"]:
                self.move(command)
            elif command == "взять":
                room.take_items(self.player)
            elif command == "инвентарь":
                self.player.inventory.show()
            elif command == "сортировать":
                self.player.inventory.sort()
                print("инвентарь отсортирован по цене.")
                self.player.inventory.show()
            elif command == "выход":
                print("вы покинули игру.")
                return
            else:
                print("неизвестная команда.")
            self.show_map()

        if self.player.alive:
            print("победа! вы выбрались из лабиринта.")
        else:
            print("вы погибли. игра окончена.")


game = Game()
game.run()