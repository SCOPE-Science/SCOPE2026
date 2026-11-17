# Two irreducible rational summands in Heawood two-point configuration homology

## Finding

Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, and let \(B_2(H)\) be the space of **unordered pairs of distinct points** of its geometric realization. The full graph automorphism group \(G=\operatorname{Aut}(H)\) has order \(336\) and is isomorphic to \(\operatorname{PGL}_2(7)\).

There is a natural isomorphism of rational \(G\)-representations
\[
H_1(B_2(H);\mathbb Q)\cong H_1(H;\mathbb Q),
\]
and an irreducible decomposition
\[
\boxed{H_2(B_2(H);\mathbb Q)\cong H_1(H;\mathbb Q)\oplus W_6},
\]
where the graph cycle representation is absolutely irreducible of dimension \(8\), and \(W_6\) is a different absolutely irreducible rational representation of dimension \(6\). Integrally, \(H_2(B_2(H);\mathbb Z)\cong\mathbb Z^{14}\); the configuration space is connected and has no homology in degrees exceeding two. The rational Betti numbers are \((1,8,14)\).

The following table gives the **complete** character, with separate rows for the two distinct conjugacy classes of order eight. The labels of these two classes are interchangeable because the listed characters agree on both.

| Conjugacy-class size | Element order | \(\chi_{H_1(H)}\) | \(\chi_{H_2(B_2(H))}\) | \(\chi_{W_6}\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 8 | 14 | 6 |
| 21 | 2 | 0 | -2 | -2 |
| 28 | 2 | -2 | -2 | 0 |
| 42 | 4 | 0 | 2 | 2 |
| 42 | 8 | 0 | 0 | 0 |
| 42 | 8 | 0 | 0 | 0 |
| 48 | 7 | 1 | 0 | -1 |
| 56 | 3 | -1 | -1 | 0 |
| 56 | 6 | 1 | 1 | 0 |

In particular, \(H_2(B_2(H);\mathbb Q)^G=0\). The graph cycle representation occurs **once** in second homology, accompanied by the exceptional six-dimensional constituent.

## Assumptions and scope

The graph has seven point vertices \(p_x\) and seven line vertices \(\ell_y\), indexed by \(0\ne x,y\in\mathbb F_2^3\), with \(p_x\sim\ell_y\) exactly when the standard binary dot product \(x\cdot y\) is zero. Thus there are fourteen vertices, twenty-one edges, degree three at every vertex, and graph girth six. The graph is an ordinary one-dimensional CW complex with unit edges; collisions are forbidden everywhere, including interiors of edges. Configuration pairs are **unordered**, not ordered, and are not sink configurations.

The group acts on configurations by its geometric graph automorphisms. The bipartition-preserving subgroup consists of the \(168\) transformations \(x\mapsto Ax\), \(y\mapsto A^{-T}y\), for \(A\in\operatorname{GL}_3(\mathbb F_2)\). The involution \(p_x\leftrightarrow\ell_x\) supplies the other coset. These comprise all automorphisms because automorphisms either preserve or swap the two color classes, and an incidence-preserving permutation of the Fano points is uniquely determined by the image of a noncollinear ordered triple.

## Proof

**Topologically valid finite model.** Prue and Scrimshaw's strengthened Abrams subdivision theorem applies to two particles: paths between distinct essential vertices have at least \(2-1=1\) edge, and every essential loop has at least \(2+1=3\) edges. Here the girth is six. Thus the inclusion of the unordered discretized cubical configuration complex \(D_2(H)\) into \(B_2(H)\) is a homotopy equivalence. The inclusion itself is \(G\)-equivariant, so it induces equivariant homology isomorphisms regardless of which deformation retraction is selected.

**Cells and incidence.** The cubical complex has \(91\) zero-cells consisting of unordered pairs of vertices, \(252\) one-cells consisting of a vertex disjoint from an edge, and \(168\) two-cells consisting of a pair of vertex-disjoint edges. Orient graph edges from the smaller to the larger vertex label. Orient a square by the ordered pair of its edges in increasing lexicographic order. For \(e=(u,w)\), \(f=(y,z)\), with \(u<w\) and \(y<z\), its boundary is
\[
\partial[e,f]=[(w,f)]-[(u,f)]-[(z,e)]+[(y,e)].
\]
The signs on square images incorporate both edge orientation reversal and the sign of interchanging the two square-coordinate directions. The accompanying program builds these integral boundary maps and verifies \(\partial_1\partial_2=0\).

**Homology dimensions without assuming modular ranks are rational ranks.** The one-skeleton is connected, as verified by exhaustive traversal of its \(91\) vertices; hence \(\operatorname{rank}\partial_1=90\) integrally. Twenty-eight six-cycles occur in \(H\). Eight can be chosen whose signed edge vectors are linearly independent modulo three. Each chosen six-cycle omits a vertex, so moving one particle around that cycle while fixing a second particle outside it defines a valid one-cycle of \(D_2(H)\). The natural particle-sum map on chains (send a zero-cell \(\{u,v\}\) to \(u+v\) and a one-cell \(\{v,e\}\) to the oriented edge \(e\)) therefore induces a surjection
\[
H_1(D_2(H);\mathbb Q)\twoheadrightarrow H_1(H;\mathbb Q)\cong\mathbb Q^8.
\]
Consequently \(\operatorname{rank}_{\mathbb Q}\partial_2\le252-90-8=154\). Independent exact elimination over \(\mathbb F_3\) gives \(\operatorname{rank}_{\mathbb F_3}\partial_2=154\); because the integral matrix cannot have smaller rank over \(\mathbb Q\) than over \(\mathbb F_3\), equality follows. It gives \(b_1=8\) and \(b_2=168-154=14\). As \(H_2\) is the kernel of a homomorphism between free abelian cellular groups in the top degree, it is torsion-free. The surjection above is thus an isomorphism over \(\mathbb Q\), and it is equivariant.

**Complete character.** For a symmetry \(g\), let \(v(g)\) count fixed graph vertices and \(e^{\pm}(g)\) be the signed number of graph edges fixed as unoriented sets. Graph cycle-space homology has character \(\chi_1(g)=e^{\pm}(g)-v(g)+1\). Let \(c_i(g)\) be the signed trace on the \(i\)-cell group of the cubical configuration model. The equivariant Euler identity gives
\[
\chi_2(g)=c_0(g)-c_1(g)+c_2(g)-1+\chi_1(g).
\]
Every one of the \(336\) graph automorphisms is enumerated from the Fano-plane model; its exact signed fixed-cell traces give the nine-class table above. An independent check constructs a \(14\)-vector basis of \(\ker\partial_2\) over \(\mathbb F_{101}\) and directly computes the trace of all \(336\) induced top-homology actions. Each agrees modulo \(101\) with the integer formula. All chain maps commute with cellular boundaries, including the two-coordinate orientation signs.

**Irreducibility.** For class sizes \(s_C\), the class-function inner product is \(336^{-1}\sum_C s_C\alpha(C)\beta(C)\). From the table one obtains
\[
\langle\chi_1,\chi_1\rangle=1,\quad
\langle\chi_1,\chi_2\rangle=1,\quad
\langle\chi_2,\chi_2\rangle=2.
\]
Therefore the eight-dimensional graph cycle representation is absolutely irreducible and occurs once in second homology. Subtracting it leaves the six-dimensional character \(\psi=\chi_2-\chi_1\), satisfying \(\langle\psi,\psi\rangle=1\) and \(\langle\psi,\chi_1\rangle=0\). The characters are afforded by rational representations: \(H_2\) is rational, while the absolutely irreducible graph cycle module is rational and has a rational isotypic projector; its rational complement realizes \(\psi\). Averaging \(\chi_2\) over the group gives zero, establishing the invariant-space statement.

## Verification

Run `python3 verification/verify.py` from the directory containing this file. It uses the Python standard library and determines graph edges, all configuration cells, both integral boundaries, independent six-cycle lifts, ranks modulo three and \(101\), all \(336\) automorphisms, the nine conjugacy classes, full chain naturality, direct top-kernel traces, and character inner products. It ends with `HEAWOOD_2POINT_FULL_SYMMETRY_PASS`. The exact expected output is embedded as `verification/expected_output.txt`.

The modular elimination is used only as a **lower bound** on rational rank; the surjection via eight explicitly verified cycles gives the opposite bound. The claim is for this single finite graph, not a statement extrapolated from small cases.

## Relationship to prior work

Barnett–Farber (2009) develops ordered two-particle deleted-product homology and intersection theory, particularly for planar graphs. Farber–Hanbury (2010) develops ordered graph two-point homology for mature nonplanar graphs, without the present Heawood unordered full-group character. Prue–Scrimshaw (2009) establishes the cubical-model homotopy equivalence used above. Ko–Park (2011) determines abelian first homology of graph braid groups, including the relevant nonplanar two-torsion phenomenon; the first-homology rank and torsion are not claimed as new. Maciążek–Sawicki (2019, §5.7, Theorem 12 and its proof) proves a stronger **generating-set statement**: second homology for graphs of valence at most three is generated by products of graph cycles. This covers the Heawood graph at the level of generators, but neither supplies their exact relations in this particular graph nor determines the complete 336-element automorphism character. The present homology-rank and symmetry calculations therefore refine, rather than replace, that broader theorem.

Indexed Heawood calculations concern either the *ordered* two-point mod-two groups, *unordered three-point* homology, or other Heawood complexes such as matching or independence complexes. None of these assertions alone determines the rational \(336\)-element action on \(H_2(B_2(H);\mathbb Q)\). In particular, knowing the ordered mod-two Betti numbers is insufficient to identify this unordered rational character without an additional exchange-equivariant comparison.

## Limitations

This result determines rational automorphism modules and proves the top integral homology group is free of rank fourteen. It **does not** determine the integral second-homology \(\mathbb Z[G]\)-lattice, the complete integral first-homology torsion, or an equivariant homotopy decomposition. It does not extend automatically to arbitrary point-line incidence graphs or configurations of more than two particles. Equivalence with an unindexed existing calculation cannot be excluded; no independent mathematical audit has been performed.

## References

- K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first submitted 2009-03-12, https://arxiv.org/abs/0903.2180.
- P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first submitted 2009-09-30, https://arxiv.org/abs/0909.5511.
- M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first submitted 2010-05-13, https://arxiv.org/abs/1005.2300.
- K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first submitted 2011-01-13, https://arxiv.org/abs/1101.2648.
- T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Commun. Math. Phys. 371 (2019), https://doi.org/10.1007/s00220-019-03583-5.
