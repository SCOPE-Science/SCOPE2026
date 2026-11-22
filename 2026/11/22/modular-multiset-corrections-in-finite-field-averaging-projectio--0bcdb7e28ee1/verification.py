#!/usr/bin/env python3
"""Direct small-field checks for finite-field averaging projection classification."""
from itertools import product, permutations, combinations_with_replacement
from math import comb, factorial
from collections import Counter

def stirling(n, r):
    t = [[0]*(r+1) for _ in range(n+1)]
    t[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,min(i,r)+1):
            t[i][j] = t[i-1][j-1]+j*t[i-1][j]
    return t[n][r]

def theory(n,q):
    return {r:sum(comb(n,s)*q**(s-r)*stirling(s,r) for s in range(r,n+1)) for r in range(n+1)}

def rank(M,q):
    A=[row[:] for row in M]; n=len(A); s=0
    for col in range(n):
        pos=next((i for i in range(s,n) if A[i][col]),None)
        if pos is None:continue
        A[pos],A[s]=A[s],A[pos]
        z=pow(A[s][col],-1,q)
        for j in range(col,n): A[s][j]=(A[s][j]*z)%q
        for i in range(n):
            if i==s:continue
            z=A[i][col]
            if z:
                for j in range(col,n):A[i][j]=(A[i][j]-z*A[s][j])%q
        s+=1
    return s

def good(v,n,q):
    M=[v[i*n:(i+1)*n] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if sum(M[i][k]*M[k][j] for k in range(n))%q!=M[i][j]:return False
    # Bilinear averaging identities on all basis pairs.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                lhs=M[k][i]*M[k][j]%q
                if lhs != M[j][i]*M[k][j]%q:return False
                if lhs != M[i][j]*M[k][i]%q:return False
    return True

def canon(M,n,perms):
    return min(tuple(M[p[i]*n+p[j]] for i in range(n) for j in range(n)) for p in perms)

def m_formula(s,q,p):
    B=comb(q//p+s//p-1,s//p) if s%p==0 else 0
    return (comb(q+s-1,s)-B)//q

def classes_theory(n,q,p):
    # Zero-coordinate component (size one each), and for every s, m_s block types.
    dp={(0,0):1}
    for s in range(1,n+1):
        t=m_formula(s,q,p)
        nxt=dp.copy()
        for j in range(1,n//s+1):
            mult=comb(t+j-1,j)
            for (v,r),cnt in dp.items():
                if v+j*s<=n:nxt[(v+j*s,r+j)]=nxt.get((v+j*s,r+j),0)+cnt*mult
        dp=nxt
    out=Counter()
    for (v,r),cnt in dp.items():out[r]+=cnt # one zero-coordinate remainder n-v, any length
    return dict(out)

def verify(q,n,p):
    perms=list(permutations(range(n)))
    ranks=Counter(); classes={}
    for v in product(range(q),repeat=n*n):
        if good(v,n,q):
            k=rank([list(v[i*n:(i+1)*n]) for i in range(n)],q)
            ranks[k]+=1
            classes[canon(v,n,perms)]=k
    exp=theory(n,q)
    observed=dict(sorted(ranks.items()))
    expected=dict(sorted(exp.items()))
    orb=Counter(classes.values())
    eor=classes_theory(n,q,p)
    assert observed==expected,(q,n,observed,expected)
    assert dict(orb)==eor,(q,n,orb,eor)
    print('PASSED q=%d n=%d total=%d labeled_by_rank=%s orbits_by_rank=%s'%(q,n,sum(ranks.values()),expected,eor))

if __name__=='__main__':
    for q,n,p in [(2,1,2),(2,2,2),(2,3,2),(2,4,2),(3,2,3),(3,3,3),(5,2,5)]:verify(q,n,p)
    print('FINITE_FIELD_AVERAGING_ORBIT_CENSUS_VERIFIED')

# Extension field checks: 4 = F_2[z]/(z^2+z+1), 9 = F_3[z]/(z^2+1).
def extension_table(p, neg_c, neg_b):
    q=p*p
    add=[[((a%p+b%p)%p)+p*((a//p+b//p)%p) for b in range(q)] for a in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            A,B=a%p,a//p; C,D=b%p,b//p
            row.append(((A*C+neg_c*B*D)%p)+p*((A*D+B*C+neg_b*B*D)%p))
        mul.append(row)
    inv={a:next(b for b in range(1,q) if mul[a][b]==1) for a in range(1,q)}
    return add,mul,inv

def check_extension(n,p,neg_c,neg_b):
    q=p*p; add,mul,inv=extension_table(p,neg_c,neg_b)
    ranks=Counter(); seen=set(); perms=list(permutations(range(n)))
    for v in product(range(q),repeat=n*n):
        M=[v[i*n:(i+1)*n] for i in range(n)]
        ok=True
        for i in range(n):
            for j in range(n):
                x=0
                for k in range(n):x=add[x][mul[M[i][k]][M[k][j]]]
                if x!=M[i][j]:ok=False;break
            if not ok:break
        if not ok:continue
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    lhs=mul[M[k][i]][M[k][j]]
                    if lhs!=mul[M[j][i]][M[k][j]] or lhs!=mul[M[i][j]][M[k][i]]:
                        ok=False;break
                if not ok:break
            if not ok:break
        if not ok:continue
        ranks['all']+=1
        seen.add(canon(v,n,perms))
    assert ranks['all']==sum(theory(n,q).values()),(q,n,ranks,theory(n,q))
    assert len(seen)==sum(classes_theory(n,q,p).values()),(q,n,len(seen),classes_theory(n,q,p))
    print('PASSED extension field q=%d n=%d total=%d orbits=%d'%(q,n,ranks['all'],len(seen)))

if __name__=='__main__':
    check_extension(2,2,1,1)
    check_extension(2,3,2,0)
    print('EXTENSION_FIELD_AVERAGING_CENSUS_VERIFIED')

def check_multiset_character_formula(q,p,neg_c,neg_b,max_size=5):
    add,_,_=extension_table(p,neg_c,neg_b)
    for s in range(1,max_size+1):
        direct=0
        for arr in combinations_with_replacement(range(q),s):
            z=0
            for a in arr:z=add[z][a]
            if z==1:direct+=1
        assert direct==m_formula(s,q,p),(q,s,direct,m_formula(s,q,p))
    print('PASSED additive multiset character formula q=%d sizes=1..%d'%(q,max_size))

if __name__=='__main__':
    check_multiset_character_formula(4,2,1,1,6)
    check_multiset_character_formula(9,3,2,0,5)
    print('ALL_AVERAGING_CHECKS_VERIFIED')
