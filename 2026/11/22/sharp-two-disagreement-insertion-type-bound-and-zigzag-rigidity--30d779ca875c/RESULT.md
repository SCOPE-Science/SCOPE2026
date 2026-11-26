# Sharp two-disagreement insertion-type bound and zigzag rigidity in the homogeneous two-order structure

## Finding

Let the base be \(n\ge2\) individually named points of the generic countable two-order structure. Name the points \(1,\ldots,n\) in the first order, and write their sequence in the second order as \(\pi=(\pi_1,\ldots,\pi_n)\). Let \(c_2(\pi)\) count the complete nonalgebraic one-point types over this base for which the two placements disagree on exactly two of the named points.

The sharp envelope is \(3(n-1)\), the grade-two case of the all-grade upper envelope \((k+1)(n-k+1)\) reported in [1]. The result here is the complete equality classification:

- At \(n=2\), only \(21\) attains the envelope.
- At \(n=3\), exactly \(231,312,321\) attain it.
- At every \(n\ge4\), exactly two patterns attain it, and they are inverse permutations. They are the successor maps of the two orientations of the unique Hamilton cycle in the square of the path on \(1,\ldots,n\). Its cyclic list starts at \(1\), goes through the evens in increasing order, then through the odds greater than \(1\) in decreasing order, and returns to \(1\).

For example, the two patterns are \(2413,3142\) at \(n=4\) and \(24153,31524\) at \(n=5\).

## Assumptions and scope

The structure is the homogeneous limit of all finite structures with two linear orders. The one-point type is for a point distinct from all named base points. Every ordered pair of insertion gaps occurs by the extension property, and ultrahomogeneity identifies all points giving the same pair of gaps over the named base. Thus there are \((n+1)^2\) such types. Put \(P_i=\{1,\ldots,i\}\) and \(Q_j=\{\pi_1,\ldots,\pi_j\}\) for \(0\le i,j\le n\). The discrepancy of gaps \((i,j)\) is \(|P_i\triangle Q_j|\).

## Proof

If this discrepancy is two, then \(|i-j|\le2\) and \(i-j\) is even. The only candidates are \((i,i)\) for \(1\le i\le n-1\) and \((i,i+2),(i+2,i)\) for \(0\le i\le n-2\), giving the envelope \(3(n-1)\). Equality means that all candidates realize discrepancy two.

For the off-diagonal candidates, discrepancy two is equivalent to \(P_i\subseteq Q_{i+2}\) or \(Q_i\subseteq P_{i+2}\), respectively. The first family of inclusions is equivalent to \(\pi^{-1}(v)\le v+2\) for all \(v\); the second is equivalent to \(\pi_t\le t+2\) for all \(t\). For example, the first follows in one direction by taking \(i=v\) for \(v\le n-2\) and is automatic for \(v>n-2\), and in the other direction because \(v\le i\) implies \(\pi^{-1}(v)\le i+2\). Together the off-diagonal conditions say \(|\pi_t-t|\le2\) for all \(t\).

At \((i,i)\), the discrepancy is twice the number of directed edges of the permutation map \(t\mapsto\pi_t\) crossing from \(P_i\) to its complement. The opposite direction has the same number of crossings. Thus the diagonal condition is one crossing each way at each proper prefix cut. In a cycle of the permutation, all cuts between its smallest and largest vertices are crossed at least once in each direction. For two different cycles their intervals of crossed cuts cannot intersect, and they cannot be adjacent: adjacency of their cut intervals would require a shared endpoint vertex. To cover every proper prefix cut there must therefore be one nontrivial cycle, containing \(1\) and \(n\).

For \(n\ge4\) this spanning cycle is not the transposition of \(1\) and \(n\), since their difference exceeds two. If an internal vertex \(j\) were fixed, the spanning cycle would have to pass across \(j\) in both directions. Its only allowed edge over \(j\) joins \(j-1\) and \(j+1\). Using that edge in both directions would form a two-cycle, which is impossible in the spanning cycle of length at least three. Thus there are no fixed points and the spanning cycle is Hamiltonian in the path square.

The path square on \(n\ge3\) vertices has one undirected Hamilton cycle. For \(n=3\) this is the triangle. For \(n\ge4\), vertex \(1\) has neighbors \(2,3\) only; replacing the segment \(2,1,3\) of a Hamilton cycle by the edge \(2,3\) gives a Hamilton cycle on the smaller path square. Conversely every Hamilton cycle of the smaller square contains \(2,3\), since vertex \(2\) in that graph has only neighbors \(3,4\); inserting \(1\) back in the edge is the inverse construction. The stated zigzag is a Hamilton cycle: its edges are all pairs \(\{k,k+2\}\) together with \(\{1,2\}\) and \(\{n-1,n\}\). This edge set crosses each internal cut \(2\le i\le n-2\) twice, via \(\{i-1,i+1\}\) and \(\{i,i+2\}\); it also crosses each end cut twice. Either orientation therefore crosses each cut once each way, and meets all off-diagonal conditions by its jump lengths. Reversing the orientation inverts the successor map.

At \(n=2,3\) the displacement condition is automatic. The diagonal conditions reduce to \(\pi_1\ne1\), and for \(n=3\) also \(\pi_3\ne3\). This gives exactly the stated small cases.

## Verification

The accompanying `verify.py` uses only the Python standard library. Its finite enumeration covers all 409112 permutations of lengths two through nine, compares two evaluations of the statistic through six, and checks both Hamilton cycle orientations through ten. `verification_output.txt` records the output. Run `python verify.py`; the all-size theorem rests on the proof above, not finite extrapolation.

## Relationship to prior work and limitations

The numerical sharp bound and its attainability are covered by the reported all-grade envelope [1] after specializing to \(k=2\); no separate novelty for the exponent or constant, or priority over that record, is claimed. An explicit attaining family at grade two does not by itself classify all maximizers. The additional conclusion proved here is that the crossing condition and the jump-length condition force the complete list of oriented zigzags and small exceptions.

The size-four pair \(2413,3142\) is not offered as a new identification: Cameron [2, p. 5] treats those two patterns under the separate condition that each pair be adjacent in at least one order. Linman–Pinsker [3] give structural context for the random permutation. The conclusion here concerns only exact grade two, over individually named finite bases, and not equality cases at general grades, higher-arity types, or a distribution obtained by sampling base permutations. An equivalent characterization under another formulation may exist.

## References

1. *Sharp all-grade envelopes for one-point disagreement types in the generic permutation*, 2026-11-22, Resultary 5c6744671985. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-all-grade-envelopes-for-one-point-disagreement-types-in-th--5c6744671985
2. P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2), R2 (2002). https://doi.org/10.37236/1674
3. J. Linman and M. Pinsker, *Permutations on the Random Permutation*, Electronic Journal of Combinatorics 22(2), P2.54 (2015). https://arxiv.org/abs/1405.4297
