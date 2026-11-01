# Exact isoperimetric-deficit law for planar information concavity

## Finding
Let \(K\subset\mathbb R^2\) be a convex body with nonempty interior, area \(A\), and perimeter \(P\). Let \(B_2\) be the Euclidean unit disk, let \(r>0\), and define
\[
K_t=(1-t)K+t rB_2,\qquad 0\le t\le1.
\]
For any planar convex body \(L\), write
\[
I(L)=\frac{\operatorname{area}(L)}{\operatorname{per}(L)}.
\]
Set
\[
P_t=(1-t)P+2\pi r t.
\]
Then for every \(0\le t_0<t_1\le1\), every \(0<\lambda<1\), and \(t_\lambda=(1-\lambda)t_0+\lambda t_1\),
\[
I(K_{t_\lambda})-(1-\lambda)I(K_{t_0})-\lambda I(K_{t_1})
=\frac{\pi r^2(P^2-4\pi A)\lambda(1-\lambda)(t_1-t_0)^2}{P_{t_0}P_{t_1}P_{t_\lambda}}.
\]
Equivalently,
\[
\frac{d^2}{dt^2}I(K_t)
=-\frac{2\pi r^2(P^2-4\pi A)}{P_t^3}.
\]
Thus the complete Jensen deficit of the disk-directed information profile is exactly proportional to the initial isoperimetric deficit \(P^2-4\pi A\). In particular the profile is concave for every planar convex body and strictly concave for every non-disk.

## Assumptions and scope
No boundary smoothness or strict convexity is assumed. The result is two-dimensional and concerns the Minkowski segment from an arbitrary convex body to a Euclidean disk. Translation of \(K\) does not affect any quantity in the statement. The endpoint \(t=1\) is included by continuity.

The claim is quantitative. The qualitative planar concavity/superadditivity phenomenon for the area-to-perimeter information functional is already known; the contribution here is the exact finite Jensen-gap identity and the exact curvature law along this natural disk-directed segment.

## Proof
For \(0\le t<1\), write
\[
K_t=(1-t)\left(K+\frac{rt}{1-t}B_2\right).
\]
The planar Steiner formulas give, for \(s\ge0\),
\[
\operatorname{area}(K+sB_2)=A+sP+\pi s^2,
\qquad
\operatorname{per}(K+sB_2)=P+2\pi s.
\]
After scaling by \(1-t\),
\[
A_t:=\operatorname{area}(K_t)
=(1-t)^2A+rt(1-t)P+\pi r^2t^2,
\]
and
\[
P_t:=\operatorname{per}(K_t)
=(1-t)P+2\pi r t.
\]
These formulas also hold at \(t=1\) by continuity. Direct expansion yields the useful invariant identity
\[
P_t^2-4\pi A_t=(1-t)^2(P^2-4\pi A).
\]
Since \(I(K_t)=A_t/P_t\), differentiating the explicit quadratic-over-linear expression twice and collecting terms gives
\[
I''(t)=-\frac{2\pi r^2(P^2-4\pi A)}{P_t^3}.
\]
This already proves concavity because the planar isoperimetric inequality gives \(P^2-4\pi A\ge0\).

For the exact finite Jensen gap, substitute the explicit formulas for \(A_t\) and \(P_t\) at \(t_0,t_1,t_\lambda\), put the three fractions over the common denominator \(P_{t_0}P_{t_1}P_{t_\lambda}\), and collect the numerator. It factors exactly as
\[
\pi r^2(P^2-4\pi A)\lambda(1-\lambda)(t_1-t_0)^2.
\]
This proves the displayed identity.

For a nontrivial interpolation, meaning \(0<\lambda<1\) and \(t_0<t_1\), equality in the Jensen identity is equivalent to \(P^2=4\pi A\). Equality in the planar isoperimetric inequality holds exactly for Euclidean disks, up to translation. Hence the profile is strictly concave precisely when \(K\) is not a disk.

## Verification
The accompanying `verify.py` performs two exact symbolic checks over rational-coefficient sparse multivariate polynomials, treating \(\pi\) as a formal indeterminate. After clearing denominators, it verifies both the finite Jensen identity and the second-derivative identity. A replay of the packaged checker returns `VERIFY_OK` with zero residual monomials for both identities.

The checker verifies only the algebraic identities. The geometric inputs are the classical planar Steiner formulas and the equality case of the planar isoperimetric inequality; no finite experiment is used as evidence for an infinite statement.

## Relationship to prior work
Gordo Malagón, Saorín Gómez, and Yepes Nicolás study first-order information functionals and the Dembo--Cover--Thomas type Brunn--Minkowski principle. Their 2026 paper records that the classical planar area-to-perimeter inequality is known and explicitly asks about the stronger full-segment concavity phenomenon in a broader abstract framework, where such a strengthening can fail. The present formula stays in the classical planar convex-body setting and identifies the entire disk-directed Jensen gap exactly.

Fradelizi, Giannopoulos, and Meyer established the relevant planar mixed-volume ratio inequality underlying the known qualitative statement. The present identity is not a new proof of novelty for planar concavity itself; it is a quantitative sharpening on the disk-directed path.

Richter and Saorín Gómez study monotonicity of the isoperimetric quotient along outer parallel bodies. That result concerns a different quotient and does not imply the displayed information-functional Jensen identity.

## Limitations
The formula is restricted to dimension two and to a Minkowski segment whose second endpoint is a Euclidean disk. It does not assert an analogous exact law for arbitrary pairs of planar convex bodies or for higher dimensions.

The closest 2003 paper was identified through its theorem statement and bibliographic record, but direct full-text retrieval from the author-hosted PDF was unavailable during this check. This leaves a residual originality risk that the elementary closed form may have appeared unindexed in earlier literature, even though targeted statement-level searches and the inspected recent literature did not reveal it.

## References
1. L. Gordo Malagón, E. Saorín Gómez, J. Yepes Nicolás, *On a Brunn-Minkowski principle for first-order information functionals*, arXiv:2609.07463, first public version 2026-09-07.
2. M. Fradelizi, A. Giannopoulos, M. Meyer, *Some inequalities about mixed volumes*, Israel Journal of Mathematics 135 (2003), DOI 10.1007/BF02776055.
3. C. Richter, E. Saorín Gómez, *On the Monotonicity of the Isoperimetric Quotient for Parallel Bodies*, Journal of Geometric Analysis 32 (2022), DOI 10.1007/s12220-021-00766-2.
