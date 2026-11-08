"""Check the exact centralizer-chart reduction in prime characteristics 2,3,5.
Standard Python 3 only.
"""
from itertools import product

def multiply(X,Y,p):
    return tuple(sum(X[3*i+k]*Y[3*k+j] for k in range(3))%p for i in range(3) for j in range(3))

def chart(a,c,d):
    return (0,a,c,0,0,0,0,d,0)

def check(p,r):
    I=(0,1,0,0,0,0,0,0,0)
    space=list(product(range(p), repeat=3))
    sqzero=[v for v in space if multiply(chart(*v),chart(*v),p)==(0,)*9]
    assert len(sqzero)==p*(2*p-1)
    solutions=0
    for vs in product(sqzero, repeat=r-1):
        matrices=(I,)+tuple(chart(*v) for v in vs)
        commute=all(multiply(X,Y,p)==multiply(Y,X,p) for X in matrices for Y in matrices)
        reduced=(all(v[1]==0 for v in vs) or all(v[2]==0 for v in vs))
        assert commute==reduced,(p,r,vs,commute,reduced)
        if commute: solutions+=1
    want=p**(r-1)*(2*p**(r-1)-1)
    assert solutions==want,(p,r,solutions,want)
    print(f'p={p}, r={r}: fixed-nonzero-chart solutions={solutions}, union-of-coordinate-spaces PASS')

if __name__=='__main__':
    for p,r in ((2,2),(2,3),(2,4),(3,2),(3,3),(5,2),(5,3)):
        check(p,r)
    print('ALL_TRANSVERSE_LOCAL_CHART_CHECKS_PASS')
