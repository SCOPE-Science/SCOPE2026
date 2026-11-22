# Sharp magnetic memory transition under position-only resetting of inertial Brownian motion

## Finding

A charged inertial Brownian particle in a constant transverse magnetic field undergoes complete spatial Poisson resets while its thermal velocity is never reset. Its stationary Cartesian position autocovariance has a sharp boundary between finitely and infinitely many temporal sign reversals. Write \(r\) for the position-reset rate, \(\gamma\) for the velocity damping, and \(\omega\) for the nonzero cyclotron frequency. For any \(r,\gamma,\omega>0\), the covariance has **infinitely many positive and negative time-lag intervals** if and only if

\[
r>\gamma\quad\text{or}\quad
\bigl(r=\gamma\ \text{and}\ 0<\omega<\gamma/\sqrt{2}\bigr).
\]

When \(r<\gamma\), the covariance is eventually strictly positive and has only finitely many sign changes. At \(r=\gamma\), it is strictly positive at every lag if \(\omega>\gamma/\sqrt2\); at \(\omega=\gamma/\sqrt2\) it has infinitely many isolated tangential zeroes but no negative values. These classifications hold at every positive thermal intensity and are independent of its magnitude.

## Assumptions and scope

Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). Consider a two-dimensional position \(X_t\) and velocity \(V_t\) with dynamics between independent rate-\(r\) Poisson events

\[
dX_t=V_t\,dt,\qquad
dV_t=(-\gamma I+\omega J)V_t\,dt+\sqrt{2\gamma\Theta}\,dW_t,
\]

where \(r,\gamma,\omega,\Theta>0\) and \(W\) is standard planar Brownian motion. At each Poisson event set \(X_t=0\) without changing \(V_t\), its Brownian driver, or the future Poisson-clock law. The model contains no additional positional diffusion, mechanical trap, particle interaction, or velocity rethermalization. All expectations below are taken in its unique stationary state. Denote the one-component autocovariance by \(C(t)=\mathbb E[X_1(0)X_1(t)]\) for \(t\ge0\). Its stationary mean vanishes by inversion symmetry.

## Proof

**Stationary mixed moments.** The velocity remains a stationary rotational Ornstein–Uhlenbeck process with \(\mathbb E[V(0)V(0)^{\mathsf T}]=\Theta I\). Put \(D=(r+\gamma)^2+\omega^2\). The stationary generator equations for \(X_1V_1\), \(X_1V_2\) and \(X_1^2\) give, respectively,

\[
(r+\gamma)b_1+\omega b_2=\Theta,\qquad
(r+\gamma)b_2=\omega b_1,\qquad
rS=2b_1,
\]

where \(b_j=\mathbb E[X_1V_j]\) and \(S=\mathbb E[X_1^2]\). Thus

\[
b_1=\frac{\Theta(r+\gamma)}{D},\qquad
b_2=\frac{\Theta\omega}{D},\qquad
S=\frac{2\Theta(r+\gamma)}{rD}>0.
\]

These moments are finite: the last Poisson age has an exponential distribution and the stationary velocity covariance decays exponentially. The exact stationary representation is the integral of the uninterrupted velocity trajectory since its most recent reset, so the generator identities apply without an assumed renewal of velocity.

**Exact lag covariance.** Conditional on the present velocity, its future expectation is \(e^{(-\gamma I+\omega J)t}V_0\). Therefore

\[
\mathbb E[X_1(0)V_1(t)]
=e^{-\gamma t}\bigl(b_1\cos\omega t-b_2\sin\omega t\bigr).
\]

The reset generator acting on the future coordinate gives the exact first-order equation

\[
C'(t)+rC(t)=\mathbb E[X_1(0)V_1(t)],\qquad C(0)=S.
\]

Integration yields, for every \(t\ge0\),

\[
\boxed{\displaystyle
C(t)=Se^{-rt}+\Theta\operatorname{Re}\!\left[
\frac{e^{(-\gamma+i\omega)t}-e^{-rt}}
{(r+\gamma-i\omega)(r-\gamma+i\omega)}\right].}
\]

In particular, the covariance is real analytic in nonnegative time and has \(C(0)=S>0\).

**Slow resets.** For \(0<r<\gamma\), separate the reset exponential:

\[
C(t)=Ae^{-rt}+\Theta e^{-\gamma t}\operatorname{Re}\!\left[
\frac{e^{i\omega t}}{(r+\gamma-i\omega)(r-\gamma+i\omega)}\right],
\]

