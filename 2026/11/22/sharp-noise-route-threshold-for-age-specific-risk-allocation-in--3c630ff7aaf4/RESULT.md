# Sharp noise-route threshold for age-specific risk allocation in a two-stage population

## Finding

Consider the stable two-stage linear population-response model
\[
J_{t+1}=F A_t+b+\xi^J_{t+1},\qquad
A_{t+1}=sJ_t+hA_t+\xi^A_{t+1}.
\]
The stage shocks are centered, independent across time and stages, and have variances \(v_J>0\) and \(v_A>0\). Fix \(0<m<1\), fecundity \(F\geq1\), external recruitment \(b>0\), and require \(h+Fs=m\), with \(0\leq h<m\) and \(s=(m-h)/F\). Here \(m\) fixes the distance \(1-m\) from the demographic replacement boundary; an allocation changes how this response is divided between adult retention and maturation/reproduction.

Let \(q=F^2v_A/v_J\), \(y=m-h\), and define the squared stationary coefficient of variation of adult abundance by \(\mathrm{CV}^2=\operatorname{Var}(A_t)/(\mathbb E A_t)^2\) in the covariance-stationary regime. Then
\[
\mathrm{CV}^2=\frac{v_J}{b^2}\,\frac{(1-m)(1-y)}{(1+y)(1+m-2y)}\left(1+\frac{q}{y^2}\right).
\]
Put \(y_0=1-\sqrt{1-m}\) and, for \(y>y_0\) with positive denominator, put
\[
Q_m(y)=\frac{y^3(2y-y^2-m)}{(1+m-2y)(1-y^2)-y(2y-y^2-m)}.
\]
The **unique** global risk-minimizing allocation, for strictly positive noise in both stages, is classified exactly:

1. If \(m<1/\sqrt2\) and \(q\geq m^4/(1-2m^2)\), then \(y_*=m\), so \(h_*=0\).
2. In every other case, the optimum is the unique \(y_*\in(y_0,m)\) satisfying \(Q_m(y_*)=q\) and the positive-denominator condition. Here \(h_*=m-y_*\).

Thus \(m=1/\sqrt2\) is a sharp structural boundary: above and at it, every finite positive adult-noise contribution leaves a strictly positive optimal adult-retention share; below it, adult retention is eliminated exactly when adult noise relative to juvenile noise crosses the displayed threshold. Equality in the threshold belongs to the zero-adult-retention regime.

## Assumptions and scope

All parameters are constant and real. The independent shocks have zero means and finite stated variances; no Gaussianity is assumed. The model is an affine *population-response* approximation, not a birth-death process with nonnegative integer-valued counts. It permits signed stage perturbations and may not preserve nonnegativity for arbitrarily large shocks. The optimality statement is for the specified fixed-\(m\), fixed-\(F\), fixed-\(b\), fixed-noise-variance policy family, not for fixed total fishing effort, constant actual Perron eigenvalue, or general density-dependent fisheries.

For \(0\leq h<m\), \(s>0\), so the stationary mean adult abundance is strictly positive and its coefficient of variation is defined. The endpoint \(h=m\) is excluded since \(s=0\) would give a zero adult mean. Stationarity here means constant means and covariances depending only on lag. Independence and constant variances allow the shock laws themselves to vary with time and thus do not require strict stationarity. If the joint shock law is time-invariant (in particular if each stage has identically distributed shocks over time), the causal state is also strictly stationary.

## Proof

