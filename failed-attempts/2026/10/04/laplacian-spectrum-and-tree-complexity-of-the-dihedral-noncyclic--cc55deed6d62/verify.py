#!/usr/bin/env python3
import sympy as sp

def mul(x,y,n):
    a,b=x; c,d=y
    return ((a + (-1 if b else 1)*c) % n, (b+d)%2)

def generated_is_cyclic(x,y,n):
    H={(0,0),x,y}
    changed=True
    while changed:
        changed=False
        for a in list(H):
            for b in list(H):
                z=mul(a,b,n)
                if z not in H:
                    H.add(z); changed=True
    for g in H:
        K={(0,0)}
        z=(0,0)
        for _ in range(1,2*n+1):
            z=mul(z,g,n); K.add(z)
        if K==H:
            return True
    return False

def noncyclic_graph(n):
    elems=[(a,b) for a in range(n) for b in (0,1)]
    e=(0,0)
    V=[x for x in elems if x!=e]
    cyc=[x for x in elems if all(generated_is_cyclic(x,y,n) for y in elems)]
    assert cyc==[e], (n,cyc)
    N=len(V)
    A=sp.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            if not generated_is_cyclic(V[i],V[j],n):
                A[i,j]=A[j,i]=1
    return V,A

for n in range(3,9):
    V,A=noncyclic_graph(n)
    N=2*n-1
    rotations=[i for i,x in enumerate(V) if x[1]==0]
    reflections=[i for i,x in enumerate(V) if x[1]==1]
    assert len(rotations)==n-1 and len(reflections)==n
    for i in rotations:
        for j in rotations:
            if i<j: assert A[i,j]==0
    for i in reflections:
        for j in reflections:
            if i<j: assert A[i,j]==1
    for i in rotations:
        for j in reflections:
            assert A[i,j]==1
    deg=[sum(int(A[i,j]) for j in range(N)) for i in range(N)]
    L=sp.diag(*deg)-A
    ev=L.eigenvals()
    expected={sp.Integer(0):1, sp.Integer(n):n-2, sp.Integer(2*n-1):n}
    assert ev==expected, (n,ev,expected)
    tau=int(L[:-1,:-1].det())
    expected_tau=(2*n-1)**(n-1)*n**(n-2)
    assert tau==expected_tau
    kf=sp.Rational(N,1)*(sp.Rational(n-2,n)+sp.Rational(n,2*n-1))
    assert sp.simplify(kf-(3*n-5+sp.Rational(2,n)))==0
    print(f'n={n} vertices={N} spectrum=0^1,{n}^{n-2},{2*n-1}^{n} trees={tau} Kf={sp.simplify(kf)}')
print('VERIFY_OK')
