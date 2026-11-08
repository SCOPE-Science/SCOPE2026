# Exact isotropic escape susceptibility and a rotational boundary layer in an absorbing disk

## Finding
For an active Brownian particle in a two-dimensional, fully absorbing disk, the leading nonzero weak-swimming correction to its orientation-averaged mean exit time has an exact modified-Bessel form. It is strictly negative at every interior starting radius, becomes strictly less negative as rotational diffusion increases, and has a nonuniform, universal high-rotation boundary layer.

Write the disk radius as \(R>0\), translational diffusivity as \(D>0\), propulsion speed as \(v\geq0\), and rotational diffusivity as \(D_{\mathrm{rot}}\geq0\). For a starting position of radius \(R\rho\), \(0\leq\rho<1\), with an initially uniform, independent heading, set \(w=vR/D\) and \(\beta=D_{\mathrm{rot}}R^2/D\). The dimensionless mean exit time satisfies, as \(w\to0\),
\[
\frac{D}{R^2}\mathbb E\tau_v=\frac{1-\rho^2}{4}+w^2g_\beta(\rho)+O_{\beta,\rho}(w^4).
\]
For \(\beta>0\), with \(k=\sqrt\beta\) and modified Bessel functions \(I_0,I_1\),
\[
g_\beta(\rho)=\frac{1}{4\beta}\left[\frac{I_0(k)-I_0(k\rho)}{kI_1(k)}-\frac{1-\rho^2}{2}\right],
\qquad
g_0(\rho)=-\frac{(1-\rho^2)^2}{128}.
\]
For every \(0\leq\rho<1\), the coefficient is strictly negative, strictly increasing in \(\beta\geq0\), and satisfies \(g_0(\rho)\leq g_\beta(\rho)<0\), with equality in the first comparison only at \(\beta=0\). For each fixed \(\rho<1\),
\[
\lim_{\beta\to\infty}\beta g_\beta(\rho)=-\frac{1-\rho^2}{8}.
\]
In the distinguished boundary scale \(\rho=1-z/\sqrt\beta\), the distinct law
\[
\lim_{\beta\to\infty}\beta^{3/2}g_\beta(1-z/\sqrt\beta)
=-\frac{z-1+e^{-z}}{4}
\]
holds locally uniformly for \(z\geq0\). This boundary profile quantifies the failure of a uniform bulk expansion near the absorbing rim.

A separate, standard-Gaussian-comparison consequence provides context for the center: if the particle begins at the disk center with any initial heading independent of the translational Brownian noise, then its entire first-exit survival function is strictly decreasing in propulsion speed at every positive time. This follows from Anderson's shifted-symmetric-convex-set inequality; it is **not** claimed as a new Gaussian inequality.

## Assumptions and scope
The dynamics up to first exit are \(dX_t=v(\cos\Theta_t,\sin\Theta_t)dt+\sqrt{2D}\,dB_t\), \(d\Theta_t=\sqrt{2D_{\mathrm{rot}}}\,dW_t\), with independent standard planar Brownian motion \(B\) and scalar Brownian motion \(W\). At \(D_{\mathrm{rot}}=0\), the heading remains fixed. The process is killed on first reaching the circle \(|X|=R\), not reflected. The quadratic formula concerns a uniform distribution of initial headings independent of the noises and fixed \(0\leq\rho<1\). The propulsion limit \(w\to0\) is taken with \(\beta,\rho\) fixed; the subsequent \(\beta\to\infty\) boundary limit concerns the already-defined quadratic coefficient, not a uniform two-parameter expansion in \(w\).

## Proof
Scale space by \(R\) and time by \(R^2/D\). Write the particle's heading relative to the outward radial direction as \(\phi\). Its dimensionless backward generator is \(\mathcal L_w=\mathcal L_0+w\mathcal A\), where
\[
\mathcal L_0=\partial_{\rho\rho}+\rho^{-1}\partial_\rho+(\rho^{-2}+\beta)\partial_{\phi\phi},\qquad
\mathcal A=\cos\phi\,\partial_\rho-\rho^{-1}\sin\phi\,\partial_\phi.
\]
The expected exit time \(T_w\) solves \(\mathcal L_wT_w=-1\) with zero Dirichlet data on \(\rho=1\). Uniform ellipticity in the two spatial coordinates, boundedness of the disk, and analytic perturbation of the killed resolvent give a local power expansion in \(w\); averaging over headings removes all odd powers by the heading reversal symmetry. At zero speed, \(T_0=(1-\rho^2)/4\).

