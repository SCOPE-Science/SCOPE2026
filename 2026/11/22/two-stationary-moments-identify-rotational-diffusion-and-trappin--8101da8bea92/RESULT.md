# Two stationary moments identify rotational diffusion and trapping in an active Brownian particle

## Finding

Fix a spatial dimension \(d\ge2\), a calibrated propulsion speed \(v>0\), and a calibrated translational diffusion coefficient \(D\ge0\). For the stationary isotropic harmonic active Brownian model defined below, the variance \(V=\mathbb E[X_1^2]\) and fourth cumulant \(C_4=\mathbb E[X_1^4]-3V^2\) of **one Cartesian coordinate in a stationary snapshot** uniquely determine both the unknown trap-relaxation rate \(\kappa>0\) and orientation-diffusion rate \(D_r>0\).

This inverse problem has an exact attainable region. For every prescribed \(V>0\), let \(x_0\) be the unique positive solution of
\[
V=Dx_0+\frac{v^2x_0^2}{d},
\]
and define \(M(V)=\frac{6}{d+2}(V-Dx_0)^2\). A pair \((V,C_4)\) occurs at finite strictly positive rates \((\kappa,D_r)\) **if and only if**
\[
V>0,\qquad -M(V)<C_4<0.
\]
For every such pair, the physical rates are uniquely recoverable by the monotone one-dimensional inversion described in the proof. Both fourth-cumulant boundaries are sharp but not attained at finite positive rates. In contrast, variance alone never identifies the pair.

## Assumptions and scope

The stationary process in \(\mathbb R^d\) satisfies
\[
\mathrm d\boldsymbol X_t=(v\boldsymbol U_t-\kappa\boldsymbol X_t)\,\mathrm dt+\sqrt{2D}\,\mathrm d\boldsymbol W_t,
\]
where \(\boldsymbol W\) is a standard \(d\)-dimensional Brownian motion independent of the stationary orientation \(\boldsymbol U_t\in\mathbb S^{d-1}\). The heading is spherical Brownian motion with generator \(D_r\Delta_{\mathbb S^{d-1}}\). There is no torque, resetting, inertia, orientation bias, or interaction. The units of \(v\) and \(D\) are calibrated externally; \(\kappa,D_r\) are unknown positive rates. The statements refer to population stationary moments, not finite-sample estimators.

## Proof

Set \(q=D_r/\kappa>0\) and \(x=1/\kappa>0\), and define
\[
B(q)=\frac{v^2}{d[1+(d-1)q]},\qquad
F_d(q)=\frac{3+(4d-1)q}{[1+dq][3+(d-1)q]}.
\]
The stationary position is the independent sum of an active harmonic filter \(\boldsymbol X^{\mathrm a}=v\int_{-\infty}^0e^{\kappa s}\boldsymbol U_s\,\mathrm ds\) and a centered Gaussian thermal component with coordinate variance \(D/\kappa\). Therefore the fourth cumulant comes entirely from the active component.

To establish the needed active moments without assuming Gaussianity, write \(z=\kappa X_1^{\mathrm a}/v\) and \(u=U_1\), and let \(m_{a,b}=\mathbb E[z^a u^b]\). The dimensionless generator applied to \(z^a u^b\) gives, for \(a+b\) even,
\[
[a+qb(b+d-2)]m_{a,b}=a m_{a-1,b+1}+qb(b-1)m_{a,b-2}.
\]
Terms with negative exponents vanish. The orientation moments obey \(m_{0,0}=1\) and \(m_{0,b}=\frac{b-1}{b+d-2}m_{0,b-2}\) for even \(b\). Successively evaluating the recurrence yields
\[
m_{2,0}=\frac{1}{d[1+(d-1)q]},
\]
\[
m_{4,0}=\frac{3[3+(d+2)q]}{d(d+2)[1+dq][1+(d-1)q][3+(d-1)q]}.
\]
Subtracting \(3m_{2,0}^2\), then reinstating the scale \(v/\kappa\), gives the exact two-observable forward map
\[
V=Dx+B(q)x^2,\qquad
C_4=-\frac{6}{d+2}[B(q)x^2]^2F_d(q).
\]

