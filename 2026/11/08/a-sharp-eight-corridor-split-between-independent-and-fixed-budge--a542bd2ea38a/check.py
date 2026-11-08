#!/usr/bin/env python3
"""Exact checks for conditional-vs-independent dispersal connectivity."""
from math import comb
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
import sympy as sy

# Each object is a two-terminal series-parallel multigraph; ('e',) is one corridor.
A=('p', ('s', ('e',), ('e',)), ('s', ('e',), ('p', ('e',), ('s', ('e',), ('s', ('e',), ('s', ('e',), ('e',)))))))
B=('p', ('s', ('e',), ('s', ('e',), ('e',))), ('s', ('e',), ('p', ('e',), ('s', ('e',), ('p', ('e',), ('e',))))))

def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return tuple(out)
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return tuple(out)
def parallel(a,b):return add(add(a,b),tuple(-v for v in mul(a,b)))
def polynomial(tree):
    if tree[0]=='e':return (0,1)
    x,y=polynomial(tree[1]),polynomial(tree[2])
    return mul(x,y) if tree[0]=='s' else parallel(x,y)
def to_counts(c):
    n=len(c)-1
    return tuple(sum(c[j]*comb(n-j,k-j) for j in range(k+1)) for k in range(n+1))
def dc(tree):
    if tree[0]=='e':return 1,1
    a,b=dc(tree[1]),dc(tree[2])
    return (a[0]+b[0],min(a[1],b[1])) if tree[0]=='s' else (min(a[0],b[0]),a[1]+b[1])

def physical_graph(tree):
    """Freshly assign two endpoints per leaf, union joints, preserve parallel edges."""
    edges=[]; parent=[]
    def node():
        i=len(parent);parent.append(i);return i
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    def union(i,j): parent[root(i)]=root(j)
    def recurse(t):
        if t[0]=='e':
            s,t=node(),node();edges.append((s,t));return s,t
        a,b=recurse(t[1]),recurse(t[2])
        if t[0]=='s':union(a[1],b[0]);return a[0],b[1]
        union(a[0],b[0]);union(a[1],b[1]);return a
    s,t=recurse(tree)
    roots={x:i for i,x in enumerate(sorted(set(root(i) for i in range(len(parent)))))}
    return [(roots[root(a)],roots[root(b)]) for a,b in edges],roots[root(s)],roots[root(t)]

def enumerate_paths(tree):
    edges,s,t=physical_graph(tree);m=len(edges);C=[0]*(m+1)
    for mask in range(1<<m):
        adj=defaultdict(list)
        for j,(a,b) in enumerate(edges):
            if mask>>j&1:
                adj[a].append(b);adj[b].append(a)
        seen={s};todo=[s]
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt not in seen:seen.add(nxt);todo.append(nxt)
        if t in seen:C[mask.bit_count()]+=1
    return tuple(C),edges,s,t

# Series/parallel closure: all distinct polynomials for exact m corridors.
L={1:{(0,1):('e',)}}
for m in range(2,9):
    out={}
    for a in range(1,m//2+1):
        for x,t in L[a].items():
            for y,u in L[m-a].items():
                out.setdefault(mul(x,y),('s',t,u))
                out.setdefault(parallel(x,y),('p',t,u))
    L[m]=out
assert tuple(len(L[m]) for m in range(1,9))==(1,2,4,10,24,64,174,496)
assert polynomial(A) in L[8] and polynomial(B) in L[8]
p=sy.Symbol('p')

def odd_interior_root(c):
    F=sy.Poly(sum(v*p**i for i,v in enumerate(c)),p)
    for irreducible,mult in F.sqf_list()[1]:
        if mult%2==1 and irreducible.eval(0)!=0 and irreducible.eval(1)!=0:
            if irreducible.count_roots(0,1)>0:return True
    return False

comparisons={}
for m in range(2,9):
    arr=list(L[m].items());eligible=0;no_sign_change=0
    for i,(a,t) in enumerate(arr):
        d=dc(t)
        if d[0]<2 or d[1]<2:continue
        for b,u in arr[i+1:]:
            if dc(u)!=d:continue
            z=tuple(v-w for v,w in zip(a,b))
            cc=to_counts(z)
            if not(min(cc)<0<max(cc)):continue
            eligible+=1
            if not odd_interior_root(z):no_sign_change+=1
    comparisons[m]=(eligible,no_sign_change)
assert comparisons=={2:(0,0),3:(0,0),4:(0,0),5:(0,0),6:(0,0),7:(50,0),8:(495,9)},comparisons
# Independent direct subset enumeration and symbolic composition agree, including all conditional counts.
CA,EA,sa,ta=enumerate_paths(A)
CB,EB,sb,tb=enumerate_paths(B)
assert len(EA)==len(EB)==8 and dc(A)==dc(B)==(2,2)
assert CA==to_counts(polynomial(A))
assert CB==to_counts(polynomial(B))
assert tuple(a-b for a,b in zip(CA,CB))==(0,0,1,3,2,-1,1,0,0)
D=sy.factor(sum((a-b)*p**i*(1-p)**(8-i) for i,(a,b) in enumerate(zip(CA,CB))))
assert sy.expand(D-p**2*(1-p)**2*(2*p**4-p**2-p+1))==0
# The quartic has a nonnegative degree-five Bernstein expansion, positive for 0<p<1.
Q=2*p**4-p**2-p+1
assert sy.expand(Q-sum(v*p**k*(1-p)**(5-k) for k,v in enumerate((1,4,5,1,0,1))))==0
assert Fraction(CA[5]-CB[5],comb(8,5))==Fraction(-1,56)
assert D.subs(p,sy.Rational(1,2))==sy.Rational(3,128)
print('SUCCESS SP m<=8 exact comparisons',comparisons)
print('A edges (s,t)',EA,(sa,ta))
print('B edges (s,t)',EB,(sb,tb))
print('reliability difference',D)
print('fixed-5 difference -1/56; independent p=1/2 difference 3/128')
