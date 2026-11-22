# Anti-forcing numbers of crown-graph matchings are determined by their derangement cycle counts

## Finding
For every integer \(n\ge 3\), let the *crown graph* be
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:i\in[n]\}.
\]
Its perfect matchings are \(M_\pi=\{a_i b_{\pi(i)}:i\in[n]\}\), indexed by derangements \(\pi\in S_n\). Let \(c(\pi)\) count the cycles in the disjoint-cycle decomposition of \(\pi\), and let \(\operatorname{af}(G,M)\) denote the smallest number of edges *outside* \(M\) whose deletion makes \(M\) the unique perfect matching. Then
\[
\boxed{\operatorname{af}(\operatorname{Cr}_n,M_\pi)
=\frac{n(n-3)}{2}+c(\pi).}
\]
Every optimum anti-forcing deletion set is obtained from a linear ordering of the matched pairs having exactly one forward *forbidden arc* within each cycle of \(\pi\): retain all available forward arcs between pairs and delete all available backward arcs. Different orders may describe the same deletion set.

The complete anti-forcing polynomial, counting *matchings* rather than deletion witnesses, is
\[
\boxed{A_n(z)=\sum_{\pi\ \mathrm{derangement}}z^{\operatorname{af}(\operatorname{Cr}_n,M_\pi)}
=z^{n(n-3)/2}\,n!\,[u^n]\exp\!\left(z\sum_{\ell\ge2}\frac{u^\ell}{\ell}\right)
=z^{n(n-3)/2}\,n!\,[u^n]e^{-zu}(1-u)^{-z}.}
\]
If \(d_{n,k}\) is the number of derangements of \([n]\) with exactly \(k\) cycles, the coefficient of \(z^{n(n-3)/2+k}\) is \(d_{n,k}\). These counts satisfy the entirely integer recurrence
\[
 d_{n,k}=(n-1)(d_{n-1,k}+d_{n-2,k-1}),\qquad
 d_{0,0}=1,
\]
with all inadmissible indices and \(d_{1,k}\) set to zero. In particular, the possible anti-forcing numbers form the uninterrupted interval
\[
\left\{\frac{n(n-3)}2+1,\ldots,\frac{n(n-3)}2+\left\lfloor\frac n2\right\rfloor\right\}.
\]
The minimum occurs on the \((n-1)!\) cyclic derangements. If \(n=2m\), the maximum occurs on exactly \(n!/(2^m m!)\) products of transpositions; if \(n=2m+1\), on exactly \(n!/(3\cdot2^{m-1}(m-1)!)\) derangements consisting of one triangle and \(m-1\) transpositions.

## Assumptions and scope
All graphs are finite, simple, undirected. The two bipartition classes of \(\operatorname{Cr}_n\) each have the fixed labels \([n]\). An anti-forcing set for \(M\) is a subset of \(E(G)\setminus M\) whose deletion preserves \(M\) but destroys all competing perfect matchings. It is the *minimum number of such deleted edges* that is counted in \(A_n(z)\). This is distinct from (i) a forcing subset lying inside \(M\), and (ii) a complete forcing subset working simultaneously for every matching.

The theorem concerns \(n\ge3\). For comparison the disconnected \(n=2\) crown consists of two isolated matching edges and has anti-forcing number zero, but is not part of the asserted range. All polynomial coefficients count labelled perfect matchings, not anti-forcing witnesses or graph-isomorphism types.

## Proof
**1. Contract the fixed matching to a directed graph.** Fix \(\pi\). Contract each edge \(a_i b_{\pi(i)}\) of \(M_\pi\) to a symbol \(i\). Encode an original nonmatching edge \(a_i b_{\pi(j)}\) as the directed arc \(i\to j\). It is available exactly when \(i\ne j\) (so it is not a matched edge) and \(i\ne\pi(j)\) (so it is not one of the deleted-diagonal edges). Thus the directed auxiliary graph consists of all \(n(n-1)\) loopless arcs except the \(n\) arcs
\[
\pi(j)\to j\quad(j\in[n]).
\]
These absent arcs form a directed cycle cover, with precisely \(c(\pi)\) cycles, of lengths at least two. The number of *available nonmatching edges* is \(n(n-2)\).

**2. Translate uniqueness into acyclicity.** A directed cycle of available arcs \(i_1\to i_2\to\cdots\to i_t\to i_1\) gives an alternating cycle of original edges relative to \(M_\pi\), and replacing its matched edges produces a second perfect matching. Conversely, the symmetric difference of \(M_\pi\) with any other perfect matching contains an alternating cycle, whose nonmatching edges encode a directed cycle. Therefore a set of deleted nonmatching edges isolates \(M_\pi\) if and only if the directed graph of surviving available arcs is acyclic.

**3. Exact largest acyclic subset.** Every finite acyclic digraph has a topological ordering of its \(n\) vertices; all surviving arcs are forward in that order. For any linear order, among the \(\binom n2\) possible forward arcs of the complete loopless digraph, at least one belongs to the absent-arc cycle cover in *each* of its \(c(\pi)\) cycles: a cyclic sequence of inequalities cannot make every arc point backward. Hence every acyclic subgraph has at most
\[
\binom n2-c(\pi)
\]
available arcs.

For each absent-arc directed cycle, list its vertices in reverse cyclic order (with an arbitrary choice of starting point). Exactly one arc from that cycle then points forward, and all its other absent arcs point backward. Concatenate these chosen orders over the disjoint cycles. The resulting order has exactly \(c(\pi)\) forward absent arcs in total. Retaining *every available forward arc* is acyclic and has exactly \(\binom n2-c(\pi)\) arcs. This proves the upper bound is sharp, independent of all cycle lengths.

