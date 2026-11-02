# Fiberwise stationary regressions in the Burke–Shaw flow
## Finding
Consider the Burke–Shaw flow
\[
\dot x=-a(x+y),
\qquad
\dot y=-y-kxz,
\qquad
\dot z=gxy+d,
\]
with
\[
a>0,\qquad k>0,\qquad g>0,\qquad d>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three nonlinear or coupled inputs satisfy exact coordinate-fiber regressions:
\[
\boxed{
\mathbb E_\mu[y\mid x]=-x
},
\]
\[
\boxed{
\mathbb E_\mu[xz\mid y]=-\frac{y}{k}
},
\]
and
\[
\boxed{
\mathbb E_\mu[xy\mid z]=-\frac{d}{g}
}.
\]

The corresponding regression residuals are precisely the three coordinate speeds, up to their coefficients:
\[
y+x=-\frac{\dot x}{a},
\]
\[
xz+\frac{y}{k}=-\frac{\dot y}{k},
\]
and
\[
xy+\frac{d}{g}=\frac{\dot z}{g}.
\]

Conditional orthogonality therefore gives three exact variance defects:
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(x)
+
\frac{1}{a^2}\mathbb E_\mu[\dot x^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(xz)
=
\frac{1}{k^2}\operatorname{Var}_\mu(y)
+
\frac{1}{k^2}\mathbb E_\mu[\dot y^2]
},
\]
and
\[
\boxed{
\operatorname{Var}_\mu(xy)
=
\frac{1}{g^2}\mathbb E_\mu[\dot z^2]
}.
\]

The same regressions force the exact stationary covariances
\[
\boxed{
\operatorname{Cov}_\mu(x,y)
=
-\operatorname{Var}_\mu(x)
},
\]
\[
\boxed{
\operatorname{Cov}_\mu(xz,y)
=
-\frac{1}{k}\operatorname{Var}_\mu(y)
},
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(xy,z)=0
}.
\]

The first defect has a complete equality classification. It vanishes exactly for invariant measures supported on the two equilibria
\[
p_\pm
=
\left(
\pm\sqrt{\frac{d}{g}},
\mp\sqrt{\frac{d}{g}},
\frac1k
\right).
\]

Hence every compact stationary state not supported on
\[
\{p_-,p_+\}
\]
satisfies
\[
\boxed{
\operatorname{Var}_\mu(y)>\operatorname{Var}_\mu(x)>0
}
\]
and
\[
\boxed{
-1<\operatorname{Corr}_\mu(x,y)<0
}.
\]
More precisely,
\[
\boxed{
\operatorname{Corr}_\mu(x,y)
=
-
\left(
1+
\frac{\mathbb E_\mu[\dot x^2]}
{a^2\operatorname{Var}_\mu(x)}
\right)^{-1/2}
}.
\]

Thus the departure from perfect \(x\)-\(y\) anticorrelation is measured exactly by normalized mean-square \(x\)-speed.

For the widely used bounded chaotic parameter set
\[
a=k=g=10,
\qquad
d=4.272,
\]
the fiber laws become
\[
\mathbb E[y\mid x]=-x,
\]
\[
\mathbb E[xz\mid y]=-\frac{y}{10},
\]
and
\[
\mathbb E[xy\mid z]=-0.4272.
\]
The variance defects specialize to
\[
\operatorname{Var}(y)-\operatorname{Var}(x)
=
\frac1{100}\mathbb E[\dot x^2],
\]
\[
\operatorname{Var}(xz)-\frac1{100}\operatorname{Var}(y)
=
\frac1{100}\mathbb E[\dot y^2],
\]
and
\[
\operatorname{Var}(xy)
=
\frac1{100}\mathbb E[\dot z^2].
\]

Previously published global Burke–Shaw forcing balances, including the integrated identity
\[
\mathbb E[x^2]=\frac{d}{g},
\]
are not part of the originality claim. The finding assessed here is the stronger fiberwise regression structure and its exact speed-defect and covariance consequences.

## Assumptions and scope
The theorem concerns the autonomous Burke–Shaw vector field on
\[
\mathbb R^3
\]
with positive coefficients
\[
a,k,g,d.
\]
Compact support guarantees integrability of all polynomial observables and one-coordinate antiderivative tests.

The original Burke–Shaw equations appeared in Shaw's 1981 article in the parameter normalization
\[
a=k=g=10,
\qquad
d=13.
\]
That original example was explicitly described as having a noncompact attracting set. The theorem here is conditional on compactly supported invariant measures and therefore does not assert that the original
\[
d=13
\]
example supplies one.

