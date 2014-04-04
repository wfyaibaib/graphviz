from graphviz import Digraph
dot = Digraph(comment = 'test')
dot.node('A', 'a')
dot.node('B', 'b')
dot.node('L', 'l')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint = 'false')
dot.format = 'png'
dot.render('test.gv')

