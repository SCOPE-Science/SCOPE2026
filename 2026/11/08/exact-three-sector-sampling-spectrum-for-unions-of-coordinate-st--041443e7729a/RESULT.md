# Exact three-sector sampling spectrum for unions of coordinate stars on Johnson slices

## Finding

Let \(n,t,k\) be integers satisfying \(t\ge3\), \(k\ge2\), and \(q:=n-t\ge k\). On the uniform Johnson slice \(X=\binom{[n]}{k}\), let \(H_1\) denote the degree-one harmonic subspace, consisting of all functions
\[
f_a(S)=\sum_{i\in S}a_i,\qquad a\in\mathbb R^n,\quad \sum_{i=1}^n a_i=0.
\]
Fix \(T\subset[n]\) with \(|T|=t\), and let \(U_T=\{S\in X:S\cap T\ne\varnothing\}\), the union of the \(t\) coordinate stars. Define \(R:H_1\to L^2(X)\) by \(Rf=\mathbf1_{U_T}f\), with the uniform probability on \(X\), and define the positive concentration operator \(C=R^*R\) on \(H_1\). Write
\[
p_0=\frac{\binom qk}{\binom nk},\qquad
\lambda_O=1-p_0\frac{n(n-1)(q-k)}{q(q-1)(n-k)},\qquad
\lambda_M=1-p_0\frac{k(n-1)t}{q(n-k)}.
\]
Then its **complete spectrum with multiplicities** is
\[
\boxed{\operatorname{spec}(C)=\{1^{[t-1]},\;\lambda_O^{[q-1]},\;\lambda_M^{[1]}\}.}
\]
Multiplicities of coincident eigenvalues are combined. All eigenvalues are positive; in particular, sampling a first-harmonic function on \(U_T\) is injective. The singular values of \(R\) are the square roots of the displayed eigenvalues. Thus the exact optimal norm of linear recovery from samples in \(R(H_1)\) is
\[
\boxed{\|R^{-1}:R(H_1)\to H_1\|=\bigl(\min\{\lambda_O,\lambda_M\}\bigr)^{-1/2}.}
\]
There is a **sharp integer phase boundary**:
\[
\boxed{\lambda_O\le\lambda_M\ \Longleftrightarrow\ n\ge(t+1)k.}
\]
At \(n=(t+1)k\), the least eigenvalue has multiplicity \(q\); above it the outside-coordinate sector is the unique least-eigenvalue sector, and below it the one-dimensional mixed sector is uniquely least. For instance, at \((n,t,k)=(8,3,2)\) both lower eigenvalues equal \(1/2\).

In the density regime where \(t\ge3\) is fixed and \(k/n\to\rho\in(0,1)\), the two non-unit eigenvalues converge, respectively, to
\[
\lambda_O\longrightarrow1-(1-\rho)^t,
\qquad
\lambda_M\longrightarrow1-t\rho(1-\rho)^{t-1}.
\]
Their crossover is exactly \(\rho=1/(t+1)\), in agreement with the finite integer boundary. For fixed \(k,t\) and \(n\to\infty\), the sharp recovery norm is asymptotic to \(\sqrt{n/[t(k-1)]}\).

## Assumptions and scope

The domain is the nontrivial finite Johnson slice with \(2\le k\le n-t\); the range uses the **ambient** uniform measure, not the probability conditioned on \(U_T\). The first harmonic degree excludes constants. The concentration operator is equivalently the restriction to \(H_1\) of \(P_{H_1}M_{\mathbf1_{U_T}}P_{H_1}\), where \(P_{H_1}\) is orthogonal projection in \(L^2(X)\). All Hilbert norms and orthogonality statements use the normalized counting inner product. The projective coordinate representation is unique on the zero-sum coefficient hyperplane because \(1\le k\le n-1\).

## Proof

