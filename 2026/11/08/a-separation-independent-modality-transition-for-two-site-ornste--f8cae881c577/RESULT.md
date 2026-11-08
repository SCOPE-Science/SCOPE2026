# A separation-independent modality transition for two-site Ornstein–Uhlenbeck resetting

## Finding

Let \(\kappa,D,r,b>0\). An Ornstein–Uhlenbeck particle evolves according to \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\) between independent Poisson resets of rate \(r\). Each reset replaces the position by \(+b\) or \(-b\), independently, with equal probabilities. Its unique stationary law has a positive, even, continuous density \(p\), and its complete modality classification is

- \(0<r<\kappa\): \(p\) decreases strictly with \(|x|\); the origin is its unique mode.
- \(r=\kappa\): \(p\) is exactly constant on \([-b,b]\), and decreases strictly with \(|x|\) outside that interval. The entire interval is the set of modes.
- \(r>\kappa\): \(p\) increases strictly on \((0,b)\), decreases strictly on \((b,\infty)\), and has precisely two modes, at \(\pm b\); the origin is a strict local minimum.

The threshold \(r=\kappa\) is independent of the noise strength and reset-site separation. The reset sites are cusps of the density for every \(r>0\). At the threshold the full stationary density is explicit. Put

\[
a=\frac{\kappa}{2D},\qquad F_a(y)=\int_y^\infty e^{-a z^2}\,dz,\qquad H=a e^{ab^2}F_a(b).
\]

Then

\[
p(x)=\begin{cases}H,&|x|\le b,\\[2pt]H\,F_a(|x|)/F_a(b),&|x|>b.\end{cases}
\]

Furthermore, its stationary mass on the plateau is \(2bH\), strictly increasing from zero to one as the dimensionless site separation \(b\sqrt{\kappa/(2D)}\) increases from zero to infinity.

## Assumptions and scope

The spatial domain is the entire real line. The Brownian motions between resets are independent of the rate-\(r\) Poisson clock and of the independent fair reset-site choices. Resetting is instantaneous. All four parameters are finite and strictly positive. The stationary density exists for every such parameter choice and is unique. Modes refer to global maximizers of the continuous stationary density; the claimed monotonicity also describes all local extrema. The classification is for an equal-weight, two-atom resetting distribution, not arbitrary resetting laws or renewal clocks.

## Proof

**1. Stationary renewal representation.** The transition law of an unreset process starting from \(y\) at age \(t>0\) is Gaussian with mean \(ye^{-\kappa t}\) and variance \(v_t=(D/\kappa)(1-e^{-2\kappa t})\). Writing \(\varphi_v(z)=(2\pi v)^{-1/2}\exp(-z^2/(2v))\), the invariant density is

\[
p(x)=\frac r2\int_0^\infty e^{-rt}\bigl[\varphi_{v_t}(x-be^{-\kappa t})+\varphi_{v_t}(x+be^{-\kappa t})\bigr]dt.\tag{1}
\]

This is a probability density, positive everywhere and even. Coupling two instances at their first common reset (using the same reset event and choice thereafter) proves uniqueness, with total-variation distance at most \(e^{-rt}\). For \(x\) away from the two reset sites, Gaussian heat-kernel regularity gives differentiability twice in \(x\); the integral is continuous on the entire line because the short-time spatial singularities are integrable in one dimension. Equation (1) yields in the distributional sense

\[
D p''+\kappa(xp)'-rp+\frac r2\bigl(\delta_{-b}+\delta_b\bigr)=0,\tag{2}
\]

and consequently \(D[p'(b+)-p'(b-)]=-r/2\), with the analogous jump at \(-b\). The density is therefore continuous with nonzero downward derivative jump at \(+b\).

**2. A forced derivative sign on the reset-free central interval.** Away from \(\pm b\), (2) reduces to

\[
D p''+\kappa xp'+(\kappa-r)p=0.
\]

With \(a=\kappa/(2D)\), multiplication by the integrating factor gives the exact derivative identity

