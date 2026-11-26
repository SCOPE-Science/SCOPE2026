# Two-pole higher-commutativity and ring-blindness of finite chain-ring Heisenberg groups

## Finding

Let \(R\) be a finite commutative chain ring of length \(m\ge2\), with residue field of order \(q\). Let \(G=\operatorname{UT}_3(R)\) be the group of upper-unitriangular \(3\)-by-\(3\) matrices. Write
\[
b_{m,q}=\frac{q^{m+1}-1}{q-1}=1+q+\cdots+q^m.
\]
For every integer \(r\ge1\), let \(T_r(G)\) be the number of ordered \(r\)-tuples of pairwise commuting elements and \(P_r(G)=T_r(G)/|G|^r\). Then
\[
\boxed{T_r(G)=b_{m,q}q^{2mr}-(b_{m,q}-1)q^{(2m-1)r},}\qquad
\boxed{P_r(G)=b_{m,q}q^{-mr}-(b_{m,q}-1)q^{-(m+1)r}.}
\]

Let \(\beta_s(G)\), for \(s\ge0\), count simultaneous-conjugacy orbits of ordered pairwise-commuting \(s\)-tuples, with \(\beta_0(G)=1\). The complete series is
\[
\boxed{\sum_{s\ge0}\beta_s(G)z^s=
\frac{b_{m,q}q^{-m}}{1-q^{2m}z}
-\frac{(b_{m,q}-1)q^{-m-1}}{1-q^{2m-1}z}.}
\]
Within the displayed family, equality of the full higher-commutativity series is equivalent to equality of \(q\) and \(m\). Nevertheless, for every prime \(p\) and \(m\ge2\),
\[
\operatorname{UT}_3(\mathbb Z/p^m\mathbb Z)
\quad\text{and}\quad
\operatorname{UT}_3(\mathbb F_p[t]/(t^m))
\]
have identical series and are not isoclinic. Thus even an entire exact commuting-tuple hierarchy is not an isoclinism classifier among these chain-ring groups.

## Assumptions and scope

The ring \(R\) is unital, commutative, finite, and has ideals linearly ordered by inclusion; its maximal ideal is \((\pi)\), with \(\pi^m=0\) and \(\pi^{m-1}\ne0\). Each quotient \(R/(\pi^h)\) has order \(q^h\), for integers \(1\le h\le m\). The formulas hold without restriction on the residue characteristic, including characteristic two and mixed-characteristic rings. The field case \(m=1\) also satisfies the counting identity, but is not part of the asserted new range; finite-field Heisenberg formulas were previously studied. All tuples are ordered, repetitions are allowed, and commuting means every pair commutes. The comparison across coefficient rings includes all integers \(r\ge1\), not merely an asymptotic limit.

## Proof

**Step 1 (commutators).** Parametrize an element of \(G\) by the three ring entries \((a,b,c)\), with multiplication
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
\]
Two elements commute precisely when \(ab'=a'b\). Also \(|G|=q^{3m}\), and its center and derived subgroup both consist of \((0,0,c)\) for \(c\in R\). For each tuple the \(r\) central coordinates are unrestricted, giving a factor \(q^{mr}\). Thus \(T_r(G)=q^{mr}F_{m,r}\), where \(F_{m,r}\) counts \(2\)-by-\(r\) matrices over \(R\) whose \(2\)-by-\(2\) minors all vanish.

**Step 2 (primitive rank-one count).** A matrix over \(R/(\pi^h)\) is *primitive* when at least one entry is a unit. If its minors all vanish, choose a unit entry and use the corresponding column and row to factor the matrix as \(uv^{\mathsf T}\), with both vectors primitive. Every other factorization arises from a unique common unit \(\lambda\), replacing the pair by \((\lambda u,\lambda^{-1}v)\). Since the length-\(h\) quotient has \(q^h\) elements and \((q-1)q^{h-1}\) units, the number of primitive zero-minor matrices is
\[
Q_{h,r}=
\frac{(q^{2h}-q^{2h-2})(q^{rh}-q^{r(h-1)})}{(q-1)q^{h-1}}
=(q+1)(q^r-1)q^{(r+1)(h-1)}.
\]
This uses actual invertible entries, not a field-rank argument for matrices over rings.

**Step 3 (valuation stratification).** Give each nonzero ring element its \(\pi\)-valuation in \(\{0,\ldots,m-1\}\); define the minimum entry valuation of a nonzero matrix likewise. A matrix with all entries in \(\pi^{\lceil m/2\rceil}R\) has automatically vanishing minors, accounting for \(q^{2r\lfloor m/2\rfloor}\) matrices, including zero. For each minimum valuation \(s\) satisfying \(0\le s<m/2\), write the matrix as \(\pi^sU\), where \(U\) is a primitive matrix modulo \(\pi^{m-s}\). Its minors vanish modulo \(\pi^m\) exactly when the reduction of \(U\) modulo \(\pi^{m-2s}\) has zero minors. Each such primitive reduction has exactly \(q^{2rs}\) lifts. Hence
\[
F_{m,r}=q^{2r\lfloor m/2\rfloor}+
\sum_{s=0}^{\lfloor(m-1)/2\rfloor}
q^{2rs}Q_{m-2s,r}.
\]
The summand simplifies to
\[
(q+1)q^{m-1-2s}\bigl(q^{mr}-q^{(m-1)r}\bigr).
\]
For odd \(m\), the coefficient \((q+1)\sum_s q^{m-1-2s}\) equals \(b_{m,q}\), while the initial term equals \(q^{(m-1)r}\). For even \(m\), the coefficient equals \(b_{m,q}-1\), and the initial term equals \(q^{mr}\). In both cases
\[
F_{m,r}=b_{m,q}q^{mr}-(b_{m,q}-1)q^{(m-1)r}.
\]
Multiplying by the free central-coordinate factor and dividing by \(|G|^r=q^{3mr}\) proves the two exact identities.

