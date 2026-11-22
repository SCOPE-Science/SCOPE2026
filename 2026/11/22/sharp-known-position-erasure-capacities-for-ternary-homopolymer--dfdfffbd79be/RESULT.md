# Sharp known-position erasure capacities for ternary homopolymer-free words of lengths five and seven

## Finding

Let \(S_n=\{w\in\{0,1,2\}^n:w_i\ne w_{i+1}\text{ for }1\le i<n\}\). Let \(E_n\) be the largest size of a code \(C\subseteq S_n\) that permits unique recovery after any **one erasure with its coordinate known to the receiver**. The exact values at the two stated lengths are

\[
E_5=23,\qquad E_7=92.
\]

There are \(48\) valid length-five words and \(192\) valid length-seven words. In particular, at length seven the elementary half-size estimate \(96\) is not attained: the actual deficit is four codewords. These are optimal finite lengths; no extrapolation to general odd length is asserted.

## Assumptions and scope

The alphabet is precisely \(\{0,1,2\}\); the source word has exactly \(n\) symbols; equal neighbors are forbidden only in the **source**, not in received data. Exactly one coordinate is erased, and the receiver learns its index. The code must distinguish every pair of distinct codewords for every erased index. No edit, substitution, burst, unknown-position deletion, or synchronization guarantee is asserted.

For words \(u,v\) of the same length, let \(d_H(u,v)\) be their Hamming distance. Unique reconstruction under a known erasure is equivalent to \(d_H(u,v)\ge2\) for all distinct codewords. Let \(G_n\) have vertex set \(S_n\) and join two words exactly when their Hamming distance is one. Thus \(E_n=\alpha(G_n)\), its ordinary independence number. The same graph is the **labeled** three-colouring reconfiguration graph of the path on \(n\) vertices; the three colors are not identified modulo permutations.

## Proof

First, choosing the initial symbol in three ways and each next symbol in two ways proves \(|S_n|=3\cdot2^{n-1}\).

The files `cert5.json` and `cert7.json` each contain three finite lists: `codewords`, `odd_cycles` (ordered around their cycles), and `paired_edges`. In each case the lists of cycles and edges are pairwise vertex-disjoint, cover every element of \(S_n\) exactly once, and each consecutive pair in every cyclic list (including its last-to-first pair) differs in exactly one position. Both endpoints of each paired edge likewise differ in exactly one position. These properties are checked directly by `verify.py` and, using a different integer state representation, by `alternate.py`.

For length seven, `cert7.json` contains eight cycles each on \(21\) vertices and twelve additional disjoint edges. No independent set contains more than \(10\) vertices from a \(21\)-cycle, or more than one endpoint of an edge. Summing upper bounds across the **vertex partition** yields

\[
\alpha(G_7)\le8\cdot10+12=92.
\]

Its `codewords` field lists exactly \(92\) distinct admissible words, with pairwise Hamming distance at least two. Therefore \(E_7=92\).

Similarly, `cert5.json` contains two vertex-disjoint \(15\)-cycles and nine disjoint edges that together cover all \(48\) valid words. Hence

\[
\alpha(G_5)\le2\cdot7+9=23.
\]

The listed set of \(23\) admissible, pairwise distance-at-least-two words meets the upper bound, proving \(E_5=23\). All uses of finite checking in this argument are exhaustive over explicitly enumerated sets, not probabilistic or asymptotic.

## Verification

With Python 3 and the four auxiliary files in the same directory, run `python3 verify.py` and `python3 alternate.py`. Both are standard-library-only. The first independently enumerates \(S_n\) via a Cartesian alphabet product, checks all pairwise code distances, checks every consecutive edge of every cycle and every matching edge, verifies disjoint exact coverage of the full source set, and computes the upper bound. The second enumerates base-three integer states, checks unique punctured-coordinate observations, reconstructs and checks every covering edge, and confirms that the cover accounts for every valid word without repetition.

Expected terminal lines are `VERIFY_OK` and `ALTERNATE_OK`. No mixed-integer solver, numerical floating-point bound, cryptographic commitment, or unpublished data is required to validate the certificates. The data files are literal finite witnesses, not a compressed search transcript.

## Relationship to prior work

Choo and MacGillivray (published online 28 March 2011) define precisely the labeled proper-coloring reconfiguration graph used here, and their Theorem 5.5 proves that the three-coloring reconfiguration graph of any tree other than an odd star is Hamiltonian. Their result covers both path lengths. A Hamiltonian graph on \(192\) vertices has independence number at most \(96\), but Hamiltonicity alone does **not** imply the exact bound \(92\); for example, the cycle on \(192\) vertices is Hamiltonian and has independence number \(96\). The distinct odd-cycle partition and corresponding sharp code witness address a different objective and yield a strictly stronger bound for this specific graph. No claim to novelty of Hamiltonicity, of the recoloring graph definition, or of its elementary half-size bound is made.

Benerjee and Banerjee (2023) define homopolymer-free codes with minimum Hamming distance, and derive general bounds by sphere packing and Gilbert–Varshamov methods. Their inspected mathematical definitions and derived bounds do not state the two exact ternary distance-two capacities or the odd-cycle certificates here. Haas and MacGillivray (2018) study canonical coloring graphs that identify color-permutation equivalence classes, a different graph from the labeled-coloring graph studied here.

## Limitations

The results concern exactly lengths five and seven, ternary words, adjacent-inequality source constraints, and one erasure at a known coordinate. The certificates do not prove the number of optimal codebooks, any large-length formula, or correction of an erasure whose location is unknown. Prior literature searching cannot exclude every unindexed independent computation. The correctness check is reproducible and finite; an independent mathematical audit has not been carried out.

## References

1. K. Choo and G. MacGillivray, *Gray code numbers for graphs*, Ars Mathematica Contemporanea 4 (2011), 125–139, first published online 28 March 2011. https://scispace.com/pdf/gray-code-numbers-for-graphs-3yxrthhv40.pdf . See the definitions of coloring graphs and Theorem 5.5.
2. K. G. Benerjee and A. Banerjee, *Bounds on Size of Homopolymer Free Codes*, arXiv:2305.10741, first posted 18 May 2023. https://arxiv.org/abs/2305.10741 . See the HF-code definition and general bounds.
3. R. Haas and G. MacGillivray, *Connectivity and Hamiltonicity of Canonical Colouring Graphs of Bipartite and Complete Multipartite Graphs*, Algorithms 11 (2018), 40, published 29 March 2018. https://www.mdpi.com/1999-4893/11/4/40 .
