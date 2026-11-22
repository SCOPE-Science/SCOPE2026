# A two-power information loss when the two discovery stages of a coupon experiment are aggregated

## Finding

Consider independent replicated experiments in which each attempted draw selects one of \(m\geq 2\) equally likely coupon types; independently, a draw is usable with probability \(0<\theta<1\). Each experiment stops once two *distinct usable* types have appeared. Write \(S_1\) for the number of failures before the first usable type, \(S_2\) for the subsequent number of draws failing to produce a second distinct usable type, and \(T=S_1+S_2\) for the observed excess waiting time. A geometric variable throughout counts failures before its first success.

**Exact identification.** Set \(\mu=\mathbb ET\), \(v=\operatorname{Var}T\), and
\[
R=\frac{v+\mu+2}{(\mu+2)^2}.
\]
Then, for every admissible \(m,\theta\),
\[
R=\frac12+\frac{1}{2(2m-1)^2},\qquad
m=\frac{1+(2R-1)^{-1/2}}{2},\qquad
\theta=\frac{2m-1}{(m-1)(\mu+2)}.
\]
Consequently the *distribution of the total alone* uniquely identifies both parameters even though the first moment alone does not.

**Sharp adjacent-size resolution with an unknown success rate.** Fix any \(h>3/2\), let \(m\to\infty\), and compare the two models with \(m\) and \(m+1\) types, choosing in each its rate to make \(\mathbb ET=2h-2\):
\[
\theta_m=\frac{2m-1}{2h(m-1)}.
\]
Let \(n=n_m\) independent experiments be observed, and put \(a=1-1/h\). If only the aggregate totals \(T\) are recorded, the information threshold for distinguishing these two models is \(n\asymp m^6\). Specifically, for \(n/m^6\to0\) their product distributions merge in total variation, while for \(n/m^6\to\infty\) an explicit test using only the empirical mean and variance separates them with both errors tending to zero. If \(n/m^6\to\kappa\in(0,\infty)\), the log-likelihood ratio in favor of \(m+1\), under \(m\), tends to a normal distribution with mean \(-\kappa/(24a^2)\) and variance \(\kappa/(12a^2)\). The best equal-prior two-point testing error tends to
\[
\Phi\!\left(-\frac{\sqrt\kappa}{4\sqrt3\,a}\right).
\]
The empirical-moment midpoint test attains this limiting error and does not require knowing \(h\).

If instead the two stage counts \((S_1,S_2)\) are retained for each experiment, the corresponding sharp threshold improves to \(n\asymp m^4\). The analogous log-likelihood ratio has limiting mean \(-\kappa/(4a)\) and variance \(\kappa/(2a)\) when \(n/m^4\to\kappa\in(0,\infty)\); the optimal equal-prior error tends to
\[
\Phi\!\left(-\frac{\sqrt\kappa}{2\sqrt{2a}}\right).
\]
A second empirical-moment midpoint test attains this limit without knowledge of \(h\). Thus discarding the stage label, although not destroying exact identifiability, costs precisely **two powers of the number of types** in the required number of independent experiments along a least-favorable nuisance-rate path.

## Assumptions and scope

Experiments are independent and have the same parameters within a row of the triangular array. The pair \((S_1,S_2)\) is labeled by chronological stage, and \(T\) is their sum, not the total number of draws (which is \(T+2\)). All limits send integer \(m\to\infty\) with the stated fixed \(h>3/2\) and arbitrary positive integer \(n_m\); Gaussian limits implicitly require \(n_m\to\infty\). The comparison uses neighboring sizes \(m,m+1\) with separately chosen success probabilities \(\theta_m,\theta_{m+1}\), so is a valid least-favorable comparison when \(\theta\) is unknown, not a claim about fixed known \(\theta\). The upper tests can be made uniform when \(h\) ranges over a fixed compact subinterval of \((3/2,\infty)\).

## Proof

**1. Exact generating functions and inversion.** The independent coupon stages have
\[
S_1\sim\operatorname{Geom}(\theta),\qquad
S_2\sim\operatorname{Geom}\!\left(\theta\frac{m-1}{m}\right).
\]
Put
\[
h=\frac{\mu+2}{2},\quad \zeta_m=\frac1{2m-1},\quad \eta_m=\zeta_m^2.
\]
The success probabilities are exactly \(p=1/[h(1-\zeta_m)]\) and \(q=1/[h(1+\zeta_m)]\). Their product probability generating function reduces to
\[
G_{h,\eta}(z)=\frac{1}{[h-(h-1)z]^2-h^2\eta(1-z)^2},\qquad \eta=\zeta_m^2.
\]
The first two cumulants of the independent geometric summands give
\[
\mu=2h-2,\qquad v=2h^2(1+\eta_m)-2h.
\]
Substitution proves \(R=(1+\eta_m)/2\), the displayed inversion, and uniqueness.

