"""Independent finite-field frequency counts for the rank-three bilinear-form metric.
Run with Python 3 stdlib: python3 verify.py
"""
from decimal import Decimal, getcontext
from itertools import product
from math import log


def gf_tables(q):
    if q in (2,3):
        return [[(a*b)%q for b in range(q)] for a in range(q)], [next((b for b in range(1,q) if a*b%q==1),0) for a in range(q)]
    if q==4:
        def mul(a,b):
            res=0
            for j in range(2):
                if b&(1<<j):res ^= a<<j
            if res&8:res ^= 0b1100  # x^3+x^2 reduction (x^2+x+1)*x
            if res&4:res ^= 0b111   # x^2+x+1
            return res
        tab=[[mul(a,b) for b in range(4)] for a in range(4)]
        assert all(tab[a][next(b for b in range(1,4) if tab[a][b]==1)]==1 for a in (1,2,3))
        return tab,[0]+[next(b for b in range(1,4) if tab[a][b]==1) for a in (1,2,3)]
    raise ValueError('unsupported sample field')


def rank_matrix(flat,m,q,tab,inv):
    a=[list(flat[i*3:i*3+3]) for i in range(m)]
    rk=0
    for col in range(3):
        pivot=next((i for i in range(rk,m) if a[i][col]!=0),None)
        if pivot is None:continue
        a[rk],a[pivot]=a[pivot],a[rk]
        if q==4:
            scalar=inv[a[rk][col]]
            a[rk]=[tab[scalar][x] for x in a[rk]]
            for i in range(rk+1,m):
                factor=a[i][col]
                if factor:a[i]=[x^tab[factor][y] for x,y in zip(a[i],a[rk])]
        else:
            scalar=inv[a[rk][col]]
            a[rk]=[(scalar*x)%q for x in a[rk]]
            for i in range(rk+1,m):
                factor=a[i][col]
                if factor:a[i]=[(x-factor*y)%q for x,y in zip(a[i],a[rk])]
        rk+=1
    return rk


def predicted(q,m,s):
    Q=q**m
    a=q*q+q+1
    if s==1:
        return (Q*(q+1)-a, Q*Q-Q*(q+1)**2+q*a, -Q*Q+Q*q*(q+1)-q**3)
    if s==2:
        return (Q-a, -(q+1)*Q+q*a, q*Q-q**3)
    if s==3:
        return (-a,q*a,-q**3)
    raise ValueError


def enumerate_frequencies(q,m):
    tab,inv=gf_tables(q)
    data=[[0]*4 for _ in range(3)]
    cubic=[[[0]*3 for _ in range(4)] for _ in range(3)] if q==3 else None
    for flat in product(range(q),repeat=3*m):
        r=rank_matrix(flat,m,q,tab,inv)
        for s in (1,2,3):
            trace=sum(flat[3*i+i] if i<s else 0 for i in range(s))
            if q==2: character=1 if trace%2==0 else -1
            elif q==3:
                character=trace%3
            elif q==4:
                arg=0
                for i in range(s):arg ^= flat[3*i+i]
                character=1 if arg in (0,1) else -1
            if q==3:
                cubic[s-1][r][character]+=1
            else:data[s-1][r]+=character
    if q==3:
        for s in (1,2,3):
            for r in range(4):
                count=cubic[s-1][r]
                assert count[1]==count[2],(s,r,count)
                data[s-1][r]=count[0]-count[1]
    for s in (1,2,3):
        assert tuple(data[s-1][1:])==predicted(q,m,s),(q,m,s,data[s-1],predicted(q,m,s))
    return data


def rank_count(q,m,s):
    if s==0:return 1
    num=1
    den=1
    for i in range(s):
        num*= (q**3-q**i)*(q**m-q**i)
        den*= q**s-q**i
    assert num%den==0
    return num//den


def root_decimal(q,m):
    getcontext().prec=65
    D=Decimal
    Q=D(q)**m;a=D(q*q+q+1)
    l2=D(2).ln();l3=D(3).ln()
    def f(t):
        tw=(l2*t).exp();thr=(l3*t).exp()
        return Q*(1+D(q)*thr-D(q+1)*tw)-a+D(q)*a*tw-D(q)**3*thr
    lo,hi=D(0),D(1)
    assert f(lo)==-1 and f(hi)>0
    for _ in range(225):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    root=(lo+hi)/2
    assert abs(f(root))<D('1e-46')
    return root


def main():
    checks=[]
    for q,m in [(2,3),(2,4),(3,3),(4,3)]:
        dat=enumerate_frequencies(q,m)
        assert sum(rank_count(q,m,s) for s in range(4))==q**(3*m)
        b=root_decimal(q,m)
        end=q**(3*m)-1-rank_count(q,m,2)
        assert 0<b<1 and end>0
        checks.append((q,m,str(b)[:20],rank_count(q,m,2),end,dat))
    for q,m in [(2,5),(2,9),(3,5),(5,4),(7,4),(11,4),(17,3)]:
        b=root_decimal(q,m)
        assert 0<b<1
        assert sum(rank_count(q,m,s) for s in range(4))==q**(3*m)
        checks.append((q,m,str(b)[:20],rank_count(q,m,2),q**(3*m)-1-rank_count(q,m,2),'formula-only'))
    print('BILINEAR_THREE_NEGATIVE_TYPE_PASS')
    for entry in checks:print('q,m,beta,endpoint_nullity,embedding_dim,data:',entry)

if __name__=='__main__':main()
