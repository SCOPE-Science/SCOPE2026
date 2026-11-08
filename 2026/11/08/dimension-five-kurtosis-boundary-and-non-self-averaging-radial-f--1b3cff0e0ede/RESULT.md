# Dimension-five kurtosis boundary and non-self-averaging radial fluctuations of a trapped run-and-tumble particle

## Finding
Consider a particle in an isotropic harmonic trap in every integer dimension \(d\geq 1\), with deterministic trap drift \(-\mu\mathbf r\), constant propulsion speed \(v_0>0\), and independent full isotropic redraws of its propulsion direction at Poisson rate \(\gamma>0\), without thermal Brownian forcing. Write \(\alpha=\gamma/\mu\) and normalize the stationary position to \(\mathbf X^{(d)}=(\mu/v_0)\mathbf r^{(d)}\). The standardized excess kurtosis of any one coordinate is **exactly**
\[
\kappa_d(\alpha)=\frac{\mathbb E[(X_1^{(d)})^4]}{\mathbb E[(X_1^{(d)})^2]^2}-3
=\frac{6\{\alpha(d-4)-6\}}{(d+2)(\alpha+2)(\alpha+3)}.
\]
Consequently, in dimensions \(d\leq4\) it is strictly negative at every finite positive \(\alpha\). In every dimension \(d\geq5\), it is negative, zero, or positive exactly when \(\alpha\) is below, equal to, or above \(6/(d-4)\). For \(d\geq5\), its unique maximum over \(\alpha>0\) occurs at
\[
\alpha_*(d)=\frac{6+\sqrt{6(d-1)(d-2)}}{d-4},
\]
while for \(d\leq4\) it increases strictly toward zero from below.

There is a complementary *non-self-averaging high-dimensional limit*. For each fixed \(\alpha>0\), let \(V_j\) be independent \(\operatorname{Beta}(1,\alpha)\) variables and let \(P_j=V_j\prod_{i<j}(1-V_i)\) be their GEM stick-breaking weights. Define
\[
H_\alpha=\sum_{j\geq1}P_j^2,\qquad T_\alpha=\sum_{j\geq1}P_j^4.
\]
Then, using the same weights in a coupling across dimensions,
\[
\|\mathbf X^{(d)}\|^2\longrightarrow H_\alpha\quad\text{in }L^2,
\qquad
\sqrt d\big(\|\mathbf X^{(d)}\|^2-H_\alpha\big)
\Longrightarrow \mathcal N\big(0,2(H_\alpha^2-T_\alpha)\big)
\]
*conditionally on the weights*, where the second limit is a centered Gaussian variance mixture. For each fixed number \(k\) of coordinate projections,
\[
\sqrt d\,(X_1^{(d)},\ldots,X_k^{(d)})
\Longrightarrow\sqrt{H_\alpha}\,(Z_1,\ldots,Z_k),
\]
where the \(Z_i\) are independent standard normals, independent of the weights. Thus the limiting coordinate distribution is not a single Gaussian, and the radial norm does **not** concentrate at a deterministic value:
\[
\mathbb E H_\alpha=\frac1{\alpha+1},\qquad
\operatorname{Var}(H_\alpha)=\frac{2\alpha}{(\alpha+1)^2(\alpha+2)(\alpha+3)}>0.
\]
The limiting coordinate's standardized excess kurtosis is \(6\alpha/[(\alpha+2)(\alpha+3)]\), with a unique maximum \(30-12\sqrt6\) at \(\alpha=\sqrt6\). These exact laws give a sharp spatial-dimension threshold and identify the temporal-disorder mechanism behind persistent non-Gaussianity in high dimension.

## Assumptions and scope
The orientation \(\mathbf U_t\) is uniform on \(S^{d-1}\) immediately after each independent rate-\(\gamma\) tumble and is fixed between tumbles. In dimension one, the sphere consists of the two signs with equal redraw probability. The dynamics are \(d\mathbf r_t/dt=-\mu\mathbf r_t+v_0\mathbf U_t\). There is no translational diffusion, no coupling among particles, no anisotropy, and no prescribed nonstationary initial law. The confining drift and positive tumble rate give a unique stationary law. The fixed-\(\alpha\) high-dimensional limit does **not** assert a joint limit in which \(\alpha\) itself grows with \(d\).

The high-dimensional statements refer to a probability coupling using one sequence of GEM weights and independent uniform sphere directions for each dimension; unconditional weak limits do not require such a coupling. The Gaussian-mixture convergence for finitely many coordinate projections and the conditional Gaussian radial-fluctuation convergence are asserted separately; independence between their fluctuations is not needed. The conditional Gaussian radial variance is strictly positive almost surely because all GEM weights are positive and at least two occur.

