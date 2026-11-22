# Eulerian-number census of shortest odd cycles in token graphs

## Finding

Let \(G\) be a finite simple graph on \(n\ge3\) vertices, let \(1\le k\le n-1\), and write \(F_k(G)\) for its graph of unordered configurations of \(k\) indistinguishable tokens. Suppose \(G\) has finite odd girth \(g\), with \(c_g(G)\) unoriented simple cycles of length \(g\). Then \(F_k(G)\) also has odd girth \(g\), and its number of shortest odd cycles is

\[
 c_g(F_k(G))=c_g(G)\sum_{h=1}^{g-1}\binom{n-g}{k-h}\left\langle {g-1\atop h-1}\right\rangle.
\]

Here \(\left\langle{m\atop j}\right\rangle\) is the Eulerian number: the number of permutations of \(m\) labels with exactly \(j\) descents. Set \(\binom ab=0\) outside \(0\le b\le a\). Every shortest odd token cycle has a unique supporting shortest odd cycle of the underlying graph; all its moves project bijectively onto the edges of that base cycle. If \(G\) is bipartite, then \(F_k(G)\) is bipartite.

For the odd base cycle \(C_g\) itself, the formula becomes \(c_g(F_k(C_g))=\left\langle{g-1\atop k-1}\right\rangle\). For example, when \(g=7\), the values for \(k=1,\ldots,6\) are \(1,57,302,302,57,1\).

## Assumptions and scope

All graphs are finite, undirected and simple, possibly disconnected. A token configuration is a \(k\)-subset of \(V(G)\); two configurations are adjacent when their symmetric difference is an edge of \(G\). A simple cycle is counted without a marked starting vertex or orientation. Odd girth is the length of a shortest odd simple cycle, or infinite if there is none. The theorem is for the full, unrestricted token graph, not the graph of token movements constrained to remain independent sets.

## Proof

**1. Parity projection and lower bound.** Consider any closed token walk of odd length \(\ell\). For each base edge \(e\), let \(m_e\) be its number of uses in this token walk and retain edges with odd \(m_e\). Because the initial and final occupancy vector agree, the mod-two sum of the endpoints of the traversed edges vanishes. Consequently the retained edge set has even degree at every base vertex. It also has odd cardinality, since \(\sum_e m_e=\ell\) is odd. An even-degree subgraph of odd size must contain an odd simple cycle (decompose its nonempty Eulerian components into cycles). Thus \(\ell\ge g\).

If \(\ell=g\), the retained edge set contains an odd simple cycle of length at least \(g\), so it consists of exactly the \(g\) edges of one base shortest odd cycle \(C\). Every edge is traversed precisely once and no other edge is used. The base support \(C\) is therefore uniquely recoverable from the token cycle. Every vertex outside \(C\) has constant occupancy. If \(h\) tokens lie on \(C\), then \(1\le h\le g-1\), and there are \(\binom{n-g}{k-h}\) choices for the fixed outside configuration.

**2. Unidirectional flow.** Fix a cyclic orientation of the base \(g\)-cycle \(C\), and index its edges \(e_i:i\to i+1\) modulo \(g\). Traverse a closed token cycle of length \(g\). Every base edge is used exactly once. Since the final occupancy agrees with the initial occupancy, the directed token-movement multigraph has equal indegree and outdegree at each vertex. On a simple cycle with each edge used once, this forces all movements to run in the same cyclic direction. Of the two ways to traverse an unoriented token cycle, exactly one has the fixed positive direction along \(C\).

**3. Eulerian count.** In that positive traversal, let \(t_i\in\{1,\ldots,g\}\) be the chronological position when edge \(e_i\) is used. These times are a permutation. A token initially occupies vertex \(i\) if and only if its outgoing edge is used before its incoming edge, that is, \(t_i<t_{i-1}\). Otherwise the vertex is initially empty, receives before sending, and ends empty. This condition simultaneously proves necessity and sufficiency: for any permutation of the times, the initial configuration given by these cyclic inequalities makes every move legal and restores the configuration at the end. Its number \(h\) of tokens equals the number of cyclic inequalities \(t_i<t_{i-1}\).

Every such \(g\)-step closed walk is a **simple** token cycle. Otherwise an internal repetition of a configuration would yield a nonempty proper contiguous collection of the distinct edges of \(C\) whose mod-two boundary is zero. But a nonempty proper subset of the edges of a simple cycle is not even-degree; contradiction.

