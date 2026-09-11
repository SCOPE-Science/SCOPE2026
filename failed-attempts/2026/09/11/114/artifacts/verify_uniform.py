"""Independent verifier: exact integer-orientation certificate for ONE uniform pair.
Recomputes from scratch (no imports from audit scripts) that for the moment-curve
configuration, sigma={0,2,4,6}, tau={1,3,5} satisfies:
  strict conv-hull intersection after EVERY vertex deletion v in 0..9.
Also verifies non-degeneracy (all cross-quadruples spanning the pair uncoplanar),
so strict_meet == true closed-hull intersection on these instances.
"""
import itertools
P = [(i, i*i, i*i*i) for i in range(10)]
def det3(M):
    (a,b,c),(d,e,f),(g,h,k) = M
    return a*(e*k-f*h)-b*(d*k-f*g)+c*(d*h-e*g)
def ori(a,b,c,d):
    pa,pb,pc,pd = P[a],P[b],P[c],P[d]
    return det3([[pb[j]-pa[j] for j in range(3)],[pc[j]-pa[j] for j in range(3)],[pd[j]-pa[j] for j in range(3)]])
def pierce(p,q,a,b,c):
    s1=ori(p,a,b,c); s2=ori(q,a,b,c)
    if s1==0 or s2==0 or (s1>0)==(s2>0): return False
    t=[ori(p,q,a,b),ori(p,q,b,c),ori(p,q,c,a)]
    if any(v==0 for v in t): return False
    return (t[0]>0)==(t[1]>0)==(t[2]>0)
def inset(x,a,b,c,d):
    o=ori(a,b,c,d)
    if o==0: return False
    return ori(x,b,c,d)*o>0 and ori(x,a,c,d)*ori(b,a,c,d)>0 and ori(x,a,b,d)*ori(c,a,b,d)>0 and ori(x,a,b,c)*ori(d,a,b,c)>0
def meet(A,B):
    A=list(A);B=list(B)
    for x in A:
        for q in itertools.combinations(B,4):
            if inset(x,*q): return True
    for x in B:
        for q in itertools.combinations(A,4):
            if inset(x,*q): return True
    for e in itertools.combinations(A,2):
        for t in itertools.combinations(B,3):
            if pierce(e[0],e[1],*t): return True
    for e in itertools.combinations(B,2):
        for t in itertools.combinations(A,3):
            if pierce(e[0],e[1],*t): return True
    return False
S=[0,2,4,6]; T=[1,3,5]
ok=True
for v in range(10):
    A=[x for x in S if x!=v]; B=[x for x in T if x!=v]
    assert len(A)>=2 and len(B)>=2, "face nonempty audit"
    r=meet(A,B)
    # non-degeneracy: every cross quadruple uncoplanar
    degen=[q for q in itertools.combinations(A+B,4) if ori(*q)==0]
    print(f"del {v}: A={A} B={B} meet={r} degen={len(degen)}")
    ok = ok and r and not degen
print("VERIFY_UNIFORM:", "OK" if ok else "FAIL")
