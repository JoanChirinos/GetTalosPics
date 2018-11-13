import os, webbrowser, time, urllib.request

def go():
##    student_id = 211938341
    student_id = 230000000
    while (True):
        print(student_id)
##        for i in range(20):
##            webbrowser.open('http://homer.stuy.edu/~jchirinos/GetTalosPics/get_imgs.py?student_id={}'.format(student_id), new=2)
        url = 'http://homer.stuy.edu/~jchirinos/GetTalosPics/get_imgs.py?student_id={}'.format(student_id)
        try:
            urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            print('FAILED AT ~ {}'.format(student_id))
        student_id += 1
##        time.sleep(18)
##        os.system("killall -9 'Google Chrome'")


def new_go():
    student_id = 209993642
    url = 'http://homer.stuy.edu/~jchirinos/GetTalosPics/get_imgs.py?student_id={}'.format(student_id)
    f = urllib.request.urlopen(url)
    print(f.read())

go()
