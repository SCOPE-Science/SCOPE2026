# Cycle-decorated trees permit positive ant-walk escape without infinite leaves

## Finding

Consider the exponentially directed-edge-reinforced random walk (the Ant RW) of Erhard, Franco and Reis, with any reinforcement parameter \(\beta>0\). There is a connected, infinite, locally finite graph in which **every vertex belongs to a finite cycle**, but the walk started at a specified vertex has strictly positive probability to escape to infinity without ever traversing an edge of a cycle.

More precisely, fix any sequence of positive integers \((b_i)_{i\ge0}\). Form the rooted tree with \(b_i\) children at every level-\(i\) vertex. At every tree vertex attach a private simple cycle of arbitrary length at least three, identifying that vertex with exactly one vertex of its cycle. All other cycle vertices have no outside edges. Denote the resulting graph by \(G\), with root \(o\). The cycle lengths may vary arbitrarily from vertex to vertex.

Let \(E\) be the event that the walk, from its first step onward, always moves from its current tree vertex to one of its children along a tree edge. Then, for every \(\beta>0\),

\[
\mathbb P_{o,\beta}(E)
=\frac{b_0}{b_0+2}
\prod_{i=1}^{\infty}\frac{b_i}{b_i+2+e^{-\beta}},
\qquad
\mathbb P_{o,\beta}(E)>0
\iff\sum_{i=1}^{\infty}\frac1{b_i}<\infty.
\]

This exact probability is **independent of all attached cycle lengths**. In particular, taking \(b_i=2^{i+2}\) and making every attached cycle a triangle gives

\[
\mathbb P_{o,\beta}\!\left(\lim_{n\to\infty}d_G(X_n,o)=\infty\right)
\ge\mathbb P_{o,\beta}(E)
\ge \frac23e^{-3/4}>0.3148
\quad\text{for every }\beta>0.
\]

The equivalence involving the reciprocal branching sum describes **only the strictly monotone outward event \(E\)**; it is not a criterion for escape of arbitrary walk trajectories.

## Assumptions and scope

The underlying graph is simple and undirected, with all degrees finite, although the degrees need not be uniformly bounded. For every tree vertex \(v\), attach a simple cycle of length \(\ell(v)\ge3\), and make the new cycle vertices adjacent only to their two cycle neighbors. Thus each original tree vertex has exactly two cycle neighbors. Every vertex lies on one of these cycles, so the graph has no hanging infinite half-line of vertices outside all cycles (the 'infinite leaf' construction in the motivating paper). The tree is infinite because every \(b_i\ge1\).

The Ant RW starts at the root \(o\) with every directed crossing number initially zero. Given the trajectory \((X_j)_{0\le j\le n}\), define

\[
c_n(x,y)=\sum_{j=0}^{n-1}\!\left(
\mathbf1_{\{X_j=x,\ X_{j+1}=y\}}
-\mathbf1_{\{X_j=y,\ X_{j+1}=x\}}
\right).
\]

Its next transition to a neighbor \(y\) of \(x=X_n\) has conditional probability

\[
\mathbb P(X_{n+1}=y\mid X_0,\ldots,X_n)
=\frac{e^{\beta c_n(x,y)}}{\sum_{z\sim x}e^{\beta c_n(x,z)}}.
\]

All probability statements concern this single-particle process on this fixed deterministic graph. The attached cycles are part of the graph, not random obstacles.

## Proof

**1. The graph has the stated structure.** Every original tree vertex is in its private cycle and has degree \(b_i+3\) if it is not the root, or \(b_0+2\) at the root. Every newly added cycle vertex has degree two and belongs to that cycle. Hence the graph is locally finite, connected and infinite, and every vertex lies on a simple finite cycle. Distinct attached cycles meet the original tree only at their own gate vertices; in particular, a cycle cannot provide a shortcut between two distinct tree vertices.

**2. Conditional outward-step probability.** Assume the walk has followed \(E\) for its first \(i\) steps. It is then at a previously unvisited level-\(i\) tree vertex. For \(i=0\), its \(b_0\) child edges and its two cycle edges all have crossing number zero. The probability that the next edge is one of the child edges is \(b_0/(b_0+2)\).

For \(i\ge1\), the edge back to the parent was just crossed from parent to child, so its crossing number in the reverse direction is precisely \(-1\), giving weight \(e^{-\beta}\). Each of the \(b_i\) child edges is still unused, as are the two incident cycle edges; they all have weight one. Therefore the conditional probability of another outward step is exactly \(b_i/(b_i+2+e^{-\beta})\). It depends only on the level, not on which branch was chosen or on the cycle lengths.

**3. Infinite product.** Let \(E_m\) denote the event of taking only child-tree edges in the first \(m\) steps. Multiplying the conditional probabilities yields, for \(m\ge1\),

