# An exact triangular stationary-law recursion for noisy voters on a star

## Finding

For every integer \(k\ge2\) and rates \(\alpha>0\), \(\beta\ge0\), \(\eta>0\), the complete stationary joint distribution of the hub opinion and the number of opinion-one leaves in a continuous-time noisy voter model on the \(k\)-leaf star is determined by the following **positive-denominator, forward triangular recurrence**, rather than by solving a growing stationary linear system.

Put \(A=\alpha+\eta\). Let \(H\in\{0,1\}\) be the stationary hub opinion, let \(M\in\{0,\ldots,k\}\) be the number of opinion-one leaves, and define normalized falling-factorial moments
\[
 F_r=\frac{\mathbb E[(M)_r]}{(k)_r},\qquad
 G_r=\frac{\mathbb E[H(M)_r]}{(k)_r},
 \quad 0\le r\le k,
\]
with \((m)_0=1\) and \((m)_r=m(m-1)\cdots(m-r+1)\). Start with \(F_0=1\), \(G_0=1/2\). For \(1\le r\le k\), successively compute
\[
 F_r=\frac{\alpha G_{r-1}+(\eta/2)F_{r-1}}{A},
\]
\[
 G_r=\frac{r(\alpha+\eta/2)G_{r-1}
 +[\eta/2+\beta r/k+\beta(k-r)\eta/(2kA)]F_r}
 {rA+\eta+\beta-\beta(k-r)\alpha/(kA)}.
\]
Both sequences require \(O(k)\) exact-rational arithmetic operations when rates are rational; the denominator in the second equation is strictly positive for all stated parameters. In particular, they recover every stationary probability through the finite **binomial inversion**
\[
 \Pr(M=m)=\sum_{r=m}^k(-1)^{r-m}\binom r m\binom k r F_r,
 \quad
 \Pr(H=1,M=m)=\sum_{r=m}^k(-1)^{r-m}\binom r m\binom k r G_r,
\]
for each \(m\in\{0,\ldots,k\}\). Recover \(\Pr(H=0,M=m)\) by subtraction. Thus the full stationary count law can be computed in \(O(k^2)\) arithmetic operations with direct binomial inversion, without exponential configuration enumeration. This finite-size **complete law** is the principal finding.

The same structure yields a transparent limiting law. For fixed positive rates as \(k\to\infty\), put
\[
 a_0=\frac{\eta}{2(\alpha+\eta)},\qquad
 d=\frac{\alpha}{\alpha+\eta},\qquad
 \vartheta=\frac{\eta(\alpha+\eta+\beta)}{2(\alpha+\eta)^2}.
\]
Then \((H,M/k)\) converges in distribution to \((H_\infty,a_0+dY)\), where \(Y\sim\mathrm{Beta}(\vartheta,\vartheta)\) and \(\Pr(H_\infty=1\mid Y=y)=y\). In particular, the limiting leaf-fraction variance is \(\alpha^2/[4((\alpha+\eta)(\alpha+2\eta)+\beta\eta)]\), strictly positive. The limiting density is endpoint-peaked on its proper support for \(\vartheta<1\), uniform for \(\vartheta=1\), and center-peaked for \(\vartheta>1\). This asymptotic observation is a consistency consequence, not claimed as a standalone discovery independent of established two-state switching-limit theory.

## Assumptions and scope

All clocks are independent. Each leaf copies the hub opinion at rate \(\alpha\). The hub copies the opinion of a uniformly chosen leaf at total rate \(\beta\) (zero allowed). Independently, each site redraws its opinion from an unbiased Bernoulli distribution at rate \(\eta\). A redraw may leave the opinion unchanged. The finite process is irreducible for \(\eta>0\), and exchangeability of leaves implies that \((H,M)\) is a Markov projection. All quantities refer to its unique stationary distribution. Fixing rates before taking \(k\to\infty\) is essential; no joint scaling of noise and degree is asserted.

## Proof

