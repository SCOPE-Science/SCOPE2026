# A fixed-point chord law for invariant measures of the Hénon map
## Finding
Consider the Hénon map
\[
F_{a,b}(x,y)
=
\left(
1-a x^2+y,\,
bx
\right),
\qquad
a>0,
\qquad
b\in\mathbb R.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure, and write
\[
m=\int x\,d\mu.
\]

The two fixed points have the form
\[
p_\pm=(x_\pm,bx_\pm),
\]
where
\[
x_\pm
=
\frac{-(1-b)\pm\sqrt{(1-b)^2+4a}}{2a},
\qquad
x_-<x_+.
\]

Then the barycenter of every invariant measure lies on the line through those two fixed points:
\[
\boxed{
\bar p
=
\int (x,y)\,d\mu
=
(m,bm)
}.
\]

More strongly,
\[
\boxed{
\operatorname{Var}_\mu(x)
=
(x_+-m)(m-x_-)
}.
\]

The second coordinate has the exact scaled marginal law
\[
y_\#\mu
=
(bx)_\#\mu,
\]
so in particular
\[
\boxed{
\operatorname{Var}_\mu(y)
=
b^2\operatorname{Var}_\mu(x)
}.
\]

Combining these identities gives the geometric fixed-point chord law
\[
\boxed{
\int
\left\|
(x,y)-\bar p
\right\|^2
\,d\mu
=
\left\|
\bar p-p_-
\right\|
\left\|
p_+-\bar p
\right\|
}.
\]

Thus the root-mean-square radius of any compact stationary Hénon state about its own barycenter is the geometric mean of the barycenter's two Euclidean distances to the fixed points.

Several consequences are immediate.

First,
\[
\boxed{
\bar p\in[p_-,p_+]
}.
\]
An endpoint occurs exactly for the corresponding fixed-point atom.

Second, if
\[
L=\|p_+-p_-\|,
\]
then
\[
\boxed{
\int
\left\|
(x,y)-\bar p
\right\|^2
\,d\mu
\le
\frac{L^2}{4}
}.
\]
This upper bound is sharp: it is attained by the equal mixture
\[
\frac12\delta_{p_-}
+
\frac12\delta_{p_+}.
\]

Equivalently, if \(\nu_m\) is the unique probability measure supported on
\[
\{p_-,p_+\}
\]
with the same barycenter as \(\mu\), then \(\mu\) and \(\nu_m\) have exactly the same total coordinate variance.

For the classical parameters
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
the fixed-point \(x\)-coordinates are
\[
x_\pm
=
\frac{-7\pm\sqrt{609}}{28}.
\]
Every compact invariant probability measure satisfies
\[
\operatorname{Var}_\mu(x)
\le
\frac{609}{784},
\]
and
\[
\boxed{
\int
\left\|
(x,y)-\bar p
\right\|^2
\,d\mu
\le
\frac{66381}{78400}
}.
\]

These formulas apply equally to periodic-orbit measures, strange-attractor measures, equilibrium measures from thermodynamic formalism, and convex mixtures of invariant measures.

## Assumptions and scope
The theorem uses the original Hénon normalization
\[
x_{n+1}=1-a x_n^2+y_n,
\qquad
y_{n+1}=b x_n.
\]

Compact support is more than enough for the argument; finite second moments would suffice for the moment identities.

The condition
\[
a>0
\]
ensures that the fixed-point quadratic
\[
a x^2+(1-b)x-1=0
\]
has two distinct real roots because its discriminant is
\[
(1-b)^2+4a>0.
\]

The foundational paper is publicly dated only to February 1976 in the publisher metadata. Its complete text was inspected, but no day-level publication date was assigned here. The structured full-date field therefore uses 1 March 1985, the earliest checked same-object source with a day-resolved public publication date, rather than inventing a day in February 1976.

The original Hénon work is classified under MSC \(37D45\) in mathematical bibliographic metadata.

## Proof
Invariance of \(\mu\) means that
\[
\int \varphi\circ F_{a,b}\,d\mu
=
\int \varphi\,d\mu
\]
for every continuous \(\varphi\).

Apply this first to the second coordinate. Since
\[
\pi_y\circ F_{a,b}(x,y)=bx,
\]
the \(y\)-marginal of \(\mu\) is exactly the pushforward of the \(x\)-marginal under multiplication by \(b\):
\[
y_\#\mu=(bx)_\#\mu.
\]
Consequently
\[
\int y\,d\mu=bm
\]
and
\[
\operatorname{Var}_\mu(y)
=
b^2\operatorname{Var}_\mu(x).
\]

Now apply invariance to the first coordinate:
\[
m
=
\int
\left(
1-a x^2+y
\right)
\,d\mu.
\]
Using
\[
\int y\,d\mu=bm
\]
gives
\[
a\int x^2\,d\mu
=
1-(1-b)m.
\]
Hence
\[
\operatorname{Var}_\mu(x)
=
\frac{1-(1-b)m}{a}-m^2.
\]

The fixed-point coordinates \(x_\pm\) are the roots of
\[
a x^2+(1-b)x-1=0,
\]
so
\[
a(m-x_-)(m-x_+)
=
a m^2+(1-b)m-1.
\]
Therefore
\[
\operatorname{Var}_\mu(x)
=
-(m-x_-)(m-x_+)
=
(x_+-m)(m-x_-).
\]

Since variance is nonnegative,
\[
m\in[x_-,x_+].
\]
Thus
\[
\bar p=(m,bm)
\]
lies on the segment joining
\[
p_-=(x_-,bx_-)
\]
and
\[
p_+=(x_+,bx_+).
\]

The total coordinate variance is
\[
\begin{aligned}
\int
\left\|
(x,y)-\bar p
\right\|^2
\,d\mu
&=
\operatorname{Var}_\mu(x)
+
\operatorname{Var}_\mu(y)\\
&=
(1+b^2)
(x_+-m)(m-x_-).
\end{aligned}
\]

Because \(\bar p,p_-,p_+\) are collinear,
\[
\|\bar p-p_-\|
=
\sqrt{1+b^2}\,(m-x_-)
\]
and
\[
\|p_+-\bar p\|
=
\sqrt{1+b^2}\,(x_+-m).
\]
Multiplying proves
\[
\int
\left\|
(x,y)-\bar p
\right\|^2
\,d\mu
=
\|\bar p-p_-\|
\|p_+-\bar p\|.
\]

If
\[
m=x_-
\quad\text{or}\quad
m=x_+,
\]
then
\[
\operatorname{Var}(x)=0.
\]
The scaled-marginal identity then gives
\[
\operatorname{Var}(y)=0.
\]
Thus \(\mu\) is the atom at the corresponding fixed point. The converse is immediate.

For a point on a segment of length \(L\), the product of the two distances to the endpoints is at most
\[
L^2/4.
\]
Equality occurs at the midpoint. The equal fixed-point mixture is invariant and has midpoint barycenter, so the bound is sharp.

At
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
the fixed-point equation becomes
\[
14x^2+7x-10=0,
\]
hence
\[
x_\pm
=
\frac{-7\pm\sqrt{609}}{28}.
\]
Therefore
\[
\frac{(x_+-x_-)^2}{4}
=
\frac{609}{784}.
\]
Since
\[
1+b^2
=
\frac{109}{100},
\]
the sharp total-variance bound is
\[
\frac{109}{100}
\frac{609}{784}
=
\frac{66381}{78400}.
\]

## Verification
The accompanying exact checker verifies the fixed-point factorization, the invariant first-moment reduction, the variance parabola, and the geometric chord identity using rational arithmetic and symbolic polynomial coefficients.

For the classical parameters
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
it verifies
\[
x_++x_-=-\frac12,
\qquad
x_+x_-=-\frac57,
\]
\[
\frac{(x_+-x_-)^2}{4}
=
\frac{609}{784},
\]
and
\[
(1+b^2)\frac{609}{784}
=
\frac{66381}{78400}.
\]

The stored checker output is `VERIFY_OK`.

No numerical trajectory is used to prove an invariant-measure statement.

## Relationship to prior work
Hénon's 1976 paper introduces the map
\[
x_{n+1}=1-a x_n^2+y_n,
\qquad
y_{n+1}=b x_n,
\]
derives its constant Jacobian, inverse, two fixed points, stability thresholds, trapping region, and the numerical strange attractor at
\[
a=1.4,
\qquad
b=0.3.
\]
The complete article was inspected. Searches across its full text found no invariant-probability-measure, moment, variance, barycenter, mean, or average formulation.

Hitzl and Zele explore the Hénon quadratic map across an extended parameter region and obtain analytic boundaries for stable cycles of periods through six and associated period-doubling bifurcations.

Cvitanović, Gunaratne, and Procaccia develop topological and metric properties of Hénon-type strange attractors through periodic points, symbolic dynamics, pruning, entropy, and singularity spectra.

Benedicks and Carleson establish rigorous long-time chaotic dynamics for strongly dissipative Hénon maps near the one-dimensional quadratic regime.

Senti and Takahasi give a full invariant-measure and thermodynamic-formalism treatment at the first bifurcation. Their complete article was inspected page by page; it develops existence and uniqueness of equilibrium measures, entropy, unstable Lyapunov exponents, Hausdorff dimension, exponential correlation decay, and a central limit theorem. Full-document text searches found no occurrence of `moment` or `barycenter`; apparent matches for `variance` were occurrences inside `variation` and related thermodynamic terminology, not coordinate variance identities.

The accepted result concerns a different layer of structure: an exact relation between the barycenter and total second moment of every compact invariant measure, independent of hyperbolicity, entropy, or ergodicity.

## Limitations
The theorem determines the barycenter and total coordinate variance relation, but not the full covariance matrix. In particular, it does not determine
\[
\operatorname{Cov}(x,y).
\]

It does not prove the existence of a strange attractor for any parameter pair, nor does it determine entropy, Lyapunov exponents, fractal dimension, decay of correlations, or basin geometry.

The equal fixed-point mixture shows that maximal total variance need not correspond to chaotic dynamics.

The original 1976 paper has only month-level publication metadata in the inspected publisher record. The later day-resolved source date is used solely to avoid fabricating a day-level date.

The proof is short once invariance is applied to coordinate functions, so a differently phrased equivalent moment identity could remain in unindexed literature.

## References
1. M. Hénon, “A Two-dimensional Mapping with a Strange Attractor,” Communications in Mathematical Physics 50, 69–77 (1976), DOI 10.1007/BF01608556.
2. D. L. Hitzl and F. Zele, “An exploration of the Hénon quadratic map,” Physica D 14, 305–326 (1985), DOI 10.1016/0167-2789(85)90092-2.
3. P. Cvitanović, G. H. Gunaratne, and I. Procaccia, “Topological and metric properties of Hénon-type strange attractors,” Physical Review A 38, 1503–1520 (1988), DOI 10.1103/PhysRevA.38.1503.
4. M. Benedicks and L. Carleson, “The Dynamics of the Hénon Map,” Annals of Mathematics 133, 73–169 (1991), DOI 10.2307/2944326.
5. S. Senti and H. Takahasi, “Equilibrium measures for the Hénon map at the first bifurcation: uniqueness and geometric/statistical properties,” Ergodic Theory and Dynamical Systems 36, 215–255 (2016), DOI 10.1017/etds.2014.61.
