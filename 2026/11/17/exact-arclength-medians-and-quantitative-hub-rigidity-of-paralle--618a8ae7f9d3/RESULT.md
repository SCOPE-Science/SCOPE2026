# Exact arclength medians and quantitative hub rigidity of parallel metric graphs

## Finding
Let \(G_m\) be a compact metric graph obtained by identifying the left endpoints of \(m\) intervals to a common hub \(A\), and their right endpoints to a common hub \(B\). Their positive lengths are \(\ell_1,\ldots,\ell_m\), and \(L=\sum_i\ell_i\). For normalized arclength measure \(\mu=ds/L\), write
\[
F(z)=\int_{G_m}d_{G_m}(z,y)\,d\mu(y).
\]
For \(m=1\), the unique minimizer is the interval midpoint. For \(m=2\), every point is a minimizer. For every \(m\ge3\), **the complete set of minimizers is exactly the two hubs** \(\{A,B\}\), even when edge lengths are unequal or tied.

For \(m\ge2\), with \(a=\min_i\ell_i\), the optimal value is
\[
F(A)=F(B)=\frac{\sum_{i=1}^m\ell_i^2+2aL-ma^2}{4L}.
\]
For \(m\ge3\), the conclusion is quantitative. If \(z\) is distance \(x\in(0,\ell_i)\) from \(A\) along edge \(i\), and \(j\ne i\) is **any** shortest other edge, then
\[
F(z)-F(A)\;\ge\;\frac{\min\{x,\ell_i-x\}}{4L}\sum_{k\notin\{i,j\}}\min\{\ell_i,\ell_k\}\;>0.
\]
No optimality of the numerical factor \(1/4\) in this stability estimate is asserted.

## Assumptions and scope
All edges have strictly positive finite lengths. The graph is endowed with its **intrinsic geodesic length metric**: an edge may be longer than the alternative route connecting its endpoints. Points, including interior points on different parallel edges, are integrated with **uniform one-dimensional arclength density**, not equal mass per edge or a measure concentrated at vertices. Edges are distinct even if their lengths coincide. The universal assertion holds for every integer \(m\ge1\).

## Proof
For \(m=1\), direct integration gives \(F(x)=[x^2+(L-x)^2]/(2L)\), uniquely minimized at \(L/2\). For \(m=2\), the glued graph is a metric circle, so \(F\equiv L/4\).

Now take \(m\ge3\). Fix an edge \(i\) of length \(s=\ell_i\), choose any shortest edge \(j\ne i\) of length \(b=\min_{k\ne i}\ell_k\), and parameterize the candidate point by \(x\in[0,s]\). The union of edges \(i\) and \(j\) is a metric circle of circumference \(s+b\), because every competing edge between the hubs has length at least \(b\). For targets belonging to these two edges, the full graph's shortest paths agree with that circle's shortest paths. Hence their **combined** contribution to \(LF(x)\) is independent of \(x\) (the integral of circular distance over the entire circle).

For each third edge \(k\notin\{i,j\}\), parameterize its points by \(y\in[0,\ell_k]\). Let \(\alpha_k(y)\) and \(\beta_k(y)\) denote the distances from \(A\) and \(B\), respectively, to \(y\) in the graph with edge \(i\) deleted. Since \(j\) is a shortest remaining hub-to-hub edge,
\[
\alpha_k(y)=\min\{y,b+\ell_k-y\},\qquad
\beta_k(y)=\min\{\ell_k-y,b+y\}.
\]
A shortest route from the interior of edge \(i\) to \(y\) leaves through either \(A\) or \(B\), so
\[
d(x,y)=\min\{x+\alpha_k(y),s-x+\beta_k(y)\}.
\]
For fixed \(y\), this is concave in \(x\). Moreover, reflection \(y\mapsto\ell_k-y\) interchanges \(\alpha_k\) and \(\beta_k\); therefore the integrals of this distance at \(x=0\) and \(x=s\) are equal. Concavity implies that each third edge contributes **nonnegatively** to \(LF(x)-LF(0)\).

