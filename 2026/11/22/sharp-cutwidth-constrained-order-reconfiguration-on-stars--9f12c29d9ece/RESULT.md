# Sharp cutwidth-constrained order reconfiguration on stars

## Finding
For an integer \(r\ge 2\), let \(S_r=K_{1,r}\) be the star with \(r\) individually labelled leaves and a distinguished hub. For an integer budget \(k\) with \(0\le k\le r\), let \(\mathcal R_{r,k}\) be the graph whose vertices are linear orders of these \(r+1\) vertices of cutwidth at most \(k\), and whose edges are swaps of consecutive positions that preserve that budget.

The graph is empty for \(k<\lceil r/2\rceil\). For \(k\ge\lceil r/2\rceil\), put \(h=2k-r+1\). It has exactly \(h\,r!\) vertices. Its exact geometry has two regimes:

1. If \(r\) is even and \(k=r/2\), it has precisely \(\binom{r}{r/2}\) connected components, one for each subset of \(r/2\) leaves before the hub. Each is the Cartesian product of two adjacent-transposition permutahedron graphs on \(r/2\) labels, has \(((r/2)!)^2\) vertices and diameter \(r(r-2)/4\). Different components are unreachable.
2. In every other nonempty case (equivalently \(h\ge2\)), \(\mathcal R_{r,k}\) is connected and **isometric in the full adjacent-transposition permutahedron**. For any two permitted orders \(\sigma,\tau\), its distance is their Kendall inversion distance
   \[
   d_{\mathcal R_{r,k}}(\sigma,\tau)
   =\#\{\{a,b\}:a\ne b,\ a\text{ precedes }b\text{ in }\sigma,\ b\text{ precedes }a\text{ in }\tau\}.
   \]
   Every vertex has eccentricity \(\binom{r+1}{2}\), which is therefore the exact diameter. An inversion-decreasing adjacent-swap algorithm constructs a shortest path of exactly that pairwise Kendall distance, never exceeding the original cutwidth budget.

The total number of edges in a nonempty graph is
\[
 |E(\mathcal R_{r,k})|=
 \begin{cases}
 r!\bigl(h(r-2)/2+h-1\bigr),&k<r,\\
 r(r+1)!/2,&k=r.
 \end{cases}
\]

Thus for odd \(r\), all minimum-cutwidth star orders are already mutually reachable by shortest unrestricted adjacent-swap paths; for even \(r\), minimum-width orders fragment and **one additional unit of cutwidth** restores connectivity and all unrestricted shortest-path distances.

## Assumptions and scope
Every vertex and leaf is individually labelled; swaps occur at adjacent *positions*, not necessarily across star edges. The cutwidth of an order is the maximum number of star edges crossing a prefix-suffix cut. Width budgets are integral and all graph edges have unit cost. The statement concerns unweighted stars, not trees in general or vertex-separation/pathwidth constraints. A disconnected graph is assigned no finite all-pairs diameter; the diameter quoted in regime 1 is per component.

## Proof
**1. Feasible orders.** Write an order as \(a_1\cdots a_c\,v\,b_1\cdots b_{r-c}\), with \(v\) the hub. Before the hub, the number of crossing edges increases from zero to \(c\); just after it, the number is \(r-c\) and then decreases to zero. Hence the exact cutwidth is \(\max(c,r-c)\). Therefore feasibility means \(r-k\le c\le k\), proving the empty threshold and \(h=2k-r+1\) possible hub positions, each with \(r!\) leaf orders.

**2. Frozen-hub regime.** If \(r\) is even and \(k=r/2\), the only feasible hub position is \(c=r/2\). No legal swap moves the hub. Each left-side leaf subset is invariant, and all adjacent permutations within the two sides are legal. Thus its component is the Cartesian product of two ordinary adjacent-swap permutation graphs. Component sizes, count and diameters follow from the factorial, binomial and inversion formulas. In particular the largest inversion distance inside a side of \(c\) leaves is \(\binom c2\), giving twice this bound for each product component.

**3. Interval lemma.** Let \(N\ge2\) labels be distinct and one label \(v\) distinguished. Restrict their adjacent-transposition graph to permutations in which precisely \(c\) entries precede \(v\), for some \(c\) in an integer interval \([L,U]\subseteq[0,N-1]\) with \(L<U\). This induced graph is isometric in the unrestricted graph.

To prove this, fix any current order \(\sigma\) and target \(\tau\) in the interval. Rank all labels by their positions in \(\tau\); an adjacent pair in \(\sigma\) is *inverted* when the first label has larger target rank. Swapping any such pair reduces Kendall distance to \(\tau\) by exactly one. If \(\sigma\ne\tau\), at least one adjacent inverted pair exists. When the current hub position \(c\) is strictly between \(L\) and \(U\), every adjacent swap is feasible and such a pair can be chosen.

