# Optimal total-dominator colourings of the Heawood graph: mixed classes and two mobility sectors

## Finding
Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano plane. A **total-dominator colouring** is a partition of \(V(H)\) into nonempty independent colour classes such that, for each vertex \(v\), at least one entire class lies inside its **open** neighbourhood \(N_H(v)\). Two colourings that differ only by a permutation of the colour names are identified.

**Theorem.** The minimum number of classes is \(\chi_{td}(H)=8\), as previously established. There are **exactly \(2751\) distinct optimal, unlabelled eight-class partitions**. According to the number of classes meeting both bipartition sides, their distribution is
\[
\begin{array}{c|rrr}
\text{mixed classes}&0&1&2\\\hline
\text{partitions}&2401&322&28.
\end{array}
\]
In particular, \(350\) optimal partitions have one or two mixed classes that are *not themselves totally dominated by any vertex*. With eight prescribed, distinguishable and all-used colour names, there are \(2751\cdot8!=110{,}920{,}320\) optimum colourings.

Define a **one-vertex recolouring** of an unlabelled optimal partition to mean moving one vertex from a class containing at least two vertices into a different existing class, while leaving eight nonempty independent classes and preserving total-dominator validity. The resulting simple, undirected graph \(\mathcal R(H)\) has \(2751\) vertices, exactly \(11{,}662\) edges, and exactly \(23\) connected components:
\[
\boxed{21K_1\ \sqcup\ \mathcal C_{966}\ \sqcup\ \mathcal C_{1764}.}
\]
The notation specifies component cardinalities, not their complete isomorphism types. The \(21\) isolated partitions are exactly those indexed by **incident point–line flags** of the Fano plane: choose a line \(L\) and a point \(p\in L\); on the point side take singleton classes for all three points of \(L\) and a fourth class containing the other four points; on the line side take singleton classes for all three lines through \(p\) and a fourth class containing the other four lines.

The component of order \(1764\) consists precisely of unmixed partitions for which the four point classes, and separately the four line classes, have size profile \((1,1,2,3)\). The component of order \(966\) has \(616\) unmixed partitions and all \(350\) mixed partitions. The degree distribution of the entire one-vertex recolouring graph is
\[
\begin{array}{c|rrrrrr}
\text{degree}&0&2&5&6&7&10\\\hline
\text{number}&21&56&224&476&168&1806.
\end{array}
\]

## Assumptions and scope
The finite, simple, undirected Fano incidence graph is defined without a graph library. Its vertices are \(p_i\) and \(\ell_j\), with \(0\le i,j<7\), where
\[
p_i\sim\ell_j\quad\Longleftrightarrow\quad i-j\pmod7\in\{0,1,3\}.
\]
No two points and no two lines are adjacent. An optimal colouring is a **set partition**, with its eight nonempty classes unlabelled but with all fourteen graph vertices distinguished. A mixed class contains at least one point vertex and at least one line vertex. An edge of \(\mathcal R(H)\) is an unordered pair of *distinct* optimal partitions differing by a single class-to-class move of one vertex; exchanging names does not constitute a move.

## Proof
**1. Exhaustive small-integer theorem with a finite complete search.** The included standalone program `global_checker.cpp` generates *all* partitions of the fourteen labelled vertices into exactly \(k\) classes for each \(1\le k\le8\), without repeated partitions. It uses the unique restricted-growth encoding: vertex zero opens class zero; at vertex \(i\), choose one of the currently open classes or open exactly one new class. An insertion into an existing class is pruned only if that class contains a neighbour of vertex \(i\); this prunes exactly the improper partial partitions. The additional bound that the remaining vertices must be numerous enough to open the required classes is logically necessary, not heuristic. At a completed partition, for every vertex \(v\) the program tests whether some entire class \(C\) satisfies the bitwise inclusion \(C\subseteq N_H(v)\). There is no statistical sampling, search limit, or timeout-dependent acceptance. The exhaustive output has no valid partitions for \(k<8\) and exactly \(2751\) at \(k=8\). This independently reproduces the known optimum and completely establishes the finite configuration count.

**2. Independently enumerated Fano-side decomposition.** Every colour class intersects either the point side, the line side, or both. Its nonempty intersections induce a partition of the seven points and a partition of the seven lines. A mixed class cannot lie inside *any* open neighbourhood, since every open neighbourhood is contained entirely on one bipartition side. Hence the point-side classes that witness line vertices and the line-side classes that witness point vertices must be **unmixed**.

The independent program `side_checker.py` first enumerates the \(877\) set partitions of each seven-element side, then retains only partitions for which every opposite-side vertex has some contained class. The exact numbers of retained partitions with \(4,5,6,7\) classes are, respectively,
\[
49,\quad140,\quad21,\quad1.
\]
No partition with fewer than four classes can witness all seven opposite-side vertices, by this complete finite enumeration. The \(49\) four-class witnesses split into \(7\) partitions with block sizes \((1,1,1,4)\), whose three singleton points are collinear, and \(42\) with sizes \((1,1,2,3)\). Duality gives the same split for lines.

To reconstruct *every* eight-class colouring, choose one valid point-side and one valid line-side partition, and pair some point blocks with some line blocks. Every pairing must be a partial one-to-one matching of their block collections; a pair is allowed only if **no incidence edge** joins its point block to its line block (properness), and neither paired block may be needed as a total-domination witness. If the two side partitions have \(a\) and \(b\) classes, precisely \(a+b-8\) pairs must be merged. This construction is bijective, as each original mixed class has precisely one intersection block on each side and each unmixed class appears on one side. The complete side-based count is
\[
\begin{array}{c|c|c|r}
\text{point blocks}&\text{line blocks}&\text{merged pairs}&\text{valid eight-class partitions}\\\hline
4&4&0&2401\\
4&5&1&161\\
5&4&1&161\\
5&5&2&28.
\end{array}
\]
All other valid side-block-count pairs contribute zero. This sum is \(2401+161+161+28=2751\), agreeing with the unrelated full-graph restricted-growth enumeration. In particular, the unmixed count is \(49^2=2401\).

