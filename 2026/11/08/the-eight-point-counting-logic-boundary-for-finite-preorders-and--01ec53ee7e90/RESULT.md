# The eight-point counting-logic boundary for finite preorders and topologies

## Finding

Let \(X\) be a nonempty finite preorder: a finite set with one reflexive, transitive relation \(R(x,y)\). Interpret \(X\) as a one-binary-relation structure with equality. Let \(C^2\) denote first-order logic with arbitrary counting quantifiers and at most two variable names.

**Theorem.** For every pair of nonisomorphic preorders of order at most seven, their unrestricted \(C^2\) theories differ. At order eight, precisely two \(C^2\)-equivalence classes contain nonisomorphic preorders; each such class has exactly two isomorphism types. The other \(35{,}975\) classes are singletons. In particular, the \(35{,}979\) eight-point preorder types produce precisely \(35{,}977\) counting-logic classes.

Both exceptional pairs are **antisymmetric**. Consequently, every non-\(T_0\) finite topological space on at most eight points is \(C^2\)-distinguished from all other nonisomorphic finite topological spaces; the first failure of this property is already present among \(T_0\)-spaces at order eight.

| Points | Preorder types | \(C^2\) classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 3 | 3 |
| 3 | 9 | 9 |
| 4 | 33 | 33 |
| 5 | 139 | 139 |
| 6 | 718 | 718 |
| 7 | 4,535 | 4,535 |
| 8 | 35,979 | 35,977 |

The first exceptional pair consists of height-two posets with four minimal and four maximal elements, all incident with two comparabilities to the other level. Their undirected comparability graphs are respectively a single eight-cycle and two four-cycles. They are nonisomorphic because their comparability graphs have different component counts.

The second exceptional pair consists of two connected height-three posets with different numbers of covering relations: respectively eight and ten. That count is an isomorphism invariant.

## Assumptions and scope

All preorders are finite, nonempty, reflexive and transitive. Isomorphism preserves the single binary relation. The corresponding topology is the finite Alexandrov topology under the specialization-preorder bijection; \(T_0\) corresponds to antisymmetry. The counting logic has equality and unlimited fixed natural-number counting thresholds, but exactly two variable names. Equivalence is **relative to the class of finite preorders**, not to arbitrary relational structures.

## Proof

**Exhaustive generation.** A preorder identifies a partition into mutual-comparability equivalence classes \(x\sim y\iff R(x,y)\land R(y,x)\). These classes carry a finite quotient poset. Conversely, every finite poset with positive integral weights assigned to its points expands uniquely to a preorder by replacing each point by a complete equivalence class of the prescribed size. Thus, to enumerate all preorders of cardinality \(n\), enumerate every poset of size \(k\le n\), and every positive \(k\)-tuple of weights summing to \(n\). Duplicate weighted descriptions are harmless; exact relation-preserving isomorphism testing removes them when necessary.

Every nonempty poset has a maximal element. Removing one maximal element produces a smaller poset; its set of strict predecessors is an order ideal. Conversely, adjoining a new maximal element whose predecessors are any order ideal produces a poset. Beginning with the empty poset, this supplies an inductive exhaustive generator. At each size the checker eliminates duplicate posets using an exact backtracking isomorphism algorithm. The resulting poset-type totals through eight points are \(1,2,5,16,63,318,2045,16999\), matching the published independent census.

**Counting-type computation.** For a preorder on \(n\) vertices, start each vertex with one uniform color. At each refinement round, replace the color of \(x\) by the ordered pair of its previous color and the multiset of all \(4\)-tuples
\[
\bigl(R(x,y),R(y,x),[x=y],\operatorname{color}(y)\bigr),
\]
as \(y\) ranges over all vertices. Use the *same global palette* for all preorder structures of a fixed order, so that colors may be compared across structures. This is the directed relational version of counting color refinement: by the two-variable counting game/standard refinement characterization, two finite binary relational structures have the same \(C^2\) theory precisely when their stable color histograms agree. The equality bit prevents conflating diagonal and off-diagonal ordered pairs.

The verifier makes exactly these refinements for all weighted descriptions. Each stable-histogram group is then split into exact isomorphism types by a complete bijection backtracking test. Up to order seven each group contains only one isomorphism type. At order eight, exactly two groups contain two types, while every other group contains one. The two exceptional groups have one-point weights throughout, proving that all their structures are antisymmetric and that no non-\(T_0\) pair collides.

**Boundary witnesses.** The two exceptional groups are recorded by strict-relation bitmask rows, indexed from zero: for each row integer, bit \(j\) indicates a strict relation from the row vertex to vertex \(j\). The height-two pair has representatives `(48,48,192,192,0,0,0,0)` and `(48,80,160,192,0,0,0,0)`. The height-three pair has representatives `(204,240,64,64,128,128,0,0)` and `(204,240,64,128,64,128,0,0)`. Restoring the reflexive diagonal gives the actual preorder relations. The complete refinement calculation is reproducible from the attached checker. Distinct component counts and covering-relation counts establish nonisomorphism without relying only on program-generated canonical names.

Since counting quantifiers distinguish finite universe cardinalities, no pair of different orders is equivalent. Thus the checks over individual orders establish the combined bound through eight points.

## Verification

Run `python verify_preorders.py` using Python's standard library. The script independently generates all quotient-poset representatives, expands every allowed positive weight tuple, performs global directed counting refinement, and checks exact isomorphism in each resulting profile class. The executed verifier reports `VERIFY_OK preorders_8=35979 c2_classes_8=35977` and enumerates two exceptional pairs. The 35,979 total agrees with the independently published sequence for unlabeled finite topologies, while 16,999 is the independently published eight-point poset count. The stand-alone verifier uses no third-party modules.

A separate experimental checker using a different isomorphism implementation reached the same totals and same two-pair structure. The published source counts do **not** themselves certify the new \(C^2\)-class counts.

## Relationship to prior work

Brinkmann and McKay (2005) enumerate isomorphism classes of finite quasiorders/topologies using quotient posets with positive weights and give 35,979 topological types at order eight. They do not tabulate their two-variable counting-theory equivalence classes. Kiefer, Schweitzer, and Selman (2015) develop the general theory and recognition machinery for finite relational structures identified by \(C^2\); the relevant inspected portions do not state this specialized sharp finite-topology census.

Earlier small-poset classifications already locate the two exceptional \(T_0\) pairs. The additional assertion proved here is that *none* of the 18,980 non-\(T_0\) eight-point topologies creates a new \(C^2\) collision, and that the full topology class has exactly 35,977 logical equivalence classes. The result is not claimed as a new general recognition algorithm.

## Limitations

The census is exhaustive only through eight points; there is no claim about the first non-\(T_0\) collision beyond that cutoff, or a formula for larger orders. Computational exhaustiveness relies on the finite-generation theorem, exact isomorphism backtracking, and the standard \(C^2\)/refinement equivalence; it is not inferred from sample testing. Historical priority remains qualified by the possibility of unindexed earlier finite computations. Independent mathematical audit has not been performed.

## References

1. G. Brinkmann and B. D. McKay, *Counting Unlabelled Topologies and Transitive Relations*, Journal of Integer Sequences **8** (2005), Article 05.2.1, https://cs.uwaterloo.ca/journals/JIS/VOL8/McKay/mckay170.pdf .
2. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1 (March 30, 2015), https://arxiv.org/abs/1503.08792 .
3. OEIS A001930, *Number of topologies, or transitive digraphs with n unlabeled nodes*, https://oeis.org/A001930 .
4. OEIS A000112, *Number of partially ordered sets with n unlabeled elements*, https://oeis.org/A000112 .