**1. Reduced generator.** From state \((h,m)\), the aggregate rate for \(m\to m+1\) is \((k-m)(\alpha h+\eta/2)\); for \(m\to m-1\) it is \(m[\alpha(1-h)+\eta/2]\). The rate for \(h\to1-h\) is \(\eta/2+\beta m/k\) if \(h=0\), and \(\eta/2+\beta(k-m)/k\) if \(h=1\). Each finite state communicates through the positive noise rates; stationarity and uniqueness follow.

**2. Triangular closure.** Let \(Z_r\) be the product of the opinion bits of any \(r\) *distinct labeled leaves*. Exchangeability gives \(\mathbb E Z_r=F_r\), \(\mathbb E(HZ_r)=G_r\). Applying the generator to \(Z_r\) and taking stationary expectations yields
\[
 0=r\{\alpha G_{r-1}+(\eta/2)F_{r-1}-AF_r\}.
\]
For the product \(HZ_r\), leaf updates contribute \(r[(\alpha+\eta/2)G_{r-1}-AG_r]\), hub redraws contribute \((\eta/2)(F_r-2G_r)\), and hub copying contributes
\[
 \beta\{(r/k)F_r+[(k-r)/k]F_{r+1}-G_r\}.
\]
The last identity holds because a randomly sampled copied leaf belongs to the chosen \(r\)-subset with probability \(r/k\). At stationarity the sum vanishes. Substitute the first identity with index \(r+1\): \(AF_{r+1}=\alpha G_r+(\eta/2)F_r\). Rearrangement is exactly the displayed second recurrence. For \(r=k\), the coefficient of \(F_{r+1}\) is zero, so the same expression remains valid without defining moments beyond \(k\). Its denominator obeys
\[
 rA+\eta+\beta[1-(k-r)\alpha/(kA)]>0,
\]
because \(\alpha/A<1\). Spin-flip symmetry gives \(G_0=\mathbb E H=1/2\). These steps establish uniqueness of the computed moment arrays without any guessed distribution.

**3. Inversion and exact finite law.** For \(s\) an indeterminate, the elementary identity \(s^M=(1+(s-1))^M\) gives
\[
 \mathbb E[s^M]=\sum_{r=0}^k\binom k r F_r(s-1)^r,
 \quad \mathbb E[Hs^M]=\sum_{r=0}^k\binom k r G_r(s-1)^r.
\]
Equating coefficients of \(s^m\) proves both inversion formulas. Conversely, those two generating polynomials uniquely determine all \(2(k+1)\) joint probabilities. A single forward pass needs \(O(k)\) operations, and direct coefficient inversion needs \(O(k^2)\). No approximations or missing normalization assumptions enter the finite theorem.

**4. Limiting joint law.** Put \(X_k=M/k\), \(Y_k=(X_k-a_0)/d\), \(A=\alpha+\eta\), \(g=\eta/2+\beta a_0=A\vartheta\). On any smooth test function in \((h,y)\), the reduced generator converges uniformly on the common compact state range, with error \(O(k^{-1})\) for each fixed polynomial test, to
\[
 \mathcal L f(h,y)=A(h-y)\partial_y f(h,y)
 +\lambda_h(y)[f(1-h,y)-f(h,y)],
\]
where \(\lambda_0(y)=g+\beta d y\) and \(\lambda_1(y)=g+\beta d(1-y)\). Compactness gives subsequential stationary limits \(\mu\), and finite stationary generator identities pass to \(\mathbb E_\mu\mathcal L f=0\) for every polynomial test. With \(m_j=\mathbb E_\mu Y^j\), the choice \(f=y^{j+1}/(j+1)\) gives \(\mathbb E_\mu[H Y^j]=m_{j+1}\). The choice \(f=hy^j\), for \(j\ge0\), cancels both the \(\beta d\)-dependent switching terms and yields
\[
 (jA+g)m_j=(jA+2g)m_{j+1},\qquad m_0=1.
\]
Thus \(m_j=(\vartheta)_j/(2\vartheta)_j\), the moments of \(\mathrm{Beta}(\vartheta,\vartheta)\). Polynomials determine probability measures on the common compact interval, so every subsequence has the same \(Y\) marginal; the identities for \(\mathbb E[HY^j]\) determine the hub conditional expectation, which is \(\mathbb E[H\mid Y]=Y\). All subsequences agree and convergence follows. The beta variance identity gives the stated limiting variance; its density is proportional to \(y^{\vartheta-1}(1-y)^{\vartheta-1}\), proving the three shape regimes. This part is also derivable by the published two-state piecewise-deterministic stationary-density method; the non-asymptotic triangular joint-law inversion is the new finite-size point.

