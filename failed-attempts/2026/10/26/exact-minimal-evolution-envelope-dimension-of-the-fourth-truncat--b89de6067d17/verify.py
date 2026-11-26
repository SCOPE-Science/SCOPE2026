#!/usr/bin/env python3
"""Self-contained exact certificate for small-field truncated-polynomial envelopes."""
from itertools import product

N = 4
PAIRS = [(i, j) for i in range(N) for j in range(i, N)]
TARGET = [tuple(int(i+j == k) for i,j in PAIRS) for k in range(N)]
WITNESSES = {
    2: ('1000', '0100', '1100', '0010', '1010', '0110', '0001', '1001'),
    3: ('0001', '1210', '1100', '1110', '1002', '0120', '1220', '1001'),
}

def pivot_extend(base, vec, p):
    """Insert vec in an echelon basis over prime field F_p, return new base, growth."""
    b = dict(base)
    v = list(vec)
    for j in range(len(v)):
        if not v[j]:
            continue
        if j in b:
            a = v[j]
            v = [(u - a*w)%p for u,w in zip(v,b[j])]
        else:
            inv = pow(v[j],-1,p)
            b[j] = tuple((inv*z)%p for z in v)
            return b, 1
    return b, 0

def rank(vectors,p):
    b = {}
    for v in vectors:
        b,_ = pivot_extend(b,v,p)
    return len(b)

def solve(rows, y, p):
    """Solve sum c_j*rows[j]=y over F_p; underdetermined is allowed."""
    n = len(rows)
    a = [[rows[j][i] for j in range(n)]+[y[i]] for i in range(len(y))]
    pivots=[];rr=0
    for col in range(n):
        h=next((k for k in range(rr,len(a)) if a[k][col]),None)
        if h is None:continue
        a[rr],a[h]=a[h],a[rr]
        inv=pow(a[rr][col],-1,p)
        a[rr]=[v*inv%p for v in a[rr]]
        for k in range(len(a)):
            if k==rr:continue
            factor=a[k][col]
            if factor:a[k]=[(v-factor*w)%p for v,w in zip(a[k],a[rr])]
        pivots.append(col);rr+=1
    assert all(any(row[:n]) or row[n]==0 for row in a)
    c=[0]*n
    for i,col in enumerate(pivots):c[col]=a[i][-1]
    assert all(sum(c[j]*rows[j][i] for j in range(n))%p==y[i] for i in range(len(y)))
    return c

def outer(v,p):
    return tuple(v[i]*v[j]%p for i,j in PAIRS)

def quotient(v,p):
    a,b,c,d=v
    return ((a*c-b*b)%p, (a*d-b*c)%p, b*d%p, c*c%p, c*d%p, d*d%p)

def test(p):
    forms=[]
    for v in product(range(p),repeat=N):
        if any(v):
            first=next(z for z in v if z)
            if first==1:forms.append(v)
    assert len(forms)==(p**N-1)//(p-1)
    outs=[outer(v,p) for v in forms]
    quot=[quotient(v,p) for v in forms]
    checked=0;nodes=0
    def branch(start,chosen,qbasis,selected):
        nonlocal checked,nodes
        nodes+=1
        if chosen==7:
            checked+=1
            mat=[outs[i] for i in selected]
            assert rank(mat+TARGET,p)>rank(mat,p), ('unexpected seven-square decomposition',p,selected)
            return
        for i in range(start,len(forms)-(7-chosen)+1):
            nb,extra=pivot_extend(qbasis,quot[i],p)
            if len(nb)>3:continue
            branch(i+1,chosen+1,nb,selected+(i,))
    branch(0,0,{},())
    assert checked>0
    witness=[tuple(int(c) for c in s) for s in WITNESSES[p]]
    assert all(v in forms for v in witness)
    rows=[outer(v,p) for v in witness]
    coefs=[solve(rows,t,p) for t in TARGET]
    output=[tuple(coefs[k][j] for k in range(N)) for j in range(8)]
    assert rank(witness,p)==4
    for a in product(range(p),repeat=N):
        for b in product(range(p),repeat=N):
            exp=tuple(sum(a[i]*b[k-i] for i in range(k+1))%p for k in range(N))
            got=tuple(sum((sum(x*y for x,y in zip(f,a))%p)*(sum(x*y for x,y in zip(f,b))%p)*z[k] for f,z in zip(witness,output))%p for k in range(N))
            assert got==exp, ('bad product',p,a,b)
    print(f'FIELD={p}: VERIFY_OK quotient_nodes={nodes} admissible_seven_subsets={checked} valid_seven=0 exhaustive_product_pairs={p**8}')
    print(f'FIELD={p}: WITNESS_FORMS={WITNESSES[p]}')
    print(f'FIELD={p}: WITNESS_OUTPUTS={tuple("".join(map(str,z)) for z in output)}')

if __name__=='__main__':
    test(2)
    test(3)
