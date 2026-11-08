# Complete non-matching homotopy filtration of the three-dimensional cube

## Finding

Let \(Q_3\) be the three-dimensional cube graph, with vertices \(0,1,\ldots,7\) encoded in binary, and an edge between distinct vertices precisely when their bitwise XOR is a power of two. For any integer \(k\geq 1\), let \(\operatorname{NM}_k(Q_3)\) be the simplicial complex whose vertices are the twelve graph edges and whose faces are edge sets having matching number strictly smaller than \(k\). Then the *entire filtration* has integral homotopy types

\[
\operatorname{NM}_k(Q_3)\simeq
\begin{cases}
\bigvee^{5} S^1,&k=2,\\
\bigvee^{9} S^3,&k=3,\\
S^5,&k=4,\\
\ast,&k\geq5.
\end{cases}
\]

At \(k=1\), the abstract complex consists of the empty face only, with no nonempty simplices. Equivalently, the positive-degree integral persistence barcode of the inclusions at increasing integer \(k\) consists of five bars \([2,3)\) in degree one, nine bars \([3,4)\) in degree three, and one bar \([4,5)\) in degree five. All other positive-degree integral bars are absent. The complete bipartite comparison \(\operatorname{NM}_k(K_{4,4})\) has sphere multiplicities \(9,9,1\) at the three respective nontrivial thresholds, whereas the cube, obtained by removing a perfect matching from \(K_{4,4}\), has \(5,9,1\).

## Assumptions and scope

Graphs are finite, simple, and undirected. The matching number \(\nu(F)\) of an edge set \(F\subseteq E(Q_3)\) is the largest size of a collection of pairwise vertex-disjoint edges from \(F\). The complex contains a simplex of dimension \(|F|-1\) for each nonempty \(F\) with \(\nu(F)<k\). The symbol \(\ast\) denotes a contractible complex; an empty wedge of spheres is interpreted as a point. Homotopy equivalences and homology statements have *integral* coefficients. The barcode claim is about inclusion-induced maps at integer thresholds and does not assert equivariance under graph automorphisms.

The ordered twelve-edge list is, with zero-based indices:

```text
0 (0,1)     1 (0,2)     2 (0,4)     3 (1,3)
4 (1,5)     5 (2,3)     6 (2,6)     7 (3,7)
8 (4,5)     9 (4,6)    10 (5,7)    11 (6,7)
```

The cube is isomorphic to \(K_{4,4}\) minus a perfect matching: split its vertices by binary parity; every even vertex is adjacent to exactly three of the four odd vertices and misses its unique antipode at Hamming distance three.

## Proof

Fix \(k\in\{2,3,4\}\), and let \(X_k=\operatorname{NM}_k(Q_3)\). All \(2^{12}=4096\) edge subsets are checked exhaustively. The matching number of a nonempty edge set \(F\) obeys the exact recursive identity

\[
\nu(F)=\max\bigl(\nu(F\setminus\{e\}),\,1+\nu(F\setminus E_{u,v})\bigr),
\]

where \(e=\{u,v\}\in F\), and \(E_{u,v}\) is the set of all cube edges incident with either \(u\) or \(v\). The base case is \(\nu(\varnothing)=0\). The first term omits \(e\); the second chooses \(e\) and then only edges disjoint from it. Thus the recurrence computes the exact matching number. A separate enumerator checks all disjoint-edge subfamilies directly and agrees on every input mask. The resulting face counts, including the empty face, are \(45,601,2665\) respectively for \(k=2,3,4\).

For each \(k\), construct a matching on the augmented face poset using the following fixed permutation \(p_k\) of the twelve edge indices. Initially all faces are available. At stage \(i\) in \(p_k\), pair *every currently available face* \(F\) not containing edge \(i\) with \(F\cup\{i\}\), provided the latter is also currently available; remove both from the pool. Each pair is a codimension-one face relation. The three fixed permutations are:

```text
k=2: 5 11 1 9 6 8 2 0 4 3 7 10
k=3: 4 6 0 1 2 9 10 5 8 3 7 11
k=4: 1 4 9 6 5 8 10 7 3 0 2 11
```

In each case the empty face is paired with a singleton. Remove just that one pair from the augmented matching, and restrict to the ordinary nonempty face poset; the singleton becomes a critical vertex. The complete outputs are:

| Threshold | Nonempty faces | Matched pairs | Critical vertices | Other critical cells | Nonempty cover relations |
| --- | ---: | ---: | ---: | --- | ---: |
| \(k=2\) | 44 | 19 | 1 | five of dimension 1 | 72 |
| \(k=3\) | 600 | 295 | 1 | nine of dimension 3 | 2,184 |
| \(k=4\) | 2,664 | 1,331 | 1 | one of dimension 5 | 13,884 |

