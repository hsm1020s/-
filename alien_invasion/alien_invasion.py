import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

    def __init__(self):
        """게임을 초기화하고 게임 자원을 만듭니다."""
        pygame.init() #

        self.clock = pygame.time.Clock()
        self.settings = Settings() #

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) #
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # 

        #배경색을 설정함
        self.bg_color = (230,230,230) #

    def run_game(self):
        """게임의 메인 루프를 시작"""
        while True: #
            # 키보드와 마우스의 이벤트에 응답
            for event in pygame.event.get(): #
                if event.type == pygame.QUIT: #
                    sys.exit()

            #루프를 반복할 때마다 화면을 다시 그린다.
            self.screen.fill(self.settings.bg_color) #
            self.ship.blitme() #

            #가장 최근 그린 화면을 표시합니다
            pygame.display.flip() #
            self.clock.tick(60)
                
if __name__ == '__main__':
    # 게임 인스턴스를 만들고 게임을 실행합니다
    ai= AlienInvasion()
    ai.run_game()