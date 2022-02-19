import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime
import time
from collections import Counter

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def crawl(date):
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL', headers=head)
    ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                            for i in r.text.split('\n') 
                                            if len(i.split('",')) == 17]).replace('=', '')), header=0)
    ret = ret.set_index(keys=['證券代號','證券名稱'])
    ret['成交金額'] = ret['成交金額'].str.replace(',','')
    ret['成交股數'] = ret['成交股數'].str.replace(',','')
    ret["收盤價"] =  ret["收盤價"].str.replace(',','')
    ret["開盤價"] =  ret["開盤價"].str.replace(',','')
    ret = ret.replace("--", "0")
    return ret

def analysis(data_1):
    data_1 = pd.DataFrame(data_1)
    data_1["收盤價"]=pd.to_numeric(data_1["收盤價"], errors='coerce')
    data_1["開盤價"]=pd.to_numeric(data_1["開盤價"], errors='coerce')
    data_1 = data_1.assign(op_clo=data_1["收盤價"]-data_1["開盤價"])
    data_1 = data_1[pd.to_numeric(data_1['開盤價'], errors='coerce') < 50]
    data_1.loc[data_1['op_clo'] > 0, 'result'] = 1
    data_1.loc[data_1['op_clo'] == 0, 'result'] = 0
    data_1.loc[data_1['op_clo'] < 0, 'result'] = -1
    return data_1
    

def scrape(days):
    data = {}
    t=0
    n_days = days
    print('day:',days)
    date = datetime.datetime.now()
    count_day=0
    fail_count = 0
    allow_continuous_fail_count = 10
    date_1 = []

    while t < n_days:
        print('parsing', date)
        # 使用 crawPrice 爬資料
        try:
            # 抓資料
            data_1 = crawl(date)
            print('success!')
            data_1 = analysis(data_1)
            data[date.date()] = data_1['result']
            date_1.append(date.date().weekday()+1)
            t+=1
            fail_count = 0
        
        except:
            # 假日爬不到
            print('fail! check the date is holiday')
            if date.date().weekday()+1 != 6 and date.date().weekday()+1 != 7:
                print('fail on weekday')
                fail_count += 1
                if fail_count == allow_continuous_fail_count:
                    raise ValueError('The count is over!')
                    break
                else:
                 time.sleep(10)
                 date += datetime.timedelta(days=1)
            
        # 減一天
        print(fail_count)
        date -= datetime.timedelta(days=1)
        time.sleep(5)

    return data, date_1
    
def day(data, days):
    day_f = 5
    data = pd.DataFrame(data=data)
    datelist = list(data)
    if days == day_f:
        print('五天')
        d1 = datelist[0]
        d2 = datelist[1]
        d3 = datelist[2]
        d4 = datelist[3]
        d5 = datelist[4]

        All_sum = {}
        All_sum = pd.DataFrame(All_sum)
        All_sum['a'] = data[d1] + data[d2] + data[d3] + data[d4] + data[d5]

        return All_sum
    else:
        print('三天')
        d1 = datelist[0]
        d2 = datelist[1]
        d3 = datelist[2]

        All_sum = {}
        All_sum = pd.DataFrame(All_sum)
        All_sum['a'] = data[d1] + data[d2] + data[d3]

        return All_sum

def ss_main(days):
    data, date = scrape(days)
    All_sum = day(data,days)
    A_l = list(All_sum)
    All_sum = All_sum.sort_values(A_l)
    All_sum = All_sum.dropna()

    Top_infive = {}
    Top_infive = pd.DataFrame(Top_infive)
    Last_infive = {}
    Last_infive = pd.DataFrame(Last_infive)

    maxs = All_sum['a'].max()
    mins = All_sum['a'].min()
    maxs = int(maxs)
    mins = int(mins)

    All_sum.loc[All_sum['a'] > maxs-1, 'b'] = maxs
    Top_infive['a'] = All_sum['b']
    Top_infive = Top_infive.dropna()
    All_sum.loc[All_sum['a'] < mins+1, 'c'] = mins
    Last_infive['a'] = All_sum['c']
    Last_infive = Last_infive.dropna()

    url = 'https://raw.githubusercontent.com/mike7777op/stock_csv/main/sc4.csv'
    sc4 = pd.read_csv(url, encoding='latin', engine='python')
    sc4['ÃÒ?¥N¸¹'] = sc4['ÃÒ?¥N¸¹'].astype(str)
    Top_infive.reset_index(inplace=True)
    Top_merge = pd.merge(Top_infive, sc4, how='left', left_on='證券代號', right_on='ÃÒ?¥N¸¹')
        

    content = ''
    for i in range(len(Top_merge)):

        t1 = Top_merge['證券代號'][i]
        t2 = Top_merge['證券名稱'][i]
        t3 = Top_merge['a_x'][i].astype(int)
        t4 = Top_merge['a_y'][i]
        content += f"{t2}\n證劵分類:{t4}\n證劵代號:{t1}\n連續漲:{t3}天 \n\n,"

    return content
