#! /usr/bin/python3

import urllib
import cgi, cgitb
cgitb.enable()

print('Content-type: text/html\n\n')

def get_image(student_id):
    try:
        url = 'https://talos.stuy.edu/static/img/id_pics/{}.jpg'.format(student_id)
        resource = urllib.urlopen(url)
        #print(student_id)

        stuff_read = resource.read()

        #print('{}\n\n'.format(stuff_read))

        if 'not found on this server' in stuff_read:
            #print('failed')
            return
        
        output = open("pics/{}.jpg".format(student_id),"wb")
        output.write(stuff_read)
        output.close()
    except Exception as e:
        print('failed')
        print(student_id)
        print('<br>')
        if hassattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        print('<br><br>')
        return

def main():
    student_id = 210032785
    fs = cgi.FieldStorage()
    new_id = fs.getvalue('student_id', 210032785)
    student_id = int(new_id)
    while (True):
        get_image(student_id)
        student_id += 1
    print('<br><br>Thanks')
    

main()
##get_image(209993641)
##get_image(209993642)
