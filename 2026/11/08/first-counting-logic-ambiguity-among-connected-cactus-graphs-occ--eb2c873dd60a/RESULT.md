# First counting-logic ambiguity among connected cactus graphs occurs at twelve vertices

## Finding
A **cactus graph** is a finite simple connected graph whose biconnected blocks are single edges or simple cycles. Let \(G\equiv_{C^2}H\) mean that two graphs satisfy the same unrestricted-depth two-variable first-order formulas with counting quantifiers, in the pure adjacency language. Equivalently, simultaneous ordinary vertex color refinement on the disjoint union has the same stable color histogram in each summand.

**Theorem.** The smallest order of two nonisomorphic connected cactus graphs that are \(C^2\)-equivalent is **\(12\)**. For every order from \(1\) to \(11\), color refinement separates all nonisomorphic connected cacti. The \(24{,}118\) isomorphism types of connected cacti on \(12\) vertices fall into exactly \(24{,}116\) stable-color equivalence classes: there are precisely **two** classes of size two and \(24{,}114\) singleton classes.

The four witnesses can be specified unambiguously by standard graph6 encodings (no graph labels beyond graph6 are needed):

| Pair | First graph6 string | Second graph6 string | Edges | Different block-size information |
| --- | --- | --- | ---: | --- |
| A | `Kl_GGE@?_?_P` | `K{CGGC@_GC?P` | 14 each | \((4,4,6)\) versus \((3,3,8)\) |
| B | ``KpCKGO_GGG?` `` | ``KtGGGC`?_C_A`` | 14 each | Both \((2,2,3,3,6)\) |

Within pair A both degree multisets have two vertices of degree four and ten of degree two. Within pair B the degrees are \((4,4,3,3,2,2,2,2,2,2,1,1)\). Pair B is nonisomorphic by its distinct canonical block-tree encodings, even though the displayed block sizes coincide.

## Assumptions and scope
Graphs are finite, simple, uncolored and undirected. A singleton is allowed as a cactus. A *block* means a maximal subgraph without a cut vertex, with bridges counted as two-vertex blocks. Color refinement starts with one common color and simultaneously replaces each vertex color by its old color and the multiset of colors on its neighbors. Colors are compared **globally** across all graphs of a fixed order, not assigned separately on each graph. There is no counting-threshold or quantifier-depth bound. The minimum and the uniqueness claims are **relative to connected cacti**, not to all graphs.

## Proof
**1. Exhaustive graph generation.** Every connected cactus on at least two vertices has a leaf block, unless it is itself a single block. Removing all vertices of a leaf block except its unique attachment vertex gives a smaller connected cactus. Conversely, every such extension is obtained by adjoining to a vertex either one edge ending in a new vertex or a new cycle, all of whose other vertices are new. The standalone program begins at the one-vertex graph and performs *all* extensions of each previously retained isomorphism type, for all allowable block lengths. This exhausts every cactus by induction on its vertex order; it cannot introduce a non-cactus because only a leaf block is added.

**2. Exact isomorphism deduplication.** For a connected cactus \(G\), its vertex-block incidence graph is a tree. For any root vertex \(v\), recursively encode incident child blocks in sorted order. An edge block is encoded with its opposite endpoint subtree. A cycle block is encoded by the cyclic order of its other vertex-subtrees, with reversal normalized by choosing the lexicographically smaller orientation. A vertex encoding is its sorted multiset of child-block encodings. Finally choose the lexicographically least encoding over **all** possible root vertices. This is a complete invariant: equality reconstructs a rooted block-incidence tree with each cycle's adjacency order; minimizing over all roots removes the marked-root choice. Conversely, an isomorphism preserves this recursive encoding. Thus one representative is retained from each isomorphism type, without probabilistic graph hashing or a black-box isomorphism test.

The exact unlabelled counts for orders \(1\) through \(12\) are
\[
1,1,2,4,9,23,63,188,596,1979,6804,24118.
\]
They agree with the independent established cactus enumeration OEIS A000083.

**3. Exact counting refinement.** At each order all retained graphs start with the *same* color zero. At each round, one shared integer palette maps each pair (old color, sorted neighbor-color multiset) to a new integer, and the same palette is used for all graphs. The procedure stops only when its total number of color classes does not increase; because each round refines the previous partition, equality of the number of classes means the partition is stable. At that point two graphs are counting-logic equivalent exactly if the sorted multisets of their global color IDs coincide. This computation uses exact Python tuples and integers, **not truncated hashes**. The stable comparison at orders \(2\) through \(12\) takes respectively \(1,3,4,5,6,7,8,9,10,11,12\) rounds in the packaged program's convention. For orders at most \(11\), every globally stable histogram is unique among nonisomorphic cactus representatives; for order \(12\), exactly two histograms occur twice and no histogram occurs more than twice. Every pair's members have distinct exact canonical block-tree encodings, so both are genuinely nonisomorphic.

**4. Logical correspondence.** For finite graphs, the standard color-refinement/two-variable counting-logic theorem says that two structures satisfy the same \(C^2\) sentences if and only if their stable color histograms, computed with a shared palette, agree. Thus the finite exhaustive result implies the theorem as stated.

## Verification
Run `python verify.py` with `networkx==3.6.1`; its dependency is pinned in `requirements.txt`. The program enumerates all cacti of orders \(1\) through \(12\), checks the known counts at each order, compares exact globally stable integer-color histograms, checks nonisomorphism for each doubleton using an independent graph-isomorphism call, checks their cactus property, prints their graph6 encodings and block-size multisets, and ends with `CENSUS_VERIFIED 24118 TWO_COLLISION_PAIRS`. The observed output is included verbatim in `verification_output.txt`.

## Relationship to prior work
Arvind–Köbler–Rattan–Verbitsky give the general equivalence of color refinement, fractional isomorphism and counting-logic indistinguishability, and analyze structural amenability. Kiefer–Schweitzer–Selman analyze identification by counting logics. The first cited works give the **criterion**, not the present class-specific first-obstruction census. OEIS A000083 supplies the standard unlabeled cactus graph totals but does not partition them by logical theory. A finite graph can fail to have its vertex-orbit partition recovered by color refinement without yielding a *pair* of nonisomorphic cacti that color refinement fails to separate; these are different properties. The present result determines the latter precise threshold.

## Limitations
The theorem is finite through \(12\) vertices and makes no classification assertion beyond that order. It does not imply that its witnesses are globally non-amenable in a unique way, nor does it characterize \(C^3\) or higher logic. The exhaustive classification depends on the correctness of the supplied generator and stable-refinement implementation; an independent mathematical audit has not been performed. The priority search is bounded; obscure or unindexed earlier calculations could cover the numerical result.

## References
1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30, https://arxiv.org/abs/1503.08792.
3. OEIS A000083, *Number of mixed Husimi trees with n nodes; or polygonal cacti with bridges*, https://oeis.org/A000083.
