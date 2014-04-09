'''
This example show fibonacci recursive, and generate a png picture in current working directory
'''
from graphviz import Digraph
dot = Digraph(comment = 'fibonacci')

dot.format = 'png'
cnt = 0
def f(n):
    global cnt
    dot.node(str(n), str(n))
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        cnt+=1
        dot.edge(str(n), str(n-2), label = str(cnt))
        a = f(n-2)

        cnt+=1
        dot.edge(str(n-2), str(n), label = str(cnt), color = 'red')

        cnt+=1
        dot.edge(str(n), str(n-1), label = str(cnt))
        b = f(n-1)

        cnt+=1
        dot.edge(str(n-1), str(n), label = str(cnt), color = 'red')

        return a + b

f(5)
dot.render('fibonacci')
