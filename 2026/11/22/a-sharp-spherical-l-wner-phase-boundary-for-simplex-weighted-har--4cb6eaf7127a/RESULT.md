# A sharp spherical-Löwner phase boundary for simplex-weighted harmonic polytopes

## Finding

Let \(n\ge2\) be an integer, \(\lambda>0\), and define the canonical simplex-weighted harmonic polytope
\[
H_n(\lambda)=(\Pi_n\times\Pi_n)+\lambda\operatorname{conv}\{(e_i,e_i):1\le i\le n\}\subset\mathbb R^n\times\mathbb R^n,
\]
where \(\Pi_n\) is the convex hull of permutations of \((1,\ldots,n)\). The ambient Euclidean metric is restricted to the affine hull of dimension \(2n-2\). Its uniquely determined smallest enclosing Euclidean ball has center \(c_\lambda=(\mu\mathbf{1},\mu\mathbf{1})\), where \(\mu=(n+1)/2+\lambda/n\), and squared radius
\[
R_n(\lambda)^2=\frac{n(n^2-1)}6+2\lambda(n-1)+\frac{2\lambda^2(n-1)}n.
\]

**Theorem (sharp spherical-Löwner criterion).** That ball is also the unique minimum-volume enclosing ellipsoid of \(H_n(\lambda)\) **if and only if**
\[
\boxed{n\ge6\quad\text{and}\quad0<\lambda\le\lambda_c(n):=\frac n2\left(\sqrt{\frac{n-2}{3}}-1\right).}
\]
At and below this threshold an explicit two-orbit isotropic distribution on the sphere contacts certifies optimality. Above it, or for \(2\le n\le5\), a strictly smaller-volume non-spherical enclosing ellipsoid exists. For the standard harmonic polytope \(\lambda=1\), the exact dimension threshold is \(n=7\): its enclosing ellipsoid is a Euclidean ball precisely for \(n\ge7\). The critical scale satisfies \(\lambda_c(n)\sim n^{3/2}/(2\sqrt3)\).

For every \(\lambda>0\), independently of the criterion, the sphere-contact vertices are exactly the \(n((n-1)!)^2\) points \((p+\lambda e_i,q+\lambda e_i)\), where both permutations \(p,q\) of \((1,\ldots,n)\) put \(n\) at coordinate \(i\). The radius and this contact classification are included to make the new ellipsoid criterion reproducible; the unit-weight minimum-sphere results and contact enumeration were previously known.

## Assumptions and scope

All assertions use ordinary Euclidean distance in the affine hyperplanes where each block has coordinate sum \(n(n+1)/2+\lambda\), not the quotient metric arising from an arbitrary nonorthogonal realization. The parameter \(\lambda\) is any positive real number; the degenerate product case \(\lambda=0\) is excluded. The result characterizes **when** the true Löwner ellipsoid is round, and provides its exact center and radius in that regime. It does not claim closed-form principal semiaxes in the nonspherical regime.

The notation \(e_i\) means the standard coordinate vector and \(\mathbf{1}\) the all-ones vector. Write \(U=\{x\in\mathbb R^n:\sum_i x_i=0\}\), so the affine tangent space is \(U\oplus U\) of dimension \(d=2n-2\).

## Proof

**1. Circumsphere and contact vertices.** Put \(h=(n-1)/2\), \(S=n(n^2-1)/12\), and \(\tau_i=e_i-\mathbf{1}/n\), with \(\|\tau_i\|^2=(n-1)/n\). After subtracting \(c_\lambda\), every generating point is
\[
(u,v)=(a+\lambda\tau_i,b+\lambda\tau_i),
\]
where \(a,b\) range over permutations of the centered list \(((1-n)/2,\ldots,(n-1)/2)\). Its squared norm is
\[
\|(u,v)\|^2=2S+2\lambda(a_i+b_i)+\frac{2\lambda^2(n-1)}n.
\]
Because \(a_i,b_i\le h\), this attains the displayed \(R_n(\lambda)^2\) exactly when \(a_i=b_i=h\). Distinct such triples give distinct vertices: choose strictly ordered support directions for both permutohedra whose maximum coordinates are \(i\), so that the diagonal simplex exposes \((e_i,e_i)\) uniquely. Every point of the Minkowski sum is a convex combination of generating points; strict convexity of squared norm means that no other points touch the sphere. The polytope and the unique minimum enclosing Euclidean ball are invariant under simultaneous coordinate permutations and exchange of the two blocks. The only fixed point in their affine hull is \(c_\lambda\), so uniqueness of the minimum enclosing ball proves it is the ball just identified.

