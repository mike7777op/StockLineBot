from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import FlexSendMessage
from .A_S import a_s


def stock_classify(ac):
    if len(ac) != 0:
        content = ''
        all_class = {'a':'水泥','b':'食品','c':'塑膠','d':'紡織纖維','e':'電機','f':'電器','g':'化學','h':'生技','i':'玻璃','j':'造紙','k':'鋼鐵','l':'橡膠','m':'汽車','n':'半導體','o':'電腦周邊','p':'光電','q':'通信網路','r':'電子零件','s':'電子通路','t':'資訊服務','u':'其他電子','w':'營造','x':'運輸','y':'觀光','z':'金融','A':'百貨','B':'油電燃氣','C':'傳產','D':'其他上市'}
        new_ac = ac[0]
        
        if all_class['a'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                a = all_class['a']
            return content, a
        elif all_class['b'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                b = all_class['b']
            return content, b
        elif all_class['c'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                c = all_class['c']
            return content, c
        elif all_class['d'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # print(rs)
                content += f'{rs}'
                d = all_class['d']
            return content, d
        elif all_class['e'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                e = all_class['e']
            return content, e
        elif all_class['f'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                f =  all_class['f']
            return content, f
        elif all_class['g'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                g = all_class['g']
            return content, g
        elif all_class['h'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                h = all_class['h']
            return content, h
        elif all_class['i'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                I = all_class['i']
            return content, I
        elif all_class['j'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                J = all_class['j']
            return content, J
        elif all_class['k'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                k = all_class['k']
            return content, k
        elif all_class['l'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                l = all_class['l']
            return content, l
        elif all_class['m'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                m = all_class['m']
            return content, m
        elif all_class['n'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                n = all_class['n']
            return content, n
        elif all_class['o'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                o = all_class['o']
            return content, o
        elif all_class['p'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                p = all_class['p']
            return content, p
        elif all_class['q'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                q = all_class['q']
            return content, q
        elif all_class['r'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                #print(rs)
                content += f'{rs}'
                r = all_class['r']
            return content, r
        elif all_class['s'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                ##print(rs)
                content += f'{rs}'
                s = all_class['s']
            return content, s
        elif all_class['t'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                ##print(rs)
                content += f'{rs}'
                t1 = all_class['t']
            return content, t1
        elif all_class['u'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                u = all_class['u']
            return content, u
        elif all_class['w'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(ts)
                content += f'{rs}'
                w = all_class['w']
            return content, w
        elif all_class['x'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                x = all_class['x']
            return content, x
        elif all_class['y'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                y = all_class['y']
            return content, y
        elif all_class['z'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                z = all_class['z']
            return content, z
        elif all_class['A'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                A = all_class['A']
            return content, A
        elif all_class['B'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                B = all_class['B']
            return content, B
        elif all_class['C'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                C = all_class['C']
            return content, C
        elif all_class['D'] in new_ac:
            for j in range(len(ac)):
                rs = ac[j]
                # #print(rs)
                content += f'{rs}'
                D = all_class['D']
            return content, D
        else:
            return None,None
    # elif i == 'nan'and len(ac) != 0:
    #     for j in range(len(ac)):
    #         rs = ac[j]
    #         # #print(rs)
    #         content += f'{rs}'
    #     return content
    else:
        rs = None
        name = None
        # rs = '今天沒有連續五天都漲的股票!'
        return rs, name


def stock_progress(days):
    contents_1 = dict()
    contents_1['type']='carousel'
    contents_2 = dict()
    contents_2['type']='carousel'
    contents_3 = dict()
    contents_3['type']='carousel'
    bubbles1 = []
    bubbles2 = []
    bubbles3 = []
    m = []
    t = a_s(days)
    for i in t:
        ac = t[i]
        m.append(ac)
    new_m = [x for x in m if x != []]
    n=12
    output=[new_m[i:i + n] for i in range(0, len(new_m), n)]
    i = 0
    print('%s 筆資料' % len(output))
    while i < len(output):
        new = output[i]
        # print('%s' %i, new)
        for j in new:
            # print(j)
            # print('%s:' %i, j)
            rs, name = stock_classify(j)
            if rs != None:
                # print("result:",name)
                # print("result:",rs)
                # print(type(rs))
                bubble= {   "type": "bubble",
                            "size": "nano",
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "證劵名稱:",
                                    "color": "#FFFFFF",
                                    "align": "start",
                                    "size": "md",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": name,
                                    "color": "#FFFFFF",
                                    "align": "start",
                                    "size": "md",
                                    "gravity": "center"
                                },
                                ],
                                "backgroundColor": "#353d45",
                                "paddingTop": "19px",
                                "paddingAll": "12px",
                                "paddingBottom": "16px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": rs,
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                    ],
                                    "flex": 1
                                }
                                ],
                                "spacing": "md",
                                "paddingAll": "12px"
                            },
                            "styles": {
                                "footer": {
                                "separator": False
                                }
                            }
                        }
                if i == 0:
                    bubbles1.append(bubble)
                elif i == 1:
                    bubbles2.append(bubble)
                else:
                    bubbles3.append(bubble)
        # print('b1:',bubbles1)
        # print('b2:',bubbles2)
        # print('b3:',bubbles3)
        i+=1
    contents_1['contents']=bubbles1
    contents_2['contents']=bubbles2
    contents_3['contents']=bubbles3
    message1=FlexSendMessage(alt_text='股票整理',contents=contents_1)
    message2=FlexSendMessage(alt_text='股票整理',contents=contents_2)
    message3=FlexSendMessage(alt_text='股票整理',contents=contents_3)
    return message1, message2, message3, len(output)
        
