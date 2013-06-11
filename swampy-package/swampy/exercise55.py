from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	

def draw(turtle, length, n):
	if n == 0:
		return
	angle = 45
	fd(turtle, length*n)
	lt(turtle, angle)
	draw(turtle, length, n-1)
	rt(turtle, 2*angle)
	draw(turtle, length, n-1)
	lt(turtle, angle)
	bk(turtle, length*n)

draw(bob, 20, 2)








wait_for_user()	