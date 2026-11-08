# A shared insphere and a sharp incenter-dimension jump for partial alternating-sign-matrix polytopes

## Finding

For every pair of positive integers \(m,n\), set \(M=\max\{m,n}\) and \(r=1/(M+\sqrt M)\). The Euclidean inradius of each of the full-dimensional matrix polytopes \(\mathrm{PASM}(m,n)\) and \(\mathrm{PPerm}(m,n)\), measured with the Frobenius norm of the unscaled matrix entries, is exactly \(r\). Both contain the ball \(B_F(r\mathbf1_{m\times n},r)\).

The matching polytope has one incenter, \(r\mathbf1_{m\times n}\). By contrast the affine dimension of the complete center locus of the partial alternating-sign-matrix polytope is
\[
\dim\operatorname{Incenters}(\mathrm{PASM}(m,n))=
\begin{cases}mn-M,&m\ne n,\\ (n-1)^2,&m=n.\end{cases}
\]
In particular, the latter locus is a singleton exactly when \(\min\{m,n}=1\); otherwise it has positive dimension. When \(n>m\), the first row is forced to equal \((r,\ldots,r)\); when \(m>n\), the first column is forced; and when \(m=n\), both are forced. These are *all* affine equalities holding throughout the center locus.

At a center in the relative interior of the center locus, the ball is tangent to precisely \(M+1\) facets for \(m\ne n\), to precisely \(2n+1\) facets for \(m=n\ge2\), or to the two endpoints for \(m=n=1\). Boundary centers may have further contacts. The conclusion is about Euclidean Frobenius geometry, not an affine-invariant quantity.

## Assumptions and scope

A partial alternating-sign matrix is an \(m\times n\) matrix whose entries belong to \(\{-1,0,1\}\) and whose **every initial row and column sum** lies in \(\{0,1\}\). Its convex hull in \(\mathbb R^{mn}\) is \(\mathrm{PASM}(m,n)\). A partial permutation matrix is a zero-one matrix with at most one one in every row and column; their convex hull is \(\mathrm{PPerm}(m,n)\). The Euclidean norm is \(\|X\|_F=(\sum_{i,j}X_{ij}^2)^{1/2}\), without any rescaling. A center \(C\) is optimal if the closed Frobenius ball of radius \(r\) about \(C\) is contained in the corresponding polytope. Both convex hulls are full-dimensional: they include the zero matrix and all \(mn\) elementary coordinate matrices.

The following exact halfspace representation for the first polytope is the published theorem of Heuer--Striker (2020/2022): for all \(1\le i\le m\), \(1\le j\le n\), both column prefixes \(\sum_{a=1}^iX_{aj}\) and row prefixes \(\sum_{b=1}^jX_{ib}\) lie in \([0,1]\). It is used as a premise, not claimed as new. The second polytope has the standard inequalities \(X_{ij}\ge0\), \(\sum_jX_{ij}\le1\), and \(\sum_iX_{ij}\le1\).

## Proof

**Ball criterion.** The coefficient vector of a row-prefix inequality of length \(j\) has Frobenius norm \(\sqrt j\); a column prefix of length \(i\) has normal norm \(\sqrt i\). Thus \(B_F(C,\rho)\subseteq\mathrm{PASM}(m,n)\) exactly when, for every \(i,j\),
\[
\rho\sqrt i\le\sum_{a=1}^i C_{aj}\le1-\rho\sqrt i,
\qquad
\rho\sqrt j\le\sum_{b=1}^j C_{ib}\le1-\rho\sqrt j.
\tag{1}
\]
This follows directly by maximizing and minimizing linear functionals on a Euclidean ball. The description need not be irredundant.

**Sharp upper bound.** The column prefixes of length one imply \(C_{1j}\ge\rho\) for all \(j\). The upper bound for the first full row therefore yields
\[
n\rho\le\sum_{j=1}^n C_{1j}\le1-\rho\sqrt n,
\]
so \(\rho\le1/(n+\sqrt n)\). Interchanging row and column gives \(\rho\le1/(m+\sqrt m)\). Therefore \(\rho\le r\). Conversely, at \(C=r\mathbf1\), every prefix of length \(k\le M\) has sum \(kr\), and \(\sqrt k\le k\) and \(k+\sqrt k\le M+\sqrt M\) give both inequalities (1). This constructs the asserted common optimal ball.

