# Sharp one-swap correction in ternary length-six 2-regular multipermutations

## Finding

Let \(\mathcal W\) be the \(90=6!/(2!)^3\) indexed words of length six over \(\{0,1,2\}\) in which every symbol appears twice. Let \(d_K(u,v)\) be the least number of swaps of unequal adjacent symbols that transforms \(u\) into \(v\). Then

\[
\boxed{\max\{|C|:C\subseteq\mathcal W,\ d_K(u,v)\ge3\ \text{for all distinct }u,v\in C\}=18.}
\]

Equivalently, exactly \(18\) messages can be represented in this fixed-composition source while correcting one arbitrary adjacent transposition of unequal symbols. In the notation of Buzaglo, Yaakobi, Etzion and Bruck, the result is \(A(3,2,3)=18\). A direct construction and an independently checkable rational clique-cover certificate prove both inequalities.

## Assumptions and scope

The alphabet symbols are labeled; the six positions are indexed. All words have composition \((2,2,2)\). One error is the interchange of the symbols at two consecutive positions when those symbols differ. The graph \(G\) has vertex set \(\mathcal W\) and an edge for each such interchange. Its shortest-path metric is \(d_K\). A code corrects zero or one error exactly when its distinct vertices have graph distance at least three. No result is asserted for other alphabets, other compositions, greater lengths, or more errors.

For any \(u\in\mathcal W\), write \(N_{\le2}(u)\) for the vertices at graph distance one or two from \(u\). The *conflict graph* \(H\) joins two distinct vertices precisely when their \(d_K\)-distance is at most two. Thus an error-correcting code is an independent set of \(H\).

## Proof

**Construction.** Begin with the six words

`001122`, `010221`, `011220`, `020211`, `021102`, `021201`.

Apply the three cyclic relabelings \(x\mapsto x+s\pmod3\), for \(s=0,1,2\), to all six words. The result has eighteen distinct words. Directly comparing every pair by the stated adjacency rule gives distance at least three. The complete sorted code is printed by `verify_certificate.py`; `verify_metric.py` separately verifies the same minimum distance using the inversion-number formula.

**Upper-bound method.** A clique of \(H\) contains at most one codeword. Write \(\Gamma=S_3\times C_2\) for the symmetries induced by permuting the three alphabet labels and optionally reversing the six positions. Every group element preserves \(d_K\), and therefore sends a clique to a clique. Define nine clique orbits from the representatives below; assign each distinct clique in the corresponding orbit weight \(a/19\), where \(a\) is the integer numerator in the second column.

| Orbit size | Weight numerator \(a\) | Representative clique (words separated by commas) |
|---:|---:|---|
| 12 | 6 | `001122`, `001212`, `001221`, `002112`, `010212` |
| 6 | 7 | `001122`, `001212`, `010122`, `010212` |
| 12 | 7 | `100221`, `001221`, `010212`, `010221`, `012021` |
| 6 | 6 | `002121`, `020112`, `020121`, `020211`, `021021`, `200121` |
| 6 | 2 | `101220`, `011202`, `011220`, `012120` |
| 6 | 3 | `102120`, `011220`, `012102`, `012120`, `012210`, `021120` |
| 12 | 4 | `102021`, `010221`, `012012`, `012021`, `012201`, `021021` |
| 6 | 5 | `102120`, `102201`, `102210`, `012210`, `120210` |
| 6 | 3 | `102210`, `012120`, `012201`, `012210`, `021210` |

These nine orbits contain \(72\) mutually distinct cliques. All their pairs are edges of \(H\), and the total **integer** weight numerator is

\[
12\cdot6+6\cdot7+12\cdot7+6\cdot6+6\cdot2+6\cdot3+12\cdot4+6\cdot5+6\cdot3=360.
\]

The sum of integer weights over cliques containing any given vertex is at least \(19\). To check every vertex without an implicit probabilistic argument, use the \(11\) orbits of \(\Gamma\) on the \(90\) words. A representative and its coverage numerator are:

