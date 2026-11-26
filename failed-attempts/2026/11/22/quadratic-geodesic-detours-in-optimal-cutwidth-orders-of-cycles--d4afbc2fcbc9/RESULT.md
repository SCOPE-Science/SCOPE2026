# Quadratic geodesic detours in optimal cutwidth orders of cycles

## Finding

For every integer \(n\ge3\), let \(C_n\) be the simple labelled cycle with vertex set \(\mathbb Z/n\mathbb Z\), and let \(\mathcal R_n\) be the graph of all vertex orders of cutwidth exactly \(2\). Two orders are adjacent when a single swap of consecutive positions leaves the cutwidth equal to \(2\). Then \(\mathcal R_n\) is connected, and it has

\[
|V(\mathcal R_n)|=n2^{n-2},\qquad
|E(\mathcal R_n)|=n(n+1)2^{n-4}.
\]

For every integer \(0\le j\le n-3\), precisely \(2n\binom{n-3}{j}\) configurations have degree \(j+2\). Orders beginning at the same labelled vertex form an isometric induced subgraph: between any two such orders, the minimum feasible swap count equals their ordinary Kendall inversion distance.

Write \(\rho_s=(s,s+1,\ldots,s+n-1)\) with entries read modulo \(n\). For every \(s\in\mathbb Z/n\mathbb Z\) and \(0\le k<n\), the *exact* distance between cyclically rotated clockwise orders is

\[
d_{\mathcal R_n}(\rho_s,\rho_{s+k})=(n-1)\min\{k,n-k\}.
\]

Their unconstrained Kendall distance is \(k(n-k)\). In particular, for \(1\le k\le\lfloor n/2\rfloor\), the optimal-cutwidth restriction forces precisely \(k(k-1)\) extra swaps, yielding a quadratic detour at half rotation. The result concerns exact optimal-width preservation, not the relaxed width bound of general order-reconfiguration theorems.

## Assumptions and scope

For a linear ordering \(\pi=(\pi_1,\ldots,\pi_n)\), its cutwidth is the maximum, over \(1\le t<n\), of the number of cycle edges with one endpoint in \(\{\pi_1,\ldots,\pi_t\}\) and the other outside. All vertices are distinguishable; neither cyclic shifts of the order nor rotations/reflections of vertex labels are identified. A move swaps the entries at consecutive *order positions*, not necessarily adjacent cycle vertices. Each intermediate order must have optimum cutwidth \(2\).

## Proof

**(1) Classification.** Every cycle vertex has degree two, so the first cut of every ordering has size two. A nonempty proper subset of vertices of a cycle has cut boundary twice the number of its cyclic connected components. Thus cutwidth two means that every nontrivial prefix of the order is one cyclic interval. Conversely, growing such an interval one vertex at a time preserves width two. Fix the first vertex \(s\). At positions \(2,\ldots,n-1\), choose whether the next vertex extends the clockwise end (bit \(1\)) or the counterclockwise end (bit \(0\)); the final vertex is forced. This is a bijection between optimal orders and pairs \((s,b)\), with \(s\in\mathbb Z/n\mathbb Z\) and \(b\in\{0,1\}^{n-2}\).

**(2) Complete move classification.** Put \(m=n-2\) and write \(b=(b_1,\ldots,b_m)\). Swapping positions one and two replaces \((s,b_1)\) by \((s+1,0)\) if \(b_1=1\), or by \((s-1,1)\) if \(b_1=0\), leaving later bits unchanged. Swapping the final two positions toggles \(b_m\). For every \(1\le i<m\), swapping positions \(i+1\) and \(i+2\) is legal exactly when \(b_i\ne b_{i+1}\), and then it exchanges those two bits. No other consecutive-position swaps exist. These assertions follow because at a swap only the intermediate prefix changes: the two candidate vertices must both be adjacent to the existing interval, and internal choices can be exchanged exactly when they extend opposite ends.

**(3) Enumeration and connectivity.** Each binary word has two boundary moves and one additional move for each adjacent unequal bit pair. There are \(2\binom{m-1}{j}\) binary words with exactly \(j\) unequal consecutive pairs (specify the initial bit and the \(j\) switch locations). Multiplication by \(n\) gives the degree census and the handshake lemma gives the edge count. Within one fixed initial vertex \(s\), any bit word can be reduced to all zeros by successively moving a \(1\) rightward through adjacent \(10\leftrightarrow01\) exchanges and deleting it by toggling the final bit. Thus each fixed-root layer is connected. First-position swaps connect successive root layers, proving global connectivity.

