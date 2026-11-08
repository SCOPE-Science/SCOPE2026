# Contact-refined punctual Hilbert series for every higher odd cusp

## Finding

Let \(k\) be an arbitrary field, let \(d\ge 2\) be an integer, and put
\[
R_d=k[[x,y]]/(y^2-x^{2d+1}),\qquad \mathbb L=[\mathbb A_k^1].
\]
For an ideal \(I\subset R_d\) of finite colength \(n\), define its \(x\)-contact \(j_x(I)=\dim_k R_d/(I+(x))\). Define the motivic contact-refined punctual Hilbert series by
\[
G_d^x(Q,z)=\sum_{n,j\ge0}[\operatorname{Hilb}_n(\operatorname{Spec}R_d,0)_{j_x=j}]\,Q^nz^j
\in K_0(\operatorname{Var}_k)[z][[Q]].
\]
The brackets denote classes of the reduced underlying locally closed varieties. Set
\[
F_d(Q)=\sum_{h=0}^{2d+1}\mathbb L^{\lfloor h/2\rfloor}Q^h
=(1+Q)\sum_{i=0}^d(\mathbb L Q^2)^i.
\]
Then **for all fields and all colengths**,
\[
\boxed{G_d^x(Q,z)=1+z(F_d(Q)-1)+z^2\frac{Q^2F_d(Q)}{1-Q^2}.}
\]
In particular, the only possible contacts are \(0,1,2\). The contact-one locus in colength \(n\) is \(\mathbb A_k^{\lfloor n/2\rfloor}\) for \(1\le n\le2d+1\), and empty otherwise. The contact-two locus admits a disjoint locally closed affine stratification whose pieces are \(\mathbb A_k^{\lfloor h/2\rfloor}\), indexed by \(h\in[0,2d+1]\) satisfying \(n-h\in2\mathbb Z_{\ge2}\). Contact zero occurs only at colength zero.

For every \(u\ge0\), applying the arbitrary-germ fat-branch formula of Huang--Jiang--Oblomkov gives the explicit identity
\[
\boxed{\sum_{n,j\ge0}[\operatorname{Hilb}_n(\{x^u(y^2-x^{2d+1})=0\},0)_{j_x=j}]Q^nz^j
=\frac{G_d^x(Q,(Q\mathbb L)^u z)}{\prod_{i=0}^{u-1}(1-Q^{i+1}\mathbb L^i z)}.}
\]
The empty product for \(u=0\) is one. The added-branch identity uses the cited theorem rather than a new proof of the modification theorem.

## Assumptions and scope

The germ is the plane unibranch singularity defined by \(y^2=x^{2d+1}\), with \(d\ge2\), at its closed origin. There is no characteristic restriction: \(x=t^2,y=t^{2d+1}\) identifies \(R_d\) with \(k[[t^2,t^{2d+1}]]\) even in characteristic two. All colengths \(n\ge0\) are included, and coefficients are in the ordinary Grothendieck ring of varieties, not a virtual or vanishing-cycle theory. Contact is measured against the fixed Cartier-coordinate direction \(x\), so exchanging the coordinates changes the statistic.

## Proof

Write \(A=k[[x]]\). The ring \(R_d=A\oplus Ay\) is free of rank two over the discrete valuation ring \(A\), with \(y^2=x^{2d+1}\). Every finite-colength ideal \(I\) is a rank-two \(A\)-submodule. Its intersection with \(A\) has the form \((x^a)\), and the projection of \(I\) to the coefficient of \(y\) is \(x^bA\), for unique \(a,b\ge0\). Since \(yx^a\in I\), necessarily \(a\ge b\). Put \(h=a-b\).

Choose a generator with \(y\)-coefficient \(x^b\), written initially as \(x^by+c(x)\). The condition \(y(x^by+c)\in I\) forces \(c\in x^bA\), so \(c=x^bg(x)\). After reduction modulo \(x^a\), the polynomial \(g\) is uniquely defined modulo \(x^h\). The exact normal form is therefore
\[
I=(x^{b+h},\ x^b(y+g(x)))_A,\quad g\in A/(x^h),\qquad n=\dim_k R_d/I=2b+h.
\]
Multiplication by \(y\) preserves this \(A\)-submodule if and only if
\[
x^h\mid x^{2d+1}-g(x)^2.
\]
Indeed \(y x^{b+h}\) is a multiple of the second generator modulo the first, and subtracting \(g\) times the second generator from \(y x^b(y+g)\) leaves \(x^b(x^{2d+1}-g^2)\). No other equation is required.

If \(h>2d+1\), the right-hand divisibility is impossible. A formal square has even \(x\)-valuation, so its leading term cannot cancel the odd-order monomial \(x^{2d+1}\), in any characteristic. For \(0\le h\le2d+1\), the divisibility condition is equivalent, on the reduced parameter variety, to \(g\equiv0\pmod{x^{\lceil h/2\rceil}}\). Conversely, every such residue satisfies the equation. The free coefficients of degrees \(\lceil h/2\rceil,\ldots,h-1\) give the affine space \(\mathbb A_k^{\lfloor h/2\rfloor}\).