\[
\big(e^{a x^2}p'(x)\big)'=\frac{r-\kappa}{D}e^{a x^2}p(x).
\]

Evenness and regularity at zero imply \(p'(0)=0\). Integration on \(0<x<b\) therefore gives

\[
p'(x)=\frac{r-\kappa}{D}e^{-a x^2}\int_0^x e^{a y^2}p(y)\,dy.\tag{3}
\]

The integral is strictly positive. Thus \(p'(x)<0\) for \(r<\kappa\), \(p'(x)=0\) for \(r=\kappa\), and \(p'(x)>0\) for \(r>\kappa\), everywhere in \((0,b)\). This gives *global* strict monotonicity there, not just a local-curvature condition at the origin.

**3. Strict decrease beyond the reset sites.** For every \(x>b\), every \(t>0\), and either Gaussian mean \(m=\pm be^{-\kappa t}\), one has \(x-m>0\) and \(\partial_x\varphi_{v_t}(x-m)=-(x-m)\varphi_{v_t}(x-m)/v_t<0\). Differentiating (1) by dominated convergence on compact subsets of \((b,\infty)\) yields \(p'(x)<0\) there. The signs in step 2, symmetry, and continuity at the reset sites now prove each asserted modality and the absence of any other modes. The derivative jump in step 1 identifies the strict maxima at the reset sites when \(r>\kappa\).

**4. Exact critical plateau.** When \(r=\kappa\), equation (3) forces the density to be constant, say \(H\), throughout \([-b,b]\). For \(x>b\), the homogeneous equation becomes \(Dp''+\kappa x p'=0\); the integrable, decaying solutions have the form \(p(x)=C F_a(x)\), since \(F_a'(x)=-e^{-ax^2}\). Continuity at \(b\) imposes \(C=H/F_a(b)\). The jump in step 1 gives

\[
D\left[-\frac{H e^{-ab^2}}{F_a(b)}-0\right]=-\frac\kappa2,
\]

so \(H=a e^{ab^2}F_a(b)\). The given piecewise density follows by symmetry. Normalization may be checked without assuming it: \(\int_b^\infty F_a(x)dx=e^{-ab^2}/(2a)-bF_a(b)\), hence \(2bH+2H F_a(b)^{-1}\int_b^\infty F_a(x)dx=1\).

Finally put \(z=\sqrt a\,b>0\). The plateau mass has the integral representation

\[
2bH=2z e^{z^2}\int_z^\infty e^{-u^2}du
=\int_0^\infty\exp\!\left(-s-\frac{s^2}{4z^2}\right)ds.\tag{4}
\]

The integrand increases strictly in \(z\) for every \(s>0\), and dominated convergence gives limits zero and one. This proves the remaining assertion.

## Verification

The provided standalone program `verify_modes.py` evaluates (1) using positive midpoint quadrature of a transformed age variable. It tests monotonicity in all three regimes for fifteen parameter combinations, checks the explicit critical plateau and normalization, and verifies strict decrease beyond the reset sites. At preparation it returned `PASS: 291 finite quadrature assertions across 15 parameter configurations`. This is numerical corroboration, not a proof of statements about all parameters, all positions, or the continuous critical density. The analytical proof above uses positivity, a Green-function derivative identity, and an explicit ODE solution; no unreported numerical optimization is needed.

To replay, run `python3 verify_modes.py` using Python 3 and the standard library. The numerical checks have a finite integration cutoff and midpoint error and therefore do not establish the infinite-domain assertions.

## Relationship to prior work

Olsen (2023), *Steady-state moments under resetting to a distribution* (arXiv:2310.04840, first version posted 7 October 2023), derives the general stationary renewal representation and all steady-state moments for Ornstein–Uhlenbeck dynamics with arbitrary reset-position distributions. Its Section III and example focus on moments and Gaussian reset distributions. The renewal integral in step 1 is an instance of that prior representation; the new statement is the exact *shape classification* for a symmetric two-site reset law, including the separation-independent threshold and critical flat-density formula. It is not claimed that the underlying renewal or Fokker–Planck machinery is new.

Trajanovski et al. (2023), *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting* (arXiv:2301.12304), develop OU propagators and single-position resetting resolvents in several geometries; their fixed-site analysis does not compare symmetric competing reset sources or classify density modes. The exact result here is a comparison of statements rather than just paper titles; neither cited paper states an all-separation transition from a unique central maximum through a whole critical plateau to two reset-site maxima. An unindexed general theorem about Sturm–Liouville Green functions or distributed resetting could imply the classification, so originality remains subject to external literature review.

## Limitations

The proof requires a one-dimensional OU drift, constant positive diffusivity, equal reset-site probabilities and Poisson reset times. For unequal weights, the critical interval need not be flat; for three or more reset sites the global mode structure can differ. Nothing is claimed about nonstationary transients, finite-sample mode estimation, multidimensional OU systems, or nonlinear confining potentials. Numerical checks validate selected cases only. The literature comparison is best-knowledge, not a proof of publication priority or an independent audit.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E 108, 044120 (2023); arXiv:2310.04840, version 1 posted 2023-10-07. https://arxiv.org/abs/2310.04840 ; https://doi.org/10.1103/PhysRevE.108.044120 .
2. P. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (2023). https://arxiv.org/abs/2301.12304 .
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters 106, 160601 (2011), arXiv:1102.2704. https://arxiv.org/abs/1102.2704 .
