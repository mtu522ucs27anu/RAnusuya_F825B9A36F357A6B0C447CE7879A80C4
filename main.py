''' Implement  a class called player that representa a circket player. The player class should  have a method  calles play()which  prints the player is playing cricket  Derive two classes, Batsman and Bowler,from the player class. Override the play() method  in each derived class tp print"The batsman batting" and "The bowler is bowling ", respectively   Write  a rogramto creaye objects of both the Batsman and Bowler classes and call the play()method for each object.
   #Define the base class player
class  player:
defplay(self):
print("The player is playing circket")
#Define the derivef classBatsman
class Batsman (player):
defplay(self):
 print("The batsman ia batting" )
#Define the derived is calssBowler
class Bowler (player):
def play(self):
print("The bowler is bowling")
#create objects of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()
#call the play() method  for search object 
batsmam.play()
bowler.play()

