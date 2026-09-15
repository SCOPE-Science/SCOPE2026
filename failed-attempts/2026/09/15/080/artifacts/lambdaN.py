# Compute Lambda_N for N = N_F(Z) = FS(S) (inner fusion = fusion of D8 on itself).
# Lambda_{FS(S)} should be [S,id] only? Check via Theorem 5.3: basis element Omega_S.
# For F = FS(S) (trivial fusion, only conjugations), each F-conjugacy class = S-conjugacy class.
# P=S is fully normalized; XP construction: start with [S], F-stable already? For F=inner, [S] has fixed points |N_S(P)| stuff... Actually need to check whether Lambda contains more than [S,id].
# Direct: minimal characteristic biset for a p-group's inner fusion system.
# Known fact: Lambda_{F_S(S)} = [S,id]? Let's verify via fixed-point criterion.
# An F-char biset Omega = sum c_Q [Q,phi]. Minimal means Omega_S from Thm 5.3.
# For F=FS(S), morphisms are conjugations. Twisted diagonals (Q,psi) with psi=c_g.
# (Q,psi)~_{F x F} (Q',incl) iff ... Lemma 5.1: yes iff psi = eta2 eta1 with eta_i conjugations => always? For inner fusion, any (Q,c_g) is F x F-conjugate to (Q,incl)? Take eta1=id, eta2=c_g: yes. So all orbits with source Q lie in same F x F class as (Q,incl).
# Then Omega_S: start with [S,id]; add orbits for lower levels to achieve stability. But [S,id] fixed points: [S,id]_{(P,phi)} = |N_{id,phi}|/|S|... For F=inner, is [S,id] already F-stable? Fixed points of (P,phi): points (a,b) with... Let's compute directly.
from itertools import product
def mul(a,b):
    i1,j1=a; i2,j2=b
    return ((i1+((-1)**j1)*i2)%4,(j1+j2)%2)
def inv(a):
    i,j=a
    return ((-i)%4,0) if j==0 else (i,1)
elems=[(i,j) for i in range(4) for j in range(2)]
names={(0,0):'1',(1,0):'r',(2,0):'r2',(3,0):'r3',(0,1):'s',(1,1):'rs',(2,1):'r2s',(3,1):'r3s'}
S=elems
def key(dom,cod,mp):
    return (tuple(sorted(dom)),tuple(sorted(cod)),tuple(sorted([(a,mp[a]) for a in dom])))
def decode(k):
    dt,ct,mt=k
    return (set(dt),set(ct),dict(mt))
# inner fusion isos
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
inner=set()
for P in subs:
    for g in S:
        Q=frozenset(mul(mul(g,x),inv(g)) for x in P)
        mp={x:mul(mul(g,x),inv(g)) for x in P}
        if len(P)==len(Q): inner.add(key(set(P),set(Q),mp))
# fixed points of [S,id]: formula [S,id]_{(P,phi)} = |N_{phi,id}|/|S| * |C| ... use Prop 3.7: [Q,psi]_{(P,phi)} = |N_{phi,psi}|*|C_S(phi P)|/|Q|.
# For orbit [S,id_S]: Q=S, psi=id: = |N_{phi,id}| * |C_S(phi P)| / |S|.
# N_{phi,id} = {x in N_S(P,S?) : id o c_x o phi^{-1} in Hom_S} = {x in N_S(P)??...}. Let's brute force fixed points directly: points of [S,id] = S (8 pts) with (a,b).w = a w b^{-1}? Stabilizer of w is (S^w? ...). Fixed point (P,phi): w with phi(p) w = w p for all p in P, i.e., w p w^{-1} = phi(p).
# So count w in S satisfying w p w^{-1}=phi(p) forall p.
def fixed_Sid(P,phi):
    n=0
    for w in S:
        if all(mul(mul(w,p),inv(w))==phi[p] for p in P):
            n+=1
    return n
# Check stability: for each P and each phi,psi in N(P,S), fixed equal?
from collections import defaultdict
by_dom=defaultdict(list)
for k in inner:
    d,c,m=decode(k)
    # consider as phi: P->S with P=d
    by_dom[tuple(sorted(d))].append((c,m))
ok=True
for P, lst in by_dom.items():
    vals=set(fixed_Sid(set(P),m) for (c,m) in lst)
    # also inclusion
    inc={x:x for x in P}
    vals.add(fixed_Sid(set(P),inc))
    if len(vals)>1:
        ok=False
        print("unstable at P=",sorted([names[x] for x in P]),vals)
