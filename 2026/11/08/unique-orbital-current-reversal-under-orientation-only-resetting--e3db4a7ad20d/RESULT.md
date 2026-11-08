# Unique orbital-current reversal under orientation-only resetting in an anisotropic harmonic trap

## Finding

Consider a swimmer that moves with fixed positive angular velocity between Poisson events which reset only its swimming angle to zero, leaving its position untouched. Under anisotropic harmonic confinement, **the stationary signed orbital circulation reverses exactly once** as the angle-reset rate increases, provided that the stiffness ratio is greater than \(3/2\). The sense of rotation between resets never reverses.

For \(a>3/2\), \(t>0\), and \(q>0\), define
\[
\begin{aligned}
P_{a,t}(q)={}&(2a-3)q^4+2(a^2-a-1)q^3\\
&+[a^2-2a+(1-6a)t^2]q^2\\
&+(1-8a-a^2)t^2q-2(a+1)(a+t^2)t^2.
\end{aligned}
\]
Then \(P_{a,t}\) has exactly one positive zero \(q_*\). The exact stationary signed area current is
\[
J=-\frac{2v^2t^3}{k}\frac{P_{a,t}(q)}{(a+1)(q^2+t^2)(q^2+4t^2)((a+q)^2+t^2)((1+q)^2+t^2)}.
\]
Consequently \(J>0\) for \(0<q<q_*\), \(J=0\) precisely at \(q=q_*\), and \(J<0\) for \(q>q_*\). At \(a=3/2\) the current is positive for every finite \(q>0\); the critical ratio \(3/2\) is also the exact boundary of the high-reset-rate current sign.

## Assumptions and scope

Fix speed \(v>0\), angular speed \(\omega>0\), weaker trap rate \(k>0\), stiffness ratio \(a=\kappa_x/k>3/2\), and reset rate \(r>0\). Put \(\kappa_y=k\), \(q=r/k\), and \(t=\omega/k\). On the planar state space \(\mathbb R^2\times S^1\), the dynamics are
\[
\begin{aligned}
\mathrm dX_s&=(-akX_s+v\cos\theta_s)\,\mathrm ds+\sqrt{2D_x}\,\mathrm dB_s^x,\\
\mathrm dY_s&=(-kY_s+v\sin\theta_s)\,\mathrm ds+\sqrt{2D_y}\,\mathrm dB_s^y,\\
\dot\theta_s&=\omega\quad\text{between Poisson resets};\qquad\theta_s\mapsto0\quad\text{at each reset}.
\end{aligned}
\]
The independent positional Brownian motions have arbitrary \(D_x,D_y\ge0\), and the rate-\(r\) Poisson clock is independent. Resets never alter \(X\) or \(Y\); there is no angular Brownian diffusion. The reset direction is aligned with the \(X\)-principal axis. The stable linear filters and regenerative angular process determine a unique stationary law with finite moments.

Define the signed circulation as the stationary Stratonovich area-production rate
\[
J=\lim_{T\to\infty}\frac1T\mathbb E\!\left[\int_0^T(X_s\circ\mathrm dY_s-Y_s\circ\mathrm dX_s)\right].
\]
The same expression holds at every time in stationarity after taking the drift expectations. Independent positional noise has vanishing cross-quadratic variation and does not contribute to this mean.

## Proof

**Stationary first and mixed angular moments.** For every positive integer \(n\), the angular generator acts on \(e^{in\theta}\) as \(in\omega e^{in\theta}+r(1-e^{in\theta})\). Therefore, writing \(m_n=\mathbb E[e^{in\theta}]\),
\[
m_n=\frac{r}{r-in\omega},\qquad \mathbb E[X]=\frac{v\operatorname{Re}m_1}{ak},\qquad\mathbb E[Y]=\frac{v\operatorname{Im}m_1}{k}.
\]
Set \(A_x=\mathbb E[Xe^{i\theta}]\) and \(A_y=\mathbb E[Ye^{i\theta}]\). The stationary generator identities (the angle jumps without positional jumps) give
\[
\begin{aligned}
(ak+r-i\omega)A_x&=\frac v2(1+m_2)+r\mathbb E[X],\\
(k+r-i\omega)A_y&=\frac v{2i}(m_2-1)+r\mathbb E[Y].
\end{aligned}
\]
These equations determine both complex mixed moments uniquely. The stationary product equation, using \(\mathrm d[X,Y]_s=0\), is
\[
(ak+k)\mathbb E[XY]=v(\operatorname{Im}A_x+\operatorname{Re}A_y).
\]
Thus
\[
\begin{aligned}
J&=(ak-k)\mathbb E[XY]+v(\operatorname{Im}A_x-\operatorname{Re}A_y)\\
&=\frac{2v}{ak+k}\bigl(ak\operatorname{Im}A_x-k\operatorname{Re}A_y\bigr).
\end{aligned}
\]
Substitution of \(m_1,m_2,A_x,A_y\), and collection over a common denominator yield the stated exact rational formula; all denominator factors are strictly positive.

