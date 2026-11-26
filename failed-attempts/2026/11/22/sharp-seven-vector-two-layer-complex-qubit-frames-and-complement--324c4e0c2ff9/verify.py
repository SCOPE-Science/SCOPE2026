"""Supplementary finite-parameter verification of explicit paired Bloch frames.

The mathematical proof is given in RESULT.md. This numerical check is not a
substitute for symbolic identities or for the dimension-bound argument.
Run: python3 verify.py (Python standard library only).
"""
import math


def polygon(k, radius=1.0, phase=0.0):
    return [(radius * math.cos(2 * math.pi * j / k + phase),
             radius * math.sin(2 * math.pi * j / k + phase))
            for j in range(k)]


def examples(n):
    if n == 2:
        u = [(0.0, 0.0, 1.0), (0.0, 0.0, -1.0)]
        return u, u
    if n == 3:
        u = [(x,y,0.0) for x,y in polygon(3)]
        return u, u
    if n == 4:
        u = [(x/math.sqrt(3), y/math.sqrt(3), z/math.sqrt(3))
             for x,y,z in [(1,1,1), (1,-1,-1),(-1,1,-1),(-1,-1,1)]]
        return u, u
    if n == 5:
        u = [(math.cos(2*math.pi*j/5),math.sin(2*math.pi*j/5),0.0) for j in range(5)]
        v = [(math.cos(4*math.pi*j/5),math.sin(4*math.pi*j/5),0.0) for j in range(5)]
        return u, v
    if n == 6:
        r = 2/math.sqrt(5)
        h = 1/math.sqrt(5)
        p = polygon(3, r)
        u = [(x,y,h) for x,y in p] + [(x,y,-h) for x,y in p]
        v = [(x,y,h) for x,y in p] + [(-x,-y,-h) for x,y in p]
        return u, v
    if n == 7:
        p = polygon(3)
        q = polygon(4)
        u = [(math.sqrt(5)/3*x,math.sqrt(5)/3*y,2/3) for x,y in p]
        u += [(math.sqrt(3)/2*x,math.sqrt(3)/2*y,-1/2) for x,y in q]
        v = [(x,y,0.0) for x,y in p]
        v += [(-math.sqrt(5/12)*x,-math.sqrt(5/12)*y,
               math.sqrt(7/12)*(-1)**j) for j,(x,y) in enumerate(q)]
        return u, v
    raise ValueError('n must be 2,...,7')


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def check():
    count=0
    for n in range(2,8):
        u,v=examples(n)
        assert len(u) == len(v) == n
        for w in (u,v):
            for p in w:
                assert abs(dot(p,p)-1) < 1e-12
                count+=1
            for k in range(3):
                assert abs(sum(p[k] for p in w)) < 1e-12
                count+=1
        for i in range(n):
            for j in range(i+1,n):
                target=-2/(n-1)
                assert abs(dot(u[i],u[j])+dot(v[i],v[j])-target) < 1e-12
                # Bloch-to-qubit projective overlap identity.
                target_overlap=(n-2)/(n-1)
                overlap=1+(dot(u[i],u[j])+dot(v[i],v[j]))/2
                assert abs(overlap-target_overlap)<1e-12
                count+=2
    u,v=examples(7)
    for a,b,expect in [(u,u,7/3),(v,v,7/3),(u,v,0)]:
        for i in range(3):
            for j in range(3):
                lhs=sum(p[i]*q[j] for p,q in zip(a,b))
                rhs=expect if i==j or expect==0 else 0
                assert abs(lhs-rhs)<1e-12
                count+=1
    print('PASS: %d assertions for N=2,...,7; seven-point orthogonal 2-design split.'%count)

if __name__=='__main__':
    check()
