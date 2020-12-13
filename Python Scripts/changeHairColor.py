import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def addBGR(img,xmin,ymin,x,y,b,g,r):    #BGR値をいじって髪色を変える
    img[ymin + y,xmin + x,0] += b
    img[ymin + y,xmin + x,1] += g
    img[ymin + y,xmin + x,2] += r 


img = cv.imread(r'images\hamabeminami.jpg')    #画像読み込み
img_test = cv.imread(r'images\hamabeminami.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)

ret,thresh = cv.threshold(gray,80,255,cv.THRESH_BINARY)    #threshを指定して白黒にはっきりとわける
thresh = cv.bitwise_not(thresh) #白黒反転させる
contours,hierarchy = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)    #contoursに領域を格納

print(f"contours={len(contours)},hierarchy={len(hierarchy)}")

area = [cv.contourArea(contours[i]) for i in range(len(contours))]  #それぞれの領域の面積を保持
area_max_index = np.argmax(area)    #リストareaの中で最大値を示す部分のインデックスを取得
# print(area_max_index)


im = cv.drawContours(img, contours[area_max_index], -1, (255,255,0), 1)   #境界線をひく


# print(contours[146])    #髪の輪郭。一番contoursの要素数が大きかった
cnt = contours[area_max_index]         #cntは座標[x,y]からなる二重配列
# for i in range(len(cnt)):
    # cv.circle(img_test,tuple(cnt[i][0]),5,[0,0,255],-1)
    # print(tuple(cnt[i]))

cnt_x_max = np.max(cnt[:,:,0])  #領域のx座標の最大値(横方向)
cnt_x_min = np.min(cnt[:,:,0])
cnt_y_max = np.max(cnt[:,:,1])  #領域のy座標の最大値(縦方向、始点は一番上なことに注意)
cnt_y_min = np.min(cnt[:,:,1])
cnt_width = cnt_x_max - cnt_x_min + 1   #領域の最大幅(for文で使うはず)
cnt_height = cnt_y_max - cnt_y_min + 1
dist_img = np.empty((cnt_height,cnt_width))

for x in range(cnt_width):
    for y in range(cnt_height):
        dist_img[y,x] = cv.pointPolygonTest(cnt,(x + cnt_x_min,y + cnt_y_min),True) #始点を[cnt_x_min,cnt_y_min]にあわせる
        if dist_img[y,x] > 0:   #領域なの点だったら
            # cv.circle(img_test,tuple([x + cnt_x_min,y + cnt_y_min]),1,[0,0,255],-1) #指定した座標に円を描く
            # img_test[y + cnt_y_min,x + cnt_x_min,0] += 40
            addBGR(img_test,cnt_x_min,cnt_y_min,x,y,85,0,0) #b,g,r値を追加！
            
print(cnt_x_max,cnt_x_min,cnt_y_max,cnt_y_min)

cv.imshow("drawContours",im)
# cv.imshow("Thresh",thresh)
# cv.imshow("HSV",hsv)
cv.imshow("img_test",img_test)

# cv.imwrite(r"images\drawContours2.jpg",im)   #画像保存
# cv.imwrite(r"images\kouichiTV_converted.jpg",img_test)

cv.waitKey(0)
cv.destroyAllWindows()
