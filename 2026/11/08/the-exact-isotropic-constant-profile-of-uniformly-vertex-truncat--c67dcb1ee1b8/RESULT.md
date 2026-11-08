# The exact isotropic-constant profile of uniformly vertex-truncated simplices

## Finding

For any nondegenerate Euclidean simplex \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\) of dimension \(d\ge2\), every point has unique barycentric coordinates \(\lambda_0,\ldots,\lambda_d\). Set
\[
K_{d,t}(S)=\left\{\sum_{i=0}^{d}\lambda_i v_i:\lambda_i\ge0,\ \sum_i\lambda_i=1,\ \lambda_i\le1-t\text{ for all }i\right\},\quad 0\le t\le\tfrac12.
\]
Here \(t\) is the fractional depth of identical barycentric vertex truncations; the endpoint \(t=1/2\) is the rectified simplex. Write \(L(K)^{2d}=\det(\operatorname{Cov}(X))/\operatorname{Vol}_d(K)^2\) for the affine-invariant isotropic constant of uniform intrinsic \(d\)-volume. Let
\[
B_d(t)=(d+1)t^d,\qquad A_d(t)=t^2+(d+2)(1-t)^2.
\]
Then, independently of the shape of the original simplex,
\[
\boxed{\frac{L(K_{d,t}(S))^2}{L(S)^2}=
\frac{1-B_d(t)A_d(t)}{(1-B_d(t))^{1+2/d}}.}
\]
For every \(d\ge3\), this ratio is strictly decreasing on \([0,1/2]\); hence among this entire truncation family, \(S\) uniquely maximizes and the rectification uniquely minimizes the isotropic constant. In dimension \(d=2\) the ratio instead decreases strictly on \([0,1/3]\), increases strictly on \([1/3,1/2]\), has unique minimum \(5/6\) at \(t=1/3\), and returns to \(1\) at \(t=1/2\). For the regular triangle the minimizer is the regular hexagon. The three-dimensional rectified endpoint has exact ratio \(2^{-1/3}\). Finally,
\[
\lim_{d\to\infty}\frac{2^{d+2}}{d^2}\left(1-\frac{L(K_{d,1/2}(S))^2}{L(S)^2}\right)=1.
\]
(The ratio and limit do not depend on the choice of \(S\).)

## Assumptions and scope

Dimensions are integers \(d\ge2\), simplex vertices are affinely independent, and \(t\in[0,1/2]\). The metric volume for the reference simplex is intrinsic Hausdorff volume in the affine hyperplane, not the ambient \((d+1)\)-dimensional Lebesgue measure. For arbitrary \(S\), the statement follows from affine invariance because barycentric truncation commutes with invertible affine maps. Strict monotonicity is with respect to the stated parameter \(t\), not an arbitrary truncation of unequal depths. No statement is made for \(t>1/2\), when removed caps overlap.

## Proof

**1. Reference simplex and cap decomposition.** By affine invariance take \(\Delta_d=\operatorname{conv}\{e_0,\ldots,e_d\}\) in \(H=\{x\in\mathbb R^{d+1}:\sum_i x_i=1\}\). Its intrinsic volume is \(V_0=\sqrt{d+1}/d!\), centroid \(\mu=\mathbf1/(d+1)\), and uniform second radial moment
\[
J_0=\mathbb E_{\Delta_d}\|X-\mu\|_2^2=\frac{d}{(d+1)(d+2)}.
\]
This follows from the Dirichlet\((1,\ldots,1)\) barycentric distribution: \(\operatorname{Var}(X_i)=d/((d+1)^2(d+2))\). For \(t\le1/2\), the \(d+1\) discarded caps \(C_i(t)=\{x\in\Delta_d:x_i>1-t\}\) have disjoint interiors and each is the homothetic image \(e_i+t(\Delta_d-e_i)\). Thus each cap has fraction \(t^d\) of the volume, the retained volume is
\[
V_t=V_0(1-B_d(t)),\qquad B_d(t)=(d+1)t^d<1,
\]
and the remaining centroid stays \(\mu\) by permutation symmetry.

**2. Exact inertia and affine normalization.** The cap barycenter is \((1-t)e_i+t\mu\). Its squared distance from \(\mu\) is \((1-t)^2d/(d+1)\). Homothety reduces the within-cap covariance by \(t^2\). Therefore its mean squared radius about \(\mu\) is
\[
t^2J_0+(1-t)^2\frac d{d+1}=J_0 A_d(t),\qquad A_d(t)=t^2+(d+2)(1-t)^2.
\]
Subtracting cap integrals gives
\[
J_t:=\mathbb E_{K_{d,t}(\Delta_d)}\|X-\mu\|_2^2
=J_0\frac{1-B_d(t)A_d(t)}{1-B_d(t)}.
\]
Permutation invariance makes the covariance operator scalar on the tangent subspace \(H_0=\{z:\sum_i z_i=0\}\): a commuting matrix has a common diagonal and common off-diagonal, and the vector \(\mathbf1\) is in its nullspace. Hence \(\operatorname{Cov}(X)|_{H_0}=(J_t/d)I_{H_0}\), giving \(\det\operatorname{Cov}(X)=(J_t/d)^d\) in any orthonormal basis of \(H_0\). Inserting \(V_t\) in the definition of \(L\) proves the displayed ratio and yields
\[
L(\Delta_d)^2=\frac{(d!)^{2/d}}{(d+1)^{(d+1)/d}(d+2)}.
\]
It also establishes positivity of the expression at the endpoints, since it is the variance of a full-dimensional body.