A later open review records the same general system and reports chaotic behavior also at
\[
a=k=g=10,
\qquad
d=4.272,
\]
with the two equilibria shown above.

The foundational 1981 publication and an earlier 1978 preprint are historically prior, but the checked records do not provide a verified day-level public date for either. To avoid inventing a date, the structured full-date field uses 30 January 2008, the earliest checked day-resolved same-object mathematical source. This does not change the archive-cohort classification.

A same-object mathematical bibliographic record assigns MSC codes in the permitted dynamical-systems class \(37\), including \(37D45\) and \(37C25\). The present statement is classified under \(37D45\).

## Proof
Let \(L\) denote the generator of the flow.

Take a continuous function \(\phi\) on the compact \(x\)-range of the support and choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
-a\phi(x)(x+y).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(x+y)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=-x.
\]

Likewise, taking arbitrary antiderivative tests in \(y\) gives
\[
\mathbb E_\mu[\psi(y)(y+kxz)]=0,
\]
so
\[
\mathbb E_\mu[xz\mid y]=-\frac{y}{k}.
\]

Taking arbitrary antiderivative tests in \(z\) gives
\[
\mathbb E_\mu[\chi(z)(gxy+d)]=0,
\]
and therefore
\[
\mathbb E_\mu[xy\mid z]=-\frac{d}{g}.
\]

