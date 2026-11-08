# Unique vertex-inertia isotropy of isocanted cubes

## Finding
For an integer \(d\ge2\), real \(\ell>0\), and cant depth \(0<a<\ell\), consider the centered isocanted cube
\[
\mathcal I_d(\ell,a)=\left\{z\in\mathbb R^d:\ |z_i|\le\frac\ell2,\quad |z_i-z_j|\le\ell-a\quad(i\ne j)\right\}.
\]
Let \(X\) be chosen **uniformly from the distinct vertices** of this polytope; this is not the uniform-volume distribution. Let \(\Sigma=\operatorname{Cov}(X)\), \(\mathbf1=(1,\ldots,1)^\mathsf T\), and \(J=\mathbf1\mathbf1^\mathsf T\). Define
\[
H=J/d,\qquad x=\frac a{\ell-a}.
\]
The entire covariance spectrum is
\[
\boxed{\lambda_\perp=\frac{2^{d-2}}{2^d-1}(\ell-a)^2\quad\text{(multiplicity }d-1\text{)}}
\]
and
\[
\boxed{\lambda_\parallel=\lambda_\perp\left[1+\frac d{2^d}\big((2^d-1)x^2+2x-1\big)\right]\quad\text{(multiplicity }1\text{)},}
\]
with eigenspaces \(\mathbf1^\perp\) and \(\operatorname{span}\{\mathbf1\}\), respectively, and
\[
\Sigma=\lambda_\perp(I-H)+\lambda_\parallel H.
\]
Both eigenvalues are strictly positive. Their ratio is strictly increasing in \(a/\ell\). **There is exactly one interior cant at which the uniform vertex cloud has isotropic covariance:**
\[
\boxed{\Sigma\text{ is a scalar matrix}\quad\Longleftrightarrow\quad\frac a\ell=\frac1{2+2^{d/2}}.}
\]
For smaller cant, diagonal-axis variance is strictly less than contrast variance; for larger cant, the inequality reverses. The Euclidean covariance condition number \(\lambda_{\max}/\lambda_{\min}\) strictly decreases until this cant, attains its unique global minimum \(1\), and strictly increases afterward. The isotropic cant is asymptotic to \(2^{-d/2}\ell\).

At the isotropic parameter, the \(2^{d+1}-2\) distinct vertices form a centered equal-weight tight frame in \(\mathbb R^d\), but they lie on exactly \(d\) **different** Euclidean spheres. Thus covariance isotropy does not require cospherical vertices. This distinction matters because the minimum-volume enclosing ellipsoid can still be non-spherical.

## Assumptions and scope
All statements concern the standard ambient Euclidean scalar product in the displayed coordinates, the **uniform counting measure on the distinct vertices**, integer \(d\ge2\), positive \(\ell\), and strict \(0<a<\ell\). Rescaling \(\ell,a\) simultaneously does not change the spectral ratio or the unique dimensionless isotropic cant. The two degenerate endpoints are excluded: at \(a=0\), previously distinct labeled vertices coalesce, so the limiting vertex-counting law is not the uniform law on the cube; at \(a=\ell\), the body collapses in dimension. No covariance assertion about uniform interior volume is made.

## Proof
**1. Complete vertex enumeration.** Put \(\delta=\ell-a\). For every nonempty \(S\subseteq[d]\), define
\[
(v_S)_i=\begin{cases}\ell/2,&i\in S,\\ a-\ell/2,&i\notin S.\end{cases}
\]
The exact distinct vertex set is
\[
\boxed{V=\{v_S,-v_S:\varnothing\ne S\subseteq[d]\}},\qquad |V|=2(2^d-1).
\]
Here is a direct verification, independently of the source vertex labeling. If a point has no active coordinate constraint \(|z_i|=\ell/2\), it can move a little in both directions along \(\mathbf1\), so it is not extreme. By central symmetry, any extreme point may be assumed to have some \(z_i=\ell/2\). Then every coordinate belongs to the interval \([a-\ell/2,\ell/2]\) of length \(\delta\). An interior coordinate can move slightly in both directions while preserving all constraints: its difference from any other coordinate is strictly smaller than \(\delta\). Therefore every coordinate is one of the interval endpoints, with at least one coordinate at the upper endpoint. Conversely each such \(v_S\) is extreme: the \(|S|\) active upper-coordinate equalities pin its upper entries, and the \(d-|S|\) difference equalities with a chosen upper entry pin its lower entries. These are \(d\) independent linear equations. The negatives give the remaining extremes, and the two lists do not overlap when \(0<a<\ell\).

**2. Second moments.** A uniform sample from \(V\) is obtained by taking a uniform nonempty subset \(S\subseteq[d]\) and an independent uniform sign \(\varepsilon\in\{-1,1\}\), setting \(X=\varepsilon v_S\). Consequently \(\mathbb EX=0\). With \(N=2^d-1\),
\[
\Pr(i\in S)=\frac{2^{d-1}}N,\qquad \Pr(i,j\in S)=\frac{2^{d-2}}N\quad(i\ne j).
\]
Writing \(b=a-\ell/2\) and \(\delta=\ell-a\), so that \((v_S)_i=b+\delta\mathbf1_{i\in S}\), a direct calculation yields
\[
\Sigma_{ii}=\frac{2^{d-1}\ell^2/4+(2^{d-1}-1)b^2}{N}
\]
and for distinct \(i,j\),
\[
\boxed{\Sigma_{ij}=\frac{2^{d-2}a^2-b^2}{N}
=\frac{(2^d-4)a^2+4a\ell-\ell^2}{4N}.}
\]
Hence \(\Sigma_{ii}-\Sigma_{ij}=2^{d-2}(\ell-a)^2/N>0\). As \(\Sigma\) has constant diagonal and constant off-diagonal, the transverse eigenvalue is exactly that difference, and the axial eigenvalue is \(\lambda_\perp+d\Sigma_{ij}\). This proves the two spectral formulas.

