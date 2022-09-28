'''
정보 창작 과제 수행

프로젝트 이름 : 시간표

📅 요일 입력하면 해당 요일의 시간표 제공
'''



Yoil = input('시간표를 볼 요일을 적어주세요.\n예)월, 월요일\n')

Wol = ['영듣', '심국(이)', '기하', '보건(최)', '생명', '수과탐', '화학']
Wha = ['보건(임)','기하','여지','화학','심국(황)','영어','창체']
Su = ['체육','심영','여지','정보','창체','창체']
Mok = ['수과탐','영어','기하','생명','심국(이)','여지','화학']
Geum = ['심국(황)','기하','생명','진로','정보','심영','체육']



if Yoil == '월' or Yoil == '월요일':
    DailyYoil = Wol
    n=0
    print('월요일 시간표를 출력합니다.')
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])

elif Yoil == '화' or Yoil == '화요일':
    DailyYoil = Wha
    n=0
    print('화요일 시간표를 출력합니다.')
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])

elif Yoil == '수' or Yoil == '수요일':
    DailyYoil = Su
    n=0
    print('수요일 시간표를 출력합니다.')
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])

elif Yoil == '목' or Yoil == '목요일':
    DailyYoil = Mok
    n=0
    print('목요일 시간표를 출력합니다.')
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])

elif Yoil == '금' or Yoil == '금요일':
    DailyYoil = Geum
    n=0
    print('금요일 시간표를 출력합니다.')
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
    n+=1
    print(str(n+1)+'교시 :',DailyYoil[n])
else:
    print('예시와 같게 요일을 입력해주세요!')




