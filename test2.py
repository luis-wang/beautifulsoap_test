#coding:utf8
'''

'''

from urllib import quote,unquote


s = r'王旭东abc'
q = quote(s)
print type(q), q

print 'unquote = ',unquote(q)


