# Decisive test: S = UT3(F3) (Heisenberg, order 27), G = S ⋊ <t>, t=diag(-1,1,1) (order 2).
# P = <e_c> noncentral line, fully normalized, noncentric. Compare N_{Lambda_F}(P) vs Lambda_{N_F(P)}.
import itertools
from collections import defaultdict
p=3
def mat(a,b,c): return (a%p,b%p,c%p)
def mmul(X,Y):
    a1,b1,c1=X; a2,b2,c2=Y
    return ((a1+a2)%p,(b1+b2+a1*c2)%p,(c1+c2)%p)
def minv(X):
    a,b,c=X
    return ((-a)%p,(-b+a*c)%p,(-c)%p)
def mconj(G,X): return mmul(mmul(G,X),minv(G))
S=[mat(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
assert len(S)==27
Z=[x for x in S if all(mmul(x,y)==mmul(y,x) for y in S)]
print("center:",Z)  # expect [(0,0,0),(0,1,0),(0,2,0)]
# t action: (a,b,c)->(-a,-b,c)
def tact(X):
    a,b,c=X; return ((-a)%p,(-b)%p,c)
for x in S:
    for y in S[:3]:
        assert mmul(tact(x),tact(y))==tact(mmul(x,y))
# G = S x C2; elements (s,e). conj action for fusion: Hom_F(A,B)={c_g|_A}.
def gconj(g,X):
    s,e=g
    Y=mconj(s,X)
    if e: Y=tact(Y)
    return Y
G=[(s,e) for s in S for e in (0,1)]
def gmul(g1,g2):
    (s1,e1),(s2,e2)=g1,g2
    s2t = s2 if e1==0 else tact(s2)
    return (mmul(s1,s2t),e1^e2)
def ginv(g):
    s,e=g
    if e==0: return (minv(s),0)
    return (tact(s),1)  # (s,1)^{-1}: solve (s,1)(x,i)=(1,0): i=1, s*tact(x)=1 -> x=tact(s^{-1})=tact(s)^{-1}... check: tact(s)=? claim inverse (tact(s),1): (s,1)(tact(s),1) = (s*tact(tact(s)),0)=(s*s,0)?? wrong unless s^2=1. recompute: need s * tact(x) = 0 -> tact(x)=minv(s) -> x=tact(minv(s)). so inverse = (tact(minv(s)),1).
print("check inverse:")
def ginv2(g):
    s,e=g
    if e==0: return (minv(s),0)
    return (tact(minv(s)),1)
for g in G:
    assert gmul(g,ginv2(g))==((0,0,0),0) and gmul(ginv2(g),g)==((0,0,0),0), g
print("inverses ok")
ginv=ginv2
# subgroups of S
def closure(gens):
    H={(0,0,0)}
    ch=True
    while ch:
        ch=False
        for h in list(H):
            for g in gens:
                for x in (mmul(h,g),mmul(g,h),minv(g)):
                    if x not in H: H.add(x); ch=True
    return frozenset(H)
subs=set()
for r in range(1<<9):
    gens=[S[i] for i in range(9) if (r>>i)&1]
    subs.add(closure(gens))
# also singletons beyond first 9? S has 27 elements; subsets from first 9 may miss. Use all cyclic + pairs.
for x in S: subs.add(closure([x]))
for x in S:
    for y in S: subs.add(closure([x,y]))
subs=sorted(subs,key=lambda h:(len(h),sorted(h)))
print("num subgroups:",len(subs),sorted([len(h) for h in subs]))
NS=len(subs)
# normalizer/centralizer
def isnorm(g,H):
    return all(gconj((g,0),h) in H for h in H)
def centra(H):
    return [g for g in S if all(mmul(g,h)==mmul(h,g) for h in H)]
def norma(H):
    return [g for g in S if isnorm(g,H)]
P=frozenset([x for x in S if x[0]==0 and x[2]==0 or x==(0,0,0)])
P=frozenset([(0,0,0),(0,0,1),(0,0,2)])
print("P size",len(P),"N_S(P)",len(norma(P)),"C_S(P)",len(centra(P)))
# F-morphisms via G: Hom_F(A,B) = {c_g|_A : gAg^-1=B}
def conjmap(g,A):
    return {x:gconj(g,x) for x in A}
# enumerate all F-isos: for each g, each A<=S: B=gAg^-1, map
from collections import defaultdict
isoF=set()
def kkey(d,c,m): return (tuple(sorted(d)),tuple(sorted(c)),tuple(sorted((a,m[a]) for a in d)))
for g in G:
    for A in subs:
        B=frozenset(gconj(g,x) for x in A)
        m={x:gconj(g,x) for x in A}
        isoF.add(kkey(set(A),set(B),m))
print("F-isos:",len(isoF))
def dec(k):
    d,c,m=k; return (set(d),set(c),dict(m))
# F-class of P
Fp=[k for k in isoF if set(dec(k)[0])==set(P)]
targets=set(tuple(sorted(dec(k)[1])) for k in Fp)
print("F-class(P) size (subgroups):",len(targets))
for t in targets: print("  ",sorted(t))
# check fully normalized: |N_S| maximal in class?
for t in targets:
    print("N_S size of",sorted(t),len(norma(set(t))))
