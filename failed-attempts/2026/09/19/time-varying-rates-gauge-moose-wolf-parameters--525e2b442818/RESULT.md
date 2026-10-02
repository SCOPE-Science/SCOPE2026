# Time-varying rates gauge away constant parameters in the Moose–Wolf inverse model

## Result

Singh and Kumari, arXiv:2609.20793v1, study two non-autonomous Moose–Wolf models and estimate two time-dependent rates together with three constant interaction parameters. Their structural-identifiability check replaces the two time-dependent rates by constants, verifies identifiability of that autonomous surrogate, and then argues that the non-autonomous model has no structural redundancy. For the non-autonomous models as written, this transfer is invalid: the unknown functions generate an exact gauge family that leaves the complete state trajectory unchanged.

For the nondimensional Holling type-II model
\[
\dot x=\alpha(t)x(1-x^4)-\frac{a x y}{b+x},\qquad
\dot y=\frac{cxy}{b+x}-\delta(t)y,
\tag{1}
\]
let \((x(t),y(t))\) be a solution on an interval on which the displayed denominators are nonzero. For any alternative constants \((a',b',c')\), define
\[
\alpha'(t)=\alpha(t)+\frac{y(t)}{1-x(t)^4}
\left(\frac{a'}{b'+x(t)}-\frac{a}{b+x(t)}\right),
\tag{2}
\]
whenever \(x(t)^4\ne1\), and
\[
\delta'(t)=\delta(t)+\frac{c'x(t)}{b'+x(t)}-\frac{cx(t)}{b+x(t)}.
\tag{3}
\]
Direct substitution gives exactly the same \(\dot x\) and \(\dot y\). Hence, on every interval where \(x^4\ne1\), the same full continuous observation of both species is compatible with a three-parameter family of constant triples, compensated by different time-dependent growth and death rates.

The ratio-dependent model has the same obstruction. For
\[
\dot x=\alpha(t)x(1-x^4)-\frac{a x y}{b y+x},\qquad
\dot y=\frac{cxy}{b y+x}-\delta(t)y,
\tag{4}
\]
the exact gauge is
\[
\alpha'(t)=\alpha(t)+\frac{y(t)}{1-x(t)^4}
\left(\frac{a'}{b'y(t)+x(t)}-\frac{a}{by(t)+x(t)}\right),
\tag{5}
\]
\[
\delta'(t)=\delta(t)+\frac{c'x(t)}{b'y(t)+x(t)}-\frac{cx(t)}{by(t)+x(t)}.
\tag{6}
\]
Again the state trajectory is unchanged identically.

There is an even simpler obstruction that does not require \(x^4\ne1\). Keeping \(a,b,\alpha\) fixed and changing only \(c\) can always be absorbed into \(\delta(t)\):
\[
\delta'(t)=\delta(t)+(c'-c)\frac{x(t)}{b+x(t)}
\]
for (1), and
\[
\delta'(t)=\delta(t)+(c'-c)\frac{x(t)}{by(t)+x(t)}
\]
for (4). Thus the constant conversion parameter \(c\) is structurally nonidentifiable whenever the predator death rate is an unrestricted unknown function, even if both state variables are observed perfectly and continuously.

Equivalently, given any positive \(C^1\) trajectory \((x,y)\), every admissible constant triple produces forcing functions
\[
\alpha_{a,b}(t)=
\frac{\dot x+a x y/(b+x)}{x(1-x^4)},\qquad
\delta_{b,c}(t)=\frac{cx}{b+x}-\frac{\dot y}{y}
\tag{7}
\]
for the Holling model, and
\[
\alpha_{a,b}(t)=
\frac{\dot x+a x y/(by+x)}{x(1-x^4)},\qquad
\delta_{b,c}(t)=\frac{cx}{by+x}-\frac{\dot y}{y}
\tag{8}
\]
for the ratio-dependent model. These formulas show that the data determine only composite terms in the two equations, not a unique decomposition into constant interaction parameters and arbitrary time functions.

## Positivity and regularity do not remove the local gauge

