#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
************************************************************************
*Binary clock                                                          *
*Copyright (C) 2010  Komarov Alexander                                 *
*                                                                      *
*This program is free software: you can redistribute it and/or modify  *
*it under the terms of the GNU General Public License as published by  *
*the Free Software Foundation, either version 3 of the License, or     *
*(at your option) any later version.                                   *
*                                                                      *
*This program is distributed in the hope that it will be useful,       *
*but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See t           *
*GNU General Public License for more details.                          *
                                                                       *
*You should have received a copy of the GNU General Public License     *
*along with this program.  If not, see <http://www.gnu.org/licenses/>. *
************************************************************************'''

#! /usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
import time
class Clock: 
     screen=pygame.display.set_mode((640, 480))
     def __init__(self):
          pygame.init()
          pygame.display.set_caption('Binary Clock')
          self.display()
     def display(self):
         
         while True:
             for e in pygame.event.get():
                 if e.type == pygame.QUIT: 
                     exit(0)
                 elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                     exit(0)
             self.capture()
             self.logic()
             pygame.display.flip()
             time.sleep(0.5)

     def capture(self):

         #Hour
         #Row1
         pygame.draw.circle(self.screen, (255, 255, 255), (70, 400), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (70, 300), 30 )
         #Row2
         pygame.draw.circle(self.screen, (255, 255, 255), (170, 400), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (170, 300), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (170, 200), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (170, 100), 30 )
         #Min
         #Row1
         pygame.draw.circle(self.screen, (255, 255, 255), (270, 400), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (270, 300), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (270, 200), 30 )
         #Row2
         pygame.draw.circle(self.screen, (255, 255, 255), (370, 400), 30 )  
         pygame.draw.circle(self.screen, (255, 255, 255), (370, 300), 30 ) 
         pygame.draw.circle(self.screen, (255, 255, 255), (370, 200), 30 ) 
         pygame.draw.circle(self.screen, (255, 255, 255), (370, 100), 30 ) 
         #Sec
         #Row1
         pygame.draw.circle(self.screen, (255, 255, 255), (470, 400), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (470, 300), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (470, 200), 30 )
         #Row2
         pygame.draw.circle(self.screen, (255, 255, 255), (570, 400), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (570, 300), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (570, 200), 30 )
         pygame.draw.circle(self.screen, (255, 255, 255), (570, 100), 30 )
     def logic(self):
         #Hour
         if int(time.asctime( time.localtime(time.time()) )[11])==1:
             pygame.draw.circle(self.screen, (255, 0, 0), (70, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[11])==2:
             pygame.draw.circle(self.screen, (255, 0, 0), (70, 300), 30 )

         if int(time.asctime( time.localtime(time.time()) )[12])==1:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==2:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==3:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==4:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==5:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==6:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 200), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==7:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 300), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==8:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 100), 30 )
         if int(time.asctime( time.localtime(time.time()) )[12])==9:
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (170, 100), 30 )
         #Min
         if int(time.asctime( time.localtime(time.time()) )[14])==1:
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[14])==2:
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[14])==3:
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[14])==4:
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[14])==5:
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 200), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (270, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==1:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==2:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==3:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==4:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==5:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==6:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 200), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==7:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 300), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==8:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 100), 30 )
         if int(time.asctime( time.localtime(time.time()) )[15])==9:
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (370, 100), 30 )
        #Sec
         if int(time.asctime( time.localtime(time.time()) )[17])==1:
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[17])==2:
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[17])==3:
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[17])==4:
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[17])==5:
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (470, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==1:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 400), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==2:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==3:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==4:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==5:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==6:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 200), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 300), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==7:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 300), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 200), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==8:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 100), 30 )
         if int(time.asctime( time.localtime(time.time()) )[18])==9:
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 400), 30 )
            pygame.draw.circle(self.screen, (255, 0, 0), (570, 100), 30 )
     
     
         
if __name__ == "__main__":Clock()
