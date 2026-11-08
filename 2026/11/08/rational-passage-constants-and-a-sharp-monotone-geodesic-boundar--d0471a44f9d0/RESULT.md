# Rational passage constants and a sharp monotone-geodesic boundary for binary two-step first-passage percolation

## Finding

Consider the undirected second power of the integer line: vertices are the integers and distinct vertices at distance at most two are joined. Each edge independently has passage weight \(1\) with probability \(p\in(0,1)\), and weight \(2\) otherwise. Let \(T_n\) be the minimum total weight over finite paths from \(0\) to \(n\). Put

\[
Z(p)=p^3+p^2-4p+4,\qquad
H(p)=14p^6-77p^5+197p^4-295p^3+272p^2-146p+36.
\]

Then the exact time constant and exact Gaussian fluctuation variance are

\[
\mu(p)=\frac{-p^3+5p^2-7p+4}{Z(p)},\qquad
\sigma^2(p)=\frac{p(1-p)H(p)}{Z(p)^3}>0.
\]

More precisely,

\[
\frac{T_n}{n}\longrightarrow\mu(p)\quad\text{almost surely and in }L^2,
\qquad
\frac{T_n-n\mu(p)}{\sqrt n}\Longrightarrow N(0,\sigma^2(p)),
\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(T_n)}n=\sigma^2(p).
\]

At the fair binary distribution, these constants are \(\mu(1/2)=13/19\) and \(\sigma^2(1/2)=544/6859\). The model also has a sharp deterministic path-geometry boundary: if every edge weight lies in an interval \([a,2a]\) with \(a>0\), some minimum-weight path between any two integers is strictly increasing or strictly decreasing in its vertex labels. The upper ratio \(2\) is sharp: for every \(b>2a\), an assignment of weights in \(\{a,b\}\) admits endpoints for which every minimum-weight path backtracks.

## Assumptions and scope

All edges of the full, two-sided infinite graph are present, and a path is a finite sequence of incident vertices; repeated vertices are permitted in the minimization but never needed for positive weights. The random weights are i.i.d. with probabilities exactly as stated. The displayed stochastic limits assume \(0<p<1\), not the degenerate endpoint distributions. At \(p=0\) and \(p=1\), the limiting speeds are respectively \(1\) and \(1/2\), and the fluctuation variances vanish. There is no finite-size uniformity assertion as \(p\) approaches an endpoint with \(n\).

## Proof

**1. Removing turns and distant excursions.** The local path shortcut works in the full infinite graph. If a path contains a strict local maximum \(z\), its neighboring path vertices are distinct from \(z\) and belong to \(\{z-2,z-1\}\). When they differ, they are adjacent in the graph, so the two incident edges, each of weight at least \(a\), may be replaced by one edge of weight at most \(2a\). When they coincide, the two-edge loop may be deleted. The same argument applies to a strict local minimum, using \(\{z+1,z+2\}\). Repeated shortcuts decrease the number of edges without raising cost. A path without strict internal extrema between endpoints \(0\) and \(n>0\) is strictly increasing. Thus the minimum over all full-graph paths equals the minimum over increasing paths contained in \(\{0,1,\ldots,n\}\), and exists.

The constant \(2\) cannot be increased universally. If \(b>2a\), assign weights \(a\) to edges \(\{0,2\}\) and \(\{1,2\}\), and weight \(b\) to every other edge. The unique increasing route from \(0\) to \(1\) has cost \(b\), whereas \(0\to2\to1\) has cost \(2a<b\). Therefore no increasing geodesic exists for this assignment.

**2. Exact finite-state recursion.** Write \(D_n=T_n\), \(D_0=0\), and \(D_1=\omega_{0,1}\). Step 1 gives, for every \(n\ge2\),

\[
D_n=\min\{D_{n-1}+\omega_{n-1,n},\ D_{n-2}+\omega_{n-2,n}\}.
\]

Set \(X_n=D_n-D_{n-1}\). The two edge weights arriving at vertex \(n\), denoted \(U_n,V_n\), are independent of all preceding pairs, so

\[
X_n=\min\{U_n,V_n-X_{n-1}\}.
\]

The increment is in the four-state set \(\{-1,0,1,2\}\). With states ordered \((-1,0,1,2)\), the transition matrix is

\[
P=\begin{pmatrix}
0&0&p&1-p\\
0&0&2p-p^2&(1-p)^2\\
0&p&1-p&0\\
p&1-p&0&0
\end{pmatrix}.
\]

For \(0<p<1\) the chain is irreducible and aperiodic, and its stationary law is

\[
\pi=\frac1{Z(p)}\bigl(p(1-p)^2,\ p^2-p+1,\ p^2-2p+2,\ (1-p)^2\bigr).
\]