| Representative | Coverage numerator |
|---|---:|
| `001122` | 19 |
| `001212` | 19 |
| `001221` | 19 |
| `010212` | 39 |
| `010221` | 19 |
| `011220` | 19 |
| `012012` | 22 |
| `012021` | 19 |
| `012120` | 19 |
| `012201` | 19 |
| `012210` | 19 |

Every coverage is constant within its orbit because the weighted clique collection is \(\Gamma\)-invariant. All table entries can be derived by applying the twelve group operations to the nine short representative cliques; the attached standard-library checker repeats that finite derivation from literal inputs.

For every independent set \(C\) of \(H\), double-counting weighted incidences gives

\[
19|C|\le\sum_{v\in C}\sum_{K\ni v}a_K
=\sum_K a_K|C\cap K|\le\sum_K a_K=360.
\]

Hence \(|C|\le\lfloor360/19\rfloor=18\). Together with the construction this proves the theorem.

## Verification

`verify_certificate.py` is a Python-standard-library, exact integer checker. It enumerates the entire \(90\)-word universe; generates the adjacency graph and its distance-two conflict relation; checks the eighteen-word construction; builds all nine symmetry-orbits of cliques; checks all \(72\) cliques; evaluates the \(90\) vertex coverages; and confirms the weighted numerator \(360\) and minimum coverage \(19\). It also rejects duplicated orbit cliques. Run `python3 verify_certificate.py`.

`verify_metric.py` independently computes all \(90\times90\) distances using breadth-first search and stable-labeled permutation inversion counts, checks their equality, and tests the proposed code directly in the latter metric. Run `python3 verify_metric.py`. Both scripts were executed and passed. Exhaustion is limited to this finite parameter; no infinite-parameter extrapolation is used.

## Relationship to prior work

Buzaglo, Yaakobi, Etzion and Bruck's 2013 paper explicitly defines \(A(m,r,d)\) in the same metric. Its Section IV numerical table gives the upper bounds \(30\) and \(34\) for \(A(3,2,3)\), not its exact value; the present result sharpens those particular bounds to \(18\). Their paper supplies the model and related inequalities but does not imply the new equality. The January 2013 publication date is given only to month precision at the Caltech repository; its original deposit datestamp is day-verified as February 15, 2013.

Related exact results on Ulam, Hamming and one-deletion codes on the same composition have different confusability relations. In particular, a reported eighteen-word optimum for single-deletion correction is not a statement about, or a certificate for, the Kendall-distance-three problem. Other published exact codes for ordinary permutations do not automatically imply this value for 2-regular multipermutations. Comparisons and unresolved priority risks are documented in `AUDIT.json`.

## Limitations

This finite classification determines the maximum **size**, not the number or orbit types of all maximum codes. The finite certificate proves the optimum only at composition \((2,2,2)\) and distance three. Priority searches cannot exclude uncatalogued independent prior computations. Independent mathematical audit has not been performed.

## References

1. S. Buzaglo, E. Yaakobi, T. Etzion, J. Bruck, *Error-Correcting Codes for Multipermutations*, CaltechAUTHORS ETR122, repository record initial datestamp 2013-02-15, https://authors.library.caltech.edu/records/ft4vp-ka042 ; full technical report https://www.paradise.caltech.edu/papers/etr122.pdf ; IEEE ISIT 2013 proceedings, https://doi.org/10.1109/ISIT.2013.6620321.
2. F. Farnoud and O. Milenkovic, *Multipermutation Codes in the Ulam Metric for Nonvolatile Memories*, initial preprint 2013-12-08, https://arxiv.org/abs/1312.2163.
3. R. A. Brualdi and G. Dahl, *Multipermutations and Stirling Multipermutations*, 2024, https://doi.org/10.1007/s00373-024-02751-2 (structural background; does not assert the coding optimum).
