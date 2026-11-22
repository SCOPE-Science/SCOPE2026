# Triangle-check peeling is graph powering, with exact stopping partitions

## Finding

Let \(n\geq 3\). Form a binary parity-check matrix \(H_n\) with columns indexed by the pairs \(\binom{[n]}2\), rows indexed by the triples \(\binom{[n]}3\), and entry \(H_n[T,e]=1\) exactly when \(e\subseteq T\). For an arbitrary initial set of erased columns \(E_0\), let \(U_0=\binom{[n]}2\setminus E_0\) be the graph of initially known pairs. Run **parallel peeling**: at each round, simultaneously recover every erased pair that is the sole erased member of some triple row, using only values known at the start of that round. Write \(U_t\) for the set of pairs known after \(t\) rounds, and \(d_0(a,b)\) for shortest-path distance in \(([n],U_0)\), with \(d_0(a,b)=\infty\) for pairs in different components.

**Complete triangle-peeling theorem.** For every integer \(t\geq0\),

\[
U_t=\{\{a,b\}:a\neq b,\ d_0(a,b)\leq 2^t\}.
\]

Consequently, if the initially known graph has connected components \(B_1,\ldots,B_c\), the unrecovered pairs at termination are exactly the edges of the complete multipartite graph with parts \(B_1,\ldots,B_c\). If \(D\) is the maximum finite distance between distinct vertices within one initial component, with \(D=0\) when all components are singletons, the **exact number of nonempty parallel rounds** is \(0\) when \(D\leq1\), and \(\lceil\log_2 D\rceil\) when \(D\geq2\).

The equivalent stopping-set classification is: \(E\subseteq\binom{[n]}2\) is a stopping set (including the empty one) precisely when \(E\) is the complete multipartite edge set of a unique set partition \(\pi\) of \([n]\). Thus the complete stopping-set polynomial is

\[
S_n(z)=\sum_{\pi\in\Pi_n}z^{\binom n2-\sum_{B\in\pi}\binom{|B|}{2}}
=\sum_{\sum_{j\geq1}j m_j=n}
\frac{n!}{\prod_{j\geq1}(j!)^{m_j}m_j!}
\,z^{\binom n2-\sum_{j\geq1}m_j\binom j2}.
\]

In particular, \(S_n(1)=B_n\), the Bell number. The nonempty inclusion-minimal stopping sets are exactly the nontrivial complete bipartite cuts \(K_{s,n-s}\), with one set for every unordered bipartition of \([n]\), hence \(2^{n-1}-1\) in total. Their smallest size is \(n-1\), attained by precisely \(n\) stars.

The binary code \(\ker_{\mathbb F_2}H_n\) is the cut-space code of \(K_n\), of dimension \(n-1\). An initially valid codeword has exactly \(2^{c-1}\) completions compatible with its known pairs, so **peeling recovers every erased coordinate if and only if maximum-likelihood erasure decoding has a unique completion**, namely when \(U_0\) is connected. If each pair is independently erased with probability \(\varepsilon\), the block success probability is the standard labelled-random-graph connectivity probability \(c_n(1-\varepsilon)\), where

\[
c_1(p)=1,\qquad
c_n(p)=1-\sum_{k=1}^{n-1}\binom{n-1}{k-1}c_k(p)(1-p)^{k(n-k)}.
\]

The worst possible number of parallel rounds, over all erasure patterns, is sharply \(\lceil\log_2(n-1)\rceil\), attained by taking \(U_0\) to be a spanning path.

## Assumptions and scope

The ground set is labelled and consists of exactly \(n\) vertices. The matrix has \(\binom n3\) parity checks, one for **every** triple, and \(\binom n2\) variables, one for **every** pair; removing checks changes the theorem. Erasures are known (not unknown symbol errors), parity checks are correct, and each decoding round uses the fully synchronous convention stated above. All graphs are simple and undirected; distances are measured in the initially **known** graph, not in the erased graph. A stopping set is any selection of variable columns such that each check row intersects that selection in zero or at least two columns. Bell-number and minimal-set enumerations count labelled pair subsets, not isomorphism classes.

