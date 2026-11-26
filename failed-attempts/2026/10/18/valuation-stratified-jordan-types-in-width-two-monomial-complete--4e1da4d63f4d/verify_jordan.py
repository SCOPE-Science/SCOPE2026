#!/usr/bin/env python3
"""Independent rank and Jordan-type census for multiplication on k[x,y]/(x^2,y^m)."""
from itertools import product
from collections import Counter

def rank_mod(matrix,p):
    rows=[list(map(lambda x:x%p,row)) for row in matrix]
    h=len(rows); w=len(rows[0]) if h else 0
    rr=0
    for c in range(w):
        ii=next((j for j in range(rr,h) if rows[j][c]),None)
        if ii is None: continue
        rows[rr],rows[ii]=rows[ii],rows[rr]
        z=pow(rows[rr][c],-1,p)
        rows[rr]=[(v*z)%p for v in rows[rr]]
        for j in range(h):
            if j!=rr and rows[j][c]:
                x=rows[j][c]; rows[j]=[(a-x*b)%p for a,b in zip(rows[j],rows[rr])]
        rr+=1
        if rr==h:break
    return rr

def product_a(a,b,m,p):
    out=[0]*(2*m)
    for e1 in (0,1):
        for i in range(m):
            ai=a[e1*m+i]
            if not ai:continue
            for e2 in (0,1):
                if e1+e2>1:continue
                for j in range(m-i):
                    out[(e1+e2)*m+i+j] = (out[(e1+e2)*m+i+j]+ai*b[e2*m+j])%p
    return tuple(out)

def val(c,m):
    return next((i for i in range(m) if c[i]),m)

def predicted_ranks(a,m,p):
    alpha=val(a[:m],m);beta=val(a[m:],m)
    ranks=[2*m]
    for t in range(1,m+3):
        if t%p==0 or beta>=alpha:
            d1=d2=t*alpha
        else:
            d1=(t-1)*alpha+beta
            d2=(t+1)*alpha-beta
        ranks.append(max(0,m-d1)+max(0,m-d2))
    return ranks

def partition(ranks):
    return tuple(j for j in range(len(ranks)-2,0,-1) for _ in range(ranks[j-1]-2*ranks[j]+ranks[j+1]))

def hist_predicted(m,p):
    q=p
    weight=lambda v: (q-1)*q**(m-v-1) if v<m else 1
    r=Counter()
    for alpha in range(1,m+1):
        for beta in range(m+1):
            a=[0]*(2*m)
            if alpha<m:a[alpha]=1
            if beta<m:a[m+beta]=1
            r[partition(predicted_ranks(a,m,p))]+=weight(alpha)*weight(beta)
    return r

def run():
    for p,ms in [(2,range(2,8)),(3,range(2,6)),(5,range(2,4)),(7,range(2,3))]:
        for m in ms:
            all_hist=Counter()
            for digits in product(range(p),repeat=2*m-1):
                a=(0,)+digits[:m-1]+digits[m-1:]
                expected=predicted_ranks(a,m,p)
                aa=(1,)+(0,)*(2*m-1)
                observed=[2*m]
                for t in range(1,m+3):
                    aa=product_a(aa,a,m,p)
                    columns=[product_a(aa,tuple(int(k==j) for k in range(2*m)),m,p) for j in range(2*m)]
                    matrix=list(zip(*columns))
                    observed.append(rank_mod(matrix,p))
                if observed!=expected:
                    raise ValueError((p,m,a,observed,expected))
                all_hist[partition(observed)]+=1
            predicted=hist_predicted(m,p)
            assert all_hist==predicted,(p,m,all_hist,predicted)
            assert sum(predicted.values())==p**(2*m-1)
            print('PASS',p,m,'elements',p**(2*m-1),'types',len(all_hist),'classes',dict(sorted(all_hist.items(),reverse=True)))
    print('VERIFY_OK_ALL_JORDAN_VALUATIONS')
if __name__=='__main__':run()
