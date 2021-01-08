from PIL import Image
from requests import post
from time import time, localtime, strftime, sleep
from concurrent.futures import ThreadPoolExecutor
#------------------------Config Start--------------------#
imagePath = "."
cookies = []
width = 100
height = 100
x1 = 1
y1 = 1
stoptime = 0.1
homepageurl = "https://luogu.com.cn/"
#---------------------Config End-------------------------#
colors = {(0, 0, 0): 0,
          (255, 255, 255): 1,
          (170, 170, 170): 2,
          (85, 85, 85): 3,
          (254, 211, 199): 4,
          (255, 196, 206): 5,
          (250, 172, 142): 6,
          (255, 139, 131): 7,
          (244, 67, 54): 8,
          (233, 30, 99): 9,
          (226, 102, 158): 10,
          (156, 39, 176): 11,
          (103, 58, 183): 12,
          (63, 81, 181): 13,
          (0, 70, 112): 14,
          (5, 113, 151): 15,
          (33, 150, 243): 16,
          (0, 188, 212): 17,
          (59, 229, 219): 18,
          (151, 253, 220): 19,
          (22, 115, 0): 20,
          (55, 169, 60): 21,
          (137, 230, 66): 22,
          (215, 255, 7): 23,
          (255, 246, 209): 24,
          (248, 203, 140): 25,
          (255, 235, 59): 26,
          (255, 193, 7): 27,
          (255, 152, 0): 28,
          (255, 87, 34): 29,
          (184, 63, 39): 30,
          (121, 85, 72): 31,
          }


def min_color_diff(color_to_match, colors):
    return min(
        (color_dist(color_to_match, test), colors[test])
        for test in colors)


def color_dist(c1, c2):
    return sum(abs(a - b) for a, b in zip(c1, c2))


def get_color(pixel):
    return min_color_diff(pixel, colors)[1]

def printpic(x,y,color,cookie):
     body = {'x': str(x+x1),'y': str(y+y1),'color': str(color)}
     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4346.0 Safari/537.36 Edg/89.0.731.0','cookie': cookie, 'Referer': "https://www.luogu.com.cn/paintBoard", "content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
     response = post(homepageurl+"paintBoard/paint",headers=headers, data=body)
     sleep(stoptime)
     return response
def getpicdata(imagePath,width,height):
     print(str(strftime("[%Y-%m-%d %H-%M-%S] Analyzing Picture...",localtime())),end = ' ')
     data = []
     img = Image.open(imagePath)
     img = img.resize((width,height))
     w,h=img.size
     for i in range(0,w,1):
          for j in range(0,h,1):
               color = get_color(img.getpixel((i,j)))
               data.append({'x':i,'y':j,'color':color})
     sleep(0.5)
     print('Done')
     return data
def picprint(data):
     print(str(strftime("[%Y-%m-%d %H-%M-%S] Start Painting...",localtime())),end = ' ')
     with ThreadPoolExecutor(max_workers=10) as t:
          now_cookie = 0
          for i in data:
               t.submit(printpic(i['x'],i['y'],i['color'],cookies[now_cookie]))
               if now_cookie+1 < len(cookies):
                    now_cookie+=1
               else:
                    now_cookie=0
               sleep(stoptime)
     print('Done')

# picprint(getpicdata(imagePath,width,height))
def main():
     print(str(strftime("[%Y-%m-%d %H-%M-%S] Luogu Paintboard Helper v1.0.0\n",localtime())),end = '')
     print(str(strftime("[%Y-%m-%d %H-%M-%S]\n",localtime())),end = '')
     print(str(strftime("[%Y-%m-%d %H-%M-%S] File",localtime()))+imagePath,end = '\n')
     print(str(strftime("[%Y-%m-%d %H-%M-%S]",localtime()))+" Width="+str(width)+" Height="+str(height),end = '\n')
     
     picprint(getpicdata(imagePath,width,height))
if __name__ =='__main__':
     try:
          main()
     except Exception as e:
          print()
          print(str(strftime("[%Y-%m-%d %H-%M-%S]",localtime())),end = ' ')
          print(e)
     finally:
          print(str(strftime("[%Y-%m-%d %H-%M-%S]",localtime()))+"",end = ' ')