**3. Complete recolouring graph.** The C++ program sorts each accepted partition's eight disjoint 14-bit masks and uses this immutable representation as a key. For each non-singleton class, each member vertex, and each of the other seven classes, it constructs the result of moving that vertex and tests membership in the complete accepted-partition dictionary. This is a necessary and sufficient adjacency test; no potential one-vertex move is omitted. It counts each undirected edge once and runs breadth-first search to find all component sizes and vertex degrees. The independent Python program reconstructs the accepted partitions by the two-side method above and performs its own recolouring/BFS calculation. The two programs agree on exactly \(11{,}662\) edges, component sizes \(1\) repeated \(21\) times together with \(966\) and \(1764\), and the displayed degree histogram.

**4. Geometric identification of the frozen cases.** The Python checker additionally tests the geometric predicate directly on all \(21\) isolated states: on each side the four class sizes must be \((1,1,1,4)\), the three point singletons must form one Fano line, the three line singletons must form a pencil through a Fano point, and that point must lie on that Fano line. It finds that every isolated state satisfies the predicate. Conversely, the \(7\) Fano lines each contain \(3\) points, so the predicate describes exactly \(21\) pairwise distinct partitions; hence this identifies **all** isolated states. It also verifies that every state in the \(1764\)-vertex component has the dual \((1,1,2,3)\) profiles and no mixed class. Since there are exactly \(42\) such partitions on each side, \(42^2=1764\) exhausts that component.

These are finite exhaustive proofs: the two independent enumerations establish the exact set of feasible optimal partitions, and adjacency is then tested exhaustively on that entire set. No inference about larger projective planes is made from the enumeration.

## Verification
Both source files are complete and self-contained. A C++17 compiler and Python 3 are the only requirements. Execute, from their common directory:

```bash
g++ -std=c++17 -O2 -Wall -Wextra global_checker.cpp -o global_checker
./global_checker
python3 side_checker.py
```

Both programs were executed on their actual accompanying source files. Each printed `PASS` and reproduced \(2751\) optima, the distribution \((2401,322,28)\), \(11{,}662\) recolouring edges, \(21\) isolated vertices, components of sizes \(966\) and \(1764\), and the full degree histogram. The C++ program also checked every palette size from one through seven and found no valid smaller total-dominator partition. The Python program additionally verified the \(21\) incident-flag descriptions and the \(1764\)-state dual block profiles. No executable depends on prior research packages, external tables, or a special graph library.

## Relationship to prior work
Kazemi introduced total-dominator colouring in a publicly available 29 July 2013 preprint, whose vertex-first definition is exactly the one used here [1]. Alaei and Kazemi proved the **scalar** total-dominator chromatic number \(2q+4\) for incidence graphs of projective planes of prime-power order in their 2024 paper; this gives \(8\) for the Heawood graph but does not give the enumeration \(2751\), mixed-class refinement, or optimal recolouring graph [2, Section 4, Theorem 4.3]. Henning studied general bounds involving total domination, not the exact set of optimal Heawood colourings [3].

A separate result on *dominated colourings* of finite projective-plane incidence graphs uses the **opposite quantifier** (every colour class has a common neighbour). It therefore does not cover this theorem (every vertex has an entirely adjacent colour class). In fact the \(350\) mixed optimum classes found here have no common neighbour, making the distinction concrete. A separate classification of four-tuples of total dominating sets of the Heawood graph concerns overlapping vertex-subset witnesses, not proper partitions into eight total-dominator colour classes. Neither result entails the counts above. A separate complete census of proper named three-colourings of the Heawood graph also features \(21\) point–line flags among its frozen states after quotienting colour names; it works with a different three-colour condition and cannot imply the eight-class total-dominator enumeration or its additional two nontrivial exchange components.

## Limitations
The theorem is for the finite fourteen-vertex Heawood graph. It does not classify optimal total-dominator colourings for projective planes of larger order, nor imply a general formula for all projective planes. The connected components are specified by their exact sizes and membership properties rather than a complete abstract graph isomorphism classification. The proof is finite exhaustive, supported by two standalone implementations; it is not a symbolic all-order counting formula. Although relevant prior work has been compared by implication, historical priority cannot be certified against unindexed literature. No independent scholarly audit has been performed.

## References
1. A. P. Kazemi, *Toat Dominator Chromatic number of a Graph*, first public arXiv submission 29 July 2013, arXiv:1307.7486, https://arxiv.org/abs/1307.7486 (later appeared under corrected title in *Transactions on Combinatorics* 4(2), 2015).
2. M. Alaei and A. P. Kazemi, *The Moore graphs; total domination and total dominator chromatic numbers*, *Filomat* 38(25) (2024), 8947–8960, Theorems 4.2 and 4.3, https://www.pmf.ni.ac.rs/filomat-content/2024/38-25/38-25-21-23911.pdf .
3. M. A. Henning, *Total Dominator Colorings and Total Domination in Graphs*, *Graphs and Combinatorics* 31 (2015), 953–974, https://pure.uj.ac.za/en/publications/total-dominator-colorings-and-total-domination-in-graphs/ .
