# Sharp logarithmic spectral cycles and measurable critical powers for radial Fock Toeplitz operators

## Finding
For every complex dimension \(d\ge1\), exponent \(\beta>0\), frequency \(\omega>0\), and modulation \(0<\eta<\beta/\sqrt{\beta^2+\omega^2}\), the positive smooth radial symbol
\[
a(z)=(1+|z|^2)^{-\beta}\left[1+\eta\cos(\omega\log(1+|z|^2))\right]
\]
induces a positive compact Toeplitz operator \(T_a\) on the Gaussian analytic Fock space over \(\mathbb C^d\). Let \(N_a(t)\) count singular values of \(T_a\) strictly greater than \(t>0\). Define \(H:\mathbb R\to(0,\infty)\) as the unique positive solution of
\[
H(\theta)^\beta=1+\eta\cos\bigl(\theta+\omega\log H(\theta)\bigr).
\]
Then \(H\) is continuous and \(2\pi\)-periodic, and the full singular-value counting function satisfies
\[
\boxed{N_a(t)=\frac{t^{-d/\beta}}{d!}\,H\left(\frac\omega\beta\log\frac1t\right)^d+O_{d,\beta,\omega,\eta}\bigl(t^{-(d-1)/\beta}\bigr)}\quad(t\downarrow0).
\]
For \(d=1\), the error term is \(O(1)\). The order of this uniform remainder cannot be improved to a little-oh remainder by any continuous counting approximation, because of spectral multiplicity jumps. In particular, the full cluster set of \(t^{d/\beta}N_a(t)\) is precisely
\[
\boxed{\left[\frac{(1-\eta)^{d/\beta}}{d!},\frac{(1+\eta)^{d/\beta}}{d!}\right]},
\]
so no ordinary constant-coefficient Weyl law exists for these smooth positive symbols.

Write \(q=d/\beta\). For every \(p>0\), \(T_a\in\mathcal S_p\) exactly when \(p>q\), while \(T_a\in\mathcal S_{q,\infty}\setminus\mathcal S_q\). At the critical power, \(T_a^q\) is positive and Dixmier-measurable, with the explicit value
\[
\boxed{\operatorname{Tr}_\mathcal D(T_a^q)=\lim_{J\to\infty}\frac1{\log J}\sum_{j=1}^J s_j(T_a)^q=\frac1{2\pi d!}\int_0^{2\pi}(1+\eta\cos u)^q\,du}
\]
for every normalized Dixmier trace \(\operatorname{Tr}_\mathcal D\). Thus a genuinely nonconvergent Weyl coefficient coexists with a unique critical singular trace.

## Assumptions and scope
The analytic Gaussian Fock space \(\mathcal F_d^2\) has squared norm \(\pi^{-d}\int_{\mathbb C^d}|F(z)|^2e^{-|z|^2}\,dV(z)\), with normalized monomial basis \(e_\nu=z^\nu/\sqrt{\nu!}\). The Toeplitz operator is \(T_a=PM_a|_{\mathcal F_d^2}\), where \(P\) is orthogonal Fock projection. Its singular values, including multiplicities, are listed in decreasing order. The stated strict amplitude restriction ensures strict monotonicity of the symbol, essential both for the single-root counting function and the sharp remainder. Only this explicit Gaussian radial family is classified, not general Shubin symbols, nonradial symbols, or arbitrary weights. The expression \(T_a^q\) is positive functional calculus, including fractional \(q\).

## Proof
**1. Exact radial eigenvalue multiset.** Rotational symmetry diagonalizes \(T_a\) on the normalized monomials. In every homogeneous degree \(k\ge0\), its eigenvalue is
\[
\lambda_k=\frac1{\Gamma(k+d)}\int_0^\infty a_0(s)s^{k+d-1}e^{-s}\,ds=\mathbb E\,a_0(S_k),\quad
S_k\sim\operatorname{Gamma}(k+d,1),
\]
where \(a_0(s)=(1+s)^{-\beta}[1+\eta\cos(\omega\log(1+s))]\). Its exact multiplicity is \(m_k=\binom{k+d-1}{d-1}\). The symbol is positive, bounded, and tends to zero, giving compactness since the diagonal eigenvalues tend to zero.

