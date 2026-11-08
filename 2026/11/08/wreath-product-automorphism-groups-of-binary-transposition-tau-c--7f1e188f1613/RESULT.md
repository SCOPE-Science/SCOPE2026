# Wreath-product automorphism groups of binary transposition \(\tau\)-cycle sets

## Finding

Let \(r\geq2\), let \(V=\mathbb F_2^r\), and choose distinct nonzero vectors \(a,b\in V\). Let \(\tau=(a\ b)\) be their transposition, fixing every other vector. Define the pointed magma on \(V\) by
\[
x\circ y=\tau(y-x)-\tau(-x),\qquad 0\in V\text{ distinguished}.
\]
This magma is a quasi-linear cycle set. Put \(Q=2^{r-1}\), \(d=a+b\), and \(H=\langle d\rangle\). With \(C_2\wr S_k\) denoting the permutation wreath product and \(S_0\) the trivial group, its complete pointed and unpointed automorphism groups are
\[
\operatorname{Aut}_0(V,\circ)\cong
C_2^{Q-1}\rtimes(C_2\wr S_{Q/2-1}),
\qquad
\left|\operatorname{Aut}_0(V,\circ)\right|
=2^{3Q/2-2}(Q/2-1)!,
\]
\[
\operatorname{Aut}(V,\circ)\cong
C_2^Q\rtimes(C_2\wr S_{Q/2-1}),
\qquad
\left|\operatorname{Aut}(V,\circ)\right|
=2^{3Q/2-1}(Q/2-1)!.
\]
Here \(\operatorname{Aut}_0\) requires fixing the distinguished zero, whereas \(\operatorname{Aut}\) refers only to the cycle-set operation. The subgroup consisting of \(\mathbb F_2\)-linear pointed automorphisms has order
\[
2^{2r-3}\lvert\operatorname{GL}_{r-2}(\mathbb F_2)\rvert.
\]
For \(r\geq3\) the \(\tau\)-group socle is exactly \(H\), and the cycle set has multipermutation level two. For \(r=2\) its socle is all of \(V\) and its multipermutation level is one. In particular, when \(r=4\), the three automorphism-group orders (pointed, unpointed, linear pointed) are respectively \(6144,12288,192\).

## Assumptions and scope

All vector spaces are finite over \(\mathbb F_2\), and \(r\geq2\). The vectors \(a\) and \(b\) are distinct and nonzero, so \(d=a+b\ne0\) and \(a\notin H\). Choose a linear complement \(U\) of \(H\) that contains \(a\); this exists because \(a\) and \(d\) are independent. Identify \(V=U\oplus H=U\times\mathbb F_2\), with \(a=(c,0)\), \(b=(c,1)\) for \(c=a\in U\setminus\{0\}\). Write \(Q=\lvert U\rvert\). Denote by \(\operatorname{Aut}_{\mathrm{lin},0}\) the pointed automorphisms linear for the original vector-space addition. The socle is \(\operatorname{Soc}(V,\tau)=\{h:\tau(z+h)=\tau(z)+\tau(h)\text{ for every }z\in V\}\). The retraction relation identifies elements with identical left translations; its iteration defines multipermutation level.

## Proof

### The explicit operation and the cycle identity

Let \(\delta(P)\in\mathbb F_2\) be one if proposition \(P\) holds and zero otherwise. In the chosen coordinates,
\[
\tau(u,t)=(u,t+\delta(u=c)),\quad
(u,t)\circ(v,s)=(v,s+\epsilon(u,v)),\quad
\epsilon(u,v)=\delta(u+v=c)+\delta(u=c).
\tag{1}
\]
The formula follows by substituting into the definition of \(\circ\) and using characteristic two. Every left translation is bijective, being a bit flip on each \(U\)-fiber. For \(x=(u,t)\), \(y=(v,s)\), \(z=(w,h)\), the two sides of the cycle identity are both
\[
(x\circ y)\circ(x\circ z)=(w,h+\epsilon(u,w)+\epsilon(v,w))
=(y\circ x)\circ(y\circ z).
\]
Thus the magma is a cycle set; the original construction makes it quasi-linear.

### Intrinsic fibers of the left-translation group

Let \(L_u\) denote left multiplication by either point \((u,t)\). Formula (1) shows that \(L_u\) is independent of \(t\). For \(u\ne c\), it flips the two points of the single fiber over \(v=c+u\), which is nonzero. For \(u=c\), it flips every nonzero fiber and fixes the two points above zero. Therefore the group
\[
P=\langle L_u:u\in U\rangle\cong C_2^{Q-1}
\]
contains all independently supported flips of the \(Q-1\) nonzero two-point fibers. Its orbits are exactly those fibers, along with the two singleton points \((0,0)\) and \((0,1)\). This proves that the partition, including its distinguished zero-fiber, can be recovered from the operation alone.

### Exhaustion of the automorphisms

Every operation automorphism \(\sigma\) conjugates \(L_x\) to \(L_{\sigma(x)}\), so it normalizes \(P\) and must permute its orbits. In particular the two singleton orbits form an invariant set. Consequently every automorphism has a unique expression
\[
\sigma_{\phi,\eta}(u,t)=(\phi(u),t+\eta(u))
\tag{2}
\]
where \(\phi\in\operatorname{Sym}(U)\) fixes \(0\), and \(\eta:U\to\mathbb F_2\) is an arbitrary function. The pointed condition is precisely \(\eta(0)=0\).