There are \(g\left\langle{g-1\atop h-1}\right\rangle\) permutations of \(g\) time labels with \(h\) cyclic descents. To see this directly, cut the cyclic list immediately after its largest time. Its remaining \(g-1\) entries form an arbitrary permutation and contribute \(h-1\) ordinary descents, while the comparison across the maximum contributes the remaining cyclic descent. The maximum has \(g\) possible labeled positions. Each unoriented token cycle is counted \(g\) times by choice of its starting configuration, and exactly once by the positive traversal direction. Therefore \(C\) supports precisely \(\left\langle{g-1\atop h-1}\right\rangle\) token cycles with \(h\) moving tokens.

**4. Complete census and upper bound.** Multiply this number by \(\binom{n-g}{k-h}\) and sum over \(h\) and over the \(c_g(G)\) distinct base cycles. The uniqueness from Step 1 prevents overlap. The sum is positive for any \(1\le k\le n-1\): there exists a permissible \(h\) satisfying \(1\le h\le g-1\) and \(0\le k-h\le n-g\), and all Eulerian numbers in range are positive. Thus a token \(g\)-cycle exists, giving equality of odd girths. If \(G\) is bipartite, the parity of the number of tokens on one bipartition class is a proper two-coloring of \(F_k(G)\); thus no odd token cycle occurs. This proves all statements.

## Verification

The companion script `VERIFY.py` constructs token graphs independently from their definitions, exhaustively counts simple odd cycles of the necessary lengths without counting orientations twice, and compares to the Eulerian formula. It passed on 39 base graph instances, 126 token counts, including odd cycles, cliques, bouquets, pendant extensions, and fixed-seed random graphs of orders at most eight. For bipartite cases, the script independently certifies bipartiteness by graph traversal. Reproduce with `python3 VERIFY.py` (Python standard library only). This is finite corroboration, not a substitute for the all-graph proof above.

## Relationship to prior work

The September 1, 2025 *Generalized Token Graphs* paper studies simultaneous-token movement, including an explicit failure of odd-cycle and bipartiteness inheritance in the two-at-a-time variant; this motivates a precise census of odd-cycle inheritance for ordinary one-at-a-time token graphs. The 2009 foundational *Token Graphs* paper introduced the token-graph construction and basic counting properties. The 2024 *A study on token digraphs*, Theorem 6.1, establishes equality of **oriented girth** between a digraph and its token digraph, but it neither enumerates shortest **undirected odd** cycles nor gives Eulerian multiplicities. The November 18, 2026 *Max-Cut on Token Graphs* paper studies token graph cuts and specifically records the known lifting and exact count of **triangles** (Section 3.2, equation (10)), which agrees with the present formula when \(g=3\): \(c_3(F_k(G))=c_3(G)\binom{n-2}{k-1}\). That triangle identity is not claimed as new. The extension to all shortest odd lengths, the supporting-cycle rigidity, and Eulerian multiplicities for larger odd girths constitute the result here.

## Limitations

The formula counts cycles of the **minimum odd length** only, not arbitrary odd lengths or the total number of cycles. It does not determine the maximum cut or frustration index of a general token graph. Independent validation and exhaustive historical-priority checking have not been performed; equivalent formulations under exclusion-process terminology could exist. The theorem and reproducibility code are limited to finite simple undirected graphs and ordinary unrestricted tokens.

## References

1. C. Amairani Herrera-Ramirez and Teresa I. Hoekstra-Mendoza, *Generalized Token Graphs*, arXiv:2509.01773v1, September 1, 2025, https://arxiv.org/html/2509.01773v1, Section 2 (ordinary versus simultaneous-token bipartiteness).
2. José Angel Alejandro-Soto et al., *Max-Cut on Token Graphs*, arXiv:2611.25153v1, first publicly posted November 18, 2026, https://arxiv.org/html/2611.25153v1, Section 3.2.
3. Cristina G. Fernandes et al., *A study on token digraphs*, arXiv:2410.20189v1, 2024, https://arxiv.org/html/2410.20189v1, Section 6, Theorem 6.1.
4. Ruy Fabila-Monroy et al., *Token Graphs*, arXiv:0910.4774v1, 2009, https://arxiv.org/html/0910.4774v1, Sections 2–4.
