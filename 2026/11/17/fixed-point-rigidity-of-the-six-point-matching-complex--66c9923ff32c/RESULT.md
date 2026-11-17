# Fixed-point rigidity of the six-point matching complex

## Finding
Let \(M_6=\mathcal M(K_6)\) be the simplicial complex of matchings of the loopless complete graph on six labeled vertices. Its vertex set consists of the fifteen edges of \(K_6\); a collection of such vertices is a simplex when the edges are pairwise disjoint. The natural permutation action of \(S_6\) on the six labels induces a simplicial action on \(M_6\). For **every** subgroup \(H\le S_6\), its *geometric* fixed space \(|M_6|^H\) has the following complete integral homotopy classification:

| Fixed-space homotopy type | Number of labeled subgroups | Conjugacy classes |
| --- | ---: | ---: |
| \(\bigvee^{16}S^1\) | 1 | 1 |
| A point (indeed, collapsible) | 1,140 | 34 |
| Three discrete points | 80 | 4 |
| Empty | 234 | 17 |
| **Total** | **1,455** | **56** |

The first row occurs only for the trivial subgroup. In particular, **every nontrivial subgroup has a fixed set that is empty, collapsible, or a disjoint union of three points**. There are no nontrivial fixed-space circles or higher-dimensional homology classes. Every entry is established by an explicit elementary-collapse certificate, rather than inferred from Euler characteristics or rational characters.

As a concrete noncyclic phenomenon, put \(A=\langle(123)\rangle\) and \(B=\langle(456)\rangle\) on the six labels. Both \(|M_6|^A\) and \(|M_6|^B\) consist of three points, but \(|M_6|^{\langle A,B\rangle}=\varnothing\). The simultaneous-fixed-space conclusion cannot be read off from the individual fixed-space homotopy types.

## Assumptions and scope
The ground graph is the simple complete graph on \(\{1,2,3,4,5,6\}\), without loops. The matching complex includes the empty face in its abstract face poset, although its geometric realization contains only nonempty faces. The fixed set \(|M_6|^H\) consists of **all** points fixed by all elements of \(H\), including barycenters of non-pointwise-fixed simplices. It is not merely the induced subcomplex of individually fixed edges. All homotopy statements concern the ordinary integral homotopy types of these geometric realizations.

## Proof
**1. Exact fixed-space simplicial model.** For any finite simplicial complex \(K\) acted upon simplicially by a finite group \(H\), the barycentric coordinates of a geometric fixed point are constant on each orbit of simplicial vertices. A vertex-orbit contributes a vertex to an orbit-compression complex exactly when that entire orbit is a simplex of \(K\). A collection of these orbit-vertices spans a simplex precisely when the union of their underlying orbits is a simplex of \(K\). Mapping each orbit-vertex to the normalized barycenter of its constituent vertices gives a simplexwise affine PL homeomorphism onto \(|K|^H\), with inverse obtained from constant barycentric coordinates. In our case, orbit-vertices are precisely edge-orbits of \(K_6\) that are matchings, and compatibility means that their combined edges remain pairwise endpoint-disjoint.

**2. Exhaustive subgroup coverage.** Permutations are represented by all \(6!=720\) bijections of six labels, and group multiplication is exact permutation composition. The subgroup algorithm starts from the trivial group; for each newly found conjugacy-class representative \(H\), it forms \(\langle H,g\rangle\) for **every** \(g\in S_6\setminus H\), and records every conjugate of each new extension. The finite search stabilizes with 56 conjugacy classes comprising 1,455 distinct subgroups. This is exhaustive, not a sample: any subgroup is obtained by adjoining its finite generating set element by element, and conjugacy carries such an extension of an arbitrary representative to an extension of the chosen representative. Independently, for each of the 56 representatives the normalizer count \(|S_6|/|N_{S_6}(H)|\) agrees exactly with the enumerated class cardinality. All representative generators and class cardinalities are included in `m6_subgroup_census.csv`.

**3. Elementary-collapse certificates.** For each representative, `m6_subgroup_census.csv` records the admissible edge orbits and the full sequence of collapse pairs \((F,E)\). At each step, \(F\) is a maximal simplex, \(E\subset F\) is a codimension-one face, and \(E\) lies in exactly one maximal simplex. Removing precisely \(F,E\) is an elementary simplicial collapse. The independent replay check in `verify_m6_fixed.py` reconstructs the complex directly from the recorded edge orbits and validates **every** free-face condition, not just the final cell counts. Across the 56 representatives, all residual complexes are empty, a single vertex, or three isolated vertices, except the trivial group.

