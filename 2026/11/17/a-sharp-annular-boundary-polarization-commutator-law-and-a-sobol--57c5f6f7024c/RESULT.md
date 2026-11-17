# A sharp annular boundary-polarization commutator law and a Sobolev criterion

## Finding
Let \(H_r^2\) be the Hardy space of the annulus \(\{z:r<|z|<1\}\) with equal normalized arclength measure on the inner and outer boundary circles. For an essentially bounded angular function \(a\in L^\infty(\mathbb T)\), let \(T_{a,r}\) be the Toeplitz operator whose symbol is \(a(e^{i\theta})\) on both circles. Let \(D_r\) be the Toeplitz compression of the indicator of the outer circle. Then for each \(0<r<1\),
\[ [D_r,T_{a,r}]\in\mathcal S_2. \]
Writing \(\widehat a(k)=(2\pi)^{-1}\int_0^{2\pi}a(e^{i\theta})e^{-ik\theta}\,d\theta\), the sharp extended-real limit is
\[
\boxed{\lim_{r\uparrow1}\frac{\|[D_r,T_{a,r}]\|_{\mathcal S_2}^2}{|\log r|}=\frac13\sum_{k\in\mathbb Z}k^2|\widehat a(k)|^2\in[0,+\infty].}
\]
In particular, the normalized energy has a finite limit exactly for angular symbols in the periodic Sobolev space \(H^1(\mathbb T)\). For every \(a\in L^\infty(\mathbb T)\cap H^1(\mathbb T)\) and every \(0<r<1\),
\[
\boxed{\|[D_r,T_{a,r}]\|_{\mathcal S_2}^2\le\frac{|\log r|}{3}\|a'\|_{L^2(\mathbb T)}^2.}
\]
The squared derivative norm uses normalized angular Lebesgue measure. The constant \(1/3\) is optimal over all annular radii and bounded Sobolev symbols: for the single Fourier mode \(a(e^{i\theta})=e^{i\theta}\), the ratio of the two sides tends to one as \(r\uparrow1\).

## Assumptions and scope
Use the Hilbert-space norm
\[
\|f\|_{H_r^2}^2=\frac{1}{2\pi}\int_0^{2\pi}\bigl(|f(e^{i\theta})|^2+|f(re^{i\theta})|^2\bigr)\,d\theta.
\]
The normalized Laurent basis is \(e_n(z)=z^n/(1+r^{2n})^{1/2}\), \(n\in\mathbb Z\). Toeplitz operators are orthogonal compressions of bounded multiplication operators on the two-circle boundary space. In particular, \(D_r=T_{\mathbf1_{\{|z|=1\}}}\) is a positive contraction but not an orthogonal projection on \(H_r^2\). The function \(a\) need not be continuous, differentiable, or Sobolev for the general extended-real limit. For the upper bound, the derivative \(a'\) is the weak angular derivative. The exponent \(\mathcal S_2\) is the Hilbert–Schmidt class.

## Proof
**1. Exact two-circle Fourier matrix.** Put \(h=-\log r>0\) and \(d(t)=(1+e^{-2t})^{-1}\). The outer-boundary compression is diagonal in the Laurent basis, with \(D_re_n=d(hn)e_n\). Since both boundary symbols of \(T_{a,r}\) coincide, its matrix element from \(e_n\) to \(e_{n+k}\) is \(\widehat a(k)u_{n,k}(h)\), where
\[
u_{n,k}(h)=\frac{1+e^{-h(2n+k)}}{\sqrt{(1+e^{-2hn})(1+e^{-2h(n+k)})}}.
\]
The two-dimensional Cauchy–Schwarz inequality applied to \((1,e^{-hn})\) and \((1,e^{-h(n+k)})\) gives \(0<u_{n,k}(h)\le1\). Therefore
\[
\langle[D_r,T_{a,r}]e_n,e_{n+k}\rangle=\widehat a(k)u_{n,k}(h)\bigl(d(h(n+k))-d(hn)\bigr).
\]
Consequently, once the Hilbert–Schmidt property is known, its exact norm is the nonnegative Fourier series
\[
\|[D_r,T_{a,r}]\|_{\mathcal S_2}^2=\sum_{k\in\mathbb Z}|\widehat a(k)|^2 F_h(k),\quad
F_h(k)=\sum_{n\in\mathbb Z}u_{n,k}(h)^2\bigl(d(h(n+k))-d(hn)\bigr)^2.
\]

**2. Hilbert–Schmidt membership even for rough bounded symbols.** Write \(P\) for the ambient Hardy projection, \(Q=I-P\), \(B=M_{\mathbf1_{\{|z|=1\}}}\), and \(A=M_a\), the latter acting with identical angular symbols on both boundary components. Their ambient multiplication operators commute, and \(B^2=B\). Restricting to the Hardy subspace gives the exact identity
\[
[D_r,T_{a,r}]=PAQBP-PBQAP.
\]
Now \(QBP\) is Hilbert–Schmidt because
\[
\|QBP\|_{\mathcal S_2}^2=\operatorname{Tr}(D_r-D_r^2)
=\sum_{n\in\mathbb Z}d(hn)(1-d(hn))<\infty;
\]
the summands decay exponentially in \(|n|\) for every fixed \(h>0\). The adjoint \(PBQ\) is likewise Hilbert–Schmidt, and multiplication by \(a\) is bounded. Thus the commutator is Hilbert–Schmidt without any smoothness assumption on \(a\), justifying the Fourier identity above.

**3. The all-radius sharp bound.** For a positive integer \(k\), denote \(d_n=d(hn)\). Telescoping \(d_{n+k}-d_n=\sum_{j=0}^{k-1}(d_{n+j+1}-d_{n+j})\) and using the triangle inequality in \(\ell^2(\mathbb Z)\) give
\[
F_h(k)\le\sum_n(d_{n+k}-d_n)^2\le k^2\sum_n(d_{n+1}-d_n)^2.
\]
By Cauchy–Schwarz on each interval \([hn,h(n+1)]\),
\[
\sum_{n\in\mathbb Z}(d_{n+1}-d_n)^2\le h\int_{\mathbb R}|d'(t)|^2\,dt.
\]
Since \(d'(t)=\frac12\operatorname{sech}^2t\) and \(\int_{\mathbb R}\operatorname{sech}^4t\,dt=4/3\), the integral is exactly \(1/3\). Also \(F_h(-k)=F_h(k)\) after reindexing and \(F_h(0)=0\). Therefore \(0\le F_h(k)\le hk^2/3\) for every \(h>0\) and integer \(k\). Inserting this into the exact Fourier sum and applying Parseval for the Sobolev derivative proves the asserted uniform inequality.

**4. Sharp thin-annulus asymptotics.** Fix an integer \(k\). On each compact interval in the rescaled lattice variable \(t=hn\), as \(h\downarrow0\), one has uniformly \(u_{n,k}(h)\to1\) and \((d(h(n+k))-d(hn))/h\to k d'(t)\). Both the difference quotients and their squared values have exponentially decaying tails in \(|hn|\), uniformly for small \(h\), because \(d'\) is exponentially decaying. Riemann summation and tail control consequently give
\[
\lim_{h\downarrow0}\frac{F_h(k)}h=k^2\int_{\mathbb R}|d'(t)|^2\,dt=\frac{k^2}{3}.
\]
For \(a\in H^1\), the uniform bound \(F_h(k)/h\le k^2/3\) permits dominated convergence over all Fourier modes. For \(a\notin H^1\), Fatou's lemma applied to the nonnegative Fourier series yields a lower limit of \(+\infty\); hence the extended-real limit is \(+\infty\). For the mode \(a(e^{i\theta})=e^{i\theta}\), only \(k=1\) contributes, so \(F_h(1)/h\to1/3\), proving optimality of the numerical constant.

## Verification
The exact formula is derived from orthonormal Laurent matrix elements, independently of asymptotic numerics. The logistic derivative normalization \(\int_{\mathbb R}|d'|^2=1/3\) is evaluated by the substitution \(y=\tanh t\). The finite-radius Hilbert–Schmidt assertion is proved by a trace-class factorization, not inferred from a finite matrix truncation. The limiting formula follows by a dominated Riemann-sum argument for each Fourier mode and then dominated convergence or Fatou's lemma for arbitrary bounded angular symbols. Numerical evaluations at several radii and Fourier modes are compatible with the coefficient \(1/3\), but no finite computation is used as a proof of the infinite-frequency statement.

## Relationship to prior work
Adhikari and Das (2026) supply the annular Hardy-space Toeplitz framework and algebraic Brown–Halmos characterization. Their main theorems concern multiplicativity and zero products, not this sharp boundary-component commutator energy. The published thin-annulus spectral law for analytic Laurent multipliers (published-finding corpus, November 2026) concerns the **positive self-commutator of multiplication by a Laurent polynomial**, a different operator whose Schatten profile depends on the multiplier derivative; it does not entail the present all-radius sharp mixed commutator inequality or the iff Sobolev criterion for arbitrary bounded angular symbols. The published harmonic power-Fock angular Sobolev leakage law concerns an entirely different projection and a logarithmic finite-index truncation; its conclusion cannot be applied to this two-circle Hardy projection and continuous annular pinching. Tattersall's 2015 thesis establishes annular Hardy context and investigates eigenfunctions of Toeplitz operators; the available introductory material supplies no direct quantitative bound, but its complete contents were not checked for every possible equivalent formulation.

## Limitations
The theorem applies to equal normalized masses on the two boundary circles and **the same angular function on both components**. It does not establish analogous constants for unequal boundary weights, independent boundary symbols, other Schatten exponents, or a rate uniform over the entire Sobolev unit ball. The originality comparison is based on the named accessible primary works and mathematical-record searches; equivalent older results may exist under a different operator-ideal or projection nomenclature. Independent validation and exhaustive publication-priority review have not been performed.

## References
1. S. Adhikari and S. Das, *Algebraic properties of Toeplitz operators on annulus and multiply connected domains*, arXiv:2611.01717v1 (first submitted 2026-11-01), https://arxiv.org/html/2611.01717v1.
2. A. Broschinski, *Eigenvalues of Toeplitz Operators on the Annulus and Neil Algebra*, arXiv:1303.3314 (2013), https://arxiv.org/abs/1303.3314.
3. J. M. Tattersall, *Toeplitz and Hankel operators on Hardy spaces of complex domains*, doctoral thesis, University of Leeds (2015), https://etheses.whiterose.ac.uk/id/eprint/11498/.
4. *Half-Schatten perimeter law and spectral Weyl profile for pinching annular Hardy multipliers*, published research result (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-schatten-perimeter-law-and-spectral-weyl-profile-for-pinchi--afd674958865.
5. *The sharp angular Sobolev leakage law for harmonic power-Fock projections*, published research result (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-sharp-angular-sobolev-leakage-law-for-harmonic-power-fock-pr--afadf5723e21.
