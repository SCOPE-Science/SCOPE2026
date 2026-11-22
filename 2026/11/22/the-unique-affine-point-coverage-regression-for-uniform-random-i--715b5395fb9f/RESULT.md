# The unique affine point-coverage regression for uniform random interval graphs

## Finding
Let \(n\ge2\) and form the interval intersection graph of \(n\) independent intervals whose two endpoints are independent uniform points of \([0,1]\). Let \(E_n\) count the graph's edges and \(K_t\) count the intervals covering a fixed point \(t\in(0,1)\). Put \(c=2t(1-t)\) and \(s=1-c\). For every integer \(0\le k\le n\),
\[
\mathbb E[E_n\mid K_t=k]
=\binom{k}{2}+\frac23 k(n-k)
+\left(\frac23-\frac{c^2}{3s^2}\right)\binom{n-k}{2}.
\]
Its second forward difference in \(k\) is exactly
\[
\Delta_k^2\mathbb E[E_n\mid K_t=k]
=\frac{(2t-1)^2}{3s^2}.
\]
Thus the conditional expectation is affine in the point-coverage count **if and only if** \(t=1/2\), and at that unique point
\[
\boxed{\mathbb E[E_n\mid K_{1/2}=k]
=\frac{n(n-1)}6+\frac{(n-1)k}{3}.}
\]
The complete finite-sample second moments satisfy
\[
\begin{aligned}
\operatorname{Var}(E_n)&=\frac{n(n-1)(2n+1)}{45},\\
\operatorname{Var}(K_t)&=ncs,\\
\operatorname{Cov}(K_t,E_n)&=\frac{n(n-1)c^2}{3},\\
\operatorname{Corr}(K_t,E_n)^2&=\frac{5(n-1)c^3}{s(2n+1)}.
\end{aligned}
\]
Consequently the squared correlation, i.e. the fraction of edge-count variance explained by **linear** prediction from \(K_t\), is uniquely maximized at \(t=1/2\), where it equals
\[
\boxed{\frac{5(n-1)}{4(2n+1)}\longrightarrow\frac58.}
\]
At the midpoint, the conditional mean is affine, so the same number is also the fraction of variance explained by the optimal unrestricted square-integrable predictor based only on \(K_{1/2}\).

## Assumptions and scope
Intervals are labeled, sampled independently, and formed by sorting two independent \(\operatorname{Unif}[0,1]\) endpoints per interval. Distinct intervals are adjacent precisely when they intersect. Endpoint coincidences have probability zero. The theorem holds for all finite \(n\ge2\), all interior \(0<t<1\), and every attainable integer \(0\le k\le n\). The symbol \(\Delta_k^2\) means the second forward difference with respect to \(k\), defined for \(0\le k\le n-2\). The point \(t\) is fixed, not chosen adaptively from the realized graph. For endpoints sampled iid from any common continuous strictly increasing distribution, the same statements hold after replacing \(t\) by its cumulative probability \(F(t)\); the distinguished location is then its unique distributional median.

## Proof
**Conditional three-class decomposition.** Classify an interval as wholly left of \(t\), crossing \(t\), or wholly right of \(t\). Their probabilities are \(t^2,c,(1-t)^2\). Conditional on \(K_t=k\), the \(k\) crossing intervals form a clique. A crossing and a noncrossing interval overlap with probability \(2/3\): when the latter is left of \(t\), its two endpoints and the left endpoint of the crossing interval are independent uniform points on \([0,t]\); the crossing interval overlaps it unless the crossing interval's endpoint lies to the right of both other endpoints, an event of probability \(1/3\). The right-side case is identical.

For two noncrossing intervals, the conditional probabilities of being left and right are \(t^2/s\) and \((1-t)^2/s\). Two on opposite sides are disjoint; two on the same side meet with probability \(2/3\). Hence their conditional overlap probability is
\[
q_{00}=\frac{2(t^4+(1-t)^4)}{3s^2}
=\frac23-\frac{c^2}{3s^2}.
\]
Summing the \(\binom{k}{2}\), \(k(n-k)\), and \(\binom{n-k}{2}\) edge classes proves the first formula. Its second difference is \(1-2(2/3)+q_{00}=(s^2-c^2)/(3s^2)=(2t-1)^2/(3s^2)\). As \(n\ge2\) all three successive coverage values are possible; this vanishes exactly at the midpoint. Substitution gives the affine midpoint formula.

