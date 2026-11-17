# The five fixed-point homotopy types of the Fano spherical building under all automorphism subgroups

## Finding

Let \(B\) be the point–line incidence graph of the Fano plane \(\mathrm{PG}(2,\mathbb F_2)\), realized as a one-dimensional simplicial complex, and let \(G=\operatorname{Aut}(B)\), including point–line dualities. The group \(G\) has order \(336\), with index-two collineation subgroup \(\mathrm{GL}_3(\mathbb F_2)\). For **each of its 413 subgroups** \(H\), the ordinary geometric fixed-point space \(|B|^H\) has one of precisely five integral homotopy types. The complete census, with numbers of actual subgroups, is:

| Geometric fixed-point homotopy type | Number of subgroups |
|---|---:|
| \(\bigvee^8 S^1\) | 1 |
| Contractible (nonempty) | 210 |
| \(S^0\) (two points) | 56 |
| Three isolated points | 28 |
| Empty | 118 |
| **Total** | **413** |

These subgroups constitute exactly \(23\) conjugacy classes in \(G\). The 179 subgroups preserving point and line types give, respectively, counts \(1,105,56,0,17\) in these five categories; the 234 subgroups containing a type-reversing duality give counts \(0,105,0,28,101\). More precisely, the 28 three-point fixed spaces belong to a single conjugacy class of 28 **order-two polarity subgroups**. Each such involution swaps point and line types, fixes exactly three flags setwise, and fixes no original vertex. These fixed points are the three corresponding flag midpoints. The accompanying census includes all 23 conjugacy-class representatives and exact fixed-graph data.

## Assumptions and scope

Label the seven points by the nonzero vectors \(x\in\mathbb F_2^3\), coded as integers 1 through 7. The seven projective lines are the triples \(\{x,y,x+y\}\) for distinct points \(x,y\). The incidence graph \(B\) has 14 vertices (seven points and seven lines) and 21 edges (flags). A geometric fixed point means a point of the realization fixed by **every** element of \(H\), not merely a vertex fixed by \(H\). The count is over the actual subgroups, not only isomorphism types or conjugacy classes. All group actions are the natural graph automorphisms of this Fano building, including type-swapping automorphisms. The statement is about the underlying ordinary homotopy types; it does not assert equivariant equivalences for varying subgroups.

## Proof

**Full symmetry group.** Every invertible binary linear map permutes the seven nonzero vectors, preserves the seven line triples, and induces an incidence automorphism. There are \((2^3-1)(2^3-2)(2^3-2^2)=168\) such maps. Conversely, a point–line-type-preserving automorphism is determined by the images of any projective frame, hence by a binary basis; thus these exhaust type-preserving graph automorphisms. The standard polarity sends a point \(x\) to the line \(\{y:x\cdot y=0\}\) and a line to its unique normal point. It reverses the bipartition and has order two. A connected bipartite graph automorphism must either preserve or exchange the two parts, so these 168 collineations and their 168 polarity composites exhaust \(G\) and give \(|G|=336\).

**Exact fixed-graph model.** Subdivide the 21 incidence edges once, placing a vertex at each flag midpoint. This barycentric subdivision is equivariant under the entire graph automorphism group and has no inversions. For an arbitrary subgroup \(H\), the geometric fixed set is the realization of the fixed subcomplex of this subdivision. Its vertices are (a) the original point and line vertices fixed individually by every member of \(H\), and (b) the midpoints of incidence edges whose unordered endpoint pairs are setwise stabilized by every member of \(H\). An edge connects a midpoint of type (b) to an endpoint of type (a) whenever that endpoint belongs to the flag. This gives an **exact PL graph model**, including midpoints of edges reversed by dualities; using only individually fixed original vertices would miss such points.

**Exhaustion of subgroups.** In the normal index-two collineation group \(G_0\), start with the identity subgroup and close under adjoining every element: replace \(H\) by \(\langle H,g\rangle\) for every \(g\in G_0\), repeat until no new subgroup occurs. Any finite subgroup has a generating sequence, so this is exhaustive; it finds exactly 179 distinct subgroups. For every subgroup \(K\leq G\) meeting the reversing coset, put \(H=K\cap G_0\) and select \(t\in K\setminus G_0\). Then \(K=H\sqcup Ht\), \(tHt^{-1}=H\), and \(t^2\in H\). Conversely these three conditions define a subgroup. Enumerating every such pair \((H,t)\) and deduplicating yields all 413 subgroups, as checked by an independent closure/inverse test. Conjugation by the complete 336-element group partitions them into 23 classes.

