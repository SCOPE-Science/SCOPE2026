# Conditional flux rigidity and opposite mean shifts in the minimal Wilhelm oscillator

## Finding
Consider the three-species four-reaction mass-action system
\[
\begin{aligned}
\dot x&=\kappa_3yz-2\kappa_2x^2,\\
\dot y&=\kappa_1y-\kappa_3yz,\\
\dot z&=\kappa_2x^2-2\kappa_4z^2,
\end{aligned}
\qquad \kappa_1,\kappa_2,\kappa_3,\kappa_4>0.
\]
Write \(\mu\) for **any** invariant Borel probability measure whose support is a compact subset of the strictly positive octant. Capital letters \(X,Y,Z\) are its three coordinate random variables; \(\mathbb E\) denotes integration with respect to \(\mu\). Define
\[
\alpha=\sqrt{\frac{2\kappa_4}{\kappa_2}},\qquad
z_*=\frac{\kappa_1}{\kappa_3},\qquad
x_*=\alpha z_*,\qquad
y_*=\frac{4\kappa_1\kappa_4}{\kappa_3^2}.
\]
The latter three numbers are the coordinates of the unique positive equilibrium. Then all of the following are exact, without restrictions on the rate constants beyond positivity:
\[
\boxed{\mathbb E[Z\mid Y]=z_*\quad\text{almost surely},\qquad
\mathbb E Z=z_*,\qquad \operatorname{Cov}(Y,Z)=0.}
\]
The other two means have the **opposite signed, exact defects**
\[
\boxed{x_*-\mathbb E X
 =\mathbb E\!\left[\frac{(X-\alpha Z)^2}{2\alpha Z}\right],
\qquad
\mathbb E Y-y_*=\frac{4\kappa_4}{\kappa_1}\operatorname{Var}(Z).}
\]
Consequently, for every \(\mu\ne\delta_{(x_*,y_*,z_*)}\),
\[
\boxed{\mathbb E X<x_*,\qquad \mathbb E Y>y_*,\qquad \mathbb E Z=z_*.}
\]
There are also exact conditional reaction-flux calibrations,
\[
\mathbb E[YZ\mid X]=\frac{2\kappa_2}{\kappa_3}X^2,
\qquad
\mathbb E[X^2\mid Z]=\frac{2\kappa_4}{\kappa_2}Z^2
\quad\text{almost surely}.
\]
In particular, each nonconstant positive periodic solution of the system has the three strict mean relations under the invariant measure of uniform **physical time** around its orbit. Such periodic solutions exist for rates near the supercritical Hopf bifurcation proved in the cited source.

## Assumptions and scope
The vector field is the original three-dimensional Wilhelm oscillator, not the different Wilhelm–Heinrich system or the four-species homogenisation. The state space is \((0,\infty)^3\), and the support of \(\mu\) is assumed compact **inside** that open set. This ensures that logarithms, conditional observables, and all displayed expectations are finite. No assertion is made for noncompact invariant measures, boundary-supported measures, stochastic reaction models, or arbitrary unbounded trajectories. The uniqueness and expression for the positive equilibrium are recalled from Boros–Hofbauer, Section 5, Theorem 15, and also follow by direct substitution.

## Proof
Let \(F\) denote the displayed polynomial vector field and \(Lh=F\cdot\nabla h\) its deterministic generator. Invariance and compact support imply \(\mathbb E[Lh]=0\) for every continuously differentiable observable \(h\) in a neighborhood of the support: differentiate the invariant integral of \(h\) along the flow at zero time.

**Catalyst calibration.** The logarithmic derivative of the second species is
\[
L\log y=\kappa_1-\kappa_3z.
\]
It follows that \(\mathbb E Z=z_*\). More strongly, let \(g\) be any continuously differentiable bounded function of one variable on a neighborhood of the compact range of \(Y\). Define \(h(y)=\int_{y_0}^{y}g(s)\,ds/s\) for any positive \(y_0\). Then
\[
Lh(y)=g(y)(\kappa_1-\kappa_3z),\qquad
\mathbb E[g(Y)(Z-z_*)]=0.
\]
Such \(g\) determine the conditional expectation, so \(\mathbb E[Z\mid Y]=z_*\) almost surely. Taking \(g(Y)=Y\) gives \(\operatorname{Cov}(Y,Z)=0\). Analogously, testing arbitrary functions of \(x\) against \(\dot x\), and arbitrary functions of \(z\) against \(\dot z\), gives the two other stated conditional-flux identities. The conditional laws do **not** assert statistical independence.

