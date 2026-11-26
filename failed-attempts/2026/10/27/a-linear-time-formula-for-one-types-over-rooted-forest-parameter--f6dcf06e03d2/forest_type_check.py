#!/usr/bin/env python3
"""Independent exhaustive checker for the finite rooted-forest type count."""
from itertools import product
from math import factorial


def recurrence(parent):
    n=len(parent)
    children=[[] for _ in range(n)]
    roots=[]
    for v,p in enumerate(parent):
        if p<0: roots.append(v)
        else: children[p].append(v)
    a=[0]*n
    for v in reversed(range(n)):
        z=1
        for c in children[v]: z*=a[c]
        a[v]=1+z
    total=1
    for r in roots: total*=a[r]
    return 2*total+sum(a)-2*n-1


def direct(parent):
    n=len(parent)
    R=[[i==j for j in range(n)] for i in range(n)]
    for v in range(n):
        p=parent[v]
        while p!=-1:
            R[p][v]=True
            p=parent[p]
    ans=0
    # 0: below new point (p<x); 1: incomparable; 2: above new point (x<p)
    for lab in product(range(3),repeat=n):
        E=[[False]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n): E[i][j]=R[i][j]
            E[i][n]=(lab[i]==0)
            E[n][i]=(lab[i]==2)
        E[n][n]=True
        valid=True
        for i in range(n+1):
            for j in range(n+1):
                if not E[i][j]: continue
                for k in range(n+1):
                    if E[j][k] and not E[i][k]:
                        valid=False; break
                if not valid:break
            if not valid:break
        ans+=valid
    return ans


def main():
    checks=0
    for n in range(0,7):
        for slots in product(*[[-1]+list(range(v)) for v in range(n)]):
            r=recurrence(slots)
            d=direct(slots)
            if r!=d:raise AssertionError((slots,r,d))
            checks+=1
        print('n',n,'verified',factorial(n) if n>0 else 1)
    examples=[([-1]*(n),2**(n+1)-1) for n in range(1,9)]
    examples += [([-1]+[i-1 for i in range(1,n)],1+n*(n+3)//2) for n in range(1,9)]
    examples += [([-1]+[0]*(n-1),3*2**(n-1)) for n in range(1,9)]
    for p,answer in examples:
        if recurrence(p)!=answer:raise AssertionError((p,answer,recurrence(p)))
    print('ALL_TESTS_PASS; exhaustive_forests=',checks,'closed_form_examples=',len(examples))

if __name__=='__main__':main()