For the first defect, define
\[
R_x=y+x=-\frac{\dot x}{a}.
\]
The first conditional law says
\[
\mathbb E[R_x\mid x]=0.
\]
Hence \(R_x\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(x\). Since
\[
y=-x+R_x,
\]
we obtain
\[
\operatorname{Var}(y)
=
\operatorname{Var}(x)
+
\mathbb E[R_x^2],
\]
which is
\[
\operatorname{Var}(y)
=
\operatorname{Var}(x)
+
\frac1{a^2}\mathbb E[\dot x^2].
\]
The same orthogonality gives
\[
\operatorname{Cov}(x,y)
=
-\operatorname{Var}(x).
\]

For the second defect, set
\[
R_y=xz+\frac{y}{k}
=
-\frac{\dot y}{k}.
\]
Because
\[
\mathbb E[R_y\mid y]=0,
\]
we have
\[
xz=-\frac{y}{k}+R_y,
\]
and therefore
\[
\operatorname{Var}(xz)
=
\frac1{k^2}\operatorname{Var}(y)
+
\frac1{k^2}\mathbb E[\dot y^2].
\]
Similarly,
\[
\operatorname{Cov}(xz,y)
=
-\frac1k\operatorname{Var}(y).
\]

For the third defect,
\[
R_z=xy+\frac{d}{g}
=
\frac{\dot z}{g}.
\]
The conditional law gives
\[
\mathbb E[R_z\mid z]=0.
\]
Since the predictor
\[
-\frac{d}{g}
\]
is constant,
\[
\operatorname{Var}(xy)
=
\mathbb E[R_z^2]
=
\frac1{g^2}\mathbb E[\dot z^2],
\]
and
\[
\operatorname{Cov}(xy,z)=0.
\]

We now classify equality in the first defect.

If
\[
\mathbb E[\dot x^2]=0,
\]
then the continuous function \(\dot x\) vanishes on
\[
\operatorname{supp}\mu.
\]
Every complete support trajectory therefore has constant \(x\), and the first equation gives
\[
y=-x.
\]
Because \(y\) is also constant along that trajectory,
\[
0=\dot y
=
-y-kxz
=
x(1-kz).
\]

The alternative
\[
x=0
\]
cannot occur on a compact invariant support when
\[
d>0,
\]
because then
\[
y=0,
\qquad
\dot z=d,
\]
and the trajectory is unbounded. Hence
\[
z=\frac1k.
\]
Since \(z\) is constant,
\[
0=\dot z
=
gxy+d
=
-gx^2+d,
\]
so
\[
x^2=\frac{d}{g}.
\]
Thus every support point is one of
\[
p_\pm.
\]

Conversely, every invariant measure supported on
\[
\{p_-,p_+\}
\]
has
\[
\dot x=0
\]
and therefore zero first defect.

If the measure is not supported on those two equilibria, then
\[
\mathbb E[\dot x^2]>0.
\]
Also
\[
\operatorname{Var}(x)>0,
\]
because constant \(x\) on compact invariant support would force the same equilibrium classification. Therefore
\[
\operatorname{Var}(y)>\operatorname{Var}(x)>0.
\]
Finally,
\[
\operatorname{Corr}(x,y)
=
\frac{-\operatorname{Var}(x)}
{\sqrt{\operatorname{Var}(x)\operatorname{Var}(y)}}
\]
and substitution of the first variance defect gives the displayed exact formula and the strict interval
\[
-1<\operatorname{Corr}(x,y)<0.
\]

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the three pointwise residual identities
\[
y+x=-\frac{\dot x}{a},
\]
\[
xz+\frac{y}{k}=-\frac{\dot y}{k},
\]
and
\[
xy+\frac{d}{g}=\frac{\dot z}{g}.
\]

It verifies the abstract conditional-regression variance and covariance algebra used in all three decompositions.

For the parameter set
\[
a=k=g=10,
\qquad
d=4.272,
\]
it verifies exactly that
\[
\frac{d}{g}=0.4272
\]
in rational arithmetic and that the two equilibrium coordinates satisfy all three vector-field equations.

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements and equality-rigidity argument are analytic consequences of invariance and compactness; they are not inferred from finite numerical trajectories.

## Relationship to prior work
Shaw's 1981 article gives the original Burke–Shaw system in the form
\[
\dot x=-10x-10y,
\qquad
\dot y=-10xz-y,
\qquad
\dot z=10xy+13.
\]
The article describes its unbounded strange attracting set and places it in a broader discussion of information production and strange-attractor geometry. The Burke–Shaw passage does not present invariant-measure conditional moments.

Panchev, Spassova, and Vitanov study the Burke–Shaw system together with generalized Lorenz systems, analyzing fixed points, asymptotic behavior, Lyapunov exponents, Lyapunov dimension, and chaotic attractors. The corresponding mathematical bibliographic record places the work in dynamical-systems MSC classes \(37D45\) and \(37C25\).

Petráš gives an open review of Lorenz-type systems and writes the exact general Burke–Shaw equations used here. It records the parameter choices
\[
a=k=g=10,
\qquad
d=13
\]
and
\[
d=4.272
\]
as chaotic examples and lists the two equilibria for the displayed parameters.

A complete recent Burke–Shaw paper on fractional-fractal control was also inspected. It writes the same integer-order Burke–Shaw core and studies stability, numerical approximation, and chaos control. Full-document searches found no occurrences of `conditional`, `variance`, `moment`, or `invariant measure`.

Published semantic-index searches located an earlier Burke–Shaw result giving global forcing balance laws, including
\[
\mathbb E[x^2]=\frac{d}{g},
\]
and a mean-height relation. Those integrated balances are treated as prior coverage and are excluded from the present originality claim.

The accepted statement is strictly stronger in a different direction: it gives infinitely many test-function constraints on three coordinate fibers,
\[
\mathbb E[y\mid x]=-x,
\quad
\mathbb E[xz\mid y]=-\frac{y}{k},
\quad
\mathbb E[xy\mid z]=-\frac{d}{g},
\]
and turns them into exact speed defects and covariance laws. The known global identities follow after integration of some of these fiber laws, not conversely.

## Limitations
The theorem does not assert existence of a compact invariant measure for every positive parameter choice.

The original
\[
d=13
\]
Burke–Shaw example was described as noncompact, so the present compact-support theorem is not claimed to characterize that particular attracting set.

The theorem does not determine the full invariant density, entropy, Lyapunov spectrum, fractal dimension, or basin geometry.

The structured full-date field uses the earliest checked day-resolved same-object mathematical source because no day-level public date was verified for the historically earlier 1978 preprint or 1981 journal article.

An earlier published result already covers the global forcing identities obtained by integrating the fiber laws. Those global balances are explicitly excluded from the originality claim.

Because the generator proof is short, an equivalent conditional-moment observation could remain in unindexed literature.

## References
1. R. Shaw, “Strange Attractors, Chaotic Behavior, and Information Flow,” Zeitschrift für Naturforschung A 36, 80–112 (1981), DOI 10.1515/zna-1981-0115.
2. S. Panchev, T. Spassova, and N. K. Vitanov, “Analytical and numerical investigation of two families of Lorenz-like dynamical systems,” Chaos, Solitons & Fractals 33, 1658–1671, DOI 10.1016/j.chaos.2006.03.037.
3. I. Petráš, “The fractional-order Lorenz-type systems: A review,” Fractional Calculus and Applied Analysis 25, 362–377 (2022), DOI 10.1007/s13540-022-00016-4.
4. “Control of chaos in the Burke-Shaw system of fractal-fractional order,” Journal of Applied Mathematics and Computational Mechanics 23 (2024), DOI 10.17512/jamcm.2024.1.07.
