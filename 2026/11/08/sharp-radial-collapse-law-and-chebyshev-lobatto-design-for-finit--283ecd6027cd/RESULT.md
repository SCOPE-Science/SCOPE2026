# Sharp radial-collapse law and Chebyshev–Lobatto design for finite Gaussian coherent-state tomography

## Finding
For a finite Fock truncation, full Hermitian tomography on radially coalescing coherent-state measurement circles has an exact smallest-singular-value collapse exponent and constant. Within all fixed, positive-weight radial designs in a prescribed narrow squared-radius band, the leading condition number is uniquely minimized by Chebyshev–Lobatto squared-radius offsets and endpoint-half angular-budget weights. The resulting leading condition coefficient is explicit for every truncation dimension. The Chebyshev scalar polynomial-regression design principle is classical; the reduction of the full Hermitian coherent-state measurement operator to that principle, including proof of the diagonal radial bottleneck and the Fock-normalized coefficient, is the specific finding.

## Assumptions and scope
Fix an integer \(n\ge2\), real \(t>0\), integer \(M\ge2n-1\), distinct real numbers \(u_1,\ldots,u_n\in[-1,1]\), and weights \(w_1,\ldots,w_n>0\) summing to one. Fix all these parameters independently of \(\varepsilon\downarrow0\), and require \(t_j=t+\varepsilon u_j>0\). Define \(v(z)=(z^k/\sqrt{k!})_{k=0}^{n-1}\). On the real Hilbert space of \(n\)-dimensional Hermitian matrices, with Frobenius norm \(\|X\|_F\), define the real measurement map
\[
(\mathcal L_\varepsilon X)_{j,a}=\sqrt{w_j/M}\,e^{-t_j}\,v(z_{j,a})^*Xv(z_{j,a}),\qquad
z_{j,a}=\sqrt{t_j}\exp(2\pi i a/M),\quad 0\le a<M.
\]
Here \(\|\mathcal L_\varepsilon X\|\) is the ordinary Euclidean norm over all \(nM\) real observations, and \(\kappa\) denotes the ratio of its extreme positive singular values. The data map acts on **all Hermitian matrices**, not solely on physical density matrices, pure states, or the trace-one subspace. In particular, its spectral conditioning is not asserted as a nonlinear state-recovery error bound.

Set
\[
P(x)=\prod_{j=1}^n(x-u_j),\quad
S_n(t)=\left(\sum_{k=0}^{n-1}\big[k!\binom{n-1}{k}t^{n-1-k}\big]^2\right)^{1/2},\quad
H_n(t)=\left(\sum_{k=0}^{n-1}\frac{t^{2k}}{(k!)^2}\right)^{1/2},
\]
\[
B(u,w)=\left(\sum_{j=1}^n\frac{1}{w_jP'(u_j)^2}\right)^{1/2}.
\]
Then the exact limits, for every fixed admissible design, are
\[
\lim_{\varepsilon\downarrow0}\frac{\sigma_{\min}(\mathcal L_\varepsilon)}{\varepsilon^{n-1}}
=\frac{e^{-t}}{S_n(t)B(u,w)},\quad
\lim_{\varepsilon\downarrow0}\sigma_{\max}(\mathcal L_\varepsilon)=e^{-t}H_n(t),
\]
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{n-1}\kappa(\mathcal L_\varepsilon)=S_n(t)H_n(t)B(u,w).
\]
Moreover \(B(u,w)\ge2^{n-2}\), with equality exactly when the \(u_j\) are the full set \(\{\cos(j\pi/(n-1)):j=0,\ldots,n-1\}\), and the normalized weights are \(1/[2(n-1)]\) at the two endpoints and \(1/(n-1)\) at the other points. This includes \(n=2\), where both weights are \(1/2\). Consequently the uniquely optimal leading squared-radius layout, up to reordering, has
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{n-1}\kappa(\mathcal L_\varepsilon)
=2^{n-2}S_n(t)H_n(t).
\]

