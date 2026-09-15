from itertools import product
# D8
def mul(a,b):
    i1,j1=a; i2,j2=b
    return ((i1+((-1)**j1)*i2)%4,(j1+j2)%2)
def inv(a):
    i,j=a
    return ((-i)%4,0) if j==0 else (i,1)
def conj(g,x): return mul(mul(g,x),inv(g))
elems=[(i,j) for i in range(4) for j in range(2)]
names={(0,0):'1',(1,0):'r',(2,0):'r2',(3,0):'r3',(0,1):'s',(1,1):'rs',(2,1):'r2s',(3,1):'r3s'}
S=elems
Z=[(0,0),(2,0)]
V=[(0,0),(2,0),(0,1),(2,1)]
Vp=[(0,0),(2,0),(1,1),(3,1)]
alpha_map={(0,0):(0,0),(0,1):(2,0),(2,0):(2,1),(2,1):(0,1)}
beta_map={(0,0):(0,0),(1,1):(2,0),(2,0):(3,1),(3,1):(1,1)}
# build iso set as before (reuse)
from collections import defaultdict
def key(dom,cod,mp):
    return (tuple(sorted(dom)),tuple(sorted(cod)),tuple(sorted([(a,mp[a]) for a in dom])))
def inv_map(mp,dom):
    return {v:k for k,v in mp.items()}
def all_subgroups():
    def gen(gens):
        H={(0,0)}
        ch=True
        while ch:
            ch=False
            for h in list(H):
                for g in gens:
                    for x in [mul(h,g),mul(g,h)]:
                        if x not in H: H.add(x);ch=True
        return H
    subs=set()
    for r in range(1<<8):
        gens=[elems[i] for i in range(8) if (r>>i)&1]
        subs.add(frozenset(gen(gens)))
    return sorted(subs,key=lambda h:(len(h),sorted(h)))
subs=all_subgroups()
conj_maps=[]
for P in subs:
    for g in S:
        Q=frozenset(mul(mul(g,x),inv(g)) for x in P)
        mp={x:mul(mul(g,x),inv(g)) for x in P}
        conj_maps.append((frozenset(P),frozenset(Q),mp))
gen=[(frozenset(V),frozenset(V),dict(alpha_map)),(frozenset(V),frozenset(V),inv_map(alpha_map,V)),
     (frozenset(Vp),frozenset(Vp),dict(beta_map)),(frozenset(Vp),frozenset(Vp),inv_map(beta_map,Vp))]
gen+=conj_maps
iso_set=set()
for d,c,m in gen:
    if len(d)==len(c): iso_set.add(key(d,c,m))
def decode(k):
    dt,ct,mt=k
    return (set(dt),set(ct),dict(mt))
changed=True
while changed:
    changed=False
    cur=list(iso_set)
    for k1 in cur:
        d1,c1,m1=decode(k1)
        for k2 in cur:
            d2,c2,m2=decode(k2)
            if c1==d2:
                try: m={x:m2[m1[x]] for x in d1}
                except KeyError: continue
                k=key(d1,c2,m)
                if k not in iso_set: iso_set.add(k);changed=True
    for k1 in list(iso_set):
        d1,c1,m1=decode(k1)
        m={v:k for k,v in m1.items()}
        k=key(c1,d1,m)
        if k not in iso_set: iso_set.add(k);changed=True
    sublist=[set(s) for s in subs]
    for k1 in list(iso_set):
        d1,c1,m1=decode(k1)
        for A in sublist:
            if A<=d1:
                B=set(m1[x] for x in A)
                m={x:m1[x] for x in A}
                k=key(A,B,m)
                if k not in iso_set: iso_set.add(k);changed=True
print("num isos",len(iso_set))
# morphisms Hom_F(P,Q): isos + inclusions? For our checks we need iso list only.
# Define Lambda_F orbits as (Q, psi) with Q subgroup, psi: Q->S injective hom in F.
# Orbit list from paper:
# o1: (D8, id)
# o2: (V, alpha)
# o3: (Vp, beta)
# o4: (Q1, phi14) where phi14: <s> -> <rs>, s->rs
# o5: (Q2, phi41): <rs> -> <s>, rs->s
Q1=frozenset([(0,0),(0,1)])
Q2=frozenset([(0,0),(1,1)])
phi14={(0,0):(0,0),(0,1):(1,1)}
phi41={(0,0):(0,0),(1,1):(0,1)}
D8=frozenset(S)
idD8={x:x for x in S}
orbits=[(D8,idD8),(frozenset(V),dict(alpha_map)),(frozenset(Vp),dict(beta_map)),(Q1,dict(phi14)),(Q2,dict(phi41))]
# verify each psi in F
for (Q,psi) in orbits:
    k=key(set(Q),set(psi.values()),dict(psi))
    print(sorted([names[x] for x in Q]), "->", sorted([names[x] for x in psi.values()]), "inF:", k in iso_set)

