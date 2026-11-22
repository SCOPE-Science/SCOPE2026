# Conditional-volume moments of centrally containing random simplices and the skewness of spherical tetrahedra

## Finding

Let \(d\ge2\), and let \(X_0,\ldots,X_d\) be independent, centrally symmetric random vectors in \(\mathbb R^d\), almost surely in linear general position. Write \(E=\{0\in\operatorname{int}\operatorname{conv}(X_0,\ldots,X_d)\}\), let \(V\) denote their Euclidean simplex volume, and put
\[
A_i=\left|\det(X_0,\ldots,\widehat X_i,\ldots,X_d)\right|,\qquad S=\sum_{i=0}^d A_i.
\]
For the uniquely defined positive barycentric coordinates \(\Lambda_i\) of the origin on \(E\), the following **marked conditional-volume identity** holds:
\[
\boxed{\Pr(E)=2^{-d},\qquad
\mathcal L\left( d!V,(\Lambda_i)_{i=0}^d\mid E\right)
=\mathcal L\left(S,(A_i/S)_{i=0}^d\right).}
\]
This identity gives an exact, rejection-free conditional sampler and reduces conditional volume moments to mixed moments of unsigned maximal minors. Its sign-orbit mechanism is the same classical mechanism underlying Wendel's theorem; the identity itself is recorded as the starting reduction, **not independently claimed as a new method**.

