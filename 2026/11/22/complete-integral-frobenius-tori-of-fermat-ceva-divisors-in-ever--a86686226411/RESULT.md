# Complete integral Frobenius tori of Fermat–Ceva divisors in every residue class

## Finding
Let \(n\ge3\) and let \(k\) be any field with \(\operatorname{char}(k)\nmid n\). Define the reduced Fermat–Ceva divisor
\[
D_n:\quad (X^n-Y^n)(Y^n-Z^n)(Z^n-X^n)=0\subset\mathbb P^2_k.
\]
Let \(T_n\) be the maximal torus **quotient** of \(\operatorname{Pic}^0(D_n/k)\), and let
\[
S_n=(\mu_n\times_k\mu_n)\setminus\{(1,1)\}
\]
be the finite étale scheme of nonidentity pairs of \(n\)-th roots of unity. There is an integral isomorphism of \(k\)-tori
\[
\boxed{T_n\cong\bigl(\operatorname{Res}_{S_n/k}\mathbb G_m\bigr)^2.}
\]
In particular, the character lattice of \(T_n\) is the **permutation** Galois lattice \(\mathbb Z[S_n(\bar k)]^{\oplus2}\), not merely a lattice isogenous to this one. This holds with no congruence assumption on \(q\) when \(k=\mathbb F_q\), for odd and even \(n\), and also when \(\operatorname{char}(k)<n\) but does not divide \(n\).

For \(k=\mathbb F_q\), let \(h=\operatorname{ord}_n(q)\), define \(f_e=\gcd(n,q^e-1)^2\), and for each divisor \(d\mid h\) let
\[
c_d=\frac1d\sum_{e\mid d}\mu(d/e)f_e,
\qquad m_d=c_d-\mathbf{1}_{d=1},
\]
where \(\mu\) is the Möbius function. Then the complete integral arithmetic classification is
\[
\boxed{T_n\cong\prod_{d\mid h}
\left(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\right)^{2m_d},
\qquad T_n(\mathbb F_q)\cong\prod_{d\mid h}
(\mathbb Z/(q^d-1)\mathbb Z)^{2m_d}.}
\]
In particular, when \((n,q)=(7,2)\), there are sixteen nonidentity triple-point Frobenius orbits, all of length three, and
\[
T_7\cong\left(\operatorname{Res}_{\mathbb F_8/\mathbb F_2}\mathbb G_m\right)^{32},
\qquad T_7(\mathbb F_2)\cong(\mathbb Z/7\mathbb Z)^{32}.
\]
For \((n,q)=(8,3)\), the nonidentity orbit lengths are \(1^{[3]}2^{[30]}\), giving
\[
T_8\cong\mathbb G_m^6\times
\left(\operatorname{Res}_{\mathbb F_9/\mathbb F_3}\mathbb G_m\right)^{60}.
\]
The known normalization point-count formula for this arrangement, recovered here as a consistency check and **not** claimed as new, is
\[
\#D_n(\mathbb F_{q^r})=3+3q^r\gcd(n,q^r-1)-2\gcd(n,q^r-1)^2
\qquad(r\ge1).
\]

## Assumptions and scope
The integer \(n\) is at least three and is invertible in the base field; no condition that \(k\) contain the \(n\)-th roots of unity is imposed. The Picard group is the connected Picard scheme of the original singular reduced curve. The assertion concerns its torus quotient; it does **not** claim that the complete unipotent subgroup is a vector group in small characteristic. The normalized geometric components are all projective lines and the divisor is geometrically connected.

The singularities are precisely three ordinary \(n\)-fold points at the coordinate vertices and \(n^2\) ordinary triple points. Its connected Picard scheme has dimension \((3n-1)(3n-2)/2\), torus dimension \(2n^2-2\), and smooth connected unipotent radical of dimension \(n^2+3\binom{n-1}{2}\). These dimension statements are standard consequences of the ordinary-multiple-point normalization sequence, not independently claimed discoveries.

