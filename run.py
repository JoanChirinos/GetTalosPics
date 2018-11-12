import os, webbrowser, time

def go():
    student_id = 211932341
    while (True):
        print(student_id)
        for i in range(20):
            webbrowser.open('http://homer.stuy.edu/~jchirinos/GetTalosPics/get_imgs.py?student_id={}'.format(student_id), new=2)
            student_id += 100
        time.sleep(18)
        os.system("killall -9 'Google Chrome'")
        

go()