**2. Quantitative gamma localization and strict ordering.** Direct differentiation gives
\[
a_0'(s)=-(1+s)^{-\beta-1}\left[\beta(1+\eta\cos u)+\eta\omega\sin u\right],\quad u=\omega\log(1+s).
\]
The bracket is at least \(c=\beta-\eta\sqrt{\beta^2+\omega^2}>0\), so \(a_0\) is strictly decreasing; all its first two derivatives satisfy \(|a_0^{(j)}(s)|\le C_j(1+s)^{-\beta-j}\). Since \(S_{k+1}\) has the same distribution as \(S_k+E\) with an independent strictly positive unit exponential \(E\), it follows that \(\lambda_{k+1}<\lambda_k\).

For large \(k\), restrict the gamma variable to \([k/2,3k/2]\). Its complementary probability is \(O(e^{-ck})\), by the exponential moment bound for gamma variables, with constants depending on \(d\). Taylor's formula about \(k\) on the central event gives a first-order contribution bounded by \(Ck^{-\beta-1}\mathbb E|S_k-k|\) but, crucially, retaining the signed first-order term yields \(a_0'(k)\mathbb E(S_k-k)=d a_0'(k)=O(k^{-\beta-1})\). The second-order remainder is bounded by \(Ck^{-\beta-2}\mathbb E(S_k-k)^2=O(k^{-\beta-1})\). Truncated-moment errors are exponentially small since the gamma distribution has exponential tails and fixed moments. Therefore
\[
\boxed{\lambda_k=a_0(k)+O_{d,\beta,\omega,\eta}(k^{-\beta-1})}.
\]
This \(O(k^{-\beta-1})\) rather than \(O(k^{-\beta-1/2})\) is needed for the optimal counting error.

**3. Exact oscillating threshold and root.** Because \(a_0\) is continuous and strictly decreasing to zero, for each sufficiently small \(t\) there is exactly one \(r(t)>0\) satisfying \(a_0(r(t))=t\). Put \(y=1+r(t)\), \(u=t^{1/\beta}y\) and \(\theta=(\omega/\beta)\log(1/t)\). The defining equation becomes \(u^\beta=1+\eta\cos(\theta+\omega\log u)\). The map \(u\mapsto u^{-\beta}[1+\eta\cos(\theta+\omega\log u)]\) has strictly negative derivative by the same \(c>0\) bound, tends to infinity at zero and to zero at infinity. Hence it has a unique positive root \(u=H(\theta)\), and
\[
r(t)=t^{-1/\beta}H(\theta)-1.
\]
The root is continuous and periodic; it lies in \([(1-\eta)^{1/\beta},(1+\eta)^{1/\beta}]\). The two endpoints are attained at phases \(\theta=-\omega\log[(1+\eta)^{1/\beta}]\) and \(\theta=\pi-\omega\log[(1-\eta)^{1/\beta}]\) respectively. Its range is therefore this entire interval.