## Proof
**1. Exact geometric incidence.** Over a separable closure, write the three line families as
\[
A_u:X=uY,\qquad B_v:Y=vZ,\qquad C_w:Z=wX,
\qquad u,v,w\in\mu_n(\bar k).
\]
The lines of each family concur at one of the three distinct coordinate vertices. Every cross-family intersection of \(A_u\) and \(B_v\) has coordinates \((uv:v:1)\), and lies on precisely \(C_{(uv)^{-1}}\). This gives \(n^2\) distinct geometric triple points \(M_{u,v}\), parameterized by \(\mu_n^2\); no other intersections occur. Since \(n\) is invertible, all involved lines are distinct and the multiple points are ordinary. The point \(M_{1,1}=(1:1:1)\) is defined over \(k\).

**2. The local-to-global Picard torus.** For any reduced connected curve whose normalization is a disjoint union of genus-zero curves, the multiplicative gluing part of the normalization exact sequence has character lattice the first integral homology of the bipartite branch-incidence graph. Each singular support contributes a vertex, each geometric component another vertex, and each normalization branch an edge oriented from its component to the singular support. Ordinary multiple points can also contribute unipotent local factors, but these do not alter the character lattice of the torus quotient. Consequently
\[
X^*(T_n)\cong H_1(\Gamma_n,\mathbb Z)
\]
as a Galois lattice. For this divisor the graph has \(3n+n^2+3\) vertices and \(3n+3n^2\) edges; its connectedness and torus rank \(2n^2-2\) follow from the explicit incidence.

**3. A Galois-invariant spanning tree with a Galois-permuted chord basis.** Include in \(\Gamma_n\) all \(3n\) branches from component lines to the coordinate-vertex singularities, and all \(n^2\) branches connecting the \(A_u\) components to the triple points \(M_{u,v}\). These edges form an acyclic forest with exactly three connected components, one for each line family. Add the two branches connecting \(M_{1,1}\) to \(B_1\) and \(C_1\). The result is a spanning tree: its edge count is \(3n+n^2+2\), one less than the number of vertices, and its three former components are connected by those two new edges.

This spanning tree is **Galois invariant**. Indeed, the three families and the three coordinate points are individually defined over \(k\), all the branches of its first two types are included, and \(M_{1,1}\), \(B_1\), \(C_1\) are fixed. Its non-tree edges are exactly the other \(B\)-to-triple and \(C\)-to-triple branches. They form two copies of the Galois set
\[
S_n(\bar k)=\mu_n(\bar k)^2\setminus\{(1,1)\}.
\]
Every chord gives a fundamental integral cycle; the fundamental cycles form a \(\mathbb Z\)-basis of graph homology. Because the spanning tree and edge orientation are invariant, Galois permutes these cycles **without signs** exactly as it permutes the chords. Thus
\[
H_1(\Gamma_n,\mathbb Z)\cong
\mathbb Z[S_n(\bar k)]^{\oplus2}
\]
integrally. The character lattice of \(\operatorname{Res}_{S_n/k}\mathbb G_m\) is \(\mathbb Z[S_n(\bar k)]\); finite-étale torus descent proves the boxed group-scheme isomorphism. The construction uses no characteristic or congruence restriction beyond \(\operatorname{char}(k)\nmid n\).

**4. Every finite-field Frobenius class.** For \(k=\mathbb F_q\), Frobenius acts on a pair of roots by \((u,v)\mapsto(u^q,v^q)\). The number of pairs fixed by its \(e\)-th power is \(f_e=\gcd(n,q^e-1)^2\). Möbius inversion yields exactly \(c_d\) cycles of length \(d\), and deleting \((1,1)\) decreases only \(c_1\) by one. Each length-\(d\) orbit of the character basis corresponds to the Weil-restriction torus \(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\). The isomorphism and finite-point group formulas follow, using the cyclicity of \(\mathbb F_{q^d}^{\times}\). No rational-character calculation or point count is substituted for the integral basis proof.