**Stationary moments.** Write \(r=Fs=m-h\) and \(M=\begin{pmatrix}0&F\\s&h\end{pmatrix}\). Its characteristic polynomial \(\lambda^2-h\lambda-r\) is negative at zero and positive at both \(\lambda=\pm1\) since \(r>0\), \(1-h-r=1-m>0\) and \(1+h-r>0\). Thus both roots have modulus less than one. On the integer time axis the causal state is \(\mu+\sum_{k\ge0}M^k\xi_{t-k}\), where \(\xi_t=(\xi_t^J,\xi_t^A)^\mathsf{T}\) and \(\mu=(I-M)^{-1}(b,0)^\mathsf{T}\). The series converges in mean square by geometric decay and the fixed finite variances. Its autocovariance at a nonnegative lag \(\ell\) is \(\sum_{k\ge0}M^{k+\ell}\operatorname{diag}(v_J,v_A)(M^k)^\mathsf{T}\), so it is covariance-stationary. Any other solution driven by the same shocks with uniformly bounded second moments differs by \(M^k\) times the difference at time \(t-k\), which tends to zero in mean square; this gives uniqueness among covariance-stationary solutions. Shift-invariance of the joint shock law, when assumed, transfers to the shift-equivariant series. For a recursion started at a finite time with finite initial second moment the same limiting first two moments follow by decay of the initial term. The adult coordinate obeys
\[
A_{t+1}=hA_t+rA_{t-1}+sb+s\xi^J_t+\xi^A_{t+1}.
\]
The last two terms are independent white innovations of total variance \(s^2v_J+v_A\). The mean is \(\bar A=sb/(1-m)\). The centered Yule--Walker identities give
\[
\gamma_1=\frac{h\gamma_0}{1-r},\quad
\gamma_2=h\gamma_1+r\gamma_0,\quad
\gamma_0=h\gamma_1+r\gamma_2+s^2v_J+v_A.
\]
Eliminating \(\gamma_1,\gamma_2\) yields
\[
\gamma_0=\frac{(s^2v_J+v_A)(1-r)}{(1+r)((1-r)^2-h^2)}.
\]
Since \((1-r)^2-h^2=(1-m)(1-r+h)\), division by \(\bar A^2\) yields the formula in the Finding. All denominator factors are strictly positive on the stated domain.

**Derivative and its sign.** Set \(y=r=m-h\), so \(0<y\leq m\), and discard the positive constant \(v_J/b^2\). Denote the remaining risk by \(R_m(y,q)\). Direct logarithmic differentiation gives
\[
\frac12\partial_y\log R_m(y,q)=T_m(y)-\frac{q}{y(y^2+q)},\quad
T_m(y)=\frac{2y-y^2-m}{(1+m-2y)(1-y^2)}.
\]
The numerator of \(T_m\) is strictly increasing for \(y<1\), and it changes sign exactly at \(y_0=1-\sqrt{1-m}\), which lies strictly between zero and \(m\). Since \(q>0\), the derivative is negative for \(y\leq y_0\). Above \(y_0\), \(T_m\) is strictly increasing: its numerator is positive and increasing, while each positive denominator factor decreases with \(y\).

If \(yT_m(y)\geq1\), the derivative is positive. If \(0<yT_m(y)<1\), the derivative has the same sign as \(Q_m(y)-q\), where \(Q_m(y)=y^3T_m(y)/(1-yT_m(y))\). It increases strictly from zero toward either its terminal value or its first pole. To verify that last strictness without relying on a numerical graph, write \(a=1-m\), \(z=1-y\), and
\[
H_m(y)=my-3m+3y^3-9y^2+8y=a(z+2)-3z^3.
\]
On \(y\in[y_0,m]\), one has \(0<z\leq\sqrt a\), hence \(H_m(y)\geq2a(1-z)>0\). Differentiating the rational expression for \(Q_m\), with \(D_m(y)=(1+m-2y)(1-y^2)-y(2y-y^2-m)\), gives
\[
Q_m'(y)=\frac{y^2(1+y)(1+m-2y)H_m(y)}{D_m(y)^2}>0
\]
wherever \(D_m(y)>0\). Thus the risk decreases and then increases, with at most one interior minimum.

