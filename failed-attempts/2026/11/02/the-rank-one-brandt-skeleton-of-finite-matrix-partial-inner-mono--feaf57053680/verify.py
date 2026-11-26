"""Reproducible finite-field checks for the rank-one skeleton theorem.

Run: python verify.py. No external dependencies.
"""
from itertools import product
from math import prod


def matrices(q, n):
    return list(product(range(q), repeat=n*n))


def multiply(a, b, q, n):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def matrix_rank(a, q, n):
    r = [list(a[i*n:(i+1)*n]) for i in range(n)]
    row = 0
    for col in range(n):
        z = next((i for i in range(row, n) if r[i][col] % q), None)
        if z is None: continue
        r[z], r[row] = r[row], r[z]
        inv = pow(r[row][col], -1, q)
        r[row] = [v*inv % q for v in r[row]]
        for i in range(n):
            if i != row:
                v=r[i][col]
                r[i] = [(a-v*b)%q for a,b in zip(r[i],r[row])]
        row+=1
    return row


def check(q,n):
    a=matrices(q,n); count=len(a); ix={z:i for i,z in enumerate(a)}
    zero=ix[(0,)*(n*n)]
    table=[[ix[multiply(x,y,q,n)] for y in a] for x in a]
    unit=[i for i,x in enumerate(a) if matrix_rank(x,q,n)==n]
    domains=[]
    expected_sizes={q**(d*d) for d in range(n+1)}
    for p in range(count):
        d=tuple(i for i in range(count) if table[p][i]==i and table[i][p]==i)
        assert len(d) in expected_sizes, (q,n,p,len(d))
        domains.append(d)
    emap={}; zmap={}
    e=set(); z=set()
    for p,d in enumerate(domains):
        if len(d)!=q: continue
        assert zero in d
        nonzero=next(k for k in d if k!=zero)
        assert matrix_rank(a[nonzero],q,n)==1
        is_e=table[nonzero][nonzero]!=zero
        v=(e if is_e else z)
        for item in d:
            if item!=zero:
                assert (table[item][item]!=zero)==is_e
                v.add(tuple(k*pow(next(t for t in a[item] if t),-1,q)%q
                            for k in a[item]))
    # Each rank-one line occurs as a generator domain.
    Q=(q**n-1)//(q-1)
    En=Q*q**(n-1)
    Zn=Q*(q**(n-1)-1)//(q-1)
    assert len(e)==En, (len(e),En)
    assert len(z)==Zn, (len(z),Zn)
    maps=set()
    for g in range(count):
        for h in range(count):
            p=table[g][h]; d=domains[p]
            if len(d)!=q: continue
            src=next(v for v in d if v!=zero)
            out=table[table[h][src]][g]
            assert out!=zero
            src_can=tuple(v*pow(next(t for t in a[src] if t),-1,q)%q for v in a[src])
            tgt_can=tuple(v*pow(next(t for t in a[out] if t),-1,q)%q for v in a[out])
            # The map is determined by the image of canonical generator of its source.
            sc=ix[src_can]; image=table[table[h][sc]][g]
            scale=next(t for t in a[image] if t)
            kind='e' if src_can in e else 'z'
            assert (tgt_can in e) if kind=='e' else (tgt_can in z)
            if kind=='e':
                idem=next(aid for aid in d if aid!=zero and table[aid][aid]==aid)
                image_idem=table[table[h][idem]][g]
                assert table[image_idem][image_idem]==image_idem
                maps.add((kind,src_can,tgt_can,1))
            else:
                maps.add((kind,src_can,tgt_can,scale))
    assert len(maps)==En*En+(q-1)*Zn*Zn,(q,n,len(maps),En*En+(q-1)*Zn*Zn)
    gl=len(unit); pgl=gl//(q-1)
    total=1+pgl+len(maps)
    print(f'q={q}, n={n}: |GL|={gl}, idempotent lines={En}, square-zero lines={Zn}, one-line maps={len(maps)}, skeleton={total}: VERIFY_OK')

if __name__=='__main__':
    check(2,2)
    check(3,2)
    check(2,3)
    print('VERIFY_OK')
