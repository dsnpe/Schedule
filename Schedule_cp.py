'''
코드 봇 대충 구상

프로젝트 이름 : 시간표 봇
🇵 🇾 / 🇯 🇸 


목적 : 매일 시간표 보기 귀찮음

📅 요일과 반을 입력하면 해당 요일, 반의 시간표 제공

🔢 반 입력하면 해당 반의 시간표 제공

❓️
    n반 리스트 = [월,화,수,목,금]
    월화수목금은 n반의 요일의 시간표에 대응하는 리스트.(리스트 말고 튜플이 더 괜찮을것같기도 함)
        ㄴ 어케하는거냐
    반에 해당하는 값을 받은 뒤 if ~elif 사용해서 8반까지 할당
    함수에 변수 2개(요일,반) 받은 뒤에 해당 반과 요일에 맞는 시간표를 출력

예외처리는 할 수 있는데까지 해놓기(반에 실수 넣거나 요일에 수 넣거나 등 대비)

'''

#  날짜 모듈
import datetime

nowtime = datetime.datetime.today()  #  현재 시각


#nowtime = datetime.datetime(2022, 9, 29, 17, 50)  #  코드 확인용

TodayDateStr = datetime.datetime.strftime(nowtime, '%Y-%m-%d')  #  오늘 날짜를 '2022-11-17' 꼴로 나타냄
TodayYoilInt = int(datetime.datetime.strftime(nowtime, '%w'))  #  오늘의 요일을 1~7로 나타냄
nowtimehour = int(datetime.datetime.strftime(nowtime, '%H'))

#  각 요일에 입력될 값 저장
Wol = ['월','월요일']
Hwa = ['화','화요일']
Su = ['수','수요일']
Mok = ['목','목요일']
Geum = ['금','금요일']
To = ['토','토요일']
Il = ['일','일요일']
nextD = {
    '' : '값을 입력하지 않으',
    ' ' : '공백을 입력하'
}

Week = [Wol,Hwa,Su,Mok,Geum,To,Il]  #  한 주의 요일을 배열로 저장
TodayYoilStr = Week[TodayYoilInt-1][1]  #  오늘의 요일을 x요일 꼴로 나타냄

#  각 반에 입력될 값 저장 
ban = ['1반','2반','3반','4반','5반','6반','7반','8반']
bannum = ['1','2','3','4','5','6','7','8']

#  각 반의 요일별 시간표 리스트
Wol_sch = [
    '0반 그런건 없다',
    ['체육','정보','화학','영듣','수과탐','심국(이)','진로'],
    ['기하','생지','심영','체육','논보1','영듣','여지'],
    ['영듣', '심국(이)', '기하', '보건(최)', '생명', '수과탐', '화학'],
    ['심국(황)','생지','논보1','영어','기하','심영','여지'],
    ['5반있음??'],
    ['6반있음???'],
    ['7반있음?'],
    ['심국(이)','체육','논보1','사문','생과(김)','고전','영어']
]

Hwa_sch = [
    '0반 그런건 없다',
    ['심국','과탐','체육','논보','기하','심영','창체'],
    ['정보','과탐','심국(황)','여지','영어','진로','창체'],
    ['보건(임)','기하','여지','화학','심국(황)','영어','창체'],
    ['여지','과탐','기하','심영','체육','심국(이)','창체'],
    ['5반있음??'],
    ['6반있음???'],
    ['7반있음?'],
    ['고전','한지','심국(이)','생과(김)','정보','수과탐','창체']
]

Su_sch = [
    '0반 그런건 없다',
    ['화학','기하','심영','여지','창체','창체'],
    ['생지','심국(이)','기하','영어','창체','창체'],
    ['체육','심영','여지','정보','창체','창체'],
    ['생지','영어','수과탐','진로','창체','창체'],
    ['5반있음??'],
    ['6반있음???'],
    ['7반있음?'],
    ['수과탐','한지','사문','심국(황)','창체','창체']
]

