# Sharp variance and skewness corrections for the area of random high-dimensional spherical triangles

## Finding
Let \(d\ge3\), and sample three independent surface-uniform points on \(S^{d-1}\). Let \(A_d\) be the intrinsic area of their shorter-geodesic spherical triangle in the canonical great \(2\)-sphere of their linear span. Then
\[
\mathbb E A_d=\frac\pi2,\qquad
\operatorname{Var}(A_d)=\frac3d+\frac6{d^2}+O(d^{-5/2}),
\]
\[
\mathbb E[(A_d-\pi/2)^3]=\frac{12}{d^2}+O(d^{-5/2}),\qquad
\sqrt{\frac d3}(A_d-\pi/2)\ \xrightarrow{\mathrm{law}}\ N(0,1).
\]
In particular the standardized skewness is \(4/\sqrt{3d}+O(d^{-1})\). The new quantitative statements are the second-order variance coefficient and the leading third centered moment (not the classical mean or the elementary Gaussian limit alone).

## Assumptions and scope
The sphere has Euclidean ambient dimension \(d\), not intrinsic dimension \(d\). Except on an event of probability zero, three independent points \(U,V,W\) span a three-dimensional linear subspace. Its intersection with \(S^{d-1}\) is a genuine unit \(2\)-sphere, in which the three shorter great-circle arcs form a unique convex spherical triangle of area \(A_d\in(0,2\pi)\). The area is its ordinary two-dimensional spherical excess; it is **not** the \((d-1)\)-dimensional surface measure of a region on the ambient sphere and is not the area of a straight-edge Euclidean triangle. All limits take \(d\to\infty\) over integers; the implied constants are absolute. No independence of the triangle's three angles is assumed.

## Proof
**1. Exact angle and mean formula.** Define \(x=U\cdot V\), \(y=U\cdot W\), and \(z=V\cdot W\). The spherical angle at \(U\) is
\[
\alpha_U=\arccos\!\left(\frac{z-xy}{\sqrt{(1-x^2)(1-y^2)}}\right),
\]
with its two cyclic counterparts. Consequently \(A_d=\alpha_U+\alpha_V+\alpha_W-\pi\). Conditional on \(U\), the unit tangent directions toward \(V\) and \(W\) are independent uniform points on \(S^{d-2}\); their angle has the same distribution as its supplement. Thus each vertex angle has mean \(\pi/2\), and the exact identity \(\mathbb E A_d=\pi/2\) follows for every \(d\ge3\).

**2. A controlled third-order expansion.** Put \(L=-(x+y+z)\), \(Q=xy+xz+yz\), and
\[
C=-\tfrac12(x^2y+x^2z+y^2x+y^2z+z^2x+z^2y)-\tfrac16(x^3+y^3+z^3).
\]
Taylor's theorem applied to the preceding three exact angles shows that, on \(\max(|x|,|y|,|z|)\le 1/8\),
\[
A_d-\frac\pi2=L+Q+C+R,\qquad
|R|\le K(|x|+|y|+|z|)^4,
\]
where \(K\) is independent of \(d\). For example, one angle has expansion
\[
\alpha_U-\frac\pi2=-z+xy-\frac z2(x^2+y^2)-\frac{z^3}{6}+O((|x|+|y|+|z|)^4).
\]
The scalar product of independent sphere-uniform vectors satisfies \(\mathbb E|x|^k=O_k(d^{-k/2})\) for every fixed positive integer \(k\), as follows from its beta density. By Hölder, the same bound holds for all fixed-degree products of \(x,y,z\). Moreover \(\Pr(\max(|x|,|y|,|z|)>1/8)\le 6e^{-c d}\) for an absolute \(c>0\) (with a harmless adjustment for small \(d\)); because \(A_d\) is bounded, the exceptional event does not change the displayed polynomial error orders. In particular, expectations involving the remainder are bounded by the total degrees of their monomials.

**3. Exact Gram moments and variance.** Isotropy and conditioning on common vertices give
\[
\mathbb E x^2=\frac1d,\quad
\mathbb E x^4=\frac3{d(d+2)},\quad
\mathbb E[xyz]=\frac1{d^2},\quad
\mathbb E[x^2y^2]=\frac1{d^2}.
\]
Any analogous monomial with an unpaired odd vertex coordinate vanishes; in particular \(\mathbb E[x^3y]=\mathbb E[x^2yz]=0\). Set \(S=x+y+z\). Expanding and using symmetry gives
\[
\mathbb E S^2=\frac3d,\quad \mathbb E[SQ]=\frac3{d^2},\quad
\mathbb E Q^2=\frac3{d^2},
\]
\[
\mathbb E\!\left[S\sum_{\mathrm{sym}}x^2y\right]=\frac6{d^2},\qquad
\mathbb E[S(x^3+y^3+z^3)]=\frac9{d(d+2)}.
\]
Here the symmetric sum has exactly six terms, as written in the definition of \(C\). Hence
\[
\mathbb E L^2=\frac3d,\quad 2\mathbb E[LQ]=-\frac6{d^2},\quad
\mathbb E Q^2=\frac3{d^2},\quad
2\mathbb E[LC]=\frac6{d^2}+\frac3{d(d+2)}.
\]
All omitted contributions have expected absolute value \(O(d^{-5/2})\), by step 2. Since the exact mean is \(\pi/2\), the second moment of \(A_d-\pi/2\) is its variance. Therefore
\[
\operatorname{Var}(A_d)=\frac3d+\frac3{d^2}+\frac3{d(d+2)}+O(d^{-5/2})
=\frac3d+\frac6{d^2}+O(d^{-5/2}).
\]

