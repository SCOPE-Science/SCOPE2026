# Sharp six-vertex failure of likelihood-ratio domination in graph parking

## Finding

**Theorem (sharp order and infinite obstruction family).** Let \(G\) be a finite simple undirected graph. Let \(S_G\) count occupied vertices after uniform random sequential nearest-neighbor-exclusion parking, and let \(U_G\) be the cardinality of a maximal independent set chosen uniformly from all such sets. Write \(s_G(k)=\Pr(S_G=k)\) and \(u_G(k)=\Pr(U_G=k)\). For every graph on at most five vertices and all \(k<\ell\) in the common positive support,
\[
 s_G(k)u_G(\ell)\le s_G(\ell)u_G(k).
\]
This is the likelihood-ratio strengthening \(U_G\le_{\mathrm{lr}}S_G\), hence in particular \(U_G\le_{\mathrm{st}}S_G\).

The six-vertex bound is sharp, **even when first-order stochastic dominance remains valid**. Let
\[
 G_m=K_1\vee(K_2\sqcup K_{1,m}),\qquad m\in\mathbb Z,\ m\ge2,
\]
where \(\vee\) is graph join and \(\sqcup\) is disjoint union. Each \(G_m\) is connected and has \(m+4\) vertices. The static and sequential occupancy laws are supported on \(\{1,2,m+1\}\), with
\[
 \bigl(u_{G_m}(1),u_{G_m}(2),u_{G_m}(m+1)\bigr)
 =\left(\frac15,\frac25,\frac25\right),
\]
\[
 \bigl(s_{G_m}(1),s_{G_m}(2),s_{G_m}(m+1)\bigr)
 =\left(\frac1{m+4},\frac{m+3}{(m+4)(m+1)},
 \frac{m(m+3)}{(m+4)(m+1)}\right).
\]
For **every** \(m\ge2\), \(U_{G_m}\le_{\mathrm{st}}S_{G_m}\), but \(U_{G_m}\not\le_{\mathrm{lr}}S_{G_m}\), since
\[
 \frac{s_{G_m}(2)/u_{G_m}(2)}{s_{G_m}(1)/u_{G_m}(1)}
 =\frac{m+3}{2(m+1)}<1.
\]
Thus six vertices is the smallest possible number for failure of the proposed likelihood-ratio ordering, among **all** finite simple graphs (not only connected graphs).

## Assumptions and scope

Graphs are finite, simple, undirected and labeled; isolated vertices and disconnected graphs are allowed in the universal five-vertex assertion. The sequential parking rule repeatedly picks one currently available vertex uniformly, retains it, and removes it and its neighbors from availability; this is equivalent to scanning all vertices in a uniformly random permutation and retaining a vertex if none of its retained neighbors is adjacent to it. The static model samples **uniformly among inclusion-maximal independent sets**, not maximum-size independent sets or all independent sets. Every maximal independent set has positive probability under sequential parking: expose all its vertices before all remaining vertices. Consequently the positive supports coincide, and likelihood-ratio inequalities are meaningful at each pair of support values.

Here \(X\le_{\mathrm{lr}}Y\) means \(\Pr(Y=k)/\Pr(X=k)\) is nondecreasing on their common positive support. Such an ordering implies ordinary first-order stochastic domination, but not conversely. The claim does not address arbitrary larger graphs, arbitrary site weights, or arbitrary random-deposition rules.

## Proof

**1. Exact finite recursion and complete small-order census.** For an induced graph on nonempty available vertex set \(A\), the sequential occupancy-size distribution satisfies
\[
 s_A(k)=\frac1{|A|}\sum_{v\in A}s_{A\setminus N[v]}(k-1),
 \qquad s_\varnothing(0)=1,
\]
where \(N[v]\) denotes the closed neighborhood within the ambient graph. This follows by conditioning on the first uniformly chosen available vertex; every following choice is independent and uniform among the remaining available vertices.

For each subset \(I\subseteq V(G)\), it is an inclusion-maximal independent set precisely when (i) no edge has both ends in \(I\), and (ii) \(I\cup\bigcup_{v\in I}N(v)=V(G)\). Thus \(u_G(k)\) is the number of such subsets of size \(k\), divided by their total number. Both descriptions use only integer subsets, finite sums, and exact rational arithmetic.

The accompanying self-contained `checker.py` enumerates **every** labeled simple graph for \(1\le n\le5\) by ranging over every one of the \(2^{\binom n2}\) edge masks. The respective graph counts are \(1,2,8,64,1024\), totaling \(1099\). For each graph, the program constructs the static counts by the two exact subset predicates and the sequential probabilities by the displayed recursion, then checks all neighboring positive-support likelihood-ratio cross-products using exact `Fraction` arithmetic. Every one of the \(772\) cross-product checks passes. To independently check the recursive distribution, the program also scans **all \(n!\) vertex permutations for each graph** and confirms equality of the two exact laws on all \(1099\) inputs. These loops are exhaustive because a simple labeled graph is uniquely determined by the binary choices for its unordered vertex pairs, and every possible sequential arrival order appears once in the permutation enumeration. The finite census is therefore a complete finite proof of the universal assertion; it is not extrapolation from random examples.

