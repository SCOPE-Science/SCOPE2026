"""Verify MSS Example 5.21 core: p=3,k=7,j=3,n=10.
Rule 15 (Mathas), Henke summand count, block (3-core) separation.
Also probe a larger double-divisibility case for general obstruction.
"""
def padic(n,p):
    if n<0: return None
    d=[]
    if n==0: return [0]
    while n>0:
        d.append(n%p); n//=p
    return d

def prec_p(a,b,p):
    # a ≼_p b : for all i either a_i=0 or a_i=b_i
    da,db=padic(a,p),padic(b,p)
    L=max(len(da),len(db))
    da+= [0]*(L-len(da)); db+=[0]*(L-len(db))
    return all(ai==0 or ai==bi for ai,bi in zip(da,db))

def leq_p(a,b,p):
    # a ≤_p b digitwise ≤
    da,db=padic(a,p),padic(b,p)
    L=max(len(da),len(db))
    da+= [0]*(L-len(da)); db+=[0]*(L-len(db))
    return all(ai<=bi for ai,bi in zip(da,db))

def decomp(n,m,j,p):
    # [Delta(2^m,1^{n-2m}) : L(2^j,1^{n-2j})]
    if m==j: return 1
    if m<j: return 0
    import math
    a=(m-j)//p if (m-j)>=0 else None
    # floor for possibly negative handled: m>=j so m-j>=0
    af=(m-j)//p
    bf=(n-2*j+1)//p if (n-2*j+1)>=0 else None
    if bf is None or bf<0: return 0
    cond1=prec_p(af,bf,p)
    cond2=((m-j)%p==0) or ((n-m-j+1)%p==0)
    return 1 if (cond1 and cond2) else 0

p,n=3,10
print("== p=3,n=10 decomposition matrix [Delta_m : L_j] ==")
print("m\\j |", " ".join(f"j={j}" for j in range(5)))
for m in range(5):
    row=[decomp(n,m,j,p) for j in range(5)]
    print(f"m={m} |", row)
# Expected: m=0:[1,0,0,0,0]; m=1:[0,1,0,0,0]? check j=0 factor?
# MSS claims Delta(2,1^8) simple, Delta(2^2,1^6)=L(1^10)|L(2^2,1^6), Delta(2^3,1^4)=L(2^2,1^6)|L(2^3,1^4)
print()
print("Delta(2,1^8) factors:", [(j,decomp(n,1,j,p)) for j in range(5)])
print("Delta(2^2,1^6) factors:", [(j,decomp(n,2,j,p)) for j in range(5)])
print("Delta(2^3,1^4) factors:", [(j,decomp(n,3,j,p)) for j in range(5)])

print()
print("== Henke summand count for M(7,3), n=10, p=3 ==")
# M(lam=(n-j,j)=(7,3)); mu=(n-m,m), m=0..3; Y(mu) summand iff j-m <=_p n-2m
for m in range(4):
    print(f"m={m}: j-m={3-m}, n-2m={10-2*m}, summand={leq_p(3-m,10-2*m,p)}")
print("=> number of summands =", sum(leq_p(3-m,10-2*m,p) for m in range(4)))

print()
print("== 3-cores of (2^m,1^{10-2m}) ==")
def core(part,p):
    # naive rim-p-hook removal
    part=list(part)
    changed=True
    while changed:
        changed=False
        # try all rim hooks of length p? use beta numbers
        # beta numbers: part_i + (len-i)
        L=len(part)
        import itertools
        # brute force: remove rim hook of size p if possible via Young diagram search
        # represent diagram as set of cells
        cells={(r,c) for r in range(len(part)) for c in range(part[r])}
        # find rim hooks: connected skew shapes of size p with no 2x2 block whose removal leaves a partition
        # brute force over subsets is too big; instead use abacus
        break
    return None
# abacus method for p-core
def pcore(part,p):
    # beta numbers with enough beads
    L=len(part)+p*4
    beta=sorted([part[i]+L-1-i if i < len(part) else L-1-i for i in range(L)], reverse=False)
    # runners: bead positions mod p; slide all beads up as far as possible
    # for core: for each runner, beads occupy topmost positions
    from collections import defaultdict
    runners=defaultdict(list)
    for b in beta: runners[b%p].append(b)
    newbeads=[]
    for r in range(p):
        beads=sorted(runners[r])
        k=len(beads)
        # positions r, r+p, ..., r+(k-1)p
        newbeads.extend([r+t*p for t in range(k)])
    newbeads=sorted(newbeads, reverse=True)
    # convert back to partition
    newpart=[]
    for i,b in enumerate(newbeads):
        v=b-(L-1-i)
        newpart.append(v)
    # strip trailing <=0
    newpart=[v for v in newpart if v>0]
    return tuple(newpart)

for m in range(5):
    lam=tuple([2]*m+[1]*(10-2*m)) if m>0 else tuple([1]*10)
    print(f"m={m} {lam}: 3-core={pcore(list(lam),3)}")
