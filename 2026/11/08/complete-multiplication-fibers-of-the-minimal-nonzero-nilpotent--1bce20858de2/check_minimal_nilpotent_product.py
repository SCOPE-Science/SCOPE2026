"""Independent exhaustive census of products from the minimal nilpotent orbit.
No external modules are required. Finite fields q=2,3,4,5,8 implemented exactly.
"""
from collections import Counter
from itertools import product

FIELDS={2:(2,0),3:(3,0),4:(2,0b111),5:(5,0),8:(2,0b1011)}

def mul(a,b,q):
    p,mod=FIELDS[q]
    if mod==0:return a*b%p
    z=0
    while b:
        if b&1:z^=a
        b >>=1;a<<=1
        if a & q:a^=mod
    return z

def add(a,b,q):
    p,mod=FIELDS[q]
    return a^b if mod else (a+b)%p

def dot(u,v,q):
    z=0
    for a,b in zip(u,v):z=add(z,mul(a,b,q),q)
    return z

def canonical(u,q):
    f=next(z for z in u if z)
    inverse=next(x for x in range(1,q) if mul(f,x,q)==1)
    return tuple(mul(a,inverse,q) for a in u)

def outer(u,v,q):
    return tuple(mul(a,b,q) for a in u for b in v)

def matrix_product(A,B,n,q):
    out=[]
    for i in range(n):
        for j in range(n):
            z=0
            for k in range(n):z=add(z,mul(A[i*n+k],B[k*n+j],q),q)
            out.append(z)
    return tuple(out)

def trace(A,n,q):
    z=0
    for i in range(n):z=add(z,A[i*n+i],q)
    return z

def predicted(C,n,q,N):
    if not any(C):
        F=(q**(n-1)-1)*q**(n-2)
        G=q**(n-1)*(q**(n-2)-1)
        return N*N-((q**n-1)*q**(n-1))*F-N*G
    rows=[C[i*n:(i+1)*n] for i in range(n)]
    nr=[r for r in rows if any(r)]
    row=nr[0]
    for r in nr:
        if r!=row and not any(tuple(mul(t,rr,q) for rr in row)==r for t in range(q)):
            return 0
    if trace(C,n,q):return (q**(n-1)-1)*q**(n-2)
    return q**(n-1)*(q**(n-2)-1)

def run(n,q):
    V=list(product(range(q),repeat=n))
    reps={canonical(u,q) for u in V if any(u)}
    Nset=[]
    for u in sorted(reps):
        for v in V:
            if any(v) and dot(u,v,q)==0:Nset.append(outer(u,v,q))
    N=len(Nset)
    expected=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert N==expected and len(set(Nset))==N
    counts=Counter()
    for A in Nset:
        for B in Nset:
            counts[matrix_product(A,B,n,q)]+=1
    assert sum(counts.values())==N*N
    for C in product(range(q),repeat=n*n):
        pred=predicted(C,n,q,N)
        assert counts[C]==pred,(n,q,C,counts[C],pred)
    zero=(0,)*(n*n)
    trace_0_nonzero=sum(1 for C,f in counts.items() if C!=zero and trace(C,n,q)==0)
    trace_nonzero=sum(1 for C,f in counts.items() if trace(C,n,q)!=0)
    print(f'PASS n={n} q={q} nilpotent_orbit={N} total_pairs={N*N} image={len(counts)} zero_fiber={counts[zero]} trace0_nonzero_targets={trace_0_nonzero} trace_nonzero_targets={trace_nonzero}')

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(3,5),(4,2)]:
        run(n,q)
    print('ALL_MINIMAL_NILPOTENT_PRODUCT_CHECKS_PASS')