**1. The ambient coefficient metric.** For two coefficient vectors with zero coordinate sums, exchangeability of the uniform \(k\)-set gives
\[
\langle f_a,f_b\rangle_{L^2(X)}
=\frac{k(n-k)}{n(n-1)}\sum_{i=1}^n a_i b_i
=:\beta\,a\cdot b.
\]
Indeed, a single coordinate is selected with probability \(k/n\), and any two distinct coordinates are selected together with probability \(k(k-1)/(n(n-1))\). Therefore the degree-one coefficient subspace has dimension \(n-1\), with the asserted positive multiple of its Euclidean metric.

**2. Orthogonal decomposition of coefficients.** Write \(O=[n]\setminus T\), with \(|O|=q\). Decompose the zero-sum coefficient hyperplane orthogonally into
\[
V_T=\{a:\operatorname{supp}(a)\subseteq T,\ \sum_{i\in T}a_i=0\},\quad
V_O=\{a:\operatorname{supp}(a)\subseteq O,\ \sum_{i\in O}a_i=0\},
\]
and the span \(V_M\) of the vector with coefficient \(q\) on \(T\) and \(-t\) on \(O\). Their dimensions are \(t-1\), \(q-1\), and one, respectively, adding to \(n-1\). Each subspace is invariant under the compression \(C\): the quadratic form of the omitted sample set \(X\setminus U_T\) is invariant under permutations within \(T\) and within \(O\), and its cross terms between these three sectors vanish by zero-sum symmetry. The same is true for the ambient form in step 1. We compute their scalar compression factors directly.

**3. First sector.** If \(a\in V_T\), then \(f_a(S)=0\) for every \(S\) disjoint from \(T\). Thus \(\|Rf_a\|_2^2=\|f_a\|_2^2\), and the entire \(V_T\) sector has eigenvalue one.

**4. Outside sector.** If \(a\in V_O\), conditional on avoiding \(T\), the random \(S\) is a uniform \(k\)-subset of the \(q\) coordinates in \(O\). The analogue of step 1 on that slice gives
\[
\mathbb E\bigl[f_a(S)f_b(S)\mid S\cap T=\varnothing\bigr]
=\frac{k(q-k)}{q(q-1)}a\cdot b.
\]
The avoidance probability is \(p_0\). Subtracting this omitted mass from the ambient inner product and dividing by \(\beta\) yields the eigenvalue \(\lambda_O\) as displayed.

**5. Mixed sector.** Let \(a_i=q\) on \(T\) and \(a_i=-t\) on \(O\), so \(\|a\|_2^2=tqn\). On the omitted set the function is the constant \(-kt\); hence the omitted squared norm is \(p_0k^2t^2\). The total squared norm from step 1 is
\[
\beta\|a\|_2^2=\frac{tqk(n-k)}{n-1}.
\]
Taking one minus the omitted-to-total ratio produces \(\lambda_M\). These three invariant sectors exhaust \(H_1\), proving the spectrum.

**6. Positivity and the exact transition.** The factor \(p_0\) is strictly positive because \(q\ge k\). The two non-unit eigenvalues are nonnegative by construction; they are in fact positive. For \(V_O\), choose a nonzero zero-sum vector supported on two outside coordinates. There are sampled \(k\)-sets meeting \(T\) whose intersections with those two coordinates differ, since \(k\ge2\) and \(q\ge k\); thus the restricted function is nonzero. For \(V_M\), write \(h=|S\cap T|\), giving \(f_a(S)=nh-kt\). Since \(t\ge3\), \(k\ge2\), and \(q\ge k\), the sample window contains sets with \(h=1\) and \(h=2\); the two corresponding function values differ, so its restricted norm is nonzero. The strict inequality \(\lambda_M<1\) follows from \(p_0>0\); \(\lambda_O=1\) precisely at \(q=k\). Finally, direct subtraction and factorization give
\[
\lambda_O-\lambda_M
=-p_0\frac{n-1}{(q-1)(n-k)}\bigl[n-(t+1)k\bigr].
\]
Since the prefactor is negative, the claimed phase boundary follows. Eigenvalue ordering and multiplicity establish the sharp inverse norm by the finite-dimensional singular-value theorem.