The first-order equation \(\mathcal L_0T_1=-\mathcal A T_0\) has \(T_1=f_\beta(\rho)\cos\phi\), with \(f_\beta\) regular at the origin, \(f_\beta(1)=0\), and
\[
f_\beta''+\rho^{-1}f_\beta'-(\rho^{-2}+\beta)f_\beta=\rho/2.
\]
Solving this Dirichlet modified-Bessel equation gives
\[
f_\beta(\rho)=\frac{I_1(\sqrt\beta\,\rho)/I_1(\sqrt\beta)-\rho}{2\beta},\quad\beta>0;
\qquad f_0(\rho)=\frac{\rho^3-\rho}{16}.
\]
At order two, the angle average \(g_\beta=\langle T_2\rangle_\phi\) satisfies
\[
g_\beta''+\rho^{-1}g_\beta'=-\frac12(f_\beta'+f_\beta/\rho).
\]
Regularity at \(\rho=0\) and \(g_\beta(1)=0\) force \(g_\beta'=-f_\beta/2\) and hence \(g_\beta(\rho)=\frac12\int_\rho^1f_\beta(s)\,ds\). Integrating \(I_1\) produces the displayed exact coefficient, including its continuous \(\beta=0\) limit.

For sign, \(I_1(k\rho)<\rho I_1(k)\) on \(0<\rho<1\) because \(I_1(z)/z\) is strictly increasing. Thus \(f_\beta<0\) in the interior, and so \(g_\beta<0\). Put \(h_\beta=-f_\beta\). It solves the positive Dirichlet problem
\[
(-\partial_{\rho\rho}-\rho^{-1}\partial_\rho+\rho^{-2}+\beta)h_\beta=\rho/2.
\]
If \(\beta_2>\beta_1\), the maximum principle applied to the difference implies \(0<h_{\beta_2}<h_{\beta_1}\) for \(0<\rho<1\). Integration proves strict increase of \(g_\beta\) in rotational diffusivity, including the \(\beta=0\) endpoint by continuity.

As \(k=\sqrt\beta\to\infty\), standard positive-real-argument modified-Bessel asymptotics give \(I_0(k)/(kI_1(k))\sim1/k\) and \(I_0(k\rho)/I_0(k)\to0\) at every fixed \(0\leq\rho<1\). Substitution yields the bulk limit. At \(\rho=1-z/k\), the ratio \(I_0(k-z)/I_0(k)\to e^{-z}\) uniformly on compact \(z\)-ranges; inserting \((1-\rho^2)/2=z/k-z^2/(2k^2)\) yields the stated boundary-layer function.

For the contextual center-start comparison, conditional on a continuous heading path, propulsion adds the Cameron–Martin path \(vH_t=v\int_0^t(\cos\Theta_s,\sin\Theta_s)ds\) to centered Brownian motion. At a finite time grid, remaining in any bounded, origin-symmetric convex domain is a symmetric convex Gaussian event; its shifted probability is even and log-concave in \(v\), by Gaussian log-concavity/Anderson's comparison. Dense-grid limits preserve nonincrease. For every fixed positive time, the path-shifted probability is real analytic in \(v\) by the Cameron–Martin formula, tends to zero as \(v\to\infty\), and is positive at zero, so it cannot have a flat interval. Strict inequality survives conditioning and averaging. This gives stochastic dominance for center starts only; the exact coefficient above instead covers every radius with initially uniform heading.

## Verification
Run `python checker.py` with NumPy, SciPy, SymPy, and mpmath available. The checker reconstructs the order-one and order-two zero-rotation ODE identities symbolically; evaluates the explicit Bessel coefficient against an independent radial integral at 42 parameter pairs; compares the small-speed coefficient at zero rotational diffusion with an exact drifted-disk center formula and its independent Green-kernel integral; and tests bulk/boundary asymptotics and sign/rotation monotonicity across sample parameters. These finite checks do not establish the infinite-dimensional Gaussian comparison or global asymptotics; those follow from the preceding arguments.

## Relationship to prior work
Di Trapani, Franosch and Caraglio (2023) solve the absorbing-disk active-Brownian propagator and first-passage distributions through spectral perturbation but identify the mean first-passage time and its moments as further observables. Iyaniwura and Peng (2025) formulate the backward mean-first-passage equation and give precisely the first-order radial modified-Bessel function \(f_\beta\) above (their Eq. 17); they note that isotropic heading removes that term and leaves a quadratic first nonzero correction, but do not state the resulting averaged quadratic coefficient or its high-rotation boundary profile. The first-order equation is therefore **prior work**, not a newly claimed lemma. The present exact isotropic second-order response and its boundary scaling arise from the subsequent angular-average Poisson problem. The global center-start ordering is specifically a consequence of the older Anderson Gaussian shift inequality, rather than a new probability comparison principle. Earlier one-dimensional weak-swimming results concern different geometry.

## Limitations
The quadratic expansion is a weak-speed statement, not a uniform expansion for simultaneous large rotational diffusivity and arbitrary speed. The high-rotation scaling is for its coefficient after the weak-speed limit. Orientation-sensitive or off-center all-speed monotonicity is not asserted. The full source propagator and prior first-order formula can be used to derive the present second-order expression, so mathematical derivability is explicitly acknowledged; the claimed gap is the closed isotropic coefficient and its nonuniform high-rotation classification. No uniqueness claim about undiscovered literature or independent scientific certification is made.

## References
1. F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian particles in a circular disk with an absorbing boundary*, Physical Review E 107, 064123 (public June 21, 2023), DOI: https://doi.org/10.1103/PhysRevE.107.064123 ; preprint https://arxiv.org/abs/2306.12702 .
2. S. A. Iyaniwura and Z. Peng, *Mean first passage time of active Brownian particles in two dimensions* (public June 18, 2025), https://arxiv.org/abs/2506.15813 ; especially disk weak-swimming Eqs. 12–17 and the discussion of isotropic headings.
3. T. W. Anderson, *The integral of a symmetric unimodal function over a symmetric convex set and some probability inequalities*, Proceedings of the American Mathematical Society 6 (1955), 170–176, https://doi.org/10.1090/S0002-9939-1955-0069229-1 .
4. NIST Digital Library of Mathematical Functions, modified Bessel functions and large-argument asymptotics, https://dlmf.nist.gov/10 .