**4. Sharp counting law.** The derivative bound gives \(-a_0'(s)\ge c(1+s)^{-\beta-1}\). The gamma estimate in Step 2 consequently sandwiches the \(k\)-th eigenvalue between \(a_0(k-C)\) and \(a_0(k+C)\) for one fixed sufficiently large \(C\), uniformly for all large \(k\). Since \(\lambda_k\) is strictly decreasing, the last degree \(K(t)\) with \(\lambda_{K(t)}>t\) satisfies \(K(t)=r(t)+O(1)\). Exactly summing degree multiplicities yields
\[
N_a(t)=\sum_{k=0}^{K(t)}\binom{k+d-1}{d-1}=\binom{K(t)+d}{d}
=\frac{r(t)^d}{d!}+O(r(t)^{d-1}),
\]
with \(O(1)\) interpreted when \(d=1\). Inserting the exact formula for \(r(t)\) proves the stated oscillating count and remainder. As \(t\to0\), its phase traverses every point of the circle infinitely often; the complete cluster interval follows from the exact range of \(H\).

The eigenvalue \(\lambda_k\) has a jump of magnitude \(m_k\asymp k^{d-1}\) in \(N_a(t)\). Its location satisfies \(\lambda_k\asymp k^{-\beta}\). Any continuous approximant must err by at least \(m_k/2\) on one side of this jump, which excludes a uniform error \(o(t^{-(d-1)/\beta})\). Thus the remainder exponent is optimal within continuous approximations, not just for the displayed main term.

**5. Schatten cutoffs and exact critical trace.** Positivity and gamma localization imply \(\lambda_k\asymp k^{-\beta}\), and \(m_k\asymp k^{d-1}\). Consequently \(\sum_km_k\lambda_k^p<\infty\) precisely when \(\beta p>d\). The counting estimate implies \(s_j(T_a)=O(j^{-1/q})\) and an asymptotic lower bound of the same order, so the stated weak ideal membership follows.

At critical power \(q=d/\beta\), the sharper gamma expansion gives
\[
m_k\lambda_k^q=\frac{[1+\eta\cos(\omega\log k)]^q}{(d-1)!\,k}+O(k^{-2}).
\]
The error is absolutely summable. Periodic averaging with substitution \(v=\log x\) and a bounded sum-integral error yields
\[
\sum_{k=1}^{K}m_k\lambda_k^q=\frac{\log K}{(d-1)!}\left(\frac1{2\pi}\int_0^{2\pi}(1+\eta\cos u)^q\,du\right)+O(1).
\]
The cumulative rank through degree \(K\) is \(J_K=\binom{K+d}{d}\), so \(\log J_K=d\log K+O(1)\). For \(J_K<J<J_{K+1}\), the remaining part of the next block is at most \(m_{K+1}\lambda_{K+1}^q=O(K^{-1})\); thus the same normalized logarithmic limit holds for all integer \(J\). Existence of the ordinary logarithmic singular-value mean makes the positive operator \(T_a^q\) Dixmier-measurable and gives the displayed trace.

## Verification
The included self-contained file `check.py` evaluates exact Gaussian gamma-moment integrals with SciPy rather than replacing them by pointwise symbols; it checks 360 successive eigenvalue inequalities, five rescaled gamma-localization errors, 101 periodic-root phases, eight threshold-count discrepancies, and the two extremal phases (577 assertions). To reproduce, run `python check.py` with Python, NumPy, and SciPy. These finite diagnostics supplement the argument for all dimensions, parameters, and thresholds in Steps 1–5; they do not certify an infinite statement by enumeration.

## Relationship to prior work
Xu and Dong, *IDA symbols and Schatten–Lorentz theory for Toeplitz operators on weighted Fock spaces* (2026), Theorems 5.1–5.2, prove constant-coefficient Weyl laws for symbols with an asymptotically homogeneous principal term. Their Proposition 5.3 instead varies the *Fock weight* and keeps a pure power symbol to demonstrate failure of a Weyl constant. The present symbol oscillates in its leading logarithmic radial factor on the *fixed standard Gaussian weight*, so it violates their asymptotic-homogeneity hypothesis and permits a sharp explicit nonconstant counting cycle. Bdarneh (2026), Sections 1–4, supplies spectral representation of radial Fock Toeplitz operators, but not this oscillatory counting coefficient or optimal remainder. Bommier-Hato, Engliš and Youssfi's earlier homogeneous-principal-part Dixmier-trace theorem does not directly cover log-periodically modulated leading radial coefficients. Published work on log-log-periodic Fock Toeplitz symbols establishes nonmeasurable critical traces, whereas the *log*-periodic symbol here has a measurable critical power; an earlier periodic Bergman commutator counting law is for a different operator and space. The exact all-dimension remainder, cluster interval, and critical trace combination was not identified in inspected sources. This comparison does not establish publication priority against the whole literature.

## Limitations
Only the displayed small-modulation family is treated. The restriction \(\eta<\beta/\sqrt{\beta^2+\omega^2}\) is a sufficient strict-monotonicity condition, not a claimed sharp phase boundary without monotonicity. The theorem does not classify arbitrary radial symbols, weighted Gaussian spaces, or nonradial symbols. The general pseudodifferential oscillatory Weyl literature may contain an equivalent asymptotic under a different formulation, which is a residual originality risk. Independent audit has not been performed.

## References
1. C. Xu and J. Dong, *IDA symbols and Schatten–Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970 (first public version September 15, 2026), Theorems 5.1–5.2, Proposition 5.3, https://arxiv.org/abs/2609.16970.
2. K. Bdarneh, *Toeplitz \(C^*\)-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652 (first public September 17, 2026), https://arxiv.org/abs/2609.20652.
3. H. Bommier-Hato, M. Engliš and E.-H. Youssfi, *Dixmier trace and the Fock space*, arXiv:1107.3254 (2011), Theorem 7 and Section 7.4, https://arxiv.org/abs/1107.3254.
4. *The logarithmic spectral filter for smooth radial Fock Toeplitz operators*, published research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-logarithmic-spectral-filter-for-smooth-radial-fock-toeplitz--0bc5b54dc8b5.
5. *Log-periodic Weyl counting with bounded remainder for a Bergman Toeplitz commutator*, published research record (November 8, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-log-periodic-weyl-counting-with-bounded-remainder-for-a-bergman--9530b76e3bef.
