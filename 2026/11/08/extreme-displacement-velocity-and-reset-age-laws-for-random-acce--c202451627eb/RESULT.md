# Extreme-displacement velocity and reset-age laws for random acceleration

## Finding

Consider a stationary, one-dimensional randomly accelerated particle whose **position and velocity are both reset to zero** by an independent rate-\(r\) Poisson clock. The stationary velocity of a particle observed at a very large nonzero displacement has a specific outward sign, a universal Gaussian fluctuation profile, and a sharp large-deviation penalty for having the wrong sign. These are conditional *snapshot* laws, not first-passage or crossing-conditioned laws.

**Theorem.** Fix any \(D,r>0\). Write \(X,V\) for the stationary position and velocity, and \(T\) for the elapsed time since the most recent reset. For every \(x\ne0\) define

\[
\sigma=\operatorname{sgn}(x),\qquad
\tau_x=\left(\frac{9x^2}{4Dr}\right)^{1/4},\qquad
\Lambda_x=r\tau_x,\qquad
v_x=\sqrt{Dr}\,\tau_x.
\]

All following statements are under a regular conditional law given \(X=x\), in the limit \(|x|\to\infty\) with \(D,r\) fixed.

1. Define the oriented scaled velocity \(U_x=\sigma V/v_x\). It satisfies a full large-deviation principle on \(\mathbb R\), with speed \(\Lambda_x\) and good rate function

\[
I(u)=\inf_{z>0}\left\{z+\frac{1}{3z^3}+\frac{(u-z^{-1})^2}{z}\right\}-\frac43.
\]

The unique zero of \(I\) is \(u=1\). In particular, \(U_x\to1\) in conditional probability, and the conditional probability of a non-outward velocity obeys the sharp logarithmic asymptotic

\[
\lim_{|x|\to\infty}\frac{1}{\Lambda_x}
\log\Pr(\sigma V\le0\mid X=x)
=-\frac{4}{3}(\sqrt2-1).
\]

2. Define centered, dimensionless age and velocity fluctuations

\[
A_x=\frac{T-\tau_x}{\sqrt{\tau_x/r}},\qquad
B_x=\frac{V-\sigma v_x}{\sqrt{D\tau_x}}.
\]

Then, jointly,

\[
(A_x,B_x)\ \Longrightarrow\
\mathcal N_2\!\left(0,
\begin{pmatrix}
1/4&-\sigma/4\\
-\sigma/4&3/4
\end{pmatrix}\right).
\]

Thus the limiting age–velocity correlation is \(-\sigma/\sqrt3\), and

\[
\frac{\operatorname{Var}(V\mid X=x)}{D\tau_x}\longrightarrow\frac34,
\qquad
\frac{\operatorname{Var}(T\mid X=x)}{\tau_x/r}\longrightarrow\frac14.
\]

The local curvature of the rate function is \(I(1+h)=\frac23h^2+O(h^3)\) as \(h\to0\). The outward-velocity concentration is of order \(|x|^{1/2}\), while its conditional standard deviation is of order \(|x|^{1/4}\).

## Assumptions and scope

Between complete resets, \(dV_t=\sqrt{2D}\,dW_t\) and \(dX_t=V_t\,dt\), with \((X,V)=(0,0)\) at each reset. The Brownian increments, resets, and successive renewal excursions are independent. There are no walls, confining potentials, observational measurement disturbances, or partial resets. At stationarity the Poisson backward age \(T\) is exponential with rate \(r\), and the conditional density of \(X\) is strictly positive for every \(x\ne0\); conditioning at those values is therefore unambiguous. The statements concern fixed positive \(D,r\) and \(|x|\to\infty\), not a joint zero-reset or zero-diffusivity limit.

## Proof

**1. Exact stationary mixture.** In an excursion of deterministic duration \(t\), started with zero position and velocity,

\[
X_t=\sqrt{2D}\int_0^t(t-s)\,dW_s,\qquad
V_t=\sqrt{2D}\,W_t.
\]

Their covariance entries are

\[
\operatorname{Var}X_t=\frac{2Dt^3}{3},\quad
\operatorname{Cov}(X_t,V_t)=Dt^2,\quad
\operatorname{Var}V_t=2Dt.
\]

