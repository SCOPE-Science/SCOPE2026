# Vary representative: condition uses specific representative stabilizer of coset rep, but membership
# N_Omega(P) depends on SOME representative? Definition: w in Omega with Stab_{S x S}(w) = (Q,psi), P<=Q, psi(P)=P, psi|_P in K.
# Stabilizer is defined up to conjugacy? No: stabilizer of a point is a specific subgroup (depends on point, not rep). Our computation above used coset rep r: Stab(rG) = r G r^{-1}. That's correct and rep-independent (different rep of same coset gives same subgroup). So above says only orbit 0 contributes.
# But wait: our coset reps give stabilizers rGr^{-1}; for orbit 1, Q-conjugates never contain Z? V-conjugates: V is normal in D8? V={1,r2,s,r2s} is normal (index 2). So Q'=V always. Z<=V yes. But psi' = c_a alpha c_b^{-1} restricted... condition psi'(Z)=Z and psi'|_Z=id?
# alpha|_Z: alpha maps r2->r2s?? alpha_map: (2,0)->(2,1), but (2,1)=r2s not in Z! So alpha does NOT preserve Z. Indeed V-conjugates: psi'(Z) may not equal Z. Our check correctly found 0.
# But hold on: psi'(Z)=Z required as sets in S. Since alpha(Z) not subset of Z, fails. Similarly beta.
# For orbits 3,4: Q' are conjugates of Q1=<s>. Some conjugates contain Z? No: |Q'|=2, Z has order 2; P<=Q' with |P|=|Q'|=2 forces Q'=Z. But Q1-conjugates: <s> conjugates in D8 are <s>,<r2s>; never Z. So 0. Good.
# So C_{Lambda}(Z) = orbit0 = [S,id] as (S,S)-biset. Size 8.
# Now compute Lambda_N for N = N_F(Z)? N=D8, N-fusion system: N_F(Z) on N_S(Z)=D8. What is N_F(Z)? Morphisms phi: A->B with extension psi~: ZA->ZB with psi~|_Z in K=Aut(Z)=1 (trivial). Since Aut(Z)=1, condition psi~|_Z=id.
# Which morphisms of F satisfy this? In particular alpha: V->V does NOT extend... alpha itself has domain V containing Z; alpha|_Z != id (alpha(r2)=r2s not even in Z). So alpha not in N. Similarly beta not in N. phi14: Q1->Q2: does it extend to ZQ1= ? Z*Q1 = {1,r2,s,r2s}=V. Extension would need psi:V->? with psi|_Z=id and psi|_Q1=phi14. But alpha|_Q1: s->r2, not rs. Is there any? Let's brute force: list all F-isos psi: ZA->ZB extending phi with psi|_Z=id.
# Then compute minimal N-characteristic biset Lambda_N via Theorem 5.3 algorithm? Or at least count orbits: Lambda_N should contain [N,id] plus possibly more. If N-fusion is trivial-ish (only inner?), Lambda_N = [S,id]? Then equality might HOLD here despite noncentricity!
# Let's compute N = N_F(Z) explicitly and its Lambda (orbit list via F-conjugacy stabilization algorithm).
from itertools import product
def mul(a,b):
    i1,j1=a; i2,j2=b
    return ((i1+((-1)**j1)*i2)%4,(j1+j2)%2)
def inv(a):
    i,j=a
    return ((-i)%4,0) if j==0 else (i,1)
elems=[(i,j) for i in range(4) for j in range(2)]
names={(0,0):'1',(1,0):'r',(2,0):'r2',(3,0):'r3',(0,1):'s',(1,1):'rs',(2,1):'r2s',(3,1):'r3s'}
def key(dom,cod,mp):
    return (tuple(sorted(dom)),tuple(sorted(cod)),tuple(sorted([(a,mp[a]) for a in dom])))
def decode(k):
    dt,ct,mt=k
    return (set(dt),set(ct),dict(mt))
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
V=frozenset([(0,0),(2,0),(0,1),(2,1)])
Vp=frozenset([(0,0),(2,0),(1,1),(3,1)])
Z=frozenset([(0,0),(2,0)])
alpha_map={(0,0):(0,0),(0,1):(2,0),(2,0):(2,1),(2,1):(0,1)}
beta_map={(0,0):(0,0),(1,1):(2,0),(2,0):(3,1),(3,1):(1,1)}
def inv_map(mp,dom): return {v:k for k,v in mp.items()}
conj_maps=[]
for P in subs:
    for g in elems:
        Q=frozenset(mul(mul(g,x),inv(g)) for x in P)
        mp={x:mul(mul(g,x),inv(g)) for x in P}
        conj_maps.append((frozenset(P),frozenset(Q),mp))
