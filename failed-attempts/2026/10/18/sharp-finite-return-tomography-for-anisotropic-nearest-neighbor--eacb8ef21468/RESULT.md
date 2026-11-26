# Sharp finite-return tomography for anisotropic nearest-neighbor lattice walks

## Finding

Fix a known integer dimension \(d\geq2\). A translation-invariant random walk on \(\mathbb Z^d\), started at the origin, makes independent steps \(+e_j\) and \(-e_j\), each with probability \(h_j/2\), where every \(h_j>0\) and \(\sum_{j=1}^d h_j=1\). Let \(r_{2m}(h)=\Pr_h(S_{2m}=0)\) and let \(f_{2m}(h)\) be the probability that the first strictly positive return occurs at step \(2m\).

**Theorem (sharp finite-return identifiability).** For any two such vectors \(h,g\),
\[
\bigl(r_2(h),r_4(h),\ldots,r_{2(d-1)}(h)\bigr)
=\bigl(r_2(g),r_4(g),\ldots,r_{2(d-1)}(g)\bigr)
\]
if and only if \(g\) is a permutation of \(h\). The identical conclusion holds with \(f_{2m}\) in place of \(r_{2m}\). For every \(d\geq3\), \(d-2\) return probabilities are **generically insufficient**: through any strictly positive vector with pairwise distinct coordinates there passes a nonconstant smooth local one-dimensional family of positive probability vectors sharing all \(r_{2m}\) for \(1\leq m\leq d-2\). In dimension \(d=2\), the one two-step return probability is sufficient, whereas no observations cannot distinguish different weights.

Thus exactly \(d-1\) successive even-time return probabilities are necessary and sufficient in the worst case, up to unavoidable coordinate relabeling. This is a finite-data theorem for fixed nearest-neighbor support, not a reconstruction theorem for arbitrary finite-range random walks.

## Assumptions and scope

The dimension is known and finite. All \(d\) coordinate weights are strictly positive, summing to one; repeated weights are allowed in the uniqueness statement. The increments are independent and identically distributed, with **equal probabilities for the two signs of each coordinate step**, and no holding probability or non-nearest-neighbor jumps. The observation \(r_{2m}\) is the exact point probability of return after \(2m\) steps, not the eventual-return probability. All odd-step returns vanish because of bipartiteness. The sharpness claim is local at every vector with pairwise distinct positive coordinates; it does not assert nonuniqueness at the uniform vector.

## Proof

**1. A product formula and its triangular inversion.** The one-step characteristic function is
\[
\phi_h(\theta)=\sum_{j=1}^d h_j\cos\theta_j.
\]
Fourier inversion, expansion of the exponential, and the integral representation of the modified Bessel function give the entire formal series identity
\[
A_h(z):=\sum_{m\geq0}\frac{r_{2m}(h)}{(2m)!}z^{2m}
=\frac1{(2\pi)^d}\int_{[-\pi,\pi]^d}e^{z\phi_h(\theta)}\,d\theta
=\prod_{j=1}^d I_0(h_jz),
\]
where \(I_0(z)=\sum_{\ell\geq0}z^{2\ell}/(4^\ell(\ell!)^2)\). The absence of odd coefficients follows from \(I_0(-z)=I_0(z)\).

