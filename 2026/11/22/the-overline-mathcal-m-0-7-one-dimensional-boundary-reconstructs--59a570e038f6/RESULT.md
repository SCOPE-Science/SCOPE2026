# The one-dimensional boundary of \(\overline{\mathcal M}_{0,7}\) reconstructs seven-point Frobenius

## Finding

Let \(k=\mathbb F_q\) be any finite field, and let \(E/k\) be a finite étale algebra of degree seven. Via the Frobenius action on the seven geometric embeddings of \(E\), form the permutation-twisted variety \(X_E\) of the labelled stable-curve compactification \(\overline{\mathcal M}_{0,7}\). Let \(\mathcal B_1(E)\) be the finite étale \(k\)-scheme whose geometric points index the one-dimensional boundary strata of \(X_E\), i.e. the strata of stable seven-marked rational curves whose marked dual trees have three internal edges. Let \(\mathcal B_0(E)\) index the zero-dimensional boundary strata (four internal edges).

**Theorem.** For all such \(k\) and \(E\):

1. \(\mathcal B_1(E)\) has \(1260\) geometric points. Its complete finite-set zeta function distinguishes all fifteen partitions of seven, hence determines the Frobenius cycle partition of \(E\). In fact, the five integers
   \[
   \bigl(\#\mathcal B_1(E)(\mathbb F_{q^r})\bigr)_{r=1}^{5}
   \]
   already determine that partition.
2. The bound five is sharp **for consecutive extension degrees starting at one**. The three partitions \((7)\), \((5,2)\), and \((5,1,1)\) all yield zero points in \(\mathcal B_1(E)(\mathbb F_{q^r})\) for \(1\leq r\leq4\), whereas their degree-five counts are respectively \(0\), \(210\), and \(1260\).
3. By contrast, \(\mathcal B_0(E)\), with \(945\) geometric points, has only eleven distinct complete Frobenius cycle spectra across the fifteen partitions. Exactly four pairs of distinct partitions have identical \(\mathcal B_0\)-zeta functions:
   \[
   \begin{gathered}
   (6,1)\sim(3,2,2),\qquad (4,2,1)\sim(4,1,1,1),\\
   (3,3,1)\sim(3,1,1,1,1),\qquad (2,2,2,1)\sim(2,2,1,1,1).
   \end{gathered}
   \]

These assertions concern **finite schemes indexing geometric boundary strata**; they do not assert corresponding counts of rational points lying *on* the positive-dimensional strata.

## Assumptions and scope

All fields have positive prime-power cardinality, with no characteristic restriction. A finite étale algebra \(E\) of degree seven is equivalent to a seven-element continuous Frobenius set and has one of the fifteen cycle partitions of seven. Every partition is realized by an algebra of the form \(\prod_i\mathbb F_{q^{d_i}}\), with \(\sum_i d_i=7\). The construction is descent of the usual label-permutation action on stable rational curves, not a classification of arbitrary unmarked moduli forms or curves in the strata.

The zero-dimensional strata correspond to trivalent unrooted trees with seven labelled leaves and four internal edges. One-dimensional strata correspond to stable unrooted trees with seven labelled leaves and three internal edges: one internal vertex is four-valent and the others trivalent. A labelled internal edge is encoded by the unordered two-partition of leaves it separates, with both blocks of size at least two.

## Proof

**(I) Complete combinatorial parametrization.** There are exactly \(56\) permissible unordered two-partitions of the seven labels. Encode a partition by the smaller of the two complementary seven-bit masks. Two internal-edge splits \(A|A^c\) and \(B|B^c\) are compatible exactly when at least one of the four intersections \(A\cap B\), \(A\cap B^c\), \(A^c\cap B\), \(A^c\cap B^c\) is empty. Every pairwise compatible family of permissible splits uniquely specifies a stable labelled tree: this is the standard split-tree correspondence, also verified here by the independent edge-insertion construction below. A family of three splits indexes a one-dimensional stratum; four splits index a point stratum.

**(II) Exact totals.** A trivalent seven-leaf tree can be constructed uniquely by adding leaves successively to internal or external edges, so there are
\[
(2\cdot7-5)!!=945
\]
maximal trees. Every such tree has four internal edges that can be contracted. Conversely each one-dimensional stable tree has one four-valent vertex, which has precisely three binary resolutions. Counting pairs consisting of a trivalent tree and a chosen internal edge gives
\[
\#\mathcal B_1(\overline k)=\frac{945\cdot4}{3}=1260.
\]
The included checker independently enumerates all three-split and four-split compatible families and all trivalent trees formed by successive leaf insertion; the two constructions coincide exactly.

**(III) Frobenius enumeration.** The label-permutation action on stable trees is the action on their unordered internal-edge splits. All conjugacy classes of \(S_7\) are indexed by the fifteen integer partitions of seven. For each partition, take the canonical disjoint-cycle representative and apply it to every compatible three-split system. Decompose the resulting permutation on \(1260\) systems into cycles of lengths \(d\), with multiplicities \(c_d\). The finite étale zeta function and extension counts are then
\[
Z_{\mathcal B_1(E)}(T)=\prod_{d\geq1}(1-T^d)^{-c_d},\qquad
\#\mathcal B_1(E)(\mathbb F_{q^r})=\sum_{d\mid r}d\,c_d.
\]
This formula holds for every finite field, because the action is entirely combinatorial and Galois descent uses the same Frobenius permutation.

Here is the complete first-five-count certificate (the complete orbit-length table is in `CERTIFICATE.json`):

| Partition | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 |
|---|---:|---:|---:|---:|---:|
| \((7)\) | 0 | 0 | 0 | 0 | 0 |
| \((6,1)\) | 1 | 3 | 22 | 3 | 1 |
| \((5,2)\) | 0 | 0 | 0 | 0 | 210 |
| \((5,1,1)\) | 0 | 0 | 0 | 0 | 1260 |
| \((4,3)\) | 1 | 3 | 4 | 15 | 1 |
| \((4,2,1)\) | 2 | 48 | 2 | 1260 | 2 |
| \((4,1,1,1)\) | 4 | 48 | 4 | 1260 | 4 |
| \((3,3,1)\) | 3 | 3 | 1260 | 3 | 3 |
| \((3,2,2)\) | 3 | 15 | 48 | 15 | 3 |
| \((3,2,1,1)\) | 3 | 15 | 210 | 15 | 3 |
| \((3,1,1,1,1)\) | 15 | 15 | 1260 | 15 | 15 |
| \((2,2,2,1)\) | 22 | 1260 | 22 | 1260 | 22 |
| \((2,2,1,1,1)\) | 48 | 1260 | 48 | 1260 | 48 |
| \((2,1,1,1,1,1)\) | 210 | 1260 | 210 | 1260 | 210 |
| \((1,1,1,1,1,1,1)\) | 1260 | 1260 | 1260 | 1260 | 1260 |

The fifteen rows are pairwise distinct. The first four columns cannot distinguish the three zero-four-prefix partitions, proving sharpness. Repeating the identical orbit calculation on four-split systems yields eleven spectra and the four collisions stated above. This is a finite **exhaustive proof of a fixed fifteen-class assertion**, not extrapolation from selected finite-field experiments.

## Verification

Run `python3 verify_boundary7.py > reproduced.json`, then compare `reproduced.json` to `CERTIFICATE.json` byte-for-byte. No dependencies beyond the Python standard library are required. The checker constructs all \(56\) splits, all \(945\) fully trivalent trees, all \(1260\) one-dimensional strata, all fifteen Frobenius types, and their two exact permutation cycle spectra. It asserts the equality of two independent tree-enumeration methods and all reconstruction and sharpness claims. The attached complete JSON table explicitly records every one-dimensional and zero-dimensional orbit-length multiplicity, along with fixed counts in degrees one through five.

## Relationship to prior work

Maya and Mostovoy (2019) explain stable-curve strata using marked-leaf trees and leaf-forgetting operations. Castravet and Tevelev (first publicly posted 2020) establish deeper symmetric-group equivariance of \(\overline{\mathcal M}_{0,n}\) and its Grothendieck-group representation. Documentation for `admcycles` independently tabulates the geometric counts \(1260\) and \(945\) at seven markings. These geometric descriptions and equivariant structures supply the setting, but **do not state the fifteen-case Frobenius orbit classification, the five-degree reconstruction theorem, or the contrast with zero-dimensional strata**. In particular a permutation representation on Grothendieck groups does not by itself identify the independent boundary-stratum permutation character.

## Limitations

The result concerns the finite étale **index schemes**, not the number of rational points on the one-dimensional boundary curves themselves, not the zeta function of the full twisted moduli space, and not an isomorphism classification of seven-pointed rational curves. The optimality assertion applies only to initial consecutive extension degrees. An equivalent one-dimensional-boundary class-character table might exist in older equivariant stable-graph or permutation-character literature; the sources inspected here did not settle that bibliographical possibility. Independent mathematical validation has not been performed.

## References

1. J. Maya and J. Mostovoy, *Simplicial equations for the moduli space of stable rational curves*, first public 2019-06-12, arXiv:1906.05223, https://arxiv.org/abs/1906.05223.
2. A.-M. Castravet and J. Tevelev, *Derived category of moduli of pointed curves -- II*, first public 2020-02-07, arXiv:2002.02889, https://arxiv.org/abs/2002.02889 (the accessible HTML revision is dated 2026-06-27, not the first public date).
3. `admcycles` documentation, `decorated_graph.stable_graphs`, genus-zero seven-marked enumeration, https://fchapoton2.gitlab.io/admcycles/decorated_graph.html.
