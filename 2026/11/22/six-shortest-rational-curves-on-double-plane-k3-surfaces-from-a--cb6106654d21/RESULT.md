# Six shortest rational curves on double-plane K3 surfaces from a rank-four Sierpiński lattice

## Finding

Let \(t\geq3\) be an integer satisfying \(t\equiv3\pmod{12}\), and let \(L_t\) be the rank-four even lattice with ordered basis \(h,e_1,e_2,e_3\) and Gram matrix
\[
G_t=\begin{pmatrix}2&t&t&t\\t&-2&4&4\\t&4&-2&4\\t&4&4&-2\end{pmatrix}.
\]
There is a complex projective K3 surface \(X_t\) with \(\operatorname{NS}(X_t)\cong L_t\), polarized by an ample class \(H_t\) corresponding to \(h\). The complete linear system \(|H_t|\) defines a finite double cover \(\pi_t:X_t\to\mathbb P^2\) branched over a **smooth plane sextic**.

Among all smooth rational curves \(C\subset X_t\), the least \(H_t\)-degree is exactly \(t\). **Exactly six** smooth rational curves attain this degree. Under the displayed marking, their classes are
\[
[e_1],\ [e_2],\ [e_3],\ [t h-e_1],\ [t h-e_2],\ [t h-e_3].
\]
The double-plane involution exchanges \(e_i\) and \(t h-e_i\). Consequently the six curves map in pairs to exactly three distinct integral rational plane curves of degree \(t\); the double cover splits over the normalization of each plane curve, and its intersection divisor with the sextic has even multiplicity on every normalization branch.

For \(i\ne j\), the intersections of these six curves satisfy
\[
e_i\cdot e_j=(t h-e_i)\cdot(t h-e_j)=4,\qquad
 e_i\cdot(t h-e_j)=t^2-4,
\]
and \(e_i\cdot(t h-e_i)=t^2+2\). Their classes span a rank-four sublattice of index precisely \(t\) in \(\operatorname{NS}(X_t)\). This is a uniform minimal-degree rational-curve classification in genus-two polarization; it does **not** classify singular rational curves or all splitting plane curves.

## Assumptions and scope

The ground field is \(\mathbb C\); \(t\) ranges over *all* positive integers congruent to \(3\) modulo \(12\). The lattice \(L_t\) and its occurrence as a K3 Néron–Severi lattice are taken from Kikuta's construction (arXiv:2611.17113v1, §4.2, especially (4.2) and Lemma 4.13). We independently verify the requisite quadratic-form identities and anisotropy. An ample chamber may be selected by reflections in \((-2)\)-classes; throughout, \(h\) denotes the corresponding ample marking. A *smooth rational curve* means an irreducible nonsingular \(\mathbb P^1\) on the surface. Its degree is its intersection with \(H_t\). Plane images are understood scheme-theoretically as reduced integral curves; no equation for the branch sextic is asserted.

## Proof

**1. Existence and double-plane model.** The lattice \(L_t\) is even and hyperbolic of signature \((1,3)\), as the lower-right block of \(G_t\) has eigenvalues \(6,-6,-6\) and its Schur complement is \(2-t^2/2<0\). Such a rank-four lattice embeds primitively in the K3 lattice and occurs as the exact Néron–Severi lattice of a complex K3 surface (as stated and used in Kikuta, Example 3.7 and §4.2). The vector \(h\) is primitive with \(h^2=2\).

Write any \(v=xh+y_1e_1+y_2e_2+y_3e_3\), let \(S=y_1+y_2+y_3\), \(T=y_1^2+y_2^2+y_3^2\), and \(q(v)=v^2/2\). Then
\[
q(v)=x^2+t x S+2S^2-3T.
\]
If \(q(v)=0\), reduction modulo \(2\) (using odd \(t\)) forces both \(x\) and \(S\) even. If exactly two \(y_i\) are odd, then \(T\equiv2\pmod4\), yielding \(q(v)\equiv2\pmod4\), a contradiction. Hence all coordinates are even; infinite descent gives \(v=0\). In particular \(L_t\) has no nonzero isotropic vectors. Also \(h^\perp\) is negative definite, so no root can be perpendicular to \(h\). Choose the sign and a Weyl-chamber translate of \(h\) to obtain an ample class \(H_t\); the marking and pairings are transported along the isometry. By the standard projective-model theorem for a primitive nef K3 class of square two (Saint-Donat), the basepoint-free \(|H_t|\) gives a degree-two map to \(\mathbb P^2\). Since no \((-2)\)-curve is perpendicular to \(H_t\), no curve is contracted, so the map is finite. A finite flat double cover of the smooth plane with smooth total surface in characteristic zero has smooth branch divisor, necessarily of degree six by the canonical-bundle formula.

**2. Exact short-root calculation.** Put \(d=(v,h)=2x+tS\). Completing the square in the displayed formula gives the identity
\[
d^2=4q(v)+(t^2-8)S^2+12T.
\]
For any root \(v^2=-2\), this becomes
\[
(*)\qquad d^2=(t^2-8)S^2+12T-4.
\]
If \(S=0\), the right side is \(8\pmod{12}\), which no integer square can be. Thus \(S\ne0\). Using \(T\ge S^2/3\), for \(|S|\ge2\) one gets
\[
d^2\ge (t^2-4)S^2-4\ge4t^2-20>t^2\quad(t\ge3).
\]
For \(|S|=1\), integrality implies \(T\ge1\), and (*) gives \(d^2\ge t^2\), with equality if and only if \(T=1\). Consequently every root has \(|(v,h)|\ge t\), and equality occurs precisely when \((y_1,y_2,y_3)=\pm\mathbf e_i\) and \(x=0\) or \(x=\mp t\) (with the sign matched to \(d\)). There are exactly twelve such signed roots, exactly six of positive degree \(t\), with the classes listed in the Finding.