**Covariance.** For a crossing interval, its left and right endpoints are independent uniforms on \([0,t]\) and \([t,1]\). An independent uniform interval is disjoint from the crossing one with conditional probability \((t^2+(1-t)^2)/3=s/3\). Since an unconditional pair overlaps with probability \(2/3\), the covariance of one crossing indicator and the adjacent edge indicator equals \(c[(1-s/3)-2/3]=c^2/3\). Indicators associated with an edge not touching the designated interval are independent. There are \(n(n-1)\) directed vertex-edge incidences, giving the displayed covariance. The \(n\) crossing indicators are independent Bernoulli variables with success probability \(c\), yielding \(\operatorname{Var}(K_t)=ncs\).

**Edge-count variance.** One edge indicator has variance \(2/9\). Two edges with disjoint endpoint-interval labels are independent. Two sharing exactly one interval have covariance equal to the variance of the conditional overlap probability given that interval. Writing the shared interval as \([a,b]\), with joint density \(2\) on \(0<a<b<1\), that probability is \(g(a,b)=1-a^2-(1-b)^2\). Exact integration gives
\[
\mathbb E[g]=\frac23,\qquad \mathbb E[g^2]=\frac{22}{45},\qquad
\operatorname{Var}(g)=\frac{2}{45}.
\]
Thus
\[
\operatorname{Var}(E_n)
=\binom n2\frac29+6\binom n3\frac{2}{45}
=\frac{n(n-1)(2n+1)}{45}.
\]
Combining these three moment formulas gives the squared correlation. Because \(c=2t(1-t)\in(0,1/2]\), it is uniquely maximized at the midpoint: the function \(c^3/(1-c)\) is strictly increasing on this interval, while \(c\) uniquely peaks at \(t=1/2\). At the midpoint, the linear conditional expectation is the \(L^2\) orthogonal projection of \(E_n\) onto all functions of \(K_{1/2}\), establishing the unrestricted prediction statement and the limit \(5/8\).

## Verification
Execute `python3 checker.py` in the directory containing this file. It makes 522 dependency-free, exact-rational assertions. These include algebraic integration of the first two moments of \(g\), exhaustive enumeration of the three region labels of each interval through six vertices for five rational positions, all attainable conditional expectations, covariance identities, and midpoint regressions. The infinite-sample limit follows by direct division of exact finite expressions, not by the finite checks.

## Relationship to prior work
The original random interval graph model, its edge probability \(2/3\), and its leading edge density were studied by Scheinerman (1988). Diaconis, Holmes, and Janson (arXiv:1102.2841, Sections 2.3 and 4) treat this model in interval-graph limit theory and relate cliques to point coverage. Iliopoulos (arXiv:1507.06275, Sections 3.3 and 5.1) studies the edge count and establishes that the midpoint maximizes the probability an individual interval covers a point. These facts do not by themselves state the finite-sample conditional edge-count polynomial, its **unique affine location**, or the optimal squared edge-count prediction coefficient \(5(n-1)/[4(2n+1)]\). The result specifically quantifies how a one-location clique count predicts the global intersection count; it is not a restatement of the previously established leading edge density or midpoint coverage maximum.

## Limitations
There is no claim of independent validation or absolute historical priority. An older article central to this model, Scheinerman (1988), could not be read in full; its known results were compared through later full-text mathematical treatments. The regression uses a **fixed spatial point** and the two-independent-endpoints model, not arbitrary independent interval laws. Away from the midpoint the displayed squared correlation measures only optimal **linear** prediction: the unrestricted conditional regression is quadratic. No central limit theorem or full joint distribution is asserted. The finite checks complement, but do not substitute for, the exact proof.

## References
- E. R. Scheinerman, *Random interval graphs*, Combinatorica **8** (1988), 357–371. DOI: https://doi.org/10.1007/BF02189092.
- P. Diaconis, S. Holmes and S. Janson, *Interval graph limits*, first public arXiv version 2011-02-14, https://arxiv.org/html/1102.2841v1.
- V. Iliopoulos, *Random Interval Graphs*, first public arXiv version 2015-07-22, https://arxiv.org/html/1507.06275v1.