As \(L_0\) flips exactly the fiber above \(c\), and \(\sigma(0,t)\) is another point above zero with the same left translation, conjugating \(L_0\) forces \(\phi(c)=c\). For each \(u\ne c\), the single fiber flipped by \(L_u\) is at \(c+u\), so conjugation yields
\[
\phi(c+u)=c+\phi(u).
\tag{3}
\]
The same equation holds for \(u=c\) since \(\phi(0)=0\) and \(\phi(c)=c\). Conversely, if \(\phi\) fixes zero and satisfies (3), then \(\phi\) preserves the truth values of both \(u=c\) and \(u+v=c\), hence \(\epsilon(\phi(u),\phi(v))=\epsilon(u,v)\). Substitution of (2) into (1) now shows
\[
\sigma_{\phi,\eta}(x\circ y)=\sigma_{\phi,\eta}(x)\circ\sigma_{\phi,\eta}(y)
\]
for every \(\eta\), with no further restriction. Equations (2)--(3) are therefore necessary and sufficient for all automorphisms, not merely a constructed subgroup.

### Structure and cardinalities

Let \(T_c:U\to U\) be translation by \(c\). Equation (3) says \(\phi T_c=T_c\phi\). Translation \(T_c\) has \(Q/2\) two-cycles, one being \(\{0,c\}\). A permutation commuting with \(T_c\) and fixing zero also fixes \(c\), and may permute the other \(Q/2-1\) pairs and flip each pair independently. Hence
\[
C_{\operatorname{Sym}(U)}(T_c)_0\cong C_2\wr S_{Q/2-1},
\quad\left|C_{\operatorname{Sym}(U)}(T_c)_0\right|
=2^{Q/2-1}(Q/2-1)!.
\]
The functions \(\eta\) form a normal elementary abelian group under pointwise addition; conjugation by \(\phi\) permutes their arguments. Requiring \(\eta(0)=0\) gives \(2^{Q-1}\) functions; dropping it gives \(2^Q\). The two semidirect products and their orders follow.

A map (2) is \(\mathbb F_2\)-linear if and only if both \(\phi\) and \(\eta\) are linear, because \(\sigma(0,1)=(0,1)\) for pointed automorphisms and the projections respect the decomposition. Linear \(\phi\) are exactly the stabilizer of \(c\) in \(\operatorname{GL}(U)\), with order \(2^{r-2}\lvert\operatorname{GL}_{r-2}(\mathbb F_2)\rvert\); there are \(2^{r-1}\) linear functionals \(\eta\). Multiplying proves the linear-subgroup formula.

### Socle and retraction

By definition of the socle, \((h,t)\) lies in it precisely when
\[
\delta(v+h=c)+\delta(h=c)=\delta(v=c)
\quad\text{for every }v\in U.
\tag{4}
\]
All \(h=0\) satisfy (4). If \(Q>2\), choosing \(v=c\) rules out any \(h\notin\{0,c\}\), while choosing \(v\notin\{0,c\}\) rules out \(h=c\). Thus only \(h=0\) remains, giving the two-element socle \(H\). If \(Q=2\), the indicator \(\delta(v=c)\) is linear and (4) holds for every \(h\), giving all of \(V\). For \(Q>2\), the maps \(L_u\) are distinct for different \(u\in U\), and the retraction identifies precisely the pairs \((u,0)\sim(u,1)\). Formula (1) shows that its quotient operation on \(U\) is \(u\circ v=v\), a trivial cycle set, so one more retraction gives a point. For \(Q=2\), every left translation is identical, so the first retraction already gives a point.

## Verification

The accompanying standalone Python program `tau_magma_verify.py` constructs the exact operation table from the transposition, checks the cycle identity in ranks two through four, and computes the socle directly in ranks two through five. It exhaustively tests all permutations in ranks two and three, both with and without the distinguished-point restriction, and confirms that the resulting sets equal the parameterized families (2)--(3). In rank four it constructs and checks all \(6144\) predicted pointed maps and all \(12288\) predicted unpointed maps and counts \(192\) linear pointed maps. It checks closed-order formulas in ranks two through five. The recorded output ends with `VERIFY_OK`. The rank-four construction is *not* claimed to enumerate all permutations of the sixteen-element set; the general proof provides exhaustion. Run `python3 tau_magma_verify.py` with Python 3 and no dependencies.

## Relationship to prior work

Byott and Jasko, *Magma Automorphisms and Quasi-Linear Cycle Sets*, arXiv:2609.20028, introduce the pointed-magma automorphism viewpoint and prove a cyclic transposition result (Theorem 3.2) under a generator condition. Their computations concern the general conjecture and do not classify the full automorphism group of this elementary abelian transposition family. The present theorem addresses precisely this noncyclic family, including non-additive automorphisms and exact wreath-product structure. Rump introduced the quasi-linear framework, and Dietzel proved general finite retractibility; the current socle and retraction conclusions are concrete calculations, not claims to solve the general retraction problem.

## Limitations

The classification is specific to the transposition of two distinct nonzero points of an elementary abelian two-group, not all permutations, other prime characteristics, or all finite abelian groups. The exact automorphism theorem is proved here but has not been independently audited for publication priority. Earlier general results about cycle-set automorphisms could conceivably subsume portions of it; the full text of the 2016 foundational Rump paper was not accessible during the literature comparison. Finite tests are supporting evidence, not an infinite proof.

## References

1. N. P. Byott and E. Jasko, *Magma Automorphisms and Quasi-Linear Cycle Sets*, arXiv:2609.20028v2 (2026), first publicly submitted September 17, 2026, https://arxiv.org/abs/2609.20028.
2. W. Rump, *Quasi-linear Cycle Sets and the Retraction Problem for Set-theoretic Solutions of the Quantum Yang-Baxter Equation*, Algebra Colloquium **23** (2016), 149--166, DOI:10.1142/S1005386716000183.
3. C. Dietzel, *Proof of Rump's Retraction Conjecture for Quasilinear Cycle Sets*, arXiv:2607.08609 (2026), https://arxiv.org/abs/2607.08609.
