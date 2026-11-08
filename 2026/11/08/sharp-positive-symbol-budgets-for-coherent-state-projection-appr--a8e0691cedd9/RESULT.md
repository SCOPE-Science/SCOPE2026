# Sharp positive-symbol budgets for coherent-state projection approximation in Fock spaces

## Finding

Let \(d\ge1\) be an integer. On the normalized Bargmann–Fock space \(\mathcal F^2(\mathbb C^d)\), let \(P_w\) denote orthogonal projection onto the normalized coherent vector at \(w\in\mathbb C^d\). For a positive symbol budget \(M\), define
\[
\mathcal E_d(M)=\inf_{0\le f\le M}\|T_f-P_w\|,
\]
where the infimum is over all measurable real-valued functions satisfying the bounds almost everywhere, and \(T_f\) is Gaussian Toeplitz quantization. The answer is independent of \(w\).

Write \(F_k(a)=\frac1{(k-1)!}\int_0^a e^{-s}s^{k-1}\,ds\) for positive integers \(k\). For \(0<M\le\frac12\),
\[
\boxed{\mathcal E_d(M)=1-M};
\]
the unique minimizing symbol up to almost-everywhere equality is the constant \(f\equiv M\).

For \(M>\frac12\), there is a unique \(a=a_d(M)>0\) solving
\[
M\bigl(F_d(a)+F_{d+1}(a)\bigr)=1.
\]
Then
\[
\boxed{\mathcal E_d(M)=M F_{d+1}(a_d(M))},
\]
and the unique minimizing symbol, among **all** bounded positive symbols rather than merely radial ones, is
\[
f(z)=M\,\mathbf1_{\{|z-w|^2\le a_d(M)\}}.
\]
At large budgets,
\[
\boxed{\mathcal E_d(M)\sim\frac{(d!)^{1/d}}{d+1}\,M^{-1/d}\quad(M\to\infty)}.
\]
Thus the inverse budget needed for small operator-norm error grows with the sharp exponent \(d\).

## Assumptions and scope

The Fock inner product is \(\langle h,g\rangle=\pi^{-d}\int_{\mathbb C^d}h(z)\overline{g(z)}e^{-|z|^2}\,dV(z)\). Its monomial orthonormal basis is \(e_\alpha(z)=z^\alpha/\sqrt{\alpha!}\). The coherent vector is \(k_w(z)=e^{z\cdot\bar w-|w|^2/2}\), and \(P_w h=\langle h,k_w\rangle k_w\). For measurable \(f\) with \(0\le f\le M\), define \(T_f=P_{\mathcal F}M_f|_{\mathcal F}\), a positive bounded operator. No integrability, continuity, rotational symmetry, or compact support is assumed on admissible \(f\). The bound on \(f\) is a pointwise symbol bound, not a bound on \(\|T_f\|\). The assertion is specifically for positive symbols; signed and complex symbols are not covered.

## Proof

**1. Reduction to the vacuum.** The Weyl displacement \((W_w h)(z)=e^{z\cdot\bar w-|w|^2/2}h(z-w)\) is unitary on Fock space, carries \(1\) to \(k_w\), and intertwines \(T_f\) with the Toeplitz operator having translated symbol \(f(\cdot-w)\). It therefore suffices to consider \(w=0\), where \(P_0\) projects onto the constants.

**2. Two unavoidable expectation constraints.** Write \(d\mu(z)=\pi^{-d}e^{-|z|^2}\,dV(z)\). For any admissible \(f\), set
\[
L=\langle T_f1,1\rangle=\int f\,d\mu,\qquad
B=\frac1d\sum_{j=1}^d\langle T_fz_j,z_j\rangle
=\frac1d\int |z|^2 f(z)\,d\mu(z).
\]
The vectors \(1,z_1,\ldots,z_d\) are normalized and mutually orthogonal. Consequently
\[
\|T_f-P_0\|\ge\max\{|1-L|,B\}.
\]
The radial random variable \(s=|z|^2\) under \(\mu\) has the \(\operatorname{Gamma}(d,1)\) density \(q_d(s)=e^{-s}s^{d-1}/(d-1)!\). If \(g(s)\in[0,M]\) is the spherical average of \(f\), then \(L=\int gq_d\) and \(B=\int gq_{d+1}\), where \(q_{d+1}(s)=s q_d(s)/d\).

**3. Sharp bathtub inequality and equality rigidity.** For \(0\le L<M\), there is a unique finite \(a\ge0\) with \(L=M F_d(a)\). Put \(g_*(s)=M\mathbf1_{[0,a]}(s)\). Since \(\int(g-g_*)q_d=0\),
\[
B-MF_{d+1}(a)
=\frac1d\int_0^\infty (g(s)-g_*(s))(s-a)q_d(s)\,ds\ge0.
\]
Indeed, each integrand factor product is nonnegative both below and above \(a\). Equality forces \(g=g_*\) almost everywhere because \(q_d>0\) on \((0,\infty)\). Since the spherical mean of an \([0,M]\)-valued function equals an extreme value \(0\) or \(M\) only when the function itself equals that extreme value on almost every point of that sphere, equality also forces \(f(z)=M\mathbf1_{\{|z|^2\le a\}}\) almost everywhere. The endpoint \(L=M\) forces \(f=M\) almost everywhere and gives \(B=M\). Thus the sharp lower envelope at prescribed vacuum expectation is
\[
\phi_M(L)=M F_{d+1}\bigl(F_d^{-1}(L/M)\bigr),
\qquad 0\le L<M,
\]
with \(\phi_M(M)=M\). The function \(\phi_M\) is continuous and strictly increasing.

