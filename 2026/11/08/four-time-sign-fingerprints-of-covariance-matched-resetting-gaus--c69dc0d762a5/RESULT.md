# Four-time sign fingerprints of covariance-matched resetting, Gaussian, and telegraph baths

## Finding
Fix \(D,r>0\). Three stationary scalar baths have the same two-time covariance
\[
C(s,t)=\frac{2D}{r}e^{-r|t-s|}:
\]
(i) a Brownian motion \(Y\) with diffusion coefficient \(D\), restarted at zero at independent rate \(r\); (ii) a centered stationary Ornstein–Uhlenbeck bath \(G\) with this covariance; (iii) a symmetric telegraph bath \(T\) taking the values \(\pm\sqrt{2D/r}\) and changing sign at rate \(r/2\).

For every ordered quadruple of real times \(t_1\le t_2\le t_3\le t_4\), put \(u=t_2-t_1\), \(v=t_3-t_2\), \(w=t_4-t_3\). Their connected fourth moments, \(\kappa_B=\operatorname{cum}(B_{t_1},B_{t_2},B_{t_3},B_{t_4})\), obey the exact sign trichotomy
\[
\begin{aligned}
\kappa_Y&=\frac{4D^2}{r^2}e^{-r(u+v+w)}\left(5+3ru-2e^{-rv}\right)>0,\\
\kappa_G&=0,\\
\kappa_T&=-\frac{8D^2}{r^2}e^{-r(u+2v+w)}<0.
\end{aligned}
\]
The result includes coincident observation times, arbitrary positive gaps, and all \(D,r>0\).

This distinction persists after *any nonzero positive linear filtering*: for four deterministic, nonnegative, nonzero almost-everywhere \(L^1([0,\infty))\) kernels \(h_i\), define \(Z_i^B(t_i)=\int_0^\infty h_i(s)B(t_i-s)\,ds\). Then
\[
\operatorname{cum}(Z_1^Y(t_1),\ldots,Z_4^Y(t_4))>0,\quad
\operatorname{cum}(Z_1^G(t_1),\ldots,Z_4^G(t_4))=0,\quad
\operatorname{cum}(Z_1^T(t_1),\ldots,Z_4^T(t_4))<0.
\]
All corresponding filtered pair covariances remain identical across the three baths. The statement applies in particular to four overdamped harmonic probes with positive coupling coefficients, even if the probes have different relaxation rates. Independent additive Gaussian noise changes second moments but not the displayed fourth cumulants.

## Assumptions and scope
The resetting process \(Y\) is the unique stationary version of the Markov jump-diffusion with generator
\[
(\mathcal Lf)(y)=Df''(y)+r[f(0)-f(y)]
\]
on bounded twice-differentiable test functions; all displayed polynomial expectations are finite. Its stationary law is the exponential-age mixture of \(N(0,2Da)\) over \(a\sim\operatorname{Exp}(r)\). The telegraph process has symmetric stationary signs, and the OU process is centered and stationary. All bath processes are independent of any optional additional Gaussian probe forcing. The definition of fourth cumulant is \(\mathbb E[B_1B_2B_3B_4]-\mathbb E[B_1B_2]\mathbb E[B_3B_4]-\mathbb E[B_1B_3]\mathbb E[B_2B_4]-\mathbb E[B_1B_4]\mathbb E[B_2B_3]\), because all three baths are centered. Filtering uses Lebesgue integrals in \(L^4\) and allows unequal probe times.

## Proof
**Stationarity and covariance.** The stationary reset-age construction gives \(\mathbb EY=0\), \(\mathbb E Y^2=2D/r\), and \(\mathbb E Y^4=24D^2/r^2\). If \(s<t\), resetting erases the earlier position, so \(\mathbb E[Y_t\mid Y_s=y]=e^{-r(t-s)}y\). Thus \(\operatorname{Cov}(Y_s,Y_t)=(2D/r)e^{-r(t-s)}\). The stationary OU parameters and symmetric telegraph switching rate stated above give exactly the same covariance.

