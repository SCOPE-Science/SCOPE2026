#!/usr/bin/env python3
"""Directly compute profile balls, extremal binary threshold, de Bruijn witnesses."""
from itertools import product

def profile(w,q):
    c=[0]*(q*q)
    for i in range(len(w)-1):
        c[w[i]*q+w[i+1]]+=1
    return tuple(c)

def ball(w,q):
    out={profile(w,q)}
    for i in range(len(w)-1):
        x=list(w)
        x[i],x[i+1]=x[i+1],x[i]
        out.add(profile(x,q))
    return out

def db(q,n):
    a=[0]*(q*n)
    output=[]
    def rec(t,p):
        if t>n:
            if n%p==0:output.extend(a[1:p+1])
        else:
            a[t]=a[t-p];rec(t+1,p)
            for j in range(a[t-p]+1,q):
                a[t]=j;rec(t+1,t)
    rec(1,1)
    assert len(output)==q**n
    return output

# Fully enumerate short binary inputs, including the unchanged profile.
maxima=[]
for n in range(2,9):
    vals=[len(ball(w,2)) for w in product(range(2),repeat=n)]
    maxima.append(max(vals))
    print('binary n',n,'max',max(vals),'maximizers',vals.count(max(vals)))
assert maxima==[2,3,4,4,4,4,5],maxima
for n in range(8,40):
    w=tuple(map(int,'01011'+'0'*(n-7)+'01'))
    assert len(w)==n and len(ball(w,2))==5
print('binary saturation starts at n=8; explicit family checked through n=39')

for q in range(2,7):
    seq=db(q,4)
    assert len({tuple((seq+seq[:3])[i:i+4]) for i in range(q**4)})==q**4
    i=next(i for i in range(len(seq)) if tuple(seq[(i+j)%len(seq)] for j in range(3))==(0,1,0))
    rot=seq[i:]+seq[:i]
    word=rot+rot[:3]
    assert len(ball(word,q))==1+2*__import__('math').comb(q,2)+14*__import__('math').comb(q,3)+24*__import__('math').comb(q,4)+2
    print('deBruijn',q,'length',len(word),'profiles',len(ball(word,q)))
print('PASS direct balls and construction')
