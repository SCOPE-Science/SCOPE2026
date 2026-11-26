# Anti-forcing distribution of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_0\), with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(M_0=\{a_i b_i:1\le i\le n\}\). Every perfect matching is uniquely
\[
M_\pi=\{a_i b_{\pi(i)}:1\le i\le n\}
\]
for a derangement \(\pi\in S_n\). If \(c(\pi)\) denotes the number of cycles in the disjoint-cycle decomposition of \(\pi\), then
\[
af(\operatorname{Cr}_n,M_\pi)=\frac{n(n-3)}2+c(\pi).
\]
Therefore the complete size distribution of anti-forcing numbers is
\[
\mathcal A_n(x)=\sum_{M}x^{af(\operatorname{Cr}_n,M)}=x^{n(n-3)/2}D_n(x),
\]
where
\[
D_n(t)=\sum_{\substack{\pi\in S_n\\\pi(i)\ne i\ \forall i}}t^{c(\pi)}
\]
is the derangement cycle enumerator. It satisfies
\[
D_0(t)=1,\qquad D_1(t)=0,\qquad D_n(t)=(n-1)\bigl(D_{n-1}(t)+tD_{n-2}(t)\bigr),
\]
and equivalently
\[
\sum_{n\ge0}D_n(t)\frac{z^n}{n!}=e^{-tz}(1-z)^{-t}.
\]
The spectrum is exactly
\[
\operatorname{Spec}_{af}(\operatorname{Cr}_n)=\left\{\frac{n(n-3)}2+k:1\le k\le\left\lfloor\frac n2\right\rfloor}\right\}.
\]
In particular,
\[
af(\operatorname{Cr}_n)=\frac{n(n-3)}2+1,
\qquad
Af(\operatorname{Cr}_n)=\frac{n(n-3)}2+\left\lfloor\frac n2\right\rfloor.
\]
The minimum is attained by exactly \((n-1)!\) perfect matchings. If \(n=2m\), the maximum is attained by exactly \(n!/(2^m m!)\) perfect matchings; if \(n=2m+1\), the number is \(n!/(3\,2^{m-1}(m-1)!)\).

## Assumptions and scope
The graph is finite, simple, and \(n\ge3\). The anti-forcing number \(af(G,M)\) of a perfect matching \(M\) is the minimum number of edges outside \(M\) whose deletion leaves \(M\) as the unique perfect matching. The result classifies every perfect matching of the crown graph, not only extremal matchings. The result does not assert an analogous formula for arbitrary matching-deleted bipartite graphs.

## Proof
A perfect matching of \(\operatorname{Cr}_n\) chooses one neighbor of each \(a_i\), so it is represented by a permutation \(\pi\in S_n\). Since \(a_i b_i\) is absent, the matching is valid exactly when \(\pi(i)\ne i\) for all \(i\), hence exactly when \(\pi\) is a derangement.

Fix \(M_\pi\). Orient every edge outside \(M_\pi\) from the \(A\)-side to the \(B\)-side, orient each matching edge oppositely, and contract every edge of \(M_\pi\). The standard anti-forcing reduction identifies anti-forcing sets with feedback arc sets of the contracted digraph. Label the contracted vertex containing \(a_i\) by \(i\), and put \(\sigma=\pi^{-1}\). An arc \(i\to j\) is present exactly when \(i\ne j\) and \(j\ne\sigma(i)\). Thus the contracted digraph is the complete bidirected graph on \(n\) vertices with the \(n\) arcs \(i\to\sigma(i)\) removed. It has \(n(n-2)\) arcs.

For any finite digraph, the largest acyclic spanning subgraph has the largest number of forward arcs over all linear orders of the vertices: every acyclic subgraph has a topological order, and for a fixed order one may include every existing forward arc without creating a directed cycle. In a chosen order there are \(\binom n2\) possible forward ordered pairs. Let \(q\) be the number of deleted arcs \(i\to\sigma(i)\) that point forward. Then the number of present forward arcs is \(\binom n2-q\).

The deleted arcs form the directed cycle cover determined by \(\sigma\). Every directed cycle has at least one forward arc in any linear order, because making every arc backward would force a cyclic chain of strict inequalities. Hence \(q\ge c(\sigma)=c(\pi)\). Conversely, within each cycle of \(\sigma\), list its vertices in reverse cyclic order; exactly one deleted arc of that cycle then points forward. Concatenate these cycle blocks arbitrarily. This realizes \(q=c(\pi)\). Therefore the largest acyclic spanning subgraph has
\[
\binom n2-c(\pi)
\]
arcs, so a minimum feedback arc set has
\[
n(n-2)-\left(\binom n2-c(\pi)\right)=\frac{n(n-3)}2+c(\pi)
\]
arcs, proving the formula.