## Proof
**Angular harmonic decomposition.** Choose the Frobenius-orthonormal real-Hermitian basis consisting of the diagonal matrix units together with, for each \(k<\ell\), the symmetric and antisymmetric imaginary combinations \((E_{k\ell}+E_{\ell k})/\sqrt2\) and \(i(E_{k\ell}-E_{\ell k})/\sqrt2\). Fourier orthogonality on the \(M\) equally spaced angles, with \(M\ge2n-1\), separates the diagonal Fourier mode from all lags \(d=1,\ldots,n-1\), without aliasing positive and negative frequencies. It yields a radial block \(A_0\in\mathbb R^{n\times n}\) and, for each \(d\ge1\), two identical real blocks \(A_d\in\mathbb R^{n\times(n-d)}\), where
\[
A_0(j,k)=\sqrt{w_j}e^{-t_j}\frac{t_j^k}{k!},\quad 0\le k<n,
\qquad A_d(j,k)=\sqrt{w_j}e^{-t_j}\frac{t_j^{k+d/2}}{\sqrt{k!(k+d)!}},\quad 0\le k<n-d.
\]
These give all \(n^2\) singular values, counting multiplicities, because \(n+2\sum_{d=1}^{n-1}(n-d)=n^2\). Each block has full column rank for every positive distinct \(t_j\), by positivity of its diagonal factors and the ordinary Vandermonde rank condition. Hence the whole tomography map has full rank.

**Only the diagonal radial block attains the worst collapse exponent.** The monomial Vandermonde for \(A_d\) has \(n-d\) columns and \(n\) rows. Selecting any fixed set of \(n-d\) distinct offsets and rescaling its columns by powers of \(\varepsilon\), a bounded invertible confluent-polynomial change of basis around \(t\) gives \(\sigma_{\min}(A_d)\ge c_d\varepsilon^{n-d-1}\) for some \(c_d>0\) depending on the fixed design and \(t\). Thus every offdiagonal singular value is asymptotically larger than order \(\varepsilon^{n-1}\) as \(\varepsilon\downarrow0\).

**Exact inverse of the diagonal block.** Let \(V_{jk}=t_j^k/k!\) and \(D=\operatorname{diag}(\sqrt{w_j}e^{-t_j})\), so that \(A_0=DV\). The inverse \(V^{-1}\) is obtained by Lagrange interpolation:
\[
(V^{-1})_{kj}=k!\,[x^k]\frac{\prod_{\ell\ne j}(x-t_\ell)}{\prod_{\ell\ne j}(t_j-t_\ell)}.
\]
Because \(t_j-t_\ell=\varepsilon(u_j-u_\ell)\), we have the entrywise, hence operator-norm, rank-one limit
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{n-1}A_0^{-1}
=e^t\,c(t)b(u,w)^T,
\quad c_k(t)=k!\binom{n-1}{k}(-t)^{n-1-k},\quad
b_j=\frac1{\sqrt{w_j}P'(u_j)}.
\]
The unique nonzero singular value of the limit is \(e^tS_n(t)B(u,w)\). Taking inverse extreme singular values establishes the claimed smallest-singular-value limit for \(A_0\), and the angular decomposition transfers it to the full map.

**Largest singular value.** At \(\varepsilon=0\), each block is rank one. The diagonal block has its nonzero singular value \(e^{-t}H_n(t)\). For \(d\ge1\), the corresponding value is
\[
e^{-t}\left(\sum_{k=0}^{n-d-1}\frac{t^{2k+d}}{k!(k+d)!}\right)^{1/2},
\]
strictly below \(e^{-t}H_n(t)\), by strict Cauchy–Schwarz applied to the positive finite sequence \((t^k/k!)_{0\le k<n}\) and its shifted truncation. Finite-dimensional singular-value continuity gives the largest-singular-value limit and hence the condition-number limit.