**Unique reversal.** The constant term of \(P_{a,t}\) is strictly negative and its leading coefficient is strictly positive for \(a>3/2\). Its linear coefficient is negative. If its cubic coefficient is negative, then \(a<(1+\sqrt5)/2<2\), which forces its quadratic coefficient to be negative for every \(t>0\). If its cubic coefficient is nonnegative, the quadratic coefficient may have either sign, but the coefficient sequence, read from highest degree to constant, still has exactly one sign change. Descartes' rule of signs gives at most one positive root, while opposite signs at zero and infinity give at least one. Since the formula for \(J\) has an overall negative multiplier, the claimed strict signs follow. At \(a=3/2\) all nonzero coefficients of \(P_{a,t}\) are negative (its quartic term vanishes), so \(J>0\) for all finite \(q>0\).

**High-reset boundary and noise robustness.** For any fixed \(a>0\) and \(t>0\), the dominant quartic term gives
\[
J=-\frac{2v^2t^3}{k}\frac{2a-3}{a+1}\,q^{-4}+O(q^{-5})\quad(q\to\infty).
\]
At \(a=3/2\) the leading term vanishes and the exact coefficient argument gives a strictly positive current for every finite positive reset rate. The angle and mixed first-moment generator equations contain no positional diffusivity, and the independent Brownian noises have zero cross variation; therefore \(J\) is exactly independent of \(D_x,D_y\ge0\).

## Verification

The self-contained Python 3 script `verify_current.py` checks the rational formula against a separately evaluated stationary-generator moment system and a distinct reset-age numerical integration. It also brackets the unique root over 45 combinations of trap ratios and angular frequencies and checks the \(a=3/2\) boundary. Replay by running `python3 verify_current.py` with only the standard library. A completed replay gave `PASS: 237 deterministic assertions; sample root 3.381098750015`. For \(a=2\), \(t=1\), the threshold is \(q_*\approx3.381098750015\); the current at \(q=1\) equals \(0.06v^2/k\), whereas it is negative at \(q=4\). These finite tests support computation reproducibility; the all-parameter claim is established analytically above.

## Relationship to prior work

Baouche, Franosch, Meiners and Kurzthaler (2024) analyze orientation-only resetting of free-space nonchiral active Brownian motion, obtaining displacement statistics but not a confined chiral orbital current. Caprini, Löwen and Marconi (2023) investigate chirality in external, including elliptic, potentials without stochastic orientation resets. Shee (2024) studies harmonic confinement with *simultaneous positional and orientational resetting*, which is a different resetting protocol. Olsen and Löwen (2024) treat chiral swimmers with random **relative-angle tumbles** in free space and study optimization of diffusion; this rotationally equivariant tumble mechanism is not a reset of the absolute heading to a fixed laboratory direction. The present conclusion requires the joint occurrence of chirality, anisotropic confinement, and **orientation-only** resetting; changing the reset protocol changes the process and its current. Its assertion is a unique zero and direction switch for every value of the stated two dimensionless parameters, not simply an isolated numerical reversal.

## Limitations

The theorem treats deterministic angular drift and Poisson angle resets to a principal-axis direction; it does not establish the same threshold when rotational diffusivity is positive, resets have a non-Poisson waiting law, the reset direction is oblique, or positional resets occur. The high-rate expansion does not classify every intermediate-rate phenomenon when \(a<3/2\). An exact identity does not establish publication priority against all inaccessible or unindexed literature. The numerical checker is not an independent scientific audit.

## References

- Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769 (first posted 2024-05-10), https://arxiv.org/abs/2405.06769 .
- L. Caprini, H. Löwen and U. Marini Bettolo Marconi, *Chiral active matter in external potentials*, arXiv:2306.11133 (first posted 2023-06-19), https://arxiv.org/abs/2306.11133 .
- A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920 (first posted 2024-09-11), https://arxiv.org/abs/2409.06920 .
- K. Stølevik Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326 (first posted 2024-05-23), https://arxiv.org/abs/2405.14326 .
- A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (first posted 2025-01-09), https://arxiv.org/abs/2501.05149 .
- A. Shee, *Steering chiral active Brownian motion via stochastic position-orientation resetting*, arXiv:2508.12223 (2025), https://arxiv.org/abs/2508.12223 .
