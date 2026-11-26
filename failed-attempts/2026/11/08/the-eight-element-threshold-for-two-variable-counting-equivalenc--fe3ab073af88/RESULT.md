# The eight-element threshold for two-variable counting equivalence of finite posets

## Finding

In the finite one-sorted signature consisting of equality and a strict partial-order relation \(<\), the first order at which two nonisomorphic posets have the same unrestricted two-variable counting theory, \(\mathrm C^2\), is **eight**. The entire first failure layer consists of precisely two unordered pairs. Thus the number of \(\mathrm C^2\)-equivalence classes on eight points is \(16{,}997\), whereas the number of isomorphism classes is \(16{,}999\).

The complete finite census is:

| Number of elements | Poset isomorphism classes | \(\mathrm C^2\)-equivalence classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 5 | 5 |
| 4 | 16 | 16 |
| 5 | 63 | 63 |
| 6 | 318 | 318 |
| 7 | 2,045 | 2,045 |
| **8** | **16,999** | **16,997** |

The empty poset is unique and causes no exception.

The first pair has respectively two and one connected components in the undirected comparability (equivalently, Hasse) graph. The second pair has connected Hasse graphs containing respectively ten and eight covering relations. Consequently, \(\mathrm C^2\) determines neither connectivity nor the number of covering relations of finite posets. Nonisomorphic equivalent pairs exist at every order at least eight.

## Assumptions and scope

A finite strict poset is a finite set \(P\) with an irreflexive, transitive relation \(<\). The reflexive relation \(\le\) is interdefinable in two variables by \(x\le y\iff (x=y\lor x<y)\); the result applies equally to the usual reflexive encoding. There are no extra unary predicates, named elements, or function symbols. Counting quantifiers range over vertices; \(\mathrm C^2\) allows arbitrary quantifier rank but uses at most two variable names. A covering pair \(x\prec y\) satisfies \(x<y\) with no intermediate \(z\) such that \(x<z<y\).

For a displayed eight-element poset, vertices are labeled \(0,\ldots,7\). Its row-code \((r_0,\ldots,r_7)\) means precisely \(i<j\iff r_i\mathbin{\&}2^j\ne0\); the code is a machine-readable representation, not a canonical label. The two exceptional pairs of row-codes are

\[
\begin{aligned}
 A_1&=(48,48,192,192,0,0,0,0),\\
 B_1&=(48,80,160,192,0,0,0,0),\\
 A_2&=(204,240,64,64,128,128,0,0),\\
 B_2&=(204,240,64,128,64,128,0,0).
\end{aligned}
\]

## Proof

**Direct existence and distinctions.** The comparability graph of \(A_1\) is the disjoint union of two four-cycles; that of \(B_1\) is an eight-cycle. Thus the posets are not isomorphic. In either, four minimal vertices have two upper neighbors and four maximal vertices have two lower neighbors. The two layers form a common equitable partition, establishing \(A_1\equiv_{\mathrm C^2}B_1\).

In both \(A_2\) and \(B_2\), the two minimal elements are strictly below exactly two of the four intermediate elements and both maximal elements; each intermediate element is strictly above one minimal element and below one maximal element; each maximal element is strictly above the two minimal elements and exactly two intermediates. Thus their common equitable three-class partition has cardinalities \((2,4,2)\). These posets are \(\mathrm C^2\)-equivalent. The transitive reductions have respectively ten and eight edges, so the posets are not isomorphic. In particular, their covering-relation counts differ although their strict-order incidence profiles coincide.

**Completeness of the finite classification.** Every nonempty finite poset has a maximal element. Removing one leaves a smaller poset; restoring it requires choosing exactly one order ideal \(I\) of the remaining poset as its strict predecessor set. Therefore, adjoining a maximal element above each ideal of each previously generated poset produces every isomorphism class at the next order. Isomorphic candidates are identified by an exact canonical form: sort vertices by the invariant pair (strict indegree, strict outdegree), enumerate every permutation within each equal-degree class, and choose the lexicographically smallest row-bit matrix. Two finite posets have the same canonical form if and only if they are isomorphic.

For each cardinality separately, directed color refinement starts with all vertices of all generated posets in one global color. In each round a new vertex color is its old color together with the multiset of colors of strict successors and the multiset of colors of strict predecessors. Color names are assigned from one common exact tuple palette across all posets of that order. This is the directed binary-relation form of the standard equivalence between color refinement and \(\mathrm C^2\). A stable global color-histogram equality is equivalent to unrestricted \(\mathrm C^2\)-equivalence. The accompanying verifier enumerates the complete set through eight points and finds no collisions below eight, exactly the two displayed pairs at eight, and no larger equivalence class there.

**All higher orders.** For any \(k\ge0\), adjoin \(k\) new isolated poset elements to both \(A_1\) and \(B_1\). Common disjoint extension preserves the two-variable counting-equivalence color-histograms, because the same isolated color contributions appear on each side at every refinement round. The resulting posets remain nonisomorphic: after removing isolated points, one comparability graph has two four-vertex components and the other a single eight-vertex component. Thus nonisomorphic \(\mathrm C^2\)-equivalent posets exist at every order at least eight. The connected-versus-disconnected distinction is asserted only for the eight-element exceptional pair.

## Verification

Run \(\texttt{python3 verify\_poset\_c2.py}\) using Python 3.9 or later; no third-party libraries are required. The program enumerates the strict-order closure directly from every order ideal, independently canonizes candidates over all degree-preserving permutations, and computes color refinement on a shared palette until the color IDs stabilize. It checks exact transitivity, both witness equivalences and nonisomorphisms, and connected-component and covering-edge distinctions. The eight-point output is \(\texttt{VERIFY\_OK 16999 16997 2}\); the full output is included in \(\texttt{census.txt}\). The poset totals match OEIS A000112 and the published Brinkmann–McKay enumeration. In a separate implementation using directed-graph isomorphism, the same numbers \(16{,}999\), \(16{,}997\), and two colliding pairs were obtained; this separate implementation is not part of the embedded replay artifact.

## Relationship to prior work

The equivalence of two-variable counting logic and directed color refinement is standard finite-model theory, and the general classification of \(\mathrm C^2\)-identified relational structures was developed by Kiefer, Schweitzer and Selman. Brinkmann and McKay enumerate posets up to sixteen points. These results supply the general logical and enumerative background. The present finite threshold, the exact two-class obstruction census, and their structural comparison are not stated in the inspected sources. No claim is made that the standard equivalence, the enumeration algorithm paradigm, or the two-cycle regularity construction itself is new.

## Limitations

The complete equivalence-class census is for orders at most eight, not arbitrary larger orders. The all-order construction proves the existence of nonisomorphic equivalent pairs, but not a general class-count formula. Unindexed or unpublished analyses of small poset color refinement may contain equivalent claims. The verification is exact and finite; it is not an independent external audit or a general theorem about arbitrary finite orders.

## References

1. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first publicly posted 2015-03-30), https://arxiv.org/abs/1503.08792.
2. G. Brinkmann and B. D. McKay, *Posets on up to 16 points*, *Order* **19** (2002), 147–179, https://users.cecs.anu.edu.au/~bdm/papers/posets.pdf.
3. OEIS A000112, *Number of partially ordered sets with n unlabeled elements*, https://oeis.org/A000112.
