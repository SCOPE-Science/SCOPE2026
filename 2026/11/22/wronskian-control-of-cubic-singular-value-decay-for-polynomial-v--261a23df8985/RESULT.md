# Wronskian control of cubic singular-value decay for polynomial Volterra commutators

## Finding
For each complex polynomial pair \(g,h\), define on \(H^2(\mathbb D)\)
\[
(T_gf)(z)=\int_0^z f(\zeta)g'(\zeta)\,d\zeta,\qquad K=T_gT_h-T_hT_g.
\]
Put \(W(z)=z^3(g''(z)h'(z)-g'(z)h''(z))\) and
\[
J=\frac1{2\pi}\int_0^{2\pi}|W(e^{i\theta})|^{1/3}\,d\theta.
\]
The commutator vanishes if and only if the two polynomial derivatives are linearly dependent. Otherwise \(J>0\) and the decreasing singular values satisfy
\[
\boxed{\lim_{N\to\infty}N^3s_N(K)=J^3.}
\]
In particular \(K\in\mathcal S_p\) exactly for \(p>1/3\), and
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^Ns_j(K)^{1/3}=J.
\]
The nonzero commutator is compact and quasinilpotent, with infinite rank. The formula includes arbitrary complex polynomial coefficients, allowing all cancellations within the Wronskian.

## Assumptions and scope
The Hardy Hilbert space \(H^2(\mathbb D)\) is the analytic power-series space with \(\|\sum_{k\ge0}c_kz^k\|^2=\sum_{k\ge0}|c_k|^2\). Both symbols are arbitrary complex polynomials; their constant terms are immaterial. Singular values \(s_1(K)\ge s_2(K)\ge\cdots\) count multiplicity. The Schatten classes \(\mathcal S_p\) for \(p>0\) use \(\sum s_j^p<\infty\). When a derivative is zero or the derivatives are proportional, \(K=0\) and the positive-coefficient assertions are not invoked. The result does not assert a singular-value law for nonpolynomial symbols.

## Proof
**1. Matrix and exact cancellation.** Identify \(H^2\) with \(\ell^2(\mathbb N_0)\) using \(e_k(z)=z^k\). Write \(g(z)=\sum_{m\ge1}a_mz^m\), \(h(z)=\sum_{n\ge1}b_nz^n\), with finite sums. Direct integration yields
\[
T_ge_k=\sum_{m\ge1}\frac{ma_m}{k+m}e_{k+m}.
\]
Thus each \(T_g\) is a finite sum of shifts with diagonal coefficients tending to zero, hence compact. The \(L\)-th subdiagonal of \(K\), with \(L\ge2\), is
\[
K_{k+L,k}=\sum_{m+n=L}
 \frac{mn(m-n)a_mb_n}{(k+m)(k+n)(k+L)}.
\]
The sum is finite and, uniformly over the finitely many nonzero subdiagonals,
\[
K_{k+L,k}=\frac{w_L}{(k+1)^3}+O((k+1)^{-4}),\quad
w_L=\sum_{m+n=L}mn(m-n)a_mb_n.
\]
By multiplication of derivatives,
\[
\sum_{L\ge2}w_Lz^L=z^3(g''h'-g'h'')=W(z).
\]
If \(W=0\), the rational derivative \((g'/h')'\) vanishes wherever \(h'\ne0\), forcing proportional derivatives; zero derivative cases are immediate. Such operators are proportional and commute. If \(W\ne0\), a subdiagonal has a nonzero leading coefficient, so \(K\ne0\) and has infinite rank.