For stage-resolved observation put
\[
Q=\frac{\mathbb ES_2-\mathbb ES_1}{\mathbb ES_1+\mathbb ES_2+2}=\zeta_m.
\]
The exact separations for neighboring sizes are
\[
\zeta_m-\zeta_{m+1}=\frac{2}{(2m-1)(2m+1)}\sim\frac1{2m^2},
\]
\[
\eta_m-\eta_{m+1}=\frac{8m}{(2m-1)^2(2m+1)^2}\sim\frac1{2m^3},\quad
R_m-R_{m+1}=\frac{4m}{(4m^2-1)^2}\sim\frac1{4m^3}.
\]

**2. The information lost by summation.** At \(\zeta=\eta=0\), both stages are independent geometric variables with success probability \(1/h\), and \(T\) has negative-binomial mass function
\[
\pi_0(t)=(t+1)h^{-2}a^t,\qquad a=(h-1)/h,\quad t=0,1,\ldots .
\]
The stage-pair score with respect to \(\zeta\) is
\[
s_{\mathrm{pair}}(s_1,s_2)=\frac{s_2-s_1}{h-1},\qquad
I_{\mathrm{pair}}=\mathbb E s_{\mathrm{pair}}^2=\frac2a.
\]
For the total, the first-order \(\zeta\) perturbation vanishes *exactly* because interchanging the two geometric success probabilities does not affect their sum. Its regular perturbation parameter is \(\eta=\zeta^2\). Differentiating the displayed rational generating function at \(\eta=0\), with \(\mu=2h-2\), yields the total-score polynomial
\[
s_{\mathrm{total}}(t)
=\frac{(t-\mu)^2-(2h-1)(t-\mu)-2h(h-1)}{6(h-1)^2}.
\]
Direct negative-binomial factorial-moment summation gives
\[
\mathbb Es_{\mathrm{total}}=0,\quad
\mathbb E[Ts_{\mathrm{total}}]=0,\quad
I_{\mathrm{total}}=\mathbb Es_{\mathrm{total}}^2=\frac1{3a^2}.
\]
These calculations are exact: the derivative coefficient of \(z^t\) in \(G_{h,\eta}\) is
\[
\frac1{h^2}\left\{\binom{t+3}{3}a^t
-2\binom{t+2}{3}a^{t-1}
+\binom{t+1}{3}a^{t-2}\right\},
\]
where any term with a negative exponent index is defined as zero. Dividing by \(\pi_0(t)\) gives the score above.

**3. Likelihood expansion, sharp lower bounds, and Gaussian experiments.** Both experiments form smooth locally regular count families at their homogeneous limits. For the full pair the geometric masses are analytic in \(\zeta\) near zero and have uniformly controlled exponential tails. For totals the convolution mass
\[
\pi_{h,\eta}(t)=pq\sum_{j=0}^t(1-p)^j(1-q)^{t-j}
\]
is invariant under \(\zeta\mapsto-\zeta\), hence its coefficients are analytic in \(\eta=\zeta^2\) near zero. For fixed \(h>3/2\) and sufficiently small parameter neighborhood, positivity and geometric-tail bounds give uniform summability of the first three likelihood derivatives and their squares. To see this explicitly, the masses are bounded below by \(c(t+1)r_-^t\), while their parameter derivatives are bounded above by \(C_j(t+1)r_+^t\), with \(0<r_-<r_+<1\) chosen arbitrarily close to \(a\) and \(r_+^4<r_-^3\). The analyticity and upper bounds follow by complex Cauchy estimates on the displayed rational generating function, choosing a small fixed parameter neighborhood. The same elementary argument (without the symmetry step) applies to the product geometric law. Consequently the standard Taylor proof of local asymptotic normality applies uniformly along \(\eta_m\to0\) or \(\zeta_m\to0\).

Under the model with \(m\), the neighboring parameter increment is negative. With \(\Delta\eta=\eta_{m+1}-\eta_m\), the log-likelihood ratio for aggregated totals satisfies
\[
\log\frac{dP_{m+1}^{\otimes n}}{dP_m^{\otimes n}}
=\Delta\eta\sum_{i=1}^n\dot\ell_{\eta_m}(T_i)
-\frac12n(\Delta\eta)^2 I_{\mathrm{total}}+o_P(1)
\]
whenever \(n(\Delta\eta)^2\) is bounded, with centered score summands and variance tending to \(I_{\mathrm{total}}\). Here \(n(\Delta\eta)^2\to\kappa/4\) for \(n/m^6\to\kappa\). Hence the Gaussian limit has variance \(\kappa I_{\mathrm{total}}/4=\kappa/(12a^2)\) and mean minus half that number. Repeating with \(\Delta\zeta=\zeta_{m+1}-\zeta_m\), and \(n(\Delta\zeta)^2\to\kappa/4\) when \(n/m^4\to\kappa\), gives the stage-pair limit with information \(I_{\mathrm{pair}}=2/a\). The Gaussian likelihood-ratio test gives the two equal-prior error limits stated above.

