# Complete two-rainbow independent domination census of the Petersen graph

## Finding
Let \(P=\operatorname{KG}(5,2)\) denote the Petersen graph, whose ten vertices are the two-element subsets of \([5]\), with disjointness as adjacency. A two-rainbow independent dominating function is a map \(f:V(P)\to\{0,1,2\}\) such that the vertices bearing label \(1\), respectively \(2\), are independent and every vertex bearing label \(0\) has a neighbor with label \(1\) and a neighbor with label \(2\). Its weight is the number of nonzero labels. The complete polynomial of **named-color** functions is
\[
R_P(z)=\sum_{f\text{ feasible}}z^{|f^{-1}(1)|+|f^{-1}(2)|}=30z^6+80z^7.
\]
Moreover, the \(110\) feasible functions form exactly five orbits under \(\operatorname{Aut}(P)\cong\mathfrak S_5\), one orbit of size \(30\) at weight \(6\) and four orbits of size \(20\) at weight \(7\). Every optimum is a pair of edge-disjoint triangles in \(K_5\) meeting in exactly one *ground vertex*. Thus the previously known minimum weight \(6\) has exactly \(30\) named-color optimizers.

## Assumptions and scope
The Petersen graph is simple and unweighted. Colors \(1\) and \(2\) are distinct, so exchanging them ordinarily produces a different function. For \(i=1,2\), let \(A_i=\{e\in\binom{[5]}2:f(e)=i\}\); write \(Z=\binom{[5]}2\setminus(A_1\cup A_2)\). Since adjacency in \(P\) means edge-disjointness in \(K_5\), independence of the two color classes means each \(A_i\) is a pairwise-intersecting edge family of \(K_5\). The zero condition means that for every \(e\in Z\), each of \(A_1,A_2\) contains an edge disjoint from \(e\).

## Proof
**Intersecting-family lemma.** A nonempty family of pairwise-intersecting edges of \(K_5\) of size at least three is either a three- or four-edge star or a triangle. Indeed, if all edges share a common endpoint, the family is a star of size at most four. If not, three pairwise-intersecting edges without a common endpoint must be precisely the three edges of a triangle, and no further edge meets all three. In particular the independent-set size of \(P\) is four.

**Small-color exclusion.** Let \(A\) be either nonzero color class. Define its intersection transversal \(T(A)=\{e\in\binom{[5]}2:e\cap a\ne\varnothing\text{ for every }a\in A\}\). An edge \(e\in T(A)\) is not adjacent in \(P\) to any color-\(A\) vertex; hence it cannot be zero. As \(A\) itself is intersecting, the entire set \(T(A)\setminus A\) must be colored with the *other* color and must consequently be intersecting. If \(|A|=1\), this forced other-color set contains two disjoint edges, and if \(A=\{ab,ac\}\), it contains the disjoint edges \(ad\) and \(bc\), with \(d\) outside \(\{a,b,c\}\). Thus \(|A|\ge3\). Neither color can be empty: otherwise an uncolored vertex lacks that color, while coloring all ten with the other color violates independence. Both classes therefore have size three or four. Two four-edge stars at distinct centers share the joining edge, and cannot be disjoint. Hence the only possible weights are six and seven.

**Exact classification.** There are three possible independent-family types of size at least three: \(3S\) (three-edge star), \(3T\) (triangle), and \(4S\) (full four-edge star). Their complete admissible ordered-pair census is

| Type of \(A_1\) | Type of \(A_2\) | Count | Weight |
|---|---|---:|---:|
| \(3T\) | \(3T\) | 30 | 6 |
| \(3S\) | \(4S\) | 20 | 7 |
| \(4S\) | \(3S\) | 20 | 7 |
| \(3T\) | \(4S\) | 20 | 7 |
| \(4S\) | \(3T\) | 20 | 7 |

To prove the table without relying on computation, first suppose \(A_1\) is the star centered at \(a\) with leaves \(b,c,d\) and missing spoke \(ae\). Its transversal is the complete star centered at \(a\), so \(ae\) must belong to \(A_2\). A three-star centered at \(e\) would leave one missing spoke forced into \(A_1\), an impossibility; a triangle containing \(ae\) would contain an edge of \(A_1\); all other stars containing \(ae\) also conflict with \(A_1\). Thus \(A_2\) is exactly the full star centered at \(e\), yielding \(5\cdot4=20\) choices.

