"""Exact arithmetic smoke tests for prime torus heat-flow spatial sampling.
Pure Python 3, standard library only. Mathematical general proof is in RESULT.md.
"""
from math import isqrt

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def primitive_root_order_p(p,ell):
    for a in range(2,ell):
        r=pow(a,(ell-1)//p,ell)
        if r!=1 and pow(r,p,ell)==1:return r
    raise RuntimeError('no root')

def rank_mod(A,ell):
    A=[list(map(lambda x: x%ell,row)) for row in A]
    h=len(A);w=len(A[0]);i=0
    for j in range(w):
        pos=next((k for k in range(i,h) if A[k][j]),None)
        if pos is None:continue
        A[i],A[pos]=A[pos],A[i]
        inv=pow(A[i][j],-1,ell)
        A[i]=[(v*inv)%ell for v in A[i]]
        for k in range(i+1,h):
            if A[k][j]:
                factor=A[k][j]
                A[k]=[(A[k][l]-factor*A[i][l])%ell for l in range(w)]
        i+=1
        if i==h:break
    return i

def candidates(p):
    r=(p-1)//2
    return [(a,b) for a in range(r+1) for b in range(a,r+1)]

def freq_block(p,a,b):
    return [(k,l) for k in range(p) for l in range(p)
            if sorted((min(k,p-k),min(l,p-l)))==[a,b]]

def check(p):
    assert prime(p) and p>=5
    ell=2*p+1
    while True:
        if prime(ell):
            root=primitive_root_order_p(p,ell)
            inv4=pow(4,-1,ell)
            vals={}
            for a,b in candidates(p):
                lam=(pow(root,a,ell)+pow(root,-a,ell)+pow(root,b,ell)+pow(root,-b,ell))*inv4%ell
                vals[(a,b)]=lam
            if len(set(vals.values()))==len(vals):break
        ell+=p
    root_pows=[pow(root,k,ell) for k in range(p)]
    S=[(x,y) for x in range(4) for y in range(2)]
    sizes=[]
    for a,b in candidates(p):
        E=freq_block(p,a,b)
        A=[[root_pows[(k*x+l*y)%p] for k,l in E] for x,y in S]
        assert rank_mod(A,ell)==len(E),(p,a,b,'block rank')
        sizes.append(len(E))
    assert sum(sizes)==p*p and max(sizes)==8
    assert len(sizes)==((p+1)//2)*((p+3)//2)//2
    if p<=11:
        rows=[]
        for x,y in S:
            for t in range(len(sizes)):
                rows.append([(pow(vals[tuple(sorted((min(k,p-k),min(l,p-l))))],t,ell)*root_pows[(k*x+l*y)%p])%ell for k in range(p) for l in range(p)])
        assert rank_mod(rows,ell)==p*p,(p,'full dynamics rank')
    print(f'PASS p={p} elliptic_modulus={ell} blocks={len(sizes)} full_columns={p*p} max_multiplicity=8')

if __name__=='__main__':
    for p in (5,7,11,13,17):check(p)
    print('ALL_PRIME_TORUS_CHECKS_PASSED')