For the acyclicity certificate, orient every cover relation \(F\prec G\) downward, except that each matched cover is oriented upward. The executable verifier constructs **every** such directed cover and removes zero-indegree vertices until no vertices remain. The number removed equals the number of nonempty faces in all three cases, so the directed Hasse diagrams are acyclic. In particular, the claimed critical-cell data are exact. This finite DAG check, together with the complete enumeration and explicit matching recipe, proves existence of the required acyclic discrete-Morse matchings, rather than relying on sampling.

By Forman's discrete Morse theorem, the realization of each \(X_k\) is homotopy equivalent to a CW complex with precisely the critical cells in the table. A CW complex with one zero-cell and only \(b\) further cells of a single positive dimension \(d\) is a wedge of \(b\) copies of \(S^d\): when \(d\geq2\), every attaching map lands in the sole zero-cell, and when \(d=1\) both endpoints attach there. This proves the three asserted homotopy equivalences. There is a four-edge perfect matching in the cube, so for \(k\geq5\) every edge subset is permitted and \(X_k\) is the full eleven-simplex. At \(k=1\), only the empty face is permitted. As the nonzero reduced integral homology degrees for successive thresholds differ, every inclusion between adjacent nontrivial stages induces the zero map in each positive degree, giving exactly the stated barcode.

## Verification

The included standalone scripts `verify_morse.py` and `verify_mod2.py` require only Python 3 and its standard library. Execute them from their directory using `python3 verify_morse.py` and `python3 verify_mod2.py`. Their full recorded output appears in `morse_output.txt` and `mod2_output.txt`.

The first script independently enumerates all disjoint-edge matchings as a check on its recursive matching-number computation, verifies the complete face counts, constructs each explicitly specified matching, and tests all directed cover relations for acyclicity. Its terminal assertion is `ALL_CHECKS_PASS`. The second script uses a different, vertex-based matching-number recurrence and direct boundary-matrix reduction over \(\mathbb F_2\), obtaining reduced Betti ranks \(5\) in degree \(1\), \(9\) in degree \(3\), and \(1\) in degree \(5\) at the respective thresholds, with all other reduced Betti ranks zero; its terminal assertion is `INDEPENDENT_MOD2_CHECKS_PASS`. The finite-field calculation is corroboration; the integral homotopy statement follows from the acyclic Morse certificates.

## Relationship to prior work

Linusson, Shareshian and Welker [1] proved that for complete bipartite graphs \(K_{r,s}\), the complex \(\operatorname{NM}_k(K_{r,s})\) is a wedge of \(\binom{r-1}{k-1}\binom{s-1}{k-1}\) spheres of dimension \(2k-3\). Their formula yields sphere multiplicities \(9,9,1\) for \(K_{4,4}\) at \(k=2,3,4\) but does not apply to the proper matching-deleted spanning subgraph \(Q_3\), whose first multiplicity is different. Holmsen and Lee [2] proved the general bipartite Leray vanishing bound; this does not determine the cube's exact low-degree homology or CW attaching maps. Shan and Wang [3] prove injection of the top-degree homology under bipartite edge addition and identify cycle examples; in particular their theorem provides valuable nonvanishing comparisons, but not the three exact homotopy equivalences of the cube's entire filtration. The ordinary matching complex of the cube uses *pairwise disjoint edge sets as faces*, and the bounded-degree two-matching complex imposes *vertex degree at most two*; neither is the non-matching complex of this result.

## Limitations

The theorem treats the eight-vertex cube, equivalently the four-crown graph, not all hypercubes or all crown graphs. It does not provide an equivariant homotopy equivalence, a general closed formula for matching-deleted complete bipartite graphs, or classification of the maps on higher homotopy groups between filtration stages. The novelty assessment is based on inspected named results and accessible records, not an exhaustive guarantee that no equivalent unpublished or unindexed computation exists. Independent mathematical review has not been performed.

## References

1. S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first posted 2004-10-15, Theorem 1.4 and Section 4.2. https://arxiv.org/abs/math/0410345
2. A. F. Holmsen, S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first posted 2020-03-25, Theorems 1.1–1.2 and Section 4.3. https://arxiv.org/abs/2003.11270
3. J. Shan, Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621, first posted 2026-09-02, Theorems 2.1–2.3. https://arxiv.org/abs/2609.02621
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (standard discrete-Morse CW theorem).
