import pygame, random, threading, queue

direction = {}

direction['UP']=0
direction['RIGHT']=1
direction['DOWN']=2
direction['LEFT']=3

directionPos = {}
directionPos['UP']=(0,-1)
directionPos['RIGHT']=(1,0)
directionPos['DOWN']=(0,1)
directionPos['LEFT']=(-1,0)

leftBorder = topBorder = 10
rightBorder = 590
bottomBorder = 390

def log(text):
	logging = True
	if logging == True: 
		print(text)

def randomStart():
	return random.randint(10,590),random.randint(10,390)
	
def showFail():
	# ~ screen.fill((0,0,0))
	font = pygame.font.Font('Calibri.ttf', 32)
	text = font.render("Game Over", True, (0,0,255), (255,255,255))
	textRect = text.get_rect() 
	textRect.center = (300,200)
	screen.blit(text, textRect)
	
	
def makeFood():
	x,y = randomStart()
	surface = pygame.Surface((50,50))
	surface.fill((100,100,100))
	screen.blit(surface,(x,y))
	return x,y
	
def clearFood(x,y):
	surface = pygame.Surface((50,50))
	surface.fill((0,0,0))
	screen.blit(surface,(x,y))
	
def atFood(x,y,foodX,foodY):
	if x>=foodX and x<=foodX+50 and y>=foodY and y<=foodY+50:
		return True
	return False

def main():
	global screen, snakePos
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((600,400))
	
	x,y = randomStart()
	
	nextDir = 'RIGHT'
	snakeSize = 50
	
	snakePos = [(x,y)]
	screen.fill((0,0,0))
	
	isFoodAvailable = False
	hasFailed = False
	exit = False
	
	log('start')
	while not exit:	
		# ~ log('in while')
		curDir = nextDir
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_ESCAPE:
					exit = True
				if event.key == pygame.K_r:
					hasFailed = False
					screen.fill((0,0,0))
					isFoodAvailable = False
					snakeSize = 50
			if not hasFailed and event.type == pygame.KEYDOWN: 
				if curDir != 'DOWN' and event.key == pygame.K_UP:
					nextDir = 'UP'
				if curDir != 'UP' and event.key == pygame.K_DOWN:
					nextDir = 'DOWN'
				if curDir != 'LEFT' and event.key == pygame.K_RIGHT:
					nextDir = 'RIGHT'
				if curDir != 'RIGHT' and event.key == pygame.K_LEFT:
					nextDir = 'LEFT'
					 
				if curDir == 'DOWN' and event.key == pygame.K_SPACE:
					nextDir = 'LEFT'
				if curDir == 'RIGHT' and event.key == pygame.K_SPACE:
					nextDir = 'DOWN'
				if curDir == 'UP' and event.key == pygame.K_SPACE:
					nextDir = 'RIGHT'
				if curDir == 'LEFT' and event.key == pygame.K_SPACE:
					nextDir = 'UP'
										
		if (x <= leftBorder and curDir == 'LEFT'): 
			nextDir = 'UP'
		if (x >= rightBorder and curDir == 'RIGHT'): 
			nextDir = 'DOWN'
		if (y <= topBorder and curDir == 'UP'):
			nextDir = 'RIGHT'
		if (y >= bottomBorder and curDir == 'DOWN'):
			nextDir = 'LEFT'
			
		x += directionPos[nextDir][0]
		y += directionPos[nextDir][1]
		
		if not isFoodAvailable:
			log('isFoodAvailable')
			foodX,foodY = makeFood()
			isFoodAvailable = True
		
		if (x,y) in snakePos:
			log('hasFailed')
			hasFailed = True
		
		if atFood(x,y,foodX,foodY):
			log('atFood')
			clearFood(foodX,foodY)
			isFoodAvailable = False
			snakeSize += 1
			
		if len(snakePos) > snakeSize:
			tailPos = snakePos.pop()
			pygame.draw.line(screen,(0,0,0),tailPos,tailPos,1)
		snakePos.insert(0,(x,y))
		pygame.draw.line(screen,(255,255,255),(x,y),(x,y),1)
		pygame.display.flip()
		
		if hasFailed:	
			showFail()	
		clock.tick(240)
	
	log('end')
	
	
if __name__ == '__main__':
	main()