**Exact deficit of the first species.** From \(\alpha^2=2\kappa_4/\kappa_2\) one checks the pointwise identity
\[
\frac{(x-\alpha z)^2}{2\alpha z}+x-\alpha z
 =\frac{\kappa_2x^2-2\kappa_4z^2}{2\alpha\kappa_2z}
 =\frac{L\log z}{2\alpha\kappa_2}.
\]
The last observable has zero invariant mean. Since \(\mathbb E Z=z_*\), integration proves
\[
x_*-\mathbb E X=\mathbb E\!\left[\frac{(X-\alpha Z)^2}{2\alpha Z}\right].
\]

**Exact excess of the second species.** The polynomial identity
\[
L(x+y+2z)=\kappa_1y-4\kappa_4z^2
\]
gives \(\mathbb E Y=(4\kappa_4/\kappa_1)\mathbb E[Z^2]\). Substitute \(\mathbb E Z=z_*\) and \(y_*=(4\kappa_4/\kappa_1)z_*^2\) to obtain the variance formula.

**Strictness and the equality case.** Both defects are nonnegative. If \(\operatorname{Var}(Z)=0\), invariance implies that every orbit through the support remains in the level plane \(z=z_*\). Since \(\dot z=\kappa_2x^2-2\kappa_4z^2\) and \(x>0\), this enforces \(x=\alpha z_*\). Invariance on this line, using \(\dot x=0\), enforces \(y=4\kappa_4z_*/\kappa_3=y_*\). Thus the measure is the equilibrium point mass. Similarly, zero first-species defect forces the support to lie in \(x=\alpha z\). On that cone \(\dot z=0\), and invariance forces \(\dot x=0\), thence \(y=4\kappa_4z/\kappa_3\); invariance of \(y\) then gives \(z=z_*\). Hence either equality condition characterizes the equilibrium measure. For any other invariant measure both inequalities are strict. This completes the proof.

## Verification
A standalone symbolic identity checker, `check_flux.py`, recomputes the equilibrium, all three pointwise generator identities, and the conditional-flux drift equations directly from the stated polynomial vector field. Run it from the extracted file directory using Python 3 and SymPy: `python check_flux.py`. Successful output is `WILHELM_FLUX_IDENTITIES_OK`. The checker tests algebra, not measure invariance or literature priority: the latter are handled by the analytic argument and source comparison above. The existence of nonconstant limit cycles near Hopf is the previously published theorem, not inferred from numerical experiments.

## Relationship to prior work
Boros and Hofbauer, *Some minimal bimolecular mass-action systems with limit cycles*, arXiv:2202.11034, Section 5, Theorem 15, establish the minimal oscillator, its unique positive equilibrium, the Hopf threshold and stable periodic orbits. Those are used as premises, not claimed as new. Their inspected Section 5 and proof do not state the conditional catalyst calibration or the pair of sign-definite mean defects. Wilhelm's 2009 article primarily treats a distinct two-species bistable minimal network and mentions the oscillatory network; it does not supply the displayed three-species invariant-measure conclusions in the inspected material.

The approach uses classical stationarity-generator identities; the contribution is the **specific model-wide exact defect pair and opposite strict mean biases**, with a conditional constraint on the catalytic reaction, which do not follow from a generic stationary-balance result without these model-specific algebraic identities. Findings about the mass-conserving four-species Wilhelm–Heinrich model concern different reaction equations and do not imply this three-species theorem. Previously published results on the Schnakenberg, Brusselator, Selkov and Oregonator oscillators likewise concern different vector fields and conditional observables.

## Limitations
The result supplies exact statistics for invariant probability measures, including physical-time periodic orbit measures. It does not prove existence or uniqueness of an invariant measure for every set of rates; Hopf-cycle existence is inherited from the source. It does not classify the global basin, transient behavior of all positive solutions, all higher joint moments, or stochastic (finite-molecule) reaction processes. Constancy of \(\mathbb E[Z\mid Y]\) does not establish independence of \(Y\) and \(Z\). Publication priority remains subject to any equivalent derivation outside the inspected literature; independent mathematical validation has not been performed.

## References
1. Balázs Boros and Josef Hofbauer, *Some minimal bimolecular mass-action systems with limit cycles*, arXiv:2202.11034 (first public version, 22 February 2022; Section 5, Theorem 15). https://arxiv.org/abs/2202.11034 ; full text https://arxiv.org/html/2202.11034v2 .
2. Thomas Wilhelm, *The smallest chemical reaction system with bistability*, BMC Systems Biology **3**, 90 (2009), DOI: 10.1186/1752-0509-3-90. https://link.springer.com/article/10.1186/1752-0509-3-90 .
