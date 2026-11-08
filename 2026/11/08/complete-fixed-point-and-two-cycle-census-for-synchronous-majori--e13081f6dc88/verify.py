#!/usr/bin/env python3
"""Exact standard-library certificate for two-color synchronous majority on prisms.

Run: python3 verify.py
All calculations use Python integers, with no imported research data.
"""
from collections import defaultdict


def maj(a, b, c):
    return int(a + b + c >= 2)


def colbits(s):
    return tuple((s >> i) & 1 for i in range(4))  # x_top,x_bottom,y_top,y_bottom


def make_graph():
    columns = [colbits(i) for i in range(16)]
    adj = [[] for _ in range(256)]
    for a in range(16):
        xa, xb, ya, yb = columns[a]
        for b in range(16):
            ua, ub, va, vb = columns[b]
            for c in range(16):
                xc, xd, yc, yd = columns[c]
                if (va == maj(xa, xc, ub) and
                    vb == maj(xb, xd, ua) and
                    ua == maj(ya, yc, vb) and
                    ub == maj(yb, yd, va)):
                    adj[16*a+b].append(16*b+c)
    return adj


def sccs(adj):
    count = 0
    stack, active = [], set()
    index, low, result = {}, {}, []
    def visit(v):
        nonlocal count
        index[v] = low[v] = count
        count += 1
        stack.append(v)
        active.add(v)
        for w in adj[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in active:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            block = []
            while True:
                w = stack.pop()
                active.remove(w)
                block.append(w)
                if w == v:
                    break
            result.append(tuple(sorted(block)))
    for v in range(len(adj)):
        if v not in index:
            visit(v)
    return result


def multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, aik in enumerate(A[i]):
            if aik:
                for j, bkj in enumerate(B[k]):
                    if bkj:
                        C[i][j] += aik*bkj
    return C


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def charpoly_from_traces(A):
    """Newton identities give det(zI-A) in descending integer coefficients."""
    n=len(A)
    power=[[int(i==j) for j in range(n)] for i in range(n)]
    tr=[0]
    for k in range(1,n+1):
        power=multiply(power,A)
        tr.append(trace(power))
    coeff=[1]
    for k in range(1,n+1):
        numerator=-sum(coeff[k-j]*tr[j] for j in range(1,k+1))
        assert numerator % k == 0
        coeff.append(numerator//k)
    return coeff


def polynomial_product(*factors):
    result=[1]
    for poly in factors:
        ans=[0]*(len(result)+len(poly)-1)
        for i,x in enumerate(result):
            for j,y in enumerate(poly):
                ans[i+j]+=x*y
        result=ans
    return result


def sequence(n):
    L=[2,1]
    for i in range(2,2*n+1):
        L.append(L[-1]+L[-2])
    f_corr=[2,1,-1,-2,-1,1][n%6]
    fixed=L[n]+2+f_corr
    r=n%6
    extra=(8*L[n]+18 if r==0 else
           2*L[n]+3 if r in (2,4) else
           4 if r==3 else 1)
    periodic=L[2*n]+extra
    assert (periodic-fixed)%2==0
    return fixed,periodic,(periodic-fixed)//2


def direct_update(state,n):
    value=0
    for layer in range(2):
        for i in range(n):
            left=(state >> (layer*n+(i-1)%n))&1
            right=(state >> (layer*n+(i+1)%n))&1
            across=(state >> ((1-layer)*n+i))&1
            value |= maj(left,right,across) << (layer*n+i)
    return value


def main():
    adj=make_graph()
    assert len(adj)==256 and sum(map(len,adj))==400
    comps=sccs(adj)
    cyclic=sorted((v for v in comps if len(v)>1 or v[0] in adj[v[0]]), key=lambda x:(-len(x),x))
    expected=[
        (0,6,9,15,96,102,105,111,144,150,153,159,240,246,249,255),
        (20,29,65,71,116,125,209,215),
        (40,46,130,139,184,190,226,235),
        (60,195),(85,),(170,)
    ]
    assert cyclic==expected,(cyclic,expected)
    assert sum(len(c) for c in comps)==256
    assert len([c for c in comps if len(c)==1 and c[0] not in adj[c[0]]])==220
    p16=polynomial_product(
        [1,-1],[1,-1],[1,1],[1,1],[1,-3,1],[1,1,1],
        [1,-1,2,1,1],[1,1,2,-1,1])
    p8=polynomial_product([1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1])
    for component, expected_polynomial in zip(cyclic,
                [p16,p8,p8,[1,0,-1],[1,-1],[1,-1]]):
        A=[[int(w in adj[v]) for w in component] for v in component]
        computed=charpoly_from_traces(A)
        assert computed==expected_polynomial,(component,computed,expected_polynomial)
    # An independently constructed cycle trace from the finite matrices.
    matrices=[]
    for component in cyclic:
        matrices.append([[int(w in adj[v]) for w in component] for v in component])
    powers=[[[int(i==j) for j in range(len(A))] for i in range(len(A))] for A in matrices]
    for n in range(1,41):
        powers=[multiply(P,A) for P,A in zip(powers,matrices)]
        count=sum(map(trace,powers))
        if n>=3:
            _,formula,_=sequence(n)
            assert count==formula,(n,count,formula)
    # Independent enumeration of all 2^(2n) configurations on short prisms.
    for n in range(3,9):
        fixed=periodic=0
        for state in range(1<<(2*n)):
            nxt=direct_update(state,n)
            fixed += (nxt==state)
            periodic += (direct_update(nxt,n)==state)
        f,t,p=sequence(n)
        assert (fixed,periodic)==(f,t),(n,fixed,periodic,f,t)
        print(f'n={n}: fixed={f}, period<=2 states={t}, strict pairs={p}')
    print('PASS: all 256 transfer vertices, 400 transitions, six recurrent blocks,')
    print('six exact characteristic polynomials, n=3..40 traces, n=3..8 exhaustive configurations.')

if __name__=='__main__':
    main()
