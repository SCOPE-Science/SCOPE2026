# Homothetic John–Löwner ellipses of intersections of equal-area centered ellipses

## Finding
Let \(A,B\) be any real symmetric positive-definite \(2\times2\) matrices with \(\det A=\det B=d>0\). Define their centered filled ellipses and intersection by
\[
E_A=\{x\in\mathbb R^2:x^{\mathsf T}Ax\le1\},\qquad
E_B=\{x\in\mathbb R^2:x^{\mathsf T}Bx\le1\},\qquad K=E_A\cap E_B.
\]
Set \(M=(A+B)/2\), and let the affine-invariant mismatch be
\[
\delta=\sqrt{\operatorname{tr}(A^{-1}B)-2}\ge0,\qquad
s=\frac{\delta}{\sqrt{4+\delta^2}}=\sqrt{1-\frac d{\det M}}\in[0,1).
\]
Then the **unique maximal-area ellipse contained in** \(K\) (John ellipse) and the **unique minimal-area ellipse containing** \(K\) (Löwner ellipse), with no restriction on their centers or orientations, are exactly
\[
\boxed{E_J=\{x:x^{\mathsf T}Mx\le(1+s)^{-1}\},\qquad
E_L=\{x:x^{\mathsf T}Mx\le1\}.}
\]
They are concentric and homothetic for **every** such pair, even if the ellipses are not congruent or have nonaligned axes. Their areas obey the exact sharp law
\[
\boxed{\frac{|E_L|}{|E_J|}=1+s=1+\frac\delta{\sqrt{4+\delta^2}}\in[1,2).}
\]
The ratio equals \(1\) precisely when \(A=B\), approaches but never attains \(2\), and recovers the affine mismatch uniquely:
\[
\boxed{\delta=\frac{2(\rho-1)}{\sqrt{\rho(2-\rho)}}\quad\text{for}\quad\rho=|E_L|/|E_J|\in[1,2).}
\]
When \(A\ne B\), \(E_L\) has four contact points (two antipodal pairs) with \(K\), precisely the four intersections of the two original ellipse boundaries; \(E_J\) has four contact points, two antipodal pairs on alternating input ellipse arcs. Their normalized contacts each form a four-point isotropic certificate.

## Assumptions and scope
The region \(K\) is the **intersection** of exactly two nondegenerate, concentric, equal-area filled Euclidean ellipses in the plane, using inverse shape (quadratic-form) matrices \(A,B\). The equality of their areas is equivalent to equality of determinants. The extremal ellipses are optimized among **all** translated and rotated ellipses, not only ellipses concentric with \(K\). The degenerate equality case \(A=B\) is included. The theorem does not assume the original ellipses have identical eccentricities or orthogonal axes; affine changes are intrinsic to its conclusion.

## Proof
**1. Spectral normalization.** The positive-definite matrix \(M\) has an invertible symmetric square root. Write \(D=(A-B)/2\), \(y=M^{1/2}x\), and \(C=M^{-1/2}DM^{-1/2}\). The two defining inequalities become
\[
y^{\mathsf T}(I+C)y\le1,\qquad y^{\mathsf T}(I-C)y\le1.
\]
Since \(\det(M+D)=\det(M-D)=d\), the explicit \(2\times2\) determinant identity \(\det(M+D)-\det(M-D)=2\det M\operatorname{tr}(M^{-1}D)\) implies \(\operatorname{tr}C=0\). Hence the real symmetric \(C\) has eigenvalues \(s\) and \(-s\), for some \(s\ge0\). Positivity of \(I\pm C\) gives \(s<1\), and taking determinants gives \(d=\det M(1-s^2)\), proving the first formula for \(s\).

