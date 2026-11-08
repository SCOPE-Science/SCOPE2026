"""Independent exact finite checks for relative co-connected complexes of complete bipartite graphs."""
from itertools import combinations, permutations
from math import comb
from collections import defaultdict


def binom(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0


def connected(nodes,L,R):
    if len(nodes)<=1:return True
    return bool(nodes & L) and bool(nodes & R)


def model(a,b,x,y,r):
    L=set(range(a));R=set(range(a,a+b));A=set(range(x)) | set(range(a,a+y))
    U=(L|R)-A;M=len(U);k=M-r
    assert k>=1
    if not A:
        if r==1: caps=(a,b)
        else: caps=(a-1,b-1)
    elif A & L and A & R: caps=(a-x,b-y)
    elif A<=L: caps=(a-x,b-1)
    else: caps=(a-1,b-y)
    def valid(S): return len(S)<=k and len(S&L)<=caps[0] and len(S&R)<=caps[1]
    facets={frozenset((L|R)-(A|set(F))) for F in combinations(sorted(U),r) if connected(set(F)|A,L,R)}
    assert facets
    family={frozenset(S) for d in range(k+1) for S in combinations(sorted(U),d) if valid(set(S))}
    actual={frozenset(S) for F in facets for d in range(len(F)+1) for S in combinations(sorted(F),d)}
    assert family==actual, (a,b,x,y,r)
    f=[sum(len(S)==i for S in family) for i in range(k+1)]
    beta=(-1)**(k-1)*sum((-1)**(i-1)*f[i] for i in range(k+1))
    if not A:
        beta_expected=1 if r==1 else binom(M-1,k)-binom(b-1,k-a)-binom(a-1,k-b)
    elif A & L and A & R:
        beta_expected=binom(M-1,k)
    elif A <= L:
        beta_expected=binom(M-1,k)-binom(a-x-1,k-b)
    else:
        beta_expected=binom(M-1,k)-binom(b-y-1,k-a)
    assert beta==beta_expected,(a,b,x,y,r,beta,beta_expected)
    return L,R,A,U,k,f,beta,actual


def sign_perm(lst,perm):
    inv=[perm[v] for v in lst]
    return (-1)**sum(inv[i]>inv[j] for i in range(len(inv)) for j in range(i+1,len(inv)))


def signed_fixed_trace(family,perm,k):
    signed=0
    for S in family:
        if frozenset(perm[v] for v in S)!=S:continue
        lst=sorted(S)
        # permutation signature relative to sorted domain, independent of labels.
        image=[perm[v] for v in lst]
        s=(-1)**sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        signed+=(-1)**(len(S)-1)*s
    return (-1)**(k-1)*signed


def exterior_trace(perm, U, k):
    if k<0:return 0
    U=set(U);cycles=[];unseen=set(U)
    while unseen:
        p=min(unseen); cycle=[];v=p
        while v not in cycle:
            cycle.append(v);unseen.remove(v);v=perm[v]
        cycles.append(len(cycle))
    coeff=[1]+[0]*len(U)
    for ell in cycles:
        for j in range(len(U)-ell,-1,-1):
            coeff[j+ell]+=(-1)**(ell-1)*coeff[j]
    # divide by 1+t
    aug=[0]*(len(U))
    for j in range(len(U)):
        aug[j]=coeff[j]-(aug[j-1] if j else 0)
    return aug[k] if k<len(aug) else 0


def char_formula(a,b,x,y,r,perm):
    L=set(range(a));R=set(range(a,a+b));A=set(range(x))|set(range(a,a+y)); U=(L|R)-A
    k=len(U)-r
    out=exterior_trace(perm,U,k)
    if not A and r>=2:
        out-=sign_perm(sorted(L),perm)*exterior_trace(perm,R,k-a)
        out-=sign_perm(sorted(R),perm)*exterior_trace(perm,L,k-b)
    elif A and not (A&L and A&R):
        if A<=L:
            out-=sign_perm(sorted(R),perm)*exterior_trace(perm,L-A,k-b)
        else:
            out-=sign_perm(sorted(L),perm)*exterior_trace(perm,R-A,k-a)
    return out


def rank_mod2(mats):
    basis={}
    for m in mats:
        t=m
        while t:
            p=t.bit_length()-1
            if p in basis: t^=basis[p]
            else:
                basis[p]=t;break
    return len(basis)


def check_homology(family,k):
    faces=[[tuple(sorted(S)) for S in family if len(S)==i] for i in range(k+1)]
    idx=[{f:j for j,f in enumerate(row)} for row in faces]
    ranks=[0]*(k+1)
    for i in range(1,k+1):
        cols=[sum(1<<idx[i-1][f[:j]+f[j+1:]] for j in range(i)) for f in faces[i]]
        ranks[i]=rank_mod2(cols)
    # reduced complex includes empty face C_{-1}; rank d0=1 if a vertex exists
    ranks[0]=1
    return [len(faces[i])-ranks[i]- (ranks[i+1] if i<k else 0) for i in range(1,k+1)]

cases=0;hom_cases=0;trace_cases=0
for a in range(2,6):
 for b in range(2,6):
  for x in range(a+1):
   for y in range(b+1):
    M=a+b-x-y
    for r in range(1,M):
     L,R,A,U,k,f,beta,family=model(a,b,x,y,r)
     cases+=1
     if M<=8:
      hb=check_homology(family,k)
      assert hb == [0]*(k-1)+[beta],(a,b,x,y,r,hb,beta)
      hom_cases+=1
     perm={v:v for v in range(a+b)}
     # reverse each unrooted shore (fix all A)
     for side in [sorted(L-A),sorted(R-A)]:
      for v,w in zip(side,reversed(side)):perm[v]=w
     char=signed_fixed_trace(family,perm,k)
     expect=char_formula(a,b,x,y,r,perm)
     assert char==expect,(a,b,x,y,r,char,expect)
     trace_cases+=1
print(f'CASES_OK={cases} HOMOLOGY_MOD2_OK={hom_cases} EQUIVARIANT_TRACES_OK={trace_cases}')
print('ALL_VERIFY_OK')
