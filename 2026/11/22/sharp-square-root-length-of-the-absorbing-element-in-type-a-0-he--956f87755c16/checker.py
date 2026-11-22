#!/usr/bin/env python3
"""Independent exact checks of a type-A 0-Hecke minimal-root theorem."""
from itertools import permutations
from math import factorial

def witness(n):
    p=[0]*n
    for j in range(1,2*(n//4)+1,2):
        c=(j,j+1,n+1-j,n-j)
        for i,x in enumerate(c): p[x-1]=c[(i+1)%4]
    if n%4==1: p[(n+1)//2-1]=(n+1)//2
    if n%4==2:
        m=n//2;p[m-1],p[m]=m+1,m
    if n%4==3:
        m=(n-1)//2
        p[m-1],p[m],p[m+1]=m+1,m+2,m
    return tuple(x-1 for x in p)

def inv_count(p):
    return sum(x>y for i,x in enumerate(p) for y in p[i+1:])

def reduced_word(p):
    q=list(p);s=[]
    for i in range(len(q)):
        j=q.index(i)
        while j>i:
            s.append(j-1);q[j-1],q[j]=q[j],q[j-1];j-=1
    return list(reversed(s))

def dsquare(p):
    q=list(p)
    for j in reduced_word(p):
        if q[j]<q[j+1]:q[j],q[j+1]=q[j+1],q[j]
    return tuple(q)

def group_square(p):return tuple(p[p[i]] for i in range(len(p)))

def exhaustive():
    observed=[]
    for n in range(2,9):
        end=tuple(range(n-1,-1,-1));L=n*(n-1)//2
        roots=[];group_roots=[]
        for p in permutations(range(n)):
            if inv_count(p)!=(L+1)//2:continue
            if dsquare(p)==end:roots.append(p)
            if group_square(p)==end:group_roots.append(p)
        if n%4 in (0,1):
            k=n//4
            assert len(roots)==len(group_roots)==factorial(2*k)//factorial(k)
        assert roots
        observed.append((n,len(roots)))
    return observed

def main():
    for n in range(2,101):
        p=witness(n);w0=tuple(reversed(range(n)))
        assert len(set(p))==n
        L=n*(n-1)//2
        assert inv_count(p)==(L+1)//2
        assert dsquare(p)==w0
        sq=group_square(p)
        if n%4 in (0,1):
            assert sq==w0
        else:
            i=n//2 if n%4==2 else (n+1)//2
            v=list(w0);v[i-1],v[i]=v[i],v[i-1]
            assert sq==tuple(v) and p[i-1]>p[i]
    print('canonical witnesses, lengths, group-square identities and Demazure squares: n=2..100 PASS')
    print('exhaustive minimum-root counts:',exhaustive())
    print('all checks PASS')
if __name__=='__main__':main()