**Higher conditional moments.** For \(\tau\ge0\), conditioning on whether any reset occurs and using the standard Brownian increment moments yields
\[
\begin{aligned}
\mathbb E[Y_{s+\tau}\mid Y_s=y]&=e^{-r\tau}y,\\
\mathbb E[Y_{s+\tau}^2\mid Y_s=y]&=e^{-r\tau}y^2+\frac{2D}{r}(1-e^{-r\tau}),\\
\mathbb E[Y_{s+\tau}^3\mid Y_s=y]&=e^{-r\tau}(y^3+6D\tau y).
\end{aligned}
\]
The last identity holds because the event of at least one reset gives zero conditional third moment, while on the no-reset event the increment is Gaussian. The second conditional formula follows alternatively by solving the exact generator equation for \(y^2\).

**Ordered fourth moment.** Iterating the Markov conditional-expectation formulas backward from \(t_4\) to \(t_1\), multiplying by the observed coordinate at each intermediate time, gives
\[
M_Y=\mathbb E[Y_{t_1}Y_{t_2}Y_{t_3}Y_{t_4}]
=\frac{4D^2}{r^2}e^{-r(u+w)}[1+e^{-rv}(5+3ru)].
\]
The three Gaussian pair products sum to \((4D^2/r^2)e^{-r(u+w)}[1+2e^{-2rv}]\). Subtracting gives \(\kappa_Y\). It is strictly positive because \(5+3ru-2e^{-rv}\ge3\). Gaussian cumulants of order greater than two vanish, proving the middle formula.

For the symmetric telegraph process, the Markov property and \(T^2\equiv2D/r\) give \(M_T=(4D^2/r^2)e^{-r(u+w)}\). Subtracting the same covariance pair products yields the stated negative \(\kappa_T\). This calculation holds at all boundaries by continuity.

**Filtering.** For \(h_i\in L^1\) the filtered variables exist in \(L^4\) by Minkowski's inequality and stationarity. Multilinearity and Fubini's theorem express their fourth cumulant as the integral over \([0,\infty)^4\) of the bath kernel at shifted times multiplied by \(\prod_i h_i(s_i)\). By symmetry of joint cumulants, sort the shifted observation times and apply the proven pointwise strict signs. The nonnegative product weight is positive on a set of positive four-dimensional measure, yielding strict signs. Equality of covariances is preserved under the same linear filtering; independent Gaussian perturbations contribute zero fourth connected moments and do not affect the conclusion.

## Verification
Execute `python verify.py` from the directory containing this file, with NumPy and SciPy installed. The checker independently propagates polynomial test functions through the five-dimensional Markov-generator matrix exponential rather than reusing the explicit fourth-moment formula; it also checks the filtered positive/negative sign comparison. All assertions are finite diagnostics, not substitutes for the analytic arguments above.

## Relationship to prior work
Guéneau, Majumdar and Schehr [1] introduced and analyzed an overdamped harmonic particle driven by Poisson-reset Brownian noise. In their public full-text treatment, their equation (37) gives precisely the stationary two-time covariance used here, and their Appendix G computes two-time probe correlations. The present assertion concerns the complete ordered *four-time connected* kernel and its strict sign after arbitrary positive linear filtering, which neither of those formulas states. Smith and Majumdar [2] study integrated Brownian functionals and resetting; integration of general multipoint relations is conceptually adjacent, but the explicit four-time sign kernel and comparison of three covariance-matched baths are distinct claims. Classical Gaussian Wick factorization and telegraph Markov conditioning supply the two comparison cases, not independent novelty claims.

## Limitations
The positive-filter sign criterion does not cover sign-changing response kernels, state-dependent nonlinear probes, or non-Poisson reset clocks. The theorem addresses fourth cumulants, not full statistical distinguishability from all conceivable non-Gaussian baths. No inference of unique physical microscopic mechanism from one measurement is claimed. Although relevant primary full text was inspected and semantic searches were performed, these do not certify worldwide priority; broader treatments of general resetting multipoint laws may imply particular pieces without using identical notation. Independent validation has not been performed.

## References
[1] M. Guéneau, S. N. Majumdar, G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, first public 2023-06-15, https://arxiv.org/abs/2306.09453 ; DOI: 10.1088/1751-8121/ad00ef.

[2] P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, J. Phys. A 55 (2022), https://doi.org/10.1088/1751-8121/ac677c. Related Brownian-functional framework; no claim is made that it proves the present ordered cumulant formula.