**3. Effectivity and irreducibility.** Let \(r\) be any one of the six positive-degree roots. Riemann–Roch on a K3 surface gives \(\chi(\mathcal O(r))=1\); therefore either \(r\) or \(-r\) is effective, and ampleness rules out \(-r\). Choose an effective divisor \(D\in|r|\). If every irreducible component of \(D\) had nonnegative self-intersection, then \(D^2\ge0\), contradicting \(D^2=-2\). Thus some component is a smooth rational \((-2)\)-curve (by adjunction and the nonnegativity of arithmetic genus), whose \(H_t\)-degree is at least \(t\) by Step 2. As \(H_t\cdot D=t\), the component is all of \(D\). Hence each of the six roots is represented by one smooth rational curve. Every smooth rational curve has class of square \(-2\), so Step 2 excludes further curves of degree \(t\) or less.

**4. Deck involution and index.** For a smooth double cover \(\pi_t\) with deck involution \(\iota\), rational cohomology of the quotient satisfies \(H^2(X_t,\mathbb Q)^\iota\cong H^2(\mathbb P^2,\mathbb Q)\), the line spanned by \(h\). As \(\iota\) is an isometry fixing \(h\), it acts as the negative identity on \(h^\perp\), hence on the rational Néron–Severi space
\[
\iota^*v=(v,h)h-v.
\]
In particular \(\iota(e_i)=t h-e_i\). Distinct smooth rational curves have distinct negative-square classes, so their six images comprise three pairs, and the three images in \(\mathbb P^2\) are distinct integral rational curves \(B_i\). Because \(C_i\) and \(\iota C_i\) are distinct and each has \(H_t\)-degree \(t\), each maps birationally to a degree-\(t\) plane curve \(B_i\). Over the function field of \(B_i\), the degree-two extension splits, yielding even order of the branch equation at every place on the normalization of \(B_i\). The intersection formulas follow by bilinearity. Finally, the six classes generate precisely \(\langle e_1,e_2,e_3,t h\rangle\), whose index in \(L_t\) is \(t\).

## Verification

The independent symbolic identity in Step 2 and modular anisotropy argument establish the infinite quantifiers; no finite enumeration is invoked as an infinite proof. The included standalone `verify.py` recomputes Gram pairings and enumerates integral roots in a finite coordinate box for \(t=3,15,27,39\), checking the six predicted minimal classes; these finite checks are diagnostic only. The degree-two morphism and smoothness conclusion rely on standard K3 projective-model and double-cover theorems and the separately reconstructed hypotheses stated in Step 1.

## Relationship to prior work

Kikuta, arXiv:2611.17113v1, §4.2 introduces \(L_t\), proves anisotropy and minimum pairwise root intersection, and realizes it on K3 surfaces to distinguish quasi-isometry classes of automorphism groups. That work does not classify the \(h\)-short roots, provide the genus-two double-plane realization, give the six-curve degree spectrum or their index-\(t\) saturation profile. Galluzzi–Lombardo, arXiv:math/0512603v2, construct rank-two double-plane K3 lattices with a degree-\(d\) rational contact curve; their rank-two configuration does not imply the precise six-curve rank-four spectrum here. Rams–Schütt, arXiv:1907.04182, count low-degree smooth rational curves mainly for high-degree polarizations; their bounds do not determine these square-two polarizations. The double-plane projective-model theorem and the existence of rational curves of arbitrarily high degrees in other settings are established background, not part of the novelty claim.

## Limitations

This is an existence-and-classification statement for a lattice-polarized *complex* family, not an explicit sextic equation, and not a classification of singular rational curves. A plane curve whose pullback splits but has singular (rather than smooth rational) lifted components is not excluded below degree \(t\). Branch-contact divisors are even on normalizations; no assertion of ordinary tangencies, nodes, or a complete plane-curve incidence scheme is made. The exact Néron–Severi isometry is a specified hypothesis of the construction; on specializations with larger Picard rank extra low-degree curves may occur. Historical priority of very specialized sextic-contact arrangements requires further specialist comparison.

## References

1. K. Kikuta, *Quasi-isometry classes of automorphism groups of K3 surfaces via Sierpiński spaces*, arXiv:2611.17113v1 (first submitted 2026-11-12), §§3–4, in particular (4.2) and Lemma 4.13. https://arxiv.org/html/2611.17113v1
2. B. Saint-Donat, *Projective models of K3 surfaces*, American Journal of Mathematics 96 (1974), 602–639, standard genus-two K3 projective-model theorem.
3. F. Galluzzi and G. Lombardo, *On the automorphisms of some K3 surface double cover of the plane*, arXiv:math/0512603v2 (2006), especially §4. https://arxiv.org/abs/math/0512603
4. S. Rams and M. Schütt, *24 rational curves on K3 surfaces*, arXiv:1907.04182 (2019), §§1–3. https://arxiv.org/abs/1907.04182
