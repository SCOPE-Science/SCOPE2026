#!/usr/bin/env python3
"""Independent direct enumeration of substitution factors and prefix windows."""

def morph(w):
    z=[]
    for x in w: z.extend((x,x,(x+1)%3))
    return z

def words(k):
    b=[[i] for i in range(3)]
    for _ in range(k): b=[morph(w) for w in b]
    return b

def seq(k):
    w=[0]
    for _ in range(k): w=morph(w)
    return w

def range_counts(data,n):
    c=sum(x==0 for x in data[:n]);lo=hi=c
    for i in range(n,len(data)):
        c+=(data[i]==0)-(data[i-n]==0)
        if c<lo:lo=c
        if c>hi:hi=c
    return lo,hi

def main():
    checked=0
    for k in range(7):
        block=words(k)
        n=3**k
        A=[range_counts(u+v,n) for u in block for v in block]
        l=min(t[0] for t in A);h=max(t[1] for t in A)
        b=seq(k+5)
        lp,hp=range_counts(b,n)
        expected=3**((k+1)//2)+2*3**(k//2)-1
        assert (lp,hp)==(l,h)
        assert h-l+1==expected
        checked+=len(b)-n+1
        print('k',k,'length',n,'min/max',l,h,'abelian complexity',expected)
    print('PASS:',checked,'direct factor-window counts checked, all 9 block pairs at each length.')
if __name__=='__main__':main()
