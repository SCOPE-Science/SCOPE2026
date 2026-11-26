# Sharp one-swap capacity and a 42-edge plateau for zigzag permutations

## Finding

Let \(\mathcal Z_n\) be the set of permutations of \(\{1,\ldots,n\}\) whose adjacent comparisons alternate, starting with either a rise or a descent. The length-one singleton is counted once. Write \(M_n\) for the maximum one-swap-correcting code cardinality in \(\mathcal Z_n\), and \(N_n\) for the number of labeled codebooks attaining it. The finite cases are:

| \(n\) | Source size | Confusable pairs | \(M_n\) | \(N_n\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 1 | 1 |
| 2 | 2 | 1 | 1 | 2 |
| 3 | 4 | 4 | 2 | 2 |
| 4 | 10 | 10 | 5 | 4 |
| 5 | 32 | 22 | 16 | 9,216 |
| 6 | 122 | 42 | 80 | \(2^{42}\) |
| 7 | 544 | 42 | 502 | \(2^{42}\) |
| 8 | 2,770 | 0 | 2,770 | 1 |

For every \(n\ge8\), the whole source is one-swap-correcting, so \(M_n=2E_n\) and \(N_n=1\), where \(E_n\) is the Euler zigzag number for one orientation. The first conflict-free length **among \(n\ge2\)** is eight; the singleton at \(n=1\) is already conflict-free. For every \(n\ge2\), with \(\mathcal U_n\) the rise-first orientation and \(\mathcal D_n\) the descent-first orientation,
\[
\min_{\pi\in\mathcal U_n,\,\sigma\in\mathcal D_n}d_K(\pi,\sigma)=\left\lceil\frac{n-1}{3}\right\rceil.
\]
At lengths six and seven the confusability graphs are \(42K_2\sqcup38K_1\) and \(42K_2\sqcup460K_1\), respectively. Both give \(2^{42}=4{,}398{,}046{,}511{,}104\) maximum codebooks.

## Assumptions and scope

The channel either leaves the permutation unchanged or swaps one pair of adjacent **positions**; every received permutation is allowed, not just zigzags. The Kendall distance \(d_K\) is the number of unordered labels with reversed relative order, equivalently the minimum number of adjacent-position swaps. Two radius-one balls meet exactly when their centers have distance at most two: for distance two use the middle step of a shortest path. Thus correcting codes are independent sets in the graph joining distinct zigzag permutations at distance at most two. Labeled codebooks are literal sets of permutations; no symmetries are quotiented out. The two comparison orientations are disjoint for \(n\ge2\).

## Proof

**Same orientation.** A single swap reverses its central comparison. Two swaps of the same pair cancel. For disjoint pairs, the reversed central comparisons persist. For neighboring pairs, the two swaps cycle a triple: with \(a<b>c\), the rotation \((b,c,a)\) starts with a descent, and \((c,a,b)\) ends with a rise. Both fail the original pattern, and reversing all inequalities gives the other case. Thus distinct words of one orientation have distance at least three.

**Opposite orientations.** Each swap affects at most three comparison positions, but the two sign strings differ everywhere. Thus distance is at least \(\lceil(n-1)/3\rceil\). For equality, number the center of a swap of positions \(k,k+1\) by \(k\). If \(n\equiv1\pmod3\), choose centers \(2,5,\ldots,n-2\); otherwise choose \(1,4,7,\ldots\) up to \(n-1\). They are spaced by three, their comparison windows cover \(1,\ldots,n-1\), and their number is \(\lceil(n-1)/3\rceil\).

Impose rise-first comparisons on distinct placeholders before the chosen swaps and descent-first comparisons after them. For an interior center with a peak at its left swapped position, the swapped peak must exceed both unswapped outer placeholders, which must both exceed the swapped valley. Those inequalities are jointly acyclic. Reverse them for a valley. At the first or last center there is only one outer placeholder, producing a chain; at length two there is just the inequality between the two swapped placeholders. Consecutive systems share at most one placeholder, with no overlap with non-neighbors. Gluing acyclic directed graphs along this chain cannot create a directed cycle: adding the next system through one vertex permits no return path through new vertices without revisiting that vertex. A topological order assigns distinct labels \(1,\ldots,n\) satisfying all comparisons. This realizes the lower bound. For \(n\ge8\) the opposite-orientation bound is at least three, and the same-orientation bound also applies. The full source is then the unique maximum code.

**Finite graph.** Enumerate permutations, retain the alternating sign strings, and join each pair whose unchanged-or-single-swap output lists intersect. This gives a complete graph census; computing pair-order discrepancies gives a separate exact check. For \(n=1,2,3\) the graphs are \(K_1,K_2,C_4\). At \(n=4\) there is one connected ten-vertex, ten-edge component with four maximum independent sets of size five. At \(n=5\) the components are \(6K_2\sqcup2P_4\sqcup2P_6\). Exhausting independent subsets of these paths gives sizes \(1,2,3\) and counts \(2,3,4\) respectively, yielding \(M_5=16\) and \(N_5=2^6\,3^2\,4^2=9,216\). At \(n=6\) the 42 edges are disjoint and come from center pairs \((1,4),(2,4),(2,5)\) with counts 12, 18 and 12; at \(n=7\) the 42 disjoint edges all come from \((2,5)\). Each maximum codebook contains every isolate and one endpoint of each edge. This gives capacities \(38+42=80\) and \(460+42=502\), respectively, and \(2^{42}\) maximum codebooks at each length. In particular, all lengths two through seven have a conflict.

## Verification

With Python 3.9 or later and the supplied text files, run `python3 verify.py`, `python3 alternate.py` and `python3 witness.py`. The first enumerates all finite output-ball intersections, graph components and small independent subsets, checks the matchings and center counts at six and seven, and validates the optimum codebooks in `optimal_6.txt` and `optimal_7.txt`. The second computes Kendall inversion distances directly through length seven. The third constructs and checks examples attaining the opposite-orientation distance bound through length 100; the all-length proof is the inequality-graph argument, not this bounded test. The respective completion markers are `VERIFY_OK`, `ALTERNATE_OK` and `WITNESS_OK`.

## Relationship to prior work and limitations

Classical Kendall-code work studies the unrestricted symmetric group [1–4], and Euler zigzag numbers count each orientation [5]. The unrestricted \(S_5\) census [6] does not give the equality census on this constrained source. A fence linear-extension swap graph [7] uses legal exchanges within the extensions of one fixed poset, rather than overlapping radius-one balls on the union of the two zigzag orientations. The present contribution is the sharp cross-orientation distance, the resulting conflict-free threshold for \(n\ge2\), and the exact small constrained graph census. It is limited to at most one adjacent-position error with unrestricted received permutations. No multi-swap or unrestricted code-size theorem is asserted.

## References

1. A. Barg and A. Mazumdar, *Codes in Permutations and Error Correction for Rank Modulation*, https://arxiv.org/abs/0908.4094.
2. A. Mazumdar, A. Barg and G. Zémor, *Constructions of Rank Modulation Codes*, https://arxiv.org/abs/1110.2557.
3. S. Buzaglo and T. Etzion, *Perfect Permutation Codes with the Kendall's \(\tau\)-Metric*, https://arxiv.org/abs/1310.5515.
4. S. Buzaglo and T. Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*, https://arxiv.org/abs/1408.4963.
5. OEIS A000111, Euler zigzag numbers, https://oeis.org/A000111.
6. *Equality census for optimal \(S_5\) Kendall–\(\tau\) codes at distance 3*, Resultary, `SCOPE-equality-census-for-optimal-s-5-kendall-tau-codes-at-distance-3--01233b6e774d`.
7. *A parity law for least-mobile fence linear extensions*, Resultary, `SCOPE-a-parity-law-for-least-mobile-fence-linear-extensions--54fe743aae41`.
