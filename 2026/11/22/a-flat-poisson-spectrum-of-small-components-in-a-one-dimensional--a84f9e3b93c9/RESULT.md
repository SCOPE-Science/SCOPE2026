# A flat Poisson spectrum of small components in a one-dimensional random geometric graph

## Finding

Let \(n\ge2\) independent uniform points lie in \([0,1]\). Join two points at separation at most \(r\), where \(0<r<1\). Let \(C_n\) be the number of connected components, and \(N_{n,j}\) the number of components containing exactly \(j\) sampled points.

**Exact conditional law.** Conditional on \(C_n=c\), whenever that event has positive probability, the ordered component sizes are uniform among all \(\binom{n-1}{c-1}\) positive integer compositions of \(n\) into \(c\) parts, irrespective of \(r\). Define \(J(t,v)=\binom{t-1}{v-1}\) for integers \(t\ge v\ge1\), \(J(0,0)=1\), and \(J(t,v)=0\) otherwise. For every fixed \(K\ge1\) and nonnegative integers \(a_1,\ldots,a_K\), with \(A=\sum_{j=1}^K a_j\) and \(S=\sum_{j=1}^K ja_j\), the complete mixed factorial-moment formula is

\[
\mathbb E\!\left[\prod_{j=1}^K(N_{n,j})_{a_j}\mid C_n=c\right]
=\frac{(c)_A\,J(n-S,c-A)}{J(n,c)},
\]
where \((u)_v=u(u-1)\cdots(u-v+1)\) and \((u)_0=1\). In particular, \(\mathbb E[N_{n,1}\mid C_n=c]=c(c-1)/(n-1)\).

**Critical-window joint Poisson plateau.** Fix \(x\in\mathbb R\) and let
\[
r_n=\frac{\log n+x}{2n}.
\]
For every *fixed* positive integer \(K\), as \(n\to\infty\),
\[
\frac{C_n}{\sqrt n}\xrightarrow{\mathbb P}e^{-x/2},\qquad
(N_{n,1},\ldots,N_{n,K})\xrightarrow{d}
(Z_1,\ldots,Z_K),
\]
where \(Z_1,\ldots,Z_K\) are independent and each follows \(\operatorname{Poisson}(e^{-x})\). Thus **every fixed component size has the same limiting expected count**, jointly with asymptotic independence. More generally, for any deterministic integer sequence \(c_n/\sqrt n\to a\in(0,\infty)\), conditional on \(C_n=c_n\), the first \(K\) size-counts converge jointly to independent \(\operatorname{Poisson}(a^2)\) variables.

## Assumptions and scope

All positions are independent and exactly uniform on the closed unit interval; the edge rule is deterministic at distance \(r\). Ties occur with probability zero. The exact conditional identities hold for every finite \(n\ge2\), feasible \(1\le c\le n\), and radius \(0<r<1\) for which the conditioning event has positive probability. The asymptotic statement holds for fixed \(x\), fixed finite \(K\), and a radius \(r_n\) which belongs to \((0,1)\) eventually. It does not concern random Poisson vertex counts, nonuniform intensity, higher-dimensional graphs, or growing \(K\).

## Proof

**1. Uniform cuts.** Write the order statistics as \(X_{(1)}<\cdots<X_{(n)}\) and their \(n+1\) spacings, including boundary spacings, as \(D_0,\ldots,D_n\). Their joint law is \(\operatorname{Dirichlet}(1,\ldots,1)\). There is a graph-component cut between \(X_{(i)}\) and \(X_{(i+1)}\) exactly when \(D_i>r\), for \(1\le i<n\). All internal spacings are exchangeable, so, conditional on there being precisely \(c-1\) cuts, each subset of \(c-1\) cut locations has equal probability. Their successive differences are therefore exactly the uniformly distributed positive compositions of \(n\) into \(c\) parts. This is not merely an asymptotic approximation and does not rely on independence of adjacent gaps.

**2. Exact conditional factorial moments.** In the product \(\prod_j(N_{n,j})_{a_j}\), choose and order \(A\) distinct component positions, specifying \(a_j\) positions to have length \(j\). There are \((c)_A\) assignments. After those lengths use \(S\) points, the remaining \(c-A\) positive parts have exactly \(J(n-S,c-A)\) completions. Divide by \(J(n,c)\). The convention \(J(0,0)=1\) covers all-boundary cases, including \(c=n\).

**3. Conditional rare-size spectrum.** If \(c=c_n\) and \(c_n/\sqrt n\to a>0\), the preceding ratio for any fixed \(A,S\) satisfies
\[
\frac{(c)_A\,J(n-S,c-A)}{J(n,c)}
=\frac{(c)_A(c-1)_A(n-c)_{S-A}}{(n-1)_S}
\longrightarrow a^{2A}.
\]
The displayed product identity holds for all sufficiently large \(n\), since then \(n-S\ge c-A\ge1\). These are precisely the mixed factorial moments of independent \(\operatorname{Poisson}(a^2)\) counts. First moments ensure tightness, and the limiting independent Poisson vector is uniquely determined by its factorial moments (equivalently its moment-generating function), establishing joint weak convergence. Here \(K\), \(a_j\) and their sum \(A\) are always fixed before \(n\to\infty\).

