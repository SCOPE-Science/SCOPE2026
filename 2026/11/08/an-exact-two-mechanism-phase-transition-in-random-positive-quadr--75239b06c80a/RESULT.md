# An exact two-mechanism phase transition in random positive quadratic quadrature

## Finding

For a target probability measure with mean zero and second moment \(c\in(0,1)\), consider exact quadrature for \(V=\operatorname{span}\{1,x,x^2\}\) supported on \(m\) independent nodes uniform on \([-1,1]\), with arbitrary nonnegative weights. The probability \(P_m(c)\) that such weights exist has an exact all-sample-size integral formula, an elementary closed form at the minimal sample size, and a sharp large-sample phase transition.

Put
\[
h(c)=\frac{1+c}{2},\qquad b(c)=1-\sqrt c,\qquad c_*=3-2\sqrt 2.
\]
For every integer \(m\ge2\), let
\[
A_m(c)=h(c)^m+\frac m2\int_c^1\left(\frac{v+c/v}{2}\right)^{m-1}\,\mathrm dv,
\]
\[
B_m(c)=\frac m2\int_c^1\left[\left(\frac{2-s-c/s}{2}\right)^{m-1}-\left(\frac{1-s}{2}\right)^{m-1}\right]\,\mathrm ds.
\]
Then the exact success probability is
\[
\boxed{P_m(c)=1-A_m(c)-B_m(c).}
\]
Here \(A_m\) is the probability that the most extreme negative and positive nodes cannot supply the requisite variance; \(B_m\) is the probability that the two nodes closest to zero on opposite sides force too large a variance. The events are disjoint up to null boundaries. In particular,
\[
\boxed{P_3(c)=\frac{3c}{2}\left(\log\frac1c-1+c\right),\quad P_4(c)=2P_3(c).}
\]
For every fixed \(c\in(0,1)\), the failure probability \(F_m(c)=1-P_m(c)\) has the **sharp equivalent**
\[
\boxed{F_m(c)\sim
\begin{cases}
\displaystyle\sqrt{\frac{\pi\sqrt c}{2(1-\sqrt c)}}\,\sqrt m\,(1-\sqrt c)^m,&0<c\le c_*,\\[5pt]
\displaystyle\frac{2}{1-c}\left(\frac{1+c}{2}\right)^m,&c_*<c<1.
\end{cases}}
\]
Consequently,
\[
\lim_{m\to\infty}-\frac1m\log F_m(c)
=-\log\max\left\{\frac{1+c}{2},1-\sqrt c\right\}.
\]
At \(c=c_*\), the two exponential bases coincide, but the central-gap mechanism dominates by a \(\sqrt m\) prefactor. For the uniform target measure, \(c=1/3\),
\[
P_3(1/3)=\tfrac12(\log3-2/3),\qquad F_m(1/3)\sim3(2/3)^m.
\]

## Assumptions and scope

The target is any Borel probability measure on \([-1,1]\) with first three moments \(1,0,c\), where \(0<c<1\); only these moments enter. The sampling law, separately, is normalized uniform Lebesgue measure on \([-1,1]\). The draws \(X_1,\ldots,X_m\) are independent, with replacement. The quadrature is \(Q(f)=\sum_{i=1}^{m}w_i f(X_i)\), where the weights may be chosen after the draw and must satisfy \(w_i\ge0\). There is no restriction that they be near equal, least-squares weights, or strictly bounded below in advance.

For \(m\ge3\), with probability one, feasibility also permits choosing every \(w_i>0\): the target moment point lies in the interior rather than on the boundary of the sampled convex polygon. The probability of exact positive quadrature with \(m\in\{1,2\}\) is zero.

## Proof

**1. Convex geometry and sharp deterministic criterion.** The moment equations are equivalent to
\[
(0,c)\in\operatorname{conv}\{(X_i,X_i^2):1\le i\le m\}.
\]
Suppose the sample has nodes of both signs. Let \(s\) and \(u\) be respectively the smallest and largest magnitudes of negative nodes, and let \(t\) and \(v\) be respectively the smallest and largest positive nodes. Thus \(0<s\le u\le1\) and \(0<t\le v\le1\). The vertical section of the convex hull of the parabola points above first coordinate zero is exactly the interval
\[
\boxed{st\ \le\ \mathbb E_{w}[X^2]\ \le\ uv.}
\]
Indeed, the lower convex-hull edge at zero is the chord joining adjacent nodes \(-s\) and \(t\); its ordinate is \(st\). Convexity of the parabola puts all remaining sampled points above this chord. Conversely, the chord between the extreme nodes \(-u\) and \(v\) gives the maximal possible ordinate \(uv\), since all sampled points lie beneath the outer endpoint chord. Mixing these two mean-zero representations fills the interval. Hence feasibility is equivalent to \(st\le c\le uv\). If only one sign occurs, feasibility is impossible almost surely.