where direct common-denominator simplification gives

\[
A=\frac{\Theta\bigl[(r-\gamma)(r-2\gamma)(r+\gamma)+(r+2\gamma)\omega^2\bigr]}
{r\bigl[(r-\gamma)^2+\omega^2\bigr]\bigl[(r+\gamma)^2+\omega^2\bigr]}.
\]

All factors in the denominator are positive. Both \(r-\gamma\) and \(r-2\gamma\) are negative, so both terms in the numerator are positive: \(A>0\). Consequently \(e^{rt}C(t)\to A>0\). The analytic, nonidentically-zero covariance has only finitely many zeroes on each compact time interval, and no sufficiently late zeroes; hence only finitely many sign changes overall.

**Fast resets.** For \(r>\gamma\), the nonzero damped harmonic above is asymptotically dominant, with coefficient of modulus \(\Theta/\bigl| (r+\gamma-i\omega)(r-\gamma+i\omega)\bigr|>0\). Its cosine-like factor has alternating strictly positive and negative values at arbitrarily large times. The faster-decaying reset exponential cannot remove these alternating signs. Continuity then gives infinitely many distinct positive and negative time-lag intervals.

**Resonant reset rate.** At \(r=\gamma\), exact simplification instead yields

\[
\boxed{\displaystyle
C(t)=\frac{\Theta e^{-\gamma t}}{4\gamma^2+\omega^2}
\left[3+\cos(\omega t)+\frac{2\gamma}{\omega}\sin(\omega t)\right].}
\]

The bracket has minimum \(3-\sqrt{1+4\gamma^2/\omega^2}\), strictly negative, zero, or strictly positive according as \(\omega<\gamma/\sqrt2\), \(\omega=\gamma/\sqrt2\), or \(\omega>\gamma/\sqrt2\). For a negative minimum, periodicity provides infinitely many intervals of each sign. At equality, the nonnegative periodic bracket has infinitely many isolated zeros of even multiplicity and never changes sign. Above equality it is strictly positive. Combining the cases proves the stated sharp classification.

## Verification

The standalone reproducibility script `check.py` tests the closed complex-resolvent formula against a separate real \(3\times3\) matrix-exponential covariance evolution at \(360\) parameter/time combinations; it independently compares the stationary variance to a Laplace quadrature of the velocity autocorrelation and tests the critical trigonometric amplitude and positive slow-reset prefactor. The script reports `PASS: 436 matrix, integral, and sharp-boundary checks.` These numerical tests supplement, but do not replace, the exact sign proof above. Execute from a Python environment with NumPy and SciPy using `python check.py`.

## Relationship to prior work

Gupta's 2018 preprint studies one-dimensional underdamped Brownian motion with position-only resetting and obtains position distributions, not the magnetically induced planar time-lag sign-classification here. Abdoli and Sharma's 2020 preprint studies Lorentz-influenced active Brownian particles with resetting to a line and analyzes steady density, polarization, current and first-passage time, not the present complete planar-position-reset covariance. Olsen and Löwen's 2024 treatment studies velocity-only resetting with position retained, an opposite reset channel. The exact two-point signal and the codimension-two resonant threshold are not logical consequences of the statements checked in those works. The underlying OU covariance, reset generator and trigonometric amplitude method are standard and not presented as new.

## Limitations

The theorem classifies whether *infinitely many* sign reversals occur, not the exact number or locations of possible finite-time negative bands when \(r<\gamma\). It concerns the specified linear planar inertial model and one Cartesian component, with positive nonzero magnetic frequency. A zero-frequency limit must be treated separately; there is no claim of oscillations there. Results are exact for ideal Poisson resets and stationarity. This is not a statement about measurement feasibility at arbitrarily late times, because the covariance amplitude decays exponentially. Broader implicit prior coverage cannot be ruled out without independent literature review.

## References

1. D. Gupta, *Stochastic resetting in underdamped Brownian motion*, arXiv:1812.07227 (first public 2018-12-18), https://arxiv.org/abs/1812.07227.
2. I. Abdoli and A. Sharma, *Stochastic resetting of active Brownian particles with Lorentz force*, arXiv:2010.02103 (first public 2020-10-05), https://arxiv.org/abs/2010.02103.
3. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (first public 2024-01-23), https://arxiv.org/abs/2401.12685.
