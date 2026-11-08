"""Reproduce the finite tree-cutoff certificate using only Python's standard library.

Run: python3 CHECK.py. No external packages or downloaded data are needed.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

TREE_COUNTS = [0,1,1,1,2,3,6,11,23,47,106,235,551]
DISTINCT_PROFILES = {4:2,5:3,6:6,7:11,8:23,9:45,10:104,11:215,12:522}
A = ((0,1),(0,7),(0,11),(1,2),(1,6),(2,3),(2,5),(3,4),(7,8),(8,9),(8,10))
B = ((0,1),(0,6),(0,10),(1,2),(2,3),(2,4),(2,5),(6,7),(7,8),(7,9),(10,11))

def adjacency(n, edges):
    g = [[] for _ in range(n)]
    for u,v in edges:
        g[u].append(v);g[v].append(u)
    return g

def canonical(n, edges):
    g=adjacency(n,edges)
    deg=[len(a) for a in g]; leaves=[i for i,d in enumerate(deg) if d<=1]; remaining=n
    while remaining>2:
        remaining-=len(leaves); nxt=[]
        for v in leaves:
            for u in g[v]:
                deg[u]-=1
                if deg[u]==1:nxt.append(u)
        leaves=nxt
    def rooted(v,parent):
        return '('+''.join(sorted(rooted(u,v) for u in g[v] if u!=parent))+')'
    if len(leaves)==1:return rooted(leaves[0],-1)
    u,v=leaves
    return '('+''.join(sorted([rooted(u,v),rooted(v,u)]))+')'

def profiles(n, edges):
    g=adjacency(n,edges);h=[0]*n
    for u in range(n):
        d=[-1]*n;d[u]=0;todo=deque([u])
        while todo:
            v=todo.popleft()
            for w in g[v]:
                if d[w]<0:
                    d[w]=d[v]+1;todo.append(w)
        assert min(d)>=0
        for v in range(u+1,n):h[d[v]]+=1
    return tuple(h[1:])

def transformed_coeffs(diff):
    # F(p)/p^3 = sum_{j>=0} diff[j+1]*p^j;
    # the Möbius transform is (1+t)^degree F(t/(1+t))/p^3.
    a=diff[1:];degree=len(a)-1
    return [sum(a[k]*comb(degree-k,j-k) for k in range(j+1)) for j in range(degree+1)]

def variations(c):
    signs=[1 if z>0 else -1 for z in c if z]
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c

def proof_lower_bound():
    states=[()]
    exceptional=[]
    for n in range(1,13):
        if n>1:
            candidates={}
            for edges in states:
                for v in range(n-1):
                    e=edges+((v,n-1),)
                    candidates.setdefault(canonical(n,e),e)
            states=list(candidates.values())
        assert len(states)==TREE_COUNTS[n],(n,len(states))
        if n<4:continue
        ss=set(profiles(n,edges) for edges in states)
        assert len(ss)==DISTINCT_PROFILES[n],(n,len(ss))
        if n>11:break
        arr=sorted(ss)
        levels=Counter()
        for i,a in enumerate(arr):
            for b in arr[i+1:]:
                diff=tuple(x-y for x,y in zip(a,b))
                v=variations(transformed_coeffs(diff))
                levels[v]+=1
                if v>=2:exceptional.append((n,diff))
        print(f'n={n}: {len(states)} trees, {len(ss)} distance profiles, sign-variation counts={dict(sorted(levels.items()))}')
    assert len(exceptional)==1 and exceptional[0][0]==11,exceptional
    diff=exceptional[0][1]
    # The only possible exception is +/-p^3*(p-1)*(3p^3+p^2-3p+1).
    want=poly_mul([-1,1],[1,-3,1,3])
    assert list(diff[1:6])==want and all(v==0 for v in diff[6:]),(diff,want)
    # The cubic has discriminant -76 and g(0)=1: its sole real root is negative.
    # Thus g is strictly positive throughout [0,1], ruling out two crossings.
    a,b,c,d=3,1,-3,1
    discriminant=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
    assert discriminant==-76
    return True

def witness():
    a=profiles(12,A);b=profiles(12,B)
    assert a==(11,14,14,12,8,5,2,0,0,0,0),a
    assert b==(11,15,11,13,10,6,0,0,0,0,0),b
    d=tuple(u-v for u,v in zip(a,b))
    # Expected connected pairs: sum_{distance r} h_r p^(r+1).
    # Difference: p^3*(p-1)*(2p-1)*(p^3+p^2-1).
    assert list(d[1:7])==poly_mul(poly_mul([-1,1],[-1,2]),[-1,0,1,1])
    assert not any(d[7:]),d
    from fractions import Fraction
    def gap(p):return sum(c*p**(i+2) for i,c in enumerate(d))
    vals=[gap(Fraction(1,4)),gap(Fraction(2,3)),gap(Fraction(9,10))]
    assert vals==[Fraction(-177,32768),Fraction(56,6561),Fraction(-392931,12500000)],vals
    # x^3+x^2-1 strictly increases from -1 to +1 on (0,1), crossing
    # once beyond 1/2; this and the 1/2 factor give exactly two crossings.
    assert Fraction(1,2)**3+Fraction(1,2)**2-1<0
    assert Fraction(1,1)**3+Fraction(1,1)**2-1>0
    print('12-site witness: distance-profile difference',d)
    print('exact signed gaps at 1/4,2/3,9/10:',vals)

if __name__=='__main__':
    proof_lower_bound()
    witness()
    print('PASS: sharp 12-site onset of two ranking reversals')
