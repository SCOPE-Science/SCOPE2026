# Sharp failure exponent for positive cubic quadrature from uniform random nodes

## Finding
Let \(X_1,\ldots,X_N\) be independent uniform points on \([-1,1]\), with \(N\ge4\), and write \(F_N\) for the event that no nonnegative weights \(w_1,\ldots,w_N\) satisfy
\[
\sum_{i=1}^N w_i X_i^k = \frac12\int_{-1}^1 x^k\,dx \quad(k=0,1,2,3).
\]
Put \(g=1/\sqrt3\) and \(\beta=(1+g)/2\). Then for every integer \(N\ge4\),
\[
\boxed{\beta^N\le\Pr(F_N)\le2\binom N3\beta^{N-3}},\qquad
\boxed{\lim_{N\to\infty}\Pr(F_N)^{1/N}=\frac{1+1/\sqrt3}{2}}.
\]
The same exponent applies to the absence of **strictly positive weights on every sampled node**, since these two failure events agree almost surely. The upper bound may exceed one for small \(N\); it is intended as a finite-sample valid bound and sharp exponential-rate certificate, not as an exact finite-sample probability.

## Assumptions and scope
The reference integral is the uniform *probability* integral on the fixed interval \([-1,1]\). The polynomial space is \(\mathcal P_3=\operatorname{span}\{1,x,x^2,x^3\}\). Nodes are independent and continuously uniform. Weights are not required to be equal, bounded by a given multiple of \(1/N\), or obtained by a specified algorithm; this is an existence result. The claim is an exponential failure rate, not a sharp subexponential prefactor. The primary mathematical topic is positive numerical quadrature.

## Proof
**1. Sharp cubic sign-support lemma.** Let \(p\not\equiv0\) be real of degree at most three and suppose \(I(p):=\frac12\int_{-1}^1p(x)\,dx\le0\). The set \(\{x\in[-1,1]:p(x)<0\}\) has total length at least \(1-g\), where \(g=1/\sqrt3\). Equivalently, under uniform sampling, \(\Pr(p(X)\ge0)\le\beta\). The bound is attained by \(p(x)=(x+g)^2(g-x)\), which has zero mean and is negative precisely on \((g,1]\) except irrelevant isolated zeros.

To prove the lemma, two-point Gauss–Legendre quadrature is exact on \(\mathcal P_3\):
\[
I(p)=\frac{p(-g)+p(g)}2.
\]
If the negative set is a single terminal interval of length less than \(1-g\), neither Gaussian node is negative; in fact at least one has a strictly positive value (a nonzero degree-three polynomial cannot have both as even-multiplicity zeros). The Gauss identity contradicts \(I(p)\le0\). If the negative set consists of two terminal intervals of total length less than \(1-g\), both Gauss points lie in the strictly positive central interval, again a contradiction.

If the negative set is a single interior interval \((a,b)\), then \(-1<a<b<1\) and, up to a positive factor,
\[
p(x)=(x-a)(x-b)(\alpha+\gamma x),\qquad \alpha>0,\quad |\gamma|\le\alpha.
\]
The mean is \(I(p)=\alpha(1/3+ab)-\gamma(a+b)/3\). The hypothesis \(I(p)\le0\) implies \(1+3ab\le|a+b|\). With midpoint \(m=(a+b)/2\) and half-width \(h=(b-a)/2\),
\[
h^2\ge\big(|m|-1/3\big)^2+2/9,
\]
so this negative interval has length at least \(2\sqrt2/3>1-g\).

There remains the arrangement of a negative left-terminal interval together with a negative interior interval. Write the three sign-changing roots as \(-1<a<b<c<1\), with negative set \([-1,a)\cup(b,c)\), and take \(p(x)=(x-a)(x-b)(x-c)\). Its mean is \(-[a+b+c+3abc]/3\). Put \(t=-a\), \(v=c-b\). If the total negative length \(L=1-t+v\) were less than \(1-g\), then \(g<t\le1\), \(0<v<t-g\). The necessary condition \(I(p)\le0\) would give
\[
0\le a+b+c+3abc=-t+2b+v-3tb(b+v).
\]
Completing the square in \(b\) bounds the right side by
\[
-t+\frac1{3t}+\frac{3tv^2}{4}
< -t+\frac1{3t}+\frac{3t(t^2-g^2)}4
=\frac{(3t^2-1)(t^2/4-1/3)}t<0,
\]
a contradiction. Reflection handles a right-terminal-plus-interior negative set. All sign arrangements for nonzero polynomials of degree at most three have now been covered; repeated or endpoint zeros simply remove sign changes and fall under the same cases. This proves the lemma, including the equality example.

