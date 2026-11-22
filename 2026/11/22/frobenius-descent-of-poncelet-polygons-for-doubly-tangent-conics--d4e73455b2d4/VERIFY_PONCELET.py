"""Exact finite-field tests and cyclic descent checks for bitangent conic Poncelet polygons.
Run with Python 3 (standard library)."""
from collections import Counter
from math import gcd

def norm(v,p):
    for a in v:
        if a%p:
            z=pow(a,-1,p)
            return tuple(x*z%p for x in v)
    raise ValueError('zero projective vector')

def cross(a,b,p):
    return ((a[1]*b[2]-a[2]*b[1])%p,
            (a[2]*b[0]-a[0]*b[2])%p,
            (a[0]*b[1]-a[1]*b[0])%p)

def order_from_trace(p,c):
    # r+r^{-1}=4c-2. Chebyshev recurrence identifies its exact order.
    a,b=2,(4*c-2)%p
    for n in range(1,p+2):
        if b==2: return n
        a,b=b,((4*c-2)*b-a)%p
    raise AssertionError('order missing')

def adjacency(p,epsilon,c):
    delta=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    pts=set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (x,y,z)==(0,0,0): continue
                if epsilon==1: val=x*z-y*y
                else: val=x*x-pow(delta,-1,p)*y*y-4*z*z
                if val%p==0: pts.add(norm((x,y,z),p))
    pts=sorted(pts)
    assert len(pts)==p+1
    adj=[set() for _ in pts]
    for i in range(len(pts)):
        for j in range(i):
            x,y,z=cross(pts[i],pts[j],p)
            if epsilon==1: val=y*y-4*c*x*z
            else: val=4*c*(x*x-delta*y*y)-z*z
            if val%p==0: adj[i].add(j); adj[j].add(i)
    seen=set(); lengths=[]
    for i in range(len(pts)):
        if not adj[i] or i in seen: continue
        todo=[i]; component=set()
        while todo:
            j=todo.pop()
            if j in component:continue
            component.add(j);todo.extend(adj[j]-component)
        assert all(len(adj[j])==2 for j in component)
        assert len(component)>=3
        seen|=component;lengths.append(len(component))
    return Counter(len(a) for a in adj), Counter(lengths)

for p in (3,5,7,11,13,17,19,23):
    for epsilon in (-1,1):
        matched=0
        for c in range(2,p):
            disc=c*(c-1)%p
            chi=1 if pow(disc,(p-1)//2,p)==1 else -1
            n=order_from_trace(p,c)
            assert n>=3 and (p-chi)%n==0
            N=p-epsilon
            degree_counts=adjacency(p,epsilon,c)
            if epsilon==chi:
                matched+=1
                assert degree_counts[0]==Counter({2:N,0:p+1-N})
                assert degree_counts[1]==Counter({n:N//n})
            else:
                assert degree_counts[0]==Counter({0:p+1})
                assert not degree_counts[1]
            # Cosets of order-n subgroup in cyclic group of order n*N.
            # Frob exponent epsilon*p; coset 'a' has k -> epsilon*a + epsilon*p*k.
            histogram=Counter()
            for a in range(N):
                rational_vertices=sum(1 for k in range(n)
                   if (epsilon*a+(epsilon*p-1)*k)%n==0)
                histogram[rational_vertices]+=1
            if epsilon==chi:
                assert histogram==Counter({0:N-N//n,n:N//n}), (p,epsilon,c,n,N,histogram)
            elif n%2:
                assert histogram==Counter({1:N})
            else:
                assert histogram==Counter({0:N//2,2:N//2})
        assert matched==((p-3)//2 if epsilon==1 else (p-1)//2)
print('PONCELET_DESCENT_EXACT_CHECKS_OK')
