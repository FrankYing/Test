import pickle as p
import requests


a = 0


def my_p(dic, i):
    global a
    for k, v in dic.items():
        if isinstance(v, dict):
            print(k, ':')
            a += 1
            my_p(v, a)
        else:
            print('-' * i, k, '->', v)


it = p.load(open('..\\itchat.pkl', 'rb'))
my_p(it, a)


# s = requests.session()
# s.get()
# s.request()