**3. Sharp isotropy and condition number.** Divide the off-diagonal formula by \(\lambda_\perp\), replace \(a/(\ell-a)\) by \(x\), and simplify:
\[
\boxed{R_d(x):=\frac{\lambda_\parallel}{\lambda_\perp}=1+\frac d{2^d}\left((2^d-1)x^2+2x-1\right).}
\]
For \(x>0\),
\[
R'_d(x)=\frac{2d}{2^d}\left((2^d-1)x+1\right)>0.
\]
The endpoint limits are \(R_d(0+)=1-d/2^d>0\) and \(R_d(x)\to\infty\) as \(x\to\infty\). Thus both eigenvalues are positive, and the ratio crosses \(1\) exactly once. Solving \((2^d-1)x^2+2x-1=0\) for its positive root gives
\[
x_*=\frac{2^{d/2}-1}{2^d-1}=\frac1{2^{d/2}+1},\qquad
\frac{a_*}\ell=\frac{x_*}{1+x_*}=\frac1{2^{d/2}+2}.
\]
For \(x<x_*\), \(R_d(x)<1\), whereas for \(x>x_*\), \(R_d(x)>1\). Therefore \(\kappa_d(x)=\max\{R_d(x),R_d(x)^{-1}\}\) decreases strictly to \(1\) and increases strictly afterwards. Its asymptotic minimizer is \(a_*/\ell\sim2^{-d/2}\).

**4. Noncospherical tight frame.** At \(a=a_*\), the equality of eigenvalues means \(\Sigma=\lambda_\perp I\). Equivalently, the equally weighted vectors in \(V\) satisfy
\[
\sum_{v\in V}vv^\mathsf T=(2^{d+1}-2)\lambda_\perp I,
\]
which is the finite tight-frame identity. However, for \(|S|=k\),
\[
\|v_S\|^2=\frac{k\ell^2}{4}+(d-k)(a-\ell/2)^2,
\]
and the successive squared radii differ by \(a(\ell-a)>0\). There are therefore exactly \(d\) distinct radial shells for every permitted cant, including \(a_*\). This proves the final assertion.

## Verification
The accompanying self-contained `verify.py` enumerates all distinct vertices from the halfspaces for \(2\le d\le8\) and five rational cants per dimension. Using exact rational arithmetic, it reconstructs every covariance entry, the axial and transverse eigenvalues, the spectral ratio, the defining inequalities, and the strict radial-shell ordering. It also verifies exact isotropy for the six even dimensions \(d=2,4,6,8,10,12\), and checks the quadratic-irrational root numerically at 70-digit precision for five odd dimensions. It prints `ISOCANTED_VERTEX_INERTIA_CHECKS_PASSED` after successful tests. Finite checks corroborate but do not establish the all-dimensional theorem; the symbolic calculation above is the proof.

## Relationship to prior work
The original 2020 paper of de la Puente and Clavería introduces isocanted alcoved polytopes, identifies their cubical zonotope structure and subset-indexed vertices, and classifies their face numbers. Their 2024 paper computes the volume and Mahler product, and the 2025 follow-up describes the centered inequalities, vertex labels, tilings, and lower-dimensional face volumes. These facts are prior work, not part of the novelty claim.

Two related published geometric studies determine respectively the Euclidean radial shells/inball and the exact John and Löwner ellipsoids of the same family. The first already gives the radial-shell classification reproduced here only to show that isotropy is noncospherical. The second determines optimal containing ellipsoids rather than the covariance ellipsoid of the uniform vertex-counting measure. Another study determines the *uniform-volume* covariance and its affine-invariant isotropic-constant optimum for this family; that measure is distinct from the uniform counting measure on vertices and its optimizing cant is different. Neither statement implies the precise vertex-inertia isotropy threshold without an additional second-moment calculation.

The contribution here is the **complete exact vertex-uniform covariance spectrum**, the **unique tight-frame cant in every dimension**, and the strict spectral-condition-number classification. Targeted searches of the same-object primary full texts and semantic mathematical records did not identify an earlier equivalent theorem; absence from searches does not establish universal priority.

## Limitations
This is specific to symmetric, equal-cant isocanted cubes with the standard Euclidean metric. The result does not identify any optimal cant for uniform-volume isotropic constants, ellipsoid volume, surface area, face geometry, or statistical performance under arbitrary sampling. Covariance isotropy is not equivalent to spherical uniformity because the vertices remain noncospherical. Historical priority is provisional, especially for equivalent calculations expressed as second moments of labeled zonotope vertices or frame-potential minimization. The finite checker is not an infinite proof.

## References
1. M. J. de la Puente and P. L. Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858, first posted 2020-09-29; Applications of Mathematics 65 (2020), 703–726, DOI 10.21136/AM.2020.0373-19. https://arxiv.org/abs/2009.13858
2. M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565, first posted 2024-06-03; DOI 10.1080/03081087.2024.2368240. https://arxiv.org/abs/2406.01565
3. M. J. de la Puente, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this \(d\)-dimensional tile*, Extracta Mathematicae 40 (2025), 1–26, DOI 10.17398/2605-5686.40.1.1. https://doi.org/10.17398/2605-5686.40.1.1
4. *Isocanted cubes have exact vertex shells and a Chebyshev-center phase transition*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-isocanted-cubes-have-exact-vertex-shells-and-a-chebyshev-center--12c715aa8342
5. *Parity-sharp Löwner contact transitions and pole avoidance for isocanted cubes*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-sharp-l-wner-contact-transitions-and-pole-avoidance-for-i--c0498570052b
