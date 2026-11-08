# Isotropic optimization of the top-coordinate norm polytopes

## Finding

For every integer \(d\ge2\) and every real \(1\le k\le d\), define the full-dimensional centrally symmetric polytope
\[
B_d(k)=\operatorname{conv}\big(B_1^d\cup k^{-1}B_\infty^d\big),
\]
where \(B_1^d=\{x:\sum_{i=1}^d|x_i|\le1\}\) and \(B_\infty^d=[-1,1]^d\). Define its squared isotropic constant by
\[
L(K)^2=\frac{(\det\operatorname{Cov}(X_K))^{1/d}}{\operatorname{Vol}_d(K)^{2/d}},\qquad X_K\sim\operatorname{Unif}(K).
\]
Write \(m=\lfloor k\rfloor\), \(n=d-m\) (also at the endpoint \(k=d\)). Then the exact all-dimensional formula is
\[
\boxed{L(B_d(k))^2=\frac{(m!\,k^n)^{2/d}}{4d(d+1)(d+2)}\left(2m+\frac{2mn}{k}+\frac{n(n+1)(d+2m+2)}{3k^2}\right).}
\]

The global minimizing parameters in every fixed dimension belong to an explicitly computable set containing **at most two points**. Set
\[
 a_d=\frac{-d+\sqrt{3d^2+6d+4}}2,\quad
 b_d=\frac{-d-3+\sqrt{3d^2+6d+1}}2,
\]
\[
 \mathcal M_d=\{m\in\{1,\ldots,d-1\}:b_d<m<a_d\},
\quad
 r_{d,m}=\frac{-(d-2m)+\sqrt{(d-2m)^2+\frac83(d-m+1)(d+2m+2)}}4.
\]
The set \(\mathcal M_d\) is nonempty and has one or two consecutive integers. **Every global minimizing parameter** is one of \(\{r_{d,m}:m\in\mathcal M_d\}\), and the global minimum is obtained by evaluating the displayed exact isotropic formula at those at-most-two points and choosing the smaller value (including both in the event of equality). There are no further local minima. For example, the global minimizers are \(\sqrt2\) in dimension two, \(1.63745776\ldots\) in dimension three, \(\sqrt5\) in dimension four, and \(2.46952938\ldots\) in dimension five.

Moreover, with \(\alpha_0=(\sqrt3-1)/2\), every sequence of global minimizers \(k_d\) satisfies
\[
\boxed{\frac{k_d}{d}\longrightarrow\alpha_0,\qquad
 \min_{1\le k\le d}L(B_d(k))^2\longrightarrow\frac{e^{1-\sqrt3}}8=0.0601152125253\ldots.}
\]
This is smaller than both limiting endpoint values \(L(B_d(1))^2=1/12\) and \(\lim_{d\to\infty}L(B_d(d))^2=1/(2e^2)\).

## Assumptions and scope

The dimension is an integer at least two. The parameter is any real number in the *closed* interval \([1,d]\), including every integer transition. Volume is ordinary Euclidean \(d\)-dimensional Lebesgue volume, and covariance is taken for the uniform interior probability distribution. All claims concern the **primal convex-hull family** \(B_d(k)\), not its polar \(kB_1^d\cap B_\infty^d\). The full exact formula applies in every dimension, while the asymptotic limit takes dimension to infinity after selecting a minimizing parameter.

## Proof

