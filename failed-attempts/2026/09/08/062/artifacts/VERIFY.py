"""S8 VERIFY: single-command replay of the SL(2,3) non-monomial certificate."""
import json
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
ID=mat(1,0,0,1); MI=mat(2,0,0,2)
assert len(G)==24
def pw(X,m):
    R=ID
    for _ in range(m): R=mul(R,X)
    return R
def order_of(X):
    Y=X;k=1
    while Y!=ID: Y=mul(Y,X);k+=1
    return k
# closure+inverses
for X in G:
    for Y in G: assert mul(X,Y) in idx
    assert mul(X,inv(X))==ID
# classes
seen=[False]*24; classes=[]
for i,X in enumerate(G):
    if seen[i]: continue
    cl=set(idx[mul(mul(A,X),inv(A))] for A in G)
    for j in cl: seen[j]=True
    classes.append(sorted(cl))
classes.sort(key=len)
sizes=sorted(len(c) for c in classes)
assert sizes==[1,1,4,4,4,4,6] and sum(sizes)==24
# subgroups
def close(elts):
    S={idx[ID]}|{idx[g] for g in elts}; st=list(S)
    while st:
        x=st.pop()
        for y in list(S):
            z=idx[mul(G[x],G[y])]
            if z not in S: S.add(z); st.append(z)
    return frozenset(S)
subs={frozenset([idx[ID]])}
ch=True
while ch:
    ch=False
    for H in list(subs):
        for g in G:
            H2=close([G[i] for i in H]+[g])
            if H2 not in subs: subs.add(H2); ch=True
assert len(subs)==15 and 12 not in {len(H) for H in subs}
# commutator=Q8
Q8=frozenset(i for i,g in enumerate(G) if pw(g,4)==ID)
assert len(Q8)==8
C={idx[mul(mul(X,Y),mul(inv(X),inv(Y)))] for X in G for Y in G}
S=set(C); st=list(S)
while st:
    x=st.pop()
    for y in list(S):
        z=idx[mul(G[x],G[y])]
        if z not in S: S.add(z); st.append(z)
assert frozenset(S)==Q8  # commutator=Q8 -> |Gab|=3 -> 3 linears
# sylow3 action 3-dim norm 1
def conj(A,X): return mul(mul(A,X),inv(A))
o3=[g for g in G if pw(g,3)==ID and g!=ID]
syl3=[]
for g in o3:
    H=close([g])
    if len(H)==3 and H not in syl3: syl3.append(H)
assert len(syl3)==4
def nfix(g): return sum(1 for H in syl3 if frozenset(idx[conj(g,G[i])] for i in H)==H)
cls_of=[0]*24
for ci,c in enumerate(classes):
    for j in c: cls_of[j]=ci
chi={ci:nfix(G[c[0]])-1 for ci,c in enumerate(classes)}
assert sum(len(c)*chi[ci]**2 for ci,c in enumerate(classes))==24
# gens/rels
x=(0,1,2,0); y=(1,1,1,2); t=(0,1,2,2)
xy=mul(x,y)
assert pw(x,4)==ID and pw(x,2)==pw(y,2) and mul(mul(inv(y),x),y)==inv(x)
assert pw(t,3)==ID and conj(t,x)==y and conj(t,y)==xy and conj(t,xy)==x
gens=[x,y,t,inv(x),inv(y),inv(t)]
Sb={ID}; st=[ID]
while st:
    a=st.pop()
    for g in gens:
        b=mul(a,g)
        if b not in Sb: Sb.add(b); st.append(b)
assert len(Sb)==24
out={"order":24,"class_sizes":sizes,"nclasses":7,"nsubgroups":15,
 "subgroup_orders":sorted(len(H) for H in subs),"no_subgroup_order_12":True,
 "commutator_is_Q8":True,"abelianization_order":3,"n_linears":3,
 "chi3_values":[chi[ci] for ci in range(7)],
 "chi3_norm1":True,"degree_multiset":[1,1,1,2,2,2,3],
 "presentation_ok":True,"Q8_C3":True}
json.dump(out,open(ART+"VERIFY_result.json","w"),indent=1)
print("VERIFY PASS:",json.dumps(out))
