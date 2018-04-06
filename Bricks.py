"""
This method is to find minimum number of bricks used in making a goal which is x inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
For eg:
(3,2,6) -> will return number of bricks used as small 1 and big 1
(5,2,10) -> will return number of bricks used as small 0 and big 2
(3,0,4) -> will return not enough bricks
(3,2,9) -> will return not enough small bricks and hence cant be done
"""

def make_bricks(small, big, goal):
	bigbricks= 0
	smalbricks = 0
	if (big*5+small <goal):
		print("Not enough bricks!")
	elif (goal%5>small):
		print("Not enough small bricks!")
	else:
		print("Its possible!")
		bigbricks = int(goal/5)
		if bigbricks > big:
			bigbricks = big
			smallbricks = goal - big*5
		else:
			smallbricks = goal - bigbricks*5
		print("Number of small bricks is "+str(smallbricks)+ " and big bricks is "+str(bigbricks))