These are genuinely locally closed affine strata in the reduced punctual Hilbert varieties, not merely counts of rational points. To see this, for a fixed colength \(n\), every ideal contains \(x^n\), so it lies in a finite Grassmannian of subspaces of the \(2n\)-dimensional \(k\)-space \(R_d/(x^n)\), with closed invariance conditions under \(x\) and \(y\). The conditions fixing the pivot degrees \(a,b\) are a Grassmannian echelon/Schubert stratum. The normal form above gives regular coordinates there, and its reduced equations are precisely the indicated coordinate vanishings. The same argument holds after arbitrary extension of the ground field.

Reducing the normal-form generators modulo \((x)\) gives \(j_x(I)=1\) if \(b=0,h\ge1\), and \(j_x(I)=2\) if \(b\ge1\). If \(b=h=0\), the ideal is the whole ring, giving \(j_x=0\). The contact-one strata therefore contribute \(z(F_d(Q)-1)\); summing the contact-two contributions over all \(b\ge1\) gives
\[
z^2\sum_{b\ge1}Q^{2b}\sum_{h=0}^{2d+1}\mathbb L^{\lfloor h/2\rfloor}Q^h
=z^2\frac{Q^2F_d(Q)}{1-Q^2}.
\]
Including the unique colength-zero ideal proves the asserted closed expression. Finally, Corollary 6.8 of Huang--Jiang--Oblomkov applies with \(g=y^2-x^{2d+1}\) and supplies the stated fat-branch formula; the denominator uses \(Qz\), not \(Q\), as its first geometric parameter.

## Verification

Setting \(z=1\) gives
\[
G_d^x(Q,1)=\frac{\sum_{i=0}^d(\mathbb L Q^2)^i}{1-Q},
\]
which agrees with the established unrefined motivic series for type \(A_{2d}\) singularities. In the boundary case \(d=1\), intentionally excluded from the novelty assertion, the formula specializes to the known contact refinement of the ordinary cusp \(y^2=x^3\).

For \(d=2\), the contact-one part is \(Qz+\mathbb L(Q^2+Q^3)z+\mathbb L^2(Q^4+Q^5)z\), while for every \(n\ge6\) the entire colength-\(n\) stratum has contact two and class \(1+\mathbb L+\mathbb L^2\). This provides an explicit low-degree diagnostic.

The standalone program `verify_contact.py`, run with `python3 verify_contact.py`, directly enumerates polynomial residues over \(\mathbb F_2\) and \(\mathbb F_3\), checks the full ideal-stability congruence for 48 parameter combinations of the degree cutoff, and compares independent coefficient expansions through colength 21. Its expected output is `FINITE_FIELD_STABILITY_AND_SERIES_TEST_OK 48`. These computations only corroborate the proof; they do not establish the infinite/all-field result.

## Relationship to prior work

The October 2026 preprint by Huang, Jiang and Oblomkov formulates computing contact-refined zeta functions of unibranch germs such as \(y^p=x^q\) as Question 11.4. Its Corollary 6.8 is the previously established universal fat-branch propagation rule used here. It does not supply the displayed contact formula for higher odd cusps.

Sōma and Watari (2015) classify and stratify punctual Hilbert schemes of type \(A_{2d}\) over algebraically closed characteristic-zero fields. Their comprehensive semigroup and affine-cell descriptions are the closest structural antecedent: they could permit extraction of related contact information, although the contact-weighted rational formula and the arbitrary-field argument are not statements established there. The unrefined formula for these cusps is also known from Hajli, Mourtada and Zhu (2025); specializing \(z=1\) is a consistency check, not a new result. The ordinary-cusp contact series is already known and is not claimed again.

## Limitations

The result treats only the \((2,2d+1)\) unibranch family and its specified thick-line additions, not arbitrary \((p,q)\) cusps, intersections of two independently fat branches, Hilbert-scheme scheme structures, or cohomological gradings. The 2015 characteristic-zero ideal-stratification literature is close enough that priority for extracting the contact statistic must remain qualified; independent review has not been performed. The all-field proof concerns reduced motivic classes and does not claim reducedness of the Hilbert schemes themselves.

## References

1. Y. Huang, R. Jiang, and A. Oblomkov, *Sheaves on nodal singularities I*, arXiv:2610.34676 (submitted 2026-10-26), especially Corollary 6.8 and Question 11.4. https://arxiv.org/abs/2610.34676
2. Y. Sōma and M. Watari, *The punctual Hilbert schemes for the curve singularities of type \(A_{2d}\)*, Journal of Singularities **11** (2015), 152–163, DOI:10.5427/jsing.2015.11f. https://www.journalofsing.org/volume11/soma-watari.pdf
3. Hajli, Mourtada, and Zhu, *On the geometry of punctual Hilbert schemes on singular curves and their motivic zeta functions*, arXiv:2509.06761 (2025), for the unrefined comparison. https://arxiv.org/abs/2509.06761
4. Y. Huang and R. Jiang, *Punctual Quot schemes and Cohen–Lenstra series of the cusp singularity*, arXiv:2305.06411 (2023), for the ordinary cusp background. https://arxiv.org/abs/2305.06411
