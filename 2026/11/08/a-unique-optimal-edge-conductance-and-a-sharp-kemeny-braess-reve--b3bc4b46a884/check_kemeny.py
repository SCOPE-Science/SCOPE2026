"""Exact independent check of a weighted graph's discrete-time Kemeny constant.
Run: python check_kemeny.py (Python 3 standard library only).
"""
from fractions import Fraction as F
from itertools import product

def inverse(M):
    n=len(M)
    Z=[list(M[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if Z[i][k])
        Z[k],Z[p]=Z[p],Z[k]
        q=Z[k][k]
        Z[k]=[z/q for z in Z[k]]
        for i in range(n):
            if i==k: continue
            t=Z[i][k]
            if t:
                Z[i]=[x-t*y for x,y in zip(Z[i],Z[k])]
    return [r[n:] for r in Z]

def graph_kemeny(a,b,w):
    """a>=3, b>=1, w>=0, K_ab plus weighted edge 0-1."""
    n=a+b
    W=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(a):
        for j in range(a,n): W[i][j]=W[j][i]=F(1)
    W[0][1]=W[1][0]=F(w)
    d=[sum(row) for row in W]
    assert all(d)
    P=[[W[i][j]/d[i] for j in range(n)] for i in range(n)]
    pi=[t/sum(d) for t in d]
    Z=inverse([[F(int(i==j))-P[i][j]+pi[j] for j in range(n)] for i in range(n)])
    return sum(Z[i][i] for i in range(n))-1

def delta(a,b,w):
    w=F(w)
    return w*(4*(a-2)*w-3*b)/(2*(b+2*w)*(a*b+w))

def main():
    count=0
    for a,b,w in product(range(3,8),range(1,6),[F(0),F(1,5),F(1,2),F(1),F(2),F(3),F(7)]):
        v=graph_kemeny(a,b,w)
        direct=F(a+b)-F(3,2)+delta(a,b,w)
        assert v==direct,(a,b,w,v,direct)
        count+=1
    assert delta(3,1,F(1))==F(1,24)
    assert delta(3,1,F(1,4))<0
    assert delta(3,1,F(3,4))==0
    assert delta(3,1,F(1))>0
    assert delta(4,2,F(3,4))==0
    for a,b in product(range(3,12),range(1,8)):
        for x in [F(1,8),F(1,2),F(3,2),F(5)]:
            assert delta(a,b,b*x)==x*(4*(a-2)*x-3)/(2*(1+2*x)*(a+x))
    print('PASS: 175 exact full-matrix inversions; 252 rational scaling identities; threshold boundary tests.')
if __name__=='__main__':main()