gen=[(V,V,dict(alpha_map)),(V,V,inv_map(alpha_map,V)),(Vp,Vp,dict(beta_map)),(Vp,Vp,inv_map(beta_map,Vp))]+conj_maps
isoF=set()
for d,c,m in gen:
    if len(d)==len(c): isoF.add(key(set(d),set(c),m))
changed=True
while changed:
    changed=False
    for k1 in list(isoF):
        d1,c1,m1=decode(k1)
        for k2 in list(isoF):
            d2,c2,m2=decode(k2)
            if c1==d2:
                try: m={x:m2[m1[x]] for x in d1}
                except KeyError: continue
                k=key(d1,c2,m)
                if k not in isoF: isoF.add(k);changed=True
    for k1 in list(isoF):
        d1,c1,m1=decode(k1)
        m={v:k for k,v in m1.items()}
        k=key(c1,d1,m)
        if k not in isoF: isoF.add(k);changed=True
    sublist=[set(s) for s in subs]
    for k1 in list(isoF):
        d1,c1,m1=decode(k1)
        for A in sublist:
            if A<=d1:
                B=set(m1[x] for x in A)
                m={x:m1[x] for x in A}
                k=key(A,B,m)
                if k not in isoF: isoF.add(k);changed=True
print("F isos:",len(isoF))
# Normalizer N_F(Z): underlying N_S(Z)=S (order 8). Morphisms: phi:A->B (A,B<=S) such that exists ext psi: ZA->ZB in F with psi|_A=phi, psi(Z)=Z, psi|_Z=id (K=Aut(Z) trivial... but K=Aut(Z)={id} anyway; for K=Aut also same since Aut(Z)=1).
# Since Z<=? ZA: if A contains... ZA = subgroup generated by Z and A.
def closure(A,B):
    # subgroup generated
    H=set(A)|set(B)
    # close
    H=set(H)
    ch=True
    while ch:
        ch=False
        for h in list(H):
            for g in list(H):
                x=mul(h,g)
                if x not in H: H.add(x);ch=True
        # inverses
        for h in list(H):
            if inv(h) not in H: H.add(inv(h));ch=True
    return frozenset(H)
# enumerate N-isos
nisos=set()
for k in isoF:
    d,c,m=decode(k)
    # k is candidate extension psi with domain D=ZA' ? We want all phi that HAVE such an extension. Instead: for each F-iso psi:D->E with Z<=D,E and psi|_Z=id, add all restrictions phi=psi|_A for A<=D with... also need psi(ZA)=? Actually definition: Hom_N(A,B)={phi in F(A,B) | exists ext psi~ in F(ZA,ZB) with psi~|_A=phi, psi~|_Z in K}.
    pass
# collect
Next=set()
for k in isoF:
    D,E,psi=decode(k)
    if set(Z)<=D and set(Z)<=E and all(psi[x] in Z for x in Z) and all(psi[x]==x for x in Z):
        # for each A<=D, phi=psi|_A, target B=psi(A)<=E<=S, add phi
        for A in subs:
            if set(A)<=D:
                B=frozenset(psi[x] for x in A)
                m={x:psi[x] for x in A}
                Next.add(key(set(A),set(B),m))
print("N isos count:",len(Next))
# Compare with F isos restricted to... and with S-conjugation isos (inner fusion FS(S))
inner=set()
for P in subs:
    for g in elems:
        Q=frozenset(mul(mul(g,x),inv(g)) for x in P)
        mp={x:mul(mul(g,x),inv(g)) for x in P}
        if len(P)==len(Q): inner.add(key(set(P),set(Q),mp))
print("inner count:",len(inner))
print("N == inner?", Next==inner)
print("N strictly bigger than inner?", inner<Next)
# list N-isos not inner
extra=[k for k in Next if k not in inner]
print("extra count:",len(extra))
for k in sorted(extra)[:20]:
    d,c,m=decode(k)
    print(" extra:",sorted([names[x] for x in d]),"->",sorted([names[x] for x in c]), {names(a):names(b) for a,b in m.items()})
# F-conjugacy vs N-conjugacy on subgroups
def classes(isos):
    used=set(); cls=[]
    for P in subs:
        t=tuple(sorted(P))
        if t in used: continue
        cl=[P]; used.add(t)
        for Q in subs:
            if tuple(sorted(Q)) in used: continue
            if any((tuple(sorted(d))==tuple(sorted(P)) and tuple(sorted(c))==tuple(sorted(Q))) for (d,c,m) in [decode(k) for k in isos]):
                # need iso P->Q
                found=any(set(d)==set(P) and set(c)==set(Q) for (d,c,m) in [decode(k) for k in isos])
                if found: cl.append(Q); used.add(tuple(sorted(Q)))
        cls.append(cl)
    return cls
print("N-classes:")
for cl in classes(Next):
    print("  ",[[names[x] for x in sorted(c)] for c in cl])
