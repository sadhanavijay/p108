import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

#Create a fingertips array with the values of finger tips.(As given in Specific task1)
finger_tips=[8,12,16,20]
thumb_tip= 4 #Assigning thumbtip variable

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            # #array to hold true or false if finger is folded (AS given in specific task 2)
            for tip in finger_tips:
                x,y=int(lm_list[tip].x*w), int(lm_list[tip]y*h)
                cv2.circle(img, (x,y),15, (255,0,0,), cv2.FILLED)
                #writing condition to check if finger is folded i.e checking if finger tip starting value is smaller than finger starting position which is inner landmark. for index finger    
                #if finger folded changing color to green(As given in specific task3)
                if lm_list[tip].x<lm_list[tip-3].x:
                    cv2.circle(img, (x,y), 15, (0, 255, 0),cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)
                #checking if all fingers are folded(As given in Specific task 5 & 6)
            if lm_list[tip].y<lm_list[thumb_tip.1].y<lm_list[thumb_tip.2].y:
                print("LIKE")
                cv2putText(img,"LIKE",(20,30),cv2.FRONT_HERSHEY,1,(0,255,0),3)
            if lm_list[tip].y>lm_list[thumb_tip.1].y>lm_list[thumb_tip.2].y:
                print("DISLIKE")
                cv2putText(img,"DISLIKE",(20,30),cv2.FRONT_HERSHEY,1,(0,0,),3)

            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)

