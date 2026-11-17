# Five-point metric rigidity and eighty-one congruence classes in the regular 24-cell

## Finding

Let \(C\subset\mathbb R^4\) be a regular 24-cell and \(V(C)\) its set of 24 vertices with the **Euclidean chord metric**. For any two five-element subsets \(A,B\subseteq V(C)\), **every distance-preserving bijection** \(f:A\to B\) is the restriction of a Euclidean symmetry \(g\) of \(C\). In particular, five-vertex subsets are Euclidean-congruent if and only if a symmetry of the 24-cell maps one to the other.

There are exactly **81** congruence classes of unordered five-vertex subsets: **49** consist of affinely independent sets (vertex-supported four-simplices), and **32** consist of affinely dependent sets. For the concrete radius-two coordinate realization
\[
V=\{\pm2e_1,\ldots,\pm2e_4\}\;\cup\;\{(\varepsilon_1,\ldots,\varepsilon_4):\varepsilon_i\in\{-1,1\}\},
\]
the complete orbit census, grouped by absolute edge determinant, is

| Absolute determinant | Symmetry orbits | Five-vertex subsets |
| ---: | ---: | ---: |
| 48 | 1 | 48 |
| 40 | 1 | 96 |
| 32 | 4 | 1,152 |
| 24 | 7 | 3,936 |
| 16 | 21 | 13,776 |
| 8 | 15 | 11,328 |
| 0 | 32 | 12,168 |
| **Total** | **81** | **42,504** |

The orbit-size spectrum is: 39 orbits of size 576, 15 of size 288, 12 of size 1,152, four each of sizes 96, 192 and 144, two of size 48, and one of size 72. The accompanying `orbit_catalogue.tsv` gives one representative of every class, its ten canonical squared distances, its orbit size and its number of internal metric automorphisms.

## Assumptions and scope

The metric is the inherited Euclidean **distance between vertices**, not shortest-path distance along edges. Symmetry means an isometry of the ambient Euclidean four-space preserving \(C\); orientation-reversing symmetries are included. Five-element subsets are unordered, while the extension assertion allows **any specified bijection** preserving all ten pairwise distances. The theorem does not assert the analogous extension property for arbitrary cardinalities or for deformed 24-cells.

All computations below use the displayed radius-two realization. Other congruent or similarly scaled regular 24-cells have the same orbit and extension properties. The determinant column is scale dependent and belongs to this explicit realization only.

## Proof

**1. The full symmetry group and distance model.** Let \(H\) be the integer matrix
\[
H=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}.
\]
The three adjacent coordinate transpositions, the sign change in the first coordinate, and \(H/2\) all preserve \(V\) and are orthogonal: \(HH^{\mathsf T}=4I\). Their action on the 24 indexed vertices generates a group \(G\) of exactly 1,152 different permutations. The standard full symmetry group of the regular 24-cell is the order-1,152 Coxeter group \(W(F_4)\); consequently these explicitly constructed symmetries exhaust it. Every squared distance in \(V\) is one of \(4,8,12,16\).

**2. Exhaustive orbit and metric-signature classification.** Index \(V\) by listing \(\pm2e_i\) in increasing coordinate order (negative first), then the sixteen sign vectors in lexicographic order with \(-1<1\). Enumerate all \(\binom{24}{5}=42,504\) increasing index quintuplets \(I\). The orbit of \(I\) is exactly \(\{\operatorname{sort}(g(I)):g\in G\}\). On discovering a set not already covered, construct this orbit and mark all its elements as covered. The completely specified integer checker reproduces 81 disjoint orbits covering all 42,504 sets; its determinant stratification is the table above.

For any five-tuple of vertex indices \(I\), define its canonical metric signature by lexicographically minimizing the list of its ten squared pairwise distances over all \(5!=120\) orderings of its indices:
\[
\sigma(I)=\min_{\pi\in S_5}\big(\|v_{i_{\pi(1)}}-v_{i_{\pi(2)}}\|^2,\ldots,\|v_{i_{\pi(4)}}-v_{i_{\pi(5)}}\|^2\big),
\]
with entries taken in lexicographic pair order. Exact evaluation for all 81 orbit representatives yields **81 pairwise different signatures**. Because the signature is constant on Euclidean isometry types, no two separate symmetry orbits are congruent. Thus the 81 orbits are exactly the 81 metric congruence classes, not merely 81 classes under a possibly smaller group.

**3. Extend the chosen *map*, not just the underlying set.** For each representative \(I=(i_1,\ldots,i_5)\), the checker constructs the full intrinsic metric automorphism group
\[
\operatorname{Aut}_{\rm met}(I)=\{\pi\in S_5:\|v_{i_j}-v_{i_k}\|^2=\|v_{i_{\pi(j)}}-v_{i_{\pi(k)}}\|^2\ \forall j,k\}.
\]
Independently it constructs all permutations of \(I\) induced by group elements \(g\in G\) with \(g(I)=I\). These two sets of permutations agree **exactly for each of the 81 representatives**. This verifies surjectivity of the natural set-stabilizer restriction map, including its possible nontrivial kernel for affinely dependent configurations.

