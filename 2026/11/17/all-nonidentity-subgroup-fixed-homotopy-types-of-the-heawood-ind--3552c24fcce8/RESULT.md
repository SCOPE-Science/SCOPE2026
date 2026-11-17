# All nonidentity subgroup-fixed homotopy types of the Heawood independence complex

## Finding
Let \(H\) be the point–line incidence graph of the Fano projective plane, let \(K=\operatorname{Ind}(H)\), and let \(G=\operatorname{Aut}(H)\) be its full group of 336 graph automorphisms, including point–line dualities. For every **nonidentity subgroup** \(U\leq G\), the geometric fixed space \(|K|^U\) is homotopy equivalent to exactly one of the following six types. The second column counts actual subgroups, not conjugacy classes.

| Integral homotopy type of \(|K|^U\) | Subgroups |
| --- | ---: |
| \(S^2\vee S^2\) | 21 |
| \(S^2\vee S^1\) | 14 |
| \(S^1\vee S^1\) | 42 |
| \(S^0\) (two isolated points) | 17 |
| A point (contractible) | 301 |
| Empty | 17 |
| **Total** | **412** |

The 412 nonidentity subgroups fall into 22 conjugacy classes. The group has 413 subgroups in 23 classes when the trivial subgroup is included. The 21 two-sphere-wedge cases are the incidence-preserving subgroups of order two; the 14 mixed sphere-and-circle cases are one conjugacy class of subgroups of order four. In particular, geometric fixed spaces contain topology in degrees one and two although the ambient independence complex has previously known homotopy type \(\bigvee^6 S^3\). This finding does **not** claim that ordinary homotopy type as new.

## Assumptions and scope
Identify the seven Fano points and seven Fano lines with the nonzero three-bit vectors and nonzero covectors \(p,a\in\mathbb F_2^3\). A point \(p\) is incident with a line \(a\) precisely when \(a\cdot p=0\). The Heawood graph has 14 vertices and 21 edges, and its independence complex is the simplicial complex of vertex subsets containing no incident point–line pair. An element of \(G\) permutes these 14 vertices, and \(|K|^U\) denotes the **geometric** fixed locus (not merely the subcomplex on individually fixed vertices). The empty geometric realization is distinct from a point, and \(S^0\) means precisely two components consisting of points. All the asserted homotopy equivalences are integral, not merely rational or mod-two conclusions. The trivial subgroup is excluded from the new claim.

## Proof
**Full automorphism group.** Every incidence-preserving automorphism of the Fano plane is determined by the images of three linearly independent point vectors: there are \(7\cdot6\cdot4=168\) choices. They are exactly the invertible binary linear transformations, acting contragrediently on line covectors. The Heawood graph is connected and bipartite, so every graph automorphism either preserves its two parts or exchanges them. The point–line polarity \(p\leftrightarrow a\) is a part-exchanging automorphism, and composing it with the 168 collineations gives all 336 graph automorphisms. `verify.py` reconstructs and checks their distinct 14-point permutations and multiplication table.

**Fixed-complex model.** For a subgroup \(U\), partition the 14 graph vertices into its orbits. Keep an orbit only when it contains no incident point–line pair. A subset of the retained orbits is a simplex exactly when the union of those vertex orbits is an independent set in \(H\). Call the resulting orbit complex \(L_U\). A point of the geometric realization \(|K|\) is fixed by \(U\) exactly when its barycentric coordinates are constant on every vertex orbit. The affine map assigning each selected orbit's coordinate uniformly to its members gives a simplicial (on the fixed affine cells) PL identification \(|L_U|\cong |K|^U\). This handles barycenters of setwise invariant simplices that need not contain any individually fixed vertex.

**Exhaustive subgroups and conjugacy.** Begin with the identity subgroup and, for every known subgroup, adjoin each omitted group element and take the subgroup generated. Repeat until no new subgroup appears. Since each subgroup of a finite group has a finite generating sequence, the resulting closure list contains **every** subgroup, rather than a selected sample. Exact multiplication checks give 413 distinct closed subgroups. Conjugation by each of the 336 automorphisms partitions them into 23 classes; the sum of the class sizes is 413, and each class size divides 336. One representative of each of the 22 nonidentity classes is then passed to the fixed-complex calculation. Conjugate subgroups give isomorphic fixed spaces.

