#!/usr/bin/env python3
"""Exact finite-field consistency checks for a family of Zinbiel multiplication tables.

The proof for arbitrary rank and characteristic zero is in RESULT.md. These
independent finite computations are necessary consistency checks, not proofs
for all dimensions.
"""

def table(k, p):
    n = 4*k + 1
    w = n-1
    mul = {}
    for i in range(k):
        u,v,t,s = 4*i,4*i+1,4*i+2,4*i+3
        for a,b,c,co in ((u,u,w,1),(u,v,t,1),(v,u,t,-1),
                          (v,v,w,1),(u,t,s,1),(v,t,w,1)):
            mul[a,b] = (c,co%p)
    return n,mul


def rank(rows, ncols, p):
    pivots = {}
    for orig in rows:
        x = {i:v%p for i,v in enumerate(orig) if v%p}
        while x:
            lead = min(x)
            if lead not in pivots:
                inv = pow(x[lead],-1,p)
                pivots[lead] = {j:(v*inv)%p for j,v in x.items() if (v*inv)%p}
                break
            y = pivots[lead]
            c = x[lead]
            for j,v in y.items():
                nv=(x.get(j,0)-c*v)%p
                if nv:x[j]=nv
                else:x.pop(j,None)
    return len(pivots)


def check(k,p):
    n,mul=table(k,p)
    w=n-1
    annihilator=set([w]+[4*i+3 for i in range(k)])
    sq=set([w]+[4*i+2 for i in range(k)]+[4*i+3 for i in range(k)])
    # Zinbiel identity on every basis triple, exact in the prime field.
    for i in range(n):
        for j in range(n):
            for h in range(n):
                left={}
                if (i,j) in mul:
                    a,c=mul[i,j]
                    if (a,h) in mul:
                        b,d=mul[a,h];left[b]=c*d%p
                right={}
                for x,y in ((j,h),(h,j)):
                    if (x,y) in mul:
                        a,c=mul[x,y]
                        if (i,a) in mul:
                            b,d=mul[i,a];right[b]=(right.get(b,0)+c*d)%p
                assert all(left.get(a,0)==right.get(a,0) for a in set(left)|set(right)), (k,p,i,j,h)
    actual_sq={v for v,c in mul.values() if c%p}
    assert actual_sq==sq
    actual_ann={a for a in range(n) if all((a,b) not in mul and (b,a) not in mul for b in range(n))}
    assert actual_ann==annihilator
    assert {v for (i,j),(v,c) in mul.items() if i in sq or j in sq}==annihilator
    # Derivation identities linear in entries D_ab, for all (i,j,h).
    rows=[]
    for i in range(n):
        for j in range(n):
            for h in range(n):
                r=[0]*(n*n)
                if (i,j) in mul:
                    v,c=mul[i,j]
                    r[h*n+v]+=c
                for v in range(n):
                    if (v,j) in mul and mul[v,j][0]==h:
                        r[v*n+i]-=mul[v,j][1]
                    if (i,v) in mul and mul[i,v][0]==h:
                        r[v*n+j]-=mul[i,v][1]
                if any(z%p for z in r):rows.append(r)
    d=n*n-rank(rows,n*n,p)
    central=(n-len(sq))*len(annihilator)
    assert d==central,(k,p,d,central)
    print('k=%s characteristic=%s dim_A=%s dim_Der=%s Zinbiel=OK annihilator=OK' % (k,p,n,d))


if __name__=='__main__':
    for p in (3,5,101):
        for k in (1,2,3):
            check(k,p)
    print('ZINBIEL_CENTRAL_AMALGAM_CHECKS_OK')
