# Reversal symmetry costs two sensors on the ternary length-three de Bruijn network

## Finding

Let \(\Sigma=\{0,1,2\}\) and let \(G\) be the simple undirected de Bruijn graph with vertex set \(V=\Sigma^3\). Two distinct words are adjacent when one is obtained from the other by deleting its first letter and appending a letter, or by deleting its last letter and prepending a letter. For \(v=abc\), its closed radius-one ball is
\[
B(v)=\{abc\}\cup\{xab:x\in\Sigma\}\cup\{bcx:x\in\Sigma\}.
\]
For \(C\subseteq V\), define \(I_C(v)=C\cap B(v)\). An identifying code is a set \(C\) such that the \(27\) sets \(I_C(v)\) are nonempty and pairwise different. Write \(r(abc)=cba\) for word reversal. A reversal-invariant identifying code satisfies \(r(C)=C\).

The minimum unrestricted identifying-code size is \(9\), as previously reported in the literature. The exact number of labeled nine-sensor codes is \(4{,}366\). Under the natural action of the six alphabet permutations and word reversal, they form exactly \(372\) classes: one class of size \(4\), fifteen of size \(6\), and \(356\) of size \(12\).

**The reversal-invariant minimum is \(11\), two sensors greater than the unrestricted minimum.** Exactly \(117\) reversal-invariant eleven-sensor codes attain this bound. Under the same natural symmetry group, these form \(22\) classes, five of size \(3\) and seventeen of size \(6\). In particular, none of the \(4{,}366\) unrestricted optimal nine-sensor codes is reversal-invariant.

Explicit unrestricted optimum:

`000 001 002 011 112 120 122 210 221`

Explicit reversal-invariant eleven-sensor optimum:

`000 012 021 022 101 102 111 120 201 210 220`

The files `optimal_orbits.tsv` and `symmetric_orbits.tsv` give one lexicographically canonical representative for every class under the stated natural group.

## Assumptions and scope

All words are labeled, indexed, length-three ternary words. Edges are undirected and repeated arcs/loops are discarded; closed balls retain the center. The identification radius is exactly one. Alphabet relabelings act uniformly in all coordinates, and word reversal acts by reversing all three coordinates. The symmetry-class counts refer to the specified group \(S_3\times C_2\), not necessarily the entire automorphism group of \(G\).

## Proof

List \(V\) lexicographically as \(v_0,\ldots,v_{26}\). Form the integer neighborhood masks
\[
b_i=\sum_{j:\,v_j\in B(v_i)}2^j,
\]
and the mask \(m(C)=\sum_{j:\,v_j\in C}2^j\). The integer \(b_i\mathbin{\&}m(C)\), where \(\&\) denotes bitwise AND, represents exactly \(I_C(v_i)\). Consequently, \(C\) is identifying if and only if its \(27\) signature masks are all nonzero and pairwise distinct. This criterion is equivalent to the mathematical definition, including for words with equal letters and repeated shift neighbors.

The standalone exhaustive enumerators `verify.py` and `verify_alt.cpp` construct these neighborhoods directly from the graph definition. They inspect all \(\binom{27}{8}=2{,}220{,}075\) eight-subsets and all \(\binom{27}{9}=4{,}686{,}825\) nine-subsets, finding respectively \(0\) and \(4{,}366\) identifying codes. Since adding sensors cannot destroy the identifying property, the absence of an eight-sensor code excludes all smaller codes. The displayed nine-sensor code supplies the attaining upper bound.

The involution \(r\) has exactly nine fixed vertices of the form \(aba\) and nine two-element orbits on the remaining vertices. Thus every reversal-invariant set is a union of a subset of exactly \(18\) specified orbits. Enumeration of **all** \(2^{18}=262{,}144\) orbit selections, with their actual sensor cardinalities, yields no identifying set of size at most \(10\), and exactly \(117\) at size \(11\). The displayed reversal-invariant eleven-sensor set attains the lower bound. This exhausts the possibilities: the orbit construction is a bijection between invariant subsets and selections of those \(18\) orbits.

Finally, apply all \(12\) transformations arising from alphabet permutations and reversal to every attaining code. Every transformation preserves adjacency, closed balls, identifying codes, code size, and (for an invariant code) reversal invariance. Taking the lexicographically least bitmask of the resulting orbit gives a unique canonical representative for each class. Exhaustive canonicalization gives the orbit-size distributions above; independently, the sizes sum to \(4+15\cdot6+356\cdot12=4{,}366\) and \(5\cdot3+17\cdot6=117\). The two lists of representatives, checked against the regenerated populations, supply an explicit classification under the stated symmetry group.

## Verification

Run `python3 verify.py` in the directory containing the two TSV files. It uses only the Python standard library and independently constructs neighborhoods, enumerates combinations and reversal-orbit selections, and checks both canonical-representative files. Its expected last token is `VERIFY_OK`.

Independently, compile and execute `verify_alt.cpp` using `g++ -std=c++17 -O3 verify_alt.cpp -o verify_alt && ./verify_alt`. It uses an integer-bitmask combination successor rather than Python combinations, and directly checks the numerical unrestricted and reversal-invariant counts. Its expected last token is `ALTERNATE_OK`.

Both independent implementations were run successfully from the packaged source contents. The certificate is a finite exhaustive computation, not an asymptotic argument.

## Relationship to prior work

Horan, Adachi and Bak, *A Comparison of Approaches for Solving Hard Graph-Theoretic Problems*, arXiv:1504.08011, first submitted 2015-04-29, already give the minimum sizes \(4\) for the binary length-three case and \(9\) for the ternary length-three case in their Tables/Figures 8 and 9. They discuss generating all satisfying models but do not report the number or symmetry types of minimum ternary placements, nor the optimum under word reversal. Those previously known minimum sizes are therefore used as context, not claimed as discoveries.

Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403, first submitted 2015-08-03, establishes identifiability in broad parameter ranges, including this graph; its conclusions leave minimum-size and construction questions open in general. Work on directed de Bruijn identifying codes has different directed-neighborhood constraints. Other finite censuses of identifying codes in binary de Bruijn networks and Kautz graphs concern different graphs or parameters. None of those known claims mathematically determines these two populations, the reversal-invariance cost, or the natural-group orbit counts.

## Limitations

The exhaustive theorem is specific to the ternary alphabet, word length three, closed radius-one undirected neighborhoods, and the stated symmetry group. It makes no claim about larger graphs, other sensing radii, the full graph automorphism group, or independent mathematical validation. The priority assessment is based on inspected primary text and indexed searches; unindexed or inaccessible earlier equivalent classifications remain possible.

## References

1. V. Horan, S. Adachi, S. Bak, *A Comparison of Approaches for Solving Hard Graph-Theoretic Problems*, arXiv:1504.08011 (2015), https://arxiv.org/html/1504.08011v2, especially Section 3 and Figures 8–9.
2. V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403 (2015), https://arxiv.org/abs/1508.00403, especially the introduction, Theorem 2.1 and future-work section.
3. D. Boutin, V. Horan Goliber, M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842 (2014), https://arxiv.org/abs/1412.5842.
