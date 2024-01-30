import numpy as np
import pygame
import mediapipe as mp
import cv2
import random

# Webcam çözünürlüğünü ayarla
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1300)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)

pygame.init()
en, boy = 1300, 700
pencere = pygame.display.set_mode((en, boy))
zaman = pygame.time.Clock()
fps = 30

# El görselini yükle
el = pygame.image.load("el.png")
el_koordinat = el.get_rect()

# Farklı meyve görsellerini yükle
elma = pygame.image.load("elma.png")
elma_koordinat = elma.get_rect()

armut = pygame.image.load("armut.png")
armut_koordinat = armut.get_rect()

kiraz = pygame.image.load("kiraz.png")
kiraz_koordinat = kiraz.get_rect()

karpuz = pygame.image.load("karpuz.png")
karpuz_koordinat = karpuz.get_rect()

cilek = pygame.image.load("cilek.png")
cilek_koordinat = cilek.get_rect()

font = pygame.font.Font(None, 60)
x, y = 500, 500
puan = 0
model = mp.solutions.hands
dongu = True

# Rastgele bir meyve görseli seç
secili_meyve = random.choice([
    ("elma.png", elma_koordinat, "Apple"),  # Elma olarak isimlendirildi
    ("armut.png", armut_koordinat, "Pear"),  # Armut olarak isimlendirildi
    ("kiraz.png", kiraz_koordinat, "Cherry"),
    ("karpuz.png", karpuz_koordinat, "Watermelon"),
    ("cilek.png", cilek_koordinat, "Strawberry"),
])

secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))

with model.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as el_algila:
    while dongu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dongu = False

        _, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = el_algila.process(rgb)
        if result.multi_hand_landmarks:
            for el_koordinatlari in result.multi_hand_landmarks:
                el_konumu = el_koordinatlari.landmark[8]
                x = int(el_konumu.x * en)
                y = int(el_konumu.y * boy)

        el_koordinat.center = (x, y)
        rgb = np.rot90(rgb)
        img = pygame.surfarray.make_surface(rgb).convert()
        img = pygame.transform.flip(img, True, False)
        pencere.blit(img, (0, 0))
        pencere.blit(el, el_koordinat)
        
        # Seçili altın görselini ekrana yerleştir
        pencere.blit(elma, (elma_koordinat.topleft[0] + 10, elma_koordinat.topleft[1] + 10))
        pencere.blit(armut, (armut_koordinat.topleft[0] - 10, armut_koordinat.topleft[1] - 10))
        pencere.blit(kiraz, (kiraz_koordinat.topleft[0] - 10, kiraz_koordinat.topleft[1] - 10))
        pencere.blit(karpuz, (karpuz_koordinat.topleft[0] - 10, karpuz_koordinat.topleft[1] - 10))
        pencere.blit(cilek, (cilek_koordinat.topleft[0] - 10, cilek_koordinat.topleft[1] - 10))
        
        yazi = font.render("Point:" + " "+ str(puan), True, (0, 0, 255), (0, 0, 0))
        yazi_koordinat = yazi.get_rect()
        yazi_koordinat.topleft = (20, 20)
        pencere.blit(yazi, yazi_koordinat)
        
        # Hangi görseli seçmeniz gerektiğini tek yazı olarak yazdır
        secili_yazi = font.render("Choose: " + secili_meyve[2], True, (255, 0, 0), (0, 0, 0))
        secili_yazi_koordinat = secili_yazi.get_rect()
        secili_yazi_koordinat.topleft = (20, 80)
        pencere.blit(secili_yazi, secili_yazi_koordinat)

        if el_koordinat.colliderect(elma_koordinat):
            elma_koordinat.topleft = (random.randint(20, en - 20), random.randint(20, boy - 20))
            if secili_meyve[2] == "Apple":
                puan += 1  # Doğru meyveyi topladınız
            else:
                puan -= 1  # Yanlış meyveyi topladınız
            # Puan değiştiğinde yeni bir görsel seç
            secili_meyve = random.choice([
                ("elma.png", elma_koordinat, "Apple"),
                ("armut.png", armut_koordinat, "Pear"),
                ("kiraz.png", kiraz_koordinat, "Cherry"),
                ("karpuz.png", karpuz_koordinat, "Watermelon"),
                ("cilek.png", cilek_koordinat, "Strawberry"),
            ])
            secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))

        if el_koordinat.colliderect(armut_koordinat):
            armut_koordinat.topleft = (random.randint(20, en - 20), random.randint(20, boy - 20))
            if secili_meyve[2] == "Pear":
                puan += 1  # Doğru meyveyi topladınız
            else:
                puan -= 1  # Yanlış meyveyi topladınız
            # Puan değiştiğinde yeni bir görsel seç
            secili_meyve = random.choice([
                ("elma.png", elma_koordinat, "Apple"),
                ("armut.png", armut_koordinat, "Pear"),
                ("kiraz.png", kiraz_koordinat, "Cherry"),
                ("karpuz.png", karpuz_koordinat, "Watermelon"),
                ("cilek.png", cilek_koordinat, "Strawberry"),
            ])
            secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))
            
        if el_koordinat.colliderect(kiraz_koordinat):
            kiraz_koordinat.topleft = (random.randint(20, en - 20), random.randint(20, boy - 20))
            if secili_meyve[2] == "Cherry":
                puan += 1  # Doğru meyve topladınız
            else:
                puan -= 1  # Yanlış meyve topladınız
            # Puan değiştiğinde yeni bir görsel seç
            secili_meyve = random.choice([
                ("elma.png", elma_koordinat, "Apple"),
                ("armut.png", armut_koordinat, "Pear"),
                ("kiraz.png", kiraz_koordinat, "Cherry"),
                ("karpuz.png", karpuz_koordinat, "Watermelon"),
                ("cilek.png", cilek_koordinat, "Strawberry"),
            ])
            secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))
            
        if el_koordinat.colliderect(karpuz_koordinat):
            karpuz_koordinat.topleft = (random.randint(20, en - 20), random.randint(20, boy - 20))
            if secili_meyve[2] == "Watermelon":
                puan += 1  # Doğru meyve topladınız
            else:
                puan -= 1  # Yanlış meyve topladınız
            # Puan değiştiğinde yeni bir görsel seç
            secili_meyve = random.choice([
                ("elma.png", elma_koordinat, "Apple"),
                ("armut.png", armut_koordinat, "Pear"),
                ("kiraz.png", kiraz_koordinat, "Cherry"),
                ("karpuz.png", karpuz_koordinat, "Watermelon"),
                ("cilek.png", cilek_koordinat, "Strawberry"),
            ])
            secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))
            
        if el_koordinat.colliderect(cilek_koordinat):
            cilek_koordinat.topleft = (random.randint(20, en - 20), random.randint(20, boy - 20))
            if secili_meyve[2] == "Strawberry":
                puan += 1  # Doğru meyve topladınız
            else:
                puan -= 1  # Yanlış meyve topladınız
            # Puan değiştiğinde yeni bir görsel seç
            secili_meyve = random.choice([
                ("elma.png", elma_koordinat, "Apple"),
                ("armut.png", armut_koordinat, "Pear"),
                ("kiraz.png", kiraz_koordinat, "Cherry"),
                ("karpuz.png", karpuz_koordinat, "Watermelon"),
                ("cilek.png", cilek_koordinat, "Strawberry"),
            ])
            secili_meyve[1].center = (random.randint(20, en - 20), random.randint(20, boy - 20))

        pygame.display.update()
        zaman.tick(fps)

pygame.quit()