The distribution follows by summing over derangements according to cycle count. The recurrence for \(D_n(t)\) follows by considering the cycle containing \(n\): either insert \(n\) immediately after one of the \(n-1\) elements of a derangement of \([n-1]\), preserving the number of cycles, or form a transposition containing \(n\) and one chosen partner and use a derangement on the remaining \(n-2\) elements, increasing the cycle count by one. The exponential generating function follows from the labelled-cycle construction with allowed cycle lengths at least two.

A derangement can have any number \(k\) of cycles with \(1\le k\le\lfloor n/2\rfloor\): take \(k-1\) transpositions and one cycle of length \(n-2(k-1)\). The minimum cycle count is one, realized by the \((n-1)!\) \(n\)-cycles. The maximum cycle count is \(\lfloor n/2\rfloor\); for even \(n=2m\) it consists entirely of transpositions, while for odd \(n=2m+1\) it consists of one 3-cycle and \(m-1\) transpositions. The stated extremal counts are the standard counts of those cycle types.

## Verification
The standalone verifier `verify_anti_forcing_crown.py` performs three independent finite stress tests. First, for every derangement through \(n=6\), it builds the contracted digraph and computes the exact minimum feedback-arc-set size by maximizing forward arcs over every vertex order. Second, through \(n=5\), it directly searches subsets of edges outside the chosen perfect matching and checks when all competing perfect matchings are destroyed. Third, through \(n=9\), it enumerates derangements, checks the cycle-count recurrence, checks every spectrum value, and checks both extremal multiplicity formulas. The replay output is:

`VERIFY_OK order_checks=320 direct_checks=55 distribution_checks=7 spectrum_checks=7 extremal_checks=14 max_order=18`

These finite computations test the proof but are not used as a substitute for the universal argument.

## Relationship to prior work
Lei, Yeh, and Zhang introduced the anti-forcing number of an individual perfect matching and proved that deleting nonmatching edges to hit all alternating cycles is equivalent, after orienting and contracting the matching, to deleting a feedback arc set. That general reduction is the starting point here. Their paper does not mention crown graphs, complete bipartite graphs minus a perfect matching, or derangements in its searchable full text.

Deng and Zhang developed anti-forcing spectra and extremal anti-forcing theory, including a general cyclomatic upper bound and exact spectra for even polygonal chains. Their searchable full text contains no crown-graph or complete-bipartite specialization. The present result instead solves the contracted feedback-arc problem exactly for the dense digraph obtained by deleting a permutation cycle cover from a complete bidirected graph, yielding the entire distribution rather than only a scalar extremum.

Later work gives sharp maximum anti-forcing bounds for broad graph classes and examples such as \(K_{n,n}\), but those results do not identify the distribution for \(K_{n,n}\) with one fixed 1-factor deleted. The crown graph is also known as \(K_{n,n}\) minus a perfect matching and as the bipartite Kneser graph \(H(n,1)\); searches under these aliases were included in the comparison.

## Limitations
The originality search found no source stating the crown-graph formula or its derangement-cycle distribution, but absence from searched indexes is not a proof that no equivalent result exists. A residual risk is an unindexed treatment under a matching-theoretic alias such as complete bipartite graph minus a 1-factor. The proof depends on the standard anti-forcing-to-feedback-set equivalence, while the crown-specific feedback-set computation and distribution are derived explicitly here. The computational verification is finite and does not certify cases beyond its stated range.

## References
1. H. Lei, Y.-N. Yeh, and H. Zhang, “Anti-forcing numbers of perfect matchings of graphs,” arXiv:1406.3796v1, 2014; journal DOI 10.1016/j.dam.2015.08.024.
2. K. Deng and H. Zhang, “Extremal anti-forcing numbers of perfect matchings of graphs,” arXiv:1607.05392v1, 2016; journal DOI 10.1016/j.dam.2017.02.024.
3. L. Shi and H. Zhang, “Tight upper bound on the maximum anti-forcing numbers of graphs,” Discrete Mathematics & Theoretical Computer Science 19(3), 2017, DOI 10.23638/DMTCS-19-3-9.
