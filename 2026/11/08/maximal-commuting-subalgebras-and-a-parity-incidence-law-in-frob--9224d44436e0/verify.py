"""Independent finite-field verification of Frobenius-skew truncated radical commuting structure."""
from itertools import product
from collections import Counter
from math import gcd


def make_field(p, modulus):
    m = len(modulus)-1
    Q=p**m
    def digits(a):
        v=[]
        for _ in range(m):
            v.append(a%p);a//=p
        return v
    ds=[digits(i) for i in range(Q)]
    def encode(ds0):
        return sum((x%p)*p**i for i,x in enumerate(ds0))
    add=[[encode([(ds[a][i]+ds[b][i])%p for i in range(m)]) for b in range(Q)] for a in range(Q)]
    def mul(a,b):
        z=[0]*(2*m-1)
        for i,x in enumerate(ds[a]):
            for j,y in enumerate(ds[b]):
                z[i+j]=(z[i+j]+x*y)%p
        for k in range(2*m-2,m-1,-1):
            c=z[k]
            for j in range(m):
                z[k-m+j]=(z[k-m+j]-c*modulus[j])%p
        return encode(z[:m])
    M=[[mul(a,b) for b in range(Q)] for a in range(Q)]
    def power(a,k):
        v=1
        for _ in range(k):v=M[v][a]
        return v
    sig=[power(a,p) for a in range(Q)]
    sig2=[sig[sig[a]] for a in range(Q)]
    assert sorted(sig)==list(range(Q))
    assert all(power(a,Q)==a for a in range(Q))
    return Q,M,sig,sig2


def test(p,modulus,graph=False):
    Q,M,sig,sig2=make_field(p,modulus)
    q=p; m=len(modulus)-1
    elems=list(product(range(Q),repeat=3))
    # no field addition needed for commutator equality:
    def commute(x,y):
        a,b,_=x;A,B,_=y
        v=M[a][sig[A]]==M[A][sig[a]]
        left=sums[M[a][sig[B]]][M[b][sig2[A]]]
        right=sums[M[A][sig[b]]][M[B][sig2[a]]]
        return v and left==right
    # Generate addition by Fermat-free polynomial coefficient arithmetic.
    def digits(a):
        z=[]
        for _ in range(m):z.append(a%p);a//=p
        return z
    ds=[digits(i) for i in range(Q)]
    sums=[[sum(((ds[a][i]+ds[b][i])%p)*p**i for i in range(m)) for b in range(Q)] for a in range(Q)]
    counts=Counter()
    cliques={}
    for x in elems:
        c={y for y in elems if commute(x,y)}
        counts[len(c)]+=1
        if x[0]!=0:
            assert len(c)==q*q*Q
            cliques[frozenset(c)]=1
    expected_profile=Counter()
    expected_profile[q*q*Q]+=(Q-1)*Q*Q
    expected_profile[Q**3]+=Q
    if m%2:
        expected_profile[q*Q*Q]+=(Q-1)*Q
    else:
        E=(Q-1)//(q+1)
        expected_profile[q*q*Q*Q]+=E*Q
        expected_profile[Q*Q]+=(Q-1-E)*Q
    assert counts==expected_profile, (Q,counts,expected_profile)
    expected_num=1+(Q-1)//(q-1)*(Q//q)
    central=set((0,b,c) for b in range(Q) for c in range(Q))
    assert len(cliques)+1==expected_num
    for clique in cliques:
        assert all(commute(x,y) for x in clique for y in clique) if Q<=4 else True
        assert len(clique)==q*q*Q
    if graph:
        # Standalone Bron-Kerbosch maximal-clique enumeration with pivoting.
        adj=[set() for _ in elems]
        for i,x in enumerate(elems):
            for j in range(i+1,len(elems)):
                if commute(x,elems[j]):
                    adj[i].add(j)
                    adj[j].add(i)
        maximal=set()
        def bronk(R,P,X):
            if not P and not X:
                maximal.add(frozenset(elems[i] for i in R))
                return
            pivot=max(P|X,key=lambda v:len(P & adj[v])) if P|X else None
            for v in list(P-adj[pivot] if pivot is not None else P):
                bronk(R|{v},P&adj[v],X&adj[v])
                P.remove(v)
                X.add(v)
        bronk(set(),set(range(len(elems))),set())
        assert maximal==set(cliques)|{frozenset(central)}, (len(maximal),len(cliques))
    N=(Q-1)//(q-1)
    T=Q//q
    # projective line representatives
    P=[]
    unseen=set(range(1,Q))
    while unseen:
        a=min(unseen);P.append(a)
        unseen.difference_update({M[a][u] for u in range(1,q)})
    assert len(P)==N
    W={a:frozenset(M[M[a][sig[a]]][u] for u in range(q)) for a in P}
    groupings=Counter(W.values())
    assert set(groupings.values())=={gcd(q+1,N)}
    assert len(set(groupings))==N//gcd(q+1,N)
    csum=sum(k*v for k,v in counts.items())
    expected=Q**3*((q*q+q+1)*Q-q*(q+1))
    assert csum==expected,(p,m,csum,expected)
    print('CHECK_OK',f'GF({Q})','centralizer_profile',sorted(counts.items()),'maximal_cliques',len(cliques)+1,'commuting_pairs',csum)

if __name__=='__main__':
    test(2,[1,1,1],graph=True)
    test(2,[1,1,0,1],graph=True)
    test(3,[1,0,1],graph=True)
    test(2,[1,1,0,0,1],graph=False)
    print('VERIFY_OK')