**Step 4 (orbit series and inverse statement).** Burnside's lemma gives \(\beta_s(G)=T_{s+1}(G)/|G|\) for all \(s\ge0\): a group element fixes precisely the commuting \(s\)-tuples in its centralizer. Substitution yields
\[
\beta_s(G)=b_{m,q}q^{-m}(q^{2m})^s
-(b_{m,q}-1)q^{-m-1}(q^{2m-1})^s.
\]
Summing geometric series establishes the stated rational function. Both residues are nonzero and its two simple poles are distinct; the quotient of their reciprocal locations is \(q\), and the larger reciprocal location is \(q^{2m}\). Thus the series determines \(q\) and then \(m\). Conversely the formula shows they determine the series.

For \(R=\mathbb Z/p^m\mathbb Z\) and \(S=\mathbb F_p[t]/(t^m)\), the residue orders and lengths both equal \((p,m)\), hence all commuting probabilities and orbit counts coincide. However the derived subgroup of \(\operatorname{UT}_3(R)\) is isomorphic to the additive group of \(R\), of exponent \(p^m\), whereas the corresponding group over \(S\) has derived subgroup exponent \(p\). Isoclinic groups must have isomorphic derived subgroups, so this pair is not isoclinic. This works for every prime and every \(m\ge2\).

## Verification

The standalone script `verify.py` checks the full group multiplication commuting criterion for every pair of noncentral coordinates in six independent small-ring configurations. It then enumerates ordered pairwise-commuting \(r\)-tuples for \(R=\mathbb F_p[t]/(t^m)\) with \((p,m,r)=(2,2,4),(2,3,3),(2,4,2),(3,2,3)\) and for \(R=\mathbb Z/p^m\mathbb Z\) with \((p,m,r)=(2,2,3),(3,2,3)\). Its count is of noncentral coordinates, compared to the derived formula for \(F_{m,r}\), so the free central factor does not need brute-force enumeration. The script returns `VERIFY_OK`. In particular, the noncentral triple counts are \(400\) for \((p,m)=(2,2)\) and \(9153\) for \((p,m)=(3,2)\) in both coefficient-ring families. The all-length, all-arity theorem relies on Steps 1–4, not on these finite tests.

## Relationship to prior work

Kaur, Prajapati and Prasad [1] establish general rationality and isoclinism invariance of simultaneous commuting-conjugacy series and document already-known examples of series-equivalent nonisoclinic finite groups; neither general phenomenon is claimed new here. Kaur, Sharma and Singh [2] calculate commuting probabilities for unitriangular groups over finite fields for low tuple arities, not arbitrary finite chain rings of length at least two. Levit and Shwartz [3] establish a general finite-pole theory and maximum-abelian-subgroup leading terms, but do not evaluate the chain-ring Heisenberg spectrum. Their separate finite-field Heisenberg theorem [4] covers the length-one boundary, not the general nilpotent coefficient rings. Previously studied maximum-size pairwise commuting configurations of rank-two prime-power modules explain the leading pole, but alone do not supply the complete two-pole formula and residue fields of nonisomorphic rings.

The present result is the evaluated two-pole series uniformly across all finite commutative chain rings, along with its parameter reconstruction and explicit infinite nonisoclinic equality family. It does not assert that higher commuting probabilities fail to classify isoclinism in general for the first time.

## Limitations

The classification is restricted to groups of \(3\)-by-\(3\) upper-unitriangular matrices over finite commutative chain rings and the **full** commuting hierarchy. It does not extend to arbitrary finite local rings, matrix size greater than three, or all class-two groups. The resulting equality of higher commuting series does not imply equality of other invariants or of group isomorphism type. Novelty assessment is relative to inspected primary sources and semantic database records; potential equivalently phrased results elsewhere remain a risk. Independent external validation has not been performed.

## References

1. D. Kaur, S. K. Prajapati, A. Prasad, *Simultaneous Conjugacy Classes as Combinatorial Invariants of Finite Groups*, arXiv:1905.07957v1 (first posted 2019-05-20), https://arxiv.org/abs/1905.07957.
2. D. Kaur, U. B. Sharma, A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1 (first posted 2020-06-02), https://arxiv.org/abs/2006.01493.
3. V. E. Levit, R. Shwartz, *Higher Commutativity in Finite Groups: Exact Asymptotics and Finite Spectrum*, arXiv:2605.02071 (2026), https://arxiv.org/abs/2605.02071.
4. V. E. Levit, R. Shwartz, *Higher Commutativity in Finite Groups, Rigidity, Extremal Bounds, and Heisenberg-Type Families*, arXiv:2605.17171 (2026), https://arxiv.org/abs/2605.17171.
