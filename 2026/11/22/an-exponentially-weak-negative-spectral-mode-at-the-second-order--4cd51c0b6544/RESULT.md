# An exponentially weak negative spectral mode at the second-order Cesàro boundary

## Finding

Let \(M_{\alpha,2}\) be the second-order generalized Cesàro operator on \(\ell^2(\mathbb N_0)\), and let \(B_{\alpha,2}\) be its canonical bounded intertwining operator constructed in [1, Theorem 2.3]. For every real \(0<h<1\), the compact self-adjoint *interrupter defect*
\[
D_h=I-B_{-h,2}^{*}B_{-h,2}
\]
has exactly one negative eigenvalue, of multiplicity one, denoted \(-\kappa(h)\). At the hyponormality boundary it emerges with the exact beyond-all-algebraic-orders law
\[
\boxed{\displaystyle\lim_{h\downarrow0}e^{1/h}\kappa(h)=4e^{\gamma-2}},
\]
where \(\gamma=\lim_{n\to\infty}(\sum_{j=1}^n1/j-\log n)\) is Euler's constant. In particular, \(\kappa(h)=o(h^q)\) for every fixed real \(q>0\).

The *new quantitative assertion* is the exponential scale together with its prefactor. Existence of negative directions and the finite-rank decomposition, from which the one-negative-mode count follows readily at order two, are already implied by [1] and [3]. This is a spectral law for the canonical interrupter \(D_h\), **not** an asymptotic formula for the nonzero negative eigenvalue of the actual self-commutator \(M_{-h,2}^*M_{-h,2}-M_{-h,2}M_{-h,2}^*\).

## Assumptions and scope

The underlying Hilbert space is the complex space \(\ell^2(\mathbb N_0)\), with standard orthonormal basis \((e_n)_{n\ge0}\). For \(\alpha>-1\) and nonnegative integers \(n,j\), the bounded matrix operator is
\[
(M_{\alpha,2})_{nj}=\begin{cases}
\displaystyle\frac{2(n-j+1)}{(n+\alpha+1)(n+\alpha+2)},&0\le j\le n,\\
0,&j>n.
\end{cases}
\]
As in [1, Eqs. (2.1), (2.15)–(2.18)], define on finitely supported sequences
\[
L_{\alpha,2}e_j=\frac{(j+\alpha+1)(j+\alpha+2)}2(e_j-2e_{j+1}+e_{j+2}),
\]
and let \(B_{\alpha,2}\) be the unique bounded extension of \(M_{\alpha,2}^{*}L_{\alpha,2}\). Ma [1] proves this extension exists and satisfies \(B_{\alpha,2}M_{\alpha,2}=M_{\alpha,2}^{*}\). Here \(0<h<1\) and \(\alpha=-h\).

Set for each \(n\ge0\)
\[
 d_n=(n+3-h)(n+4-h),\qquad
 r_n=\frac{4n+10-4h}{d_n},\qquad
 u_n=\frac{n+\frac52+\frac h2}{d_n},\qquad
 w_n=\frac1{d_n},\qquad
 \beta_h=3h(1-h^2).
\]
All denominators and \(r_n\) are positive; \(u,w\in\ell^2\), \(r_n\sim4/n\), \(u_n\sim1/n\) and \(w_n\sim1/n^2\). Rank-one notation \(vv^*\) denotes \(x\mapsto\langle x,v\rangle v\). The spectral eigenvalue \(-\kappa(h)\) is measured relative to the standard Hilbert-space norm, without a hidden normalization of the interrupter.

## Proof

**1. Specialization of the exact defect.** The algebraically proved decomposition of [1, Theorem 2.3] at integer order two gives the bounded-operator identity
\[
\boxed{D_h=R_h-4h\,u_hu_h^*+\beta_h\,w_hw_h^*,\quad R_h=\operatorname{diag}(r_n).}
\]
Indeed, the two coefficients in [1, Eq. (2.18)] are \(4\alpha=-4h\) and \(3\alpha(\alpha^2-1)=3h(1-h^2)\). The corresponding normalized discrete Gram polynomials are \(p_{2,0}(n;\alpha)=n+(5-\alpha)/2\) and \(p_{2,1}=1\), yielding exactly \(u\) and \(w\). Define \(P_h=R_h+\beta_h w_hw_h^*\). It is strictly positive as a quadratic form, and compact: \(r_n\to0\), while the two remaining terms have rank one. The perturbation \(D_h=P_h-4h u_hu_h^*\) has at most one negative eigenvalue, counted with multiplicity.

