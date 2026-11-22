# A unique annular quadrupole maximum in weakly swimming escape from an absorbing disk

## Finding

A small swimming velocity produces a second-angular-harmonic (quadrupolar) response of the mean time to reach a fully absorbing circular wall. This second-order response is positive at every noncentral interior starting radius and has **exactly one radial maximum**, for every positive rotational diffusivity. The position of the maximum crosses over from a universal interior fraction to a narrow layer against the absorbing boundary as rotational diffusion increases.

Let \(I_j\) denote the modified Bessel function of the first kind of integer order \(j\), and put \(k=\sqrt{q/D}\). Define the coefficient \(H_q(\rho)\) of \(v^2\cos(2\psi)\) in the mean first-exit-time expansion. It is exactly

\[
H_q(\rho)=\frac{Rk}{12Dq^2 I_1(kR)}\left[I_2(k\rho)-\frac{I_2(kR)}{I_2(2kR)}I_2(2k\rho)\right].
\]

For all \(D,R,q>0\), \(H_q(0)=H_q(R)=0\), \(H_q(\rho)>0\) for every \(0<\rho<R\), and \(H_q\) has one and only one interior critical point \(\rho_*\), a strict maximum. More precisely,

\[
\lim_{q\downarrow0}H_q(\rho)=\frac{\rho^2(R^2-\rho^2)}{192D^3},\qquad
\lim_{q\downarrow0}\rho_*/R=\frac1{\sqrt 2},
\]

uniformly on closed radial subintervals, whereas

\[
\lim_{q\to\infty}\sqrt{q/D}\,(R-\rho_*)=\log2,
\qquad
H_q(\rho_*)\sim\frac{R}{48D^{3/2}q^{3/2}}.
\]

The strong-rotational-diffusion near-wall profile is explicit: for every fixed \(s\ge0\),

\[
H_q(R-s/k)\sim \frac{Rk}{12Dq^2}\bigl(e^{-s}-e^{-2s}\bigr)
\]

when \(s>0\), with an absolute-error version also valid at \(s=0\).

## Assumptions and scope

Consider the stochastic differential equations in a disk \(\{x\in\mathbb R^2:|x|<R\}\):

\[
dX_t=v(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2D}\,dW_t,\quad
d\Theta_t=\sqrt{2q}\,dB_t,
\]

where \(D,R,q>0\), \(W\) is planar standard Brownian motion, \(B\) is independent scalar Brownian motion, and the process is killed at the first hit of \(|X_t|=R\). For initial polar radius \(\rho>0\), set \(\psi=\Theta_0-\arg X_0\), and write \(T_v(\rho,\psi)=\mathbb E\tau\). The heading-angle convention is irrelevant at \(\rho=0\), where regularity is interpreted in Cartesian coordinates.

At fixed positive \(D,R,q\), the Dirichlet elliptic backward operator admits an analytic expansion in sufficiently small real \(v\). For \(0<\rho<R\),

\[
T_v(\rho,\psi)=\frac{R^2-\rho^2}{4D}+vF_q(\rho)\cos\psi
+v^2\bigl[G_q(\rho)+H_q(\rho)\cos(2\psi)\bigr]+O(v^3),
\]

where the remainder is uniform on compact interior sets, and in fact can be controlled by a bounded Dirichlet resolvent for small \(v\). The radial coefficients \(F_q\), \(G_q\) are also explicitly characterized below. Only the quadrupole coefficient is the principal asserted result.

## Proof

**1. The backward hierarchy.** The mean exit time is the unique Dirichlet solution of

\[
\bigl[D\Delta_x+q\partial_\Theta^2+v\mathbf e_\Theta\cdot\nabla_x\bigr]T_v=-1.
\]

Uniform ellipticity in the compact position-angular cylinder, plus the spectral gap of the zero-boundary passive generator, makes \((-L_0)^{-1}(\mathbf e_\Theta\cdot\nabla)\) bounded on a suitable Dirichlet Sobolev scale. Its Neumann series gives analyticity for \(v\) in a neighborhood of zero. The passive solution is \(T_0=(R^2-\rho^2)/(4D)\). Writing \(T_1=F_q(\rho)\cos\psi\) gives

