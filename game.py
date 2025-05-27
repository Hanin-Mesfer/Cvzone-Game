import cv2
import random
import time
from cvzone.HandTrackingModule import HandDetector
import pygame

pygame.mixer.init()
catch_sound = pygame.mixer.Sound('mixkit-arcade-game-jump-coin-216.wav')  # حط ملف صوتي بصيغة wav بنفس مسار السكربت


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(detectionCon=0.8, maxHands=1)


num_circles = 5  
circles = []
circle_radius = 40
score = 0
game_duration = 60
start_time = 0
game_started = True
start_time = time.time()


def create_circles(num):
    new_circles = []
    for _ in range(num):
        pos = [random.randint(100, 540), random.randint(100, 380)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_circles.append({'pos': pos, 'color': color, 'radius': circle_radius})
    return new_circles

circles = create_circles(num_circles)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

   

    
    time_remaining = int(game_duration - (time.time() - start_time))
    hands, img = detector.findHands(frame)

    if hands:
        lm_list = hands[0]['lmList']
        index_finger_tip = lm_list[8][0:2]

        for circle in circles:
            dist = ((index_finger_tip[0] - circle['pos'][0]) ** 2 + (index_finger_tip[1] - circle['pos'][1]) ** 2) ** 0.5

            if dist < circle['radius']:
                score += 1
              
                circle['pos'] = [random.randint(100, 540), random.randint(100, 380)]
                circle['color'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
               
                circle['radius'] = max(20, 40 - score // 5)
                
                pygame.mixer.Sound.play(catch_sound)

    
    for circle in circles:
        circle['radius'] = max(20, 40 - score // 5)


    for circle in circles:
        cv2.circle(frame, tuple(circle['pos']), circle['radius'], circle['color'], -1)

   

    font = cv2.FONT_HERSHEY_SIMPLEX
    color_text = (255, 255, 255) 

    cv2.putText(frame, f'Score: {score}', (20, 50), font, 1.2, color_text, 3)
    cv2.putText(frame, f'Time: {time_remaining}s', (190, 50), font, 1.2, color_text, 3)

    


    if time_remaining <= 0:
        cv2.putText(frame, "Game Over!", (200, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        cv2.putText(frame, f'Your Score: {score}', (200, 260),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        cv2.imshow("Catch the Circles", frame)
        cv2.waitKey(3000)
        break

    cv2.imshow("Catch the Circles", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

