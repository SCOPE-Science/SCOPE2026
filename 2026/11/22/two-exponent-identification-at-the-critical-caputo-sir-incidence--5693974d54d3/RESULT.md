# Two-exponent identification at the critical Caputo SIR incidence cancellation

## Finding

For the constant-rate Caputo susceptible–infectious–removed (SIR) epidemic with known population size \(N\), positive transmission and removal rates, and a positive initial infectious count strictly below \(N\), **the fractional order remains structurally identifiable from perfect continuous incidence on every interval starting at the known initial time, even when its usual leading generalized Taylor coefficient vanishes**.

The exceptional, naturally determined hypersurface is
\[
\beta(N-2I_0)=\gamma N.
\]
On it the incidence has a strictly negative second fractional coefficient and a strictly positive third coefficient, so its first two nonconstant powers are exactly \(t^{2\alpha}\) and \(t^{3\alpha}\). An alternative ordinary or fractional order whose first power is \(2\alpha\) cannot reproduce the second, \(3\alpha\), power. This gives a sharp resolution of the initial-flatness ambiguity, including the case \(\alpha=1/2\), in which the leading incidence change is proportional to ordinary time.

## Assumptions and scope

Let \(N>0\), \(0<\alpha\le1\), \(\beta,\gamma>0\), and \(I_0\in(0,N)\). Set \(S_0=N-I_0\), \(R_0=0\). The system is
\[
{}^{C}\!D_t^{\alpha}S=-\frac{\beta SI}{N},\qquad
{}^{C}\!D_t^{\alpha}I=\frac{\beta SI}{N}-\gamma I,\qquad
{}^{C}\!D_t^{\alpha}R=\gamma I.
\]
At \(\alpha=1\), the derivative is ordinary. At smaller orders it is the standard Caputo derivative based at \(t=0\). Define *incidence* by \(x(t)=\beta S(t)I(t)/N\). We consider exact, continuously observed \(x\) on \([0,\varepsilon]\) for any \(\varepsilon>0\) on which the solution exists. The time origin, population size and model class are known. The rates and \(I_0\) may be unknown; the claim identifies only \(\alpha\), not every individual parameter. Transmission is constant rather than an unrestricted function of time.

Define
\[
 c=\frac{\beta}{N},\quad A=N-I_0,\quad B=I_0,\quad x_0=cAB,\quad
 H_2=\frac{\Gamma(1+2\alpha)}{\Gamma(1+\alpha)^2},\quad
 H_3=\frac{\Gamma(1+3\alpha)}{\Gamma(1+\alpha)\Gamma(1+2\alpha)}.
\]
The equality \(\beta(N-2I_0)=\gamma N\) is feasible precisely with \(0<I_0<N/2\) and the corresponding positive rates. It describes zero initial \(t^{\alpha}\)-coefficient of incidence, not a disease-free equilibrium.

## Proof

**1. Finite generalized expansion.** For \(k\ge0\), use the normalized basis \(e_k(t)=t^{k\alpha}/\Gamma(1+k\alpha)\). The Caputo Volterra operator satisfies \(\mathcal I^{\alpha}e_k=e_{k+1}\). Local Lipschitz continuity of the polynomial right-hand side and repeated substitution into the Volterra equations yield asymptotic expansions to any prescribed finite order in this basis. The remainder at the third order is \(o(t^{3\alpha})\). No convergence of an infinite formal series is required.

Write \(S=A+\sum_{k=1}^{3}s_ke_k+o(t^{3\alpha})\), \(I=B+\sum_{k=1}^{3}i_ke_k+o(t^{3\alpha})\), and \(x=x_0+\sum_{k=1}^{3}x_ke_k+o(t^{3\alpha})\). The Volterra equations give \(s_{k+1}=-x_k\) and \(i_{k+1}=x_k-\gamma i_k\), with \(i_0=B\), and product coefficients give
\[
\begin{aligned}
 x_1&=c(s_1B+Ai_1),\\
 x_2&=c(s_2B+Ai_2+H_2s_1i_1),\\
 x_3&=c(s_3B+Ai_3+H_3(s_1i_2+s_2i_1)).
\end{aligned}
\]
In particular, \(s_1=-x_0\), \(i_1=x_0-\gamma B\), and
\[
 x_1=x_0\bigl(c(A-B)-\gamma\bigr).
\]
Thus \(x_1=0\) exactly on the stated hypersurface; elsewhere it is nonzero.

**2. Exact critical coefficients.** Suppose \(c(A-B)=\gamma\). Then
\[
 i_1=cB^2>0,\qquad s_2=0,\qquad i_2=-\gamma i_1.
\]
Substitution gives
\[
\boxed{x_2=-c i_1(\gamma A+H_2x_0)<0.}
\]
For the next coefficient, \(s_3=-x_2\) and \(i_3=x_2+\gamma^2i_1\). Hence
\[
\begin{aligned}
 x_3
 &=c\{(A-B)x_2+A\gamma^2i_1+H_3\gamma x_0i_1\}\\
 &=\boxed{c\gamma i_1x_0(H_3-H_2)>0},
\end{aligned}
\]
where the second identity uses \(c(A-B)=\gamma\) and the formula for \(x_2\). Finally
\[
 \frac{H_3}{H_2}=
 \frac{\Gamma(1+3\alpha)\Gamma(1+\alpha)}{\Gamma(1+2\alpha)^2}>1,
\]
by strict log-convexity of the Gamma function, since \(1+2\alpha\) is the midpoint of \(1+\alpha\) and \(1+3\alpha\). The strict inequality holds for every \(\alpha>0\). This proves
\[
 x(t)=x_0+\frac{x_2}{\Gamma(1+2\alpha)}t^{2\alpha}
       +\frac{x_3}{\Gamma(1+3\alpha)}t^{3\alpha}
       +o(t^{3\alpha}),\qquad x_2<0<x_3.
\]
The infectious count initially increases since \(i_1>0\), even though incidence initially decreases at its leading nonzero order.

