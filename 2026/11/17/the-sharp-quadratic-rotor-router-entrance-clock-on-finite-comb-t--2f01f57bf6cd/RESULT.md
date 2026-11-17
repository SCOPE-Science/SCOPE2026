# The sharp quadratic rotor-router entrance clock on finite comb trees

## Finding

For each integer \(n\ge2\), define the finite comb \(C_n\) with spine vertices \(v_0,\ldots,v_{n-1}\), spine edges \(v_iv_{i+1}\) for \(0\le i<n-1\), and one private leaf \(\ell_i\) adjacent to each \(v_i\). Starting from \(v_0\), the sharp maximum first-periodic-entry time of the one-chip rotor-router map, ranging over all initial rotors, is

\[
\tau_{\max}(n)=(n-1)(2n-1).
\]

The maximum is attained by **exactly one** initial spine-rotor configuration: all nonterminal spine rotors point toward the next vertex, and the terminal rotor points to its private leaf. Thus the maximum is asymptotically \(2n^2\), and the comb family has worst-case quadratic first-recurrence time.

## Assumptions and scope

Every undirected edge is available in both directions. At an internal spine vertex \(v_i\) with \(1\le i\le n-2\), the cyclic exit order is \((v_{i-1},\ell_i,v_{i+1})\); at \(v_0\) the order is \((\ell_0,v_1)\), and at \(v_{n-1}\) it is \((v_{n-2},\ell_{n-1})\). Each leaf's unique rotor points to its parent. A step advances the rotor at the chip's current vertex by one cyclic position and then moves the chip along the selected edge. One step is one edge traversal. Periodicity concerns the **entire** chip-and-rotor state, not merely chip position. First-entry time \(\tau\) is the least nonnegative time at which that full state belongs to a periodic orbit.

## Proof

**The frontier excursion lemma.** Fix any initial spine rotors and consider successive first visits to \(v_j\), provided recurrence has not occurred earlier. At the first visit to \(v_j\), every earlier spine vertex \(v_i\) with \(i<j\) has its rotor aimed toward \(v_{i+1}\), and all leaves attached to those earlier vertices aim toward their parent. This follows by induction: on a tree, starting at the root of a directed rotor tree pointing toward the root, increment-before-move performs at most one depth-first excursion through each child subtree before taking a designated unvisited exit. Every completed child excursion restores its subtree rotors to their parent-pointing directions. When the chip exits from \(v_j\) toward the previously unvisited \(v_{j+1}\), all earlier rotors therefore point toward the new frontier.

For a direct count, at first arrival at \(v_j\), regard the visited-prefix tree consisting of \(v_0,\ldots,v_j\) and their \(j+1\) leaves, rooted at \(v_j\). It has \(j\) spine edges and \(j+1\) leaf edges, hence \(2j+1\) edges. All rotors except that at its root point toward their parent. Before the root rotor next selects the fresh exit to \(v_{j+1}\), each rooted subtree can be completely toured at most once (each of its edges once in each direction). Thus the time between first visits to \(v_j\) and \(v_{j+1}\) is at most

\[
2(2j+1)+1=4j+3,\qquad 0\le j\le n-2.
\]

The bound is an equality precisely when the rotor at \(v_j\), at its first visit, is initially directed toward \(v_{j+1}\): all its other cyclic exits must then be used before the new exit. All other rotor positions shorten this stage. In particular, if there is no earlier recurrence, the first visit to \(v_{n-1}\) occurs by time

\[
\sum_{j=0}^{n-2}(4j+3)=(n-1)(2n-1).
\]

**Why this bounds the first recurrent entrance.** Upon first arriving at the terminal spine vertex, every earlier spine rotor points toward it and the attached leaves all point inward. The terminal rotor still has its initial direction. If it points left, its parent points right and the two spine vertices form the unique directed two-cycle; if it points to its leaf, those two form the unique directed two-cycle. The chip is on that cycle. For a rotor walk on a connected finite Eulerian digraph, such a state (a rotor unicycle with the chip on its cycle) is recurrent. Therefore first recurrence is no later than first terminal arrival, whether or not an earlier recurrence occurred.

**Attainment.** Initialize every \(v_j\), \(j<n-1\), toward \(v_{j+1}\), and initialize \(v_{n-1}\) toward its leaf. At every frontier the excursion takes all \(4j+3\) steps; first terminal arrival is therefore exactly the sum above. Until then, the untouched terminal rotor and its leaf form a directed two-cycle disjoint from the chip, so no earlier state can be a recurrent unicycle. On terminal arrival that dimer is the sole directed rotor cycle and contains the chip. This proves equality.

**Uniqueness.** Equality in the stage-by-stage upper bound forces each nonterminal spine rotor initially to point toward the next spine vertex. If the terminal rotor instead points left, the initial rotor of \(v_{n-2}\) already points right. At the first arrival at \(v_{n-2}\), the terminal edge is the unique directed dimer and the chip is on it, so the orbit is already recurrent strictly before the final endpoint visit (including the case \(n=2\), when that time is zero). Hence only the specified terminal leaf orientation achieves equality. This proves exactly one maximizer.

## Verification

A standalone C++ exhaustive enumeration (`verification/comb_exhaustive.cpp`) checks every possible initial spine rotor configuration for \(2\le n\le12\). For every tested size, the maximum matches \((n-1)(2n-1)\), and its maximizing multiplicity is one. The recurrence detector checks that the rotors have exactly one directed two-cycle and that the chip lies on it. On a tree every directed rotor cycle has length two, so this is exactly the recurrent-unicycle criterion. The numerical enumeration checks small instances; the proof above establishes all lengths.

| \(n\) | \(\tau_{\max}\) | Number of maximizers |
|---:|---:|---:|
| 2 | 3 | 1 |
| 3 | 10 | 1 |
| 4 | 21 | 1 |
| 5 | 36 | 1 |
| 6 | 55 | 1 |
| 7 | 78 | 1 |
| 8 | 105 | 1 |
| 9 | 136 | 1 |
| 10 | 171 | 1 |
| 11 | 210 | 1 |
| 12 | 253 | 1 |

## Relationship to prior work

The foundational rotor-unicycle criterion characterizes recurrence but supplies no sharp comb-specific entrance-time maximizer. General one-chip rotor-router stabilization bounds of order edges times diameter give an \(O(n^2)\) upper bound on this family but do not identify the leading constant or its unique realizing initialization. Existing research on the infinite comb addresses multi-particle aggregation and harmonic measures, not the finite one-chip first-recurrence extremum. Exact entrance clocks on paths, equal-arm spiders and sunlet graphs do not cover the leaf-decorated open spine with its particular cyclic mechanism.

## Limitations

This theorem fixes the starting spine endpoint and local cyclic rotor orders. It maximizes over initial rotor positions only, not over start vertices, rotor orders, or all trees of the same size. It does not classify all submaximal first-entry times or attraction basins. No independently conducted mathematical audit is claimed. Equivalent unindexed historical results remain possible.

## References

- W. Huss and E. Sava, *Rotor-Router Aggregation on the Comb*, arXiv:1103.4797 (first public preprint 2011-03-24), especially its introduction and aggregation theorems; https://arxiv.org/abs/1103.4797.
- V. S. Poghosyan and V. B. Priezzhev, *Euler tours and unicycles in the rotor-router model*, arXiv:1310.1225 (2013), sections I–II; https://arxiv.org/abs/1310.1225.
- J. Chalopin et al., *Lock-in Problem for Parallel Rotor-router Walks*, arXiv:1407.3200 (2014), abstract and introduction, including the one-chip \(2mD\) bound; https://arxiv.org/abs/1407.3200.
