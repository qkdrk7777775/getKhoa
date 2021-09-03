# getKhoa

This package is Khoa download using api.

## Installation
The missImputeTS package For installation execute in python:

```
pip install getKhoa
```

import getKhoa
a=getKhoa.GetData(key='BehDhlIyPwKozERUb2BYQ==',
               station_type_list=['조위관측소','해양관측소','해양과학기지','해양관측부이'])

st=a.stations
st#관측소 위치정보, 목록 및 ID정보

## 관측자료 다운로드 
"""
특정 위치(DT_0001:가덕도)의 특정 기간동안(2021-02-01 ~ 2021-03-01) 시간단위 조위관측소 예측조위 자료 추출
"""
df,err=a.downloadApi(start_date='20210201',end_date='20210301',
                     station_list=['DT_0001'],data_type_list=['tideObsPre'])

"""
특정 위치(DT_0001:가덕도)의 특정 기간동안(2021-03-01 ~ 2021-03-01) 분단위 조위관측소 예측조위 자료 추출
"""
df,err=a.downloadApi(start_date='20210301',end_date='20210301',
                     station_list=['DT_0001'],data_type_list=['tideObsPre'],
                     time_type='min')

"""
특정 위치(DT_0001:가덕도)의 특정 기간동안(2021-03-01 ~ 2021-03-01) 분단위 
(조위관측소 예측조위, 실측 염분, 실측 수온) 자료 추출
"""
df,err=a.downloadApi(start_date='20210301',end_date='20210301',
                     station_list=['DT_0001'],data_type_list=['tideObsPre','tideObsSalt','tideObsAirTemp'],
                     time_type='min')

##파고
df,err=a.getData('obsWaveHight',add_query=f'&ObsCode=TW_0062&Date=20160601')
df,err=a.downloadApi(start_date='20160601',end_date='20160601',
                     station_list=['TW_0062'],data_type_list=['obsWaveHight'],time_type='min')


#조화상수
df,err=a.getData('tideObsHar',add_query=f'&ObsCode=DT_0001&Date=20160601')

#Tide Bed 에측 조위
df,err=a.getMetaData('tideBedPre',add_query=f'&ObsLon=128.3845&ObsLat=33.9518&Date=20130101')

#따로 쿼리 
""" 
downloadApi
    start_date : 다운로드 받을 자료의 처음시간
    end_date   : 다운로드 받을 자료의 끝시간
    and_query  : URL에 추가로 붙을 query
    time_type : 다운로드 받을 자료의 시간해상도(H : 시간단위, min : 분단위). (default = H)
    station_list : 다운받을 지점의 지점명. class에 잇는 stations로 확인 가능. 
                   빈 리스트는, 전체지점을 의미. default=[]
    data_type_list : 다운로드 받을 자료 유형. 
                    default=['tideObs','tideObsTemp','tideObsSalt',
                             'tideObsAirTemp','tideObsAirPres','tideObsWind']
                    # 조위관측소 실측조위, 조위관측소 수온, 조위관측소 염분, 
                    # 조위관측소, 기온, 조위관측소 기압, 조위관측소 풍향/풍속

        #조위
        'tideObs':'조위관측소 실측조위'
        'tideObsPre':'조위관측소 예측 조위'
        'tideCurPre':'조위관측소 실측&예측 조위'
        'tideObsPreTab':'조석예보'
        'tideObsHar':'조위관측소 조화상수'
        'tideBedPre':'tideBED 예측조위'
        'tideShortLong':'비실시간 장단기 조위'
        #파고
        'obsWaveHight':'파고관측망(해양관측소, 종합해양과학기지, 해양관측부이) 실측파고'
        #조류
        'tidalBu':'해양관측부이 실측조류'
        'fcTidalCurrent':'조류예보'
        'tidalPreTab':'조류예보 최강 창낙조 및 전류'
        #해수유동
        'tideHfRadar':'해수유동 관측소 실측 유향 유속'
        'romsTemp':'황동중국해(모델)예측 유향 유속(Roms)'
        'KIOPS':'통합정보(모델) 예측 유향 유속'
        'tidalCurrentArea':'수치조류도 예측 유향 유속/면단위 수치조류도 예측 유향유속(geojson)'
        'tidalCurrentPoint':'수치조류도 지점별 최강창낙조'
        #수온
        'tideObsTemp':'조위관측소 실측수온'
        'tidalBuTemp':'해양관측부이 실측수온'
        'tideObsSalt':'조위관측소 실측염분'
        'tideObsAirTemp':'조위관측소 실측 기온'
        'tidalBuAirTemp':'해양관측부이 실측 기온'
        'tideObsAirPres':'조위관측소 실측 기압'
        'tidalBuAirPres	':'해양관측부이 실측 기압'
        #풍향/푹속
        'tideObsWind':'조위관측소 실측 풍향/풍속'
        'tidalBuWind':'해양관측부이 실측 풍향/풍속'
        #해무
        'seafog':'해무관측소 실측 해무'
        ...
"""