print("stable:",ok)
# Also need |Omega|/|S| prime to p: |S|/|S|=1 ok. So [S,id] is N-characteristic. Since any char biset contains [S,id]? Minimal => Lambda_N=[S,id]. Verify minimality: [S,id] contains [S,id] orbit; basis element Omega_S smallest containing it => Omega_S=[S,id] since [S,id] is already semicharacteristic (generated+stable). So Lambda_N=[S,id], size 8.
# Compare: C_{Lambda_F}(Z) computed = [S,id] (8 points) = Lambda_N. So equality HOLDS in this example despite Z noncentric!
# Centralizer fusion C_F(Z): underlying C_S(Z)=S (since Z central). Morphisms: phi with extension psi: ZA? For K=1: Hom_C(A,B)={phi: exists ext psi: ZA->ZB with psi|_Z=id}. Same as N here since Aut(Z)=1 and N_S=S. So C_F(Z)=N_F(Z)=inner. Lambda_C=[S,id] too. Holds.
# So D8/Z example does NOT refute. Need another example.
# Key: need N_F(P) strictly larger than inner but subbiset misses orbits.
# Think: need P noncentric with N_S(P) large and F has exotic morphisms normalizing P but not centralizing... but exotic morphisms must preserve P and act trivially on P to be in normalizer with K=Aut? For K=Aut(P), condition psi(P)=P only. Exotic alpha may normalize P.
# Let's search: other subgroups, e.g., P=Q1=<s> (order 2, noncentric since C_S(Q1)=V? C_D8(<s>) = {1,r2,s,r2s}=V, not <= Q1, so noncentric). N_S(Q1)=V (order 4). Fully normalized? F-conjugacy class of Q1 = all 5 subgroups order 2 (from earlier). N_S sizes: N_S(<s>)=V(4), N_S(<r2>)=S(8). So Q1 not fully normalized! Its fully normalized conjugate is <r2>=Z. So for TARGET we need fully normalized P. Take P=Z only fully-normalized noncentric? Order-2 class fully normalized rep is Z. Others not fully normalized, excluded.
# What about P=1? P=1 is noncentric? C_S(1)=S not <= 1, so noncentric. Fully normalized (only one). N_F(1)=F itself? N_S(1)=S. Morphisms: phi:A->B extends to psi: A->B with trivial condition on P=1. So N=F. N_{Lambda}(1): points with Stab (Q,psi), 1<=Q (always), psi(1)=1 always, psi|_1=id in K (K<=Aut(1)=1). So N=whole Lambda_F! Lambda_N = Lambda_F. Holds trivially.
# So in F_D8(A6), all fully-normalized noncentric P give equality?! Interesting.
# Need a group where fully normalized noncentric P has N_F(P) with exotic morphisms, and Lambda_F's N-subbiset has extra/missing orbits.
# General theory: N_{Lambda_F}^K(P) always contains exactly one Lambda_N (Thm 9.15 first part, no centricity needed!). Question is whether it EQUALS Lambda_N (no extra orbits). Extra orbits in N-subbiset correspond to (N,N)-orbits [A,phi]_N with A<N? or [N,alpha] with alpha != id?
# Extra orbits arise from F-orbits [Q,psi]_S whose restriction to N gives such.
# Let's think structurally: (N,N)-orbit of w in N-subbiset has stabilizer (A, phi|_A?)... If A contains P? Prop 9.11: all stabilizers (Q,psi) of Lambda_F have O_p(F)<=Q. Hmm.
# For counterexample, want an F-orbit [Q,psi] with Q not centric, Q cap N = A large, psi|_A != id but still in N, giving extra [A,...] orbit in N-subbiset beyond Lambda_N's decomposition.
# Simplest: find F where Lambda_F has an orbit [Q,psi] with P < Q <= N but psi|_P in K, psi|_? ...
# Note: if Q<=N and psi(Q)<=N and psi|_P in K, then the whole (S,S)-orbit [Q,psi]_S intersect N-subbiset = ? Some subset forming one or more (N,N)-orbits, including [Q,psi|..]... These give "extra" orbits unless [Q,psi] already accounted in Lambda_N.
# But Lambda_N itself contains basis orbits for each N-class. So extra occurs iff the (N,N)-orbit type [A,theta] appears in N-subbiset with HIGHER multiplicity than in Lambda_N, or a type that shouldn't appear... Since both are N-semicharacteristic, write N-sub = Lambda_N + sum_{R<N} c_R Omega^N_R. Extra iff some c_R>0.
# When does that happen? Precisely when Lambda_F contains F-orbits that "fold down".
# Let's brute-force search small p-groups with computer: enumerate all saturated fusion systems? Hard. Alternative: take F = F_S(G) for G with S Sylow, compute Lambda_F? Lambda_F for group fusion can be computed via algorithm (Reeh). Then compute N-sub and Lambda_N and compare.
# Candidate: S = extra-special? Or S = D8 x C2? P = ... Let's instead try F = fusion of S3 x S3? Hmm.
# Maybe theorem is TRUE and we should prove it? Let's examine proof of Thm 9.15 centric case: uses Puig Prop 8.3 (unique extension for centric) + Thm 8.6 (only [S,id] among centric orbits) to show only stabilizer (A,incl) is (N,id). For noncentric P, Puig extension fails; extra orbits possible in principle. But maybe using Op(F)<=Q (Prop 9.11) + ... one can still prove equality when K<=Inn or >=Inn? Let's test: suppose w in N-sub with (N,N)-stab (A,incl). Then (S,S)-stab (Q,psi) with A=Q cap N, psi|_A=id. Want to show (Q,psi)=(S,id) (then A=N). In centric proof: P<=A<=N, all F-centric, psi=cz, Q=S. Without centricity, psi need not be cz; Q may be < S. So extra orbits correspond to (Q,psi) with psi|_{Q cap N}=id but (Q,psi)!=(S,id).
# Does such (Q,psi) occur in Lambda_F? Lambda_F orbits are [R,alpha] over representatives. Need (Q,psi) subconjugate... Possibly yes.
# So counterexample needs F with an orbit [Q,psi], psi != incl, but psi restricts to id on Q cap N.
# Example: Q cap N small, psi nontrivial outside. E.g., N=N_S(P) small; Q cap N = P or so; psi|_P in K trivial but psi nontrivial on Q\P.
# In D8 example with P=Z, N=S, Q cap N = Q, psi|_Q=id forces... orbits [V,alpha]: alpha|_V != id, so excluded. Good - no extras. To get extras need orbit where psi fixes Q cap N pointwise but moves rest of Q. That means psi has fixed subgroup >= Q cap N. E.g., Q large, N small.
# Let's search computationally: take S = group of order p^3 or p^4, F with automorphisms having large fixed subgroups.
