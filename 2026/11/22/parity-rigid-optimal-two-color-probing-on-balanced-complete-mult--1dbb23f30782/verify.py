"""Exact checks of two-color resolvent probing on balanced multipartite graphs.
Python 3 standard library only. Empirical checks complement the symbolic proof.
"""
from fractions import Fraction as F
from itertools import product,combinations
from math import comb

count=0

def chk(condition, note=''):
    global count
    count += 1
    if not condition:
        raise AssertionError(f'{note}; check {count}')

def offdiag(q,m,mu):
    N=q*m; d=(q-1)*m
    b=F(1,1)/(mu*(mu+N))
    a=b*F(d,1)/(mu+d)
    return a,b

def variance_for_counts(q,m,mu,ks):
    a,b=offdiag(q,m,mu)
    same_within=sum(comb(k,2)+comb(m-k,2) for k in ks)
    same_cross=sum(ks[i]*ks[j]+(m-ks[i])*(m-ks[j]) for i in range(q) for j in range(i+1,q))
    return 4*(a*a*same_within+b*b*same_cross)

def predicted(q,m,mu):
    a,b=offdiag(q,m,mu)
    if q%2==0:
        return 2*q*m*(m-1)*a*a+q*(q-2)*m*m*b*b
    eps=m%2
    return ((2*q-1)*m*m-2*q*m+eps)*a*a+(q-1)**2*m*m*b*b

def is_predicted_optimal(q,m,ks):
    s=[2*k-m for k in ks]
    if q%2==0:
        return all(abs(v)==m for v in s) and sum(s)==0
    # For m=1 all values are at endpoints, but the class assignment below still covers all optima.
    for j in range(q):
        if abs(s[j]) != (m%2):
            continue
        others=s[:j]+s[j+1:]
        if all(abs(v)==m for v in others) and sum(others)==0:
            return True
    return False

def inverse_of_q(q,m,mu):
    N=q*m; d=(q-1)*m
    M=[[((mu+d) if i==j else (F(-1) if i//m != j//m else F(0))) for j in range(N)] for i in range(N)]
    B=[[M[i][j] for j in range(N)]+[F(int(i==j)) for j in range(N)] for i in range(N)]
    for k in range(N):
        p=next(i for i in range(k,N) if B[i][k])
        B[k],B[p]=B[p],B[k]
        pivot=B[k][k]
        B[k]=[v/pivot for v in B[k]]
        for i in range(N):
            if i==k: continue
            x=B[i][k]
            if x:B[i]=[v-x*w for v,w in zip(B[i],B[k])]
    return [row[N:] for row in B]

for q in range(2,7):
    for m in range(1,5):
        for mu in [F(1,3),F(1),F(7,2),F(13)]:
            vmin=None; optim=[]
            for ks in product(range(m+1),repeat=q):
                if not 0<sum(ks)<q*m:continue
                v=variance_for_counts(q,m,mu,ks)
                if vmin is None or v<vmin: vmin=v;optim=[ks]
                elif v==vmin:optim.append(ks)
            chk(vmin==predicted(q,m,mu),('min',q,m,mu,vmin,predicted(q,m,mu)))
            for ks in optim:chk(is_predicted_optimal(q,m,ks),('false positive',q,m,ks))
            for ks in product(range(m+1),repeat=q):
                if not 0<sum(ks)<q*m:continue
                chk((ks in optim)==is_predicted_optimal(q,m,ks),('classification',q,m,mu,ks))

for q,m in [(2,2),(3,2),(3,3),(4,2),(5,2),(5,3)]:
    for mu in [F(2,3),F(7,2)]:
        G=inverse_of_q(q,m,mu)
        N=q*m; a,b=offdiag(q,m,mu)
        for i in range(N):
            for j in range(i+1,N):
                chk(G[i][j]==(a if i//m==j//m else b),('inverse',q,m,i,j))
        for ks in product(range(m+1),repeat=q):
            if not 0<sum(ks)<N:continue
            plus={i*m+t for i,k in enumerate(ks) for t in range(k)}
            v=4*sum(G[i][j]**2 for i in range(N) for j in range(i+1,N) if ((i in plus)==(j in plus)))
            chk(v==variance_for_counts(q,m,mu,ks),('direct variance',q,m,ks))
print('PASS: %d exact rational checks' %count)
