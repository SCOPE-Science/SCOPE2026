#!/usr/bin/env python3
"""Independent projective-point/line-incidence enumeration for Fermat surfaces.
Usage: python verify_point_incidence.py
No external dependencies. Finite fields of prime or quadratic order only.
"""
from collections import Counter


def field(p, nonsquare=None):
    q=p if nonsquare is None else p*p
    table=[[0]*q for _ in range(q)]
    for x in range(q):
        a,b=(x%p,x//p) if nonsquare is not None else (x,0)
        for y in range(q):
            c,d=(y%p,y//p) if nonsquare is not None else (y,0)
            if nonsquare is None:
                table[x][y]=(a*c)%p
            else:
                table[x][y]=((a*c+nonsquare*b*d)%p)+p*((a*d+b*c)%p)
    add=[[0]*q for _ in range(q)]
    for x in range(q):
        for y in range(q):
            if nonsquare is None:
                add[x][y]=(x+y)%p
            else:
                add[x][y]=((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def exp(x,n):
        r=1
        while n:
            if n&1:r=table[r][x]
            x=table[x][x];n>>=1
        return r
    return q,add,exp


def point_spectrum(p, nonsquare=None):
    q,add,exp=field(p,nonsquare)
    assert (q-1)%4==0
    d=(q-1)//4
    f=[exp(x,d) for x in range(q)]
    pairs=[((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]
    cnt=Counter(); not_on=[]
    def addpoint(x):
        z=add[add[f[x[0]]][f[x[1]]]][add[f[x[2]]][f[x[3]]]]
        if z:return
        incidence=0
        for ((i,j),(k,l)) in pairs:
            if add[f[x[i]]][f[x[j]]]==0 and add[f[x[k]]][f[x[l]]]==0:
                def ratio_count(a,b):
                    if b==0:return d if a==0 else 0
                    return 1 if exp(table_inv[b][a],d)==p-1 else 0
                incidence+=ratio_count(x[i],x[j])*ratio_count(x[k],x[l])
        cnt[incidence]+=1
        if incidence==0 and len(not_on)<3:not_on.append(x)
    # Build inversion quotient table for line ratios, outside enumeration loops.
    mul=field_mul_table(p,nonsquare)
    inv=[0]*q
    for a in range(1,q):
        inv[a]=next(b for b in range(1,q) if mul[a][b]==1)
    table_inv=[[mul[inv[b]][a] if b else 0 for a in range(q)] for b in range(q)]
    for a in range(q):
        for b in range(q):
            for c in range(q):addpoint((1,a,b,c))
    for b in range(q):
        for c in range(q):addpoint((0,1,b,c))
    for c in range(q):addpoint((0,0,1,c))
    addpoint((0,0,0,1))
    total=9*d**3+6*d
    off=0
    if p==3:off=4*d*d
    if p==5:off=4*d**3+12*d*d
    assert sum(cnt.values())==total+off,(q,cnt,total,off)
    expected=Counter({1:6*d**3,2:3*d**3,d:6*d,0:off})
    if d==2:expected[2]=3*d**3+6*d
    if d==1:raise ValueError('degree one excluded')
    expected={j:n for j,n in expected.items() if n}
    assert dict(cnt)==expected,(q,cnt,expected)
    print(f'q={q}, d={d}, char={p}, counts={dict(sorted(cnt.items()))}, off-examples={not_on}')


def field_mul_table(p,nonsquare):
    q=p if nonsquare is None else p*p
    if nonsquare is None:return [[a*b%p for b in range(q)] for a in range(q)]
    return [[((a%p*b%p+nonsquare*(a//p)*(b//p))%p)+p*((a%p*(b//p)+(a//p)*(b%p))%p) for b in range(q)] for a in range(q)]

if __name__=='__main__':
    for p, c in [(3,2),(13,None),(17,None),(5,2),(29,None),(37,None),(7,3)]:
        point_spectrum(p,c)
    print('VERIFY_POINT_INCIDENCE_OK')
