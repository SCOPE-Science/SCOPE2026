"""Independent combinatorial validators of the proposed all-length identities.
The proof is mathematical; these are finite diagnostic checks, not infinite certification.
"""
from collections import Counter

def direct_update(w):
    n=len(w)
    out=[]
    for i,bit in enumerate(w):
        ones=sum(w[j] for j in range(n)
                 if j != i and j != (i-1)%n and j != (i+1)%n)
        deg=n-3
        out.append(1 if 2*ones>deg else 0 if 2*ones<deg else bit)
    return out

def formula(m,t):
    if t%2==0:
        return [1]*(t+2)+[0,1]*(m-t-2)+[0]*(t+2)
    return [0]*(t+2)+[1,0]*(m-t-2)+[1]*(t+2)

def runs_cyclic(w):
    n=len(w)
    assert 0<sum(w)<n
    # Count maximal cyclic runs of zero and one, with a canonical cut at a change.
    i=next(i for i in range(n) if w[i]!=w[(i-1)%n])
    vals=[]
    cur=w[i];k=0
    for j in range(n):
        b=w[(i+j)%n]
        if b==cur:k+=1
        else:
            vals.append((cur,k));cur=b;k=1
    vals.append((cur,k))
    return vals

for m in range(4,41):
    N=2*m
    w=formula(m,0)
    assert len(w)==N and sum(w)==m
    for t in range(m-2):
        assert w==formula(m,t)
        assert direct_update(w)==formula(m,t+1)
        assert sum(w)==m
        w=direct_update(w)
    assert w==formula(m,m-2)
    assert direct_update(w)==[1-b for b in w]
    assert direct_update(direct_update(w))==w
    assert all(formula(m,t)!=formula(m,t+2) for t in range(m-3))

# Independently verify the odd-run counting identity for a wide set of patterns.
for N in range(7,17,2):
    m=(N-1)//2
    count_eq=0
    for mask in range(1<<N):
        if mask.bit_count()!=m:continue
        w=[(mask>>i)&1 for i in range(N)]
        R=runs_cyclic(w)
        a=sum(bit==1 and length>=2 for bit,length in R)
        b=sum(bit==0 and length>=2 for bit,length in R)
        y=direct_update(w)
        assert sum(y)==m+1-a-b
        if sum(y)==m:
            count_eq+=1
            assert w==y and (a,b)==(0,1)
        else:assert sum(y)<m
    assert count_eq==N
    print(f'odd N={N} middle-layer equality states={count_eq} verified')
print('SYMBOLIC_CHECK_OK: even m=4..40, odd N=7..15')
