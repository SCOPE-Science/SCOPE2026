# Polar volumes of complete-split symmetric edge polytopes: a Gaussian critical window

## Finding
For every integer pair \(p,q\ge2\), consider the complete-split graph \(G_{p,q}=K_p\vee\overline{K_q}\) and the symmetric edge polytope \(P_{p,q}\). The polar's volume is an explicit binomial tail:
\[
\operatorname{vol}_{n-1}(P_{p,q}^{\circ})=\frac{1}{\sqrt n}\frac{n}{\binom np}\sum_{j=p-1}^{n-1}\binom{n-1}{j},\qquad n=p+q.
\]
The formula has a sharp transition between exponential volume growth and linear volume growth in rooted coordinates, with a Gaussian \(n^{3/2}\) critical window. Define the rooted-coordinate volume \(W_{p,q}=\sqrt n\,\operatorname{vol}_{n-1}(P_{p,q}^{\circ})\) and \(\alpha_n=p/n\). For \(\alpha_n\to\alpha\in(0,1/2)\),
\[
 W_{p,q}\sim n^{3/2}\sqrt{\frac{\pi\alpha_n(1-\alpha_n)}2}\exp\left(n[\log2-H(\alpha_n)]\right),\quad H(t)=-t\log t-(1-t)\log(1-t).
\]
For \(\alpha_n\to\alpha\in(1/2,1)\),
\[
 W_{p,q}\sim\frac{p^2}{p-q}\sim\frac{\alpha^2}{2\alpha-1}n.
\]
For every sequence with \((p-q)/\sqrt n\to s\in\mathbb R\),
\[
 \frac{W_{p,q}}{n^{3/2}}\longrightarrow F(s):=\frac14\int_0^{\infty}e^{-sx-x^2/2}\,dx=\frac{\sqrt{2\pi}}4e^{s^2/2}\Phi(-s).
\]
At \(p=q\), the critical coefficient is \(F(0)=\sqrt{\pi/2}/4\). Here \(\Phi\) is the standard normal cumulative distribution function and all logarithms are natural.

## Assumptions and scope
The graph has a designated clique of \(p\ge2\) vertices and an independent set of \(q\ge2\) vertices, joined by every possible cross-edge. Let \(H=\{u\in\mathbb R^{n}:\sum_i u_i=0\}\) with the inherited Euclidean inner product, and set
\[
 P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G_{p,q})\}\subset H.
\]
The polar is taken *inside \(H\)*, so
\[
 L_{p,q}=P_{p,q}^{\circ}=\{u\in H:|u_i-u_j|\le1\text{ for each edge }\{i,j\}\}.
\]
The indicated \((n-1)\)-volume is intrinsic Euclidean volume in \(H\), not normalized lattice volume. Fix the first clique vertex as the root and define \(x_i=u_i-u_1\), for the other \(n-1\) vertices. Lebesgue measure in these coordinates is denoted \(dx\); its volume \(W_{p,q}\) is related to intrinsic volume by the Jacobian \(\operatorname{vol}_{n-1}(L_{p,q})=W_{p,q}/\sqrt n\). All asymptotic sequences have integer \(p,q\ge2\) tending to infinity with \(n=p+q\), and the stated regime hypotheses specify their limits.

## Proof
**Step 1: fiber integration.** For a fixed clique configuration \(x_1=0,x_2,\ldots,x_p\), all clique constraints are equivalent to its range \(r=\max_{i\le p}x_i-\min_{i\le p}x_i\) lying in \([0,1]\). The allowable interval for each independent-set coordinate is \([\max_{i\le p}x_i-1,\,\min_{i\le p}x_i+1]\), of length \(2-r\). The independent coordinates are mutually unconstrained, so their total fiber volume is \((2-r)^q\).

**Step 2: exact range measure.** For any integrable \(f:[0,1]\to\mathbb R\), the rooted clique configurations satisfy
\[
\int_{\substack{x_1=0\\ \max x_i-\min x_i\le1}}f(\max x_i-\min x_i)\,dx_2\cdots dx_p
=p(p-1)\int_0^1r^{p-2}f(r)\,dr.
\]
To derive this identity, begin with \(p\) free real coordinates in an interval of length \(L\), integrate their range via choosing the unique minimum and maximum (ties have measure zero), and quotient the common-translation direction by anchoring the first coordinate to zero. Equivalently, for a fixed range \(r\), the set of anchored configurations has density \(p(p-1)r^{p-2}\). The latter equality can also be checked by partitioning according to which of the \(p\) coordinates are extremal and integrating the other \(p-2\) coordinates in their enclosing interval. Setting \(f(r)=(2-r)^q\) yields
\[
 W_{p,q}=p(p-1)\int_0^1 r^{p-2}(2-r)^q\,dr.
\]

