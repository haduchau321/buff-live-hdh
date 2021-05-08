import requests
from ast import literal_eval
from random import randint


class main_buff(object):
    def find_string(self,s, st, ed):
        if (st in s) and (ed in s):
            if st == '':
                tmp = s
            else:
                tmp = s[(s.find(st) + len(st)):]
            if ed == '':
                return tmp
            elif ed in tmp:
                s = tmp[:(tmp.find(ed))]
                return s
            else:
                return ''
        else:
            return ''

    def __init__(self,cookie):
        jcookies = literal_eval('{"' + cookie.strip().replace('	', '').replace(' ', '').replace(';', '", "').replace('=', '": "') + '"}')
        print(jcookies)
        self.s = requests.session()
        self.s.cookies.update(jcookies)
        self.s.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
        self.s.headers.update({'accept-encoding': 'gzip, deflate, br'})
        self.s.headers.update({'accept-language': 'en-US,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5'})
        self.s.headers.update({'cache-control': 'max-age=0'})
        self.s.headers.update({'content-type': 'application/x-www-form-urlencoded'})
        self.s.headers.update({'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'})
        self.s.headers.update({'sec-ch-ua-mobile': '?0'})
        self.s.headers.update({'sec-fetch-dest': 'document'})
        self.s.headers.update({'sec-fetch-mode': 'navigate'})
        self.s.headers.update({'sec-fetch-site': 'same-origin'})
        self.s.headers.update({'sec-fetch-user': '?1'})
        self.s.headers.update({'upgrade-insecure-requests': '1'})
        self.s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/94.0.202 Chrome/88.0.4324.202 Safari/537.36'})

    def get_data(self):
        data = self.s.get(f'https://www.facebook.com/')
        print(data.text)
        self.jazoest = self.find_string(str(data.text),'<input type="hidden" name="jazoest" value="','"')
        self.fb_dtsg = self.find_string(str(data.text),'<input type="hidden" name="fb_dtsg" value="','"')
        return {'id_sy':self.fb_dtsg,'id_post':self.jazoest}

    def buff(self,fb_dtsg,jazoest,id_video):
        url = 'https://www.facebook.com/video/unified_cvc/'
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        data_buff = {'d':'{"pps":{"m":false,"pf":'+str(random_with_N_digits(6))+',"s":"playing","sa":'+str(random_with_N_digits(7))+'},"ps":{"m":false,"pf":'+str(random_with_N_digits(6))+',"s":"playing","sa":'+str(random_with_N_digits(7))+'},"si":"f5f5cb31c03b4c","so":"tahoe::not_specified_please_fix","vi":"'+id_video+'","tk":"3pBBm0ZZYRQrSLbJ+ApFfHflnGIkTzMQyON55EvXqy011aNrrOS3oE4ru8dqDu4tD965HJkWlcxxbCXXWcw5SQ==","ls":true}',
                    'dpr': '1',
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest
        }
        bd = self.s.post(url,data_buff)
        return {'Phản Hồi':' Thành Công'}
