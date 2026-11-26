# Beta-product coupling and sharp stationary confinement laws for a run–stop–run particle

## Finding
Consider a one-dimensional run-and-tumble particle in a harmonic trap with a genuine exponentially distributed resting (tumbling) stage. Its position solves
\[\dot X_s=-\kappa X_s+v\,S_s,\]
where \(\kappa,v>0\). The internal state \(S_s\in\{-1,0,+1\}\) jumps from each of \(\pm1\) to \(0\) at rate \(\gamma_R>0\), and from \(0\) to each of \(\pm1\) at rate \(\gamma_T/2\). The departure direction from a rest is therefore fair and independent of earlier choices. Define the dimensionless rates \(R=\gamma_R/\kappa\), \(T=\gamma_T/\kappa\), and normalized stationary position \(Z=\kappa X/v\).

**Theorem.** Let \(U\sim\operatorname{Beta}(T/2,R/2)\) and \(V\sim\operatorname{Beta}(1/2,R/2)\) be independent, and let \(\varepsilon\) be an independent fair sign. The unique stationary position obeys
\[\boxed{Z\;\overset{d}=\;\varepsilon\sqrt{UV}.}\]
This identity is a statement about the one-time stationary law, not an independence decomposition of the physical trajectory.

It implies a **strict stochastic ordering of the complete confinement profile**: for \(R_2\ge R_1>0\) and \(0<T_2\le T_1\), with at least one strict inequality,
\[\boxed{\Pr(|Z_{R_2,T_2}|>x)<\Pr(|Z_{R_1,T_1}|>x)\quad(0<x<1).}\]
Thus every nonconstant strictly increasing measurable confinement cost with finite expectation, and every stationary absolute-position quantile in \((0,1)\), responds in the same direction: increasing the run-to-rest transition rate or decreasing the rest-to-run transition rate pulls the entire stationary distribution inward. In particular, at a fixed total transition-rate budget \(R+T\), transferring rate from run termination to rest termination moves the entire absolute-position law strictly outward. The strict order is stronger than comparison of mean-square displacements.

There are exact and independent central and endpoint localization laws. Write \(c=R/2\), \(a=T/2\), and \(B(\cdot,\cdot)\) for Euler's beta function. The even stationary density \(f_{R,T}\) is strictly positive on \((-1,1)\), zero outside \([-1,1]\), and as \(x\to0\),
\[
\begin{aligned}
0<T<1:\quad f_{R,T}(x)&\sim\frac{B((1-T)/2,c)}{B(1/2,c)B(T/2,c)}|x|^{T-1},\\
T=1:\quad f_{R,1}(x)&\sim\frac{2}{B(1/2,c)^2}\log\frac1{|x|},\\
T>1:\quad f_{R,T}(0)&=\frac{B((T-1)/2,c)}{B(1/2,c)B(T/2,c)}<\infty.
\end{aligned}
\]
At either turning boundary, as \(|x|\uparrow1\),
\[\boxed{f_{R,T}(x)\sim\frac{2^{R-1}B(R/2,R/2)}{B(1/2,R/2)B(T/2,R/2)}(1-|x|)^{R-1}.}\]
In particular, the **central power/logarithm/finite transition is exactly at \(T=1\)**, while the **boundary divergence/finite/vanishing transition is exactly at \(R=1\)**. Every coefficient displayed is strictly positive. The two transition exponents can be varied independently.

The distinguished line \(R=2\) has an elementary closed density for all \(T>0\):
\[
 f_{2,T}(x)=
 \begin{cases}
 \dfrac{T}{2(T-1)}\bigl(1-|x|^{T-1}\bigr),&T\ne1,\\[4pt]
 \dfrac12\log\dfrac1{|x|},&T=1,
 \end{cases}\qquad 0<|x|<1.
\]
These are normalized two-sided densities, with no point atoms.

## Assumptions and scope
The theorem assumes exponential run and rest durations, an independent fair choice of \(+1\) or \(-1\) at the beginning of each run, deterministic linear confinement, no translational thermal noise, and strictly positive \(\kappa,v,\gamma_R,\gamma_T\). It applies to every pair of positive real dimensionless rates, not only integer or rational rates. Rates are not constrained to be equal. All claims concern the stationary position marginal; no pathwise monotonicity of sample trajectories is asserted. The support is contained in \([-v/\kappa,v/\kappa]\) in physical units.

