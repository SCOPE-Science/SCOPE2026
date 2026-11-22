# A sharp hidden-energy anticorrelation frontier for a periodically bath-swapped Brownian gyrator

## Finding

For a stable two-coordinate harmonic Langevin system, periodically *exchanging* the two thermal bath temperatures leaves the **entire stationary two-time covariance matrix function** identical to that of a single-temperature equilibrium Ornstein–Uhlenbeck process when measurements are not synchronized with the switching clock. Nevertheless, the covariance of the squared observed coordinates crosses from positive to negative at one and only one switching half-period in an explicit parameter regime. The whole sign phase diagram has the sharp universal coupling boundary \(|k|/a=\sqrt{2-\sqrt3}\).

Put \(F(z)=1-\tanh(z)/z\) for \(z>0\). The exact connected energy-like covariance at a uniformly randomized observation phase is
\[
\operatorname{Cov}(X^2,Y^2)=\frac{2k^2T_0^2}{(a^2-k^2)^2}-\frac{\delta^2}{a^2}F(a\tau).
\]
The fourth cumulant of either coordinate is \(3\delta^2F(a\tau)/a^2>0\), and the mixed fourth cumulant is \(-\delta^2F(a\tau)/a^2\).

## Assumptions and scope

Fix \(a>0\), \(-a<k<a\), \(T_0>\delta>0\), and \(\tau>0\). Let \(K=\begin{psmallmatrix}a&k\\k&a\end{psmallmatrix}\), and let \(\sigma\) be the \(2\tau\)-periodic square wave with value \(+1\) on \([0,\tau)\) and \(-1\) on \([\tau,2\tau)\). With independent standard Brownian motions, consider
\[
 dX_t=-(aX_t+kY_t)\,dt+\sqrt{2(T_0+\delta\sigma(t))}\,dW_{x,t},
 \qquad
 dY_t=-(kX_t+aY_t)\,dt+\sqrt{2(T_0-\delta\sigma(t))}\,dW_{y,t}.
\]
As \(K\) is positive definite, there is a unique centered Gaussian solution in the \(2\tau\)-periodic stationary regime. Choose one random phase \(U\) uniformly from \([0,2\tau)\), independently of the Brownian noise, and shift the entire periodically stationary process by \(U\). Its resulting law is stationary, although it is generally not Gaussian. Expectations and cumulants below refer to that phase-randomized law. A single observation at an externally fixed phase remains Gaussian; this distinction is essential.

For \(h\ge0\), let \(G(h)=\mathbb E[Z_{t+h}Z_t^{\mathsf T}]\), with \(Z=(X,Y)^{\mathsf T}\), for this stationary phase-randomized process. Then
\[
 G(h)=T_0e^{-Kh}K^{-1},\qquad G(-h)=G(h)^{\mathsf T}.
\]
This is exactly the equilibrium two-time covariance, at **every lag**, with drift \(K\) and uniform temperature \(T_0\).

Define \(u=|k|/a\) and \(R=\delta/T_0\). For \(k\ne0\), the squared-position covariance is strictly decreasing with \(\tau\), is positive near \(\tau=0\), and is negative for sufficiently long half-periods if and only if
\[
 R>\frac{\sqrt2\,u}{1-u^2}.
\]
When this inequality holds, the unique zero is determined by
\[
 F(a\tau_c)=\frac{2u^2}{R^2(1-u^2)^2},
\]
and the covariance is positive for \(\tau<\tau_c\), negative for \(\tau>\tau_c\). At equality it is positive for every finite \(\tau\) and tends to zero as \(\tau\to\infty\). If the inequality fails it is positive at every finite \(\tau\). An admissible \(R<1\) satisfying the strict crossing inequality exists precisely when \(0<u<\sqrt{2-\sqrt3}\). For \(k=0\), the covariance is strictly negative for every \(\tau>0\).

## Proof

Write the conditional covariance at phase \(t\) as \(C(t)=\mathbb E[Z_tZ_t^{\mathsf T}\mid\sigma]\). The matrix Lyapunov equation is
\[
 C'(t)=-KC(t)-C(t)K+2\operatorname{diag}(T_0+\delta\sigma(t),T_0-\delta\sigma(t)).
\]
Define \(S=C_{xx}+C_{yy}\), \(H=C_{xy}\), and \(\Delta=C_{xx}-C_{yy}\). Their exact equations are
\[
 S'=-2aS-4kH+4T_0,\qquad H'=-2aH-kS,\qquad \Delta'=-2a\Delta+4\delta\sigma(t).
\]
The homogeneous \((S,H)\) subsystem is exponentially stable because \(a>|k|\). Since it has constant forcing, its unique periodic solution is constant:
\[
 S=\frac{2aT_0}{a^2-k^2},\qquad H=-\frac{kT_0}{a^2-k^2}.
\]
Consequently, with \(v=aT_0/(a^2-k^2)\) and \(c=-kT_0/(a^2-k^2)\),
\[
 C(t)=\begin{pmatrix}v+\Delta(t)/2&c\\c&v-\Delta(t)/2\end{pmatrix}.
\]
Periodic matching at the switch points gives, for \(0\le t<\tau\),
\[
 \Delta(t)=\frac{2\delta}{a}\left(1-\frac{2e^{-2at}}{1+e^{-2a\tau}}\right),\qquad
 \Delta(t+\tau)=-\Delta(t).
\]
A direct integral over the complete period yields
\[
 \overline\Delta=0,\qquad
 \overline{\Delta^2}=\frac{4\delta^2}{a^2}\left(1-\frac{\tanh(a\tau)}{a\tau}\right).
\]
Hence \(\overline C=T_0K^{-1}\). Conditional transition expectation gives \(\mathbb E[Z_{t+h}\mid Z_t,U=t]=e^{-Kh}Z_t\) for \(h\ge0\); averaging the corresponding cross-product over the phase yields \(G(h)=e^{-Kh}\overline C=T_0e^{-Kh}K^{-1}\). The reverse-lag case follows by transpose.