**Step 3: binomial-tail identity.** Substitute \(r=2t\), so the integral becomes \(p(p-1)2^{n-1}B_{1/2}(p-1,q+1)\). The beta-binomial identity at probability \(1/2\), together with \(B(p-1,q+1)=(p-2)!q!/(n-1)!\), gives
\[
 W_{p,q}=\frac{n}{\binom np}\sum_{j=p-1}^{n-1}\binom{n-1}{j}.
\]
For the metric normalization, the inverse rooted map is \(u_i=x_i-\overline x\), with \(x_1=0\), and the Gram matrix of its \(n-1\) coordinate columns is \(I_{n-1}-\mathbf1\mathbf1^T/n\). Its determinant is \(1/n\). Hence intrinsic Euclidean volume is \(W_{p,q}/\sqrt n\).

**Step 4: the subcritical side.** If \(\alpha_n\to\alpha<1/2\), a Chernoff bound for a \(\operatorname{Bin}(n-1,1/2)\) variable shows
\[
 \sum_{j=p-1}^{n-1}\binom{n-1}{j}=2^{n-1}(1+o(1)).
\]
Uniform Stirling asymptotics for \(\binom np\), with \(\alpha_n\) retained in the exponential factor, give the first displayed asymptotic.

**Step 5: the supercritical side.** If \(\alpha_n\to\alpha>1/2\), the tail is dominated by its first term: the ratio of the following to the first term tends to \((1-\alpha)/\alpha<1\), and the ratios decrease as the summation index increases. Dominated convergence of the resulting series gives
\[
 \sum_{j=p-1}^{n-1}\binom{n-1}{j}
\sim\binom{n-1}{p-1}\frac{\alpha}{2\alpha-1}.
\]
Since \(\frac{n}{\binom np}\binom{n-1}{p-1}=p\), the second asymptotic follows as \(p^2/(p-q)\).

**Step 6: Gaussian crossover.** Suppose \((p-q)/\sqrt n\to s\). The standardized threshold in the binomial tail converges to \(s\); thus the central limit theorem makes that tail \(2^{n-1}(\Phi(-s)+o(1))\). The local Stirling approximation gives
\[
\binom np\sim 2^n\sqrt{\frac{2}{\pi n}}\exp(-s^2/2).
\]
Multiplication yields \(W_{p,q}/n^{3/2}\to(\sqrt{2\pi}/4)e^{s^2/2}\Phi(-s)\), which equals the integral representation of \(F(s)\) by completing the square. These three regimes exhaust the asserted hypotheses; no uniform approximation is claimed across unbounded window parameters.

## Verification
Run `python artifacts/verify.py` with Python, NumPy, and SciPy. The program compares the binomial-tail expression against exact rational polynomial integration in 840 parameter profiles. Separately it enumerates integer vertices of nine small polar polytopes through tight-edge spanning connectivity and compares their independently computed convex-hull volumes to the formula, using floating-point tolerances only in this independent geometric check. Expected marker:

`SPLIT_LIPSCHITZ_POLAR_VOLUME_CHECKS_PASSED exact_profiles=840 independent_hulls=9`

The infinite-parameter statements are proved analytically above. Exact finite checks do not certify the asymptotic limits.

## Relationship to prior work
The lead 2023 work of A. Mori, K. Mori, and H. Ohsugi establishes bounds on *facet numbers* of symmetric edge polytopes for graph joins, including a shared facet-potential criterion, but does not evaluate their polar volumes or derive a Gaussian volume crossover. Gordon–Petrov develop the combinatorics of Lipschitz polytopes in general. D'Alì–Juhnke-Kubitzke–Koch identify polar Ehrhart lattice points with bounded cuts, a general framework from which polar volumes can in principle be recovered by an additional asymptotic lattice-counting calculation; the explicit complete-split binomial-tail evaluation and the three sharp large-dimensional regimes are not stated there. Earlier volume results for *the original symmetric edge polytope* and for PQ adjacency polytopes are distinct from the intrinsic volume of its polar. The present claim makes no priority assertion beyond the materials inspected.

## Limitations
The exact formula requires an unweighted complete-split graph with the given standard edge-root realization and a polar in the zero-sum hyperplane. Other graph joins, weighted polars, the original polytope's volume, and fixed-ratio limits at the endpoints \(\alpha=0,1\) are not covered. The historical literature review may not exhaust alternative names for polar volume or general bounded-cut enumeration; independent assessment of novelty has not been performed.

## References
- A. Mori, K. Mori, H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, first publicly posted 2023-12-18, arXiv:2312.11287, https://arxiv.org/abs/2312.11287.
- J. Gordon, F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848, https://arxiv.org/abs/1608.06848.
- A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, first publicly posted 2023-07-10, arXiv:2307.04933, https://arxiv.org/abs/2307.04933.
- B. Braun, R. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303, https://arxiv.org/abs/2201.13303.