**3. Identifiability against every competing order.** For any admissible parameter vector, step 1 says that the first nonconstant exponent of incidence is \(\alpha\) when \(x_1\ne0\), or \(2\alpha\) when \(x_1=0\). If two incidence functions agree on \([0,\varepsilon]\), their constant terms and first nonzero exponents agree. Two generic models therefore have the same order, as do two exceptional models. Suppose instead an exceptional model of order \(\alpha\) agreed with a generic model of order \(\alpha'\). Leading exponents would force \(\alpha'=2\alpha\). A generic model of order \(\alpha'\) has a generalized expansion solely in integer multiples of \(\alpha'\); after the \(t^{2\alpha}\) term its remainder is \(O(t^{4\alpha})\). But step 2 gives a *nonzero* \(t^{3\alpha}\) term in the exceptional model. Subtracting the common leading term and dividing by \(t^{3\alpha}\) is contradictory. The reverse pairing is symmetric. Thus equality of exact incidence always forces equality of \(\alpha\) for the entire stated positive-parameter domain. This does not assert recoverability from finite or noisy observations.

**4. Explicit half-order witness.** Take \(N=3\), \(I_0=1\), \(\beta=3\), \(\gamma=1\), and \(\alpha=1/2\). Then \(A=2\), \(x_0=2\), \(i_1=1\), \(H_2=4/\pi\), and \(H_3=3/2\). Thus
\[
 x(t)=2-\left(2+\frac8\pi\right)t
 +\frac{3-8/\pi}{\Gamma(5/2)}t^{3/2}+o(t^{3/2}).
\]
Although the first change is linear in ordinary time, the strictly positive \(t^{3/2}\) coefficient precludes identical constant-rate ordinary SIR incidence, which has an ordinary integer-power Taylor expansion.

## Verification

The standalone `check.py` (Python standard library only) verifies the coefficient recurrences and critical identities for 500 seeded positive parameter choices across five fractional orders, and verifies the exact \(\alpha=1/2\) specialization across seven test orders. Execute `python3 check.py`. This is a finite algebraic cross-check, **not** the proof of all parameters or of Gamma log-convexity. The infinite-domain sign and uniqueness claims are established in steps 1–3. An independent scientific audit has not been performed.

## Relationship to prior work

Hossain and Alam (arXiv:2611.13590v1, first released 10 November 2026) formulate the Caputo hybrid SIR model and compare fixed-rate and reconstructed time-dependent transmission in forecasting; their Theorem 5.1 addresses slow forgetting of initial-state errors, not order recovery at flat incidence. Zinihi (arXiv:2509.22760v1, 26 September 2025) numerically learns the fractional order of a different SEIRD model; an empirical inference method does not imply these exact SIR coefficients.

A closely related later paper by Hossain and Alam (arXiv:2611.25440v1, first released 19 November 2026) proves generic exact-data order identifiability in Proposition 4.1 under \(x_1\ne0\), and explicitly notes that this condition fails at \(\beta(N-2I_0)=\gamma N\). The **new component assessed here** is the exact second/third-coefficient calculation and proof that the excluded hypersurface cannot be confused with any generic alternative order. General fractional-order inverse theory, including Liu and Yamamoto (arXiv:2206.02108), already exploits short-time exponents for other equations; that strategy itself is not claimed as new.

## Limitations

The data are noiseless, continuous and observed from the known initial instant. A finite collection of observations cannot determine the exponents by the above limiting argument. Severe observational noise or unknown reporting delays could conceal the small \(t^{3\alpha}\) term; practical statistical identification is not proved. The results require constant positive \(\beta\) and \(\gamma\), zero initial recovered population, one common Caputo order, and the classical bilinear SIR incidence law. Allowing unrestricted time-varying transmission destroys order identifiability. Neither other parameters' unique recovery nor predictive benefit is established. Historical priority remains literature-bounded.

## References

1. M. B. Hossain and M. S. Alam, *Fractional-Order Hybrid SIR Forecasting of COVID-19 in Bangladesh and the United States: Memory Effects and Out-of-Sample Evaluation*, arXiv:2611.13590v1 (10 November 2026). https://arxiv.org/abs/2611.13590
2. A. Zinihi, *Identifying Memory Effects in Epidemics via a Fractional SEIRD Model and Physics-Informed Neural Networks*, arXiv:2509.22760v1 (26 September 2025). https://arxiv.org/abs/2509.22760
3. M. B. Hossain and M. S. Alam, *Fractional Order or False Memory: Identifiability of Caputo SIR Models from Incidence Data*, arXiv:2611.25440v1 (19 November 2026), §4, Proposition 4.1. https://arxiv.org/abs/2611.25440
4. Y. Liu and M. Yamamoto, *Uniqueness of orders and parameters in multi-term time-fractional diffusion equations by short-time behavior*, arXiv:2206.02108 (5 June 2022). https://arxiv.org/abs/2206.02108