All coordinates are strictly positive and sum to one. Taking the stationary mean of the increment vector \(f=(-1,0,1,2)^{\mathsf T}\) gives \(\mu(p)=\pi f\), which simplifies to the stated rational expression. The finite-state Markov strong law proves the almost-sure and \(L^2\) speed limits (the increments are bounded).

**3. Exact variance and central limit.** Let \(\mathbf1\) be the four-column vector of ones, \(g=f-\mu(p)\mathbf1\), and let \(h\) uniquely solve

\[
(I-P+\mathbf1\pi)h=g.
\]

The stationary Markov additive-functional variance is

\[
\sigma^2(p)=2\sum_i\pi_i g_i h_i-\sum_i\pi_i g_i^2.
\]

Exact rational elimination with the displayed \(P\) and \(\pi\) yields precisely \(p(1-p)H(p)/Z(p)^3\), as reproduced by `verify.py`. The standard finite-state Markov-chain Poisson-equation martingale decomposition gives the Gaussian central limit and the limiting normalized variance, from any initial law (including the law of \(X_1\)). Positivity is explicit: with \(r=1-p\),

\[
H(1-r)=1+9r^2-3r^3+22r^4-7r^5+14r^6>0\quad(0\le r\le1).
\]

Indeed, \(9r^2-3r^3\ge6r^2\) and \(22r^4-7r^5\ge15r^4\). This completes the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The script independently constructs the transition matrix from all four pairs of incoming edge weights, checks its row sums, verifies the stationary law, performs symbolic Poisson-equation elimination, verifies the exact drift and variance rational functions and the strict-positivity polynomial identity, and exhaustively compares the dynamic recursion against undirected Dijkstra shortest paths for all binary edge assignments on intervals with up to eight vertices. A successful run reports `PASS: 10962 exact symbolic or finite checks`.

The symbolic algebra is a finite exact certificate for the displayed polynomial identities. Exhaustive finite interval enumeration does not by itself establish the path shortcut for arbitrary graph size: that is proved in Step 1. The infinite-probability limits use standard theorems for finite irreducible aperiodic Markov chains and the bounded-increment additive functional.

## Relationship to prior work

Dey and Kim, *First-Passage Percolation on Spread-out line graphs: Microscopic Regime* (arXiv:2607.28865, first posted 2026-07-30), establish general LLN/CLT results for this exact underlying graph with general independent nonnegative passage weights, but state their constants through regenerative block expectations rather than the above rational functions. Their Section 5 explicitly discusses open geometric questions. The present result does **not** claim a new general CLT; it supplies explicit sharp constants for an important natural two-point law together with a deterministic monotone-geodesic boundary.

Ahlberg's 2011/2015 one-dimensional periodic-graph theory provides broad regeneration-based limit results but not the displayed constants. Flaxman, Gamarnik and Sorkin (2011) compute a rational Bernoulli time constant on a *different* width-two ladder graph, and Schlemm (2011) derives a Markov-chain variance method for exponential weights on that ladder. The graph studied here has four neighbours per interior vertex (the second power of the line), rather than the three neighbours in the square ladder, and the shortcut geometry permits the particular four-state reduction above. The rational-solvability technique is not claimed as new.

## Limitations

The exact formulas concern only i.i.d. binary weights \(1\) and \(2\) at fixed \(p\). The graph-level shortcut property requires all weights to lie within a factor of two; it is not asserted for general continuous weights or larger ratio. The general LLN and CLT, and finite-state Markov variance methods, are existing tools. Historical priority of these exact specialized rational functions has not been independently established, and a related ladder paper was accessible only through its abstract; the latter's different graph geometry excludes direct application of its stated formula but does not eliminate every possible equivalence. No claim is made about hop-count fluctuations or the exact finite-size distribution of passage time.

## References

1. P. S. Dey and D. Kim, *First-Passage Percolation on Spread-out line graphs: Microscopic Regime*, arXiv:2607.28865v2 (first public version 2026-07-30), https://arxiv.org/html/2607.28865.
2. D. Ahlberg, *Asymptotics of First-Passage Percolation on One-Dimensional Graphs*, arXiv:1107.2276; Advances in Applied Probability 47 (2015), 182–209, https://arxiv.org/abs/1107.2276.
3. A. Flaxman, D. Gamarnik and G. B. Sorkin, *First-passage percolation on a ladder graph, and the path cost in a VCG auction*, Random Structures & Algorithms 38 (2011), 350–364, https://doi.org/10.1002/rsa.20328.
4. E. Schlemm, *On the Markov transition kernels for first passage percolation on the ladder*, Journal of Applied Probability 48 (2011), 366–388, https://arxiv.org/abs/1201.4485.
