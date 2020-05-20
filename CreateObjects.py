
class Robot:
    def __init__(self, description):
        self.name = description[0]
        self.color = description[1]
        self.weight = description[2]
        self.owner = None

    def introduce_yourself(self):
        print("Hello!, I am " + self.name  + ".")
        print("I am " + self.color + " colored.")
        print("I weigh " + self.weight + " pounds.")
        if self.owner is None:
            print("I don't belong to anyone.")
        else:
            print("I belong to " + self.owner + ".")


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.robot = None
    
    def assignOwner(self):
        self.robot.ownername = self.player_name


if __name__ == '__main__':
    robot1_description = list(map(str, input().split()))
    robot2_description = list(map(str, input().split()))

    robot1_object = Robot(robot1_description)
    robot2_object = Robot(robot2_description)

    playerOne = Player("Atul")
    playerOne.robot = robot1_object
    playerOne.assignOwner()

    playerTwo = Player("Ankit")
    playerTwo.robot = robot2_object

    playerOne.robot.introduce_yourself()
    print("\n")
    playerTwo.robot.introduce_yourself()