\[
\mathbb P(E_m)=\frac{b_0}{b_0+2}
\prod_{i=1}^{m-1}\frac{b_i}{b_i+2+e^{-\beta}}.
\]

Since \(E_{m+1}\subseteq E_m\) and \(E=\bigcap_{m\ge1}E_m\), continuity of probability from above gives the displayed infinite product. Put \(a=2+e^{-\beta}\in(2,3)\). For each positive integer \(b\),

\[
\frac{a}{(1+a)b}
\le \log\!\left(1+\frac{a}{b}\right)
\le\frac{a}{b}.
\]

Indeed, \(x/(1+x)\le\log(1+x)\le x\) for \(x>0\), and \(b\ge1\). Consequently the sum of negative logarithms of the nonroot factors converges if and only if \(\sum_{i\ge1}b_i^{-1}\) converges, proving the exact positivity criterion.

**4. Constructive uniform bound and escape.** Choose \(b_i=2^{i+2}\). Then \(b_0/(b_0+2)=2/3\), and \(\sum_{i=1}^\infty b_i^{-1}=1/4\). Applying \(\log(1+x)\le x\) and \(a<3\),

\[
\mathbb P(E)=\frac23\exp\!\left[-\sum_{i=1}^\infty
\log\!\left(1+\frac{a}{b_i}\right)\right]
\ge\frac23\exp\!\left(-3\sum_{i=1}^\infty\frac1{b_i}\right)
=\frac23e^{-3/4}.
\]

On \(E\), the walk's position after \(m\) steps is at tree depth \(m\); the private cycles cannot shorten the root-to-vertex path. Hence \(d_G(X_m,o)=m\to\infty\) on \(E\). No cycle edge is traversed, so the walker never becomes trapped in a directed circuit there. This completes the proof.

## Verification

The standalone script `verify.py` independently constructs finite truncated trees of cycle blocks, explicitly computes signed crossing numbers and all transition weights along every monotone outward path, and sums the rational probabilities over all such paths. It checks varying branch vectors and both constant and variable cycle lengths. At exactly rational reverse weights, the finite answers agree with the product identity. It reports **10,942 finite exact-rational comparisons** and **117 high-precision inequalities** against the analytic uniform lower bound. Reproduce with `python3 verify.py` using the Python standard library; no downloaded data or external modules are required.

These finite checks do not establish the infinite product or the iff criterion, which are supplied by the mathematical argument above.

## Relationship to prior work

Erhard, Franco and Reis [1] define precisely this signed-crossing, exponentially reinforced single-ant model. Their Theorem 2.2 proves eventual directed-circuit trapping for finite non-tree graphs and for \(\mathbb Z^d\) with \(d\ge2\). Section 2.2 identifies a triangle attached to an infinite leaf as an escape example and explicitly suggests, without proving, that an infinite tree of circuits with rapidly growing branching and cycle lengths might allow escape **without** an infinite leaf. Their figure caption describes that possible phenomenon as conjectural. The present theorem supplies a rigorous affirmative example, an exact monotone-event probability, a sharp reciprocal-branching criterion for that event, and the additional observation that cycle lengths need not grow at all.

Erhard and Reis [2] investigate competing reinforcements and multiple walkers, rather than this single-walker escape event on a tree of privately attached cycles. The theorem does **not** settle the general almost-sure trapping-or-escape dichotomy (Conjecture 2.3 of [1]); it only constructs a positive-probability escaping trajectory in an explicit infinite family.

## Limitations

The theorem permits unbounded vertex degrees, relies on private cycles meeting the base tree at one gate, and gives an exact probability for the particular strictly monotone event \(E\), not the full escape probability. The 'only if' direction for \(\mathbb P(E)>0\) does not rule out escape with backtracking when \(\sum b_i^{-1}=\infty\). It does not establish a positive escape probability for uniformly bounded-degree cyclic graphs or resolve the general dichotomy of [1]. Its historical originality has not been independently certified.

## References

[1] D. Erhard, T. Franco, and G. Reis, *The Directed Edge Reinforced Random Walk: The Ant Mill Phenomenon*, first public preprint 17 November 2019, arXiv:1911.07295; *Journal of Statistical Physics* 190, article 18 (2023), DOI:10.1007/s10955-022-03031-0. Preprint: https://arxiv.org/abs/1911.07295 . Open-access full text: https://link.springer.com/article/10.1007/s10955-022-03031-0 .

[2] D. Erhard and G. Reis, *Stochastic Processes with Competing Reinforcements*, arXiv:2105.00880 (first public preprint 3 May 2021), *Annals of Applied Probability* 34 (2024), 4513–4553, DOI:10.1214/24-AAP2073.