When \(c=L\), the only potentially forbidden adjacent swap is moving the hub left. Suppose for contradiction that no feasible inverted pair exists. Every adjacent pair except possibly the pair immediately before the hub and the hub is then increasing in target rank. Consequently the hub precedes **every** entry to its right in \(\tau\). If the exceptional pair is not inverted then \(\sigma=\tau\), contradicting the choice. If it is inverted, the entry immediately left of the hub follows the hub in \(\tau\). Hence at most \(L-1\) entries can precede the hub in \(\tau\), contradicting the required target hub position at least \(L\). The analogous argument at \(c=U\) says that if the only inverted pair would move the hub right, then the hub follows every entry to its left **and** its immediate right neighbor in the target order, so the target hub position must be at least \(U+1\), also impossible. (If the hub is at an endpoint of the entire permutation, the corresponding forbidden adjacent pair does not exist.) Thus a *feasible* inverted pair always exists. Repeating swaps decreases the nonnegative inversion count by exactly one until \(\tau\) is reached. Every path requires at least one move per reversed pair, proving exact isometry and the constructive algorithm.

**4. Connected regime, diameter and edge enumeration.** Apply the lemma with \(N=r+1\), \(L=r-k\), \(U=k\) whenever \(h\ge2\). This proves connectivity and all pairwise distances. The reversal of any permitted word is again permitted because its hub position changes from \(c\) to \(r-c\), and \([r-k,k]\) is symmetric about \(r/2\). Reversal disagrees on every pair, giving eccentricity at least \(\binom{r+1}{2}\) at every vertex; the isometric upper bound proves equality.

If \(k<r\), all feasible hub positions are internal. At each fixed hub position there are \(r!\) states, each with \(r-2\) legal leaf-leaf swaps, contributing \(r!h(r-2)/2\) edges. Each of the \(h-1\) transitions between consecutive hub positions contributes exactly \(r!\) hub-leaf swaps. The displayed edge formula follows. For \(k=r\), all \((r+1)!\) orders and all \(r\) adjacent transpositions per order are legal, yielding \(r(r+1)!/2\) edges.

## Verification
The independent standard-library program `verify.py` enumerates all labelled orders and computes their actual star cutwidth by counting crossing edges for every prefix. It constructs the constrained swap graph directly, then compares observed components, edge counts and distances with the theorem. For connected cases, checking BFS from one representative at each hub position covers **all ordered pairs** by the free action of leaf-label relabelling. For disconnected cases, every component and all within-component distances are checked. The program succeeds for all \(2\le r\le7\), all integer \(0\le k\le r\), plus \((r,k)=(8,4),(8,5)\): 35 parameter pairs in total. Execute `python verify.py` next to this file. The proof, not the finite checks, establishes all \(r\) and \(k\).

## Relationship to prior work
Arrighi, Fernau, de Oliveira Oliveira and Wolf formulate cutwidth-bounded order reconfiguration and prove that two orders of cutwidth at most \(k\) can be connected while permitting width at most \(2k\), with polynomially many adjacent swaps [1,2]. That theorem does not directly imply connectivity *at the original budget* or the exact shortest feasible distance, especially at the minimum-width disconnected boundary. Here the star-specific cutwidth formula produces a sharp one-unit threshold and a metric stronger than mere polynomial-length reachability. The underlying unrestricted Kendall inversion metric of the permutahedron is classical; the interval lemma proves preservation under the imposed position restriction. Related permutation-reconfiguration claims for forbidden fixed points or partial permutohedra address different constrained state spaces [3,4] and do not imply this star-cutwidth classification.

## Limitations
No conclusion is claimed for weighted stars, arbitrary trees or other width notions. The proof gives an exact unweighted shortest path and a polynomial-time constructive procedure, but not a closed formula for the number of distinct shortest paths. Independent external mathematical review has not been performed. Historical-priority uncertainty remains for an equivalent result under alternative permutation-window terminology.

## References
[1] E. Arrighi, H. Fernau, M. de Oliveira Oliveira and P. Wolf, *Order Reconfiguration Under Width Constraints*, MFCS 2021, Article 8, published 2021-08-18, https://doi.org/10.4230/LIPIcs.MFCS.2021.8.

[2] E. Arrighi, H. Fernau, M. de Oliveira Oliveira and P. Wolf, *Order Reconfiguration under Width Constraints*, Journal of Graph Algorithms and Applications 27(6), 409–431 (2023), https://doi.org/10.7155/jgaa.00628.

[3] *Component signatures for permutations avoiding selected fixed points*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-component-signatures-for-permutations-avoiding-selected-fixed-po--79c08e75f702.

[4] *Geodesic rigidity of the permutohedral facet in partial permutohedra*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-geodesic-rigidity-of-the-permutohedral-facet-in-partial-permutoh--7910cdad70d2.