Write \(\log I_0(z)=\sum_{m\geq1}c_mz^{2m}\). The differential equation \(I_0''(z)+z^{-1}I_0'(z)-I_0(z)=0\), valid as a formal identity at the removable singularity, implies
\[
c_1=\frac14,\qquad
c_m=-\frac1{m^2}\sum_{k=1}^{m-1}k(m-k)c_kc_{m-k}\quad(m\geq2).
\]
Induction proves \((-1)^{m-1}c_m>0\) for every \(m\geq1\): every term in the recurrence has the common opposite sign of \(c_m\). In particular none of these constants vanish. Taking logarithms of the product formula yields
\[
[z^{2m}]\log A_h(z)=c_m\sum_{j=1}^d h_j^{2m}.
\]
The coefficient on the left depends only on \(r_2,\ldots,r_{2m}\), since \(A_h(0)=1\). Therefore equality of the first \(d-1\) even-time return probabilities is equivalent to equality of the first \(d-1\) power sums \(s_m(h)=\sum_j h_j^{2m}\).

**2. A monotone last-coefficient argument.** Set \(q_j=h_j^2>0\), and let \(e_k(q)\) denote the elementary symmetric polynomial of degree \(k\) in these \(d\) numbers. Newton's identities recursively recover \(e_1,\ldots,e_{d-1}\) from \(s_1,\ldots,s_{d-1}\). Hence two candidate vectors \(h,g\) consistent with the observations have polynomials
\[
Q_h(t)=\prod_{j=1}^d(t+h_j^2),\qquad Q_g(t)=\prod_{j=1}^d(t+g_j^2)
\]
that differ, if at all, by a **constant** \(e_d(g)-e_d(h)\). Their derivatives are therefore identical. Both polynomials and their common derivative are strictly positive for \(t>0\).

For any positive \(q\), the beta integral gives
\[
\sqrt q=\frac1\pi\int_0^\infty\frac{q\,dt}{\sqrt t\,(t+q)}.
\]
Consequently,
\[
\sum_{j=1}^d h_j
=\frac1\pi\int_0^\infty t^{-1/2}
\left(d-t\frac{Q_h'(t)}{Q_h(t)}\right)dt.
\]
Both integrals converge absolutely because the integrands are \(O(t^{-1/2})\) near zero and \(O(t^{-3/2})\) at infinity. If \(e_d(g)>e_d(h)\), the difference of these integrals is strictly positive:
\[
\sum_j g_j-\sum_j h_j
=\frac1\pi\int_0^\infty t^{1/2}Q_h'(t)
\left(\frac1{Q_h(t)}-\frac1{Q_g(t)}\right)dt>0.
\]
This contradicts \(\sum_j g_j=\sum_j h_j=1\). Interchanging \(h\) and \(g\) excludes \(e_d(g)<e_d(h)\). Thus their remaining elementary symmetric polynomials coincide as well, so \(Q_h=Q_g\). Equality of their root multisets gives \(\{h_j^2\}=\{g_j^2\}\); strict positivity implies that \(g\) is a permutation of \(h\). The converse follows directly from the symmetric product formula. This argument also proves uniqueness when the vector contains repeated positive weights.

**3. Sharpness of the observation count.** Suppose \(d\geq3\) and fix a vector \(h\) with \(d\) distinct positive coordinates. Consider
\[
F(x)=\left(\sum_{j=1}^d x_j,\ \sum_{j=1}^d x_j^2,\ldots,\sum_{j=1}^d x_j^{2(d-2)}\right)
\]
as a map from a neighborhood of \(h\) in \(\mathbb R^d\) to \(\mathbb R^{d-1}\). Its derivative has rows \((1)_j\) and \((2k x_j^{2k-1})_j\), \(1\leq k\leq d-2\). Any linear dependence among these rows would give a nonzero polynomial of the form
\[
P(t)=a_0+\sum_{k=1}^{d-2}a_kt^{2k-1}
\]
vanishing at \(d\) distinct positive coordinates \(h_j\). A polynomial with at most \(d-1\) nonzero monomials has at most \(d-2\) strictly positive roots (Descartes' rule of signs, counting multiplicities). Thus the derivative has rank \(d-1\). By the implicit-function theorem the level set \(F(x)=F(h)\) near \(h\) is a nontrivial smooth one-dimensional manifold; it stays inside the positive simplex in a sufficiently small neighborhood and cannot consist solely of finitely many permutations. The product/log identity in Step 1 shows that every vector on this manifold has the same first \(d-2\) even-time returns. For \(d=2\), no-data insufficiency is immediate. Hence the cutoff is sharp.

**4. First-return equivalence.** Let \(f_{2m}=\Pr(T=2m)\) and \(r_0=1\). The first-return decomposition is valid for any fixed finite horizon, recurrent or transient:
\[
r_{2m}=\sum_{k=1}^m f_{2k}\,r_{2(m-k)}\qquad(m\geq1).
\]
It is a triangular transformation with diagonal coefficient \(r_0=1\), so \(f_2,\ldots,f_{2M}\) and \(r_2,\ldots,r_{2M}\) determine each other for every finite \(M\). The preceding uniqueness and sharpness transfer verbatim to first-return probabilities.

**5. Constructive recovery.** From the observed return values compute the truncated series \(A_h\), extract \([z^{2m}]\log A_h/c_m\) for \(1\leq m\leq d-1\), and use Newton's identities to determine \(e_1,\ldots,e_{d-1}\) of the unknown positive numbers \(q_j=h_j^2\). The remaining coefficient \(e_d\) is the unique **admissible** constant term for which \(Q(t)=t^d+e_1t^{d-1}+\cdots+e_{d-1}t+e_d\) factors with positive \(q_j\) and satisfies \(\sum_j\sqrt{q_j}=1\). The strict integral monotonicity proves uniqueness, not numerical stability. Sorting the positive square roots recovers the unordered weights.

## Verification

A standalone standard-library Python program, `verify.py`, performs exact rational checks of the Bessel-log recurrence and alternating signs, the product-return coefficients, logarithmic power-sum inversion, Newton identities, finite-horizon renewal inversion, and generic Jacobian minors in dimensions \(2\) through \(8\). Running `python3 verify.py` completed **249 exact rational checks**, all passing.

It also gives a simple explicit sharpness witness in dimension three: \(h=(1,5,6)/12\) and \(g=(2,3,7)/12\). Both have \(r_2=31/144\), but their four-step return probabilities are respectively \(961/9216\) and \(865/9216\). These are nonpermutation vectors. The theorem for arbitrary dimension, all real positive weights and infinite families is proved in Steps 1–4, not established by finite experiments.

## Relationship to prior work

Hsiau, Tsai and Yao (2026, arXiv:2609.36728) analyze **exactly this family** of anisotropic nearest-neighbor lattice walks and prove stochastic dominance of first-return times under weight-vector majorization. Their main theorem and return/first-return identities are forward comparisons, not identification of arbitrary positive weights by a sharp finite prefix. The product expression used above is a classical Fourier–Bessel identity; neither it nor Newton's identities are claimed as new.

Belmans, Galkin and Mukhopadhyay (2026, arXiv:2610.08348), especially Section 6 and its symmetric-walk discussion, show that **general** finite-range lattice walks can have equal complete return sequences despite inequivalent supports, and provide symmetric walks with identical return sequences but different step weights on a square support. The present theorem avoids that obstruction by fixing the much smaller support \(\{\pm e_1,\ldots,\pm e_d\}\) and strict sign symmetry. It does not address their open shape-recovery question for arbitrary symmetric finite-range walks. Zhou (2015, arXiv:1512.04142) proves an all-return-sequence uniqueness theorem for primitive symmetric walks on the **one-dimensional** lattice, not a dimension-dependent sharp finite-data result for these multidimensional nearest-neighbor walks.

The distinguishing result here is the finite \(d-1\) cutoff **and its generic optimality** within a precisely specified probability simplex. Prior inverse-moment methods may exist outside the inspected material; no independent priority certification is claimed.

## Limitations

Recovery is only up to coordinate permutation. The dimension and exact nearest-neighbor support are assumed known, and each coordinate weight must be positive. The theorem does not cover asymmetric directions, holding steps, general symmetric finite-range supports, or inference from noisy return-frequency estimates. Although the reconstruction is unique, no quantitative conditioning or error bound near repeated weights is asserted. Generic necessity means positive distinct-coordinate neighborhoods, not every point of the simplex. Previous results on more general support classes remain fully applicable in their own domains. Independent verification of priority and mathematical correctness has not been performed.

## References

1. S.-R. Hsiau, T.-Y. Tsai and Y.-C. Yao, *Stochastic dominance of first return times for nearest-neighbor random walks on \(\mathbb Z^d\)*, arXiv:2609.36728, first posted 2026-09-29, https://arxiv.org/abs/2609.36728.
2. P. Belmans, S. Galkin and S. Mukhopadhyay, *Can one hear the shape of a lattice random walk?*, arXiv:2610.08348, first posted 2026-10-06, https://arxiv.org/html/2610.08348v1, Section 6.
3. M. Zhou, *Return Probabilities of Random Walks*, arXiv:1512.04142, first posted 2015-12-14, https://arxiv.org/abs/1512.04142.
4. Classical facts used: Fourier inversion for lattice return probabilities, the modified Bessel equation, Newton identities, Descartes' rule of signs, and the implicit-function theorem.
