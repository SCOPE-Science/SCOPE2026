"""Exact rational checks for random three-pair averaging in a four-type QSO."""
from fractions import Fraction as F
from itertools import product
from math import comb

T=((0,1),(1,2),(0,2))
p0=(F(1,2),F(3,10),F(1,5))
x4_0=F(2,5)
z0=tuple(p-F(1,3) for p in p0)

def swap_average(p,edge):
    a,b=edge
    out=list(p)
    out[a]=out[b]=(p[a]+p[b])/2
    return tuple(out)

def qso(x,edge):
    x4=x[3]
    y=swap_average(x[:3],edge)
    return tuple(2*x4*yj for yj in y)+(x4*x4+(1-x4)*(1-x4),)

def sqnorm(p):
    return sum(v*v for v in p)

for n in range(1,9):
    hist=[0]*n
    count=[[[0]*3 for _ in range(n)] for _ in range(3)]
    squared_sum=F(0)
    fourth_sum=F(0)
    for word in product(range(3),repeat=n):
        p=p0
        x=tuple((1-x4_0)*v for v in p0)+(x4_0,)
        for i in word:
            p=swap_average(p,T[i])
            x=qso(x,T[i])
        normal=tuple(v/(1-x[3]) for v in x[:3])
        assert normal==p
        z=tuple(v-F(1,3) for v in p)
        k=sum(word[j]!=word[j-1] for j in range(1,n))
        unpaired=3-sum(T[word[0]])
        expected=F(3,2)*z0[unpaired]**2 /4**k
        assert sqnorm(z)==expected,(n,word,sqnorm(z),expected)
        assert x[3]==F(1,2)*(1+(2*x4_0-1)**(2**n))
        hist[k]+=1
        count[word[0]][k][word[-1]]+=1
        squared_sum+=expected
        fourth_sum+=expected**2
    assert hist==[3*comb(n-1,k)*2**k for k in range(n)]
    for i in range(3):
        for k in range(n):
            for j in range(3):
                prob=F(1,3)+(-F(1,2))**k*(int(i==j)-F(1,3))
                assert F(count[i][k][j],comb(n-1,k)*2**k)==prob
    moment2=F(1,2)**n*sqnorm(z0)
    moment4=F(1,3)*sum((F(3,2)*z0[3-sum(edge)]**2)**2 for edge in T)*F(3,8)**(n-1)
    assert squared_sum/F(3**n)==moment2
    assert fourth_sum/F(3**n)==moment4
    print('n',n,'words',3**n,'K-hist',hist)
print('RANDOM_QSO_THREE_PROJECTION_ALL_EXACT_OK; all_words=9840, joint_endpoint=PASS, moments_2_4=PASS')