## Proof
**Stationarity and uniqueness.** The three-state continuous-time chain is irreducible and admits a unique two-sided stationary realization. Given that chain, the pullback integral
\[Z_s=\int_{-\infty}^s e^{-(s-u)}S_u\,du\]
(in dimensionless time) exists, is bounded by one, and is stationary. For two solutions driven by the same chain their difference decays as \(e^{-s}\), proving uniqueness of the joint stationary law and hence its position marginal. Sign symmetry forces all odd position moments to vanish.

**Independent generator calculation.** Let \(P_n,M_n,H_n\) denote stationary expectations of \(Z^n\) multiplied by the indicators of the positive-run, negative-run, and resting states. Set \(A_n=P_n+M_n\), \(C_n=P_n-M_n\). Stationarity of the generator applied to those three monomials gives, for every integer \(n\ge1\),
\[
(n+R)A_n=nC_{n-1}+T H_n,\quad
(n+R)C_n=nA_{n-1},\quad
(n+T)H_n=RA_n.
\]
At degree zero, \(A_0=T/(R+T)\), \(C_0=0\), and \(H_0=R/(R+T)\). Eliminating \(H_n\) gives
\[A_n=\frac{n+T}{n+R+T}C_{n-1},\qquad C_n=\frac{n}{n+R}A_{n-1}.\]
For \(m_n=\mathbb E Z^n=A_n+H_n\), these equations imply the **exact recurrence**
\[
 m_0=1,\quad m_{2k+1}=0,\quad
 \boxed{\frac{m_{2k}}{m_{2k-2}}=
 \frac{2k-1}{2k-1+R}\frac{2k-2+T}{2k-2+R+T}\quad(k\ge1).}
\]
There is no appeal to the previously published characteristic function in this derivation.

**Beta factorization.** For \(W\sim\operatorname{Beta}(p,q)\), its integer moments are \(\mathbb EW^k=(p)_k/(p+q)_k\). Independence of \(U,V\) therefore gives
\[\mathbb E(\varepsilon\sqrt{UV})^{2k}=
\frac{(1/2)_k}{((R+1)/2)_k}\frac{(T/2)_k}{((R+T)/2)_k},\]
whose consecutive ratio is precisely the recurrence above; odd moments vanish by sign symmetry. Both distributions have support in \([-1,1]\), where moments determine the measure (polynomials are dense in continuous functions). Thus the equality in distribution follows without density inversion or numerical approximation.

**Strict stochastic coupling.** For every fixed \(q>0\), the beta family \(\operatorname{Beta}(p,q)\) is strictly stochastically increasing in \(p>0\), while \(\operatorname{Beta}(p,q)\) is strictly decreasing in \(q>0\). Construct the first property by writing a beta variable as \(G_p/(G_p+H_q)\), where independent gamma variables have shapes \(p,q\). Increasing a shape adds an independent strictly positive gamma increment, producing a strict almost-sure ordering. Construct the two beta factors independently and couple all their numerators and denominators by these gamma increments. Under the theorem's parameter ordering the product for \((R_2,T_2)\) is almost surely smaller than that for \((R_1,T_1)\). Strict inequality holds for every interior tail cutoff because the gamma-variable densities are positive on \((0,\infty)\), allowing a positive-probability crossing of each prescribed cutoff. This proves the stated strict first-order stochastic order; the quantile and increasing-cost implications follow by standard tail integration.

**Central asymptotics.** The symmetric beta-root variable \(Y=\varepsilon\sqrt V\) has density \(g(y)=(1-y^2)^{c-1}/B(1/2,c)\) on \((-1,1)\). The other root \(W=\sqrt U\) has density \(h(w)=2w^{T-1}(1-w^2)^{c-1}/B(T/2,c)\) for \(0<w<1\). The product density is the Mellin convolution
\[f_{R,T}(x)=\frac{2}{B(T/2,c)}\int_{|x|}^1 w^{T-2}(1-w^2)^{c-1}g(x/w)\,dw.\]
For \(T<1\), substitute \(y=|x|/w\), divide by \(|x|^{T-1}\), and use dominated convergence on compact subintervals followed by integrable endpoint estimates. The limit is \(\mathbb E|Y|^{-T}/B(T/2,c)\), which equals the beta ratio in the theorem. The integrability condition is exactly \(T<1\). For \(T>1\), the integrand at \(x=0\) is integrable and gives \(g(0)\mathbb E U^{-1/2}\), the stated finite value; local continuity follows by splitting away the two endpoints and applying domination to the remaining beta-weight integrals. For \(T=1\), the intermediate scale \(|x|\ll w\ll1\) contributes \(2g(0)/B(1/2,c)\int_{|x|}^1dw/w\); the remaining endpoint regions contribute lower-order terms. This gives precisely \(2/B(1/2,c)^2\) times the logarithm.

