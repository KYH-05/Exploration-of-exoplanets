#이걸로 케플러도 고치면 됨 ㅋㅋ
#-----------------------------------------------------------------------------------------------------------------------
import pygame,sys
import matplotlib.pyplot as plt
import math
import time
import os
pygame.init()
SW=1200
SH=700
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('A')
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Px=370#planet
Py=550
Sx=370#star
Sy=320
Cx=370#center
Cy=350
Ex=40#Earth(관측점)
Ey=350
Ox=370#orbit
Oy=350
R=200#행성 공전 반지름-단위km인데 여기에 1000000을 곱한
r=30#항성 공전 반지름
T=8#주기
w=2*math.pi/T#각속도
v=r*w#항성의 공전속도
xs=[]
ys=[]
spectrumX=640
spectrumY=320
spectrumW=500
spectrumH=101.875
rate=5/8
spectrumS=350
spectrumE=700
#-----------------------------------------------------------------------------------------------------------------------
def Pmove():
  pygame.draw.circle(screen, (BLUE), (Px,Py),7)
def Smove():
  pygame.draw.circle(screen, (RED), (Sx, Sy), 7)
def center():
  pygame.draw.circle(screen, (WHITE), (Cx, Cy), 2)
def earth():
  pygame.draw.circle(screen, (GREEN), (Ex, Ey), 7)
def orbit():
  pygame.draw.circle(screen,(WHITE),(Ox,Oy),R,2)
def draw():
  screen.fill(BLACK)
  Pmove()
  Smove()
  center()
  earth()
  orbit()

#-----------------------------------------------------------------------------------------------------------------------
t1=time.time()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  draw()

  t=time.time()-t1
  Px = Cx-(R * math.sin(w * t))
  Py= Cy-(R * math.cos(w * t))
  Sx=Cx+(r * math.sin(w * t))
  Sy=Cy+(r * math.cos(w * t))
  rad=w * t
  rv=v*math.cos(rad)#Radial velocity(시선속도)
  xs.append(t)
  ys.append(rv)
  plt.plot(xs,ys,c='r')
  plt.pause(0.000000000001)


  img = pygame.image.load(os.getcwd()+"\spectrum.jpg")
  #img = pygame.image.load("C:/Users/EK/Desktop/earth/spectrum.jpg")
  img = pygame.transform.scale(img, (spectrumW,spectrumH))
  screen.blit(img, (spectrumX,spectrumY))
  lineN = 4
  lineX = [410, 434, 486, 656]
  reallineX=[0,0,0,0]
  c = 1070000000 / 1000000  # 행성공전 반지름 200->200*1000000km로 간주
  for i in range(0,lineN):
    reallineX[i]=(rv/c*lineX[i])+lineX[i]
  for i in range(0, lineN):
    asX = ((reallineX[i] - spectrumS) * (spectrumW/(spectrumE-spectrumS))) + spectrumX
    asY = spectrumY
    asW = 5
    asH = spectrumH
    pygame.draw.rect(screen, (BLACK), (asX, asY, asW, asH))


  pygame.display.update()
  clock.tick(60)
#-----------------------------------------------------------------------------------------------------------------------
plt.show()
#질량조절시(항성-행성관 관련성)
# 행성의 질량을 낮추었을 때, 질량중심과 항성과의 거리가 줄어들고 케플러 3법칙에 따라 공전주기가 짧아지기 때문에 도플러 효과가 잘 나타나지 않는다는 것을 분석함.
# 행성 공전 반지름과 항성 공전 반지름
