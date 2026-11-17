# Integral two-torsion in alternating-permutation word complexes on four and five letters

## Finding

For \(n\in\{3,4,5\}\), let \(A_n\) denote the even permutations of \([n]\). Form the finite regular semisimplicial word complex \(X(A_n)\): its \(k\)-cells are the injective words of length \(k+1\) that occur as ordered subsequences of at least one permutation in \(A_n\); the \(i\)-th face deletes the \(i\)-th letter. Its geometric realization has the following **complete reduced integral homology**:

\[
\begin{aligned}
\widetilde H_j(X(A_3);\mathbb Z)&\cong
\begin{cases}\mathbb Z,&j=1,\\0,&j\ne1;\end{cases}\\
\widetilde H_j(X(A_4);\mathbb Z)&\cong
\begin{cases}\mathbb Z^3\oplus\mathbb Z/2,&j=2,\\0,&j\ne2;\end{cases}\\
\widetilde H_j(X(A_5);\mathbb Z)&\cong
\begin{cases}\mathbb Z^{16}\oplus(\mathbb Z/2)^4,&j=3,\\0,&j\ne3.\end{cases}
\end{aligned}
\]

Moreover, \(X(A_4)\) is simply connected and \(X(A_5)\) is \(2\)-connected. The torsion occurs in their first potentially nonzero reduced homology, not in their fundamental groups. In particular neither complex is a wedge of spheres or a pure shellable complex. No complete homotopy decomposition is claimed.

## Assumptions and scope

The parity is that of the full length-\(n\) permutation; it is **not** the parity of a shorter subword. The semisimplicial cells distinguish different orderings of the same underlying set. All homology coefficients above are over the integers; the result is not a mod-two-only calculation. The three finite values \(n=3,4,5\) are exhaustive within the stated claim; no formula for arbitrary \(n\) is asserted. The barycentric subdivision of this regular cell structure agrees with the usual order-complex definition of a permutation complex.

## Proof

**1. All lower cells occur.** For each injective word of length \(n-1\), insert its one missing letter into consecutive positions. The resulting two full permutations have opposite parity; hence at least one belongs to \(A_n\). Every shorter injective word extends to a word of length \(n-1\). Consequently \(X(A_n)\) and the full injective-word complex \(\operatorname{Inj}([n])\) have exactly the same \((n-2)\)-skeleton. The latter is homotopy equivalent to a wedge of \((n-1)\)-spheres by the Björner–Wachs theorem, so the shared skeleton is \((n-3)\)-connected. Adding only top cells preserves that connectivity.

**2. Exact cellular differential.** Put \(C_{k-1}=\mathbb Z[W_k]\), where \(W_k\) is the set of all admitted length-\(k\) words. In this word basis the differential is
\[
\partial_{k-1}(a_1\cdots a_k)
=\sum_{i=1}^{k}(-1)^{i-1}a_1\cdots\widehat{a_i}\cdots a_k.
\]
In particular, enumerating all even permutations and their subsequences gives, in increasing word length, cellular ranks \((3,6,3)\), \((4,12,24,12)\), and \((5,20,60,120,60)\) for \(n=3,4,5\), respectively.

**3. Exact integral reduction.** Apply integer elementary row and column operations to the top boundary matrices. A reproducible deterministic elimination (the accompanying `check_alternating_words.py`) repeatedly selects the first entry \(+1\) or \(-1\) in row-major order in the remaining block, swaps it into the pivot position, and eliminates entries below it. Such operations are unimodular. The top matrices have, respectively, \(3,11,56\) unit pivots. The residual block is zero for \(n=3\); for \(n=4,5\), every residual entry is even, and dividing that block by two yields respectively \(1\) and \(4\) further unit pivots, with no remaining nonzero columns. Since the leading unit block splits off integrally, this proves exact top Smith invariants
\[
\begin{array}{c|c}
n&\text{nonzero Smith diagonal}\ \\ \hline
3&1,1,1\\
4&1^{\times11},2\\
5&1^{\times56},2^{\times4}.
\end{array}
\]
Thus every top differential is injective; the top homology vanishes. Because the image of the next lower differential is free abelian, the torsion in its kernel modulo the top-boundary image is exactly the torsion of the full top-boundary cokernel. The top Smith diagonals therefore determine the displayed \(2\)-primary torsion without assuming any homological cancellation.

**4. Free ranks and vanishing.** The ranks of the differentials going from word length two up to the maximal length are, respectively, \((2,3)\), \((3,9,12)\), and \((4,16,44,60)\). Hence the free ranks in the one remaining possible degrees are \(6-2-3=1\), \(24-9-12=3\), and \(120-44-60=16\). Connectivity from Step 1 eliminates all lower reduced homology; injectivity eliminates the top group. Together these steps establish all groups in the finding.

## Verification

The complete computational certificate is the standalone standard-library Python script `check_alternating_words.py`, with recorded deterministic output in `check_output.txt`. It enumerates every relevant ordered face, verifies every consecutive boundary product is zero **over the integers**, checks lower ranks modulo three primes, and carries out exact unimodular integer elimination of each top matrix. The resulting unit/2-unit factors agree with an additional independently implemented Smith-normal-form computation using SymPy. The finite enumeration establishes precisely the stated three cases, not an infinite extrapolation.

## Relationship to prior work

Chachólski–Levi–Meshulam (2019) established general theory of permutation complexes and a distinct 15-permutation complex on four letters realizing a suspension of the projective plane; that generating set is not \(A_4\), and its homotopy statement does not determine the present parity-subgroup complexes. Libman (2023) established contractibility for complexes generated by non-derangements, a different restriction. Govc (2026) proved every permutation complex has free fundamental group; our examples are consistent with this while demonstrating **higher integral torsion** for a natural entire subgroup. Elizalde–Hanlon–Hersh (2026) obtained shellability of several pattern-avoidance complexes; a restriction by total permutation parity is a different construction, and the torsion here excludes an analogous shellability conclusion. The full text of that last comparator could not be obtained in this review, so priority relative to any unindexed special case remains a residual risk.

## Limitations

The result classifies integral homology, not integral homotopy or \(A_n\)-module structures. It proves nothing about \(n\ge6\). The reproducible integer calculations are exact finite calculations, but they have not been independently audited. Inability to inspect the full 2026 pattern-avoidance manuscript and unindexed literature are bibliographic risks, not evidence of novelty.

## References

- W. Chachólski, R. Levi and R. Meshulam, *On the topology of complexes of injective words* (first public version August 9, 2019), https://arxiv.org/abs/1908.03394.
- A. Libman, *The complex of injective words of permutations which are not derangements is contractible* (September 13, 2023), https://arxiv.org/abs/2309.06808.
- S. Elizalde, P. Hanlon and P. Hersh, *Complexes of pattern-avoiding injective words* (October 5, 2026), https://arxiv.org/abs/2610.07303.
- D. Govc, *Fundamental Groups of Permutation Complexes* (November 8, 2026), https://arxiv.org/abs/2611.11362.
- A. Björner and M. Wachs, *On lexicographically shellable posets*, Transactions of the AMS 277 (1983), Theorem 6.1 as cited by the previous papers.