Mok_sch = [
    '0반 그런건 없다',
    ['심국','기하','영어','수과탐','정보','과탐','여지'],
    ['기하','심영','수과탐','여지','심국(황)','과탐','체육'],
    ['수과탐','영어','기하','생명','심국(이)','여지','화학'],
    ['정보','심국(이)','여지','체육','논보2','과탐','기하'],
    ['5반있음??'],
    ['6반있음???'],
    ['7반있음?'],
    ['체육','사문','고전','영듣','논보2','심영','진로']
]

Geum_sch = [
    '0반 그런건 없다',
    ['심국','과탐','여지','영어','화학','논보','기하'],
    ['수과탐','과탐','정보','기하','생지','심국(이)','논보2'],
    ['심국(황)','기하','생명','진로','정보','심영','체육'],
    ['기하','과탐','영듣','수과탐','생지','심국(황)','정보'],
    ['5반있음??'],
    ['6반있음???'],
    ['7반있음?'],
    ['정보','영어','심영','심국(황)','생과(이)','고전','한지']
]

Week_sch = [Wol_sch,Hwa_sch,Su_sch,Mok_sch,Geum_sch]

#  날짜별 함수 설정
def Wol_Sigan(cls) :
    print(str(cls)+'반의',Wol[1],'시간표 출력\n')
    today = Wol_sch[cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def Hwa_Sigan(cls) :
    print(str(cls)+'반의',Hwa[1],'시간표 출력\n')
    today = Hwa_sch[cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def Su_Sigan(cls) :
    print(str(cls)+'반의',Su[1],'시간표 출력\n')
    today = Su_sch[cls]

    for i in range(0,6) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def Mok_Sigan(cls) :
    print(str(cls)+'반의',Mok[1],'시간표 출력\n')
    today = Mok_sch[cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def Geum_Sigan(cls) :
    print(str(cls)+'반의',Geum[1],'시간표 출력\n')
    today = Geum_sch[cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1


######  수정 필요  ######
def Before18pm(cls) :
    print('아직 18시가 지나지 않았습니다.')
    print(str(cls)+'반의',Week[TodayYoilInt-1][1],'시간표 출력\n')
    today = Week_sch[TodayYoilInt-1][cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def After18pm(cls) :
    print('18시가 지났습니다.')
    print(str(cls)+'반의',Week[TodayYoilInt][1],'시간표 출력\n')
    today = Week_sch[TodayYoilInt][cls]

    for i in range(0,7) :
        print(str(i+1)+'교시 :',today[i])
        i+=1

def nextD_Sigan(cls) :
    if abs(nowtimehour - 7) < 8 :
        Before18pm(cls)


    elif abs(nowtimehour - 7) >= 8 :
        After18pm(cls)
######  수정 필요  ######



#  요일별 함수 할당
def schedule(Yoil,cls) :
    print('\n')
    if Yoil in Wol :
        Wol_Sigan(cls)

    elif Yoil in Hwa :
        Hwa_Sigan(cls)

    elif Yoil in Su :
        Su_Sigan(cls)

    elif Yoil in Mok :
        Mok_Sigan(cls)

    elif Yoil in Geum :
        Geum_Sigan(cls)

    elif Yoil in nextD :
        print(nextD[Yoil]+'셨습니다.') # 아침 10시와 가장 가까운', Week[TodayYoilInt][1]+'의 시간표가 보여집니다.\n')
        nextD_Sigan(cls)
    
    else :
        print('요일을 예시와 같게 입력해주세요.')
    print('\n실행 완료')

#  사용자에게 받는 입력
print('\n시간표를 볼 요일을 적어주세요.\n예)월, 월요일\n오늘은 '+TodayYoilStr+'입니다.')
Yoil = input('\n공백을 입력하거나 입력하지 않을 시 아침 10시와 가장 가까운 날의 시간표가 보여집니다.\n')
cls = input('\n시간표를 볼 반을 적어주세요.\n')


#  cls의 값을 int로 변환
if cls in ban :
    cls = ban.index(cls)-1

elif cls in bannum :
    cls = int(cls)

else :
    print('반을 예시와 같게 입력해주세요.')

#  함수 호출
schedule(Yoil,cls)
'''
print('현재 시각 :',nowtime)
print('오늘 요일 정수 :',TodayYoilInt)
'''