A final orthogonal change of \(y\)-coordinates diagonalizes \(C\). In the resulting coordinates \(z\), the intersection has the **exact** description
\[
\boxed{K'=\left\{z\in\mathbb R^2:\|z\|^2+s|z_1^2-z_2^2|\le1\right\}.}
\]
Thus it has all reflections and quarter-turn rotations of a square, regardless of the initial ellipses' orientations. In polar coordinates the boundary radius is
\[
r(\theta)=(1+s|\cos 2\theta|)^{-1/2},\qquad
(1+s)^{-1/2}\le r(\theta)\le1.
\]

**2. Exact global optimality.** Every compact convex body with interior has unique John and Löwner ellipses; both optimizers transform affinely under invertible linear coordinate changes. The uniqueness and central reflection symmetry of \(K'\) force both optimal ellipses to be centered at the origin. The quarter-turn symmetry then forces their quadratic matrices to commute with a right-angle rotation, and symmetry of those matrices makes them scalar multiples of \(I\). Hence **both are circles**, even when the optimization permits arbitrary translated and tilted ellipses. The largest centered disk inside \(K'\) has radius \((1+s)^{-1/2}\), attained at the coordinate axes; the smallest centered disk containing \(K'\) has radius \(1\), attained on the two diagonals. Therefore these disks are the unique John and Löwner ellipses of \(K'\). Transforming them back by \(M^{-1/2}\) proves both boxed quadratic-form descriptions.

For explicit contact certificates in the normalized eigenbasis, the four John contacts are \(\pm(1+s)^{-1/2}e_1\) and \(\pm(1+s)^{-1/2}e_2\). The four Löwner contacts are the vectors \(\pm(e_1+e_2)/\sqrt2\) and \(\pm(e_1-e_2)/\sqrt2\). After scaling by the respective optimal radii, each four-point set has vector sum zero and outer-product sum \(2I\), so assigning weight \(1/2\) to each point produces \(I\), the usual planar isotropic extremality certificate. For \(s>0\), the outer four points lie on both source ellipse boundaries, while each inner contact lies on one source boundary (alternating with the other).

**3. Invariant formula and sharpness.** The determinant identity for a sum of two \(2\times2\) matrices gives
\[
\det M=\frac14\bigl(\det A+\det B+\det A\operatorname{tr}(A^{-1}B)\bigr)
=d\left(1+\frac{\delta^2}{4}\right).
\]
Hence \(s=\delta/\sqrt{4+\delta^2}\). Since a planar ellipse \(\{x:x^{\mathsf T}Mx\le c\}\) has area \(\pi c/\sqrt{\det M}\), the optimum area ratio is \(1+s\). Inverting this strictly increasing function yields \(\delta=2(\rho-1)/\sqrt{\rho(2-\rho)}\). Equality \(\rho=1\) forces \(s=0\), hence \(C=0\) and \(A=B\). The upper endpoint is sharp: take \(A=\operatorname{diag}(t,t^{-1})\) and \(B=\operatorname{diag}(t^{-1},t)\) with \(t\to\infty\); their area ratio is \(2t^2/(1+t^2)\to2\). Strict positive definiteness excludes the limiting value.

## Verification
The independently executable `CHECK.py` constructs 187 equal-determinant matrix pairs, including noncommuting positive-definite matrices and nearly degenerate pairs. It compares the two mismatch expressions, both normalized spectral eigenvalues, containment and contact identities, the exact area ratio, and bounds on the numerically integrated intersection area. Running `python CHECK.py` from the extracted package returned `EQUAL_AREA_ELLIPSE_EXTREMAL_PAIR_CHECKS_OK 187`. These are finite consistency checks only; the exact equal-determinant symmetry argument above proves the theorem for all admissible pairs.

## Relationship to prior work
Kahan's 1968 ellipsoid-intersection theorem (also available in an expanded 2006 author-hosted version) already classifies a complete family of *tight outer circumscribing ellipsoids* by convex combinations of the two input quadratic matrices. In particular, the present **outer-ellipse formula alone is not claimed as novel**; it also follows from determinant maximization within Kahan's family. Seeger (1993) supplies general exact calculus representations of intersections, convex hulls and approximating ellipsoids but does not state this optimal *joint inner-and-outer* pair for two equal-area ellipses or its sharp spectral ratio. The novelty assessed here is specifically the global John–Löwner homothety theorem, including its exact John ellipse and inverse affine mismatch from their area ratio. General Löwner–John existence, uniqueness and contact certificates are classical, as is the universal factor-two upper bound for the area ratio of an arbitrary centrally symmetric planar convex body. The new assertion is the exact lens-family ratio, strictness, and its inverse spectral classification. Hughes and Chraibi (2011) determine overlap area algorithmically rather than either optimal ellipse. Earlier work on exact hull area of equal-area ellipse pairs and exact Mahler area products of perpendicular pairs supplies different invariants; their statements do not furnish the present optimal inner ellipse and ratio without an additional extremality argument.

## Limitations
The equal determinant and common center hypotheses are essential to the normalization; no claim is made for two unequal-area or translated ellipses or for three or more ellipses. The outer-ellipsoid part has an explicit classical precursor. The formula is an exact analytic result; finite checks do not establish global optimality. Specialist priority assessment may locate an earlier equivalent result under a different parametrization, particularly in ellipsoidal optimization or covariance-intersection literature. There has been no independent mathematical validation.

## References
- W. Kahan, *Circumscribing an Ellipsoid about the Intersection of Two Ellipsoids*, Canadian Mathematical Bulletin 11 (1968), 437–441, DOI: 10.4153/CMB-1968-050-2; expanded author-hosted text https://people.eecs.berkeley.edu/~wkahan/Ellipint.pdf.
- A. Seeger, *Calculus Rules for Combinations of Ellipsoids and Applications*, Bulletin of the Australian Mathematical Society 47 (1993), 1–12, DOI: 10.1017/S0004972700012211; full text https://www.cambridge.org/core/services/aop-cambridge-core/content/view/23D96ED16EB5A8CE04D54D746917BF3B/S0004972700012211a.pdf/calculus-rules-for-combinations-of-ellipsoids-and-applications.pdf.
- G. B. Hughes and M. Chraibi, *Calculating Ellipse Overlap Areas*, arXiv:1106.3787, first submitted 2011-06-19; https://arxiv.org/abs/1106.3787.
- M. Henk, *Löwner–John Ellipsoids*, Documenta Mathematica Extra Volume ISMP (2012), 95–106, DOI: 10.4171/DMS/6/15.