If \(A_1\) is the complete star centered at \(a\), the other class must have three edges, all among the remaining four ground vertices. It can be any of the four three-stars or any of the four triangles on those four vertices: \(5\cdot(4+4)=40\) possibilities, split into \(20\) of each type. All their uncolored edges have an edge-disjoint witness in each color.

Finally suppose \(A_1\) is the triangle on ground set \(U\), with \(|U|=3\). The other class can be a full star centered at either of the two points outside \(U\), giving \(\binom53\cdot2=20\) cases, or another triangle meeting \(U\) in exactly one point, giving \(\binom53\cdot3=30\) cases. A three-star cannot work: if its center is in \(U\) it would overlap the first triangle or have fewer than three available spokes; if its center is outside \(U\), its missing spoke belongs to \(T(A_2)\setminus A_2\) yet cannot belong to \(A_1\). The uncolored edges in both allowed types again have disjoint witnesses in each color. This exhausts all cases and proves \(R_P(z)=30z^6+80z^7\).

**Orbits.** A permutation of the five ground points induces an automorphism of \(P\). Every admissible type above is one orbit under this action: an ordered pair of stars is specified by its ordered centers, a triangle–full-star pair by its triangle and an outside center, and an ordered triangle pair by its unique common ground point and a partition of the remaining four points into two named pairs. The five type counts are their orbit sizes. The graph automorphism group equals \(\mathfrak S_5\): its five maximum independent sets are exactly the four-edge stars and their pairwise intersections recover the ten vertices. Thus there are no additional orbit mergers, and the five displayed orbits are the complete automorphism-orbit classification.

## Verification
Two standalone Python 3 programs accompany this result. Run `python3 checks/direct_ternary.py` and `python3 checks/independent_family_census.py`. The former checks each of the \(3^{10}=59049\) ternary assignments directly against adjacency and computes the ground-permutation orbits. The latter enumerates all \(75\) nonempty pairwise-intersecting edge families and tests ordered disjoint pairs using an independent edge-mask implementation. Both yield identical complete feasibility-membership SHA-256 values: `9b0ed36c88e965202e95769ae99bad5673ac9d9bd0b3ecb0e1910e9aa8648087`. The scripts use only the Python standard library. They are exact exhaustive finite cross-checks; the structural proof above establishes the result independently.

## Relationship to prior work
The two-rainbow independent domination invariant was introduced by Kraner Šumenjak, Rall and Tepeh (2018). Gabrovšek, Peperko and Žerovnik announced results for generalized Petersen graphs \(P(n,2)\) in 2021 and published the complete minimum-value analysis in 2023; the Petersen case yields minimum weight six, already known. Božović, Radić and Tepeh (2025, Lemma 12) independently prove that same minimum for the Petersen graph. The present claim **does not claim the minimum weight as new**. It gives the whole named-color enumeration and automorphism-orbit geometry, which are not implied by a minimum-value result. Ordinary two-rainbow domination, independent rainbow domination and two-rainbow *independent* domination have different feasibility rules and cannot be substituted without a proof.

## Limitations
This is a finite theorem for the Petersen graph only, not an extension to arbitrary generalized Petersen graphs. Independently scrutinized mathematical validation has not been performed. Although several closely related published full articles were inspected, the 2021 conference proceedings' relevant section could not be retrieved in this analysis; additional unindexed or inaccessible enumeration data could affect publication priority. Computations are included for reproducibility, not as independent external certification.

## References
1. T. Kraner Šumenjak, D. F. Rall, A. Tepeh, *On k-rainbow independent domination in graphs*, Applied Mathematics and Computation 333 (2018), 353–361, https://doi.org/10.1016/j.amc.2018.03.113.
2. B. Gabrovšek, A. Peperko, J. Žerovnik, *2-rainbow independent domination numbers of some graphs*, SOR 2021, pp. 173–178, ISBN 978-961-6165-57-0; proceedings reported publicly available by 2021-09-24, https://arhiv.fov.um.si/sor_21/.
3. B. Gabrovšek, A. Peperko, J. Žerovnik, *On the 2-rainbow independent domination numbers of some graphs*, Central European Journal of Operations Research 31 (2023), 817–831, https://doi.org/10.1007/s10100-023-00840-w.
4. D. Božović, G. Radić, A. Tepeh, *2-rainbow independent domination in complementary prisms*, Computational and Applied Mathematics 44 (2025), article 235, https://doi.org/10.1007/s40314-025-03189-9.
