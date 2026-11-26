# Four-orbit essential norms of analytic Bergman slant commutators

## Finding
Let \(A^2(\mathbb D)\) be the classical Bergman Hilbert space with normalized area measure. Define \(W z^{2n}=z^n\) and \(W z^{2n+1}=0\) for all integers \(n\geq0\), and write \(B_f=WT_f\), where \(T_f\) is the Bergman Toeplitz operator. For arbitrary analytic symbols \(f,g\) in the disk algebra \(A(\mathbb D)\), put
\[
P(z)=g(z)f(z^2)-f(z)g(z^2).
\]
The commutator has the **exact essential norm**
\[
\boxed{\|[B_f,B_g]\|_{\mathrm{ess}}=
\max_{|\zeta|=1}\left(\sum_{k=0}^{3}|P(i^k\zeta)|^2\right)^{1/2}.}
\]
Here \([B_f,B_g]=B_fB_g-B_gB_f\) and the essential norm is the distance, in operator norm, to the compact operators. In particular, the commutator is compact precisely when \(f\) and \(g\) are linearly dependent over \(\mathbb C\). The qualitative commutativity conclusion is established in earlier literature; the quantitative four-orbit formula is the finding.

For polynomials \(P(z)=\sum_{t\geq0}p_tz^t\), define four finite polynomials
\[
Q_r(z)=\sum_{\substack{t\geq0\\t+r\equiv0\pmod4}}p_tz^{(t+r)/4},\qquad r=0,1,2,3.
\]
Then the equivalent exact finite optimization is
\[
\|[B_f,B_g]\|_{\mathrm{ess}}
=2\max_{|z|=1}\left(\sum_{r=0}^{3}|Q_r(z)|^2\right)^{1/2}.
\]
The four-orbit formula also gives an exact evaluation for nonpolynomial disk-algebra symbols, by taking their continuous boundary values.

## Assumptions and scope
The Hilbert-space basis is \(e_n(z)=\sqrt{n+1}z^n\), for \(n\geq0\). The operator \(W\) is defined on all analytic polynomials by the displayed monomial action and extends boundedly to Bergman space with norm \(\sqrt2\). Every \(f\in A(\mathbb D)\) is bounded and analytic in the unit disk, continuous on its closure, so \(T_f\) acts as multiplication by \(f\). The statement applies to every pair \(f,g\) in this class, including zero symbols, constants and dependent pairs. The maximum is taken over a compact unit circle. No assertion is made for general measurable or polyanalytic symbols.

## Proof
**1. Exact commutator identity.** For every analytic multiplier \(f\) one has \(M_fW=WM_{f(z^2)}\) on monomials and hence, by boundedness and density, on Bergman space. Therefore
\[
B_fB_g=W^2M_{f(z^2)g},\qquad [B_f,B_g]=W^2M_P.
\]
This basic product identity is already used in the earlier qualitative commutativity literature. The new step is to evaluate its essential norm exactly.

**2. A compactly equivalent four-fold decimation.** First assume \(P\) is a polynomial. In the normalized Bergman basis,
\[
W^2M_Pe_n=
\sum_{\substack{t\geq0\\n+t\equiv0\pmod4}}
 p_t\sqrt{\frac{n+1}{(n+t)/4+1}}\ e_{(n+t)/4}.
\]
Let \(L_P\) denote the unweighted decimation with the same matrix pattern:
\[
L_Pe_n=\sum_{\substack{t\geq0\\n+t\equiv0\pmod4}}p_t e_{(n+t)/4}.
\]
For fixed \(t\), the coefficient in the first display is \(2\sqrt{(n+1)/(n+t+4)}\), which converges to \(2\) as \(n\) tends to infinity. The map corresponding to fixed \(t\) sends distinct permitted input indices to distinct output indices. Consequently its difference from twice its unweighted version is compact: it is a weighted partial shift whose coefficients tend to zero. A polynomial has only finitely many such terms, so
\[
W^2M_P-2L_P\ \text{is compact},\qquad
\|[B_f,B_g]\|_{\mathrm{ess}}=2\|L_P\|_{\mathrm{ess}}.
\]

**3. The row-multiplier norm is its essential norm.** Identify the input coefficient space unitarily with a fourfold Hardy space by grouping the sequences with indices \(4j+r\), for \(r=0,1,2,3\). Identify the output coefficient space with one Hardy space. Under these identifications, \(L_P\) is the analytic row multiplication operator
\[
M_Q:(F_0,F_1,F_2,F_3)\longmapsto\sum_{r=0}^{3}Q_rF_r.
\]
Boundary-value Cauchy--Schwarz gives
\[
\|M_Q\|\le\max_{|z|=1}\left(\sum_r|Q_r(z)|^2\right)^{1/2}.
\]
Conversely, let \(k_w(z)=\sqrt{1-|w|^2}/(1-\overline wz)\) be a normalized Hardy reproducing kernel. Then \(k_w\) tends weakly to zero as \(|w|\) tends to one, and
\[
\|M_Q^*k_w\|^2=\sum_r|Q_r(w)|^2.
\]
For every compact \(K\), \(\|K^*k_w\|\) tends to zero. Approaching a boundary point where the displayed row-norm maximum occurs proves the reverse essential-norm inequality. Thus
\[
\|M_Q\|_{\mathrm{ess}}=\|M_Q\|=
\max_{|z|=1}\left(\sum_r|Q_r(z)|^2\right)^{1/2}.
\]