**2. A sharp contact cross-correlation interval.** On a sphere contact \((u,v)\), both \(a_i=b_i=h\) and each block has the same squared norm
\[
L=S+2\lambda h+\lambda^2\frac{n-1}n=\frac{R_n(\lambda)^2}2.
\]
Its cross inner product is \(C=\langle u,v\rangle=\langle a,b\rangle+2\lambda h+\lambda^2(n-1)/n\). With the largest entry pinned to the same coordinate in the two permutations, the rearrangement inequality says the minimum of \(\langle a,b\rangle\) is achieved by pairing the remaining \(n-1\) entries in reverse order, while the maximum pairs them equally. Direct summation gives
\[
\min\langle a,b\rangle=-\frac{n(n-5)(n-1)}{12},\qquad
\max\langle a,b\rangle=S.
\]
Hence the exact minimum and maximum contact correlations are
\[
C_-= (n-1)\left(-\frac{n(n-5)}{12}+\lambda+\frac{\lambda^2}n\right),\qquad C_+=L>0.
\]
Thus \(C_-\le0\) is equivalent to \(n\ge6\) and \(\lambda^2+n\lambda\le n^2(n-5)/12\). Solving the positive quadratic root gives the stated \(\lambda_c(n)\).

**3. Global ellipsoid optimality when \(C_-\le0\).** Choose a contact triple with \(\langle u,v\rangle=C_+\) (the two centered permutations agree) and one with \(\langle u,v\rangle=C_-\) (their remaining entries are oppositely ordered). Average each triple under the full simultaneous coordinate-permutation group. Each orbit measure has mean zero in \(U\oplus U\). On either orbit, the within-block covariance is exactly \(L I_U/(n-1)\), by the irreducibility of the standard permutation representation; its cross-block covariance is \(C I_U/(n-1)\), as follows by taking traces and using the same invariance. Mix the two orbit measures with respective weights
\[
\theta=\frac{-C_-}{C_+-C_-},\qquad1-\theta=\frac{C_+}{C_+-C_-}.
\]
These are nonnegative and sum to one (at the equality boundary the first weight is zero). The mixture has cross covariance zero and total covariance
\[
\operatorname{Cov}(u,v)=\frac{L}{n-1}I_{U\oplus U}=\frac{R_n(\lambda)^2}{d}I_{U\oplus U}.
\]
For any enclosing ellipsoid \(E=\{z:(z-t)^TQ(z-t)\le1\}\) in the affine hull with \(Q\) positive definite, averaging its inequalities over this contact measure yields
\[
\frac{R_n(\lambda)^2}{d}\operatorname{tr}Q+t^TQt\le1.
\]
In particular \(\operatorname{tr}Q\le d/R_n(\lambda)^2\). The arithmetic-geometric mean inequality on the eigenvalues gives \(\det Q\le R_n(\lambda)^{-2d}\), with equality only for \(Q=R_n(\lambda)^{-2}I\) and \(t=0\). Since ellipsoid volume is proportional to \((\det Q)^{-1/2}\), the ball is the unique globally volume-minimizing ellipsoid.

**4. Strictly better anisotropic ellipsoids when \(C_->0\).** Every sphere contact now has strictly positive block correlation. On \(U\oplus U\) consider the positive-definite form
\[
Q_\varepsilon(u,v)=\|u\|^2+\|v\|^2-2\varepsilon\langle u,v\rangle,
\qquad0<\varepsilon<1.
\]
At every sphere contact it is at most \(R_n(\lambda)^2-2\varepsilon C_-\). There are finitely many other generating points and all have a positive Euclidean radial gap; for sufficiently small \(\varepsilon>0\), the maximum of \(Q_\varepsilon\) over the whole polytope is exactly \(M_\varepsilon=R_n(\lambda)^2-2\varepsilon C_-\) (convexity puts maxima at generating points). The ellipsoid \(Q_\varepsilon\le M_\varepsilon\) therefore encloses the polytope. The form has eigenvalues \(1-\varepsilon\) and \(1+\varepsilon\), each of multiplicity \(n-1\); thus its volume divided by that of the circumball equals
\[
\left(1-\frac{2\varepsilon C_-}{R_n(\lambda)^2}\right)^{d/2}
(1-\varepsilon^2)^{-(n-1)/2}=1-\frac{dC_-}{R_n(\lambda)^2}\varepsilon+O(\varepsilon^2)<1.
\]
The ball is not the Löwner ellipsoid. Any spherical Löwner ellipsoid would have to equal this circumball, because the unique Löwner ellipsoid inherits all polytope symmetries and its center must be \(c_\lambda\); hence the criterion is also necessary.