For \(n/m^6\to0\) (or \(n/m^4\to0\) with the stages retained), the one-experiment Kullback–Leibler divergence is \(\tfrac12I(\Delta)^2+o((\Delta)^2)\). Additivity over the replicates and Pinsker's inequality force the product total variation to zero. Thus no test can have both errors tending to zero in these subcritical regimes.

**4. Explicit nuisance-free tests and sharp upper bounds.** Define the empirical population-variance convention \(\widehat v=n^{-1}\sum_i(T_i-\overline T)^2\), and
\[
\widehat R=\frac{\widehat v+\overline T+2}{(\overline T+2)^2}.
\]
For labeled stages define
\[
\widehat Q=\frac{\overline S_2-\overline S_1}{\overline S_1+\overline S_2+2}.
\]
The triangular-array central limit theorem and delta method, using uniformly bounded geometric fourth moments, yield as \(m,n\to\infty\):
\[
\sqrt n(\widehat R-R_m)\Rightarrow N(0,3a^2/4),\qquad
\sqrt n(\widehat Q-\zeta_m)\Rightarrow N(0,a/2).
\]
At the homogeneous limit, their influence functions are exactly \((3a^2/2)s_{\mathrm{total}}(T)\) and \((a/2)s_{\mathrm{pair}}(S_1,S_2)\), respectively; both have the inverse-information variance required for estimating \(R=(1+\eta)/2\) or \(\zeta\). A threshold at the midpoint of \(R_m,R_{m+1}\), or of \(\zeta_m,\zeta_{m+1}\), therefore attains the displayed limiting Gaussian two-point error. By the exact separations from step 1 and uniform \(O(1/n)\) variance bounds, its two errors vanish when \(n/m^6\to\infty\) for totals or \(n/m^4\to\infty\) for labeled stages. These test statistics and thresholds do not use \(\theta\) or \(h\), and the arguments hold uniformly for \(h\) in compact subsets of \((3/2,\infty)\).

## Verification

Run `python3 check_coupon.py` with a standard Python 3 interpreter. It performs exact-fraction calculations of the two-stage generating function, its coefficient recurrence, convolution probabilities, moments, identification formulae, the total-score coefficient identity and score information, and adjacent-size differences. The expected report is `PASS: 6029 exact-rational identities (finite diagnostics only)`. Independent high-precision KL sums for \(h=2\) also approach the analytically predicted limits \(m^6D_{\rm KL}(P_m^T\Vert P_{m+1}^T)\to1/6\) and \(m^4D_{\rm KL}(P_m^{\rm pair}\Vert P_{m+1}^{\rm pair})\to1/2\). These numerical checks are diagnostics; the infinite and asymptotic assertions depend on the analytical argument above, not finite enumeration.

## Relationship to prior work

O'Neill's 2022 negative-occupancy paper gives the independent-geometric convolution and generating functions; the 2022 preprint appeared before its journal version. A second O'Neill preprint (2022) analyzes the occupancy Markov chain, recursions, and stochastic comparison. Neither inspected primary full text states the unknown-rate adjacent-bin inference experiment or its aggregated-versus-labeled \(m^6\) versus \(m^4\) detection thresholds. A later generic signed negative-binomial approximation for heterogeneous geometric sums describes second-order distributional effects around equal component parameters, but it neither formulates this nuisance-parameter inference problem nor gives its sharp two-observation-scheme LAN constants. The general likelihood expansions are classical; the contribution is the explicit sharp inference contrast for this published occupancy law, not a new general LAN theorem.

## Limitations

Only two collected distinct usable types are studied; no claim is made for arbitrary \(k\). The sample size is the number of *independent repeated experiments*, and the two observation schemes retain different information. The sharp detection lower bounds are built on a fixed-mean nuisance-rate path; they do not assert that every pair with a fixed common \(\theta\) has the same rate. The Gaussian critical experiments use fixed \(h>3/2\); compact-uniform claims avoid the boundary \(\theta=1\). Finite numerical diagnostics do not certify the asymptotic laws. Independent historical priority checking and mathematical audit remain outstanding.

## References

- B. O'Neill (2022). *An examination of the negative occupancy distribution and the coupon-collector distribution*. arXiv:2201.03122, first posted 2022-01-10. https://arxiv.org/abs/2201.03122 ; open full-text journal version https://doi.org/10.1007/s11009-022-09966-x.
- B. O'Neill (2022/2023). *Three Distributions in the Extended Occupancy Problem*. arXiv:2209.02220, first posted 2022-09-06; journal version https://doi.org/10.1007/s11009-023-10053-y.
- *A signed negative-binomial correction for heterogeneous geometric sums* (2026), published research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-signed-negative-binomial-correction-for-heterogeneous-geometri--7476715dcf93 .
