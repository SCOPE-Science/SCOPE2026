"""Exhaustive direct-adjacency test of contact-(2,2) Poncelet distributions, for prime fields.
No external files or packages; run: python _verify_poncelet22.py
"""
from itertools import product, combinations
from collections import Counter
from math import gcd, prod


def norm(v,p):
    for x in v:
        if x%p:
            iv=pow(x%p,-1,p)
            return tuple((iv*y)%p for y in v)
    raise ValueError('zero projective vector')


def det3(M,p):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p


def adj3(M,p):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return [[(e*i-f*h)%p,(c*h-b*i)%p,(b*f-c*e)%p],
            [(f*g-d*i)%p,(a*i-c*g)%p,(c*d-a*f)%p],
            [(d*h-e*g)%p,(b*g-a*h)%p,(a*e-b*d)%p]]


def dot(v,w,p): return sum(a*b for a,b in zip(v,w))%p

def cross(v,w,p):
    return ((v[1]*w[2]-v[2]*w[1])%p,(v[2]*w[0]-v[0]*w[2])%p,(v[0]*w[1]-v[1]*w[0])%p)

def mult(M,v,p):return [dot(row,v,p) for row in M]


def Qsquare(a,b,c,p):return (a*a%p,2*a*b%p,(b*b+2*a*c)%p,2*b*c%p,c*c%p)

def build_square_lookup(p):
    squares={}
    for j in range(3):
        for tail in product(range(p),repeat=2-j):
            abc=(0,)*j+(1,)+tail
            a,b,c=abc
            discriminant=(b*b-4*a*c)%p
            if not discriminant:continue
            key=norm(Qsquare(a,b,c,p),p)
            sign=1 if pow(discriminant,(p-1)//2,p)==1 else -1
            assert key not in squares
            squares[key]=sign
    return squares


def projective_vectors(n,p):
    for j in range(n):
        for tail in product(range(p),repeat=n-1-j):
            yield (0,)*j+(1,)+tail


def graph_types(D,p,points,lines):
    A,B,C,E,F,G=D
    H=((2*A,B,C),(B,2*E,F),(C,F,2*G))
    Hinv=adj3(H,p)
    adj=[[] for _ in points]
    for (i,j),ell in lines.items():
        if dot(ell,mult(Hinv,ell,p),p)==0:
            adj[i].append(j);adj[j].append(i)
    degrees=Counter(map(len,adj))
    assert all(d in (0,2) for d in degrees), (p,D,degrees)
    visited=set();sizes=[]
    for i in range(len(points)):
        if i in visited or not adj[i]:continue
        stack=[i];visited.add(i);order=0
        while stack:
            v=stack.pop();order+=1
            for w in adj[v]:
                if w not in visited:visited.add(w);stack.append(w)
        assert order>=3
        sizes.append(order)
    assert len(set(sizes))<=1
    return (sizes[0],len(sizes)) if sizes else (0,0)


def solve(p):
    square_lookup=build_square_lookup(p)
    points=[(t*t%p,t,1) for t in range(p)]+[(1,0,0)]
    lines={(i,j):cross(points[i],points[j],p) for i,j in combinations(range(p+1),2)}
    observed=Counter(); types=Counter(); contact=Counter(); all_conics=0
    for D in projective_vectors(6,p):
        A,B,C,E,F,G=D
        H=((2*A,B,C),(B,2*E,F),(C,F,2*G))
        if det3(H,p)==0: continue
        all_conics+=1
        quartic=(A,B,(C+E)%p,F,G)
        if quartic==(0,)*5:continue
        s=square_lookup.get(norm(quartic,p))
        if s is None:continue
        contact[s]+=1
        t=graph_types(D,p,points,lines)
        observed[t]+=1
        types[(s,t[0])]+=1
    assert all_conics==p*p*(p**3-1),(p,all_conics)
    assert sum(observed.values())==p*p*(p-2),(p,observed)
    assert contact[1]==p*(p+1)*(p-2)//2
    assert contact[-1]==p*(p-1)*(p-2)//2
    def phi(n):return sum(gcd(j,n)==1 for j in range(1,n+1))
    expected=Counter()
    for sig in (1,-1):
        for n in range(3,p+2):
            if (p-sig)%n==0:
                expected[(n,(p-sig)//n)]+=p*(p+sig)*phi(n)//4
    expected[(0,0)]=p*p*(p-2)-sum(expected.values())
    assert observed==expected,(p,observed,expected)
    return {'q':p,'total_smooth_conics':all_conics,'contact_22_per_C':sum(observed.values()),'by_contact_sign':dict(contact),'rational_graph_spectrum':{f'{n}_gon_{cycles}_cycles':v for (n,cycles),v in sorted(observed.items())}}

if __name__=='__main__':
    import json
    for q in (3,5,7,11,13):
        print(json.dumps(solve(q),sort_keys=True))