**Turning-boundary asymptotics.** Near \(+1\), the density of \(Y\) behaves as \(2^{c-1}(1-y)^{c-1}/B(1/2,c)\) and the density of \(W\) behaves as \(2^c(1-w)^{c-1}/B(T/2,c)\). Since \(1-YW=(1-Y)+(1-W)+O((1-Y)(1-W))\), convolution of their two small deficits yields a beta integral \(B(c,c)\). Consequently the positive-side density coefficient is \(2^{2c-1}B(c,c)/(B(1/2,c)B(T/2,c))\) with exponent \(2c-1=R-1\). The negative boundary has the same law by symmetry. Positivity gives the sharp divergence thresholds, including the nonzero finite endpoint value when \(R=1\).

**Elementary family.** When \(R=2\), \(V\sim\operatorname{Beta}(1/2,1)\), so \(Y\) is uniform on \((-1,1)\). Also \(U\sim\operatorname{Beta}(T/2,1)\). Integrating the conditional uniform density of \(Y\sqrt U\) directly gives the displayed elementary formulas; the logarithm is the continuous \(T\to1\) limit. Their normalization is immediate by integration.

## Verification
The accompanying `check.py` uses only Python's standard library. It constructs the state-resolved generator equations over 576 positive rational pairs of rates and degrees one through sixteen, independently compares the resulting stationary moments with the beta-product moments, verifies the exact elementary family against the full moment hierarchy, and checks its central and boundary coefficient limits. The decoded program passed 37,096 assertions. This is independent finite corroboration, not proof of the statements for all real parameters. The proof above supplies the infinite-parameter argument.

Reproduction: place `check.py` beside this document and run `python check.py`. The normalized parameters are arbitrary positive real numbers, not measurement data or fitted coefficients.

## Relationship to prior work
Sun, Ye, and Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (first posted 1 September 2024), derive stationary one-dimensional characteristic functions, hypergeometric densities and moment recursions for unequal run and tumble rates. These earlier **one-time distributions and moments are not claimed as new**. Their article discusses independent central and edge singularities qualitatively. The present contribution is a **positive independent-beta representation** with a global simultaneous coupling across all positive rate pairs, the resulting **strict all-quantile stochastic ordering**, and explicit general-rate localization amplitudes. These comparisons distinguish a new ordering theorem from reprinting an already known marginal law. See their sections II–V, especially the characteristic function (38), density (39) and discussion following it.

Basu, Majumdar, Rosso, Sabhapandit and Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (22 October 2019), study the special equal-rate three-state chain and describe power/logarithmic critical central behavior there. Accordingly, neither the existence of a logarithmic center transition in that subfamily nor a general three-state stationary density is claimed as new here. The present strict stochastic order addresses two independently variable positive transition rates.

Guéneau, Majumdar, and Schehr, arXiv:2602.08436 (2026), develop a stick-breaking representation for a trapped model with nonzero velocities resampled at instantaneous tumbles; that cited setting does not impose a separate, exponentially timed zero-velocity stage. It is relevant structural literature but does not by itself establish the two-rate order proved here. The newest article's abstract, rather than its entire text, was inspected; a wider relation remains a priority risk.

## Limitations
The beta representation is a distributional identity, not a joint pathwise factorization. The earlier hypergeometric density completely determines each fixed-rate marginal; the value of the present result is therefore the previously unlocated global coupling/strict stochastic-order structure and exact coefficient formulas, not discovery of a new stationary distribution. Because these are derived from a known marginal characterization, an existing general beta-comparison theorem or an overlooked observation in adjacent literature may subsume the ordering; independent priority review is necessary. The formulas require independent exponential run/rest clocks, fair direction resampling, and absence of thermal diffusion. At zero rates or with additional Brownian noise, limiting or convolution modifications are needed. No numerical experiment proves novelty or the infinite-parameter theorem; no independent audit has been performed.

## References
1. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (1 September 2024); revised arXiv:2409.00578v2 (16 April 2025), https://arxiv.org/html/2409.00578v2 ; *Physical Review E* 111, 044136 (2025).
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1 (22 October 2019), https://arxiv.org/abs/1910.10083 ; *Journal of Physics A* 53, 09LT01 (2020).
3. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (9 February 2026), https://arxiv.org/abs/2602.08436 .
