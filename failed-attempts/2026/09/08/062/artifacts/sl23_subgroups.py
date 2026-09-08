"""S3: subgroups of SL(2,3), Q8 normal Sylow, C3 quotient linears, S4-action 3-dim."""
import json
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def mat_inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
ID=mat(1,0,0,1)
def close(gens):
    S={idx[ID]}; stack=[idx[ID]]
    els={idx[g] for g in gens}
    S|=els; stack+=list(els)
    while stack:
        x=stack.pop()
        for y in list(S):
            for z in (mul(G[x],G[y]),mul(G[y],G[x])):
                k=idx[z]
                if k not in S: S.add(k); stack.append(k)
    return frozenset(S)
# all subgroups via successive adjoining
subs={frozenset([idx[ID]])}
changed=True
while changed:
    changed=False
    for H in list(subs):
        for g in G:
            H2=close([G[i] for i in H]+[g])
            if H2 not in subs: subs.add(H2); changed=True
subs=sorted(subs,key=lambda H:(len(H),sorted(H)))
print("nsubgroups:",len(subs),"orders:",sorted(len(H) for H in subs))
from collections import Counter
print(Counter(len(H) for H in subs))
# Q8 = elements with g^4==1
def pw(X,n):
    R=ID
    for _ in range(n): R=mul(R,X)
    return R
Q8=frozenset(i for i,g in enumerate(G) if pw(g,4)==ID)
print("|Q8|:",len(Q8),"is subgroup:",Q8 in set(subs))
# normality: conjugate-closed?
def conj(A,X): return mul(mul(A,X),mat_inv(A))
for A in G:
    assert frozenset(idx[conj(A,G[i])] for i in Q8)==Q8
print("Q8 normal: True")
# quotient G/Q8 order 3 -> cyclic -> linears
# cosets
cosets=[]
used=set()
for i in range(24):
    if i in used: continue
    c=frozenset(idx[mul(G[i],G[j])] for j in Q8)
    cosets.append(c); used|=set(c)
print("ncosets:",len(cosets))
# action of G on cosets by left mult -> quotient map; pick generator image order
# find element t with t^3 in Q8 but t not in Q8
t=None
for g in G:
    if idx[g] not in Q8 and idx[pw(g,3)] in Q8:
        t=g; break
print("t=",t,"t^3 in Q8:",idx[pw(t,3)] in Q8)
# Sylow-3 subgroups (order 3): cyclic closures of order-3 elements
o3=[g for g in G if pw(g,3)==ID and g!=ID]
print("nelements order 3:",len(o3))
syl3=[]
for g in o3:
    H=close([g])
    if len(H)==3 and H not in syl3: syl3.append(H)
print("nSylow3:",len(syl3))
# action on Sylow-3 by conjugation -> permutation rep; character perm(g)=#fixed - 1 (minus trivial) -> candidate 3-dim
def perm_fix(g):
    return sum(1 for H in syl3 if frozenset(idx[conj(g,G[i])] for i in H)==H)
# class reps: reuse class computation
seen=[False]*24; classes=[]
for i,X in enumerate(G):
    if seen[i]: continue
    cl=set(idx[mul(mul(A,X),mat_inv(A))] for A in G)
    for j in cl: seen[j]=True
    classes.append(sorted(cl))
classes.sort(key=len)
chi3={}
for c in classes:
    chi3[c[0]]=perm_fix(G[c[0]])-1
print("chi3 on class reps:",{k:v for k,v in chi3.items()})
sizes=[len(c) for c in classes]
norm=sum(s*chi3[c[0]]**2 for c,s in zip(classes,sizes))//24
print("norm chi3:",sum(s*chi3[c[0]]**2 for c,s in zip(classes,sizes)),"/24 =",norm)
json.dump({"nsubgroups":len(subs),"orders":sorted(len(H) for H in subs),
           "Q8":sorted(Q8),"syl3":[sorted(H) for H in syl3],
           "classes":[sorted(c) for c in classes],
           "chi3":{str(k):v for k,v in chi3.items()},"norm3":norm},
          open(ART+"sl23_subgroups.json","w"))
print("saved sl23_subgroups.json")
