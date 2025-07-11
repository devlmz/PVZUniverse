import pygame
import sys
import os
import screen

pygame.init()
pygame.mixer.init()
path = os.getcwd()
images_path = path.replace("str","images\\")    #图片路径
music_path = path.replace("str","music\\")      #音乐音效路径
pygame.mixer.music.load(music_path+'Faster.mp3')
pygame.mixer.music.play(-1)     #音乐播放

#下载图片
#以及获得按钮图片的位置矩形
surface = pygame.image.load(images_path+"Surface.jpg").convert()
adventure = pygame.image.load(images_path+'SelectorScreenAdventure1.png').convert_alpha()
adventure_start = pygame.image.load(images_path+'SelectorScreenStartAdventure.png').convert_alpha()
adventure_down = pygame.image.load(images_path+"SelectorScreenAdventure1.png").convert_alpha()
challenges = pygame.image.load(images_path+'SelectorScreenChallenges.png').convert_alpha()
challenges_rect = challenges.get_rect()
survival = pygame.image.load(images_path+'SelectorScreenSurvival.png').convert_alpha()
survival_rect = survival.get_rect()
WoodSign1 = pygame.image.load(images_path+'SelectorScreen_WoodSign1_32.png').convert_alpha()
WoodSign2_down = pygame.image.load(images_path+'SelectorScreen_WoodSign2_32_1.png').convert_alpha()
WoodSign2 = pygame.image.load(images_path+'SelectorScreen_WoodSign2_32.png').convert_alpha()
WoodSign3 = pygame.image.load(images_path+'SelectorScreen_WoodSign3_32.png').convert_alpha()
WoodSign2_rect = WoodSign2.get_rect()
WoodSign2_rect.left,WoodSign2_rect.top = 20,140
WoodSign2_rect.width,WoodSign2_rect.height = WoodSign2_rect.width-20,WoodSign2_rect.height-20
survival_shadow = pygame.image.load(images_path+'SelectorScreen_Shadow_Survival.png').convert_alpha()
adventure_shadow = pygame.image.load(images_path+'SelectorScreen_Shadow_Adventure.png').convert_alpha()
challenges_shadow = pygame.image.load(images_path+'SelectorScreen_Shadow_Challenge.png').convert_alpha()

def inter():
    counter = 1          #关卡计数器
    if counter == 1 :
        adv = adventure_start
    else:
        adv = adventure
        #默认显示
    wood2 = WoodSign2
    adv_rect1 = adv.get_rect()
    adv_rect2 = adv.get_rect()
    adv_rect1.left,adv_rect1.top = 478,85
    adv_rect1.width,adv_rect1.height = adv_rect1.width - 9, adv_rect1.height - 70
    adv_rect2.left,adv_rect2.top = 478+205,85+74
    adv_rect2.width,adv_rect2.height = 117,23
    adv_button = screen.GameButton(adv,adventure_down,(adv_rect1,adv_rect2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            adv_button.down(event,"down_up",'level'+str(counter))
                #鼠标移动事件处理
            if event.type == pygame.MOUSEMOTION:
                if WoodSign2_rect.collidepoint(event.pos):
                    wood2 = WoodSign2_down
                else:
                    wood2 = WoodSign2
        screen.screen1.blit(surface, (0, 0))
        screen.screen1.blit(WoodSign1, (10, 0))
        screen.screen1.blit(wood2, (10,140))
        screen.screen1.blit(WoodSign3, (10, 200))
        screen.screen1.blit(adventure_shadow,(466,54))
        screen.screen1.blit(survival_shadow, (476,166))
        screen.screen1.blit(challenges_shadow,(481,255))
        screen.screen1.blit(adv_button.image, (475, 53))
        screen.screen1.blit(survival, (475, 161))
        screen.screen1.blit(challenges, (480, 251))
        pygame.display.flip()