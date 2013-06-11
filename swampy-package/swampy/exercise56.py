from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.01

def draw(turtle, length, n):
	if n == 0:
		return
	angle = 45
	kochCurve(turtle, length*n)
	lt(turtle, angle)
	draw(turtle, length, n-1)
	rt(turtle, 2*angle)
	draw(turtle, length, n-1)
	lt(turtle, angle)
	bk(turtle, length*n)

def kochCurve(turtle, n):
	if n<3:
		fd(turtle, n)
		return
	angle = 60 
	m = n/3.0
	kochCurve(turtle, m)
	lt(turtle, angle)
	kochCurve(turtle, m)
	rt(turtle, angle*2)
	kochCurve(turtle, m)
	lt(turtle, angle)
	kochCurve(turtle, m)
kochCurve(bob, 100)

def snowflake(turtle, n):
	for i in range(3):
		kochCurve(turtle, n)
		rt(turtle, 120)
		
snowflake(bob, 100)
		

wait_for_user()	