## Proof

**1. Exact round dynamics.** A triple \(\{a,b,c\}\) has exactly one erased pair, \(\{a,b\}\), exactly when the pairs \(\{a,c\}\) and \(\{c,b\}\) are known and \(\{a,b\}\) is not. Hence one parallel peeling round replaces the known-edge graph by its square (adding all pairs joined by a walk of length two). Inductively, its \(t\)-round known pairs are those at initial distance at most \(2^t\). The forward inclusion follows by concatenating two walks each of length at most \(2^t\). Conversely, a shortest path of length at most \(2^{t+1}\) can be cut at a vertex into two subpaths, each of length at most \(2^t\), so its endpoint pair is obtained by the next round (or was known already). If two vertices are in separate original components they never become adjacent. Thus each component becomes a clique, and no cross-component pair can be recovered. The smallest number of rounds needed to complete all components is the least \(t\) with \(2^t\geq D\), using the explicit \(D\leq1\) convention. A spanning path has diameter \(n-1\), proving the worst-round bound is sharp.

**2. All stopping sets.** Write \(U=\binom{[n]}2\setminus E\). The stopping condition forbids a triple with exactly one erased edge, equivalently a triple with exactly two known edges. A graph with no induced three-vertex path is precisely a disjoint union of cliques: if some connected component were not complete, a shortest path between nonadjacent vertices in that component would have its first three vertices forming an induced path of length two. Hence \(U\) is a disjoint clique union. Its uniquely determined component partition gives the complete multipartite complement \(E\), and every such complement satisfies the stopping condition.

**3. Counting and inclusion minimality.** The partition-to-stopping-set map is injective because the complement's clique components recover the partition. For a partition with part sizes \(b_1,\ldots,b_c\), the complement has \(\binom n2-\sum_i\binom{b_i}2\) edges. Summing over partitions, or using multiplicities \(m_j\) of block size \(j\), yields the displayed polynomial. Containment of stopping sets corresponds, in reverse order, to coarsening of partitions. A partition with three or more parts can be properly coarsened to a partition with at least two parts, giving a smaller nonempty stopping set. A partition with exactly two parts can only be coarsened to one part, giving the empty set, hence its stopping set is inclusion-minimal. A bipartition with block sizes \(s,n-s\) has \(s(n-s)\) cross edges, minimized at \(s=1\) or \(n-1\). The \(n\) resulting stars are distinct for \(n\geq3\). There are \(\tfrac12(2^n-2)=2^{n-1}-1\) unordered nontrivial bipartitions.

**4. Code-theoretic and random-graph consequences.** The triangle equations say \(x_{ab}+x_{ac}+x_{bc}=0\) over \(\mathbb F_2\). Fixing vertex \(1\) and setting \(y_1=0\), \(y_j=x_{1j}\) gives \(x_{ij}=y_i+y_j\); conversely these assignments satisfy every row. They have dimension \(n-1\), since the only redundant vertex-potential change is adding the same bit to every vertex. If the initially known graph has \(c\) components, a compatible alternative may independently flip all vertex potentials in any component, modulo the common flip, yielding exactly \(2^{c-1}\) completions. Full peeling recovery and unique global completion are therefore equivalent to initial connectivity. Under independent erasure probability \(\varepsilon\), initial known edges are precisely the independent-edge random graph with probability \(p=1-\varepsilon\). In the recurrence, partition the event of disconnection by the size \(k\) of the component containing a distinguished vertex: its \(k-1\) other vertices can be chosen in \(\binom{n-1}{k-1}\) ways, its induced graph must be connected with probability \(c_k(p)\), and every one of its \(k(n-k)\) outgoing pairs must be missing, with probability \((1-p)^{k(n-k)}\). Summing \(k=1,\ldots,n-1\) gives precisely the displayed recursion.

## Verification