**Boundary and completeness.** At \(y=m\),
\[
mT_m(m)=\frac{m^2}{1-m^2},\qquad
Q_m(m)=\frac{m^4}{1-2m^2}\quad\text{if }m<1/\sqrt2.
\]
If \(m<1/\sqrt2\), the pole is absent from \((y_0,m]\); the monotonicity just proved gives a unique interior minimum for \(0<q<Q_m(m)\), and the boundary minimum \(y=m\) for \(q\ge Q_m(m)\). If \(m\ge1/\sqrt2\), \(yT_m(y)\) reaches one at or before \(m\). Then \(Q_m\) grows from zero to infinity before or at the endpoint, and every finite \(q>0\) has exactly one interior minimizer. These cases are exhaustive for positive shocks in both stages. The separate zero-adult-shock limit is a known constant-innovation-variance two-lag optimizer, not part of the novelty claim.

## Verification

The standalone `verify.py` uses Python standard-library exact rational arithmetic to check stationary covariance identities independently through the two-by-two Lyapunov matrix equation, the normalized risk formula, rational derivative-sign equivalences, selected exact minimizer witnesses, and sample-grid unimodality. Executing `python verify.py` gives `PASS 57978 exact rational assertions`. These finite tests do **not** establish global uniqueness; the derivative factorization and sign proof above do so.

For a fully rational interior witness take \(m=1/2\), \(q=1/351\): the unique minimizer has \(y_*=1/3\), \(h_*=1/6\). In contrast, with \(m=1/2\) and \(q=1/4\), the unique minimizer has \(h_*=0\), because the sharp cutoff is \(q_c=1/8\). Both cases can be realized with strictly positive juvenile and adult noise variances.

## Relationship to prior work

Age-selective fishery and bycatch models motivate distinguishing juvenile and adult survival, notably Takashina (2024), which treats deterministic delay-driven oscillations rather than this two-noise stationary-risk allocation. General affine population covariance and sensitivity formulas are established by Schreiber and Moore (2018); Sadykov and colleagues (2022) analyze age-structured frequency responses. Those broad frameworks establish covariance methods but do not state the present fixed-margin, two-independent-shock sharp global allocation boundary.

A published *Exact noise-optimal weighting and the negative-feedback frontier for two-lag iterations* (2026), research record 7dc18efbbac0, proves the constant-innovation-variance two-lag weight optimum. That prior theorem **does cover the \(q=0\) limiting optimizer** under a coefficient change, and that zero-adult-shock case is excluded from the claimed new result. It does **not** cover the competing, allocation-dependent second noise variance \(s^2v_J+v_A\), the policy-dependent positive mean, or the \(q>0\) finite-versus-zero-adult-retention threshold. The claim's contribution is precisely the two-positive-noise exact phase classification, including its necessary and sufficient conditions.

## Limitations

This is a mathematically exact theorem for one idealized linear response family. It does not show that real harvesting policies can maintain the chosen replacement-margin parameter while trading stage survival, that environmental noise intensities remain constant across interventions, or that abundance stays nonnegative under large additive shocks. Nor does it establish finite-sample risk, adaptive controls, nonlinear stability or empirical benefits. The earlier generic covariance theory contains enough machinery to derive moments; equivalently framed risk optimization may exist in uninspected ecological or autoregressive literature. Independent external validation has not occurred.

## References

1. N. Takashina, *Understanding the impact of selective fishery and bycatch on stock dynamics*, Natural Resource Modeling (first published 11 June 2024), https://doi.org/10.1111/nrm.12403 .
2. S. J. Schreiber and J. L. Moore, *The structured demography of open populations in fluctuating environments*, Methods in Ecology and Evolution (2018), https://doi.org/10.1111/2041-210X.12991 .
3. A. Sadykov, K. Farnsworth, D. Sadykova, and N. C. Stenseth, *The transfer function method reveals how age-structured populations respond to environmental fluctuations with serious implications for fisheries management*, Population Ecology (2022), https://doi.org/10.1002/1438-390X.12124 .
4. *Exact noise-optimal weighting and the negative-feedback frontier for two-lag iterations* (2026), published research record 7dc18efbbac0.
5. Classical Yule--Walker identities for second-order autoregressions and discrete Lyapunov covariance equations (used as known mathematical tools).
