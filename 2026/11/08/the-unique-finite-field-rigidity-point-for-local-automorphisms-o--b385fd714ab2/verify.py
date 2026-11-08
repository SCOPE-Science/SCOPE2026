"""Independent exhaustive linear-local-automorphism tests for H_3(F_2), H_3(F_3).
All test vectors, automorphism witnesses and candidate linear maps are enumerated.
No third-party modules are needed.
"""
from itertools import product

def mul(A,x,p):
    return tuple(sum(A[i][j]*x[j] for j in range(3))%p for i in range(3))

def det2(a,b,c,d,p):
    return (a*d-b*c)%p

def test(p):
    vecs=list(product(range(p),repeat=3))
    aut=[]
    for a,b,c,d in product(range(p),repeat=4):
        delta=det2(a,b,c,d,p)
        if not delta: continue
        for u,v in product(range(p),repeat=2):
            aut.append(((a,b,0),(c,d,0),(u,v,delta)))
    orbits={x:set() for x in vecs}
    for T in aut:
        for x in vecs: orbits[x].add(mul(T,x,p))
    la=ordinary=0
    for E in product(range(p),repeat=9):
        T=(E[:3],E[3:6],E[6:9])
        local=all(mul(T,x,p) in orbits[x] for x in vecs)
        d=det2(T[0][0],T[0][1],T[1][0],T[1][1],p)
        predicted=bool(d and T[2][2] and T[0][2]==0 and T[1][2]==0)
        assert local==predicted,('local mismatch',p,T)
        la+=local
        ordinary+=T in aut
    gl2=(p*p-1)*(p*p-p)
    assert la==(p-1)*p*p*gl2
    assert ordinary==p*p*gl2
    return p,p**9,la,ordinary

def order_index(q,m):
    gl=q**(m*(2*m-1))
    for j in range(1,2*m+1): gl*=q**j-1
    sp=q**(m*m)
    for j in range(1,m+1): sp*=q**(2*j)-1
    formula=q**(m*(m-1))
    for j in range(1,m+1):formula*=q**(2*j-1)-1
    assert gl%sp==0 and gl//sp==formula
    return formula

def binary_sp4_census():
    # Independent direct enumeration of 4x4 matrices in F2, including
    # nonsymplectic invertibles. Basis x1,x2,y1,y2.
    def symp(x,y):
        return ((x[0]&y[2])^(x[1]&y[3])^(x[2]&y[0])^(x[3]&y[1]))
    def rank(rows):
        b=list(rows); k=0
        for j in range(4):
            t=next((t for t in range(k,4) if (b[t]>>j)&1),None)
            if t is None: continue
            b[k],b[t]=b[t],b[k]
            for t in range(4):
                if t!=k and (b[t]>>j)&1: b[t]^=b[k]
            k+=1
        return k
    gl=sp=0
    for entries in product(range(16),repeat=4):
        if rank(entries)!=4: continue
        gl+=1
        cols=[[ (entries[i]>>j)&1 for i in range(4)] for j in range(4)]
        if all(symp(cols[i],cols[j]) == (int(i+2==j or j+2==i)) for i in range(4) for j in range(4)):
            sp+=1
    assert (gl,sp,gl//sp)==(20160,720,28)
    return gl,sp

if __name__=='__main__':
    for p in (2,3): print('field matrices local automorphisms',test(p))
    for q in (2,3,4,5):
        for m in (1,2,3):
            idx=order_index(q,m)
            assert (idx==1)==(q==2 and m==1)
    assert order_index(2,2)==28
    print('binary rank two group census GL4 Sp4',binary_sp4_census())
    print('VERIFY_OK all_linear_matrices=20195 finite_fields=2 group_order_cases=12 sp4_direct=65536')
