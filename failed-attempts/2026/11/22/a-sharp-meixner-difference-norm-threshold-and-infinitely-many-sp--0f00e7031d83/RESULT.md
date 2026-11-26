# A sharp Meixner difference-norm threshold and infinitely many spectral outliers

## Finding
For every \(0<c<1\) and \(\beta>0\), put \(w_k=(\beta)_k c^k/k!\) for integers \(k\ge0\), and define the forward difference \((\Delta f)(k)=f(k+1)-f(k)\) on the real weighted Hilbert space \(H_{c,\beta}=\ell^2(\mathbb N_0,w)\). Let \(\gamma_n(c,\beta)\) be the sharp inequality constant \(\|\Delta p\|_{c,\beta}\le\gamma_n(c,\beta)\|p\|_{c,\beta}\) among all polynomials of degree at most \(n\). Then the limit \(\Gamma(c,\beta)=\lim_{n\to\infty}\gamma_n(c,\beta)\) exists and equals \(\|\Delta\|_{H_{c,\beta}\to H_{c,\beta}}\).

The limiting sharp constant has the exact phase boundary
\[
\Gamma(c,\beta)=1+c^{-1/2}\quad\text{if and only if}\quad\beta\ge1.
\]
For fixed \(c\), it is strictly decreasing on \(0<\beta<1\), is constant on \([1,\infty)\), and satisfies
\[
\lim_{\beta\downarrow0}\sqrt{c\beta}\,\Gamma(c,\beta)=1,
\qquad \lim_{\beta\uparrow1}\Gamma(c,\beta)=1+c^{-1/2}.
\]
The squared forward-difference operator has essential spectrum exactly
\[
\sigma_{\rm ess}(\Delta^*\Delta)
=[(c^{-1/2}-1)^2,(c^{-1/2}+1)^2].
\]
When \(0<\beta<1\), it additionally has *infinitely many distinct simple eigenvalues strictly above* the upper edge \((1+c^{-1/2})^2\); these can accumulate only at that edge. When \(\beta\ge1\), there is no spectrum above the edge. In particular, for \(\beta<1\), every polynomial degree sufficiently large has \(\gamma_n(c,\beta)>1+c^{-1/2}\).

## Assumptions and scope
Here \((\beta)_0=1\), \((\beta)_k=\beta(\beta+1)\cdots(\beta+k-1)\) for \(k\ge1\), and all parameters are real. The theorem concerns the real or complex Hilbert-space norm (the constants coincide), *all* \(n\ge0\), and the closure of all finite-degree algebraic polynomials. Essential spectrum is that of the bounded self-adjoint operator \(\Delta^*\Delta\); discrete eigenvalues above it are counted with multiplicity. No claim about the exact positions or spacing of those eigenvalues is made.

## Proof

**1. Polynomial density.** The negative-binomial moments are finite: \(\sum_{k\ge0} w_k r^k=(1-cr)^{-\beta}\) for \(0\le r<1/c\); hence every polynomial lies in \(H_{c,\beta}\). Suppose \(f\in H_{c,\beta}\) is orthogonal to every polynomial. The power series \(F(z)=\sum_{k\ge0}w_k f(k)z^k\) is holomorphic for \(|z|<c^{-1/2}\), because Cauchy--Schwarz bounds its absolute sum by \(\|f\|_{c,\beta}(1-c|z|^2)^{-\beta/2}\). Since \(c^{-1/2}>1\), \(F\) is analytic near \(z=1\). Orthogonality to the falling-factorial polynomials gives \(F^{(m)}(1)=0\) for every integer \(m\ge0\). The identity theorem yields \(F\equiv0\), so \(f(k)=0\) for every \(k\). Thus polynomials are dense.

**2. The Jacobi representation and its essential band.** Under the unitary transformation \((Uf)_k=\sqrt{w_k}f(k)\), the forward shift \(Sf(k)=f(k+1)\) becomes the backward weighted shift \((Tx)_k=a_kx_{k+1}\), with
\[
a_k=\sqrt{\frac{k+1}{c(k+\beta)}},\qquad a=c^{-1/2}.
\]
It is bounded because \(\sup_k a_k<\infty\). Thus \(\Delta\) is bounded, and polynomial density implies \(\gamma_n\uparrow\Gamma=\|T-I\|\).

Conjugate \(J=(T-I)^*(T-I)\) by the alternating diagonal signs \((-1)^k\) to get the self-adjoint Jacobi operator \(B_\beta\) with
\[
(B_\beta)_{00}=1,\qquad
(B_\beta)_{kk}=1+a_{k-1}^2\ (k\ge1),\qquad
(B_\beta)_{k,k+1}=a_k>0.
\]
Since \(a_k\to a\), this operator is a compact perturbation of the half-line Jacobi operator with constant diagonal \(1+a^2\) and constant off-diagonal \(a\): subtracting the two matrices gives a finite-rank boundary term plus vanishing diagonal and weighted-shift coefficients. The constant-coefficient operator is diagonalized by the discrete sine transform, yielding the stated essential interval \([(a-1)^2,(a+1)^2]\) by compact-perturbation invariance of the essential spectrum.

**3. The flat phase.** If \(\beta\ge1\), then \(a_k\le a\) for every \(k\), so \(\|T-I\|\le\|T\|+1\le a+1\). The essential spectral upper edge \((a+1)^2\) gives the reverse inequality. Thus \(\Gamma=1+a\), and no spectral value of \(J\) exceeds that edge.

