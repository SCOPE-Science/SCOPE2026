# Six extremal rank-deletion codes in the six-letter alternating-permutation class

## Finding
Let \(A\) be the 61 permutations \(p=(p_1,\ldots,p_6)\) of \(\{1,\ldots,6\}\) satisfying \(p_1<p_2>p_3<p_4>p_5<p_6\). Let \(D(p)\) be the set of rank-standardized permutations obtained by deleting one coordinate of \(p\). A code \(C\subseteq A\) corrects one such deletion when \(D(p)\cap D(q)=\varnothing\) for every distinct \(p,q\in C\).

The maximum cardinality is **exactly 11**; there are **exactly six** labeled maximum codebooks. Their intersection consists of the seven permutations `153426`, `153624`, `351426`, `351624`, `354612`, `561324`, `563412`. Under simultaneous positional reversal and value complementation \(p\mapsto (7-p_6,\ldots,7-p_1)\), four optimal codebooks are fixed and the remaining two are exchanged, so there are **five** symmetry orbits.

The six codebooks, listed with one six-digit permutation per entry, are:

1. `132546 153426 153624 162534 342516 351426 351624 354612 362514 561324 563412`
2. `132546 153426 153624 162534 342615 351426 351624 354612 362415 561324 563412`
3. `132546 153426 153624 231645 263415 351426 351624 354612 362514 561324 563412`
4. `132546 153426 153624 261534 263415 342615 351426 351624 354612 561324 563412`
5. `132546 153426 153624 261534 263514 342516 351426 351624 354612 561324 563412`
6. `132645 153426 153624 231546 263415 351426 351624 354612 362514 561324 563412`

## Assumptions and scope
Each symbol is labeled and every source has six distinct values. The codewords are *not* identified under symbol relabeling; the only symmetry quotient mentioned is the simultaneous reversal-complement involution. Deletion removes exactly one coordinate, and the five surviving values are standardized in increasing-value order to \(1,2,3,4,5\), so receiver symbols are relative ranks, not original absolute labels. Each deletion deck is a **set**, rather than a multiset: repeated outcomes are deduplicated. Only the up-down orientation displayed above is included.

## Proof
This is a finite exhaustive theorem with a complete independently executable combinatorial enumeration. First enumerate the \(6!=720\) permutations in lexicographic order and retain exactly those with alternating strict adjacent comparisons. The deterministic source predicate returns 61 items, in agreement with the classical Euler zigzag count. For each retained permutation and each of the six deletion positions, remove that position and replace each surviving entry \(x\) by \(1+\#\{y:y<x\}\). This generates its complete set \(D(p)\), including deduplication.

Define the **confusability graph** \(G\) on the 61 sources by placing an undirected edge between distinct sources when their deletion decks intersect. Exact pairwise intersection creates 480 edges. As a separate cross-check, start with each of the \(5!=120\) possible received words, insert each of the six possible new values at each of the six positions, and retain resulting parents in \(A\). Joining every pair of distinct eligible parents reconstructs exactly the same 480-edge graph. The two definitions generate precisely the same collisions because deleting and standardized inserting are inverse operations.

A correcting code is exactly an independent set of \(G\), equivalently a clique in its simple complement \(H\). The embedded `checker.py` applies the following exhaustive Bron–Kerbosch recursion to \(H\), whose adjacency masks are 61-bit integers. For current clique \(R\), candidate vertices \(P\), and already processed vertices \(X\), terminate and record \(R\) if \(P\cup X\) is empty; otherwise choose any pivot \(u\in P\cup X\) maximizing \(|P\cap N_H(u)|\) and recursively extend \(R\) by each vertex in \(P\setminus N_H(u)\), moving that vertex from \(P\) to \(X\) after its recursive call. No size cutoff or sample restriction is applied. The standard clique-extension invariant proves every maximal clique is reported exactly once: a maximal clique containing \(R\) has an unprocessed extension in \(P\), and it must intersect \(P\setminus N_H(u)\) unless the pivot already belongs to it, in which case the pivot itself is that extension when in \(P\). Cases previously handled are excluded through \(X\).

The exhaustive maximal-clique size histogram is:

| Cardinality | Number of maximal compatible codebooks |
|---:|---:|
| 6 | 777 |
| 7 | 10,498 |
| 8 | 16,495 |
| 9 | 5,033 |
| 10 | 393 |
| 11 | 6 |

These 33,202 maximal sets exhaust all possibilities. Every clique is contained in some maximal clique in a finite graph, so the histogram proves the upper bound 11 and the existence of exactly six equality cases. Each recorded equality case is explicitly rechecked for pairwise disjoint deletion decks. Their intersection is the seven-element set in the statement. The reversal-complement map preserves the alternating constraints and all deck collisions; applying it to each optimum yields four fixed codebooks and one swapped pair.

## Verification
Run `python3 checker.py` with Python 3 and no third-party packages. The script reconstructs both collision graphs, performs the unpruned exhaustive maximal-clique traversal, confirms the exact histogram and all six encoded equality cases, directly tests each equality case's disjointness, finds their common core, and checks the symmetry orbit calculation. It prints `VERIFY_OK` only if all assertions pass. Enumeration is finite and complete; unlike sampling, the recursion covers the entire 61-vertex graph. The graph-generation and enumeration algorithms are specified here to make the computation inspectable.

## Relationship to prior work
Gabrys, Yaakobi, Farnoud, Sala, Bruck and Dolecek (2014) define the same **rank-standardized** deletion channel, establish deletion/insertion equivalence, and construct correcting codes using the signatures of a permutation and its inverse. Their Construction 1, restricted to the fixed alternating signature here, already provides a class of size **11** through an inverse-signature VT syndrome. This lower bound is **prior coverage**, not a novelty claim. In fact codebook 3 in the above list is one such syndrome class. The contribution here is the **sharp upper bound** on the alternating source language and the **complete six-codebook equality classification**, including the seven-word forced intersection and the reversal-complement orbit count. The inspected full 2014 article does not state those restricted finite claims; its asymptotic unrestricted upper bound does not imply them.

## Limitations
This is a theorem for the specified six-coordinate constrained class, not a claim for all alternating permutation lengths, both orientations jointly, multiple deletions, or symbol-preserving rather than rank-standardized reads. Its finite exhaustive proof depends on the fully disclosed checker and the standard completeness invariant of the maximal-clique algorithm, not an independent proof assistant or an external independent audit. Prior unindexed finite code tables could contain an equivalent equality classification; that priority risk remains. The verified online-availability day associated with the antecedent article is an author's public upload on April 14, 2015; its 2014 conference date is distinct and has not been used as a day-verified public-availability date.

## References
1. R. Gabrys, E. Yaakobi, F. Farnoud, F. Sala, J. Bruck, L. Dolecek, *Single-Deletion-Correcting Codes over Permutations*, IEEE International Symposium on Information Theory (2014), pp. 2764–2768, DOI: 10.1109/ISIT.2014.6875337. Open full text: https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf
2. Author-upload metadata (April 14, 2015) associated with the same article: https://www.researchgate.net/publication/269272026_Single-deletion-correcting_codes_over_permutations