**4. Four-point Fourier identity.** Let \(\omega=i\). For each unit \(\zeta\), split \(P\) into its four Taylor-coefficient residue classes. The discrete Fourier transform on the orbit \(\{\zeta,\omega\zeta,\omega^2\zeta,\omega^3\zeta\}\), together with Parseval, gives
\[
\sum_{k=0}^{3}|P(i^k\zeta)|^2
=4\sum_{r=0}^{3}|Q_r(\zeta^4)|^2.
\]
As \(\zeta\) traverses the circle so does \(\zeta^4\); combining this identity with Steps 2--3 proves the claimed formula for polynomials.

**5. Extension to the disk algebra.** Given \(f,g\in A(\mathbb D)\), approximate each uniformly on the closed disk by analytic polynomials. Since \(\|B_f\|\le\sqrt2\|f\|_{\infty}\), their commutators converge in operator norm. The corresponding defect functions converge uniformly, and the four-orbit maximum is continuous under uniform convergence. The polynomial identities therefore pass to the limit without any assumption about absolute summability of Taylor coefficients. Equivalently, the four row symbols are well-defined disk-algebra functions, since taking each residue class is an average over the four rotations.

**6. Zero-defect rigidity.** The four-orbit maximum vanishes exactly when \(P\equiv0\). If neither symbol is zero, the meromorphic ratio \(h=f/g\) satisfies \(h(z^2)=h(z)\) near the origin. Comparing its leading Laurent term forces order zero, and comparing the smallest nonconstant Taylor coefficient forces that coefficient to vanish. Thus \(h\) is constant near zero and by analytic continuation is constant wherever defined. Hence \(f\) and \(g\) are proportional; the converse is immediate. This establishes the stated qualitative corollary independently but does not claim it as new.

## Verification
A standalone script `verify.py` constructs finite matrices for polynomial symbols in the normalized Bergman basis and checks the exact commutator entries against the decimation formula; it also checks the four-point Parseval identity and the monomial special cases. It passed **5,444** supplementary numerical and algebraic comparisons, including random complex-coefficient polynomials of degree at most five. Finite matrices are only finite checks: the universal compact-perturbation, multiplier essential-norm and disk-algebra extension arguments above supply the infinite-dimensional proof. To reproduce, run `python verify.py` with NumPy installed. The full text and script are included together in this package.

For example, \(f(z)=1\) and \(g(z)=z+z^4\) give \(P(z)=z+z^4-z^2-z^8\). The nonzero polyphase terms are \(Q_0(z)=z-z^2\), \(Q_2(z)=-z\), and \(Q_3(z)=z\), so
\[
\|[B_1,B_{z+z^4}]\|_{\mathrm{ess}}=2\sqrt6.
\]
This displays phase interaction not captured by listing monomial norms separately.

## Relationship to prior work
Liu and Lu (2013, Theorem 17) characterized commuting analytic-symbol slant Toeplitz operators on Bergman space. Zhang (2025, Lemma 2.3) wrote down the analytic multiplier--slant intertwining identity used in Step 1. Cui, Li and Lu (2026, Theorem 2.5 and Corollary 2.6) established broader qualitative commutativity and finite-rank rigidity for polyanalytic symbols. Earlier work on essential commutativity and monomial examples supplies qualitative and special-case results. None of the inspected main results provides the present exact four-boundary-orbit formula for all disk-algebra pairs; the equality identifies the Calkin norm, not merely whether it vanishes. The standard Hardy row-multiplier computation in Steps 3--4 is credited as a tool rather than claimed to be a new general theorem.

## Limitations
The statement concerns the specified classical Bergman normalization and analytic disk-algebra symbols. The matrix proof does not extend without modification to symbols with negative Fourier frequencies, other Bergman weights or unbounded analytic symbols. No exact ordinary operator norm, essential spectrum, Schatten behavior or finite-rank approximation-number profile is claimed. Publication priority cannot be proved by finite literature searches; unindexed norm results and less-accessible older slant Toeplitz literature remain possible equivalence risks. Independent external validation has not been performed.

## References
1. P. Cui, R. Li and Y. Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1 (first submitted 7 October 2026), https://arxiv.org/html/2610.09728v1 .
2. C. Liu and Y. Lu, *Product and Commutativity of kth-Order Slant Toeplitz Operators*, Abstract and Applied Analysis (2013), article 473916, https://doi.org/10.1155/2013/473916 .
3. H. Zhang, *Commuting Slant Toeplitz Operators on the Bergman Space*, arXiv:2504.01042v1 (first submitted 31 March 2025), https://arxiv.org/html/2504.01042v1 .
4. Y. Lu, C. Liu and J. Yang, *Commutativity of kth-Order Slant Toeplitz Operators*, Mathematische Nachrichten (2010), https://doi.org/10.1002/mana.200710100 .