To quantify the positive contribution put \(t_k(y)=(s+\beta_k(y)-\alpha_k(y))/2\). Subtracting the chord joining the endpoint values of the piecewise-affine concave distance, the exact contribution from edge \(k\) is
\[
2\int_0^{\ell_k}\left[\min\left\{x\left(1-\frac{t_k(y)}s\right),t_k(y)\left(1-\frac xs\right)\right\}\right]_+dy,
\]
where \([u]_+=\max\{u,0\}\). This formula is valid even when \(t_k(y)\) lies outside \([0,s]\). At \(y=\ell_k/2\) one has \(\alpha_k=\beta_k\) and \(t_k=s/2\). Both \(\alpha_k\) and \(\beta_k\) are \(1\)-Lipschitz functions of \(y\), so
\[
|t_k(y)-s/2|\le|y-\ell_k/2|.
\]
On the interval \(I_k=[\ell_k/2-\delta_k,\ell_k/2+\delta_k]\), where \(\delta_k=\min\{s,\ell_k\}/4\), one therefore has \(t_k(y)\in[s/4,3s/4]\). The nonnegative bracket above is at least \(\min\{x,s-x\}/4\) there (check separately \(x\le s/2\) and \(x\ge s/2\)). Thus the third-edge integral is at least \(\min\{x,s-x\}\min\{s,\ell_k\}/4\). Summing over the third edges and dividing by \(L\) gives the advertised quantitative estimate, which is strictly positive for every \(0<x<s\). All graph points are either hubs or belong to some edge interior, proving uniqueness.

It remains to evaluate the hub value. For a target a distance \(y\) along edge \(k\), let \(b_k=\min_{j\ne k}\ell_j\). The distance from hub \(A\) is \(\min\{y,\ell_k-y+b_k\}\). Its integral on edge \(k\) is \(\ell_k^2/2\) when \(b_k\ge\ell_k\), and otherwise \( (\ell_k^2+2b_k\ell_k-b_k^2)/4\). With \(a=\min_j\ell_j\), every edge either has \(b_k=a\) or is shortest itself, in which case the same quadratic expression with \(b_k=a=\ell_k\) also applies. The sum is \( [\sum_k\ell_k^2+2aL-ma^2]/4\), proving the formula. This also covers tied shortest edges.

## Verification
The included `checker.py` evaluates every edge integral via an independent exact piecewise-linear integration routine and compares it with the closed hub formula, circle case, and stability estimate. It also performs direct midpoint quadrature of the four competing shortest-path candidates. Run: `python3 checker.py`. Numerical tests do not replace the analytic proof.

## Relationship to prior work
Blanquero and Carrizosa (2012 preprint, published 2013) study precisely the general continuous-demand one-median objective on networks and establish a difference-of-convex decomposition and an algorithm, but do not classify the minimizers on all unequal-length parallel-edge graphs or provide this closed hub formula and positive gap. Their general method can, in principle, solve individual instances; no claim is made that the objective or its optimization was first introduced here.

Kennedy–Kurasov–Malenova–Mugnolo (2015) study the same two-hub multi-edge geometric family as *pumpkin* or *banana* quantum graphs, optimizing the spectral gap rather than arclength one-medians. Garijo–Márquez–Silveira (2023) and Baptista–Kennedy–Mugnolo (2023) study the *double* mean distance averaged over **both** endpoints, not its minimizer over one endpoint. The former additionally assumes each edge itself is shortest between its endpoints, an assumption generally violated by unequal-length parallel edges. Hansen–Labbé (1989) use an edge-to-point **maximum**, not a uniform arclength integral, in their different continuous p-median model. These comparisons concern statements and definitions, not titles alone.

## Limitations
The theorem requires uniform density per arclength and no vertex atoms. It does not assert hub optimality for general weighted densities, heterogeneous edge-demand masses, arbitrary metric graphs, or any optimal constant in the quantitative gap. The formulas use the intrinsic metric, not physical Euclidean embedding. Historical priority has not undergone independent audit; broad location-theory results remain a possible indirect derivation route.

## References
1. R. Blanquero and E. Carrizosa, *Solving the median problem with continuous demand on a network*, manuscript dated November 5, 2012; *Computational Optimization and Applications* **56** (2013), 723–734. https://idus.us.es/server/api/core/bitstreams/c248990d-954d-43b0-b17f-8f9747308ad4/content
2. J. B. Kennedy, P. Kurasov, G. Malenova, and D. Mugnolo, *On the Spectral Gap of a Quantum Graph*, arXiv:1504.01962v1, posted April 8, 2015. https://arxiv.org/abs/1504.01962
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, *Results in Mathematics* **78** (2023), 139. https://doi.org/10.1007/s00025-023-01902-w
4. L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952v1, posted December 8, 2023. https://arxiv.org/abs/2312.04952
5. P. Hansen and M. Labbé, *The continuous p-median of a network*, *Networks* **19** (1989), 595–606. https://doi.org/10.1002/net.3230190509