## Verification

The standalone `verify_noisy_star.py` uses only Python's standard library. It independently builds the reduced Markov generator, solves the finite rational stationary equations from scratch, computes all normalised factorial moments and both generating-polynomial inversions, and compares each quantity exactly with the recurrence for five distinct star sizes and six parameter triples. It also checks the limiting beta moment recurrence through degree 16. Run `python verify_noisy_star.py`. The checker reported 2,550 exact-rational assertions passed across 30 finite chains. These tests cover finite examples; the all-degree theorem is proved by the preceding generator and inversion identities, not by extrapolation from tests.

For example, with \(k=3\) and \(\alpha=\beta=\eta=1\), the marginal probabilities \(\Pr(M=m)\) for \(m=0,1,2,3\) are exactly \((17,27,27,17)/88\). In the same parameters but with growing \(k\), the limiting scaled beta shape parameter is \(3/8\), so the large-star distribution has endpoint singularities on \([1/4,3/4]\). This contrast motivates retaining exact finite-size information instead of replacing it prematurely with the limit.

## Relationship to prior work

Cox, Peres and Steif (first public arXiv release 2014-08-21, arXiv:1408.5122), Section 4, identify the hub/count Markov projection on a star and prove a mixing-time result, but do not give the all-order triangular stationary moments or the binomial-inverted complete joint law. Carro, Toral and San Miguel (arXiv:1602.06935, 2016; open full text PMCID PMC4837380) analyze noisy voter dynamics on complex networks with annealed approximations and lower-order moment formulas, rather than an exact finite-star complete stationary distribution. Pymar and Rivera (arXiv:2112.01478) analyze a different, degree-weighted density and explicitly note that their regularity criterion fails for stars. Caligiuri and Galla (arXiv:2305.19096, Section III.3.3) give an exact stationary formula for general two-state switching-fluid limits, which *does cover the limiting beta calculation in principle* but not the finite-\(k\) triangular stationary distribution. Granovsky and Madras (1995) give general noisy-voter duality formulas; the complete article was not available to compare all possible stationary specialization formulas, and priority relative to its uninspected sections remains a risk. No discovery of the original noisy voter model, star lumping, general duality, or general two-state piecewise-deterministic stationary formula is asserted.

## Limitations

Exactness concerns a continuous-time symmetric-redraw binary model with a single hub, exchangeable leaves, and independent update clocks. The closure relies on that symmetry and need not survive heterogeneous leaf copying rates, correlated external redraws, or larger hub networks. Arithmetic operation counts do not account for the growth of rational numerator/denominator bit lengths. The triangular recurrence may have unpublished equivalents in noisy-voter duality or finite telegraph-driven population literature. Independent historical-priority and mathematical audits have not been performed.

## References

- J. T. Cox, Y. Peres and J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122 (first posted August 21, 2014), https://arxiv.org/abs/1408.5122.
- A. Carro, R. Toral and M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (2016); https://pmc.ncbi.nlm.nih.gov/articles/PMC4837380/.
- R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (2021), https://arxiv.org/abs/2112.01478.
- A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (2023), https://arxiv.org/abs/2305.19096.
- B. L. Granovsky and N. Madras, *The noisy voter model*, Stochastic Processes and their Applications 55 (1995), 23–43, https://doi.org/10.1016/0304-4149(94)00035-R (abstract inspected; full text unavailable).