Three standalone programs are supplied. `verify_peeling.py` explicitly performs row-wise parallel peeling on **every** erasure pattern for \(n=3,4,5,6\), independently computes shortest paths from initially known pairs, and checks both the final residual set and exact round count. Its inclusion-minimal stopping sets are checked against all proper nonempty stopping subsets, not merely single-edge deletions. `verify_components.cpp` reconstructs triangle constraints and initial graph distances in separate representations and exhaustively checks the same state spaces, also comparing stopping counts with a Bell recurrence. `verify_partitions.py` enumerates set partitions without using Tanner decoding and independently computes the stopping polynomial, plus the labelled connected-graph recurrence. All programs exited successfully with the supplied commands and expected finite output.

For \(n=3,4,5,6\), the stopping-set totals are \(5,15,52,203\), and the numbers of erasure patterns successfully decoded at erasure probability \(1/2\), counted without probability weights, are \(4,38,728,26704\). These are exhaustive finite checks, **not** substitutes for the all-\(n\) proof above.

Reproduce using:

```bash
python3 verify_peeling.py
python3 verify_partitions.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_components.cpp -o verify_components
./verify_components
```

## Relationship to prior work

The definition and importance of stopping sets for binary erasure decoding were established previously, and the general design bound of Kashyap and Vardy yields the smallest stopping-set size for some incidence structures. Specifically, the \(n-2\) triples containing any given pair make column weight \(n-2\), while any two pair columns meet in at most one row, so their general lower bound already gives \(n-1\) here; **this minimum lower bound is not claimed new**. Their paper's examined complete projective-plane stopping enumerations use different matrices and do not give the all-\(n\) triangle-check closure theorem. Psota and Pérez describe generic Tanner-graph stopping-set mechanisms, not this exact all-round graph-power equivalence. General results on the cut-space code of a graph, labelled connected-graph counts and Bell numbers are also classical. The proposed contribution is their **joint exact identification with the particular all-triples synchronous peeling dynamics**: its full residual configuration, exact number of parallel rounds, all stopping configurations and maximum-likelihood agreement.

Relevant published mathematical-result records about stopping sets in \(\operatorname{PG}(2,3)\) concern a 13-column point–line incidence matrix, not the pair–triple matrix with \(\binom n2\) columns. Thus those numerical results do not imply the present theorem. This is a best-knowledge priority assessment, not a mathematical proof of originality.

## Limitations

This theorem requires all triple checks and does not extend by the given proof to arbitrary sparse parity-check row selections, other Boolean rank levels, noisy transmission, or asynchronous update times. It gives the exact independent-erasure success law, but does not claim a new derivation of classical random-graph connectivity asymptotics. The cut-code structure, the P3-free characterization and the general stopping-set bound are established mathematical ingredients. A prior equivalent result under another coding or graph-closure terminology may exist; no independent scholarly priority audit was conducted.

## References

1. N. Kashyap and A. Vardy, *Stopping Sets in Codes from Designs*, IEEE International Symposium on Information Theory (2003), DOI: 10.1109/ISIT.2003.1228136. Author-hosted full manuscript: https://ece.iisc.ac.in/~nkashyap/Papers/stopsets.pdf ; readable full text: https://www.researchgate.net/publication/4033626_Stopping_sets_in_codes_from_designs
2. E. Psota and L. C. Pérez, *The Manifestation of Stopping Sets and Absorbing Sets as Deviations on the Computation Trees of LDPC Codes*, Journal of Electrical and Computer Engineering (first published 2010-08-04), DOI: 10.1155/2010/432495, https://onlinelibrary.wiley.com/doi/10.1155/2010/432495
3. K. A. S. Abdel-Ghaffar and J. H. Weber, *Complete Enumeration of Stopping Sets of Full-Rank Parity-Check Matrices of Hamming Codes*, arXiv:cs/0603007 (2006). Different parity-check representation; referenced as a nearby enumeration topic, not asserted to settle this result.
