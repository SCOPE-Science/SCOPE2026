#!/usr/bin/env python3
"""Self-contained exact checks for consecutive-size star decompositions of bicliques."""

def rep(n,k):
    return (n//k >= n%k) if n>=0 else False

def star_sizes(n,k):
    assert rep(n,k)
    q,r=divmod(n,k)
    return [k+1]*r+[k]*(q-r)

def construct(k,a,b):
    """Return an orientation binary matrix: 1 means A -> B, 0 means B -> A."""
    assert k>=3 and 1<=a<=b and a+b>=k*k-1
    if rep(b,k):
        M=[[1]*b for _ in range(a)]
    elif rep(a,k):
        M=[[0]*b for _ in range(a)]
    else:
        assert a>=k+2
        q,r=divmod(b,k)
        assert 1<=q<r<=k-1
        T=b*(a-k)
        assert T>=k*(k-1)
        L=(T+k)//(k+1)
        J=T-k*L
        assert 0<=J<=L<=a*q
        assert a*q*(k+1)-T==k*b-a*(r-q)>0
        # Give each of a vertices at most q slots, each slot initially of size k.
        slots=[0]*a
        left=L
        for i in range(a):
            slots[i]=min(q,left); left-=slots[i]
        assert left==0
        rem=J
        degrees=[]
        for x in slots:
            upgrades=min(x,rem);rem-=upgrades
            degrees.append(k*x+upgrades)
        assert rem==0 and max(degrees)<=q*(k+1)<=b
        assert sum(degrees)==T
        # Simple bipartite Havel--Hakimi realization of prescribed row and equal column sums.
        capacity=[a-k]*b
        M=[[0]*b for _ in range(a)]
        for i,deg in sorted(enumerate(degrees),key=lambda p:-p[1]):
            chosen=sorted(range(b),key=lambda j:-capacity[j])[:deg]
            assert all(capacity[j]>0 for j in chosen)
            for j in chosen:
                M[i][j]=1;capacity[j]-=1
        assert all(z==0 for z in capacity)
    for i in range(a):
        assert rep(sum(M[i]),k)
    for j in range(b):
        assert rep(a-sum(M[i][j] for i in range(a)),k)
    # Explicitly create the stars and certify exact edge coverage.
    used=set()
    for i in range(a):
        outs=[j for j in range(b) if M[i][j]]
        offset=0
        for size in star_sizes(len(outs),k):
            for j in outs[offset:offset+size]:
                assert (i,j) not in used; used.add((i,j))
            offset+=size
        assert offset==len(outs)
    for j in range(b):
        outs=[i for i in range(a) if not M[i][j]]
        offset=0
        for size in star_sizes(len(outs),k):
            for i in outs[offset:offset+size]:
                assert (i,j) not in used; used.add((i,j))
            offset+=size
        assert offset==len(outs)
    assert len(used)==a*b
    return M

def independent_brute_exist(k,a,b):
    """Exact DP over each B-column's A->B mask; feasible for a <= 5."""
    from itertools import product
    allowedA={t for t in range(b+1) if rep(t,k)}
    allowedB={t for t in range(a+1) if rep(t,k)}
    col_masks=[m for m in range(1<<a) if a-m.bit_count() in allowedB]
    states={(0,)*a}
    for j in range(b):
        nxt=set()
        for state in states:
            for m in col_masks:
                vec=tuple(state[i]+((m>>i)&1) for i in range(a))
                if all(v<=b and v<=max(allowedA) for v in vec):nxt.add(vec)
        states=nxt
    return any(all(x in allowedA for x in vec) for vec in states)

def run():
    checks=0
    # Check the exact representability criterion, including the Frobenius boundary.
    for k in range(3,60):
        for n in range(0,k*k+2):
            assert rep(n,k)==any(n==i*k+j*(k+1) for i in range(n//k+1) for j in range(n//(k+1)+1))
            checks+=1
    print('NUMERICAL_SEMIGROUP_AND_FROBENIUS_TEST_PASS',checks)
    nmat=0
    for k in range(3,12):
        cond=k*k-1
        cap=k*(k-1)-1
        for a in range(1,cond//2+1):
            for b in range(max(a,cond-a),cap+1):
                M=construct(k,a,b)
                assert len(M)==a and all(len(row)==b for row in M)
                nmat+=1
    print('ALL_NONTRIVIAL_SHORE_PAIRS_AND_ORIENTATIONS_PASS',nmat)
    nlarge=0
    for k in (12,16,20,25):
        cap=k*(k-1)-1
        for a in (k+2,k+3,k+4):
            if rep(a,k):continue
            for b in (cap,cap-k,cap-2*k):
                if a<=b and a+b>=k*k-1 and not rep(b,k):
                    construct(k,a,b); nlarge+=1
        print('LARGE_PARAMETER_BOUNDARY_PASS',k)
    print('LARGE_BOUNDARY_ORIENTATIONS_PASS',nlarge)
    nsmall=0
    for k in (3,4):
        for a in range(1,5):
            for b in range(a,10):
                if a*b>35:continue
                exists=independent_brute_exist(k,a,b)
                if a+b>=k*k-1:assert exists
                if (a,b)==(k-1,k*(k-1)-1):assert not exists
                nsmall+=1
    print('INDEPENDENT_COMPLETE_ORIENTATION_DP_PASS',nsmall)
    for k in range(3,50):
        a=k-1;b=k*(k-1)-1
        assert a+b==k*k-2 and not rep(b,k) and a<k
    print('SHARP_FORBIDDEN_BICLIQUE_FAMILY_PASS')
    print('VERIFY_OK')
if __name__=='__main__':run()