**Homotopy calculation.** For every subgroup representative, compute the fixed vertices, fixed flag-midpoints, and fixed barycentric edges by their explicit defining predicates above. Union-find on this finite graph determines the number \(c\) of components; its cycle rank is \(e-v+c\). Independently evaluate these predicates for every conjugate subgroup, recovering all 413 counts. All nontrivial-subgroup fixed graphs have cycle rank zero. Their numbers of components are exactly 0, 1, 2, or 3, so they are respectively empty, contractible forests, two points, or three points, up to homotopy. The trivial subgroup fixes \(B\) itself: it is connected and its cycle rank is \(21-14+1=8\), so \(|B|\simeq\bigvee^8 S^1\). The certified classification follows. The 28 order-two reversing subgroups each have three fixed flag midpoints and no fixed original vertices, while the other 206 reversing subgroups have at most one fixed flag midpoint. The finite search is **exhaustive**, by the subgroup-generation and index-two decomposition arguments, rather than an extrapolation from a sample.

## Verification

The standalone standard-library Python program `verify_building.py` constructs the 336 permutations directly from binary vector arithmetic and the explicit polarity, verifies all preserve incidence, constructs the group product/inverse tables, exhaustively generates the 413 subgroups, verifies their subgroup axioms, forms all 23 conjugacy classes, constructs the fixed subdivided graphs, and checks every subgroup independently. It emits `census.json`, providing 23 representative group-index sets, class sizes, numbers of fixed original vertices/flag-midpoints/edges, connected components, first Betti numbers, and homotopy types. Execute `python verify_building.py --census census.json` from the directory containing the verifier. Its deterministic output is recorded in `verifier_output.txt`. The emitted census is generated from the explicit construction, with no external databases or downloaded dependencies. Group element indices are determined by lexicographic sorting of the 14-point permutation images in the source program.

## Relationship to prior work

The Fano building and its 168 collineations, 336 total graph automorphisms, and ordinary cycle rank eight are standard and not claimed as new. Bate, Martin and Röhrle [1, Theorems 2.1 and 2.3, Remark 3.2(iv)] relate noncontractibility of type-preserving fixed subbuildings to complete reducibility; their results explain much of the type-preserving fixed-space dichotomy but do not supply this 413-subgroup census or enumerate duality-containing subgroup loci. Ramos-Cuevas [2] establishes the spherical-building center conjecture, not the exact fixed-graph homotopy counts. Lawrence, Flapan and Wilson [3] study symmetry groups realizable by **spatial embeddings** of the Heawood graph in three-space, not the fixed sets of all subgroups acting on the abstract graph itself. The present contribution is the **complete finite topological fixed-space spectrum** for the smallest thick rank-two building under its full type-preserving and type-reversing graph automorphism group. No claim is made that the general fixed-subbuilding formalism is new.

## Limitations

This is an exact finite classification for the Fano plane, not an all-orders projective-plane theorem. The data determine ordinary fixed-space homotopy types and component counts; they do not determine normalizer permutations of components, equivariant attachment data, quotient homotopy types, or induced representations on integral chains. The group enumeration and graph homotopy calculation are machine-checkable finite calculations with a human-readable exhaustive reduction, not independently audited mathematical certification. Equivalent tabulations in obscure finite-group databases or unindexed texts remain a publication-priority risk.

## References

1. M. Bate, B. Martin and G. Röhrle, *On Tits' Centre Conjecture for Fixed Point Subcomplexes*, arXiv:0811.4294 (first posted November 26, 2008), Theorems 2.1–2.3 and Remark 3.2(iv). https://arxiv.org/html/0811.4294v2
2. C. Ramos-Cuevas, *The Center Conjecture for thick spherical buildings*, arXiv:0909.2761 (first posted September 15, 2009). https://arxiv.org/html/0909.2761v2
3. E. D. Lawrence, E. Flapan and R. T. Wilson, *Topological Symmetry Groups of the Heawood Graph*, arXiv:1910.08095 (first posted October 17, 2019), also *Symmetry* **12** (2020), article 546. https://www.mdpi.com/2073-8994/12/4/546
4. J. Baez, *Heawood Graph*, AMS Visual Insight, August 1, 2015. https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/