The obstruction is not an artifact of allowing pathological forcing. If the original trajectory and rates are \(C^k\) (or analytic) and the denominators stay away from zero, the transformed rates have the same regularity. On a compact interval, if \(\delta(t)\) is strictly positive with a positive minimum, then sufficiently small changes of \((b,c)\) preserve positivity of \(\delta'\). Likewise, positivity of \(b,c\) is preserved under sufficiently small perturbations. The source implements \(\delta\) through a softplus output and \(b,c\) through positive maps; these restrictions therefore do not restore local structural identifiability at interior parameter/function points. Its growth-rate network is not constrained to be positive, and the reported fitted growth rate in fact takes both signs.

The reported data also lie in the regular state region relevant to (2) and (5): the source uses \(K=2400\), with observed moose abundance between 385 and 2398, and wolf abundance between 2 and 50. Thus the normalized observations satisfy \(0<x<1\) and \(y>0\). The three-constant gauge applies on any continuous model interval that stays in this regular region; the one-constant \(c\)-gauge is available even without the \(x<1\) condition.

## Why pointwise freezing does not prove identifiability

The autonomous surrogate and the non-autonomous inverse problem are different identification problems. In the autonomous surrogate, \(\alpha\) and \(\delta\) are unknown scalars shared across all times, so data at different times constrain the same finite list of numbers. In the intended model, \(\alpha(t)\) and \(\delta(t)\) are unknown functions. Changing a constant parameter can be compensated at each time by changing those functions according to (2)–(6). Freezing the function values at one instant removes precisely the freedom responsible for this indistinguishability, so autonomous identifiability cannot be transferred pointwise to the non-autonomous model.

This is consistent with the general unknown-input identifiability literature: unknown time-varying parameters must be treated as unknown inputs, and their joint identifiability with constant parameters requires a dedicated analysis. The issue is structural, not a consequence of noise or sparse sampling.

## What additional information can break the gauge

The formulas also show what information is missing. In the Holling type-II model, if \(\delta(t)\) were known independently, then
\[
q(t):=\frac{\dot y}{y}+\delta(t)=\frac{cx}{b+x}
\]
gives
\[
\frac1{q(t)}=\frac1c+\frac bc\frac1{x(t)}.
\]
Hence, if \(x\) takes at least two distinct positive values, \((b,c)\) are generically identifiable; however \(a\) remains gaugeable while \(\alpha(t)\) is free. Conversely, if \(\alpha(t)\) is known, then
\[
p(t):=\frac{\alpha(t)(1-x^4)-\dot x/x}{y}=\frac{a}{b+x}
\]
generically identifies \((a,b)\) from a varying \(x\), while \(c\) remains gaugeable if \(\delta(t)\) is free. Analogous relations hold for the ratio-dependent model, with \(y/x\) replacing \(1/x\) in the predator equation and with generic non-collinearity of \((x,y)\) needed in the prey equation.

Thus independent information about the time-dependent rates, or an explicitly specified low-dimensional function class with its own identifiability analysis, can remove the obstruction. Smoothness penalties, neural-network architecture, initialization, parameter bounds, and optimization bias may select one representative numerically, but such selection is regularization or model restriction rather than structural identifiability of equations (1) or (4).

## Consequence for arXiv:2609.20793v1

The source's autonomous calculation can still be correct for the constant-rate surrogate. The correction is narrower: it does not establish structural identifiability of the actual non-autonomous models in which \(\alpha(t)\) and \(\delta(t)\) are estimated as functions. The exact gauges above show that the intended ODE inverse problem is structurally nonidentifiable without additional restrictions on those functions.

This does not imply that the reported PINN trajectory fits are numerically invalid, nor that a particular training procedure cannot return stable parameter values. It means that such values are not uniquely determined by the non-autonomous ODE and perfect state observations alone. Notably, the source itself reports a roughly order-of-magnitude spread in the fitted Holling half-saturation parameter across windows and states that this parameter is not fixed by the data; that numerical behavior is compatible with, but is not needed for, the structural argument.

## Verification

`artifacts/verify_gauge.py` symbolically substitutes the transformed rates into both source models and verifies that all four state-equation residuals vanish identically. It also verifies the reconstruction formulas (7)–(8). The corresponding output is in `artifacts/verification_output.txt`.

## Limitations

The result concerns structural identifiability of the non-autonomous ODE model when \(\alpha(t)\) and \(\delta(t)\) are treated as unknown time-varying functions of the regularity stated above. If instead the neural-network architecture itself is declared part of a finite-dimensional parametric model, its weights and constants define a different structural-identifiability problem; this record does not analyze that augmented network model. The full three-parameter gauge formulas require intervals where \(x^4\ne1\), although nonidentifiability of \(c\) persists without that restriction. No claim is made about statistical identifiability under a specific prior or regularizer.

## References

1. A. Singh and N. Kumari, *A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park*, arXiv:2609.20793v1 (2026). https://arxiv.org/abs/2609.20793
2. A. Martinelli, *Identifiability of nonlinear ODE Models with Time-Varying Parameters: the General Analytical Solution and Applications in Viral Dynamics*, arXiv:2211.13507 (2022/2023). https://arxiv.org/abs/2211.13507
3. A. F. Villaverde, N. Tsiantis, and J. R. Banga, *Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models*, J. R. Soc. Interface 16 (2019), 20190043. https://doi.org/10.1098/rsif.2019.0043
4. A. F. Villaverde, *Observability and Structural Identifiability of Nonlinear Biological Systems*, Complexity 2019, 8497093. https://doi.org/10.1155/2019/8497093
5. R. Dong, C. Goodbrake, H. A. Harrington, and G. Pogudin, *Differential Elimination for Dynamical Models via Projections with Applications to Structural Identifiability*, SIAM J. Appl. Algebra Geom. 7 (2023), 194–235. https://doi.org/10.1137/22M1469067
