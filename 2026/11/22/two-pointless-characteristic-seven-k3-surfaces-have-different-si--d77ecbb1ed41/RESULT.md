# Two pointless characteristic-seven K3 surfaces have different singular-fiber spectra and quadratic point counts

## Finding
Work over \(k=\mathbb F_7\). Two independently published smooth and pointless K3 surfaces are double covers of \(\mathbb P^1\times\mathbb P^1\). They have distinct complete geometric singular-fiber configurations in their displayed genus-one projections, and distinguishable point counts already over \(\mathbb F_{49}\).

For the Brandhorst--Takada surface \(X_{\mathrm{BT}}\), use base coordinates \([u:v]\), fiber coordinates \([r:s]\), and equation \(w^2=G_{\mathrm{BT}}\), where
\[
G_{\mathrm{BT}}=\sum_{i,j=0}^4 c_{ij}u^{4-i}v^i r^{4-j}s^j,\qquad
(c_{ij})=\begin{pmatrix}
6&0&3&0&3\\2&6&6&4&0\\1&2&1&6&6\\5&1&1&3&0\\6&0&3&0&3
\end{pmatrix}.
\]
For the Auel--Engel--Kedlaya--Shaikh surface \(X_{\mathrm{AEKS}}\), use base \([z:w]\), fiber \([x:y]\), and a separate double-cover coordinate \(h\) with \(h^2=G_{\mathrm{AEKS}}\), where
\[
\begin{aligned}
Q_1&=x^2+y^2, &Q_2&=2x^2-xy-2y^2,\\
R_1&=3w(z-3w)(z-5w)(z-6w),&R_2&=6z(z-w)(z-2w)(z-4w),\\
G_{\mathrm{AEKS}}&=R_1Q_1^2+R_2Q_2^2.
\end{aligned}
\]
These are exactly the published models, not new constructions.

Put \(t=v/u\) for the first base and \(a=z/w\) for the second. The discriminants of the binary quartics in the respective fiber coordinates, computed in \(\mathbb F_7[t]\) and \(\mathbb F_7[a]\), are
\[
\begin{aligned}
\operatorname{Disc}_r G_{\mathrm{BT}}(1,t,1,r)
&=(t^7-t)^2 P(t)Q(t),\\
P(t)&=t^4+t^3+t^2-t+1,\\
Q(t)&=t^4+2t^3+t^2-2t+1;\\
\operatorname{Disc}_x G_{\mathrm{AEKS}}(a,1,x,1)
&=2(a^7-a)^2 U(a)^2V(a)^2,\\
U(a)&=a^2+2,\qquad V(a)=a^2+3a-2.
\end{aligned}
\]
The discriminants are homogeneous sections of degree \(24\); the fiber at the omitted infinity parameter has multiplicity \(2\) in each. Both quartics \(P,Q\) are irreducible over \(\mathbb F_7\), and both quadratics \(U,V\) are irreducible.

Hence the *entire* geometric singular-fiber data, including the arithmetic parameter orbits, is:

| Model | Over the eight rational base parameters | Additional singular parameters | Total singular fibers |
|---|---|---|---|
| \(X_{\mathrm{BT}}\) | eight nonsplit \(I_2\) | eight \(I_1\), in two degree-four Frobenius orbits | sixteen |
| \(X_{\mathrm{AEKS}}\) | eight nonsplit \(I_2\) | four \(I_2\), in two degree-two Frobenius orbits; split over \(\mathbb F_{49}\) | twelve |