**1. Ordered-coordinate simplex and moments.** Denote the ordered absolute coordinate magnitudes by \(x_{(1)}\ge\cdots\ge x_{(d)}\ge0\). The gauge of the convex hull above is the top-coordinate norm
\[
\|x\|_{(k)}=\min_{t\ge0}\left(kt+\sum_{i=1}^d(|x_i|-t)_+\right)
=\sum_{i=1}^m x_{(i)}+(k-m)x_{(m+1)}
\]
when \(k<d\); at \(k=d\), it is the ordinary \(\ell_1\)-norm. This follows by minimizing the infimal-convolution gauge \(\inf_{u+v=x}(\|u\|_1+k\|v\|_\infty)\) coordinate by coordinate at fixed \(t=\|v\|_\infty\). Set \(x_{(d+1)}=0\) and \(y_i=x_{(i)}-x_{(i+1)}\). Then
\[
\|x\|_{(k)}=\sum_{i=1}^d c_i y_i,\qquad c_i=\min\{i,k\}.
\]
Thus in each of the \(2^d d!\) sign-and-order chambers, the linear change \(z_i=c_i y_i\) identifies the body with the standard simplex \(z_i\ge0\), \(\sum_i z_i\le1\), with constant Jacobian \((\prod_i c_i)^{-1}\). In particular,
\[
\operatorname{Vol}_d(B_d(k))=\frac{2^d}{\prod_{i=1}^d c_i}
=\frac{2^d}{m!\,k^{d-m}}.
\]
For a uniform point, the ordered absolute coordinates therefore admit the exact distributional representation
\[
|X|_{(j)}\;\stackrel{\rm law}=\;\sum_{i=j}^d\frac{Z_i}{c_i},
\quad (Z_1,\ldots,Z_d,Z_{d+1})\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
Independent uniform signs and a uniform random permutation recover the original unordered coordinates. This classical weighted-simplex principle also provides every polynomial moment by expansion, using
\[
 \mathbb E\prod_{i=1}^d Z_i^{h_i}=\frac{d!\prod_{i=1}^d h_i!}{(d+\sum_i h_i)!}
\]
for nonnegative integer exponents. We use this representation as a proof technique, not as a separate novelty claim; see the probabilistic methods in the references.

**2. Exact second moment and isotropic constant.** Permutation and sign symmetry imply \(\operatorname{Cov}(X)=\sigma_d(k)^2 I_d\), with
\[
\sigma_d(k)^2=\frac{1}{d}\,\mathbb E\|X\|_2^2=\frac{H}{d(d+1)(d+2)},\quad
H=\sum_{i,j=1}^d\frac{\min(i,j)}{c_ic_j}+\sum_{i=1}^d\frac{i}{c_i^2}.
\]
Indeed, \(\mathbb E Z_i^2=2/((d+1)(d+2))\) and \(\mathbb E Z_iZ_j=1/((d+1)(d+2))\) for \(i\ne j\). With \(c_i=i\) for \(i\le m\), \(c_i=k\) for \(i>m\), the low-index terms sum to \(2m\), the cross terms to \(2mn/k\), and the high-index terms to \(n(n+1)(d+2m+2)/(3k^2)\). Dividing \(\sigma_d(k)^2\) by the volume to the power \(2/d\) yields the claimed exact formula.

**3. Complete finite-dimensional candidate theorem.** Fix a chamber \(m<k<m+1\), where \(1\le m\le d-1\) and \(n=d-m\). Up to a positive constant independent of \(k\), the displayed isotropic constant equals
\[
 k^{-2m/d}P_{d,m}(k),\qquad
 P_{d,m}(k)=2mk^2+2mnk+\frac{n(n+1)(d+2m+2)}3.
\]
Its derivative has exactly the sign of
\[
 q_{d,m}(k)=2k^2+(d-2m)k-\frac{(d-m+1)(d+2m+2)}3,
\]
because \(dkP'_{d,m}-2mP_{d,m}=2mnq_{d,m}\). The quadratic is strictly increasing for \(k\ge m\), so each chamber has at most one critical point, necessarily a strict minimum. Its positive root is \(r_{d,m}\), and it lies strictly inside its chamber exactly when \(b_d<m<a_d\), by evaluating \(q_{d,m}(m)\) and \(q_{d,m}(m+1)\).

At an internal integer \(k=m\), the sign-determining quadratics obey
\[
q_{d,m}(m)-q_{d,m-1}(m)=-\frac{d+2m+2}{3}<0.
\]
Hence the left derivative cannot be negative while the right derivative is positive: no internal integer can be a local minimum. At \(k=1\) the right derivative is negative; at \(k=d\) the left derivative is positive. The function is continuous across all integers, so every global minimizer is one of the interior critical points. Finally,
\[
 a_d-b_d=\frac32+\frac{3}{2\big(\sqrt{3d^2+6d+4}+\sqrt{3d^2+6d+1}\big)}<2
\]
for all \(d\ge2\), so at most two consecutive integer indices qualify. Existence follows from compactness and exclusion of endpoint and integer minima.

**4. Sharp high-dimensional optimum.** Because any admissible index satisfies \(b_d<m<a_d\) and its parameter lies in \((m,m+1)\), every global minimizing sequence satisfies
\[
 \frac{k_d}{d}\longrightarrow\frac{\sqrt3-1}{2}.
\]
More generally, for every fixed \(0<\alpha\le1\), if \(k_d/d\to\alpha\), the exact second-moment formula and Stirling's formula give
\[
L(B_d(k_d))^2\longrightarrow
F(\alpha)=\frac{e^{-2\alpha}}{12}(1+3\alpha^2+2\alpha^3).
\]
Its derivative is
\[
 F'(\alpha)=-\frac{e^{-2\alpha}}6(\alpha-1)(2\alpha^2+2\alpha-1).
\]
Therefore \(F\) decreases strictly until \(\alpha_0=(\sqrt3-1)/2\), increases strictly afterwards on \((\alpha_0,1)\), and \(1+3\alpha_0^2+2\alpha_0^3=3/2\). This proves the stated global limiting minimum. The endpoint values are verified directly from the cube and cross-polytope formulas.

## Verification

The accompanying executable checker `check.py` implements exact-rational gap identities in 91 finite parameter chambers, exact symbolic differentiation and asymptotic simplification, the at-most-two local-candidate rule for 69 dimensions, and an **independent convex-hull triangulation** for 12 rational-parameter examples in dimensions two through four (526 facet simplices). Each triangulated simplex is integrated with exact rational determinants and second moments; Qhull is used only to choose facet simplices. In the tested examples, these independent Euclidean integrals exactly match the ordered-gap volume and radial second moments. Completion marker: `TOP_K_NORM_ISOTROPY_CHECKS_PASSED`. These finite computations are corroboration; the argument above establishes the all-dimensional results.

To reproduce with Python and installed NumPy, SciPy, and SymPy, run `python check.py` in the directory containing this document and its checker. No external data files are needed.

## Relationship to prior work

Deza, Hiriart-Urruty and Pournin (arXiv:2011.05607, first submitted 2020-11-11) defined the same norm-ball interpolation and proved the general volume formula, facet descriptions, surface areas, and a Mahler-product identity. **Those results are prior work, not discoveries here.** Gaudioso and Hiriart-Urruty later examined top-coordinate norm balls and their face structure. Kabluchko, Prochno and Sonnleitner (arXiv:2303.04728) proved a closely related Dirichlet/exponential representation for Lorentz balls with fixed power weights. The chamber method in this note is an elementary adaptation of that established method. The new assertion assessed here is the **exact squared isotropic-constant formula, complete two-candidate finite-dimensional minimization, and sharp optimally tuned high-dimensional limit** for this distinct family with a moving top-coordinate cutoff. The literature inspected did not state these optimization results.

A separate result on the polar family \(kB_1^d\cap B_\infty^d\) does not imply the present primal-body covariance determinant or its minimizing parameter: polarity does not preserve the normalized covariance determinant, and the two asymptotic optimizing fractions differ. General results about Hanner polytopes do not cover these generic intermediate norm balls. A remaining historical-priority risk is that a more general theorem for weighted ordered-coordinate balls already implies the full optimization without naming this parametrization.

## Limitations

The finite-dimensional theorem characterizes the global minimizer by **at most two explicit algebraic candidates**, not by one branch choice valid uniformly in dimension, and it does not assert uniqueness when the two values happen to coincide. The high-dimensional limit does not specify finite-dimensional error rates or fluctuations of the uniform point distribution. The Dirichlet representation and original volume formula are known methodological inputs; originality is limited to the isotropic optimization. No independent external validation, certification, or exhaustive historical priority is claimed.

## References

1. A. Deza, J.-B. Hiriart-Urruty, and L. Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607 (submitted 2020-11-11), later Contributions to Discrete Mathematics 16 (2021), 125–138. https://arxiv.org/abs/2011.05607
2. M. Gaudioso and J.-B. Hiriart-Urruty, *Deforming the \(\ell_1\) norm into the \(\ell_\infty\) norm via polyhedral norms: A pedestrian approach*, SIAM Review, DOI 10.1137/21M1391481. https://doi.org/10.1137/21M1391481
3. Z. Kabluchko, J. Prochno, and M. Sonnleitner, *A probabilistic approach to Lorentz balls*, arXiv:2303.04728 (submitted 2023-03-08), Theorem A and proof. https://arxiv.org/abs/2303.04728
4. A. Doležalová and J. Vybíral, *On the volume of unit balls of finite-dimensional Lorentz spaces*, arXiv:1906.04997 (submitted 2019-06-12). https://arxiv.org/abs/1906.04997
