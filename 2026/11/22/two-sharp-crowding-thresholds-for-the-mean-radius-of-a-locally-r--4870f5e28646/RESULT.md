# Two sharp crowding thresholds for the mean radius of a locally reset active droplet

## Finding

A symmetric stationary two-phase run-and-tumble gas with local resetting can become *more spatially spread out* even as its central liquid droplet shrinks strictly. Its complete mean-absolute-position response to the crowding parameter admits a sharp three-regime classification.

Fix a total mass \(M>0\), bare speed \(v_0>0\), tumbling intensity \(\alpha>0\), and local reset intensity \(r>0\), with
\[
\chi=\frac{\sqrt{r(r+\alpha)}}{v_0}>0,\qquad c=\frac{M\chi}{2}>1.
\]
For the symmetric one-dimensional two-phase stationary branch specified below, let \(\mu>4\) denote the motility crowding threshold. Normalize the density to a position probability law and write \(R_\mu=|X_\mu|\). Set
\[
q_\mu=\frac{2}{1+\sqrt{1-4/\mu}}\in(1,2),
\qquad \mu=\frac{q_\mu^2}{q_\mu-1}.
\]
Then the following exact first radial moment holds:
\[
\boxed{\mathbb E R_\mu=\frac{1}{c\chi}\left[\frac{(c-1)(q_\mu-1)}{q_\mu^2}+\frac{1+q_\mu+4/q_\mu}{6}\right].}
\]
The globally complete classification as \(\mu\) runs over \((4,\infty)\), with \(c,\chi\) held fixed, is:

1. If \(1<c\leq3/2\), \(\mathbb E R_\mu\) is **strictly increasing** in \(\mu\).
2. If \(3/2<c<7/3\), \(\mathbb E R_\mu\) has **exactly one stationary point**, a strict global maximum, attained at
\[
\boxed{q_* =\sqrt{6c-5}-1,\quad \mu_*=\frac{q_*^2}{q_*-1},\quad \max_{\mu>4}\mathbb E R_\mu=\frac{q_*+1+q_*^{-1}}{3c\chi}.}
\]
3. If \(c\geq7/3\), \(\mathbb E R_\mu\) is **strictly decreasing** in \(\mu\).

At both open domain endpoints the exact limiting values are
\[
\lim_{\mu\downarrow4}\mathbb E R_\mu=\frac{3c+7}{12c\chi},\qquad
\lim_{\mu\to\infty}\mathbb E R_\mu=\frac1{c\chi}.
\]
The dense-droplet half-width is always \(b_\mu=\log(c)/(\mu\chi)\), and therefore strictly decreases throughout all three regimes. The three-regime change is a property of the *whole normalized spatial distribution*, not the droplet boundary.

## Assumptions and scope

Consider the one-dimensional, local-Poisson-reset, two-orientation continuum stationary model in [1]. The bulk motility is \(v_0(1-\rho/\mu)\) on its physical low-density gas branch and \(v_0/\mu\) in the dense phase; \(\mu>4\). The total stationary density \(\rho_\mu(x)\) is even, integrable with total mass \(M\), and consists of a central liquid region \(|x|\leq b_\mu\) and a monotone gas tail outside. At the interface the positive velocity-weighted mass flux is continuous, but the density may jump. The stationary velocity-flux relation and matched interface value are those of the two-phase stationary branch in [1]. Resetting is instantaneous to the origin; no thermal diffusion, finite-speed return leg, or finite-particle effects are included.

The parameters \(M,v_0,r,\alpha\) are all *fixed* when \(\mu\) varies. In particular \(c>1\) and \(\chi>0\) do not vary with crowding. The statement concerns the existence and properties of this stationary branch, not dynamic selection from an arbitrary initial condition or metastability of other branches. The normalization is \(\mathbb P(X_\mu\in dx)=\rho_\mu(x)dx/M\), and \(R_\mu=|X_\mu|\).

## Proof