At each phase, the position vector is centered Gaussian. Wick's formula gives
\[
 \mathbb E[X^2Y^2\mid U=t]=C_{xx}(t)C_{yy}(t)+2C_{xy}(t)^2
 =v^2-\Delta(t)^2/4+2c^2.
\]
After phase integration, \(\operatorname{Cov}(X^2,Y^2)=2c^2-\overline{\Delta^2}/4\), proving the asserted exact formula. Also
\[
 \kappa_4(X)=3\bigl(\overline{C_{xx}^2}-\overline{C_{xx}}^{\,2}\bigr)
 =3\delta^2F(a\tau)/a^2,
 \qquad
 \kappa_{2,2}(X,Y)=-\delta^2F(a\tau)/a^2.
\]
The latter is the connected fourth cumulant with the two Wick pairings \(2\mathbb E[XY]^2\) removed. In particular \(\kappa_4(X)=-3\kappa_{2,2}(X,Y)\).

Finally, \(F(z)\to0\) as \(z\downarrow0\) and \(F(z)\to1\) as \(z\to\infty\). Its derivative is
\[
 F'(z)=\frac{\tanh z-z\operatorname{sech}^2z}{z^2}>0,
\]
since the numerator starts at zero and has derivative \(2z\operatorname{sech}^2z\tanh z>0\) for \(z>0\). Thus the crossing is unique whenever its target is strictly between zero and one. Writing the target in terms of \(u,R\) proves the contrast criterion. Solving \(\sqrt2u/(1-u^2)<1\) for \(u\in(0,1)\) gives \(u<\sqrt{2-\sqrt3}\). The zero-coupling case follows by setting \(c=0\) in the exact formula.

## Verification

The accompanying `checker.py` reconstructs the periodic conditional covariance independently by composing two full matrix Ornstein–Uhlenbeck propagators and solving a discrete Lyapunov fixed point. It integrates conditional fourth moments by 96-point Gauss–Legendre quadrature in each half-cycle, then compares all claimed covariance and fourth-cumulant expressions across a heterogeneous finite parameter grid. It also checks equilibrium-lag covariance, strict sign change and a numerical crossing example; all 639 deterministic assertions passed in a fresh execution.

For \((a,k,T_0,\delta)=(2,1/2,1,9/10)\), the exact crossover solves \(F(2\tau_c)=128/729\), hence \(\tau_c=0.408293049159024\ldots\). The squared-position covariance is positive at \(\tau=0.1\) and negative at \(\tau=0.5\). The continuum theorem is proved above; finite checks are corroboration, not its logical basis.

## Relationship to prior work

Cerasoli et al. (2022) study the two-coordinate Brownian gyrator with fixed bath temperatures, emphasizing how its Gaussian spectral fluctuations distinguish equilibrium from fixed-temperature nonequilibrium operation. Chen, Gibson and Craven (2023) study a *single underdamped coordinate coupled to two time-oscillating baths*, deriving time-dependent energetic currents and hysteresis. These are related but do not assert the present coupled, oppositely square-wave-driven two-coordinate fourth-order sign classification. The general stationary Gaussian gyrator of Dotsenko et al. (2013) is background theory, not claimed as a new result.

## Limitations

The equality of covariance functions depends on equal diagonal drift coefficients, fixed total noise temperature, independent Gaussian baths and uniform independent observation phase. It does not imply equality of full path laws, entropy production, response functions or phase-conditioned distributions. The sign change concerns \(\operatorname{Cov}(X^2,Y^2)\), not \(\operatorname{Cov}(X,Y)\) or a thermodynamic heat-current sign. The checker uses floating-point quadrature; exact uniqueness and sharpness follow analytically. Literature comparisons support a best-knowledge originality assessment, not a certification of publication priority or independent external validation.

## References

1. S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti and L. Rondoni, *Spectral fingerprints of non-equilibrium dynamics: The case of a Brownian gyrator*, arXiv:2201.04903, originally public 2022-01-13; *Physical Review E* 106, 014137 (2022). https://arxiv.org/abs/2201.04903
2. R. Chen, T. Gibson and G. T. Craven, *Energy transport between heat baths with oscillating temperatures*, *Physical Review E* 108, 024148 (published 2023-08-31). https://doi.org/10.1103/PhysRevE.108.024148
3. V. Dotsenko, A. Maciolek, O. Vasilyev and G. Oshanin, *Two-temperature Langevin dynamics in a parabolic potential* (2013). https://arxiv.org/abs/1302.4056
