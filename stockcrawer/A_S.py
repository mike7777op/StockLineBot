from .stockcrawer import *

def function(jj):
    for i in jj:
        # print(i)
        # print(type(i))
        return i

def A_s(days):
    r = ss_main(days)
    x = r.split(",")
    # print(x)
    x_list = list(x)
    # print(x_list)
    # print(type(x_list))

    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    I = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t1 = []
    u = []
    w = []
    x = []
    y = []
    z = []
    A = []
    B = []
    C = []
    D = []
    nan = []

    # all_class = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'I':I,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t1':t1,'u':u,'z':z,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5,'nan':nan}

    all_class = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'I':I,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t1':t1,'u':u, 'w':w, 'x':x, 'y':y, 'z':z,'A':A,'B':B,'C':C,'D':D, 'nan':nan}
    
    t = x_list

    for i in range(len(t)):
        # print(t[i])
        if 'nan' in t[i]:
            new = t[i].replace('nan', '個股權證或上櫃')
            # nan.append(new)
            # function(nan)
        
        elif 'a' in t[i]:
            new = t[i].replace('a', '水泥')
            a.append(new)
            
        
        elif 'b' in t[i]:
            new = t[i].replace('b', '食品')
            b.append(new)
        
        elif 'c' in t[i]:
            new = t[i].replace('c', '塑膠')
            c.append(new)

        elif 'd' in t[i]:
            new = t[i].replace('d', '紡織纖維')
            d.append(new)


        elif 'e' in t[i]:
            new = t[i].replace('e', '電機')
            e.append(new)

        elif 'f' in t[i]:
            new = t[i].replace('f', '電器')
            f.append(new)

        elif 'g' in t[i]:
            new = t[i].replace('g', '化學')
            g.append(new)
        
        elif 'h' in t[i]:
            new = t[i].replace('h', '生技')
            h.append(new)
        
        elif 'I' in t[i]:
            new = t[i].replace('i', '玻璃')
            I.append(new)

        elif 'j' in t[i]:
            new = t[i].replace('j', '造紙')
            j.append(new)

        elif 'k' in t[i]:
            new = t[i].replace('k', '鋼鐵')
            k.append(new)

        elif 'l' in t[i]:
            new = t[i].replace('l', '橡膠')
            l.append(new)

        elif 'm' in t[i]:
            new = t[i].replace('m', '汽車')
            m.append(new)

        elif 'n' in t[i]:
            new = t[i].replace('n', '半導體')
            n.append(new)

        elif 'o' in t[i]:
            new = t[i].replace('o', '電腦周邊')
            o.append(new)

        elif 'p' in t[i]:
            new = t[i].replace('p', '光電')
            p.append(new)

        elif 'q' in t[i]:
            new = t[i].replace('q', '通信網路')
            q.append(new)
            
        elif 'r' in t[i]:
            new = t[i].replace('r', '電子零件')
            r.append(new)

        elif 's' in t[i]:
            new = t[i].replace('s', '電子通路')
            s.append(new)

        elif 't' in t[i]:
            new = t[i].replace('t', '資訊服務')
            t1.append(new)
        
        elif 'u' in t[i]:
            new = t[i].replace('u', '其他電子')
            u.append(new)

        elif 'w' in t[i]:
            new = t[i].replace('w', '營造')
            w.append(new)

        elif 'x' in t[i]:
            new = t[i].replace('x', '運輸')
            x.append(new)

        elif 'y' in t[i]:
            new = t[i].replace('y', '觀光')
            y.append(new)
        
        elif 'z' in t[i]:
            new = t[i].replace('z', '金融')
            z.append(new)

        elif 'A' in t[i]:
            new = t[i].replace('A', '百貨')
            A.append(new)

        elif 'B' in t[i]:
            new = t[i].replace('B', '油電燃氣')
            B.append(new)
        
        elif 'C' in t[i]:
            new = t[i].replace('C', '傳產')
            C.append(new)

        elif 'D' in t[i]:
            new = t[i].replace('D', '其他上市')
            D.append(new)

    return all_class

def a_s(days):
    t = A_s(days)
    return t