Gaussian conditioning therefore gives the **exact** finite-age law

\[
V\mid(X=x,T=t)\ \sim\
\mathcal N\left(\frac{3x}{2t},\frac{Dt}{2}\right).
\]

Multiplying the exponential age density by the Gaussian position likelihood yields

\[
 f_{T\mid X=x}(t)=\frac{t^{-3/2}
 \exp[-rt-3x^2/(4Dt^3)]}
 {\int_0^\infty s^{-3/2}
 \exp[-rs-3x^2/(4Ds^3)]\,ds},\qquad t>0.
\]

The normalization is finite and positive whenever \(x\ne0\).

**2. Strict saddle and age localization.** The exponent

\[
F_x(t)=rt+\frac{3x^2}{4Dt^3}
\]

has its unique minimum at \(t=\tau_x\), because \(F_x'(t)=r-9x^2/(4Dt^4)\), and
\(F_x''(\tau_x)=4r/\tau_x>0\). Put \(z=t/\tau_x\). Then

\[
F_x(\tau_x z)=\Lambda_x\varphi(z),\qquad
\varphi(z)=z+\frac{1}{3z^3},\quad
\varphi(1)=\frac43,\quad
\varphi''(1)=4.
\]

The function \(\varphi\) has a unique nondegenerate global minimum at \(1\) and diverges at both endpoints of \((0,\infty)\). Standard one-dimensional Laplace estimates, including the locally smooth factor \(z^{-3/2}\), show

\[
 A_x=\sqrt{\Lambda_x}(z-1)\ \Longrightarrow\
 A\sim\mathcal N(0,1/4).
\]

They also provide uniform integrability of every fixed polynomial moment of \(A_x\) and of the needed inverse powers of \(z\), after localization; outside any fixed neighborhood of \(z=1\), the posterior mass and polynomially weighted tails are exponentially small.

**3. Full conditional large deviations.** Let \(u=\sigma v/v_x\). The conditional Gaussian variance in part 1 becomes \(z/(2\Lambda_x)\) on this velocity scale, with conditional mean \(1/z\). Consequently the exact joint conditional density of \((z,u)\) is, up to its positive normalization,

\[
 z^{-2}\exp[-\Lambda_x \Psi(z,u)],\qquad
\Psi(z,u)=z+\frac{1}{3z^3}+\frac{(u-z^{-1})^2}{z}.
\]

The continuous function \(\Psi\) is coercive on \((0,\infty)\times\mathbb R\): \(z\) cannot approach zero or infinity on a bounded sublevel set, and then neither can \(|u|\). Its unique global minimum point is \((z,u)=(1,1)\), with \(\inf\Psi=4/3\). The finite-dimensional Laplace upper and lower bounds therefore establish the joint LDP with good rate \(\Psi-4/3\). Contraction to \(u\) proves the stated full velocity LDP, including exponential tightness.

For each fixed \(z>0\), the squared Gaussian deviation \((u-z^{-1})^2/z\) is minimized over \(u\le0\) at \(u=0\). Thus the wrong-way event has exponent

\[
\inf_{z>0}\Psi(z,0)-\frac43
=\inf_{z>0}\left(z+\frac{4}{3z^3}\right)-\frac43
=\frac{4}{3}(\sqrt2-1),
\]

because its unique minimizing age ratio is \(z=\sqrt2\). The strict/open-set LDP bounds agree by approaching \(u=0\) from below, proving the exact limit. Expanding the minimization at \((z,u)=(1,1)\) gives \(\Psi(1+a,1+h)=4/3+2a^2+(a+h)^2+O((|a|+|h|)^3)\). Its minimum has \(a=-h/3+O(h^2)\), hence \(I(1+h)=2h^2/3+O(h^3)\).

**4. Joint central limit theorem.** The exact conditional law in part 1 can be realized by taking an independent \(Z\sim\mathcal N(0,1)\) and writing

\[
V=\frac{3x}{2T}+\sqrt{\frac{DT}{2}}\,Z.
\]

Since \(3x/(2\tau_x)=\sigma v_x\) and \(v_x/\sqrt{D\tau_x}=\sqrt{\Lambda_x}\), expansion at \(T=\tau_x\) yields

\[
B_x=-\sigma A_x+\frac{Z}{\sqrt2}+o_{\Pr}(1).
\]

The independence of \(Z\) from the conditioned age, plus the age limit, gives \((A_x,B_x)\Rightarrow (A,-\sigma A+Z/\sqrt2)\). This proves the displayed covariance matrix and correlation. Uniformly integrable localized moments justify the asserted limits of conditional variances, beyond merely distributional convergence.

## Verification

Run `python3 verify.py` with the Python standard library. The checker independently evaluates the exact Gaussian Schur complement using rational arithmetic, checks the zero-velocity rate minimizer and local rate curvature, performs deterministic quadrature of the exact conditioned age density, and compares conditional covariance and wrong-way logarithmic rates with their limiting values. The finite numerical tests are not substitutes for the Laplace-principle and central-limit proofs above.

A representative check with dimensionless saddle parameter \(\Lambda_x=300\) gives a wrong-way logarithmic rate approximately \(0.565443412\), converging toward \(4(\sqrt2-1)/3\approx0.552284750\). The code verifies the conditional age variance \(1/4\), velocity variance \(3/4\), and normalized age–velocity covariance \(-1/4\) at increasing saddle parameter. For negative \(x\), the covariance sign reverses by spatial symmetry.

## Relationship to prior work

Prashant Singh, *Random acceleration process under stochastic resetting* (arXiv:2007.05576v1, 10 July 2020), establishes the full stationary position–velocity mixture for complete resetting and the stretched-exponential stationary **position** tail (particularly section 3.1 and Appendix A). The present result does not claim novelty for that mixture or tail. It extracts a different, conditional observable: the entire extreme-displacement velocity LDP, its explicit wrong-way exponent, and a coupled age–velocity Gaussian fluctuation limit.

Meerson, *Mortal Brownian motion: three short stories* (arXiv:1903.03963v1, 10 March 2019), gives the area law of a Brownian motion stopped at an exponential time, equivalent at cycle endpoints to the position distribution underlying the present posterior age saddle; it does not supply a snapshot-conditioned terminal velocity LDP.

Montero, Palassini and Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes* (arXiv:2312.13968v1, 21 December 2023), analyze Rice-type crossing intensities and a stationary position marginal, including its saddle-point approximation (sections II, IV–V). A crossing-weighted velocity law is not the ordinary stationary snapshot law conditioned on \(X=x\); the inspected portions do not supply the present conditional LDP or joint age–velocity limit.

Olsen and Löwen, *Dynamics of inertial particles under velocity resetting* (arXiv:2401.12685v1, 23 January 2024), primarily reset velocity while position remains unreset. That process has different stationary properties and does not cover the present complete-reset conditional law. General contraction/Laplace methods underpin the proof and are not claimed as novel.

## Limitations

The model requires exact, simultaneous complete resets of position and velocity to zero; position-only or velocity-only resetting may not have this stationary joint distribution. The asymptotics apply to a stationary observation at a specified position, not an absorbing target, first arrival, or the size-biased law of velocities at crossing instants. The explicit large-deviation profile is given as a variational formula; uniqueness of its minimizer for every remote velocity value is not asserted. Neither a non-asymptotic error bound nor an independent external validation is claimed. Since the underlying exact joint stationary mixture is published, these asymptotic consequences may ultimately be judged derivable from prior formulas without being separately new in publication priority.

## References

1. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576v1 (2020-07-10), https://arxiv.org/abs/2007.05576 ; journal DOI: 10.1088/1751-8121/abaf2d.
2. M. Montero, M. Palassini and J. Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes*, arXiv:2312.13968v1 (2023-12-21), https://arxiv.org/abs/2312.13968 ; DOI: 10.1103/PhysRevE.110.014116.
3. B. Meerson, *Mortal Brownian motion: three short stories*, arXiv:1903.03963v1 (2019-03-10), https://arxiv.org/abs/1903.03963.
4. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (2024-01-23), https://arxiv.org/abs/2401.12685.
5. American Mathematical Society, *Mathematics Subject Classification 2020*, category 82C31, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C26.
