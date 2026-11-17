#!/usr/bin/env python3
"""Exact, dependency-free certificates for a binary five-site cellular automaton."""
from itertools import product
from math import gcd

def local(bits):
    a, b, c, d, e = bits
    return a ^ d ^ (b & (1 ^ c) & e)

def mat(label):
    A = [[0]*16 for _ in range(16)]
    for i in range(16):
        w = [(i >> (3-k)) & 1 for k in range(4)]
        for e in (0, 1):
            if local(w + [e]) == label:
                j = ((i & 7)<<1) | e
                A[i][j] += 1
    return A

def mul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i, row in enumerate(A):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(B[k]):
                    if y: C[i][j] += x*y
    return C

def tr(A):
    return sum(row[i] for i, row in enumerate(A))

def charpoly(A):
    # Characteristic coefficients c_k by Newton's identities.
    n = len(A)
    P = [[int(i==j) for j in range(n)] for i in range(n)]
    s = [0]
    for k in range(1, n+1):
        P = mul(P,A)
        s.append(tr(P))
    c = [1]
    for k in range(1, n+1):
        q = -sum(c[k-i]*s[i] for i in range(1,k+1))
        assert q % k == 0
        c.append(q//k)
    return c

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_prod(polys):
    p=[1]
    for q in polys:p=poly_mul(p,q)
    return p

def cyclic_output(x):
    n=len(x)
    return [local([x[(i+k)%n] for k in range(5)]) for i in range(n)]

def expected(n,kind):
    if kind == 0:return 8 if n%6==0 else 2
    if kind == 1:return (8 if n%6==0 else 2) if n%2==0 else 0
    if kind == 2:return 8 if n%16==0 else 0
    raise ValueError(kind)

def main():
    A0, A1 = mat(0),mat(1)
    P=mul(A0,A1)
    # Coefficient arrays descending, exact expected polynomial products.
    E0=poly_prod([[1]+[0]*8, [1,-1],[1,-1],[1,-1],[1,1],[1,-1,1],[1,1,1]])
    E1=poly_prod([[1]+[0]*8, [1,-1],[1,-1],[1,1],[1,1],[1,-1,1],[1,1,1]])
    E2=poly_prod([[1]+[0]*8, [1]+[0]*7+[-1]])
    assert charpoly(A0)==E0, (charpoly(A0),E0)
    assert charpoly(A1)==E1
    assert charpoly(P)==E2
    print('CHARPOLY_OK',len(E0),len(E1),len(E2))
    powers=[[[int(i==j) for j in range(16)] for i in range(16)] for _ in range(3)]
    for n in range(1,129):
        for k,A in enumerate((A0,A1,P)):
            powers[k]=mul(powers[k],A)
            t=tr(powers[k])
            assert t==expected(n if k<2 else 2*n,k), (n,k,t)
    checks=0
    for n in range(1,13):
        counts=[0,0,0]
        for word in product((0,1),repeat=n):
            out=cyclic_output(word)
            if out==[0]*n: counts[0]+=1
            if out==[1]*n: counts[1]+=1
            if n%2==0 and out==[i%2 for i in range(n)]: counts[2]+=1
            checks+=1
        assert counts[0]==expected(n,0)
        assert counts[1]==expected(n,1)
        if n%2==0: assert counts[2]==expected(n,2)
    n=16
    hits=[]
    for i in range(1<<n):
        w=[(i>>k)&1 for k in range(n)]
        if cyclic_output(w)==[k%2 for k in range(n)]:hits.append(w)
    assert len(hits)==8
    for w in hits:
        assert all(any(w[i]!=w[(i+p)%n] for i in range(n)) for p in (1,2,4,8))
    first=hits[0]
    orbit={tuple(first[(i+2*k)%n] for i in range(n)) for k in range(8)}
    assert orbit==set(map(tuple,hits))
    print('VERIFY_OK', 'exact_charpolys=3', 'trace_powers=384',
          'bruteforce_ring_states='+str(checks), 'alternating_N16_preimages=8')

if __name__=='__main__':main()