For independent isotropic points \(X_i=R_iU_i\), where the \(U_i\) are independent uniform unit-sphere directions and the strictly positive \(R_i\) are independent identically distributed radii independent of those directions, define \(\mu_j=\mathbb E R^j\) and
\[
a_d=\frac{\Gamma(d/2)^d}{\sqrt\pi\,\Gamma((d+1)/2)^{d-1}},\qquad
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
Whenever the displayed moments are finite,
\[
\boxed{
\mathbb E[V\mid E]=\frac{d+1}{d!}a_d\mu_1^d,\qquad
\mathbb E[V^2\mid E]
=\frac{d+1}{d!\,d^d}\left(\mu_2^d+d^2c_d^2\mu_2^{d-1}\mu_1^2\right).}
\]
In particular, when \(d=3\) and all four points are independent and uniform on the *surface* of the unit sphere, the **first three conditional volume moments are evaluated exactly**:
\[
\boxed{
\mathbb E[V\mid E]=\frac\pi{12},\quad
\mathbb E[V^2\mid E]=\frac{13}{162},\quad
\mathbb E[V^3\mid E]=\frac{7\pi}{1152}+\frac{2}{81\pi}.}
\]
Consequently, the centered third moment of the conditional tetrahedral volume is **strictly negative**:
\[
\boxed{\mathbb E\left[\left(V-\frac\pi{12}\right)^3\mid E\right]
=\frac{12\pi^4-145\pi^2+256}{10368\pi}<0.}
\]
The nontrivial evaluated ingredient is the three-minor angular correlation \(2/(9\pi)\), which is needed for the third moment and does not follow from the individual-determinant moment formula alone.

## Assumptions and scope

Linear general position means that every \(d\)-element subfamily of the \(d+1\) vectors is linearly independent almost surely. Joint absolute continuity is a sufficient, but not necessary, condition. Central symmetry means each \(X_i\) and \(-X_i\) have the same law. Independence is assumed throughout. The event \(E\) is strict full-dimensional containment, not inclusion in a closed lower-dimensional hull. Conditional expectations and variances always refer to the Euclidean \(d\)-simplex spanned by the vectors. The isotropic specialization additionally assumes independent positive radii and uniform independent directions; \(\mu_1,\mu_2\) are taken finite for the corresponding formula. The three-dimensional third moment concerns radius exactly one. No formula is claimed for anisotropic angular laws beyond the marked identity.

## Proof

**1. Signed-minor reduction and normalization.** Let \(C_i=(-1)^i\det(X_0,\ldots,\widehat X_i,\ldots,X_d)\). Laplace expansion in the \((d+1)\)-column matrix gives \(\sum_i C_iX_i=0\). By general position every \(C_i\ne0\), and the nullspace is one-dimensional. The origin lies strictly inside the simplex precisely when all \(C_i\) have a common sign. If the vector \(X_j\) is independently sign-flipped by \(s_j\in\{-1,1\}\), then \(C_i\) changes to \((\prod_j s_j)s_i C_i\). In each sign orbit, exactly two of the \(2^{d+1}\) sign patterns have all cofactors of one sign. Since central symmetry and independence make the sign group measure preserving, \(\Pr(E)=2^{-d}\). More strongly, each \(A_i\) is invariant under every sign flip. Thus the entire vector \((A_i)\) is independent of the event \(E\). On \(E\), the unique positive null vector gives \(\Lambda_i=A_i/S\); the homogeneous augmented determinant for simplex volume satisfies \(d!V=\left|\sum_i C_i\right|=S\). This proves the joint conditional law, for all bounded measurable test functions, without a moment assumption.

**2. Mean of a spherical determinant.** For independent uniform \(U_1,\ldots,U_d\in S^{d-1}\), orthogonal Gram–Schmidt factors \(|\det(U_1,\ldots,U_d)|\) into successive projected lengths. Their beta integrals telescope to
\[
\mathbb E|\det(U_1,\ldots,U_d)|
=\frac{\Gamma(d/2)^d}{\sqrt\pi\,\Gamma((d+1)/2)^{d-1}}=a_d.
\]
Each unsigned maximal minor of the \(d+1\) points contains exactly \(d\) independent radius factors. Therefore \(\mathbb E S=(d+1)a_d\mu_1^d\), proving the first-moment formula.

**3. Diagonal and overlapping second minor moments.** Standard independent uniform-sphere second moments, \(\mathbb E(UU^\mathsf T)=I_d/d\), yield
\[
\mathbb E\det(U_1,\ldots,U_d)^2=\frac{d!}{d^d}.
\]
For two distinct maximal minors, the common \(d-1\) columns span a random hyperplane. Conditional on these columns, each remaining direction has independent absolute orthogonal component with mean \(c_d=\mathbb E|U_1|\), where \(U_1\) denotes one Cartesian coordinate of a sphere-uniform point. The common \((d-1)\)-parallelotope has expected squared volume \(d!/d^{d-1}\). Consequently
\[
\mathbb E[A_i^2]=\frac{d!}{d^d}\mu_2^d,\qquad
\mathbb E[A_iA_j]=\frac{d!}{d^{d-1}}c_d^2\mu_2^{d-1}\mu_1^2\quad(i\ne j).
\]
Expanding \(S^2\) into \(d+1\) diagonal terms and \(d(d+1)\) ordered off-diagonal terms, then dividing by \((d!)^2\), gives the second-moment formula. The same derivation shows that second moments are not generally determined by only a first radial moment.

**4. The three correlations for four spherical points.** For \(d=3\) write \(Q_i=A_i\) for each unsigned triple determinant. Since any two independent sphere directions have dot product uniform on \([-1,1]\), a cross-product length has third moment \(\mathbb E|U\times W|^3=3\pi/16\). Conditional on the cross product's direction, independent absolute axial cosines have moments \(\mathbb E|T|=1/2\), \(\mathbb ET^2=1/3\), and \(\mathbb E|T|^3=1/4\). Hence, for distinct indices,
\[
\mathbb E Q_i^3=\frac{3\pi}{64},\qquad
\mathbb E Q_i^2Q_j=\frac\pi{32}.
\]
For three distinct minors their determinant triples share exactly one original vertex. Condition on that unit vector, rotate it to the north pole and project the other three directions to the orthogonal plane. Each projected length is \(r=\sqrt{1-T^2}\), with \(\mathbb Er^2=2/3\); each of the three projected directions occurs in exactly two absolute planar determinants. Independent uniform azimuths therefore give
\[
\mathbb E Q_iQ_jQ_k=\left(\frac23\right)^3
\mathbb E\bigl[|\sin\alpha\sin\beta\sin(\alpha-\beta)|\bigr]
=\left(\frac23\right)^3\frac{3}{4\pi}=\frac{2}{9\pi}.
\]
For clarity, the angular integral is \(\pi^{-2}\int_0^\pi\int_0^\pi\sin u\sin v|\sin(u-v)|\,dv\,du=3/(4\pi)\). By exchangeability, expansion of the cube of four minors has four repeated triples, \(36\) ordered two-equal triples and \(24\) all-distinct triples. Thus
\[
\mathbb E[V^3\mid E]=\frac{4(3\pi/64)+36(\pi/32)+24(2/(9\pi))}{6^3}
=\frac{7\pi}{1152}+\frac2{81\pi}.
\]
The first two moments similarly evaluate to \(\pi/12\) and \(13/162\).

**5. Strictly negative skewness.** Substituting the three moments gives the displayed centered cubic \(f(\pi)\), where \(f(t)=(12t^4-145t^2+256)/(10368t)\). Its derivative \(f'(t)=t^2/288-145/10368-2/(81t^2)\) is strictly increasing for \(t>0\) and already positive at \(t=223/71\). The classical rational bounds \(223/71<\pi<22/7\) then imply \(f(\pi)<f(22/7)=-1091/6519744<0\). This is a strict algebraic sign proof, not a floating-point inference. \(\square\)

## Verification

The accompanying `checks/verify.py` uses exact symbolic arithmetic to confirm the three moment expansions and the strict rational sign bound, then conducts independent fixed-seed numerical checks of the spherical minor correlations and of the sign-orbit distributional identity. It checks conditional volume and conditional barycentric coordinates directly on accepted sign configurations, as well as first and second moments in dimensions two through four. The executable and its dependency manifest are included with this result. The finite tests are diagnostics: the proof above establishes the identities for all admissible dimensions and distributions.

## Relationship to prior work

Wendel's 1962 theorem proves the origin-containment probability using symmetry of independent random points. The complete signed-minor reduction used here is a direct sharpening of that same sign argument, and it is not independently promoted as a new probabilistic principle. Cover and Efron (1967) study convex-cone absorption and face statistics. The Ruben–Miles (1980) canonical decomposition concerns affine-hull geometry of isotropic point sets and does not state the full-dimensional origin-conditioned volume statistic. Miles (1971) and later general spherical-simplex volume-moment formulas evaluate *unconditional* moments. Those do not directly give the joint minor correlations needed for **origin-conditioned** volume moments. Previously published conditional Gaussian barycentric laws address a related but nonidentical Gaussian model and weight distribution, not the explicit surface-spherical third volume moment and sign of its centered skewness. Other conditional sphere-tetrahedron results treat the very-small-volume tail or shallow central facets, not the first three full conditional moments. The proposed contribution is therefore the evaluated conditional-volume moment hierarchy, especially the three-minor angular contraction and the exact negative-skewness conclusion. The comparison cannot establish exhaustive historical priority.

## Limitations

The conditional representation requires independent centrally symmetric vectors in linear general position. The dimension-wide moment formulas require rotationally invariant directions and independent identically distributed positive radii; radial moment assumptions cannot be omitted. The exact third moment and skewness sign are only proved for four independent unit-sphere vertices in three dimensions. Higher conditional moments and the full conditional CDF are not evaluated. Original full text of Miles (1971) was not accessible, so any unpublished or overlooked conditional formulation remains a priority risk. No independent mathematical audit has been performed.

## References

1. J. G. Wendel, *A Problem in Geometric Probability*, *Mathematica Scandinavica* **11** (1962), 109–112, doi:10.7146/math.scand.a-10655, https://doi.org/10.7146/math.scand.a-10655.
2. T. M. Cover and B. Efron, *Geometrical Probability and Random Points on a Hypersphere*, *Annals of Mathematical Statistics* **38** (1967), 213–220, https://isl.stanford.edu/~cover/papers/paper6.pdf.
3. R. E. Miles, *Isotropic Random Simplices*, *Advances in Applied Probability* **3** (1971), 353–382, doi:10.2307/1426176.
4. J. Grote, Z. Kabluchko and C. Thäle, *Limit theorems for random simplices in high dimensions*, initial preprint arXiv:1708.00471 (2017), https://arxiv.org/abs/1708.00471; published in *ALEA* **16** (2019), 141–177.
5. E. W. Weisstein, *Sphere Tetrahedron Picking*, MathWorld, https://mathworld.wolfram.com/SphereTetrahedronPicking.html, for unconditioned spherical tetrahedron moments.
6. H. Ruben and R. E. Miles, *A canonical decomposition of the probability measure of sets of isotropic random points in Rn*, *Journal of Multivariate Analysis* **10** (1980), 1–18, doi:10.1016/0047-259X(80)90077-9.