For probability calculations set \(U=0\) if no negative node and otherwise \(U=u\); define \(V\) analogously. The failure event splits disjointly, outside null equality boundaries, into
\[
\mathcal A=\{UV<c\},\qquad
\mathcal B=\{\text{both signs occur and }st>c\}.
\]
The events are disjoint because \(st\le uv\) when both signs occur.

**2. Exact law of the extreme-span obstruction.** For \(0\le u,v\le1\),
\[
\Pr(U\le u,V\le v)=\left(\frac{u+v}{2}\right)^m,
\]
since every node must belong to \([-u,v]\). Thus \(\Pr(V\le c)=h(c)^m\). Conditional on the positive maximum taking a value \(v>c\), the density that also \(U\le c/v\) holds is the partial \(v\)-derivative of this joint distribution at fixed \(u=c/v\), namely \(\frac m2((v+c/v)/2)^{m-1}\). Integration yields \(\Pr(\mathcal A)=A_m(c)\).

**3. Exact law of the central-gap obstruction.** When both signs exist, the joint density of the nearest negative magnitude \(s\) and nearest positive magnitude \(t\) is
\[
\frac{m(m-1)}4\left(\frac{2-s-t}{2}\right)^{m-2},\qquad 0<s,t<1.
\]
It follows by differentiating twice the survival probability that no sample lies in \((-s,t)\). Integration over \(st>c\), followed by integrating the \(t\)-coordinate from \(c/s\) to \(1\), gives
\[
\Pr(\mathcal B)=\frac{m(m-1)}4\int_c^1\int_{c/s}^1\left(\frac{2-s-t}{2}\right)^{m-2}\,\mathrm dt\,\mathrm ds=B_m(c).
\]
This proves the exact integral probability formula.

**4. Three- and four-node cases.** With three nodes, feasibility requires a one-versus-two sign split, whose combined probability is \(3/4\). Conditional on such a split, denote the unique magnitude on the singleton side by \(u\). The two independent magnitudes on the other side must straddle \(c/u\), which is possible only for \(u>c\) and has conditional probability \(2(c/u)(1-c/u)\). Consequently,
\[
P_3(c)=\frac34\int_c^1 2\frac cu\left(1-\frac cu\right)\,\mathrm du
=\frac{3c}{2}(\log(1/c)-1+c).
\]
Substituting \(m=4\) into the exact integrals and integrating polynomial and reciprocal-polynomial terms gives \(P_4(c)=3c(\log(1/c)-1+c)=2P_3(c)\).

**5. Sharp asymptotics.** The function \(f(v)=(v+c/v)/2\) is strictly convex on \([c,1]\). Its two endpoint maxima are \(h(c)\), and its derivative magnitudes there are \((1-c)/(2c)\) and \((1-c)/2\). The standard one-sided Laplace expansion at these two nondegenerate boundary maxima gives
\[
\frac m2\int_c^1 f(v)^{m-1}\,\mathrm dv
\sim\frac{1+c}{1-c}h(c)^m,
\qquad A_m(c)\sim\frac{2}{1-c}h(c)^m.
\]
For the other integral, \(g(s)=1-(s+c/s)/2\) has a unique nondegenerate interior maximum at \(s_0=\sqrt c\), with \(g(s_0)=b(c)\) and \(g''(s_0)=-1/\sqrt c\). The subtracted integrand \(((1-s)/2)^{m-1}\) is exponentially smaller, since \((1-c)/2<b(c)\). The interior Laplace expansion therefore gives
\[
B_m(c)\sim
\sqrt{\frac{\pi m\sqrt c}{2b(c)}}\,b(c)^m.
\]
Finally, \(h(c)=b(c)\) exactly at \(c=c_*\), obtained by solving \(c+2\sqrt c-1=0\). On opposite sides of this point, the larger base dominates exponentially; at equality, the interior-saddle contribution has the larger polynomial prefactor. This proves every displayed asymptotic and the sharp phase transition.