**2. Lower bound.** Set \(p_0(x)=(x+g)^2(g-x)\). Its mean is zero by Gauss quadrature and \(p_0(x)>0\) for all \(-1\le x<g\) except \(x=-g\). If every sampled point lies below \(g\), any nonnegative normalized weights give a strictly positive quadrature value for \(p_0\), almost surely, and cannot reproduce its zero integral. This event has probability \(\beta^N\).

**3. Upper bound.** The point \(\mu=(0,1/3,0)\in\mathbb R^3\) must belong to the convex hull of the moment-curve nodes \(v(X_i)=(X_i,X_i^2,X_i^3)\) exactly when nonnegative normalized cubic-exact weights exist. For \(N\ge4\) the distinct sampled nodes are almost surely in general affine position: every four augmented moment vectors form a nonzero Vandermonde determinant. Their convex hull is therefore a full-dimensional simplicial polytope, with each facet supported by exactly three sample points.

If \(\mu\) lies outside this polytope, at least one facet inequality is violated. Its oriented affine functional in moment space is a nonzero polynomial \(p\in\mathcal P_3\) vanishing at the three facet nodes, satisfying \(p(X_i)\ge0\) at every remaining node, and \(I(p)=p(\mu)<0\). For any fixed triple of sampled nodes, the corresponding polynomial, up to scaling, is \(\pm\prod_{j\in T}(x-X_j)\); there are only two orientations. Conditional on the three nodes, the sign-support lemma shows that the chance of all remaining \(N-3\) nodes being nonnegative for an orientation whose mean is nonpositive is at most \(\beta^{N-3}\). Union-bounding over the two orientations and \(\binom N3\) triples proves the stated upper bound.

Finally, taking \(N\)-th roots of the two bounds and sending \(N\to\infty\) gives the sharp exponential limit. An interior point of a finite convex hull admits a representation with strictly positive coefficients on *every* generating point (average suitable positive-weight representations). Conversely strict weights imply the target is interior when the hull is full-dimensional. The target lies on a facet with probability zero, since the signed integral of a random triple-root cubic is a nonzero polynomial in its three continuously distributed roots. Thus the strict-weight and nonnegative-weight events agree almost surely.

## Verification
Run `python checker.py` using Python and SymPy. It checks Gauss exactness for degrees zero through three, the extremal zero-mean cubic, the triple-root moment identity, the vertex bound in the mixed-interval case, and the interior-interval mean identity. A seeded set of 20,000 random root triples checks the sign-support inequality numerically as a diagnostic. The infinite-probability statement follows from the analytical proof above, *not* from finite experiments. The closed-form bounds can be evaluated without any computational package.

## Relationship to prior work
Neumayer, Schäfer and Ullrich (2026) construct positive random-node Richter–Tchakaloff rules for general finite-dimensional spaces and provide dimension-dependent sufficient sampling bounds; their general result does not give the sharp fixed-space failure exponent derived here. Previously published uniform-node degree-two feasibility calculations obtain a different sharp base \(2/3\); the current result concerns simultaneous exactness up to degree three and uses the full three-dimensional moment curve rather than only the first two nontrivial moments. More general existence and numerical stability literature does not imply the explicit constant \((1+1/\sqrt3)/2\) in this specific random model without an additional extremal sign-support analysis.

## Limitations
The union bound is not an asymptotic equivalence for the failure probability and yields no polynomial prefactor. All weights may be nonnegative rather than well-conditioned or nearly equal, and no weight-finding algorithm is analyzed. The exponent is specific to independent uniform points on one interval and degree at most three. The literature comparison is bounded by accessible published sources and mathematical-record searches; historical priority is not independently certified.

## References
1. S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1, 23 October 2026, https://arxiv.org/abs/2610.32699.
2. *Exact all-sample positivity probabilities for random quadratic quadrature*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-all-sample-positivity-probabilities-for-random-quadratic-q--c46807d7872b.
3. *Exact random-node feasibility and a two-mechanism phase transition for positive quadratic quadrature*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-random-node-feasibility-and-a-two-mechanism-phase-transiti--03159ea86990.
4. *Stable high-order randomized cubature formulae in arbitrary dimension*, Journal of Approximation Theory (2022), https://doi.org/10.1016/j.jat.2022.105706 (publisher full text was not accessible during the comparison).
