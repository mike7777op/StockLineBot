from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import UserInfo, UserInfo2
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    QuickReplyButton,
    QuickReply
)
from .stockcrawer import *
from apscheduler.schedulers.background import BackgroundScheduler 
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import time
from .Flex_Msg import stock_progress

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


def stock_flex_3():
    days_t = 3 
    message_t = []
    t1,t2,t3, len_t = stock_progress(days_t)
    if len_t == 1:
        message_t.append(t1)
    elif len_t == 2:
        message_t.append(t1)
        message_t.append(t2)
    else:
        message_t.append(t1)
        message_t.append(t2)
        message_t.append(t3) 

    return message_t

def stock_flex_5():
    days_f = 5 
    message_f = []
    f1,f2,f3, len_t = stock_progress(days_f)
    if len_t == 1:
        message_f.append(f1)
    elif len_t == 2:
        message_f.append(f1)
        message_f.append(f2)
    else:
        message_f.append(f1)
        message_f.append(f2)
        message_f.append(f3)

    return message_f

def stock_srawer():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print('stock crawer work')
    # uid = UserInfo2.objects.filter(uid=uid)
    uid = UserInfo2.objects.all()
    uid = uid.values()
    message_3 = stock_flex_3()
    message_5 = stock_flex_5()
    for uid in uid:
        days = uid['days']
        print(days)
        my_uid = uid['uid']
        print(my_uid)
    #     # line_bot_api.push_message(uid,message_t)
        if days == 5:
            line_bot_api.push_message(my_uid,message_5)
            # print(my_uid,'in five')
        else:
            line_bot_api.push_message(my_uid,message_3)
            # print(my_uid,'in three')

sched = BackgroundScheduler(timezone="Asia/Taipei")
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13, minute=58)
def stock_time_4():
    print('The schedule work!')
    stock_srawer()
        
sched.start()
 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # ???????????????
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # ?????????????????????
                message = []
                uid = event.source.user_id
                # uid = '123456'
                profile = line_bot_api.get_profile(uid)
                name = profile.display_name
                if event.message.text == '???????????????':
                    data = UserInfo2.objects.filter(uid=uid).exists()
                    print(data)
                    if data == True:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='???????????????!'))
                    else:
                        UserInfo2.objects.create(uid=uid, name=name,days=5)
                        reply_arr = []
                        reply_arr.append(TextSendMessage(text="??????????????????!"))
                        reply_arr.append(
                            TemplateSendMessage(
                            alt_text='Buttons templates',
                            template=ButtonsTemplate(
                                title='??????????????????',
                                text='???????????????',
                                actions=[
                                    PostbackTemplateAction(
                                        label='??????',
                                        text='??????',
                                        data='A&3'
                                    ),
                                    PostbackTemplateAction(
                                        label='??????',
                                        text='??????',
                                        data='A&5'
                                    )
                                ]
                            )
                        ))
                        line_bot_api.reply_message(event.reply_token, reply_arr)
            
                elif event.message.text == "????????????":
                    days_f = 5
                    days_t = 3 
                    message_f = []
                    message_t = []
                    my_uid = UserInfo2.objects.filter(uid=uid)
                    my_uid = list(my_uid.values())
                    for i in my_uid:
                        day = i['days']
                        t1,t2,t3, len_t = stock_progress(day)
                        if day == 3:
                            if len_t == 1:
                                message_t.append(t1)
                            elif len_t == 2:
                                message_t.append(t1)
                                message_t.append(t2)
                            else:
                                message_t.append(t1)
                                message_t.append(t2)
                                message_t.append(t3)
                            for j in message_t:
                                if j:
                                    line_bot_api.push_message(uid,j)
                                else:
                                    print(i,'is None')
                        else:
                            if len_t == 1:
                                message_f.append(t1)
                            elif len_t == 2:
                                message_f.append(t1)
                                message_f.append(t2)
                            else:
                                message_f.append(t1)
                                message_f.append(t2)
                                message_f.append(t3)
                            for j in message_f:
                                if j:
                                    line_bot_api.push_message(uid,j)
                                else:
                                    print(i,'is None')

                elif event.message.text == '????????????':
                    line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
                            alt_text='Buttons templates',
                            template=ButtonsTemplate(
                                title='????????????',
                                text='???????????????',
                                actions=[
                                    PostbackTemplateAction(
                                        label='??????',
                                        text='??????',
                                        data='A&3'
                                    ),
                                    PostbackTemplateAction(
                                        label='??????',
                                        text='??????',
                                        data='A&5'
                                    )
                                ]
                            )
                        ))

            # ?????????????????????
            elif isinstance(event, PostbackEvent):
                uid = event.source.user_id
                if event.postback.data[0:1] == "A":
                    days = event.postback.data[2:]
                    print(days)
                    UserInfo2.objects.filter(uid=uid).update(days=days)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='????????????!'))

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def clock(request):
    return render(request, 'clock.html')