Now let \(f:A\to B\) preserve distances. The signature classification supplies \(g_0\in G\) taking \(A\) onto \(B\). Then \(g_0^{-1}\circ f\) is an intrinsic metric automorphism of \(A\). Transport the corresponding representative's verified stabilizer equality to \(A\): there exists \(h\in G\) stabilizing \(A\) and restricting to \(g_0^{-1}\circ f\). Hence \(g_0h\in G\) restricts to **the prescribed bijection** \(f\), establishing the stronger extension property.

**4. Independent orbit-total check.** For any \(g\in G\) with cycle lengths \(c_1,\ldots,c_s\) in its 24-point action, the number of fixed five-element subsets equals
\[
[z^5]\prod_{j=1}^s(1+z^{c_j}).
\]
Computing this coefficient by an exact five-entry integer recurrence and summing over the group gives \(93,312\). Burnside's formula therefore gives \(93,312/1,152=81\) orbits, matching the direct orbit partition. This cross-check does not replace the signature and stabilizer checks needed for metric extension.

All finite verification steps are executable as standalone standard-library Python code in `verify.py`. It uses only integer arithmetic, finite permutations, and explicit assertions. The 81 full representatives and canonical signatures are printed in the accompanying catalogue, which the checker regenerates and compares byte-for-byte.

## Verification

Run `python3 verify.py` from the package directory without Python's assertion-disabling optimization option. The expected terminal line is:

`24_CELL_FIVE_POINT_METRIC_RIGIDITY_PASSED group=1152 sets=42504 orbits=81 spanning=49 degenerate=32 distinct_signatures=81 burnside_sum=93312 strong_extension=81`

The checker verifies group closure and every group element's distance preservation on all vertex pairs, counts every five-subset once, produces the full orbit partition, confirms distinct canonical ten-distance signatures, and compares **all** metric automorphisms with the induced set-stabilizer restrictions at all 81 orbit representatives. It separately reconstructs the Burnside count from cycle decompositions and checks the catalogued orbit sizes and determinant stratification. This is an exact exhaustive finite proof contingent on the transparent checker implementation; no floating-point sampling is used.

## Relationship to prior work

Whitehead's Wythoff classification supplies the regular-polytope and Coxeter-group framework for the 24-cell, including the distinction between a regular polytope's global symmetry and configurations of arbitrary subsets. Simon and Timofeyev study inscribed polytopal partitions with prescribed symmetry, not the metric automorphisms of five-element subsets of the fixed 24-cell.

The closest published same-body calculation, *Exact largest-simplex volume and equality classification in the regular 24-cell*, already establishes the **complete seven-level absolute-determinant count** and the single orbit of the 48 maximum-volume five-root subsets, as well as an equality theorem for continuously inscribed simplices. Those facts are **not new here**. The determinant count in the table above is used only as a consistency test, after accounting for the different coordinate scale. A determinant class can split into many metric classes: in particular, the zero-determinant class splits into 32 different metric classes. The new assertion is the **81-class complete Euclidean classification and extension of every prescribed local five-point isometry to a global symmetry**, which the cited determinant count or regularity of the polytope does not imply.

## Limitations

The theorem addresses the exact regular 24-cell's 24 Euclidean vertices and subsets of cardinality five. The computation proves a finite classification, not a general result about every Coxeter orbit, every subset size, the graph shortest-path metric, or any stability of the property under geometric deformation. Historical priority remains provisional: a classical Coxeter orbit table or unindexed five-point configuration census might contain an equivalent statement. Neither the complete determinant spectrum nor mere polytope flag-transitivity is sufficient to establish the claimed metric extension property. Independent mathematical audit has not been performed.

## References

Spencer Whitehead, *Classifying Regular Polyhedra and Polytopes using Wythoff's Construction*, arXiv:2001.09364v1, first made public 2020-01-25, https://arxiv.org/abs/2001.09364.

Steven Simon and Tobias Timofeyev, *Inscribed Tverberg-Type Partitions for Orbit Polytopes*, arXiv:2110.09322v1, first made public 2021-10-18, https://arxiv.org/abs/2110.09322.

*Exact largest-simplex volume and equality classification in the regular 24-cell*, published scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-largest-simplex-volume-and-equality-classification-in-the--bda0674b8ea5 (full `RESULT.md` compared for statement-level overlap).

H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The D4 root system is not universally optimal*, arXiv:math/0607447, first made public 2006-07-19, https://arxiv.org/abs/math/0607447 (spherical-configuration context; distinct optimization problem).