\[
D\bigl(F_q''+F_q'/\rho-F_q/\rho^2\bigr)-qF_q=\rho/(2D),
\qquad F_q(R)=0,
\]

with regularity at the origin. Thus

\[
F_q(\rho)=\frac{R I_1(k\rho)/I_1(kR)-\rho}{2Dq}.
\]

**2. Second-order harmonic projection.** In radial-relative-angle variables, the advection operator is

\[
\mathcal A=\cos\psi\,\partial_\rho-\frac{\sin\psi}{\rho}\partial_\psi.
\]

Consequently, \(\mathcal A(F_q\cos\psi)=\tfrac12(F_q'+F_q/\rho)+\tfrac12(F_q'-F_q/\rho)\cos2\psi\). Writing \(T_2=G_q+H_q\cos2\psi\), the two Dirichlet equations become

\[
D(G_q''+G_q'/\rho)=-\tfrac12(F_q'+F_q/\rho),
\quad G_q'=-F_q/(2D),\quad G_q(R)=0,
\]

and

\[
D\left(H_q''+\frac{H_q'}\rho-\frac{4H_q}{\rho^2}\right)-4qH_q
=-\frac12\left(F_q'-\frac{F_q}\rho\right),\qquad H_q(R)=0.
\]

The Bessel identity \(I_1'(z)-I_1(z)/z=I_2(z)\) gives

\[
F_q'-F_q/\rho=\frac{Rk}{2DqI_1(kR)}I_2(k\rho).
\]

The radial operator on \(I_2(k\rho)\) equals \(k^2 I_2(k\rho)\), while on \(I_2(2k\rho)\) it equals \(4k^2 I_2(2k\rho)\). Hence a particular solution is \(RkI_2(k\rho)/(12Dq^2I_1(kR))\), and the regular homogeneous solution is proportional to \(I_2(2k\rho)\). Imposing \(H_q(R)=0\) yields the boxed expression.

**3. Strict positivity and unique maximum.** Every coefficient of the power series of \(I_2(z)/z^2\) is strictly positive. Thus the ratio \(I_2(2z)/I_2(z)\) is strictly increasing for positive \(z\) (it is a positive-coefficient weighted average of the strictly increasing sequence \(4^j\)). For \(0<\rho<R\), this ratio inequality gives \(H_q(\rho)>0\). Regularity yields \(H_q(0)=0\), and the Dirichlet condition gives \(H_q(R)=0\).

Let \(L=kR\) and \(c=I_2(L)/I_2(2L)\). The sign of \(H_q'(\rho)\) equals that of \(A(k\rho)-c\), where

\[
A(z)=\frac{I_2'(z)}{2I_2'(2z)}.
\]

The positive power series \(I_2'(z)/z=\sum_{j\ge0}a_jz^{2j}\), with all \(a_j>0\), gives the strict decrease of \(A\) from \(A(0+)=1/4\). Meanwhile \(c<1/4\), and \(A(L)<c\) follows from the strictly positive derivative of \(I_2(2z)/I_2(z)\) at \(z=L\). The intermediate value theorem and strict monotonicity show exactly one zero of \(H_q'\), separating increasing and decreasing portions. No other local extrema exist.

**4. Endpoint regimes.** Expanding \(I_1\) and \(I_2\) at zero and canceling the leading quadratic terms gives \(H_q(\rho)\to\rho^2(R^2-\rho^2)/(192D^3)\), with one maximum at \(R/\sqrt2\). The exact unique-maximizer equation and convergence of derivatives imply \(\rho_*/R\to1/\sqrt2\).

For \(L\to\infty\), standard modified-Bessel asymptotics, uniformly for bounded \(s=k(R-\rho)\), show

\[
\frac{I_2(k\rho)}{I_1(kR)}=e^{-s}(1+o(1)),\qquad
\frac{I_2(L)I_2(2k\rho)}{I_2(2L)I_1(L)}=e^{-2s}(1+o(1)).
\]

The derivative root equation gives \(\rho_*=R-O(1/k)\) and then \(k(R-\rho_*)\to\log2\). Evaluating the profile at that unique peak gives the height constant, since \(\max_{s\ge0}(e^{-s}-e^{-2s})=1/4\), attained only at \(s=\log2\).

## Verification

The embedded `check.py` computes the exact Bessel formula and derivative for seven distinct positive rotational diffusivities, checks positivity and derivative signs across an interior grid, locates the unique candidate maximum, verifies the second-harmonic Dirichlet ODE residual at four further diffusivities and multiple interior radii, and confirms the small-\(q\) limit. It requires Python 3 with NumPy and SciPy. Those finite tests are a reproducibility aid; global uniqueness and positivity rely on the power-series arguments above. One may run `python check.py` from the extracted artifact directory.

## Relationship to prior work

Di Trapani, Franosch and Caraglio (2023), *Active Brownian Particles in a Circular Disk with an Absorbing Boundary* (Phys. Rev. E 107, 064123), formulate this exact absorbing active-Brownian system and compute its propagator, survival probability and first-passage distribution. Iyaniwura and Peng (2025), *Mean first passage time of active Brownian particles in two dimensions* (New J. Phys. 27, 104401), derive the backward mean-time PDE and the exact **first angular harmonic at first order** in swimming speed; their disk calculation truncates at \(O(v^2)\) without computing its second-order coefficient. A separate published disk-susceptibility note establishes a second-order **orientation-averaged** correction and its complete monotonicity but, according to its indexed scientific summary, does not assert the present second-angular-harmonic positivity, its unique maximizer, or the sharp large-rotational-diffusion position and height. General propagator methods can in principle imply the coefficient after additional calculations, so originality is limited to the explicitly classified quadrupole coefficient and not to a new stochastic model or backward equation.

## Limitations

The assertion is a weak-swimming Taylor-coefficient theorem at fixed positive parameters, not a claim of a unique maximum of the **complete finite-swimming** mean-time function. The second harmonic vanishes at the radial center where the relative-angle coordinate is undefined. The theorem assumes a fully absorbing circular wall, independent isotropic translational and angular Brownian noise, and no chirality or hydrodynamic interactions. The high-\(q\) boundary layer is an asymptotic statement for the coefficient alone. Earlier broader exact propagator formulas and unindexed equivalent calculations remain priority risks; independent assessment has not been performed.

## References

1. F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian particles in a circular disk with an absorbing boundary*, Phys. Rev. E **107**, 064123 (2023), first journal publication June 21, 2023. DOI: https://doi.org/10.1103/PhysRevE.107.064123 . Preprint: https://arxiv.org/abs/2306.12702 .
2. S. A. Iyaniwura and Z. Peng, *Mean first passage time of active Brownian particles in two dimensions*, New J. Phys. **27**, 104401 (2025), https://arxiv.org/abs/2506.15813 . Full text: https://zhiweipeng.com/assets/pdf/IP2025.pdf .
3. *Completely monotone weak-activity escape susceptibility for an absorbing active-Brownian disk*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-completely-monotone-weak-activity-escape-susceptibility-for-an-a--b7fecaf47750 .