**5. Point-count cross-check.** The normalization contains three copies of the finite-étale \(n\)-th-root scheme times \(\mathbb P^1\). Gluing its branches at the three rational coordinate points and the finite-étale scheme of \(n^2\) triple points gives \(3+3q^r s_r-2s_r^2\) points over \(\mathbb F_{q^r}\), where \(s_r=\gcd(n,q^r-1)\). This formula is already covered by the earlier all-twist arithmetic-normalization treatment and is included solely as an independent consistency test of the Frobenius orbit description.

## Verification
The attached standard-library script `verifier.py` reconstructs the full component/singularity incidence graph, checks the stated forest and Galois-invariant spanning tree, verifies that all \(2n^2-2\) fundamental-cycle chords are permuted under Frobenius, and compares Frobenius fixed-point counts to gcd formulas for 128 admissible \((n,q)\) pairs with \(3\le n\le15\). It also directly enumerates projective points in prime fields and in 24 extensions of degrees two or three, confirming the independently derived point-count formula. The observed final marker is `ALL_FERMAT_CEVA_TORUS_AND_ZETA_CHECKS_OK`. These are finite tests; the proof for all fields and all admissible \(n\) is the equivariant spanning-tree argument in Steps 1–4.

## Relationship to prior work
The Fermat/Ceva line arrangement, ordinary multiple-point configuration and dual Hesse member are classical; Artebani–Dolgachev describe the nine-line dual Hesse configuration. Nagel–Seceleanu study the associated Fermat point ideals and their Rees algebras, not arithmetic Picard-torus descent. A published treatment, *Integral Frobenius tori and zeta functions of odd-degree Ceva divisors*, already establishes the split and inversion Frobenius cases for odd \(n\ge5\) with \(p>n\), including the induced quadratic torus and both zeta functions. These special cases are **covered prior results**, not new parts of the present claim. Another published treatment, *Arithmetic wall crossing in twisted triangular Fermat line divisors*, already gives the all-twist point counts and zeta functions, including the untwisted formula reproduced in Step 5.

The claim here is solely the complete **integral torus isomorphism for every Frobenius residue class**, every \(n\ge3\), and all characteristics prime to \(n\). In particular, arbitrary higher-order Frobenius cycles are covered by a single invariant spanning tree, whereas the earlier odd-degree torus proof constructs a paired-chord basis only under inversion Frobenius; the all-twist zeta treatment supplies no integral torus character lattice. A priori identical rational zeta spectra do not determine a torus's integral character lattice. The higher-order and even-degree examples above make the extra scope concrete.

## Limitations
No assertion is made when the characteristic divides \(n\), where the displayed equation is nonreduced before taking its reduction. The classification is for the torus quotient of the connected Picard scheme, not the whole generalized Jacobian in all characteristics and not the Jacobian of a smooth normalization. The ordinary-multiple-point singularities, arithmetic genus, and point counts are classical or previously covered context, not novel stand-alone contributions. This is a same-model mathematical proof and verification package, without independent specialist validation. Although the relevant prior results and primary geometry sources have been compared, an unindexed older equivalent integral torus classification remains a historical-priority risk.

## References
1. Michela Artebani and Igor Dolgachev, *The Hesse pencil of plane cubic curves*, first public arXiv posting 2006-11-19, arXiv:math/0611590, especially Remark 3.1 on the dual nine-line arrangement. https://arxiv.org/abs/math/0611590
2. Brian Harbourne and Alexandra Seceleanu, *Containment Counterexamples for Ideals of Various Configurations of Points in Projective Space*, first public 2013-06-16, arXiv:1306.3668. https://arxiv.org/abs/1306.3668
3. Uwe Nagel and Alexandra Seceleanu, *Ordinary and symbolic Rees algebras for ideals of Fermat point configurations*, first public 2015-09-16, arXiv:1509.04977. https://arxiv.org/abs/1509.04977
4. *Integral Frobenius tori and zeta functions of odd-degree Ceva divisors*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-frobenius-tori-and-zeta-functions-of-odd-degree-ceva-di--daef787a6781 (full `RESULT.md` compared).
5. *Arithmetic wall crossing in twisted triangular Fermat line divisors*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-wall-crossing-in-twisted-triangular-fermat-line-divis--5105b8223fe7 (full `RESULT.md` compared).
