#!/usr/bin/env python3
"""Exact space-time transfer certificate for temporal period dividing four of ECA 54.
No third-party packages are needed. Run with Python 3.
"""
from collections import defaultdict

RULE = 54
TIME = 4

def update(left, center, right):
    return (RULE >> ((left << 2) | (center << 1) | right)) & 1

def transitions(p):
    edge = set()
    for a in range(1 << p):
        for b in range(1 << p):
            for c in range(1 << p):
                if all(((b >> ((t+1) % p)) & 1) == update((a >> t) & 1, (b >> t) & 1, (c >> t) & 1) for t in range(p)):
                    edge.add(((a, b), (b, c)))
    return edge

def strongly_connected(edge):
    vertices = set(x for x, y in edge) | set(y for x, y in edge)
    adj = {x: [] for x in vertices}
    for x,y in edge:
        adj[x].append(y)
    index, index_of, low, stack, onstack, out = 0, {}, {}, [], set(), []
    def visit(v):
        nonlocal index
        index_of[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in adj[v]:
            if w not in index_of:
                visit(w)
                low[v] = min(low[v],low[w])
            elif w in onstack:
                low[v] = min(low[v],index_of[w])
        if low[v] == index_of[v]:
            c = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                c.append(w)
                if w == v:
                    break
            out.append(tuple(sorted(c)))
    for v in sorted(vertices):
        if v not in index_of:
            visit(v)
    cyclic = [c for c in out if len(c) > 1 or (c[0],c[0]) in edge]
    return sorted(cyclic,key=lambda c:(len(c),c))

def mat_for(component,edge):
    index={x:i for i,x in enumerate(component)}
    m=[[0]*len(component) for _ in component]
    for x,y in edge:
        if x in index and y in index:
            m[index[x]][index[y]]+=1
    return m

def mul(a,b):
    d=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d)) for j in range(d)] for i in range(d)]

def identity(d):
    return [[int(i==j) for j in range(d)] for i in range(d)]

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

def charpoly(a):
    d=len(a); b=identity(d); coefficients=[1]
    for k in range(1,d+1):
        b=mul(a,b)
        t=trace(b)
        assert t%k==0
        coef=-(t//k)
        coefficients.append(coef)
        for i in range(d):
            b[i][i]+=coef
    return coefficients

def traces(a,nmax):
    b=identity(len(a)); arr=[]
    for n in range(1,nmax+1):
        b=mul(a,b)
        arr.append(trace(b))
    return arr


def main():
    c1=strongly_connected(transitions(1))
    c3=strongly_connected(transitions(3))
    assert c1==[((0,0),)] and c3==[((0,0),)]
    print('cyclic_components_p1', c1)
    print('cyclic_components_p3', c3)
    c2=strongly_connected(transitions(2))
    assert [len(c) for c in c2]==[1,4]
    c4=strongly_connected(transitions(4))
    assert [len(c) for c in c4]==[1,4,10,10]
    print('cyclic_components_p2', [(len(c),c) for c in c2])
    print('cyclic_components_p4', [(len(c),c) for c in c4])
    assert c4[0]==((0,0),)
    for c in c4[1:]:
        a=mat_for(c,transitions(4))
        cp=charpoly(a)
        print('component_dim',len(c),'charpoly_descending',cp)
    # Characteristic polynomial lambda^10-lambda^6-2lambda^4-2lambda^3-lambda^2-2lambda-1.
    expected=[1,0,0,0,-1,0,-2,-2,-1,-2,-1]
    a=mat_for(c4[2],transitions(4)); b=mat_for(c4[3],transitions(4))
    assert charpoly(a)==expected
    assert charpoly(b)==expected
    assert a!=b
    t=traces(a,30)
    assert t==traces(b,30)
    assert t[:10]==[0,0,0,4,0,12,14,12,18,30]
    for n,x in enumerate(t,1):
        assert x%2==0
        returned2=1+4*(n%4==0)
        returned4=returned2+2*x
        primitive4=(returned4-returned2)//4
        assert primitive4==x//2
        if n<=20:
            print('n',n,'Fix_F2',returned2,'Fix_F4',returned4,'primitive_4_orbits',primitive4)
    assert all((t[n-1]>0)==(n==4 or n>=6) for n in range(1,31))
    # The existence equivalence for every n follows from the four explicit
    # positive trace lengths 6,7,8,9 and closure under appending any 4-cycle.
    # A common vertex (5,6) has closed walks of lengths 4,6,7,8,9,
    # certified independently by powers of the adjacency matrix.
    vertex=(5,6)
    component=c4[2]
    idx=component.index(vertex)
    m=mat_for(component,transitions(4))
    mm=identity(10)
    for nn in range(1,10):
        mm=mul(mm,m)
        if nn in (4,6,7,8,9): assert mm[idx][idx]>0
    assert all(t[n+3]>0 for n in range(5,26))
    for n in range(1,21):
        # recurrence b_{n+10}=b_{n+6}+2b_{n+4}+2b_{n+3}+b_{n+2}+2b_{n+1}+b_n
        assert t[n+9] == t[n+5]+2*t[n+3]+2*t[n+2]+t[n+1]+2*t[n]+t[n-1]
    print('PASS: exact transfer, SCCs, characteristic polynomial, traces, and recurrence')

if __name__=='__main__':
    main()