**2. Law on the family.** For \(G_m\), call the unique universal vertex \(h\); the remaining vertices form an isolated edge and a star with \(m\) leaves. The maximal independent sets are \(\{h\}\), either endpoint of the edge together with the star center, and either endpoint of the edge together with **all** \(m\) star leaves. Their sizes are respectively \(1,2,m+1\), with multiplicities \(1,2,2\). This gives the static probabilities.

For sequential parking, \(h\) is first with probability \(1/(m+4)\), producing size one. Otherwise \(h\) is immediately blocked. The edge then always contributes exactly one retained vertex; the star contributes its center alone if its center has the earliest priority within the star (probability \(1/(m+1)\)) and otherwise contributes all \(m\) leaves. Independent uniform priorities restricted to the star remain uniformly ordered after conditioning that \(h\) is not the first global vertex: by symmetry (or the independent exponential-key representation) the within-star rank order is uniform under this conditioning. This yields the stated sequential probabilities.

**3. Separating the two stochastic orders.** The sequential-to-static size ratios, in increasing support order, equal
\[
 r_1=\frac5{m+4},\quad
 r_2=\frac{5(m+3)}{2(m+4)(m+1)},\quad
 r_{m+1}=\frac{5m(m+3)}{2(m+4)(m+1)}.
\]
They satisfy \(r_2/r_1=(m+3)/(2(m+1))<1\) and \(r_{m+1}/r_2=m>1\), so they are **not** nondecreasing. Yet at the only nontrivial CDF thresholds,
\[
 \Pr(S_{G_m}\le1)=\frac1{m+4}\le\frac15=\Pr(U_{G_m}\le1),
\]
\[
 \Pr(S_{G_m}\le2)=\frac{2(m+2)}{(m+4)(m+1)}
 \le\frac35=\Pr(U_{G_m}\le2),
\]
where the latter inequality is equivalent to \(3m^2+5m-8\ge0\) for \(m\ge2\). All remaining thresholds are trivial. This proves first-order domination throughout the family and proves the six-vertex boundary at \(m=2\). In that first example, the sequential and static mass vectors are exactly \((1/6,5/18,5/9)\) and \((1/5,2/5,2/5)\), respectively. \(\square\)

## Verification

From this directory run `python3 checker.py` under Python 3.10 or newer; no third-party modules, network access, or random seeds are required. It prints the exhaustive labeled-graph counts, verifies all \(772\) likelihood-ratio cross-product inequalities and \(1099\) independently enumerated permutation distributions, and confirms the six-vertex witness and fourteen additional exact family instances. The infinite family is proved by the explicit combinatorial argument above, **not** inferred from fourteen cases. The program's full source is included here, so the finite exhaustion is inspectable and reproducible.

## Relationship to prior work

Higuita-Diaz, López and Roldán-Correa (2026), *Stochastic Dominance in Discrete Parking Processes on Graphs*, establishes first-order sequential-over-static domination for paths and cycles, studies small connected graphs and counterexamples, and uses an **auxiliary-to-static likelihood-ratio comparison** in its path proof. That comparison is between a specially defined auxiliary model and the static model, not the sequential-to-static cardinality laws examined here. The present result identifies the sharp obstruction to upgrading the comparison between those two original occupancy laws: first-order domination holds on the explicit infinite family even though likelihood-ratio domination fails.

Krivelevich, Mészáros, Michaeli and Shikhelman (2019/2023) study random greedy maximal independent sets and their densities; the random-priority mechanism and first-vertex recursion are classical. Related published work on exact uniformity of greedy outputs on cycles concerns probabilities of **individual maximal sets**, not likelihood-ratio ordering of the **two cardinality laws**. Related finite work confirms likelihood-ratio domination on connected graphs of maximum degree at most three through ten vertices; it does not cover the present family, whose first witness has maximum degree five, and it does not assert a global sharp boundary across all graphs. The novelty claim is limited to the combined sharp threshold and explicit first-order-but-not-likelihood-ratio family, not these prior tools.

## Limitations

This does not assert likelihood-ratio ordering on every graph with six or more vertices, nor characterize all witnesses, nor settle the conjectured subcubic first-order domination for arbitrary orders. The universal lower bound through five vertices relies on a transparent exact finite exhaustion rather than a short hand classification; all infinite-parameter statements follow analytically. Relevant publication coverage was checked but historical priority remains subject to independent verification. No independent mathematical audit has been performed.

## References

1. R. Higuita-Diaz, L. López and A. Roldán-Correa, *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1, first public 2026-11-10. https://arxiv.org/abs/2611.14718
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216v6 (2023; first posted 2019). https://arxiv.org/abs/1907.07216
3. *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles* (2026), publicly accessible mathematical finding; its pointwise terminal-set statement is not a cardinality likelihood-ratio comparison.
4. *Likelihood-ratio domination through ten vertices in subcubic parking graphs* (2026), publicly accessible mathematical finding; its degree-three scope is distinct from the present universal sharp counterexample.