For strict positivity of **all** node weights, the sample moment points are almost surely pairwise distinct and no three are collinear. When feasible, their target point is almost surely in the interior of the convex hull. Let \(z\) be the average of the sample moment points, an interior point represented by equal positive weights. For sufficiently small \(\varepsilon>0\), \(((0,c)-\varepsilon z)/(1-\varepsilon)\) remains in the hull; representing it with nonnegative weights and mixing with \(\varepsilon z\) makes every weight strictly positive.

## Verification

Run `python3 verify.py` in an environment with Python 3 standard library. The script exhaustively compares the sharp deterministic criterion with an independent exact-rational Carathéodory/Lagrange-weight test on 46,440 finite configurations. It additionally checks the \(m=2,3,4\) integral laws, selected large-sample prefactors via numerical integration, and three seeded Monte Carlo comparisons, printing `VERIFY_OK` on success. These are cross-checks; the all-\(m\) identities and limits are established by the preceding analytic proof, not by finite enumeration or simulation.

## Relationship to prior work

Neumayer, Schäfer, and Ullrich (arXiv:2610.32699v1, first posted October 23, 2026) prove probabilistic existence and constructive near-reference positive quadrature rules for general finite-dimensional spaces using Lewis-density sampling and logarithmic oversampling. Their paper's Sections 1.1–1.2 and 2.3 give qualitative and quantitative high-probability bounds, not this exact uniform-node quadratic moment law or its two-mechanism asymptotic prefactors. The present theorem studies **feasibility with unrestricted nonnegative weights**, not their stronger near-reference-weight property, and it makes no claim to improve their universal bounds.

Hayakawa, Lyons, and Oberhauser (2023) treat probabilities that a fixed vector belongs to a random convex hull, giving general inequalities in terms of Tukey/halfspace depth and sample size. The event here is an instance of their random-convex-hull formulation. General depth-based bounds alone do not specify the present exact all-\(m\) integrals, the \(m=3\) probability, or the sharp \(\sqrt m\)-versus-constant asymptotic prefactors. Wendel's symmetric-point probability formula is inapplicable: the lifted node distribution \((X,X^2-c)\) is generally not centrally symmetric.

The related randomized-least-squares positive-weight analysis of Bělík, Narayan, and Turnage (2026) constrains a specific weight-construction procedure, whereas the present theorem asks whether **any** positive exact quadratic weights exist. Published findings on affine least-squares quadrature failure and positivity of deterministic Legendre/Korobov weights involve different spaces or weight rules, so neither implies this quadratic random-support classification.

## Limitations

The exact law requires iid *uniform* nodes and only three polynomial moments. The target measure can differ from the sampling law, and weights are chosen without upper, lower, closeness, or numerical-conditioning constraints. For strictly positive all-node weights the equivalence holds almost surely, not on exceptional algebraic node configurations. The asymptotic equivalences are pointwise for fixed \(c\in(0,1)\); they are not claimed to be uniform as \(c\to0\), \(c\to1\), or within a sample-size-dependent window around \(c_*\). Extensions to higher polynomial degree, dependent sampling, and explicit weight-stability bounds are not proved. Independent mathematical validation has not been performed.

## References

1. S. Neumayer, M. Schäfer, and T. Ullrich, *Random nodes with positive weights: Richter-Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (posted 2026-10-23), https://arxiv.org/abs/2610.32699.
2. S. Hayakawa, T. Lyons, and H. Oberhauser, *Estimating the probability that a given vector is in the convex hull of a random sample*, *Probability Theory and Related Fields* **185** (2023), 705–746, https://doi.org/10.1007/s00440-022-01186-1; arXiv:2101.04250.
3. F. Bělík, A. Narayan, and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1 (2026), https://arxiv.org/abs/2609.09506.
4. S. Hayakawa, *Convex-Geometric Error Bounds for Positive-Weight Kernel Quadrature*, arXiv:2605.05705v1 (2026), https://arxiv.org/abs/2605.05705.
5. J. G. Wendel, *A Problem in Geometric Probability*, *Mathematica Scandinavica* **11** (1962), 109–111, https://doi.org/10.7146/math.scand.a-10655.
