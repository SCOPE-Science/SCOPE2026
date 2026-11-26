# A one-switch law for nested isolation counts in circular geometric graphs

## Finding
Let \(n\ge3\) points be sampled independently and uniformly on a circle of circumference one. At radius \(r\in(0,1/2)\), connect distinct points whose shorter circular distance is at most \(r\), and let \(I_n(r)\) count isolated vertices. Although \(I_n(s)\le I_n(t)\) for \(0<t\le s<1/2\), the covariance of these nested counts may be **strictly negative**.

Write \(P_n(u)=(1-u)_+^{n-1}\), where \(z_+=\max(z,0)\). The exact cross-radius covariance is
\[
\boxed{\operatorname{Cov}(I_n(t),I_n(s))=n\left[P_n(2s)+2P_n(t+2s)+(n-3)P_n(2t+2s)-nP_n(2t)P_n(2s)\right].}\tag{1}
\]
Define the sharp smaller-radius boundary
\[
t_c(n)=\frac{1-n^{-1/(n-1)}}2.\tag{2}
\]
The **complete finite-size sign classification** for every \(n\ge3\) and \(0<t\le s<1/2\) is:

1. If \(0<t<t_c(n)\), there is exactly one \(s_*(n,t)\in(t,(1-t)/2)\) with covariance zero; covariance is strictly positive for \(t\le s<s_*\) and strictly negative for \(s_*<s<1/2\).
2. If \(t=t_c(n)\), covariance is positive for \(t\le s<(1-t)/2\) and zero for every \((1-t)/2\le s<1/2\).
3. If \(t_c(n)<t<1/2\), covariance is strictly positive at every \(t\le s<1/2\).

The unique root in case 1 can be found without optimization: let \(z\) be the unique solution in \((t/(1-2t),1)\) of
\[
1+2(1-z)^{n-1}+(n-3)(1-2z)_+^{n-1}=n(1-2t)^{n-1};\tag{3}
\]
then \(s_*(n,t)=(1-t/z)/2\). For instance, \(n=3,t=1/10,s=2/5\) yields the **exact negative covariance** \(-63/1250\).

There is also a sharp sparse-radius dependence frontier: for fixed \(0<x\le y\),
\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}\left(I_n(x/n),I_n(y/n)\right)=e^{-2(x+y)}\left[e^{2x}+2e^x-3-4xy\right].\tag{4}
\]
The limiting covariance has exactly one sign reversal in \(y\), at
\[
y_c(x)=\frac{e^{2x}+2e^x-3}{4x}>x,\qquad n s_*(n,x/n)\longrightarrow y_c(x).\tag{5}
\]

## Assumptions and scope
The sample size is deterministic and satisfies \(n\ge3\). Positions are independent and exactly uniform on the circle, with the shortest-arc metric. The graph has a hard deterministic radius; it is not a Poissonized, independently thinned, or soft random connection graph. All radius inequalities may be taken strict because ties occur with probability zero. The first three parts concern exact finite-sample covariance at all radii \(0<t\le s<1/2\); the last part concerns fixed positive \(x\le y\) as \(n\to\infty\). No claim is made about the full joint distribution or correlation coefficients.

## Proof
**Dirichlet spacing representation.** Use the first sampled point as the starting vertex in the cyclic order, rather than the first point clockwise from a fixed spatial origin. Rotate it to zero. Conditional on its original location, the other \(n-1\) rotated points remain iid uniform. The spacings of their order statistics with endpoints 0 and 1 are the \(n\) clockwise gaps \(D_1,\dots,D_n\); their joint law is \(\operatorname{Dirichlet}(1,\dots,1)\). The isolate counts are independent of this choice of indexing. For distinct gap indices with nonnegative lower bounds \(a_j\), translating the corresponding coordinates in the simplex gives
\[
\Pr(D_{i_j}>a_j\text{ for all }j)=\left(1-\sum_j a_j\right)_+^{n-1}.\tag{6}
\]
Vertex \(i\) is isolated at radius \(r\) if and only if **both** its adjacent gaps \(D_{i-1},D_i\) exceed \(r\). Consequently \(\mathbb E I_n(r)=nP_n(2r)\).

**Exact mixed moment.** Expand \(\mathbb E I_n(t)I_n(s)\) over cyclic ordered pairs of vertices, with \(t\le s\). There are \(n\) identical-vertex pairs; both adjacent gaps must exceed \(s\), contributing \(nP_n(2s)\). There are \(2n\) pairs of distinct neighboring vertices; their three involved gaps require lower bounds totaling \(t+2s\), contributing \(2nP_n(t+2s)\). There are \(n(n-3)\) remaining ordered pairs; their four distinct gaps require total lower bound \(2t+2s\), contributing \(n(n-3)P_n(2t+2s)\). This enumeration also covers \(n=3\), where the last class is empty. Subtracting the product \(n^2P_n(2t)P_n(2s)\) proves (1).

