"""Independent exact integer-characteristic-polynomial comparison.
Requires sympy. Run: python check_spectral.py.
"""
import sympy as s

def block_ones(a,b):return s.ones(a,b)

def graph_f():
    A=s.zeros(33)
    for k in range(16):
        i,j=1+2*k,2+2*k
        for u,v in ((0,i),(0,j),(i,j)):
            A[u,v]=A[v,u]=1
    return A

def graph_h():
    A=s.zeros(33)
    for i in range(3):
        for j in range(3):
            if i!=j:A[i,j]=1
        for j in range(3,8):A[i,j]=A[j,i]=1
    for i in range(5):
        for j in range(5):
            if i!=j:A[3+i,8+j]=A[8+j,3+i]=1
    for i in range(10):
        A[13+2*i,14+2*i]=A[14+2*i,13+2*i]=1
    return A

x=s.symbols('x');expected=(x+1)**16*(x-1)**15*(x*x-x-32)
for name,make in [('friendship F16',graph_f),('exceptional plus 10 K2',graph_h)]:
    p=make().charpoly(x).as_expr()
    assert s.expand(p-expected)==0
    print(name,'matches common exact integer characteristic polynomial')
print('PASS')