**(4) Root-fixed isometry.** Let \(\pi,\sigma\) be optimal orders with the same first vertex. Suppose their first \(t-1\) positions agree and the desired vertex \(\sigma_t\) occurs at position \(j\ge t\) of the current order. The desired vertex is adjacent on the cycle to the already agreed nonempty prefix. Bubble it successively left across positions \(j-1,j-2,\ldots,t\). In each adjacent swap, the only changed prefix gains this desired vertex in place of its last member; it remains connected because it contains the agreed prefix to which the desired vertex is adjacent. All later prefixes are unchanged. Each swap removes one inversion relative to \(\sigma\), since all displaced vertices follow \(\sigma_t\) in the target. Repeating yields a feasible sequence of length exactly the Kendall inversion distance, and the latter is a lower bound on every sequence of adjacent swaps even when root changes temporarily. Therefore the fixed-root layers are isometric in \(\mathcal R_n\).

**(5) A conserved boundary flux and sharp rotation distances.** Regard \(b_i=1\) as a particle in cell \(i\) of a path of \(m\) cells. There are \(m+1=n-1\) interfaces: a left reservoir, the \(m-1\) internal adjacencies, and a right reservoir. Each legal swap in (2) moves exactly one particle through exactly one interface: the left move changes the initial root by \(+1\) for a particle exiting left, or \(-1\) for a particle entering left; internal swaps exchange a particle with a vacancy; the right move inserts or removes a particle. For a path from \((s,(1,\ldots,1))\) to \((s+k,(1,\ldots,1))\), let \(F_i\) denote the signed net particle flux through interface \(i\), positive toward the left. Conservation at every cell gives \(F_0=F_1=\cdots=F_m=F\), because its occupancy is unchanged. The root displacement equals \(F\) modulo \(n\), so \(|F|\ge\min\{k,n-k\}\). Each move crosses exactly one interface, and consequently every such path has at least \(\sum_{i=0}^{m}|F_i|=(n-1)|F|\) swaps.

This bound is achievable: from an all-one word, move one particle out through the left interface, transport the resulting vacancy from cell one to cell \(m\) by \(m-1\) internal swaps, and fill it through the right interface. This costs \(m+1=n-1\) and advances the initial root by one, restoring the all-one word. Reversing the sequence retreats the root by one at the same cost. Repeating in the shorter circular direction proves the distance formula. Ordinary Kendall distance between the two clockwise orders is \(k(n-k)\), the number of inversions between the rotated blocks. Subtraction gives \(k(k-1)\) for \(k\le n/2\).

## Verification

Run `python verification/enumerate_orders.py` and `python verification/flux_graph.py` from the directory containing this file. The first program constructs actual permutations, computes cutwidth directly, and exhaustively checks all the formulas and every root-fixed pair for \(3\le n\le8\). The second constructs the independently specified binary-transition graph and tests the degree and rotation-distance assertions for \(3\le n\le14\). Both are finite corroborations; the preceding arguments establish the statements for every integer \(n\ge3\).

## Relationship to prior work

Arrighi, Fernau, de Oliveira Oliveira and Wolf initiated the study of width-bounded adjacent-order swaps, establishing a general \(2k\)-width reconfiguration guarantee from orders of width \(k\), first publicly documented in 2021 and expanded in 2023. That guarantee allows intermediate width exceeding the optimum; it does not determine the exact width-two feasible graph of cycles, its degree census, its fixed-start isometry, or its sharp rotation distance. The quadratic detour is particular to the cyclic optimal-prefix constraint, not a claimed general obstruction for all graphs. A result on adjacent swaps among pattern-avoiding permutations concerns a different feasible permutation family and does not imply this cycle-graph theorem.

## Limitations

No formula is asserted for the distance between two arbitrary orders with different initial vertices, nor for the global radius or diameter. The exact rotation formula applies to clockwise full-cycle orders with identical growth-bit words, not to arbitrary states sharing an initial-root displacement. The result has an elementary proof and is subject to the possibility of historical equivalent formulations under other terminology for connected-prefix search orders.

## References

1. E. Arrighi, H. Fernau, M. de Oliveira Oliveira, and P. Wolf, *Order Reconfiguration Under Width Constraints*, MFCS 2021, LIPIcs 202, article 8. Publicly available 2021-08-18. https://doi.org/10.4230/LIPIcs.MFCS.2021.8
2. E. Arrighi, H. Fernau, M. de Oliveira Oliveira, and P. Wolf, *Order Reconfiguration under Width Constraints*, Journal of Graph Algorithms and Applications 27(6), 409–431 (2023). https://doi.org/10.7155/jgaa.00628
