#!/usr/bin/env python3
"""Exact finite-field tests of weight-zero Rota--Baxter cycle-resonance statements."""
import itertools

def rb_zero(n,p,perm,w,R):
    # R[i][s] = coefficient at e_s in R(e_i)
    for i in range(n):
        for j in range(n):
            lhs=[0]*n
            for s in range(n):
                lhs[perm[s]]=(lhs[perm[s]]+w[s]*R[i][s]*R[j][s])%p
            rhs=[0]*n
            for s in range(n):
                # R(e_i)e_j contributes w_j*R[i][j] e_perm[j]
                # e_i R(e_j) contributes w_i*R[j][i] e_perm[i]
                rhs[s]=(w[j]*R[i][j]*R[perm[j]][s]+w[i]*R[j][i]*R[perm[i]][s])%p
            if lhs != rhs:
                return False
    return True

def cycles(perm):
    seen=set();out=[]
    for i in range(len(perm)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:
            seen.add(j);c.append(j);j=perm[j]
        assert j==i
        out.append(c)
    return out

def allowed(n,p,perm,diag):
    cs=cycles(perm)
    active={c[0] for c in cs if diag[c[0]]}
    return all((all((diag[v]!=0)==(c[0] in active) for v in c) and (not diag[c[0]] or (p!=2 and (pow(2,len(c),p)==1)))) for c in cs)

def construct(n,p,perm,w,enabled):
    R=[[0]*n for _ in range(n)]
    for c in cycles(perm):
        if c[0] not in enabled:continue
        assert p!=2 and pow(2,len(c),p)==1
        d=1
        for i in c:
            R[i][i]=d;d=d*pow(2,-1,p)%p
    return R

checks=0
for n,p in [(2,2),(2,3),(2,5),(2,7),(3,3)]:
    perm=list(range(1,n))+[0]
    w=[1]*n
    good=[]
    for t in itertools.product(range(p), repeat=n*n):
        R=[list(t[n*i:n*(i+1)]) for i in range(n)]
        if rb_zero(n,p,perm,w,R):
            good.append(R)
            assert allowed(n,p,perm,[R[i][i] for i in range(n)])
        checks+=1
    print('EXHAUSTIVE',n,p,'matrices',p**(n*n),'RB',len(good),'ranks_nondiagonal',sum(any(R[i][j] for i in range(n) for j in range(n) if i!=j) for R in good))
    assert (len(good)>1)==(p!=2 and pow(2,n,p)==1)
    if n==2 and p==3:
        assert len(good)==5
        # char3: zero + nonzero diagonal and rank-one exceptional branches
        assert sum(any(R[i][j] for i in range(n) for j in range(n) if i!=j) for R in good)==2

for n,perm,w,p in [
(2,[1,0],[1,2],3),
(3,[1,2,0],[1,3,2],7),
(4,[1,0,3,2],[1,2,2,1],3),
(5,[1,2,0,4,3],[1,2,3,1,2],7),
(5,[1,2,0,4,3],[1,2,3,1,2],3),
(6,[1,2,0,4,5,3],[3,2,1,1,1,2],7),
]:
    cs=cycles(perm)
    resonant=[c[0] for c in cs if p!=2 and pow(2,len(c),p)==1]
    for mask in range(1<<len(resonant)):
        enabled={resonant[i] for i in range(len(resonant)) if mask>>i&1}
        R=construct(n,p,perm,w,enabled)
        assert rb_zero(n,p,perm,w,R)
        assert allowed(n,p,perm,[R[i][i] for i in range(n)])
        checks+=1
    print('WEIGHTED',n,p,'cycles',list(map(len,cs)),'resonant',len(resonant),'supports',1<<len(resonant))

# Rank one and full-rank operators on the unweighted 3-cycle over F7:
p=7;n=3;perm=[1,2,0];w=[1,1,1]
Rdiag=construct(n,p,perm,w,{0})
assert rb_zero(n,p,perm,w,Rdiag)
f=[1,4,2]
Rone=[f[i:i+1]*3 for i in range(n)] # rows constant f_i
assert rb_zero(n,p,perm,w,Rone)
assert all(sum(x%p!=0 for x in row)==3 for row in Rone)
print('UNWEIGHTED_3_CYCLE rank_one_and_full_rank PASS')
print('VERIFY_OK checks',checks)