**Finite one-switch argument.** The positive factor \(nP_n(2s)\) can be removed since \(s<1/2\). Put \(z=t/(1-2s)>0\). Equation (1) becomes
\[
\frac{\operatorname{Cov}(I_n(t),I_n(s))}{nP_n(2s)}=F_n(z)-n(1-2t)^{n-1},\quad F_n(z)=1+2(1-z)_+^{n-1}+(n-3)(1-2z)_+^{n-1}.\tag{7}
\]
For every \(n\ge3\), \(F_n\) is continuous and strictly decreasing for \(0<z<1\), and equals one for \(z\ge1\). As \(s\) increases, \(z=t/(1-2s)\) increases strictly. At \(s=t\) the original covariance is \(\operatorname{Var}(I_n(t))>0\): a cluster of all points within an arc shorter than \(t\) yields no isolates, while a configuration with one vertex separated from the others by both adjacent gaps exceeding \(t\) yields an isolate; both configurations have positive probability for \(t<1/2\). The terminal normalized sign is that of \(1-n(1-2t)^{n-1}\), changing exactly at (2). If it is negative, continuity and strict monotonicity give one root before \(z=1\), whose representation is (3). If it is zero, (7) is positive until \(z=1\) and then identically zero. If it is positive, (7) stays positive. This proves all cases and all boundary statements.

**Sparse limit.** For fixed \(u\), \((1-u/n)^{n-1}=e^{-u}[1+(u-u^2/2)/n+O(n^{-2})]\). Apply this to (1), with \(t=x/n,s=y/n\). The four-distinct-gap term, minus the product of means, has limit per vertex \(-(3+4xy)e^{-2(x+y)}\); the same and adjacent vertex terms contribute \(e^{-2y}+2e^{-(x+2y)}\). This proves (4). Its bracket decreases strictly and affinely in \(y\) and vanishes only at (5). To see that \(y_c(x)>x\), put \(h(x)=e^{2x}+2e^x-3-4x^2\). Then \(h(0)=0\) and the Taylor lower bounds \(e^{2x}\ge 1+2x+2x^2\), \(e^x\ge 1+x\) give \(h'(x)\ge4-2x+4x^2>0\) for \(x>0\). Also \(nP_n(2x/n)\to\infty\), so \(x/n<t_c(n)\) eventually. For any \(x\le y_-<y_c(x)<y_+\), the limiting covariances per vertex at \(y_-\) and \(y_+\) have opposite strict signs, and thus so do their finite-size versions for all large \(n\). The unique finite-size zero satisfies \(y_-<ns_*(n,x/n)<y_+\). Taking arbitrarily close brackets proves (5).

## Verification
Run the accompanying standard-library script `verify.py` using `python verify.py`. It independently enumerates all ordered vertex pairs and their gap requirements in exact rational arithmetic before comparing with (1). It also tests the monotonic sign sequence at many radii and checks sparse-scale approximations against (4). A separate direct simulation from sorted uniform points (300,000 samples at each of three configurations) matched the predicted negative covariances within sampling error. These finite checks are corroboration; the all-parameter proof rests on the simplex-volume identity and exact monotonicity.

## Relationship to prior work
Wilsher, Dettmann and Ganesh (2022) study isolated-node counts and a Poisson limit on a one-dimensional torus under random Poisson vertex counts and genuinely soft independent-edge connections; their nontrivial soft-connection assumption excludes deterministic hard cutoffs. Their 2020 precursor gives one-radius mean and variance analysis in a Poisson soft-graph setting. Dłotko and coauthors (2022) motivate multiscale geometry through Euler characteristic curves but do not present the covariance of nested isolated-vertex counts.

Earlier public findings about *single-gap exceedance counts* establish a different one-switch law and a zero plateau. These do **not** give (1): isolation requires the intersection of **two adjacent gap exceedances**, and mixed moments involve distinct overlap classes with two, three, and four gaps, rather than one and two. Prior isolated-vertex/edge covariance formulas concern different observables at the **same radius**. Classical simplex survival identities and one-radius isolation theory are not claimed as novel; the assessed contribution is the exact two-radius isolation covariance and complete one-switch classification, including its distinct sparse crossover (5).

## Limitations
The result does not extend automatically to nonuniform point distributions, independent-edge graphs, higher-dimensional random geometric graphs, or Poissonized sample sizes. Covariance sign is not a statement of statistical independence or monotone stochastic association. General earlier random geometric graph or spacing literature may implicitly contain the same special case; its complete historical priority remains unverified.

## References
1. M. Wilsher, C. P. Dettmann and A. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, arXiv:2202.08044, first publicly posted 2022-02-16. https://arxiv.org/abs/2202.08044
2. M. Wilsher, C. P. Dettmann and A. Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs*, arXiv:2007.06301, first publicly posted 2020-07-13. https://arxiv.org/abs/2007.06301
3. P. Dłotko, N. Hellmer, Ł. Stettner and R. Topolnicki, *Topology-Driven Goodness-of-Fit Tests in Arbitrary Dimensions*, arXiv:2210.14965, first publicly posted 2022-10-25. https://arxiv.org/abs/2210.14965
4. *One-switch and zero-plateau law for multiscale circular coverage gaps*, Resultary public record (2026), https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-one-switch-and-zero-plateau-law-for-multiscale-circular-coverage--53ce2ae4db4a
5. *One sign reversal across scales for component counts in a one-dimensional random geometric graph*, Resultary public record (2026), https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-one-sign-reversal-across-scales-for-component-counts-in-a-one-di--b5b7d44a06aa
6. *Double sign reversal of edge–isolate covariance on the random geometric circle*, Resultary public record (2026), https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-double-sign-reversal-of-edge-isolate-covariance-on-the-random-ge--8d8230a37768