**4. The outlier phase and its infinite multiplicity in count.** Let \(0<\beta<1\) and \(\delta=1-\beta>0\). Then \(a_k>a\). For \(k\ge1\), the diagonal gain over the constant tail is
\[
a_{k-1}^2-a^2=\frac{\delta}{c(k+\beta-1)}>0.
\]
For integers \(K\ge2,L\ge2\), take a nonnegative vector \(h\) supported on \(K,\ldots,K+L-1\) with \(h_{K+j-1}=\sin(j\pi/(L+1))\), \(1\le j\le L\). Writing \(E=(1+a)^2\), the standard sine-vector identity for a constant Jacobi chain, the strictly positive diagonal gains, and the nonnegative off-diagonal gains give
\[
\frac{\langle h,B_\beta h\rangle}{\|h\|_2^2}
\ge E-2a\left(1-\cos\frac{\pi}{L+1}\right)
+\frac{\delta}{c(K+L+\beta-2)}.
\]
Set \(L=\lfloor K^{3/4}\rfloor\). The negative term is \(O(K^{-3/2})\) whereas the positive term is asymptotic to \(\delta/(cK)\), so for all sufficiently large \(K\) the quotient is strictly greater than \(E\). Choose arbitrarily many such blocks mutually separated by at least one unused site. The Jacobi matrix couples only nearest neighbors, so cross terms vanish; their span is an arbitrarily high-dimensional subspace with Rayleigh quotients strictly above \(E\). The min--max principle and the essential-spectrum bound yield infinitely many eigenvalues above \(E\), with only possible accumulation point \(E\). Each eigenvalue is simple: the first-row eigenvalue equation determines the second coordinate from the first, and the nonzero off-diagonals then determine all subsequent coordinates; a zero first coordinate forces the whole vector to vanish.

**5. Strict parameter transition and endpoint behavior.** For \(0<\beta_1<\beta_2<1\), every off-diagonal coefficient of \(B_{\beta_1}\) is larger than its counterpart in \(B_{\beta_2}\), as is every diagonal coefficient after index zero. The top eigenvalue of \(B_{\beta_2}\) is isolated above \(E\) and has a strictly positive normalized eigenvector: replacing an eigenvector by its entrywise absolute value cannot lower its Rayleigh quotient, and Jacobi irreducibility excludes zeros. Evaluating the form difference on that positive eigenvector shows
\[
\lambda_{\max}(B_{\beta_1})>\lambda_{\max}(B_{\beta_2})>E.
\]
Taking positive square roots proves strict decrease of \(\Gamma\) below one. For \(0<\beta<1\), the sequence \(a_k\) decreases with \(k\), so \(\|T\|=a_0=(c\beta)^{-1/2}\). The triangle and reverse triangle bounds \(a_0-1\le\Gamma\le a_0+1\) prove the asserted \(\beta\downarrow0\) limit. Uniform convergence \(\sup_k|a_k(\beta)-a_k(1)|\to0\) as \(\beta\uparrow1\) gives continuity of the bounded-shift norm and the second limit. This completes the proof.

## Verification
The proof of polynomial density is analytic, and the proof of infinitely many eigenvalues uses arbitrarily many disjoint trial subspaces; neither relies on finite numerical truncation. The accompanying standalone `check.py` uses NumPy and SciPy. Run `python check.py` to verify eight direct finite-section Gram identities, ten spectral samples on both sides of the threshold, and two explicit positive block-quotient certificates. The supplied numerical checks are corroboration only and cannot count infinitely many eigenvalues.

## Relationship to prior work
Dimitrov and Nikolov [1] introduced precisely these Meixner difference constants, proved finite-degree monotonicity in \(\beta\), established the \(\beta=1\) limiting constant, and gave bounds for general sequence inputs. Their Theorem 4.1 represents the finite-degree constants through finite Jacobi matrices. The present claim does not repeat these results: it identifies the *complete limiting parameter threshold*, the strict-to-flat transition, and infinitely many discrete spectral outliers for every \(0<\beta<1\). Polynomial density is supplied as an elementary supporting bridge, not claimed to be historically new. Sasaki's Meixner birth-and-death analysis [2] addresses a different, state-dependent second-order generator, not the singular spectrum of the unweighted forward difference considered here. Standard weighted-shift spectral facts support the compactness step but do not by themselves give the outlier count.

## Limitations
No closed form is proved for \(\Gamma(c,\beta)\) when \(0<\beta<1\), nor for the individual outlier eigenvalues, their spacing, or convergence rates of \(\gamma_n\). The result does not concern other \(\ell^p\) exponents or continuous Meixner-type weights. Possible earlier spectral-theory formulations of the same specialized Jacobi family remain a historical-priority risk; the comparisons are not an independent priority determination.

## References
[1] D. K. Dimitrov and G. P. Nikolov, *A discrete weighted Markov--Bernstein inequality for polynomials and sequences*, first public arXiv submission 2020-07-08, arXiv:2007.04061, https://arxiv.org/abs/2007.04061. Published under a revised title in *Journal of Mathematical Analysis and Applications* 493 (2021), 124522.

[2] R. Sasaki, *Multivariate Meixner polynomials as Birth and Death polynomials*, first public arXiv submission 2023-10-08, arXiv:2310.04968, https://arxiv.org/abs/2310.04968.

[3] *On the spectrum of weighted shifts*, 2022, https://link.springer.com/article/10.1007/s13398-022-01328-z (general weighted-shift context).