**4. Third centered moment.** Keeping terms of total degree at most four gives
\[
\mathbb E[(A_d-\pi/2)^3]=\mathbb E L^3+3\mathbb E[L^2Q]+O(d^{-5/2}).
\]
The first term is \(-6\mathbb E[xyz]=-6/d^2\). Since \(\mathbb E[(x^2+y^2+z^2)Q]=0\) and \(\mathbb E Q^2=3/d^2\), we have \(\mathbb E[L^2Q]=6/d^2\). The result is \(12/d^2+O(d^{-5/2})\). Dividing by the variance to the power \(3/2\) gives standardized skewness \(4/\sqrt{3d}+O(d^{-1})\).

**5. Gaussian limit.** Represent each uniform sphere point as an independent standard Gaussian vector divided by its length. A three-coordinate multivariate central limit theorem applied to coordinatewise products, followed by the strong law for the three Gaussian lengths, gives
\[
\sqrt d\,(x,y,z)\ \xrightarrow{\mathrm{law}}\ N(0,I_3).
\]
The quadratic and higher-order Taylor contributions, multiplied by \(\sqrt d\), vanish in probability. Hence \(\sqrt d(A_d-\pi/2)\) converges to the negative sum of three independent standard Gaussians, proving the asserted normalized central limit theorem.

## Verification
The accompanying standalone `checker.py` recomputes the four key Gram contractions, exact polynomial contributions, the variance and third-moment coefficients, and independently samples triples of Gaussian-normalized vectors. It compares measured area and centered moments against the expansions at several dimensions. Monte Carlo is corroboration only: the proof of the infinite-dimensional limits is analytic and uses the uniform Taylor remainder and sphere concentration bounds. Run with `python checker.py`; the checker uses only the Python standard library.

## Relationship to prior work
Finch and Jones (2010) analyze the density of area and other statistics for triangles of three uniform points on the ordinary \(2\)-sphere (the case \(d=3\)); this classical exact area law is not claimed as new. Philip (2015) computes moments for the same \(2\)-sphere model. Grote, Kabluchko and Thäle (2017) prove high-dimensional limit theorems for **Euclidean convex-hull volumes** of random simplices, which are different from intrinsic great-circle triangle area. Kabluchko (2026) computes moments of solid angles of **full-dimensional cones generated by \(d\) random rays in \(\mathbb R^d\)**; its theorem on the third moment involves the \(d\)-th moment of a random triangle area on the ordinary \(2\)-sphere, not the third moment of the triangle area made by **three** random rays in varying ambient \(\mathbb R^d\). These differences in the random variables, number of generators and changing dimension rule out direct implication of the coefficients here from the inspected stated results. A published note on LKJ correlation matrices, *Exact triangle cumulants reveal the first hidden dependence in LKJ correlation matrices* (2026), independently proves the cubic Gram contraction \(\mathbb E[xyz]=d^{-2}\) in equivalent sample-correlation parameters; that contraction is a known input, not a claimed new lemma. The note does not analyze spherical excess or its nonlinear area corrections. Literature priority is still provisional; an older equivalent Gram-matrix expansion cannot be excluded without exhaustive historical review.

## Limitations
The variance and third-moment formulas are asymptotic, not exact identities for fixed dimension. Their explicit error powers do not give numerical constants. The central limit theorem alone does not imply the moment asymptotics; the latter use additional uniform-integrability estimates. No Berry–Esseen constant, exact full distribution in arbitrary dimension, or independent validation is claimed. The ambient area convention (the unique great \(2\)-sphere containing the three sampled directions) is essential.

## References
1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329 (first posted 2010-09-27). https://arxiv.org/abs/1009.5329
2. J. Philip, *The Area and Perimeter of a Random Spherical Triangle* (manuscript dated 2015-05-07), especially Section 9, Case 2. https://people.kth.se/~johanph/spherical.pdf
3. J. Grote, Z. Kabluchko and C. Thäle, *Limit theorems for random simplices in high dimensions*, arXiv:1708.00471 (first posted 2017-08-01). https://arxiv.org/abs/1708.00471
4. Z. Kabluchko, *Random Polyhedral Cones I: Distributional Results via Gale Duality*, arXiv:2602.08581 (first posted 2026-02-09), especially Section 4 and Theorem 4.2. https://arxiv.org/abs/2602.08581
5. *Exact triangle cumulants reveal the first hidden dependence in LKJ correlation matrices* (2026), published mathematical note, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-triangle-cumulants-reveal-the-first-hidden-dependence-in-l--955e3ffe3131/RESULT.md
