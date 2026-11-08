# First integral top-class obstruction in the two-Chern filtration of three-plane Grassmannians

## Finding

For each integer \(1\leq\ell\leq16\), let \(G_\ell=\operatorname{Gr}(3,\mathbb C^{\ell+3})\). Let \(S\) be its tautological rank-three bundle, and write \(e_i=c_i(S^\vee)\in H^{2i}(G_\ell,\mathbb Z)\) for \(i=1,2\). Define the integral two-Chern subalgebra \(A_\ell=\mathbb Z[e_1,e_2]\subseteq H^{2*}(G_\ell,\mathbb Z)\), and let \(I_\ell\) be the index of its top-degree subgroup in \(H^{6\ell}(G_\ell,\mathbb Z)=\mathbb Z[\mathrm{pt}]\).

Then, *for every integer in the stated range*,
\[
I_\ell=\begin{cases}3,&\ell=13,14,15,\\1,&1\leq\ell\leq12\text{ or }\ell=16.\end{cases}
\]
Thus the first failure of integral top-class generation by the first two Chern classes occurs at \(\operatorname{Gr}(3,\mathbb C^{16})\). It persists through ambient dimensions \(17\) and \(18\), but integral top-class generation resumes for ambient dimension \(19\). Rational top-class generation holds for each of these spaces; the new distinction concerns the *integral lattice index*.

## Assumptions and scope

All Grassmannians are complex and carry their canonical orientation. We use integral singular cohomology and the Schubert normalization in which \(\sigma_{(\ell,\ell,\ell)}=[\mathrm{pt}]\) integrates to \(1\). The tautological dual Chern classes are the column Schubert classes \(e_1=\sigma_{(1)}\) and \(e_2=\sigma_{(1,1)}\). The theorem makes no assertion about widths \(\ell\geq17\), any lower cohomological degree, or integral generation of the *whole* ring.

The index has the concrete formula
\[
I_\ell=\gcd_{0\leq b\leq\lfloor3\ell/2\rfloor}\left\{\int_{G_\ell}e_1^{3\ell-2b}e_2^b\right\}.
\]
Indeed these finitely many monomials span the top homogeneous component of the *integral* polynomial subalgebra additively, and the target is free of rank one. The gcd is positive, since the displayed intersection coefficients are positive.

## Proof

For each width \(\ell\), represent Schubert classes by partitions \(\lambda=(\lambda_1,\lambda_2,\lambda_3)\) satisfying \(\ell\geq\lambda_1\geq\lambda_2\geq\lambda_3\geq0\). The integral Pieri rule says that multiplication by \(e_r\), for \(r\in\{1,2\}\), replaces \(\lambda\) with the sum of all partitions obtained by adding one box to each row in an \(r\)-element subset, retaining only partitions inside the rectangle; each admissible successor occurs with coefficient one. No rational operations enter the recursion.

For fixed \((\ell,b)\), initialize a function \(F(0,0,0)=1\), with every other coefficient zero. Apply the two-box vertical Pieri operator exactly \(b\) times, followed by the one-box operator exactly \(3\ell-2b\) times. The resulting coefficient \(F(\ell,\ell,\ell)\) is precisely
\[
M_{\ell,b}=\int_{G_\ell}e_1^{3\ell-2b}e_2^b.
\]
Every state of this recurrence is an integral triple within a rectangle with finite, explicitly bounded coordinates. Consequently the supplied exhaustive finite recurrence is a proof of each stated \(M_{\ell,b}\); taking the ordinary integer gcd gives the exact index, rather than an approximate or statistical estimate.

For an independently derived evaluation, let \(a=3\ell-2b\). Chern roots \(x,y,z\) and the Grassmannian alternant formula give
\[
M_{\ell,b}=[x^{\ell+2}y^{\ell+1}z^\ell]\,(x+y+z)^a(xy+xz+yz)^b(x-y)(x-z)(y-z).
\]
Expand the six monomials in the Vandermonde factor and use multinomial coefficients in the remaining two factors. `CHECK.py` implements this coefficient calculation without calling the Pieri state transition; it agrees exactly with the Pieri calculation for every one of the \(\sum_{\ell=1}^{16}(\lfloor3\ell/2\rfloor+1)=216\) tested monomials. (The exact number is also checked in the verification file.)

Finally, `CERTIFICATE.json` contains all resulting integer values for every width \(1\) through \(16\) and every permitted \(b\), rather than just a list of claimed gcds. Recomputing those numbers in either manner and performing the Euclidean algorithm establishes precisely \(I_{13}=I_{14}=I_{15}=3\), and \(I_\ell=1\) for the other thirteen widths. This is an exhaustive proof for the explicitly bounded range, not a claim of an unproved infinite pattern.

## Verification

The standard-library-only `CHECK.py` constructs all admissible vertical-strip transitions, evaluates all top coefficients, independently expands the Chern-root alternant, compares the two lists of integers, and checks the exact stored `CERTIFICATE.json`. From a directory containing both files run `python3 CHECK.py CERTIFICATE.json`. Successful execution ends with `PIERI_AND_ALTERNANT_CHECKS_OK` and `FIRST_NONPRIMITIVE_WINDOW_EXACT`.

For a checkable large case, when \(\ell=13\), the first four top intersections \(M_{13,0},\ldots,M_{13,3}\) are \(57468093927120\), \(21172455657360\), \(7820456594160\), and \(2896406039280\); all twenty top intersections have gcd \(3\). The complete integer arrays, including the transition at \(\ell=16\), are embedded in the certificate. The proof requires no extrapolation beyond the finite domain and no floating-point arithmetic.

## Relationship to prior work

Huan Xiong, *Low-degree filtrations in ordinary and Lagrangian Grassmannian cohomology* (2026), proves rational generation/filtration results. Its Corollary 7.4 implies rational top-class generation by the first two Chern classes, while Remark 7.9 expressly does not assert integral analogues. Its Appendix C.3 gives the classical integral intersection/Kostka-number formula, a starting identity used here, but not the stated first-loss/return classification for the top lattice index. Reiner--Tudose's 2003 conjectures and the 2020 Polymath Jr. filtration paper concern rational coefficient generation and Hilbert series; these neither imply nor exclude the nontrivial finite integral index. An integer top generator exists in the rational span even when the integral subalgebra has index three.

## Limitations

The classification is deliberately confined to the first sixteen widths; no periodicity, asymptotic assertion, or claim for larger widths is made. It concerns only the *top-degree* integral image of a two-generator subalgebra, not its integral Hilbert series in all degrees. The exact finite procedure is fully reproducible, but no independent mathematical audit has been performed. Older unpublished or specialized divisibility results could affect historical priority.

## References

1. H. Xiong, *Low-degree filtrations in ordinary and Lagrangian Grassmannian cohomology*, arXiv:2610.28780v1 (first public version 2026-10-20), especially Corollary 7.4, Remark 7.9, Appendix C.3.
2. V. Reiner and G. Tudose, *Conjectures on the cohomology of the Grassmannian*, arXiv:math/0309281 (2003).
3. Polymath Jr. Grassmannian group, *Filtering cohomology of ordinary and Lagrangian Grassmannians*, arXiv:2011.03179v2 (2021).
4. W. Fulton, *Young Tableaux: With Applications to Representation Theory and Geometry*, Cambridge University Press (1997), for integral Schubert and Pieri rules.
