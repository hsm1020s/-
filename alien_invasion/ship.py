import pygame

class Ship:
    """우주선을 관리하는 클래스"""

    def __init__(self,ai_game):
        """우주선을 초기화하고 시작 위치를 설정합니다"""
        self.screen = ai_game.screen #
        self.screen_rect = ai_game.screen.get_rect() #

        # 우주선 이미지를 불러오고 사각형을 가져옵니다
        self.image = pygame.image.load(r'C:\renew\Shooting.py\alien_invasion\images\ship.bmp') #
        self.rect = self.image.get_rect()

        # 우주선의 초기 위치는 화면 하단 중앙입니다
        self.rect.midbottom = self.screen_rect.midbottom #
#-------------------------------------------------------------------------------------------------------------
        self.image_mhs = pygame.image.load(r'C:\renew\Shooting.py\alien_invasion\images\mhs.bmp')
        self.rect2 = self.image_mhs.get_rect()

        # self.image_mhs를 화면 중앙에 그립니다
        self.rect2.center = self.screen_rect.center
        

    def blitme(self): #
        """우주선을 현재 위치에 그립니다"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image_mhs, self.rect2)


    