s1 = 'Pemrograman Python'
s2 = "Pemrograman Python 2"
s3 = '''Pemrograman 
python 3'''
##
s4 = 'testing'
s4[0], s4[1], s4[2]
##
data = 'p001\tspidol\t\t9000\np002\tpensil\t\t6000'
#print(data)
data2 = '\tharga\n' + data
#print(data2)

'''
Membandingkan STRING
'''
a1 = 'python'
a2 = 'PYTHON'
#a1 == a2
#a1 != a2
#a1 < a2

'''
Mengekstrak SubString
'''
x = 'Pemrograman Python dan PyQt'
x1 = x[0:11]
#x1
#len(x1)
##
x2 = x[:11]
x3 = x[:8]
x4 = x[8:]
x5 = x[0:11:2]
x6 = x[0:11:1]
x7 = x[0:11:3]

'''
String dengan format tertentu
'''
t = 'balonku ada %d, meletus %d tinggal %d' % (5,2,3)
#t