**7. Limits.** For fixed \(t\) and \(k/n\to\rho\in(0,1)\), the avoidance probability \(p_0\) tends to \((1-\rho)^t\), and each rational factor has the limit indicated in the finding. For fixed \(t,k\), the avoidance probability satisfies \(p_0=1-tk/n+O(n^{-2})\) and the outside-sector rational factor equals \(1+t/n+O(n^{-2})\). Thus \(\lambda_O=t(k-1)/n+O(n^{-2})\), while \(\lambda_M=1+O(n^{-1})\). For sufficiently large \(n\), the outside sector is the bottleneck and the asserted recovery-norm asymptotic follows.

## Verification

A standalone standard-library exact-rational checker, `verify.py`, independently computes the restricted Gram form by summing coordinate inclusion probabilities, rather than using the conditional-variance reductions in the proof. For every permitted \(5\le n\le13\), \(t\ge3\), and \(2\le k\le n-t\), it checks the three sector eigenvalues, all cross-sector orthogonalities, the sharp phase comparison, and positivity. This covers 165 parameter instances, including four ties. A separate boundary test treats \(k=1\), where the outside sector is invisible and injectivity fails. Exact finite tests corroborate the general analytic proof; they are not substitutes for it. Run `python3 verify.py` next to this document.

## Relationship to prior work

Filmus (2014) proves the harmonic decomposition of functions on Boolean slices, including the degree-one zero-sum representation used here; that foundational decomposition does not itself evaluate concentration on a union of coordinate stars or its least singular value. The Johnson-graph concentration analysis of Bernard, Crampé, and Vinet (2021) uses distance neighborhoods of a reference \(k\)-set, not the present mask consisting of all \(k\)-sets meeting a prescribed \(t\)-set. The prior two-coordinate-face calculation supplies a complete spectrum for the **intersection** of two coordinate stars and all cumulative harmonic cutoffs; its mask and parameter range do not give the three-or-more-star **union** and exact phase boundary of this result. The prior finite-Grassmann one-point-star calculation addresses a single subspace-incidence star, not the present multi-star Johnson sampling family. The present statement makes no originality claim for the Johnson harmonic decomposition or the general theory of singular-value recovery.

## Limitations

The theorem concerns first harmonics **without constants**, uniform ambient probability, and a nonempty union of at least three coordinate stars; it does not give higher-degree Slepian spectra, independently weighted stars, conditioned rather than ambient sample norms, or other window shapes. The prescribed window has a large symmetric stabilizer that enables the three-sector reduction. An equivalent result under a different association-scheme or frame-theoretic normalization could be present in unindexed prior literature. Independent mathematical validation has not been performed.

## References

1. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first public 2014-06-01), especially §§2–4; *Electronic Journal of Combinatorics* 23 (2016), P1.23. https://arxiv.org/abs/1406.0142
2. P.-A. Bernard, N. Crampé, and L. Vinet, *Entanglement of Free Fermions on Johnson Graphs*, arXiv:2104.11581 (first public 2021-04-23), especially spatial masks and concentration methods. https://arxiv.org/html/2104.11581v1
3. *Exact two-coordinate-face concentration spectrum on Johnson slices* (2026), published mathematical finding, sections Finding, Proof, Relationship to prior work. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-two-coordinate-face-concentration-spectrum-on-johnson-slic--d102febb3be1/RESULT.md
4. *Two-level Slepian spectrum for point stars in finite Grassmann schemes* (2026), published mathematical finding, sections Finding and Assumptions and scope. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-two-level-slepian-spectrum-for-point-stars-in-finite-grassmann-s--09f37b63a641/RESULT.md