**2. Weighted finite-band singular-value lemma.** We prove the specific counting principle used here. Let \(\alpha>0\), and let \(B\) have a fixed finite number of subdiagonals with coefficients \(B_{k+L,k}=w_L(k+1)^{-\alpha}\). Write \(w(e^{i\theta})=\sum_Lw_Le^{iL\theta}\). For \(\lambda\downarrow0\), let \(N_B(\lambda)=\#\{j:s_j(B)>\lambda\}\). The assertion is
\[
\lim_{\lambda\downarrow0}\lambda^{1/\alpha}N_B(\lambda)
=\frac1{2\pi}\int_0^{2\pi}|w(e^{i\theta})|^{1/\alpha}\,d\theta.
\]
For completeness, put \(Q=\lambda^{-1/\alpha}\), cut input indices below \(\delta Q\) and above \(RQ\), and let the constants obey \(0<\delta<1<R\). The first piece has rank at most \(\delta Q+O(1)\). The last piece has norm at most \(C(RQ)^{-\alpha}\) (the bound follows by the finite-band Schur estimate), so after choosing \(R\) large it contributes nothing to a counting estimate at any fixed proportional threshold \(\lambda\). Divide the middle indices into finitely many geometric blocks with successive endpoint ratio at most \(1+\eta\). At a block boundary remove at most the bandwidth number of crossing columns; the total discarded rank is independent of \(Q\) when \(\delta,R,\eta\) are fixed. On a block beginning at \(rQ\), replace \((k+1)^{-\alpha}\) by \((rQ)^{-\alpha}\). The replacement has norm at most \(C\eta(rQ)^{-\alpha}\), by the same finite-band bound. The resulting block is a scalar multiple of a finite Toeplitz section with symbol \(w\).

The singular-value distribution of long sections of a finite-band Toeplitz polynomial is \(|w(e^{i\theta})|\) under normalized angular measure. One direct proof observes that all fixed polynomial moments of \(T_M(w)^*T_M(w)\), divided by \(M\), converge to the corresponding angular integrals: expanding each product, only a fixed-width boundary set differs from the bilateral Laurent operator; normalized boundary traces disappear. Uniform norm bounds and polynomial approximation extend moment convergence to all continuous functions on the bounded spectral interval. This supplies the asserted singular-value distribution. The cutoff and replacement errors are controlled by the Weyl inequalities for counting functions at thresholds \((1\pm\varepsilon)\lambda\). Let \(Q\to\infty\), then \(\eta\downarrow0\), \(\delta\downarrow0\) and \(R\uparrow\infty\). The block-counting sum becomes
\[
\frac1{2\pi}\int_0^{2\pi}\int_0^\infty
 \mathbf 1_{\{r^{-\alpha}|w(e^{i\theta})|>1\}}\,dr\,d\theta
=\frac1{2\pi}\int_0^{2\pi}|w(e^{i\theta})|^{1/\alpha}\,d\theta.
\]
The discrepancy of threshold levels \(1\pm\varepsilon\) tends to zero as \(\varepsilon\downarrow0\), using homogeneity. Thus the stated limit follows. If the right-hand side is positive, inversion of monotone counting functions gives
\[
\lim_{N\to\infty}N^\alpha s_N(B)
=\left(\frac1{2\pi}\int_0^{2\pi}|w(e^{i\theta})|^{1/\alpha}\,d\theta\right)^\alpha.
\]

**3. Removing the higher-order remainder.** Let \(B_{k+L,k}=w_L(k+1)^{-3}\) and \(E=K-B\). The expansion in Step 1 gives \(|E_{k+L,k}|\le C(k+1)^{-4}\) for each nonzero subdiagonal. The operator norm of the tail after its first \(M\) input columns is \(O(M^{-4})\), by the finite-band Schur bound, so \(s_{M+1}(E)=O(M^{-4})\). Apply the singular-value inequalities \(s_{j+k-1}(B+E)\le s_j(B)+s_k(E)\) and their reverse versions. Choose \(k=\lfloor j^q\rfloor\), where \(3/4<q<1\). Then \(k=o(j)\) while \(s_k(E)=O(j^{-4q})=o(j^{-3})\). Hence \(j^3s_j(K)\) and \(j^3s_j(B)\) have the same limit, proving the formula with \(\alpha=3\) and \(w=W\).

**4. Spectral consequences.** A nonzero polynomial \(W\) has positive angular \(L^{1/3}\) integral, so \(J>0\). The sharp law is equivalent to \(s_j(K)\sim J^3j^{-3}\), giving Schatten membership exactly for \(p>1/3\); also \(s_j(K)^{1/3}\sim J/j\), hence the logarithmic average. As a compact operator with only strictly positive subdiagonals, \(K\) has no nonzero eigenvalues: if \(Kx=\mu x\) and \(\mu\ne0\), the first nonzero coordinate of \(x\) contradicts the strict lower-triangular matrix relation. Thus the compact spectrum is \(\{0\}\) and \(K\) is quasinilpotent.

## Verification
The finite rational checker in `verify.py` independently implements the compositions and the closed-form subdiagonal identity for multiple polynomial pairs and monomial examples, tests the leading-symbol expansion, and optionally compares finite-matrix singular values against the stated asymptotic. The exact rational calculations passed 4,815 assertions; optional numerical probes passed. These experiments do not establish the infinite singular-value law, which follows from the block-counting argument in Step 2. As an exact check for \(g(z)=z^m\), \(h(z)=z^n\), with distinct positive integers \(m,n\), the nonzero singular values, in decreasing order, are
\[
s_{k+1}(K)=\frac{mn|m-n|}{(k+m)(k+n)(k+m+n)},\qquad k\ge0,
\]
so \(\lim_{j\to\infty}j^3s_j(K)=mn|m-n|\), agreeing with the general Wronskian formula.

## Relationship to prior work
Chalmoukis and Stylogiannis introduce the generalized Volterra framework on coefficient spaces and prove quasinilpotency for individual operators. The present statement instead concerns noncommuting *pairs*, an exact cubic singular-value coefficient for their commutator, and the sharp Schatten threshold. Finite-band Toeplitz singular-value distribution is classical (Böttcher–Grudsky, Chapter 9); its finite-dimensional ingredient is reconstructed in the proof above. The weighted block-counting argument is supplied to justify its distinct nonstationary extension. The claim is not a classification of general analytic-symbol Volterra operators, Dirichlet-series Volterra operators, or their arbitrary commutators.

## Limitations
Only polynomial symbols are treated. The angular coefficient involves an integral, not an elementary closed form for general pairs. The derivation is analytic, and finite numerical matrix comparisons are supplementary, not independent mathematical validation. Earlier specialized or unpublished equivalent results cannot be excluded by database searching alone; priority is not certified. No individual singular-value formula is claimed outside the monomial example.

## References
- N. Chalmoukis and G. Stylogiannis, *Quasi-nilpotency of Generalized Volterra Operators on Sequence Spaces*, Results in Mathematics 76, 173 (2021), https://doi.org/10.1007/s00025-021-01482-7 ; original preprint https://arxiv.org/abs/2005.01660 (first submitted 2020-05-04).
- A. Böttcher and S. M. Grudsky, *Spectral Properties of Banded Toeplitz Matrices*, Chapter 9, *Singular Values*, SIAM (2005), https://doi.org/10.1137/1.9780898717853.ch9 .
- F. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, Monatshefte für Mathematik (2020), https://doi.org/10.1007/s00605-020-01396-6 .