**Sharp optimal design and equality.** The monic Chebyshev polynomial \(q(x)=2^{2-n}T_{n-1}(x)\) obeys \(\|q\|_{L^\infty([-1,1])}=2^{2-n}\). The leading-coefficient Lagrange identity for any distinct \(u_j\) gives \(\sum_jq(u_j)/P'(u_j)=1\). Weighted Cauchy–Schwarz implies
\[
1\le\left(\sum_j\frac1{w_jP'(u_j)^2}\right)^{1/2}
\left(\sum_jw_jq(u_j)^2\right)^{1/2}
\le B(u,w)\,2^{2-n},
\]
so \(B(u,w)\ge2^{n-2}\). Equality requires all \(n\) distinct points to be the \(n\) extrema of \(T_{n-1}\), and equality in Cauchy–Schwarz forces \(w_j\propto1/|P'(u_j)|\). The standard Chebyshev-extrema barycentric weights have endpoint magnitude half that at interior points, giving exactly the stipulated normalized weights. They attain equality, including the endpoint-only case \(n=2\).

## Verification
The supplied standalone script `check.py` constructs the full **real** measurement matrix directly from the Hermitian orthonormal basis, without using the Fourier block decomposition. It checks numerical singular values against both analytical limits for \(2\le n\le6\), the exact Chebyshev coefficient, positivity/rank, and randomized design comparisons. Run `python3 check.py` with NumPy; the current run completed 105 assertions and reported `RADIAL_FOCK_TOMOGRAPHY_CHECKS_PASS 105`. Numerical tests do not establish the universal theorem, whose proof is analytical.

## Relationship to prior work
The Husimi/coherent-state polynomial-interpolation approach to continuous-variable tomography is established in Landon-Cardinal, Govia, and Clerk (arXiv:1706.07816), which uses two-dimensional sampling geometry including Padua points; it does not give this radially coalescing multi-circle Hermitian spectrum. Multi-window Gaussian time–frequency phase-retrieval results (arXiv:2207.10620) concern uniqueness on sampling lattices, not the present sharp least-singular-value coefficient. The two-circle pure-state uniqueness theorem in arXiv:2009.02061 is a different, weaker object class and does not provide general Hermitian information completeness or stability. Clustered Fourier Vandermonde estimates (arXiv:2107.09326) establish other concentration and singular-value bounds, not this exact weighted Fock lift. The Chebyshev-polynomial optimal-design principle is **classical**, with precursors in polynomial regression and optimal design (Pukelsheim and Studden, 1993); novelty is **not claimed** for its standalone scalar interpolation inequality. The distinct contribution here is the explicit reduction and exact normalization for the entire multi-circle Hermitian coherent-state measurement operator.

## Limitations
The design weights and offsets are fixed as \(\varepsilon\to0\); no uniform minimax claim over \(\varepsilon\)-dependent offsets or vanishing weights, and no exact finite-width optimality, is established. The result uses at least \(2n-1\) equally spaced angles on **each** circle and squared-radius offsets in \([-1,1]\); arbitrary nonuniform angular sampling is not covered. Noise is measured in Euclidean intensity coordinates. No claim is made about shot noise, positivity/trace constraints, pure-state nonlinear phase retrieval, or nonlinear estimation under a prior. Historical priority remains provisional: equivalent Hermitian-tomography formulations in quantum measurement design or older generalized regression literature could exist despite the recorded searches.

## References
1. Landon-Cardinal, Govia, and Clerk, *Quantitative tomography for continuous variable quantum systems*, first public June 23, 2017, arXiv:1706.07816, https://arxiv.org/pdf/1706.07816.
2. Grohs, Liehr, and Rathmair, work on multi-window short-time Fourier phase retrieval, first public July 21, 2022, arXiv:2207.10620, https://arxiv.org/pdf/2207.10620.
3. Pure-state phase retrieval from two circular modulus traces, arXiv:2009.02061, https://arxiv.org/pdf/2009.02061.
4. Batenkov and Goldman, work on singular values of clustered Fourier/Vandermonde matrices, arXiv:2107.09326, https://arxiv.org/pdf/2107.09326.
5. F. Pukelsheim and W. J. Studden (1993), classical polynomial-regression optimal design, https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1993b.pdf.
