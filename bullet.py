#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen=screen
		
		#��(0,0)������һ����ʾ�ӵ��ľ��Σ���������ȷ��λ��
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		#�洢��С����ʾ���ӵ�λ��
		self.y=float(self.rect.y)
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
	
	def update(self):
		#���±�ʾ�ӵ���С��ֵ
		self.y-=self.speed_factor
		self.rect.y=self.y
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