For each fixed \(V>0\) and every \(q\ge0\), the first equation has precisely one positive solution \(x=x(q)\), since its right-hand side is strictly increasing from zero to infinity in \(x\). Since \(B'(q)<0\), implicit differentiation shows
\[
x'(q)=-\frac{B'(q)x(q)^2}{D+2B(q)x(q)}>0.
\]
Define \(A(q)=B(q)x(q)^2=V-Dx(q)>0\). Thus \(A'(q)=-Dx'(q)\le0\), including \(A(q)\equiv V\) when \(D=0\). Independently,
\[
F_d'(q)=-\frac{d(d-1)q[(4d-1)q+6]}{[1+dq]^2[3+(d-1)q]^2}<0
\]
for every \(d\ge2\) and \(q>0\). Hence \(-C_4(q)=6A(q)^2F_d(q)/(d+2)\) is **strictly decreasing and continuous** as a function of \(q\in(0,\infty)\).

At \(q\downarrow0\), \(x(q)\to x_0\), \(F_d(q)\to1\), so \(-C_4(q)\to M(V)\). At \(q\to\infty\), \(F_d(q)\to0\) while \(0<A(q)\le V\), so \(-C_4(q)\to0\). Continuity and strict monotonicity prove that every \(C_4\in(-M(V),0)\) has exactly one positive solution \(q\). Then \(\kappa=1/x(q)\), \(D_r=q/x(q)\) recover the physical rates. Both limits lie outside the finite positive-rate domain, proving sharp non-attainment. Finally, for each fixed \(V\), every \(q>0\) produces a distinct positive pair with that same variance, proving that variance alone is insufficient. \(\square\)

## Verification

The standalone standard-library checker `check.py` derives the dimensionless athermal second and fourth moments using **exact rational arithmetic and the generator recurrence**, compares the cumulant to the closed formula, and independently solves the inverse map for physical parameter grids including \(D=0\). Executing `python3 check.py` yielded **362 passed assertions**. The proof of global strict monotonicity is algebraic and not dependent on a finite grid. The delivered code does not require external datasets or proprietary libraries.

## Relationship to prior work

Chaudhuri and Dhar [1] calculate stationary radial second and fourth moments and radial kurtosis of the same active Brownian model; see in particular their equations (28), (31), (32). By isotropy, \(\mathbb E[X_1^2]=\mathbb E[|\boldsymbol X|^2]/d\) and \(\mathbb E[X_1^4]=3\mathbb E[|\boldsymbol X|^4]/[d(d+2)]\), so the two forward observables are determined by those radial moments. The additional result here is the sharp complete attainable region and global **two-parameter injectivity from only one-coordinate variance and fourth cumulant**, despite nonmonotonic kurtosis under some fixed-parameter sweeps in that paper. Frydel [2] gives a different moment recurrence and thermal convolution. Nakul and Gopalakrishnan [3] focus on stationary spatial shape transitions, and Malakar et al. [5] give a forward stationary-density series with thermal diffusion in dimension two. Related passive-optical-trap calibration by Bera et al. [4] concerns time-series inference in an ordinary Ornstein–Uhlenbeck process, not active-heading identification.

## Limitations

The result concerns structurally exact population moments; finite-sample uncertainty, experimental calibration errors, temporal correlations between sampled observations and statistical efficiency are not analyzed. If the propulsion speed or thermal diffusivity is also unknown, two observables are generally insufficient to identify all rates. The inverse is poorly conditioned as the fourth cumulant approaches zero at fixed variance. At the **lower** fourth-cumulant boundary with \(D=0\), \(C_4+M(V)=M(V)[1-F_d(q)]\sim M(V)d(d-1)q^2/3\) as \(q\downarrow0\), so the inverse loses Lipschitz regularity there as well. No generalization to anisotropic, chiral, inertial, or reset-active particles is claimed. Relevant unindexed literature may contain an equivalent inverse argument; the result is not independently peer-reviewed.

## References

1. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234 (first submitted 2020-05-28), https://arxiv.org/abs/2005.14234.
2. D. Frydel, *Active oscillator: recurrence relation approach*, arXiv:2312.05406 (first submitted 2023-12-08), https://arxiv.org/abs/2312.05406.
3. U. Nakul and M. Gopalakrishnan, *Stationary states of an active Brownian particle in a harmonic trap*, arXiv:2209.09184 (first submitted 2022-09-19), https://arxiv.org/abs/2209.09184.
4. S. Bera et al., *Fast Bayesian inference of optical trap stiffness and particle diffusion*, *Scientific Reports* **7**, 41638 (2017), https://doi.org/10.1038/srep41638.
5. K. Malakar, A. Das, A. Kundu, K. V. Kumar and A. Dhar, *Steady state of an active Brownian particle in a two-dimensional harmonic trap*, *Physical Review E* **101**, 022610 (2020), https://arxiv.org/abs/1902.04171.