**5. The unit-weight dimension threshold.** At \(\lambda=1\), the inequality is \(n^2(n-5)\ge12(n+1)\). It fails through \(n=6\) and holds at \(n=7\). Its left side grows strictly faster thereafter (equivalently, \(\lambda_c(n)\) is increasing for integer \(n\ge6\)); thus exactly \(n\ge7\) is the spherical regime. The asymptotic for \(\lambda_c(n)\) follows by extracting \(\sqrt{n/3}\) in its closed form.

## Verification

The standalone \(check.py\) uses rational arithmetic to enumerate all formal Minkowski-sum generating points for \(2\le n\le5\) at three positive rational values of \(\lambda\). It confirms the exact radius, the full contact count and that every contact has the stated top-coordinate property (12 complete formal-vertex configurations). Separately, for \(2\le n\le8\) and three rational weights, it enumerates all pairings of the remaining entries after fixing the common top coordinate, confirming the analytic rearrangement extrema and the threshold sign (21 configurations). The executed program prints `HARMONIC_LOEWNER_THRESHOLD_PASS formal_vertex_cases= 12 rearrangement_cases= 21`. These are finite consistency checks; the unrestricted assertions for all integers and real parameters are proved by the algebraic and convex-geometric arguments above.

## Relationship to prior work

Ardila and Escobar (arXiv:2006.03078, first version June 4, 2020) introduce \(H_{n,n}\), its Minkowski description, vertex classification and combinatorial enumeration. Previously reported Euclidean shell and minimum-sphere results already establish the unit-weight radius and contact set; neither a radius calculation nor that classification is asserted as new. Other work on the simplex-weighted harmonic family establishes an **inball** center transition, not a criterion for when the unrestricted **minimum-volume enclosing ellipsoid** is spherical. Uniform-vertex covariance studies of harmonic polytopes concern a different probability measure from the optimizing measure on circumsphere contacts. The general Löwner contact criterion (and analogous work on metric polytopes) supplies a tool, but not this family's exact inequality \(\lambda^2+n\lambda\le n^2(n-5)/12\). The contribution here is the exact all-parameter outer-ellipsoid roundness boundary, the construction of an optimal isotropic contact distribution on one side and an explicit strict-volume competitor on the other.

## Limitations

The result does not calculate the nonround Löwner ellipsoid's semiaxes or its contacts in the complementary parameter regime. It assumes strictly positive simplex weight; the product polytope at zero weight has a different vertex structure. Although related literature and public mathematical-record searches were compared, an unindexed equivalent criterion remains possible and historical priority has not been independently established. The verification script is not a substitute for the all-parameter proof or for independent mathematical review.

## References

- F. Ardila and L. Escobar, *The harmonic polytope*, arXiv:2006.03078v1 (June 4, 2020), https://arxiv.org/abs/2006.03078 ; full text https://arxiv.org/html/2006.03078v2 .
- R. Gartsman and N. Linial, *On the Löwner–John Ellipsoids of the Metric Polytope*, arXiv:2305.02113 (2023), https://arxiv.org/abs/2305.02113 . The isotropic contact criterion appears in their Section 2 for a different geometric object.
- *Harmonic-polytope vertices form exactly n Euclidean shells*, public mathematical record (2026). Prior unit-weight circumsphere and contact calculations.
- *A sharp inball-center phase transition in simplex-weighted harmonic polytopes*, public mathematical record (2026). Prior inball (not Löwner) parameter transition.
- *A nine-label covariance-axis reversal in harmonic polytopes*, public mathematical record (2026). Prior uniform-vertex covariance, not contact covariance.