# Build explicit biset points: cosets of graph G=(Q,psi) in S x S.
# Points of [Q,psi] = (S x S)/G, left action of S x S. Represent coset reps.
def graph(Q,psi):
    return set((psi[x],x) for x in Q)

def cosets(Q,psi):
    G=graph(Q,psi)
    SxS=[(a,b) for a in S for b in S]
    seen=set(); reps=[]
    for (a,b) in SxS:
        if (a,b) in seen: continue
        # coset (a,b)G = {(a*g1, b*g2)? careful: S x S acts on left? Our biset [Q,psi]= (S x S)/(Q,psi) where (Q,psi)={(psi(q),q)}.
        # Cosets: left cosets? Action is left multiplication by S x S. Points = right cosets? Let's use left cosets (a,b)G.
        cos=set((mul(a,g1),mul(b,g2)) for (g1,g2) in G)
        # wait G elements are (psi(q),q): first coord in left S, second in right S? Our (S,S)-biset has left action by first S and right by second? Represent as left S x S set via (h,g).w = h w g^{-1}. Stabilizer convention: Stab((h,g))... For coset enumeration, left S x S-set (S x S)/G with left mult is fine; (N,N)-orbits correspond.
        for c in cos: seen.add(c)
        reps.append((a,b))
    return reps

def stabilizer_of_coset(rep,Q,psi):
    # stabilizer in S x S of coset rep*G = rep G rep^{-1} intersect? Actually Stab((a,b)G) = (a,b) G (a,b)^{-1}
    (a,b)=rep
    ai=inv(a); bi=inv(b)
    stab=set()
    for (g1,g2) in graph(Q,psi):
        stab.add((mul(mul(a,g1),ai),mul(mul(b,g2),bi)))
    return stab

def graph_to_pair(stab):
    # stab is subgroup of S x S of form (Q',psi'): find Q' = proj2, psi from mapping
    # proj2:
    Q2=set(y for (x,y) in stab)
    # check size equals sqrt? |stab|==|Q2|
    mp={}
    for (x,y) in stab:
        if y in mp: assert mp[y]==x
        mp[y]=x
    return (frozenset(Q2),mp)

P=frozenset(Z)
# K trivial (centralizer) and K=Aut (normalizer). Since Aut(Z)=1, same.
for idx,(Q,psi) in enumerate(orbits):
    reps=cosets(Q,psi)
    print(f"orbit {idx}: Q={[names[x] for x in Q]} size={len(reps)} (=64/{len(Q)})")
    # enumerate stabilizers
    from collections import Counter
    c=Counter()
    for r in reps:
        st=stabilizer_of_coset(r,Q,psi)
        (Qp,mp)=graph_to_pair(st)
        # check condition for centralizer: P<=Q', psi'(P)==P and psi'|_P == id
        cond = (set(P)<=set(Qp)) and all(mp[x] in P for x in P) and all(mp[x]==x for x in P)
        # for normalizer with K=Aut: need psi'(P)==P (any)
        condN = (set(P)<=set(Qp)) and all(mp[x] in P for x in P)
        c[(len(Qp),cond,condN)]+=1
    print("  stab distribution (lenQ, inC, inN):",dict(c))

# Now build C subbiset points and decompose as (N,N)-biset with N=D8 (=S here since N_S(Z)=S)
# Since N=S, (N,N)-orbits = ? The selected points form union of (S,S)-subsets? Actually N=S so (N,N)=(S,S), decomposition same as (S,S)-orbits but restricted to selected points: each original orbit contributes a subset (possibly empty/proper).
# For each orbit, selected points subset size:
for idx,(Q,psi) in enumerate(orbits):
    reps=cosets(Q,psi)
    sel=[]
    for r in reps:
        st=stabilizer_of_coset(r,Q,psi)
        (Qp,mp)=graph_to_pair(st)
        if set(P)<=set(Qp) and all(mp[x] in P for x in P) and all(mp[x]==x for x in P):
            sel.append(r)
    print(f"orbit {idx} selected {len(sel)}/{len(reps)}")
    # decompose sel under S x S action? Since sel is S x S stable? Is N_Omega(P) an (S,S)-subbiset? No! Only (N,N)-stable. With N=S it's (S,S)-stable? N=S so yes stable. Check: sel should be union of full orbits (since N=S). Indeed if N=S, condition is S x S invariant? Let's verify: conjugation by (a,b) sends stabilizer... condition P<=Q etc not invariant under arbitrary (a,b) unless... Actually with N=S, N_Omega(P) need not be (S,S)-stable per Remark 9.5. Hmm but N=S means (N,N)=(S,S) action is same, but subset need not be union of orbits. Let's check orbit structure: group acting is N x N = S x S on the subset - same group, but subset may not be union of S x S orbits of the big set? Wait the action of N x N on N_Omega(P) is restriction of action of S x S on Omega. Since N=S, actions coincide, so N_Omega(P) is an (S,S)-subset (closed under action? Lemma 9.6 says it is (N,N)-biset, i.e., closed under N x N action; with N=S, closed under S x S action, hence union of orbits). So sel per orbit is either all or empty? Let's see numbers.
