# Boundary-rank enumeration of short cycles in permutation-overlap graphs

## Finding

For every pair of integers \(k\ge 1\) and \(n\ge 2k\), rooted, edge-distinguished closed walks of length \(k\) in the full permutation-overlap multigraph \(G(n)\) can be counted exactly by enumerating at most
\[
(n)_k\binom{n-k}{k}
\]
possible boundary descriptions, reconstructing **at most one vertex per description**, and testing its \((n+1)^k\) rank-insertion walks. Consequently the count is computable in \(O_k(n^{3k+1})\) elementary arithmetic operations, rather than requiring enumeration of all \(n!\) vertices. The exact construction and proof are below.

As an independently useful finite application, the complete exact number of edge-distinguished directed three-cycles of \(G(n)\), for every integer \(6\le n\le24\), is recorded in `three_cycle_census.csv`. In order of \(n=6,7,\ldots,24\), these numbers are
\[
56,76,98,98,124,152,152,184,218,218,256,296,296,340,386,386,436,488,488.
\]
A directed cycle is counted up to cyclic choice of starting vertex, but distinct edge labels (including parallel edges) distinguish cycles. These are finite exact counts, **not** an assertion of an all-\(n\) quasi-polynomial formula.

## Assumptions and scope

Let \(\mathfrak S_n\) be the permutations of \(\{1,\ldots,n\}\). For a sequence of distinct real entries, \(\operatorname{st}\) replaces entries by their relative ranks. The multigraph \(G(n)\) has vertex set \(\mathfrak S_n\) and one directed edge for each \(\pi\in\mathfrak S_{n+1}\), going from \(\operatorname{st}(\pi_1,\ldots,\pi_n)\) to \(\operatorname{st}(\pi_2,\ldots,\pi_{n+1})\). Different permutations can supply parallel edges, and they are distinguished throughout.

A *rooted closed \(k\)-walk* specifies a starting vertex and an ordered list of \(k\) labeled edges returning to it. A *directed three-cycle* has three distinct vertices and is identified under cyclic rotation of its three edges, but not under reversal. The algorithmic theorem assumes \(n\ge2k\); the small-length direct computation is a separate check.

## Proof

**1. The overlap test.** A permutation \(v=(v_1,\ldots,v_n)\) can support a rooted closed \(k\)-walk only if
\[
\operatorname{st}(v_1,\ldots,v_{n-k})
=\operatorname{st}(v_{k+1},\ldots,v_n).
\tag{1}
\]
This follows by composing the \(k\) consecutive order-pattern overlaps. Conversely, condition (1) is sufficient for a closed walk: choose a permutation of \(n+k\) distinct numbers whose first \(n\) entries standardize to \(v\), and whose last \(n\) entries have the same relative order as \(v\); the equality of overlap orders gives a consistent acyclic partial order (the two windows overlap in \(n-k\) positions), so a linear extension supplies all \(k\) edge labels. This is also the overlap characterization proved in Asplund–Fox [1, Theorems 1 and 3]. Sufficiency is not necessary for the candidate-enumeration upper bound, but shows that every surviving vertex is relevant.

**2. Boundary-rank reconstruction.** Write \(A=(v_1,\ldots,v_k)\), an **ordered** \(k\)-tuple of distinct ranks, and \(B=\{v_{n-k+1},\ldots,v_n\}\), an **unordered** \(k\)-element rank set. Since \(n\ge2k\), these rank sets are disjoint. Put
\[
X=\{1,\ldots,n\}\setminus B,
\qquad Y=\{1,\ldots,n\}\setminus\{A_1,\ldots,A_k\}.
\]
There is a unique increasing bijection \(f:X\longrightarrow Y\), obtained by matching their ranks in ascending order. Equality (1) is equivalent to the \(n-k\) exact equations
\[
v_{i+k}=f(v_i),\qquad 1\le i\le n-k.
\tag{2}
\]
Thus, fixing \(A\) and \(B\) forces every value in positions congruent to \(r\) modulo \(k\), starting from \(A_r\), to be an iterate of \(f\). Reconstruct these \(k\) chains. Reject a description if an iterate is undefined before its prescribed final position, if an iterate exists after that final position, or if any rank is repeated. When none of these occurs, the construction assigns exactly \(n\) distinct elements of \(\{1,\ldots,n\}\); equation (2) holds, the endpoint ranks are precisely \(B\), and the reconstructed permutation is valid. The actual first \(k\) ranks and last-\(k\) rank set of a permutation recover its boundary description uniquely, so no vertex is counted twice.

There are exactly \((n)_k\binom{n-k}{k}\) possible input descriptions. Constructing each rank map and its chains costs \(O(n)\) operations for fixed \(k\). In particular, the candidate set is polynomial in \(n\) for any *fixed* \(k\).

