# Universal signed spectral boundary layer for monomial differentiation–composition self-commutators

## Finding
For each integer \(m\ge2\), real \(s\), and \(h>0\), let \(\mathcal H_s\) be the Hilbert space of analytic functions \(f(z)=\sum_{n\ge0}a_nz^n\) on the unit disk with
\[
\|f\|_s^2=|a_0|^2+\sum_{n\ge1}n^s|a_n|^2<\infty.
\]
Define the compact composition–differentiation operator \(D_{m,h}f(z)=f'(e^{-h}z^m)\) and its trace-class self-commutator
\[
K_{m,s,h}=D_{m,h}^*D_{m,h}-D_{m,h}D_{m,h}^*.
\]
The adjoints are taken with respect to the exact displayed Hilbert norm. Define the two continuous spectral profiles
\[
A_{m,s}(x)=m^s x^2e^{-2x},\qquad
B_{m,s}(x)=m^s x^2e^{-2x}-m^{s-2}x^2e^{-2x/m}
\quad (x\ge0).
\]

**Two-branch signed spectral law.** In the normalized monomial basis \(e_0=1\), \(e_n=z^n/n^{s/2}\) for \(n\ge1\), let \(d_k(h)=\langle K_{m,s,h}e_k,e_k\rangle\). For every continuous function \(F(x,y)\) compactly supported in the first coordinate \(x\ge0\),
\[
\boxed{\lim_{h\downarrow0}h\sum_{k\ge0}F(hk,h^2d_k(h))
=\frac{m-1}{m}\int_0^\infty F(x,A_{m,s}(x))\,dx
+\frac1m\int_0^\infty F(x,B_{m,s}(x))\,dx.}
\]
This is a local spectral counting law in monomial degree, not a finite-dimensional eigenvalue approximation. The first branch is positive for \(x>0\); the second changes sign *exactly once*, at
\[
\boxed{x_*(m)=\frac{m\log m}{m-1},}
\]
independently of \(s\). In particular, for every fixed \(h>0\), the compact self-commutator has infinitely many strictly positive and infinitely many strictly negative eigenvalues; the associated operator is neither hyponormal nor cohyponormal.

**All Schatten exponents.** For every fixed \(p>0\), with the standard Schatten quasi-norm when \(p<1\),
\[
\boxed{\lim_{h\downarrow0}h^{2p+1}\|K_{m,s,h}\|_{\mathcal S_p}^{p}
=\frac{m-1}{m}\int_0^\infty A_{m,s}(x)^p\,dx
+\frac1m\int_0^\infty|B_{m,s}(x)|^p\,dx.}
\]
Also,
\[
\boxed{\lim_{h\downarrow0}h^2\|K_{m,s,h}\|=m^s e^{-2}.}
\]
The trace-norm coefficient is elementary. Writing \(\xi=x_*(m)\),
\[
\boxed{\lim_{h\downarrow0}h^3\|K_{m,s,h}\|_{\mathcal S_1}
=2m^{s-1}(m-1)e^{-2\xi}
\left(\frac{\xi^2}{2}+\frac{(m+1)\xi}{2}+\frac{m^2+m+1}{4}\right).}
\]
The squared Hilbert–Schmidt coefficient likewise has the exact closed form
\[
\boxed{\lim_{h\downarrow0}h^5\|K_{m,s,h}\|_{\mathcal S_2}^2
=\frac{3m^{2s}}{64}-\frac{3m^{2s+2}}{2(m+1)^5}.}
\]

## Assumptions and scope
The degree \(m\ge2\) and coefficient exponent \(s\in\mathbb R\) are fixed while \(h\downarrow0\). All functions are complex analytic on the disk; the Hilbert norm is specified exactly and is not interchangeable with an equivalent norm when computing adjoints. The classical Dirichlet space occurs at \(s=1\), and Hardy space at \(s=0\). In the local spectral law, compact support is required only in the nonnegative degree variable \(x\), and the test function is continuous in both arguments. Schatten exponents \(p>0\) are fixed (not varying with \(h\)). The fixed-parameter operator is compact and has summable singular values of every positive order; its commutator is self-adjoint and trace class.

## Proof
**1. Exact monomial action and trace-class diagonal.** The monomials above are an orthonormal basis. Direct differentiation gives \(D_{m,h}e_0=0\), \(D_{m,h}e_1=e_0\), and for every integer \(n\ge2\),
\[
D_{m,h}e_n=n^{1-s/2}[m(n-1)]^{s/2}e^{-h(n-1)}e_{m(n-1)}.
\]
All nonzero images are mutually orthogonal and have distinct target degrees. Set \(w_0^2=0\), \(w_1^2=1\), and
\[
w_n^2=m^s n^{2-s}(n-1)^s e^{-2h(n-1)}\quad(n\ge2).
\]
Then \(D_{m,h}^*D_{m,h}\) has diagonal \((w_k^2)_{k\ge0}\), whereas \(D_{m,h}D_{m,h}^*\) has the value \(1\) at degree zero, the value \(w_{j+1}^2\) at degree \(mj\) for \(j\ge1\), and zero elsewhere. Consequently, the **complete exact** commutator diagonal is
\[
d_0(h)=-1,\qquad d_k(h)=w_k^2-\mathbf1_{m\mid k}\,w_{k/m+1}^2\quad(k\ge1).
\]
The exponential factor makes \(\sum_{k\ge1}w_k^2<\infty\), for any real \(s\). Hence \(D_{m,h}\) is Hilbert–Schmidt and \(K_{m,s,h}\) is trace class, with \(\operatorname{Tr}K_{m,s,h}=0\) because the two Gram operators have the same trace. In fact the exact finite cutoff identity, for integers \(N\ge m\), is
\[
\sum_{k=0}^{N}d_k(h)=\sum_{n=\lfloor N/m\rfloor+2}^{N}w_n^2.
\]
This tail tends to zero as \(N\to\infty\) at fixed \(h>0\).

**2. Signs.** For every positive index \(k\) not divisible by \(m\), \(d_k(h)=w_k^2>0\). Along multiples \(k=mj\), \(j\to\infty\), the quotient \(w_{mj}^2/w_{j+1}^2\sim m^2e^{-2h((m-1)j-1)}\to0\). Thus all sufficiently large such indices have \(d_{mj}(h)<0\), proving infinite inertia of both signs for each \(h>0\). The identity \(B_{m,s}(x)=m^sx^2e^{-2x}[1-m^{-2}e^{2x(1-1/m)}]\) shows its unique positive root is \(x_*(m)\) and establishes the stated sign pattern and its independence from \(s\).

**3. Local two-branch limit.** On compact positive intervals in the scaled variable \(x=hk\),
\[
h^2w_k^2\longrightarrow A_{m,s}(x)
\]
uniformly whenever \(hk\to x\), while for multiples \(k=mj\),
\[
h^2w_{j+1}^2\longrightarrow m^{s-2}x^2e^{-2x/m}.
\]
For a compact interval of \(x\) away from zero, the convergence is uniform by expanding the finite factors \(k/(k-1)\) and replacing \(h(k-1)\) with \(hk+O(h)\). Near \(x=0\), boundedness of the scaled coefficients (with finitely many low indices contributing \(O(h)\) to the test sum) suffices. Separate the arithmetic progressions \(k\equiv0\pmod m\) and \(k\not\equiv0\pmod m\). The mesh is \(mh\) for each progression; right-endpoint Riemann sums converge to the two integrals, weighted by the respective natural densities \(1/m\) and \((m-1)/m\). This proves the displayed local spectral law, including the boundary at zero by approximation.

**4. Schatten limits and norm edge.** The scalar quantities \(h^2w_k^2\), for \(k\ge2\), are bounded by \(C_{m,s}(hk)^2e^{-hk}\), uniformly for all sufficiently small \(h\). On the progression \(k=mj\), the term \(h^2w_{j+1}^2\) has a bound of the form \(C_{m,s}(hk)^2e^{-hk/m}\). The finitely many smallest indices make a vanishing contribution after multiplication by \(h\). Thus the \(p\)-th powers of all scaled diagonal entries have uniformly summable exponential tails for every fixed \(p>0\). Apply the two-progression Riemann argument of Step 3 on bounded intervals and then discard the tails uniformly to obtain the Schatten \(p\)-formula. No triangle inequality in the quasi-norm range is used because the operator is exactly diagonal.

Both nonnegative functions \(A_{m,s}\) and \(C_{m,s}(x):=m^{s-2}x^2e^{-2x/m}\) have the same global maximum \(m^se^{-2}\), reached at \(x=1\) and \(x=m\), respectively. Their difference \(B_{m,s}=A_{m,s}-C_{m,s}\) satisfies \(|B_{m,s}|\le\max(A_{m,s},C_{m,s})\le m^se^{-2}\). Nonmultiples of \(m\) with \(hk\to1\) achieve the latter upper bound asymptotically. Compact-interval convergence and the preceding uniform tail estimates justify taking the supremum and give the operator-norm limit.

**5. Exact trace and Hilbert–Schmidt constants.** Since the trace is zero and negative spectral mass for the limiting profiles comes only from the multiples branch, the \(p=1\) formula reduces to
\[
\frac2m\int_{\xi}^\infty (C_{m,s}(x)-A_{m,s}(x))\,dx,
\qquad\xi=\frac{m\log m}{m-1}.
\]
Use \(\int_\xi^\infty x^2e^{-a x}\,dx=e^{-a\xi}(\xi^2/a+2\xi/a^2+2/a^3)\) and \(e^{-2\xi/m}=m^2e^{-2\xi}\). Elementary simplification gives the asserted \(\mathcal S_1\) coefficient. For \(p=2\), expand \((A-C)^2\) in the two-branch integral and evaluate the three gamma integrals using \(\int_0^\infty x^4e^{-a x}\,dx=24/a^5\). The result is exactly \(3m^{2s}/64-3m^{2s+2}/(2(m+1)^5)\), as displayed. Both constants are positive for all allowed parameters.

## Verification
Run `python3 checker.py` using only the Python standard library. It constructs finite monomial-action matrices, independently forms both Gram diagonals, and verifies their agreement with the asserted exact self-commutator entries across degrees and Hilbert indices. It additionally checks finite spectral trace, Hilbert–Schmidt and operator-norm scaling on shrinking parameter grids and confirms the predicted sign frontier. The expected report is `PASS 2304 finite exact-structure and numerical diagnostic comparisons; limits are proved analytically`. The finite matrix and numerical tests are supplementary; Steps 1–5 establish all infinite-dimensional and asymptotic quantifiers.

## Relationship to prior work
Allen–Heller–Pons [1, Section 6] study \(f'\circ\varphi\) on the Dirichlet space and give exact norms and spectrum for monomial \(\varphi(z)=az^m\). Their monomial action is the starting point for the exact adjoint-diagonal computation here; their displayed results do not give a self-commutator spectral distribution, sign frontier or sharp trace-norm boundary coefficient. Abdollahi–Mehrangiz [2, Theorem 4.1] calculate self-commutators of the **ordinary composition** operators \(f\mapsto f(z^m)\) on the classical Dirichlet space: their commutator is a noncompact multiple of an orthogonal projection, unlike the trace-class signed self-commutator of \(f\mapsto f'(e^{-h}z^m)\) here. The published arithmetic Dirichlet composition findings [3] concern that ordinary composition map and its coefficient-weighted variants; the published differentiation–dilation spectral-edge findings [4,5] involve symbols \(z^r f^{(k)}(az)\), whose output degree is a *fixed translate* of the input degree rather than the multiplicative degree map present here. Likewise the compact composition–adjoint product [6] is a different partial permutation with purely geometric weights. The two-branch signed distribution and explicit trace coefficient are assessed as a distinct natural invariant, not as a general theorem on arbitrary weighted partial permutations.

## Limitations
The profile is proved only for strict radial contractions in a fixed monomial of degree \(m\ge2\), with the normalized coefficient Hilbert scale shown, and fixed real \(s\). It does not cover general nonlinear symbols, simultaneous variable degrees, the nondamped endpoint \(h=0\), or variable Schatten exponents. This is a specialization using arithmetic-progression Riemann sums rather than a new general spectral-distribution method. Complete historical priority cannot be certified from indexed sources: a general theorem on diagonally weighted partial permutations could imply the specialization, and such unindexed coverage remains a residual risk. The proof is analytic and has not been independently validated.

## References
1. R. F. Allen, K. C. Heller and M. A. Pons, *Composition-differentiation operators on the Dirichlet space*, arXiv:2207.09015v1, first posted 19 July 2022; especially Section 6. https://arxiv.org/abs/2207.09015
2. A. Abdollahi and S. Mehrangiz, *Self-Commutators of Composition Operators with Monomial Symbols on the Dirichlet Space*, Abstract and Applied Analysis (2011), article 618968, Theorem 4.1. https://doi.org/10.1155/2011/618968
3. *Weak-trace spectral defect of power composition on Dirichlet-type Hilbert scales*, published published-finding corpus finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-weak-trace-spectral-defect-of-power-composition-on-dirichlet-typ--a8e9d1ae552d
4. *A theta-function spectral-edge transition for monomial Dirichlet composition–differentiation operators*, published published-finding corpus finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-theta-function-spectral-edge-transition-for-monomial-dirichlet--0d3a36fdff0e
5. *Two-scale singular-spectrum law for polynomially weighted Dirichlet dilations*, published published-finding corpus finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-scale-singular-spectrum-law-for-polynomially-weighted-dirich--30feb1a39297
6. *Two-ideal spectral rigidity for damped monomial composition–adjoint products*, published published-finding corpus finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-ideal-spectral-rigidity-for-damped-monomial-composition-adjo--ba7c08a56403