**Explicit elementary collapses.** Every representative's complex \(L_U\) is finite. Starting with all its nonempty faces, repeatedly delete a facet together with a ridge contained in no other facet. These are genuine elementary simplicial collapses, preserving homotopy type. The complete deterministic algorithm and all class outcomes appear in `verify.py` and `CENSUS.json`. Every proposed ridge and facet is checked against the current face set; no unverified discrete-Morse assertion is used.

The collapsed complexes have only the following forms:

- A single point; two isolated points; the empty complex; or a connected graph with six vertices and seven edges. Such a graph has homotopy type \(S^1\vee S^1\).
- For the order-four conjugacy class of size 14, a connected triangulated closed two-manifold with eight vertices, eighteen edges and twelve triangles, plus one additional edge joining two vertices on that surface. Every surface edge belongs to exactly two triangles, and every vertex link is a connected cycle. Euler characteristic two therefore makes the surface a two-sphere. Adding the extra edge gives \(S^2\vee S^1\) up to homotopy.
- For the order-two conjugacy class of size 21, the remaining complex is a union of two closed triangulated two-spheres along a **single common filled triangle**. One sphere has eight triangular faces, the other ten. For each component all edges belong to exactly two triangles, all vertex links are cycles, and Euler characteristic is two. Their intersection is exactly the filled triangle, a contractible subcomplex. The gluing theorem gives \(S^2\vee S^2\).

These tests are combinatorial and exhaustive. Specifically, the verifier verifies every candidate two-dimensional surface's local links and edge incidences, rather than inferring that a homology sphere is a topological sphere. The class-weighted totals are \(21,14,42,17,301,17\), as displayed. No claim about other graphs or finite projective planes is extrapolated from this finite case.

## Verification
Run `python3 verify.py` in the directory containing `CENSUS.json`. The program reconstructs the Fano incidence graph, all 336 automorphisms, the exact group table, all 413 subgroups, 23 conjugacy classes, the orbit complexes, and every elementary collapse. It verifies the residual graph ranks, the two triangulated surfaces and their full intersection, and the six class-weighted totals. It compares a newly generated census byte-for-byte with `CENSUS.json`. The recorded stdout in `verification_output.txt` ends with `FANO_INDEPENDENCE_NONIDENTITY_SUBGROUP_FIXED_SPACES_PASS`. Python's standard library alone is sufficient. The computation takes place in a **finite** 336-element group and finite face sets; it is exact enumeration, not experimental extrapolation.

## Relationship to prior work
Barmak's 2010 study develops star-cluster methods and establishes general topology of triangle-free graph independence complexes. An earlier published Heawood calculation gives \(\operatorname{Ind}(H)\simeq\bigvee^6S^3\), and a separate published study determines the 168-collineation rational character on third homology. A published computation of 21 minimal homology carriers concerns induced **vertex subcomplexes**, not the geometric loci fixed by subgroups. Those results give the ambient graph's topology, representations, or inclusion maps but do not imply the integral homotopy types of all 412 nonidentity fixed spaces. In particular, knowing traces on ambient homology determines Euler characteristics of element-fixed spaces but not, in general, the simultaneous fixed loci for noncyclic subgroups or their homotopy types.

## Limitations
The classification is specific to the fourteen-vertex Heawood independence complex. It does not classify fixed spaces of other Fano-associated complexes, incidence graphs of higher-order projective planes, normalizer actions on the resulting homology, or orbit-space fundamental groups. It does not identify attaching maps between the various fixed loci in a genuine equivariant homotopy model. Although exact finite certificates support the result, an independent mathematical audit and exhaustive publication-priority search have not been performed. Differently indexed equivalent calculations remain possible.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public version 2010-07-02, https://arxiv.org/abs/1007.0418.
- *The Heawood independence complex is a wedge of six three-spheres*, published mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2.
- *The exceptional rational homology representation of the Heawood independence complex*, published mathematical record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-exceptional-rational-homology-representation-of-the-heawood--213fded46807.
- *Twenty-one minimal Heawood homology carriers and their Fano-plane relations*, published mathematical record (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-twenty-one-minimal-heawood-homology-carriers-and-their-fano-plan--86d8b5d59b6c.
- S. Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), DOI:10.55016/ojs/cdm.v12i1.62277.