**3. Exact edge multiplicities.** To obtain each outgoing **labeled** edge from a vertex \(v\), select the last entry's rank \(t\in\{1,\ldots,n+1\}\). Increment every entry of \(v\) that is at least \(t\), append \(t\), delete the first entry, and standardize the remaining length-\(n\) sequence. Distinct choices of \(t\) mean distinct \(\mathfrak S_{n+1}\) edge labels even when their endpoints coincide. Repeat this process for \(k\) steps and count exactly those rank sequences that return to \(v\). Every rooted labeled walk has precisely one starting vertex and one rank sequence, proving completeness and absence of double counting.

The number of rank sequences for a candidate is \((n+1)^k\), with \(O(kn)\) work per sequence. The total is
\[
O\!\left((n)_k\binom{n-k}{k}\bigl(n+kn(n+1)^k\bigr)\right)
=O_k(n^{3k+1}).
\]
As the count itself has at most \(O_k(\log n)\) bits, exact integer arithmetic also has polynomial bit complexity for each fixed \(k\). No claim of fixed-parameter tractability with exponent independent of \(k\) is made.

**4. Three-cycles versus closed walks.** Write \(W_3(n)\) for the rooted closed three-walk total, including edge multiplicities. For \(n>3\), the only vertices with loops are the increasing and decreasing permutations. They lie on no genuine directed two- or three-cycle [1, Theorem 6]. Any nonsimple closed three-walk must include a loop (because three positions with a repeated vertex force two neighboring vertices to coincide), and the remaining two steps, if not both loops, would form a two-cycle through the loop vertex, which is impossible. Hence the only nonsimple rooted closed three-walks are the two triple repetitions of the two trivial loops. All remaining closed three-walks have three distinct vertices and three possible roots, so
\[
C_3(n)=\frac{W_3(n)-2}{3}\qquad(n\ge4).
\tag{3}
\]
This also agrees with the prime-length decomposition principle of [1, Section 5], but here the distinction between **vertices**, **walks** and **edge multiplicities** is explicit.

**5. Finite exact computation.** The accompanying C++17 program implements the described boundary-rank bijection and triple rank-insertion enumeration with integer counters, exhaustively for \(6\le n\le24\). Each line in `three_cycle_census.csv` gives \(n\), the number of reconstructed candidate vertices, \(W_3(n)\), and \(C_3(n)\). For \(3\le n\le8\), a separate Python program constructs the entire graph directly from all \((n+1)!\) edge labels and evaluates its weighted three-step adjacency trace, giving agreement for all overlapping lengths. Neither check relies on Monte Carlo sampling or numerical approximation.

## Verification

From the directory containing the standalone files, run `python3 verify_counts.py` with Python 3 and a C++17 compiler (`g++`). It builds `count_three_cycles.cpp` in a temporary directory, checks all 19 rows of the supplied exact table, checks the divisibility and cycle-root identity (3), and independently performs direct graph construction for orders three through eight. A successful replay prints `VERIFY_OK` and `DIRECT_GRAPH_CHECK_OK`. The exhaustive counts are finite results; the all-\(n\), fixed-\(k\) algorithmic assertion is proved by Steps 1–3, rather than inferred from the finite tests.

## Relationship to prior work

Asplund and Fox [1] define the same multigraph and establish the standardization condition for closed walks. They count two-cycles, give a full vertex census only in a different parameter range, obtain upper bounds for parts of the remaining range, and explicitly ask in Question 24 for the number of \(k\)-cycles for \(3\le k<n\). The rank-set boundary reconstruction and resulting polynomial-for-fixed-\(k\) edge-multiplicity algorithm above are the assessed additions; the graph definition, overlap criterion, two-loop observation and earlier low-order examples are not new claims.

Ehrenborg, Kitaev and Steingrímsson [2] give a closed cycle formula for the **312-avoiding subgraph**, not this unrestricted multigraph. Borga and Penaguiao [3] study a **cycle polytope of limiting consecutive-pattern frequencies**, which does not supply these exact finite labeled-cycle multiplicities or this boundary-rank enumeration. The original full-text comparison to [1] and [2], and abstract/available article information for [3], is informative but does not establish absolute historical priority.

## Limitations

The polynomial bound applies when \(k\) is fixed and \(n\ge2k\). Its exponent depends on \(k\); the implementation covers only \(k=3\). The displayed three-cycle values are certified by explicit exhaustive computation for \(6\le n\le24\), **not** a formula for every \(n\). The result does not enumerate primitive cycles for arbitrary composite \(k\) without an additional period reduction. A matching historical result outside the inspected material may exist; no independent priority audit has been performed.

## References

[1] J. Asplund and N. B. Fox, *Enumerating cycles in the graph of overlapping permutations*, arXiv:1609.02210v1 (first posted 2016-09-07), https://arxiv.org/abs/1609.02210 .

[2] R. Ehrenborg, S. Kitaev and E. Steingrímsson, *Number of cycles in the graph of 312-avoiding permutations*, arXiv:1310.1520v1 (2013-10-05), https://arxiv.org/abs/1310.1520 .

[3] J. Borga and R. Penaguiao, *The feasible region for consecutive patterns of permutations is a cycle polytope*, *Algebraic Combinatorics* 3 (2020), 1259–1281, https://doi.org/10.5802/alco.135 .