The anti-forcing number therefore equals the total available nonmatching edges minus the largest number retained:
\[
 n(n-2)-\left(\binom n2-c(\pi)\right)
=\frac{n(n-3)}2+c(\pi).
\]
If a deletion set is minimum, the surviving directed graph is acyclic of maximum size. Pick any topological ordering. Since it already has the largest feasible number of arcs, it must retain *all* available forward arcs for that order, and the order must have exactly one forward absent arc in each absent cycle. This proves the characterization of every minimum deletion set. Conversely, any order with the stated property gives a minimum set by deleting its backward available arcs.

**4. Enumerate perfect matchings by cycle count.** A perfect matching must avoid all diagonal edges, hence is exactly a derangement of \([n]\). The standard labelled permutation cycle construction with cycle lengths at least two gives
\[
\sum_{n,k\ge0}d_{n,k}z^k\frac{u^n}{n!}
=\exp\!\left(z\sum_{\ell\ge2}\frac{u^\ell}{\ell}\right)=e^{-zu}(1-u)^{-z}.
\]
Multiplying by the established fixed-matching weight proves the formula for \(A_n(z)\). To obtain the recurrence directly, insert the largest symbol either into one of the \(n-1\) positions on an existing permutation cycle or pair it as a new transposition with one of the \(n-1\) other symbols, leaving a derangement of \(n-2\) symbols. This gives the recurrence above. All \(1\le k\le\lfloor n/2\rfloor\) are feasible: partition \([n]\) into \(k-1\) two-cycles and one remaining cycle of length \(n-2(k-1)\ge2\). The extreme counts follow from counting a single \(n\)-cycle, all transpositions, or one three-cycle and all remaining transpositions, respectively.

## Verification
The standalone standard-library file `checker.py` constructs derangements and the contracted arc sets independently. For *every* derangement at orders \(3,4,5,6\), it searches all \(n!\) linear orders to determine the true minimum number of backward available arcs, and compares this with the cycle-count formula. For *every* derangement at orders \(3\) and \(4\), it also independently searches deletion subsets and checks their ability to hit every other perfect matching, without employing the digraph argument. At order \(7\), it verifies the count distribution over all derangements but does not independently optimize, so order-seven counts alone are not a proof of the optimum.

Run `python3 checker.py`. The recorded output is:
```
3 2 [(1, 2)] passed True
4 9 [(3, 6), (4, 3)] passed True
5 44 [(6, 24), (7, 20)] passed True
6 265 [(10, 120), (11, 130), (12, 15)] passed True
7 1854 [(15, 720), (16, 924), (17, 210)] passed True
VERIFY_OK
```
These finite tests are checks of the argument and implementation. They do not establish the infinite statement; the four proof steps do so.

## Relationship to prior work
The anti-forcing number for a fixed perfect matching is a standard invariant. Zhang and Zhang, arXiv:2009.05746v1 (first public 2020-09-12), study global forcing numbers and maximum anti-forcing bounds for bipartite graphs. In their full arXiv manuscript, Theorems 3.5--3.6 and Proposition 3.9 concern broad inequalities, the complete biclique, and a biclique with *one edge* deleted. These results neither supply the fixed-derangement cycle law nor the crown-graph anti-forcing polynomial.

Two close crown-graph enumerations address mathematically different edge-set predicates. “All forcing subsets of perfect matchings in crown graphs” (published-finding corpus record dated 2026-10-12) proves a fixed-matching **forcing** polynomial \(x^n+nx^{n-1}+(n-t_2(\pi))x^{n-2}\) using edges *inside* a matching. “The complete-forcing polynomial of crown graphs” (published-finding corpus record dated 2026-10-12) counts sets forcing *every* matching at once. Their full publicly available `RESULT.md` texts have been read. Neither theorem determines the number of deletions *outside a selected matching* needed to isolate it; in particular, the new invariant depends on the **total** cycle count rather than just the transposition count.

The result also differs from anti-forcing polynomials for polyomino and pyrene systems, whose underlying graphs are not crowns. The classical formula for deleting all backward arcs of a directed graph motivates the proof but does not already supply the crown-specific missing-cycle optimum or its associated-Stirling distribution without the present specialization.

## Limitations
The exact formula is for crowns (complete bipartite graphs with an entire perfect matching deleted), not arbitrary matching-deleted bipartite graphs. It counts perfect matchings by their minimum *anti-forcing number*, not how many different minimum deletion sets each matching admits. No claim is made that the result solves anti-forcing for all regular bipartite graphs. Index searches and inspected related primary works did not reveal the formula, but unindexed or unavailable literature could still establish overlap. Independent mathematical validation has not been performed.

## References
1. Y. Zhang and H. Zhang, “Relations between global forcing number and maximum anti-forcing number of a graph,” arXiv:2009.05746v1, publicly posted 2020-09-12, https://arxiv.org/abs/2009.05746.
2. K. Deng, S. Liu and X. Zhou, “Forcing and anti-forcing polynomials of perfect matchings of a pyrene system,” arXiv:2004.05112v1, publicly posted 2020-04-10, https://arxiv.org/abs/2004.05112.
3. “All forcing subsets of perfect matchings in crown graphs,” published-finding corpus public repository, record dated 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-all-forcing-subsets-of-perfect-matchings-in-crown-graphs--2c97788f0907.
4. “The complete-forcing polynomial of crown graphs,” published-finding corpus public repository, record dated 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-complete-forcing-polynomial-of-crown-graphs--1d11197e01f2.