**The entire partial-ASM center locus.** At optimal radius \(r\), the chain of equalities in the preceding first-row bound forces each \(C_{1j}=r\) when \(n=M\); the transposed argument forces each \(C_{i1}=r\) when \(m=M\). There can be no additional affine equalities: we construct a point with *every other* inequality in (1) strict. If \(n>m\), fix the first row at \(r\), and in each subsequent row put \(r+\varepsilon\) in column one and \(r-2\varepsilon/(n-1)\) in the other columns. At \(\varepsilon=0\), the only additional tight inequalities are first-column lower bounds and full-row upper bounds; positive sufficiently small \(\varepsilon\) makes these strict, while preserving strictness of the other nonforced inequalities. Every column prefix beyond its first element has positive slack because \(i>\sqrt i\) and \(m+\sqrt m<n+\sqrt n\). The case \(m>n\) is its transpose. If \(m=n\ge2\), keep the first row and column at \(r\) and set each remaining entry to \(r-\varepsilon\). All nonforced bounds then become strict for small positive \(\varepsilon\). The case \(m=n=1\) is the interval \([0,1]\). The strict-slack witnesses give a relatively open full-dimensional set in the affine space specified by forced entries, proving the dimension formula exactly.

**Tangencies.** Heuer--Striker's irredundant facet description includes all nonnegativity inequalities on first-row entries, those on first-column entries, the upper full-first-row inequality, and the upper full-first-column inequality (when not duplicates in dimension one). The strict-slack witnesses show that precisely these hyperplanes are tangent at relative-interior optimal centers: the first-row \(n\) coordinate facets plus its full-row facet in the regime \(n>m\); the transpose when \(m>n\); and \(2n-1\) coordinate facets plus the two full-sum facets for a square with \(n\ge2\).

**Matching-polytope comparison.** For a ball of radius \(\rho\) to lie in \(\mathrm{PPerm}(m,n)\), the nonnegativity facets force *every* \(C_{ij}\ge\rho\). The row and column upper facets give the same upper bounds as above; the uniform matrix \(r\mathbf1\) attains them. If \(n=M\), each row has \(n\) entries at least \(r\) but must have sum at most \(1-r\sqrt n=nr\); all entries are therefore exactly \(r\). The case \(m=M\) is symmetric. Thus the matching incenter is unique although the larger partial-ASM polytope generally has many centers.

For illustration, when \(m=n=2\), all partial-ASM optimal centers are exactly the segment
\[
\begin{pmatrix}r&r\\r&z\end{pmatrix},\qquad
r(\sqrt2-1)\le z\le r,
\quad r=(2+\sqrt2)^{-1}.
\]
In contrast the matching polytope admits only \(z=r\).

## Verification

The accompanying `check.py` independently formulates the complete row/column-prefix Chebyshev linear programs and matching-polytope programs, then solves both for every \((m,n)\) with \(1\le m,n\le8\) (128 linear programs). It verifies the all-parameter formula for these cases, checks affine equality ranks using strict-slack witnesses, checks explicit distinct centers and the two-by-two center segment. Run `python check.py` with the versions of NumPy and SciPy described in `requirements.txt`. The observed message is `PASM_INBALL_CHECKS_PASSED 64 128 linear programs, ranks and witnesses`. These finite checks corroborate, but do **not** establish, the universal theorem; the proof above does that.

## Relationship to prior work

Heuer and Striker's primary paper defines \(\mathrm{PASM}(m,n)\), proves its complete prefix-halfspace and irredundant facet descriptions and studies its face lattices and volumes. These descriptions are necessary premises, and not novel components of this finding. Striker's earlier ordinary alternating-sign-matrix polytope is a different fixed-row/column-sum object. The more recent \(\nu\)-face theory of Heuer, Solhjem, and Striker studies combinatorial faces and their order/flow-polytope identifications. The present claim concerns the exact Euclidean inball, *the full optimal-center locus*, and its contrast with the smaller partial-permutation matching polytope. No implication from the inspected published theorems to this explicit complete metric classification was identified without the new arguments above; earlier equivalent metric formulas remain a priority risk.

## Limitations

The results concern the ordinary unweighted Frobenius metric; scaling entries or changing the norm generally changes the formula. The dimension result is for the **set of centers**, not for a face of the original polytope. No volume, John ellipsoid, or affine-invariant extremality assertion is made. Computer checks cover finitely many dimensions and are not an independent mathematical audit. The earliest source date is the arXiv v1 date of the defining polytope, not its later publication date.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first submitted December 17, 2020, revised 2022; SIAM Journal on Discrete Mathematics **36** (2022), 2863–2888. https://arxiv.org/html/2012.09901v3
2. D. Heuer, S. Solhjem, and J. Striker, *On nu faces of partial alternating sign matrix polytopes*, arXiv:2403.02204, first submitted March 4, 2024. https://arxiv.org/abs/2403.02204
3. J. Striker, *The alternating sign matrix polytope*, Electronic Journal of Combinatorics **16** (2009), #R41. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r41
