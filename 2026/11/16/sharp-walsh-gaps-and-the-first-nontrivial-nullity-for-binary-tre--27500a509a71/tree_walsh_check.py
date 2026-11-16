"""Exact Walsh spectrum of independent sets of a complete binary tree.

No numerical approximations or external dependencies are used.
Run: python3 tree_walsh_check.py
"""
from collections import Counter
from functools import lru_cache

def tree_edges(h):
    edges=[]
    def visit(k):
        here=len(vertices); vertices.append(k)
        if k:
            left=visit(k-1); right=visit(k-1)
            edges.extend(((here,left),(here,right)))
        return here
    vertices=[]
    visit(h)
    return len(vertices),edges

def fwht(a):
    n=len(a);step=1
    while step<n:
        for i in range(0,n,2*step):
            for j in range(step):
                x,y=a[i+j],a[i+j+step]
                a[i+j],a[i+j+step]=x+y,x-y
        step*=2

def direct(h):
    n,edges=tree_edges(h)
    a=[0]*(1<<n)
    for mask in range(1<<n):
        if all(not(mask>>i&1 and mask>>j&1) for i,j in edges):
            a[mask]=1
    count=sum(a)
    fwht(a)
    return a,count

def recursive(h):
    n=(1<<(h+1))-1
    def val(height,mask):
        if height==0:return (2 if not mask&1 else 0,1)
        sz=(1<<height)-1
        left=(mask>>1)&((1<<sz)-1)
        right=(mask>>(1+sz))&((1<<sz)-1)
        f,g=val(height-1,left)
        F,G=val(height-1,right)
        ex=f*F
        return ex+(1 if mask&1==0 else -1)*g*G,ex
    return [val(h,i)[0] for i in range(1<<n)]

def special(h):
    if h==0:return 1
    sub=special(h-1)
    sz=(1<<h)-1
    root=1 if h%3==0 else 0
    return root | sub<<1 | sub<<(1+sz)

def special_eval(h,mask):
    if h==0:return (2 if mask==0 else 0,1)
    sz=(1<<h)-1
    a,b=special_eval(h-1,(mask>>1)&((1<<sz)-1))
    c,d=special_eval(h-1,mask>>(1+sz))
    return a*c+(1 if mask&1==0 else -1)*b*d,a*c

def audit():
    for h in range(4):
        a,count=direct(h)
        b=recursive(h)
        assert a==b,(h,'frequency mismatch')
        m=1<<(2**(h+1)-1)
        assert sum(v*v for v in a)==m*count
        delta=min(abs(v) for v in a if v)
        zeros=a.count(0)
        assert delta==(2 if h%3==0 else 1)
        assert (zeros>0)==(h%3==0)
        assert special_eval(h,special(h))==[(0,1),(1,0),(1,1)][h%3]
        print('height',h,'vertices',(1<<(h+1))-1,'sets',count,'zero',zeros,'rank',m-zeros,'gap',delta,'signed_levels',len(set(a)))
        if h==3:
            print('height3 histogram',sorted(Counter(a).items()))
            assert count==2306 and zeros==14402 and m-zeros==18366
    for h in range(4,20):
        assert special_eval(h,special(h))==[(0,1),(1,0),(1,1)][h%3]
    print('BINARY_TREE_WALSH_PASS')

if __name__=='__main__':audit()
