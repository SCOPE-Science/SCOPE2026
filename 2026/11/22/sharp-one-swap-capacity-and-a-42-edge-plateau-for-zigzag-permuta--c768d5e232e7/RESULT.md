# Sharp one-swap capacity and a 42-edge plateau for zigzag permutation codes

## Finding

A zigzag permutation alternates between rises and descents in successive positions. A rank-modulation communication channel that permits either no change or exactly one swap of consecutive positions can correct a code precisely when all distinct source codewords have Kendall--\(\tau\) distance at least three.

**Theorem.** For every integer \(n\ge1\), let \(\mathcal Z_n\) contain every permutation of \(\{1,\ldots,n\}\) with alternating adjacent comparisons, starting with either a rise or a descent. Write \(M_n\) for its maximum one-swap-correcting code cardinality and \(N_n\) for the number of labeled codebooks attaining that maximum. Let \(E_n\) be the classical Euler zigzag number for one orientation. Then:

| Length \(n\) | Source size | Confusable pairs | \(M_n\) | \(N_n\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 1 | 1 |
| 2 | 2 | 1 | 1 | 2 |
| 3 | 4 | 4 | 2 | 2 |
| 4 | 10 | 10 | 5 | 4 |
| 5 | 32 | 22 | 16 | 9,216 |
| 6 | 122 | 42 | 80 | \(2^{42}\) |
| 7 | 544 | 42 | 502 | \(2^{42}\) |
| 8 | 2,770 | 0 | 2,770 | 1 |

For **every** \(n\ge8\), the complete zigzag source is itself one-swap-correcting, so \(M_n=2E_n\) and \(N_n=1\). The distance between the two opposite zigzag orientations is sharply bounded, for every \(n\ge2\), by

\[
\min_{\pi\in\mathcal U_n,\ \sigma\in\mathcal D_n}d_K(\pi,\sigma)=\left\lceil\frac{n-1}{3}\right\rceil.
\]

The length-six and length-seven confusability graphs are respectively \(42K_2\sqcup38K_1\) and \(42K_2\sqcup460K_1\): both therefore have exactly \(2^{42}=4,398,046,511,104\) maximum codebooks. Thus length eight is the first length for which no zigzag source word must be removed, and the same 42 pairwise ambiguities persist at two consecutive smaller lengths.

## Assumptions and scope

For each length at least two, \(\mathcal U_n\) is the set of one-line permutations \(\pi\) with \(\pi_1<\pi_2>\pi_3<\cdots\), and \(\mathcal D_n\) has the reversed adjacent inequalities. They are disjoint and \(\mathcal Z_n=\mathcal U_n\cup\mathcal D_n\). The singleton at length one has no comparison orientation and is counted once. The Euler zigzag number \(E_n\) counts each orientation; in particular \(E_2,\ldots,E_8=1,2,5,16,61,272,1385\).

The Kendall--\(\tau\) distance \(d_K(\pi,\sigma)\) is the smallest number of swaps of *adjacent positions* transforming \(\pi\) to \(\sigma\), or equivalently the count of unordered label pairs having opposite relative orders. Every possible received permutation of length \(n\) is permitted, whether or not it is a zigzag. Therefore two radius-one output sets intersect if and only if the two source permutations are at Kendall distance at most two. The **confusability graph** has all words in \(\mathcal Z_n\) as vertices and such pairs as edges; a correcting code is exactly an independent set. A labeled codebook is a literal set of permutations, without quotienting by symmetries.

## Proof

**1. Words in the same orientation have distance at least three.** For a single adjacent swap, the comparison between the swapped elements reverses, so the result cannot have the original complete up--down sign pattern. Two swaps at the same position cancel. If two swaps at disjoint positions differ by at least two in index, at least one of their central comparison signs is reversed and cannot be repaired by the other swap. If the two swaps are on neighboring position pairs, they cyclically reorder three elements: one resulting outer comparison is necessarily the reverse of the original outer comparison in any strict alternating triple. Hence two *different* permutations with the same zigzag orientation require at least three adjacent swaps. This rules out all within-orientation edges.

**2. Sharp cross-orientation bound for all lengths.** One adjacent swap can affect only the comparison at its central index and the two immediately neighboring comparison indices: at most three signs in all. The sign strings of \(\mathcal U_n\) and \(\mathcal D_n\) are opposite at every one of the \(n-1\) positions. Therefore every path between them in the adjacent-transposition Cayley graph takes at least \(\lceil(n-1)/3\rceil\) swaps.

To attain the bound, for \(n\equiv1\pmod3\) choose swap centers (one-based) \(2,5,8,\ldots,n-2\); for \(n\equiv0\) or \(2\pmod3\) choose centers \(1,4,7,\ldots\) up to \(n-1\). These positions are separated by three, and their comparison windows together cover all \(n-1\) comparisons. Prescribe alternating up--down inequalities on a tuple of distinct placeholders \(a_1,\ldots,a_n\). Independently prescribe opposite down--up inequalities on the tuple after swapping the two placeholders at each chosen center. A swap at an interior center imposes four-place inequalities, whose union is acyclic: for a peak centered at the left swapped position, its two unswapped outer placeholders both lie strictly between the smaller and larger swapped placeholders; for a valley, reverse all inequalities. A first- or last-pair swap similarly imposes an acyclic three-place chain, or a two-place inequality when \(n=2\). Consecutive local constraint systems share at most one placeholder (because centers are three apart) and no other positions overlap, so gluing their directed acyclic inequality graphs cannot introduce a directed cycle. Topologically order all placeholders and assign the distinct integers \(1,\ldots,n\) in that order. This gives a permutation in \(\mathcal U_n\) which becomes one in \(\mathcal D_n\) by exactly the prescribed \(\lceil(n-1)/3\rceil\) adjacent swaps. The argument applies also at \(n=2,3\). A second constructive algorithm is in `witness.py`.

For \(n\ge8\), the cross-orientation lower bound is at least three, and Step 1 gives the same within either orientation. Thus the full \(\mathcal Z_n\) is correcting. No code can contain more than all its source words, and a maximum of that size is uniquely the entire source. This proves the all-length part.

**3. Finite exact classification of the remaining lengths.** For \(1\le n\le7\), enumerate the permutations of \(\{1,\ldots,n\}\), retain exactly those with alternating comparisons, construct the complete output ball consisting of the input and every single adjacent-position swap, and join precisely those pairs appearing in a common output ball. This enumerates *every* vertex and *every* edge of the finite confusability graph. A separate implementation checks all pairwise Kendall inversion distances directly, not via ball intersection.

At \(n=3\) the graph is \(C_4\); its maximum independent-set size is two and it has two maxima. At \(n=4\) it is one ten-vertex ten-edge connected component with exactly four maximum independent sets of size five. At \(n=5\) it is
\[
6K_2\ \sqcup\ 2P_4\ \sqcup\ 2P_6.
\]
The maximum sizes for \(K_2,P_4,P_6\) are respectively \(1,2,3\), with respectively \(2,3,4\) maximizers, giving
\[
M_5=6+2\cdot2+2\cdot3=16,\qquad N_5=2^6\cdot3^2\cdot4^2=9,216.
\]
At length six, the output-ball computation gives 42 edges, none sharing an endpoint, and exactly 38 isolated vertices. The 42 edges are contributed by the unordered pairs of swap centers \((1,4),(2,4),(2,5)\), respectively with multiplicities \(12,18,12\). At length seven, 42 edges again have disjoint endpoints, all arising from centers \((2,5)\), and there are 460 isolates. Each isolated vertex belongs to every maximum independent set and one endpoint of each separate edge must be chosen; hence
\[
M_6=38+42=80,\quad M_7=460+42=502,\quad N_6=N_7=2^{42}.
\]
For lengths one and two, direct enumeration yields one singleton or one edge; the length-three and four assertions above complete the finite range. `verify.py` includes a full exact component-by-component independent-set enumeration for dimensions one through five and checks every claimed edge, component and matching size through dimension eight.

## Verification

All computations are over exact finite integers and require only Python's standard library, version 3.9 or later. In a directory containing the provided artifacts run:

```sh
python3 verify.py
python3 alternate.py
python3 witness.py
```

`verify.py` independently generates the zigzag words, generates every radius-one received word, assembles every collision edge, enumerates all independent subsets of every small connected component, validates the length-six and length-seven matching decomposition and swap-center counts, and checks all 80 and 502 supplied optimum codewords in `optimal_6.txt` and `optimal_7.txt`. Its completed execution ends `VERIFY_OK`. `alternate.py` computes Kendall inversion distance directly on all cross- and within-orientation pairs through length seven, independently reconstructing the conflict counts and matching property; it ends `ALTERNATE_OK`. `witness.py` algorithmically constructs the sharp opposite-orientation paths by topological ordering and checks the construction for all lengths from two through one hundred; it ends `WITNESS_OK`. Finite witness tests are corroboration rather than a proof of the all-length statement, which follows from Step 2.

The two text files list explicit maximum codebooks for dimensions six and seven, respectively, one permutation per line. No solver, API, database, or external software package is necessary.

## Relationship to prior work

Barg and Mazumdar's 2009 theory and the later rank-modulation constructions of Mazumdar, Barg and Zémor study Kendall-error-correcting codes over the unrestricted permutation space. Buzaglo and Etzion's perfect-code and general bounds papers likewise address unrestricted permutation spheres and bounds. None of these inspected formulations determines a maximum inside the union of the two alternating-permutation families, let alone the finite equality-case counts or the first length where the full zigzag source corrects one swap. The classical Euler zigzag count supplies \(E_n\), but it is a source-enumeration identity rather than a distance bound.

Related public results on Kendall codes in \(S_5\) optimize over all 120 permutations, while a study of a zigzag-fence *linear-extension exchange graph* counts swaps that retain one fixed fence orientation. Neither implication provides the present cross-orientation confusability graph, independent-set classification, or matching plateau. A separate public analysis of an “alternating permutation codebook” uses even-parity permutation matrices for Fourier recovery, not the up--down pattern restriction used here. Equivalent unindexed work remains a historical-priority risk.

## Limitations

The all-length capacity and uniqueness claim concerns only correcting **at most one adjacent-position swap**, with unrestricted received permutations. It does not establish correction of multiple swaps, other error models, or general optimal codes in the full symmetric group. The numerical optimal-codebook counts at small lengths follow from exhaustive exact finite search, not an explicit formula for all possible suboptimal codebooks. The displayed 42-edge plateau is specific to lengths six and seven, while the sharp opposite-orientation distance theorem applies to all lengths. No independently performed scientific audit is asserted.

## References

1. Alexander Barg and Arya Mazumdar, “Codes in Permutations and Error Correction for Rank Modulation,” arXiv:0908.4094 (first posted 2009-08-27), https://arxiv.org/abs/0908.4094.
2. Arya Mazumdar, Alexander Barg and Gilles Zémor, “Constructions of Rank Modulation Codes,” arXiv:1110.2557 (2011), https://arxiv.org/abs/1110.2557.
3. Shlomo Buzaglo and Tuvi Etzion, “Perfect Permutation Codes with the Kendall's \(\tau\)-Metric,” arXiv:1310.5515 (2013), https://arxiv.org/abs/1310.5515.
4. Shlomo Buzaglo and Tuvi Etzion, “Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric,” arXiv:1408.4963 (2014), https://arxiv.org/abs/1408.4963.
5. OEIS A000111, Euler zigzag numbers, https://oeis.org/A000111.
6. “Equality census for optimal \(S_5\) Kendall--\(\tau\) codes at distance \(3\),” public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-equality-census-for-optimal-s-5-kendall-tau-codes-at-distance-3--01233b6e774d.
7. “A parity law for least-mobile fence linear extensions,” public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-parity-law-for-least-mobile-fence-linear-extensions--54fe743aae41.