**4. Scalar minimax and the transition.** Every admissible symbol satisfies
\[
\|T_f-P_0\|\ge\max\{|1-L|,\phi_M(L)\},\quad 0\le L\le M.
\]
If \(M\le1/2\), the first term is at least \(1-M\), attained only when \(L=M\), hence only by \(f=M\). For \(M>1/2\), on \(0\le L\le\min\{M,1\}\), the decreasing branch \(1-L\) meets the strictly increasing branch \(\phi_M(L)\) at a unique \(L_*\). Such a crossing exists because \(\phi_M(0)=0<1\) and either \(\phi_M(M)=M>1-M\), or \(\phi_M(1)>0=1-1\). Values \(L>1\), if available, cannot improve the minimum because \(\phi_M\) increases. Setting \(L_*=MF_d(a)\) gives \(1-MF_d(a)=MF_{d+1}(a)\), precisely the displayed equation. Strict monotonicity proves uniqueness of the optimizing \(L_*\), and equality in step 3 proves uniqueness of the optimizing symbol.

**5. Attainment and the full operator norm.** For the candidate \(f_*(z)=M\mathbf1_{\{|z|^2\le a\}}\), unitary symmetry makes \(T_{f_*}\) scalar on each homogeneous polynomial degree. The eigenvalue in degree \(N\ge0\) is
\[
\lambda_N=M\int_0^a q_{d+N}(s)\,ds=M F_{d+N}(a).
\]
The Gamma distribution with integer shape \(d+N+1\) is the distribution of an independent unit exponential added to one with shape \(d+N\). Hence \(\lambda_0>\lambda_1>\lambda_2>\cdots>0\) for finite positive \(a\). Therefore
\[
\|T_{f_*}-P_0\|=\max\bigl\{|1-\lambda_0|,\lambda_1\bigr\}
=MF_{d+1}(a),
\]
which achieves the lower bound. For \(M\le1/2\), \(T_M=MI\) has \(\|MI-P_0\|=1-M\), also achieving its lower bound. Weyl covariance gives the asserted center \(w\).

**6. High-budget asymptotic.** As \(M\to\infty\), the equation forces \(a\to0\). Since \(F_k(a)=a^k/k!+O(a^{k+1})\), it follows that \(a=(d!/M)^{1/d}(1+o(1))\). Thus
\[
MF_{d+1}(a)=\frac{(d!)^{1/d}}{d+1}M^{-1/d}(1+o(1)).
\]
This proves the exact leading constant and exponent.

## Verification

The companion program `verification.py` evaluates the integer-shape Gamma cumulative probabilities, solves the balancing equation by bisection, verifies the predicted equality of vacuum and first-excited errors, and checks the ordering against higher homogeneous degrees for several dimensions and symbol budgets. Its finite assertions were executed successfully. The all-dimensional proof above is analytical; no finite sampling is used to establish infinitely many spectral inequalities or global uniqueness.

## Relationship to prior work

Lin, Lu and Zu (2026) establish a Fourier criterion for bounded-symbol Fock Toeplitz representability, motivating the question of **quantitative symbol cost** for an operator that has no bounded function symbol. Borichev and Rozenblum (2013) prove finite-rank rigidity for Fock Toeplitz operators with function symbols; the present theorem asks for the exact distance to a fixed coherent rank-one projection with a bounded *positive* symbol budget, a different and quantitative question. Galbis (2021/2022) proves norm estimates for radial selfadjoint Fock Toeplitz operators in terms of the symbol's \(L^1\) and \(L^\infty\) norms, but not the constrained projection-approximation optimum. Dewage and Ólafsson (2021/2022) provide radial and quasi-radial spectral representations; their spectral formulas support the normalization but do not supply the sharp global minimax, its unique optimizer, or the inverse-budget exponent. The comparison uses mathematical implication, not absence of matching terminology.

## Limitations

The restriction \(f\ge0\) is essential to the bathtub lower bound and uniqueness argument. No optimization is asserted over signed or complex-valued bounded symbols, other finite-rank projections, or alternative Hilbert-space norms. The eigenvalue calculation proves only the specified radial indicator's spectrum; optimality among nonradial symbols is justified separately in steps 2–4. Publication priority remains open to broader general symmetrization/minimax results that might imply this sharp formula without using its present notation.

## References

1. Z. Lin, Y. Lu, C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102, first public version 2026-07-05.
2. A. Borichev, G. Rozenblum, *The finite rank theorem for Toeplitz operators in the Fock space*, arXiv:1303.2996 (2013).
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (2021); Complex Analysis and Operator Theory 16 (2022), article 15.
4. V. Dewage, G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (2021); Complex Analysis and Operator Theory 16 (2022), article 61.