## Proof
**1. Exact stationary random barycenter.** Rescale time by \(\mu\). Look backward from a stationary observation time along the independent Poisson event history; the successive exponential intervals have rate \(\alpha\). The normalized solution is the exponentially discounted integral of the past direction process. Integrating over the intervals writes it as
\[
\mathbf X^{(d)}\ \overset{\mathrm d}=\ \sum_{j\geq1}P_j\mathbf U_j^{(d)},
\]
where the directions are independent uniform points on \(S^{d-1}\), independent of the weights, and the interval contribution fractions are independent \(\operatorname{Beta}(1,\alpha)\) stick breaks. The weights are strictly positive and sum to one almost surely. This stationary representation is the Dirichlet-process construction already established for the harmonic run-and-tumble model by Guéneau, Majumdar and Schehr; it is an explicit premise here, not a claimed discovery.

**2. Direct stationary-generator calculation of the fourth moment.** Work in normalized time with \(\dot{\mathbf X}=-\mathbf X+\mathbf U\). Let \(q=\mathbb E\|\mathbf X\|^2\), \(a=\mathbb E(\mathbf X\cdot\mathbf U)\), \(c=\mathbb E(\mathbf X\cdot\mathbf U)^2\), \(b=\mathbb E[\|\mathbf X\|^2(\mathbf X\cdot\mathbf U)]\), and \(m_4=\mathbb E\|\mathbf X\|^4\). The stationary generator applied successively to these bounded polynomial observables gives
\[
0=1-(1+\alpha)a,\quad 0=-2q+2a,\quad
0=2a+\alpha q/d-(2+\alpha)c,
\]
\[
0=q+2c-(3+\alpha)b,\qquad 0=-4m_4+4b.
\]
The angular redraw identities are \(\mathbb E\mathbf U'=0\) and \(\mathbb E(\mathbf X\cdot\mathbf U')^2=\|\mathbf X\|^2/d\). Solving yields
\[
q=\frac1{\alpha+1},\qquad
m_4=\frac{\alpha+6+2\alpha/d}{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
Rotation symmetry gives \(\mathbb E X_1^2=q/d\) and \(\mathbb E X_1^4=3m_4/[d(d+2)]\), including dimension one. Substitution and cancellation prove the displayed formula for \(\kappa_d\). Its derivative has the sign opposite to the polynomial
\[
(d-4)\alpha^2-12\alpha-6(d+1).
\]
For \(d\leq4\) this is negative on all \(\alpha>0\). For \(d\geq5\) it has exactly one positive root, namely \(\alpha_*(d)\), proving all zero, sign, monotonicity and maximum claims.

**3. Exact GEM moments.** Let \(H=\sum_jP_j^2\) and \(T=\sum_jP_j^4\). For four independent samples from the random discrete weights, the usual sequential predictive probabilities of the GEM/Dirichlet process give
\[
\mathbb EH=\frac1{\alpha+1},\qquad
\mathbb ET=\frac6{(\alpha+1)(\alpha+2)(\alpha+3)},
\]
\[
\mathbb EH^2=\frac{\alpha+6}{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
The last identity splits the event that sample pairs \((1,2)\) and \((3,4)\) agree into all-four-equal and two-distinct-pairs cases. Subtraction gives the stated strictly positive variance. In addition, conditional on the weights,
\[
\mathbb E_{\mathbf U}\|\mathbf X^{(d)}\|^2=H,\qquad
\mathbb E_{\mathbf U}(\|\mathbf X^{(d)}\|^2-H)^2
=\frac2d(H^2-T).
\]
Indeed, expand the squared norm and use \(\mathbb E(\mathbf U_i\cdot\mathbf U_j)=0\) and \(\mathbb E(\mathbf U_i\cdot\mathbf U_j)^2=1/d\) for distinct indices. Products from different unordered pairs are orthogonal in expectation, including pairs sharing one index. Since \(0\leq H^2-T\leq1\), the first radial limit holds in \(L^2\).

**4. Conditional second-order radial fluctuations.** For any fixed positive integer \(M\), write \(\mathbf U_j^{(d)}=\mathbf G_j/\|\mathbf G_j\|\) for independent standard Gaussian \(d\)-vectors, \(j\leq M\). The multivariate central limit theorem applied to independent coordinate products \(G_{i\ell}G_{j\ell}\) shows that the vector \(\{\sqrt d(\mathbf U_i^{(d)}\cdot\mathbf U_j^{(d)}):1\leq i<j\leq M\}\) converges to independent standard normal variables. Hence
\[
2\sqrt d\sum_{1\leq i<j\leq M}P_iP_j(\mathbf U_i\cdot\mathbf U_j)
\Longrightarrow \mathcal N\!\left(0,4\sum_{1\leq i<j\leq M}P_i^2P_j^2\right)
\]
for each fixed weight sequence. The conditional second moment of the discarded terms is exactly \(4\sum_{i<j:\max(i,j)>M}P_i^2P_j^2\), which tends to zero as \(M\to\infty\), uniformly in \(d\). Passing to the limit by truncation yields conditional Gaussian convergence with variance \(4\sum_{i<j}P_i^2P_j^2=2(H^2-T)\). Boundedness of conditional characteristic functions then gives the stated unconditional Gaussian-variance mixture.

**5. Fixed-coordinate Gaussian variance mixture.** For every fixed \(k,M\), the first \(k\) entries of \(\sqrt d\mathbf U_j^{(d)}\), \(j\leq M\), jointly converge to independent standard normal entries. Therefore the first \(k\) scaled coordinates of the truncated weighted sum converge, conditional on the weights, to centered Gaussians with covariance \((\sum_{j\leq M}P_j^2)I_k\). The omitted tail has conditional second moment \(\sum_{j>M}P_j^2\) in every scaled coordinate, independent of \(d\), and goes to zero. This proves the fixed-coordinate limit. Gaussian mixing gives \(\mathbb E Y_1^2=\mathbb EH\), \(\mathbb E Y_1^4=3\mathbb EH^2\), and hence excess kurtosis \(3\operatorname{Var}(H)/(\mathbb EH)^2=6\alpha/[(\alpha+2)(\alpha+3)]\). Differentiating shows the unique maximum at \(\alpha=\sqrt6\), with value \(30-12\sqrt6\).

## Verification
The included `checker.py` uses only Python's standard library. Run `python3 checker.py` alongside this file. It independently solves the finite-dimensional generator balance equations using exact rational numbers; compares the results with independently obtained GEM four-sample probabilities; verifies the \(d=1\) beta-law fourth moment; checks angular Gram variance algebra; and checks the signs and optimizer on finite parameter grids. Its recorded execution passed 1,951 diagnostics. These computations are checks, **not** proofs of an infinite-dimensional or all-parameter statement; the analytic arguments above establish those assertions.

## Relationship to prior work
Guéneau, Majumdar and Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential* (arXiv:2602.08436, first public February 9, 2026), derive the general stationary law and Dirichlet-process stick-breaking representation in arbitrary dimension and explicitly analyze several low-dimensional radial densities. **Those stationary representations and their general moment machinery are prior work.** In particular, the raw finite-dimensional second and fourth moment identities are derivable from their general framework and are not presented here as independently novel. The asserted contribution is the sharp dimension-five sign and optimum classification together with the *conditional high-dimensional Gaussian fluctuation law*, the persistent random-radius limit, and their connection to the limiting non-Gaussian coordinate mixture. These are limit theorems and shape classifications not stated in the inspected source text. The already classical GEM construction and Simpson concentration statistic are likewise acknowledged, not claimed as new.

Related mathematical literature on the Gini–Simpson index (including the 2026 study by Bissiri, Corradin and Ongaro) treats diversity functionals of random discrete weights. That material supplies context for \(H_\alpha\), but the angular Gram fluctuations and their role in the dimension-dependent active-particle kurtosis statement are distinct questions. published-finding corpus and own-record similarity/alias searches were conducted, without identifying a prior statement of this joint theorem; absence from an index is not a proof of priority.

## Limitations
The theorem fixes \(\alpha>0\) as \(d\to\infty\); joint fast-tumbling/high-dimension scaling, transient relaxation, interacting particles, anisotropic forcing, and Gaussian thermal noise are outside the claim. The radial CLT is conditional on the random GEM weights, not an ordinary normal limit with deterministic variance. The moment identities alone would be a routine use of previously known formulas; the principal mathematical content lies in the sharp sign regime and the conditional limit law. Published general finite-\(d\) stationary distribution formulas provide broad starting information and may facilitate further derivations. The possibility of an unindexed older theorem that directly covers these high-dimensional angular-mixing limits remains a publication-priority risk. Independent scholarly review has not been performed.

## References
- M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (initial submission 2026-02-09), https://arxiv.org/abs/2602.08436 .
- T. S. Ferguson, *A Bayesian analysis of some nonparametric problems*, Ann. Statist. **1** (1973), 209–230 (Dirichlet processes).
- J. Sethuraman, *A constructive definition of Dirichlet priors*, Statistica Sinica **4** (1994), 639–650 (stick-breaking construction).
- P. G. Bissiri, R. Corradin, A. Ongaro, *Nonparametric Bayesian inference for the Gini–Simpson index*, arXiv:2607.25737 (2026-07-28), https://arxiv.org/abs/2607.25737 (related diversity-statistic context, not asserted direct coverage).