For the trivial group, the complex has 15 vertices, 45 edges and 15 triangular faces. Its certified fifteen elementary collapses leave a connected graph with 15 vertices and 30 edges. A connected graph with \(E-V+1\) independent cycles is homotopy equivalent to that many circles, here \(30-15+1=16\). For a nontrivial subgroup, every residual complex is either empty, one vertex, or three isolated vertices, proving the three remaining types. Conjugate subgroups have PL-homeomorphic fixed sets, so the 56 representatives classify all 1,455 subgroups. The certificate also recomputes the complete fixed complex independently for **each** labeled subgroup and verifies the 1,455-type tally directly.

**4. Counts.** The 56 representative classes yield respectively \((1,34,4,17)\) conjugacy classes, and summing their independently verified conjugacy sizes yields \((1,1140,80,234)\) labeled subgroups in the four rows. Both lists sum to 56 and 1,455 respectively.

## Verification
Run `python3 verify_m6_fixed.py` in a directory containing the accompanying `m6_subgroup_census.csv`. It uses the Python standard library only. It reconstructs all 720 permutations and their products, computes all 56 subgroup classes and 1,455 distinct subgroups, checks each class cardinality against a normalizer computation, enumerates the fixed-space orbit-compression complexes, and validates every elementary collapse against the current complete face poset. It then separately recalculates the homotopy classification for each of the 1,455 subgroups, without reusing the representative class's result. Success prints:

`MATCHING_K6_SUBGROUP_FIXED_SPACE_CENSUS_PASS subgroups=1455 conjugacy_classes=56 circles=1 contractible=1140 three_points=80 empty=234`

All computations use exact finite permutations and finite simplicial face sets. The run output is included as `verification_output.txt`. No infinite extrapolation or computational timeout argument is used.

## Relationship to prior work
The matching complex \(M_n\) and its ordinary homology and symmetric-group representations predate this calculation: Bouc's 1992 analysis and Shareshian–Wachs's first-public 2004 manuscript establish the classical framework. The known ordinary first homology of \(M_6\) is **not** claimed new. Published geometric fixed-space calculations for a single permutation, including the complete cycle-type theorem and the involution theorem, cover all cyclic subgroups but do not classify simultaneous fixed points of arbitrary noncyclic subgroups. A related arbitrary-subgroup classification for the **line-clique complex** of \(K_n\) concerns pairwise-intersecting edge collections, not the present pairwise-disjoint matching complex; neither statement implies the other. A direct search for an exact complete \(S_6\)-subgroup fixed-locus table found no covering result. This is a best-knowledge comparison, not proof of publication priority.

## Limitations
This is a complete classification for the six-ground-vertex matching complex only. It does not classify all subgroup fixed spaces for larger complete graphs, the residual normalizer action on fixed-space components, the full equivariant homotopy type, or geometric **quotients**. The finite certificate establishes the stated finite census but is subject to the ordinary possibility of software or transcription error despite exhaustive checks. Unindexed prior publications could contain an equivalent result. Independent mathematical validation has not been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first publicly posted 2004-09-03, particularly Sections 1–2. https://arxiv.org/abs/math/0409054
2. S. Bouc, *Homologie de certains ensembles de 2-sous-groupes des groupes symétriques*, 1992, as cited and summarized by Shareshian–Wachs; original full text was not examined.
3. *Cycle-type geometric fixed points of complete-graph matching complexes*, publicly indexed research finding, 2026-10-25, full `RESULT.md` inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cycle-type-geometric-fixed-points-of-complete-graph-matching-com--790f558ef1ba
4. *Geometric fixed points of complete-graph matching complexes under every involution*, publicly indexed research finding, 2026-10-25, full `RESULT.md` inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-geometric-fixed-points-of-complete-graph-matching-complexes-unde--8949870375bb
5. *Subgroup fixed-point homotopy of complete-graph line-clique complexes*, publicly indexed research finding, 2026-10-25, full `RESULT.md` inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-subgroup-fixed-point-homotopy-of-complete-graph-line-clique-comp--6bad44993bfb