**2. Exact secular equation and uniqueness.** For \(\kappa>0\), \(P_h+\kappa I\) has a bounded inverse. The rank-one eigenvalue identity implies
\[
 -\kappa\in\sigma_{\mathrm p}(D_h)
 \quad\Longleftrightarrow\quad 4hK_h(\kappa)=1,\qquad
 K_h(\kappa)=\langle u_h,(P_h+\kappa I)^{-1}u_h\rangle.
\]
The associated eigenvector is proportional to \((P_h+\kappa I)^{-1}u_h\), so each negative eigenvalue is simple. Resolvent differentiation yields \(K_h'(\kappa)=-\|(P_h+\kappa I)^{-1}u_h\|_2^2<0\); also \(K_h(\kappa)\to0\) as \(\kappa\to\infty\). The Sherman–Morrison resolvent formula gives
\[
\begin{split}
K_h(\kappa)&=S_h(\kappa)-\frac{\beta_h C_h(\kappa)^2}{1+\beta_h W_h(\kappa)},\\
S_h(\kappa)&=\sum_{n=0}^{\infty}\frac{u_n^2}{r_n+\kappa},\\
C_h(\kappa)&=\sum_{n=0}^{\infty}\frac{u_nw_n}{r_n+\kappa},\qquad
W_h(\kappa)=\sum_{n=0}^{\infty}\frac{w_n^2}{r_n+\kappa}.
\end{split}
\]
For fixed \(h\in(0,1)\), the last two series are uniformly bounded as \(\kappa\downarrow0\), since their terms are respectively \(O(n^{-2})\) and \(O(n^{-3})\). But \(S_h(\kappa)\to\infty\), since \(u_n^2/r_n\sim1/(4n)\). Thus \(K_h(0+)=+\infty\); continuity and strict decrease give exactly one solution \(\kappa(h)>0\) for every \(0<h<1\). Compact self-adjointness rules out any other negative spectrum.

**3. Uniform logarithmic subtraction.** For \(0\le h\le1/2\), as \(n\to\infty\), uniformly in \(h\),
\[
 u_n=\frac1{n+1}+O((n+1)^{-2}),\qquad
 r_n=\frac4{n+1}+O((n+1)^{-2}),\qquad r_n\ge\frac{c}{n+1}
\]
for an absolute \(c>0\). Introduce the explicitly summable comparison
\[
 T(\kappa)=\sum_{n=0}^{\infty}
 \frac{1}{4(n+1)(1+\kappa(n+1)/4)}
 =\frac14\left[\psi\!\left(1+\frac4\kappa\right)+\gamma\right]
 =\frac14\left(\log\frac4\kappa+\gamma\right)+o(1)
\]
as \(\kappa\downarrow0\), where \(\psi\) is the digamma function. To justify passing two limits through the difference, write \(a_n=(n+1)^{-1}\). The inequalities \(|u_n^2-a_n^2|\le C(n+1)^{-3}\) and \(|r_n-4a_n|\le C(n+1)^{-2}\) imply, for all \(\kappa\in[0,1]\), \(h\in[0,1/2]\),
\[
\left|\frac{u_n^2}{r_n+\kappa}-\frac{a_n^2}{4a_n+\kappa}\right|
 \le\frac{C'}{(n+1)^2}.
\]
The finitely many small indices are covered by enlarging the constant. This is an absolutely summable bound independent of both parameters. By dominated convergence,
\[
\lim_{(h,\kappa)\to(0,0)}[S_h(\kappa)-T(\kappa)]
 =\sum_{n=0}^{\infty}\left(\frac{u_{n,0}^2}{r_{n,0}}-\frac1{4(n+1)}\right).
\]
At \(h=0\) we have \(r_{n,0}=4u_{n,0}\) and
\[
 u_{n,0}=\frac{n+5/2}{(n+3)(n+4)}
 =-\frac1{2(n+3)}+\frac3{2(n+4)}.
\]
Therefore the telescoping harmonic-number identity gives
\[
\sum_{n\ge0}\left(u_{n,0}-\frac1{n+1}\right)
 =\frac12H_2-\frac32H_3=-2,
\]
and the displayed limit is exactly \(-1/2\). In addition, for \(h\le1/2\), the series \(C_h,W_h\) are bounded uniformly even at \(\kappa=0\), and \(\beta_h=O(h)\). Consequently
\[
\boxed{K_h(\kappa)=\frac14\left(\log\frac4\kappa+\gamma\right)-\frac12+o(1)}
\]
whenever \(h\downarrow0\) and simultaneously \(\kappa\downarrow0\).

**4. Inversion of the logarithmic singularity.** Since \(K_h(\kappa)\le\|u_h\|_2^2/\kappa\) and \(\|u_h\|_2\) stays bounded for \(h\le1/2\), the exact equation \(K_h(\kappa(h))=1/(4h)\) implies \(\kappa(h)=O(h)\), hence \(\kappa(h)\to0\). Applying Step 3 at this solution gives
\[
\frac1h=\log\frac4{\kappa(h)}+\gamma-2+o(1),
\qquad
\kappa(h)=4e^{\gamma-2}e^{-1/h}(1+o(1)).
\]
The error remains \(o(1)\) after taking logarithms, so exponentiation preserves the multiplicative prefactor. Finally, \(e^{-1/h}=o(h^q)\) for each fixed \(q>0\), completing the assertion. \(\square\)

## Verification

The included pure-standard-library script `check_cesaro.py` checks the order-two columns of \(B=M^*L\) directly from finite matrix multiplication and verifies the exact identity \(D_h=R_h-4hu_hu_h^*+3h(1-h^2)w_hw_h^*\) for every pair of indices in a finite grid and five rational shifts. It performs 1010 exact rational assertions and reports `EXACT_ORDER_TWO_CESARO_INTERRUPTER_OK 1010`. This validates normalization and finite-entry algebra, not the infinite-dimensional spectrum or its asymptotic.

The four analytic checks that prove the infinite statement are: (i) the published bounded-operator decomposition, (ii) monotonicity and divergence of the Birman–Schwinger scalar, (iii) a uniform summable estimate for the digamma-subtracted series, and (iv) the exact harmonic finite-part \(-1/2\). Every limit is along real positive shifts \(h\downarrow0\), and no assertion uses finite truncations as an exhaustive spectral certificate.

## Relationship to prior work

Ma [1] establishes the exact defect identity, positivity for nonnegative shifts, and negative finite-support witnesses for negative shifts, but does not determine any exponentially small spectral eigenvalue or its prefactor. The finite Gram reduction [3] shows that a natural *weighted* lower commutator coefficient is \(-\infty\) for negative shifts; this neither computes nor bounds the ordinary negative eigenvalue of the canonical compact interrupter. The published third-order study [4] proves that an *actual self-commutator* has one negative eigenvalue, but explicitly leaves its magnitude uncomputed; it concerns order three, not the spectral onset in the order-two canonical interrupter. Rhaly [2] studies the order-two generalized Cesàro operator and a different positive interrupter pair, without the sharp negative spectral onset. A known Carleman rank-one perturbation law [5] also has an exponential weak-coupling eigenvalue, but its continuous-spectrum kernel, secular equation, coupling normalization and coefficient differ; the result does not imply the present formula.

## Limitations

The theorem concerns only the uniquely specified canonical interrupter \(I-B_{\alpha,2}^*B_{\alpha,2}\) from [1], not arbitrary positive factors, alternate interrupters or the nonzero eigenvalue of the actual self-commutator. It is specific to integer order two and a real negative parameter approaching zero. It does not assert an analogous law for higher orders or nonreal shifts. The finite diagnostic is not a proof of the limiting eigenvalue, and absence of a matching result in inspected sources cannot exclude every unindexed equivalent statement. Independent external validation has not been performed.

## References

[1] Y. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (public submission listed 18 September 2026), esp. Theorem 2.3 and Section 7. https://arxiv.org/abs/2610.00193 ; accessible full text https://borowiecki.dev/pdf/2610.00193

[2] H. C. Rhaly Jr., *Supraposinormality and hyponormality for the generalized Cesàro matrices of order two*, arXiv:1602.01408v1 (2016), Sections 2–3. https://arxiv.org/abs/1602.01408

[3] *Finite Gram reduction of sharp Cesàro self-commutator bounds at every order*, published mathematical research record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-finite-gram-reduction-of-sharp-ces-ro-self-commutator-bounds-at--2747cc29070a

[4] *Exactly one negative eigenvalue for third-order shifted Cesàro self-commutators*, published mathematical research record, 17 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exactly-one-negative-eigenvalue-for-third-order-shifted-ces-ro-s--88dd990f36ce

[5] *Opposite weak-coupling scales for a rank-one exponential perturbation of the Carleman operator*, published mathematical research record, 18 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-opposite-weak-coupling-scales-for-a-rank-one-exponential-perturb--b7b5ef288886