**4. Random component count at the critical radius.** For \(r=r_n\), put \(I_i=\mathbf1\{D_i>r\}\) for \(1\le i<n\). Uniform-simplex volume gives
\[
q_n=\mathbb P(I_i=1)=(1-r_n)^n,
\quad q_{2,n}=\mathbb P(I_i=I_j=1)=(1-2r_n)_+^n
\]
for \(i\ne j\). Therefore \(C_n=1+\sum I_i\), \(\mathbb E(C_n-1)=(n-1)q_n\sim e^{-x/2}\sqrt n\), and
\[
0\le\operatorname{Var}(C_n)
=(n-1)q_n(1-q_n)+(n-1)(n-2)(q_{2,n}-q_n^2)
\le(n-1)q_n=O(\!\sqrt n\!),
\]
because \((1-2r)_+\le(1-r)^2\). Chebyshev's inequality proves \(C_n/\sqrt n\to e^{-x/2}\) in probability. Moreover \(\mathbb E[C_n^2/n]\to e^{-x}\), so \(C_n^2/n\) converges in mean as well as in probability. The conditional mean of \(N_{n,j}\) is bounded by \(C_n(C_n-1)/(n-1)\), and its ratio to that bound tends to one whenever \(C_n/\sqrt n\to e^{-x/2}\) with \(j\) fixed; mean convergence and uniform integrability therefore give \(\mathbb E N_{n,j}\to e^{-x}\). Conditioning on \(C_n\), apply Step 3 to any deterministic subsequence of realizable counts with the same scaled limit; this and bounded convergence for conditional expectations of bounded continuous test functions give the unconditional joint weak limit.

## Verification

Run `python3 verify.py` with the Python standard library. It enumerates exact uniform compositions, checks boundary cases, validates mixed factorial moments against direct composition enumeration, checks the radius-independent cut-count distribution using inclusion–exclusion on Dirichlet spacings, and checks the negative cut-indicator covariance bound. It reports 5,345 exact assertions (3,343 initial, 1,458 mixed-factorial, and 544 covariance assertions). Those checks test finite examples only; the all-\(n\) statements and asymptotic limits are established by the analytical proof above.

## Relationship to prior work

Decreusefond and Ferraz (first publicly posted 30 August 2010) study a **Poisson-number-of-points** one-dimensional geometric graph, derive queueing transforms and the total number of components, and identify cluster lengths; those statements do not directly give the fixed-sample size-spectrum factorial moments or the simultaneous finite-size Poisson plateau here. Zhao, Yağan and Gligor (arXiv posting 2 February 2015, **subsequently withdrawn**) describe the distinct zero–one isolation threshold \(\log n/(2n)\); their result does not specify the joint asymptotic counts of all fixed sizes inside that threshold window. Penrose (initial posting 25 July 2015) gives general Poisson approximation theorems for fixed-order components, but Theorems 2.2–2.3 require a connection kernel uniformly tending to zero, or uniformly bounded below one; both hypotheses fail for the hard graph kernel, which has supremum one. These theorems therefore do not imply the present hard-geometric vector law. Prior work also treats isolated counts jointly with Gaussian component-count fluctuations on the **circle**; the single-size marginal does not imply the joint flat spectrum for the **interval**. Independent Poisson plateaus are known in other finite-range percolation models, but their bond-percolation component mechanism does not imply the uniform geometric-point formula here. The exchangeability/composition step itself is a classical consequence of uniform spacings and is not asserted as new in isolation.

## Limitations

The novelty assessment is relative to the cited inspected sources and targeted prior-result comparisons, not a guarantee of historical priority across all random-composition and renewal-process literature. Related older geometric-graph and discrete-composition theorems could supply an equivalent formulation; some such sources were not fully accessible. No total-variation rate, infinite-dimensional joint limit, or claim of independence at finite \(n\) is made. The self-review is not independent validation.

## References

1. L. Decreusefond and E. Ferraz, *On the One Dimensional Poisson Random Geometric Graph*, arXiv:1008.5140 (initial posting 2010-08-30), https://arxiv.org/abs/1008.5140; Journal of Probability and Statistics (2011), DOI:10.1155/2011/350382.
2. M. D. Penrose, *Inhomogeneous Random Graphs, Isolated Vertices, and Poisson Approximation*, arXiv:1507.07132 (initial posting 2015-07-25), https://arxiv.org/abs/1507.07132; Journal of Applied Probability 55 (2018), 112–136.
3. J. Zhao, O. Yağan and V. Gligor, *A Curious Gap in One-Dimensional Geometric Random Graphs between Connectivity and the Absence of Isolated Node*, arXiv:1502.00404 (initial posting 2015-02-02, **withdrawn**), https://arxiv.org/abs/1502.00404. The earlier related zero–one-law work of Appel and Russo (2002) and Han and Makowski (2008) is also acknowledged.
4. Uniform order-statistic spacings and their Dirichlet distribution: classical probability theory; this input is used as standard background rather than attributed as a new result.