The stationary flux relation in [1] on \(x>0\) reads \(F'(x)=-\chi\rho_\mu(x)\), where \(F=v(\rho)\rho/v_0\) is dimensionless and \(F(0)=c\). The matched liquid/gas interface has \(F(b)=1\). Thus the liquid profile is
\[
\rho_\ell(x)=\mu c e^{-\mu\chi x},\qquad 0\leq x\leq b,
\qquad b=\frac{\log c}{\mu\chi}.
\]
On the gas side \(F=\rho_g(1-\rho_g/\mu)\), so its interface density is the small root \(q=q_\mu\in(1,2)\) of \(q(1-q/\mu)=1\). The low-density solution satisfies the inverse relation
\[
\chi(x-b)=\log\frac{q}{u}-\frac{2(q-u)}{\mu},\qquad u=\rho_g(x),\quad 0<u\leq q.
\]
Its spatial Jacobian is \(-dx/du=(1/u-2/\mu)/\chi\). The one-sided stationary mass in the gas is therefore \(\int_b^\infty\rho_g(x)dx=1/\chi\); the one-sided mass in the liquid is \((c-1)/\chi\). Consequently \(M=2c/\chi\) as required, without any change of normalization with \(\mu\).

The liquid contribution to the unnormalized first absolute moment on the positive half-line is the elementary integral
\[
\int_0^b x\rho_\ell(x)dx=\frac{c-1-\log c}{\mu\chi^2}.
\]
For the gas, integrate \(F'(x)=-\chi\rho_g(x)\) by parts (the gas flux decays exponentially) to get
\[
\int_b^\infty x\rho_g(x)dx=\frac{b}{\chi}+\frac1\chi\int_b^\infty F(x)dx
=\frac{\log c}{\mu\chi^2}+\frac1{\chi^2}\int_0^q\left(1-\frac{u}{\mu}\right)\left(1-\frac{2u}{\mu}\right)du.
\]
The latter elementary integral equals
\[
B(q)=q-\frac{3q^2}{2\mu}+\frac{2q^3}{3\mu^2}.
\]
Adding liquid and gas, multiplying by the two sides and dividing by \(M=2c/\chi\), gives
\[
\mathbb E R_\mu=\frac1{c\chi}\left(\frac{c-1}{\mu}+B(q)\right).
\]
The exact substitution \(\mu=q^2/(q-1)\) reduces \(B(q)\) to \((1+q+4/q)/6\), proving the boxed moment formula.

Write \(G_c(q)\) for the bracketed expression. Direct differentiation and factorization yield
\[
\boxed{G_c'(q)=\frac{2-q}{q^3}\left[(c-1)-\frac{q(q+2)}6\right].}
\]
On the strict interval \(1<q<2\) the prefactor is positive, whereas \(q(q+2)/6\) increases strictly from \(1/2\) to \(4/3\). Also \(d\mu/dq=q(q-2)/(q-1)^2<0\). If \(c-1\leq1/2\), the displayed bracket is negative throughout, giving strict increase of the mean with \(\mu\). If \(c-1\geq4/3\), it is positive throughout, giving strict decrease with \(\mu\). In the remaining open range it has exactly one zero, at \(q_*=-1+\sqrt{6c-5}\); its sign switches from negative to positive as \(q\) decreases through \(q_*\), making a unique global maximum as \(\mu\) increases. Substitution of the defining equation \(q_*(q_*+2)=6(c-1)\) gives its stated height. The endpoint limits follow by evaluating \(G_c\) at \(q=2\) and \(q=1\), respectively. All inequalities and limiting statements hold for every real \(c>1\) and \(\mu>4\); numerical sampling is not used for any global assertion.

## Verification

The accompanying standalone Python 3 program `verify_spread.py` evaluates the independently parametrized gas spatial quadrature via the change of variable \(u=q e^{-t}\), plus direct integration of the liquid profile. This avoids integrable endpoint logarithms in naive spatial coordinate transforms. The checker compares the result to the simplified formula over 144 parameter triples, checks 48 endpoint expressions, and tests seven representative monotonicity/optimizer regimes. Run `python3 verify_spread.py`; no external packages are needed. The recorded execution completed **199 passing checks**. Analytical differentiation establishes uniqueness and all-parameter validity; this finite set of checks is only a reproducibility aid.

## Relationship to prior work

Grange [1] first derives the kinetic model, stationary two-phase profiles, flux matching, interface density, mass and droplet width, and the unique optimum of that *width versus reset rate*. Those input facts are not claimed as new. The result here instead studies the previously unreported normalized mean absolute position *as crowding \(\mu\) varies at fixed reset rate and mass*, and obtains the two exact crowding-response thresholds \(c=3/2\) and \(c=7/3\). It is not a reparameterization of the width optimum: width always decreases here, while the mean radius can increase, peak, or decrease.

A relevant published coexistence transport result [2] gives a quantile order and \(W_1\)/\(W_\infty\) distance *between the coexisting pure-gas and droplet solutions at fixed \(\mu\)*, with an optimal distance versus reset rate in a restricted coexistence interval. That exact comparison does not imply this global three-regime behavior of the mean radius of one droplet branch as \(\mu\) changes, especially outside pure-gas coexistence. Another published general-flux result [3] obtains gas-independent droplet mass and optimal dense width for power-law liquid constitutive fluxes. It does not address this mean position observable, this variation of the gas crowding law, or the two sharp thresholds. The present theorem is a direct motivated new observable of existing exact profiles; publication priority remains subject to unindexed equivalent calculations.

## Limitations

Only an exact mathematical stationary-state observable is established. No microscopic stochastic finite-population convergence, stability under fluctuations, dynamics of relaxation, alternate constitutive law, other spatial dimension, or finite-speed-return model is claimed. At \(\mu=4\) and \(\mu=\infty\), endpoint values are limits, not attained parameter values. The first radial moment is determined by the known stationary profiles, so the contribution is the exact nonmonotone response and global thresholds, not a new solution of the kinetic equations. Closely related but unindexed analyses could affect novelty priority. No independent audit is claimed.

## References

[1] P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149v1, first posted 19 October 2026, https://arxiv.org/abs/2610.26149 .

[2] *Exact transport separation and a universal crowding threshold in resetting active-matter coexistence*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-transport-separation-and-a-universal-crowding-threshold-in--deefcd2d517d .

[3] *Gas-independent droplet geometry and power-law optimal resetting in active matter*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-gas-independent-droplet-geometry-and-power-law-optimal-resetting--c82a3ef3fe29 .