Finally, finite-field character sums give
\[
\boxed{\#X_{\mathrm{BT}}(\mathbb F_{49})=3040,\qquad
\#X_{\mathrm{AEKS}}(\mathbb F_{49})=3320.}
\]
Thus the surfaces are **not isomorphic over \(\mathbb F_7\)**, not merely inequivalent as marked fibrations.

## Assumptions and scope
All equations and fiber classifications are over the prime field \(\mathbb F_7\); fiber types are geometric Kodaira types after base change to an algebraic closure, and the adjectives split/nonsplit refer to their residue fields of definition. The two double covers are smooth K3 surfaces by the cited primary constructions. We study the specified genus-one maps to their indicated base lines; no section is assumed. The base-coordinate symbols in the two equations are independent. The numerical point counts are exact counts of rational points, not extrapolations from a sample.

## Proof
**1. Complete discriminants.** Insert each displayed quartic into the universal binary-quartic discriminant, or take the Sylvester resultant of the quartic and its derivative and divide by its leading coefficient before polynomial specialization. Exact expansion modulo \(7\) gives the displayed identities. Homogenization shows that each discriminant has degree \(24\); as its affine expression has degree \(22\), its zero at infinity has order exactly \(2\). The factors \(P,Q\) have no factor of degree one or two: their gcd with each of \(t^7-t\) and \(t^{49}-t\) is \(1\). Since each has degree four, both are irreducible. The quadratics \(U,V\) have nonsquare discriminants \(6\) and \(3\), respectively. All listed polynomial factors are distinct.

**2. Fibers over rational parameters.** In either model, at each base point of \(\mathbb P^1(\mathbb F_7)\), the fiber quartic is \(c q^2\), where \(q\) is a separable irreducible binary quadratic over \(\mathbb F_7\) and \(c\) is a nonsquare. This follows by substituting all seven finite parameters and infinity; in the second model it also follows directly from the factorization of \(R_1R_2\). Geometrically the fiber equation factors as \((h-\sqrt c\,q)(h+\sqrt c\,q)=0\): two smooth rational components meet transversally at the two distinct zeros of \(q\), so the fiber is \(I_2\). Its components and crossing points have no \(\mathbb F_7\)-rational representatives; it is a nonsplit fiber with no rational point.

**3. Remaining fibers of \(X_{\mathrm{BT}}\).** Each root of \(P Q\) is a *simple* zero of the quartic discriminant. For a smooth total surface in odd characteristic, simple vanishing of the discriminant in a one-parameter family of genus-one double covers means the branch quartic develops exactly one double root with ordinary smoothing; the resulting fiber is an irreducible nodal \(I_1\). The two irreducible degree-four factors give two Frobenius orbits of four nodal fibers. No others occur because the degree-\(24\) discriminant has been exhausted.

**4. Remaining fibers of \(X_{\mathrm{AEKS}}\).** Modulo \(U(a)\), exact polynomial arithmetic gives
\[
G_{\mathrm{AEKS}}=(1-2a)(x^2+xy-y^2)^2;
\]
modulo \(V(a)\) it gives
\[
G_{\mathrm{AEKS}}=(2-3a)(x^2+xy-y^2)^2.
\]
The quadratic \(x^2+xy-y^2\) has discriminant \(5\), hence distinct roots in \(\mathbb F_{49}\). At a root of \(U\), the norm of \(1-2a\) to \(\mathbb F_7\) is \(2\), and at a root of \(V\), the norm of \(2-3a\) is \(4\). Both are squares in \(\mathbb F_7\), so both coefficients are squares in \(\mathbb F_{49}\). Hence these four fibers are geometrically \(I_2\), and *both their components and crossing points are defined over their residue field* \(\mathbb F_{49}\). Again the complete degree-\(24\) discriminant leaves no further bad fibers. As a check, the sums of geometric fiber Euler numbers are \(8\cdot2+8\cdot1=24\) and \(12\cdot2=24\), respectively.

**5. Exact quadratic-extension counts.** For each of the \(50^2\) pairs \((b,c)\in\mathbb P^1(\mathbb F_{49})^2\), the double cover has exactly \(1+\chi(G(b,c))\) rational points above it, where the quadratic character is \(\chi(0)=0\) and \(\chi(\lambda)=\lambda^{24}\in\{\pm1\}\) for nonzero \(\lambda\). Summing over the entire finite base, with \(\mathbb F_{49}=\mathbb F_7[\alpha]/(\alpha^2-3)\), gives \(3040\) and \(3320\). The included executable checker repeats the count using the alternative field representation \(\alpha^2=5\). Because these numbers differ, no \(\mathbb F_7\)-isomorphism between the K3 surfaces exists.

## Verification
Run `python3 verify.py` with SymPy installed (see `requirements.txt`). The checker independently expands both discriminants modulo \(7\), tests their factor degrees and quartic-square fibers, verifies the two nonrational quadratic specializations and norm characters, and exhaustively enumerates the point counts over \(\mathbb F_7\) and two presentations of \(\mathbb F_{49}\). Its expected final output is `ALL CHECKS PASSED: BT=(0,3040), AEKS=(0,3320)`. Only integer and finite-field arithmetic are used. The finite point-count enumeration is exhaustive; the geometric identification of fiber types also uses the displayed discriminant and square-factor calculations, together with the cited smoothness of the total surfaces.

## Relationship to prior work
Brandhorst--Takada, arXiv:2611.06366v1, Section 9.2, publishes the first matrix and proves the first surface pointless and smooth. Auel--Engel--Kedlaya--Shaikh, arXiv:2611.08356v1, Proposition 8.1, Remark 8.2 and Table 6, publishes the second model, proves its pointlessness, and already specifies nonsplit \(I_2\) fibers above **rational** base parameters. Those are prior results, not discoveries here. Neither inspected primary text determines the complete additional singular-fiber orbit structures of both displayed models or compares their \(\mathbb F_{49}\)-point counts. Generic facts about Kodaira fibers and binary-quartic discriminants provide methods but not these explicit arithmetic comparisons. Targeted research-record and literature comparisons did not locate the exact pairwise theorem; older or unindexed calculations may exist.

## Limitations
The theorem distinguishes the two surfaces **over \(\mathbb F_7\)**. It does not exclude an isomorphism over \(\overline{\mathbb F}_7\), classify alternative fibrations or compute either full zeta function or geometric Picard lattice. The geometric smoothness of the two published models is taken from the primary references, rather than reproved here; the discriminant and point-count computations are rederived and checked exactly. Some unindexed or independently computed tables could affect historical priority. There has been no independent mathematical audit.

## References
1. A. Auel, P. Engel, K. S. Kedlaya, S. Shaikh, *Pointless K3 surfaces over finite fields*, arXiv:2611.08356v1, November 5, 2026, §8, Proposition 8.1, Remark 8.2 and Table 6, https://arxiv.org/html/2611.08356v1.
2. S. Brandhorst, Y. Takada, *Pointless K3 surfaces over finite fields*, arXiv:2611.06366v1, November 4, 2026, §9.2 and the \(q=7\) matrix, https://arxiv.org/html/2611.06366v1.