**3. Complete derivative classification.** Let \(F_d(t)=L(K_{d,t}(S))^2/L(S)^2\). Direct differentiation on \((0,1/2)\) gives
\[
F_d'(t)=\frac{(d+2)B_d(t)}{t(1-B_d(t))^{2+2/d}}\,S_d(t),
\]
where
\[
S_d(t)=1-d+2(d+1)t-(d+3)t^2-2(d+1)t^d(1-t).
\]
The prefactor is positive. For \(d=2\),
\[
S_2(t)=(t-1)(2t-1)(3t-1),
\]
so the derivative changes from negative to positive only at \(t=1/3\). Substitution gives \(F_2(1/3)=5/6\) and \(F_2(1/2)=F_2(0)=1\). For \(d=3\),
\[
S_3(t)=2(t-1)(t+1)(2t-1)^2<0\quad(0<t<1/2).
\]
For \(d=4\),
\[
S_4(t)=(t-1)(10t^4-7t+3)<0.
\]
Indeed \(p(t)=10t^4-7t+3\) decreases on \([0,1/2]\) because \(p'(t)=40t^3-7\le-2\), and \(p(1/2)=1/8>0\). For all \(d\ge5\), write \(S_d(t)=P_d(t)-2(d+1)t^d(1-t)\), where \(P_d(t)=1-d+2(d+1)t-(d+3)t^2\). Since \(P_d'(t)=2(d+1)-2(d+3)t\ge d-1>0\) for \(0\le t\le1/2\), we have \(P_d(t)\le P_d(1/2)=(5-d)/4\le0\). The subtracted term is strictly positive on \((0,1/2)\). Therefore \(F_d\) strictly decreases in every dimension \(d\ge3\). Continuity extends the extremal classification to both endpoints.

**4. Exact endpoint and asymptotic.** For \(t=1/2\),
\[
F_d(1/2)=\frac{1-(d+1)(d+3)/2^{d+2}}{(1-(d+1)/2^d)^{1+2/d}}.
\]
For \(d=3\) this is \(2^{-1/3}\). Put \(b_d=(d+1)/2^d\) and \(a_d=(d+3)/4\). Expanding \((1-b_d)^{-1-2/d}\) as \(d\to\infty\) yields
\[
1-F_d(1/2)=b_d\left(a_d-1-\frac2d\right)+O(d^2b_d^2)
\sim\frac{d^2}{2^{d+2}},
\]
proving the claimed limit.

## Verification

The standalone script `check_truncation.py` independently constructs the truncated-simplex vertex sets and obtains simplicial boundary triangulations from convex hulls. It integrates the quadratic radial moment over coned simplicial cells with **exact rational determinants and exact rational second moments**, without using the cap-removal formula to perform the integrations. It compares exact volume and moment values against the theorem for \(d=2,3,4\) and \(t\in\{1/5,1/3,2/5,1/2\}\). It also symbolically checks the polynomial factorizations for \(d=2,3,4\). The recorded successful output is `SIMPLEX_TRUNCATION_EXACT_CHECKS_PASSED 12 330 3`. These are finite checks; the proof in Section 3 establishes all integer dimensions.

## Relationship to prior work

Kipp, *Isotropic constants and Platonic solids* (first arXiv version, July 1, 2024) studies local maximizing polytopes and various zonotopes, giving structural conditions rather than an exact isotropic-constant profile for simplex vertex truncations. Baci–Kabluchko–Prochno–Sonnleitner–Thäle, *Limit theorems for random points in a simplex* (May 11, 2020), develops asymptotic norm laws for a uniform random point in the untruncated simplex; its starting Dirichlet model concerns the reference distribution but does not supply the conditional cap-removal profile or its monotonicity. Rademacher's earlier simplicial-maximizer theorem addresses a different global optimality question. The special rectified tetrahedron is a regular octahedron with a known isotropic constant; that endpoint cannot itself establish the complete dimension-dependent interpolation or the planar reversal. Searches in related terminology, including clipped simplices and truncated Dirichlet laws, did not identify a theorem subsuming this statement; priority under alternative terminology remains open to external literature verification.

## Limitations

The analysis is restricted to simultaneous equal-depth barycentric truncations up to the first edge-midpoint transition. It does not cover nonuniform cap depths, later truncation phases, or other polytope families. The monotonicity is a relative, affine-invariant comparison along this one-parameter family; it does not prove that a rectified simplex is an absolute minimizer among all convex bodies or that a simplex is a global maximizer. The finite checker provides reproducibility, not infinite-dimensional certification. Independent mathematical audit and comprehensive historical priority verification have not been performed.

## References

- C. Kipp, *Isotropic constants and Platonic solids*, arXiv:2407.01353v1, July 1, 2024, https://arxiv.org/abs/2407.01353.
- A. Baci, Z. Kabluchko, J. Prochno, M. Sonnleitner, and C. Thäle, *Limit theorems for random points in a simplex*, arXiv:2005.04911v1, May 11, 2020, https://arxiv.org/abs/2005.04911.
- L. Rademacher, *A simplicial polytope that maximizes the isotropic constant must be a simplex*, arXiv:1404.5662, April 22, 2014, https://arxiv.org/abs/1404.5662.
