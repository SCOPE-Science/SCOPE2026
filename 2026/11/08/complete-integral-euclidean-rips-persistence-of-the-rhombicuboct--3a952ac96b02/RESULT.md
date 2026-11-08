# Complete integral Euclidean Rips persistence of the rhombicuboctahedron

## Finding
Let \(P\) be the set of all \(24\) signed coordinate permutations of \((1+\sqrt2,1,1)\) in \(\mathbb R^3\). For every real \(r\ge0\), let \(X_r\) be the **inclusive Euclidean Vietoris–Rips complex**: a finite subset of \(P\) spans a simplex precisely when all its pairwise Euclidean distances are at most \(r\). Then the complete **integral** homotopy-type sequence is
\[
X_r\simeq
\begin{cases}
\text{24 discrete points},&0\le r<2,\\
\bigvee^{17}S^1,&2\le r<2\sqrt2,\\
S^2,&2\sqrt2\le r<\sqrt{12+8\sqrt2},\\
\bigvee^{7}S^3,&\sqrt{12+8\sqrt2}\le r<\sqrt{16+8\sqrt2},\\
S^{11},&\sqrt{16+8\sqrt2}\le r<\sqrt{20+8\sqrt2},\\
\ast,&r\ge\sqrt{20+8\sqrt2}.
\end{cases}
\]
Moreover, these groups are free abelian and **all inclusion-induced integral homology maps are determined**. The nonzero reduced barcode consists of \(23\) degree-zero intervals \([0,2)\), \(17\) degree-one intervals \([2,2\sqrt2)\), one degree-two interval \([2\sqrt2,\sqrt{12+8\sqrt2})\), seven degree-three intervals \([\sqrt{12+8\sqrt2},\sqrt{16+8\sqrt2})\), and one degree-eleven interval \([\sqrt{16+8\sqrt2},\sqrt{20+8\sqrt2})\). In degree zero of unreduced homology there is additionally one infinite interval.

The unique degree-two persistence generator is a geometrically **marked integral fundamental cycle** of the rhombicuboctahedral boundary, triangulated by a fixed diagonal in each square. It remains primitive through three distinct, strictly increasing Euclidean distance shells, and an explicit integral \(79\)-tetrahedron chain fills it at the exact death threshold. The same fixed boundary triangulation is the target of elementary collapses at all three sphere stages.

## Assumptions and scope
Write \(a=1+\sqrt2\) and index vertices by the lexicographically ordered triples of coordinate pairs \((u,v)\) representing \(u+v\sqrt2\). In the finite certificates, the \(24\) points are sorted lexicographically as triples, where the long coordinate is \((\pm1,\pm1)\) and the two short coordinates are \((\pm1,0)\), with matching signs. The exact squared distances are the following seven increasing shells, each represented in \(\mathbb Z[\sqrt2]\):
\[
4,\quad 8,\quad8+4\sqrt2,\quad12+4\sqrt2,\quad
12+8\sqrt2,\quad16+8\sqrt2,\quad20+8\sqrt2.
\]
Their respective unordered-pair multiplicities are \(48,36,48,48,36,48,12\), totaling \(276=\binom{24}{2}\). The phrase *three sphere stages* refers to the three distinct inclusive thresholds with squared radii \(8\), \(8+4\sqrt2\), and \(12+4\sqrt2\). The result concerns these exact Euclidean coordinates and the inclusive, not strict, filtration.

Let \(K\) be the surface triangulation obtained by taking all eight triangular polyhedron faces and, in each of the eighteen square faces, choosing the lexicographically smaller missing diagonal and its two incident triangles. Thus \(K\) has face vector \((24,66,44)\). The explicit ordered simplicial collapse certificates refer to this **same** subcomplex \(K\) of each \(X_r\) at the three sphere thresholds.

## Proof
**Exact shell enumeration and first stage.** Differences of the listed coordinates have squared norms in \(\mathbb Z[\sqrt2]\). Exhausting all \(276\) unordered vertex pairs produces exactly the seven shells above; the displayed order follows directly from their componentwise-increasing integer coefficients. At the first nontrivial threshold the complex has face vector \((24,48,8)\). Its eight triangles are vertex-disjoint. Each can be removed together with a free edge, leaving a connected graph on \(24\) vertices and \(40\) edges, hence a wedge of \(40-24+1=17\) circles.

**The marked surface.** The graph of shortest Euclidean edges has precisely eight triangular faces and eighteen induced square faces. Choosing a diagonal in each square gives \(K\), a connected closed combinatorial surface with face vector \((24,66,44)\); every edge belongs to exactly two triangles and every vertex link is one cycle. Its Euler characteristic is \(2\), so \(K\cong S^2\). Orient the \(44\) triangles outward. Their signed sum is an integral fundamental cycle \(z\), with vanishing simplicial boundary.

**Three exact collapses.** At the three consecutive thresholds with squared radii \(8\), \(8+4\sqrt2\), and \(12+4\sqrt2\), complete clique enumeration gives respectively \(206\), \(638\), and \(2782\) nonempty faces. The serialized `collapse_certificate.json` lists respectively \(36\), \(252\), and \(1324\) ordered elementary collapse pairs. The standalone verifier reconstructs every face and checks, at each deletion, that the lower simplex has exactly the displayed unique immediate coface, while neither member lies in \(K\). At the end, the remaining complex is **exactly** \(K\), with \(134\) nonempty faces. Therefore the inclusions \(K\hookrightarrow X_r\) at each stage are integral homology isomorphisms, and the intermediate inclusions act as the identity on the marked generator \([z]\). This is stronger than matching Betti numbers.

**The next-stage three-sphere wedge.** At squared radius \(12+8\sqrt2\), the face vector in dimensions zero through eight is
\[
(24,216,944,2202,2904,2236,960,192,8).
\]
An explicit sequence of \(3872\) further elementary collapses reduces the \(9686\)-face complex to a \(3\)-dimensional complex with \(1942\) faces. It is simply connected: the preceding stage retracts onto \(K\cong S^2\), and all \(36\) newly introduced edges span triangles whose other two edges were already present at the preceding stage. Those triangles kill the new edge generators; attaching other faces cannot create fundamental-group generators.

The integral boundary map from \(3\)-chains to \(2\)-chains has a certificate of \(751\) independent **unit pivots** (each \(\pm1\)) in a \(944\)-row integer matrix with \(2202\) tetrahedral columns. This produces a unimodular \(751\)-minor, proving its image is saturated in the free group of \(2\)-chains. Independently the \(2\)-to-\(1\) boundary has rank \(193\): this is verified over \(\mathbb F_2\), and cannot exceed the \(216-24+1=193\) graph-cycle rank over \(\mathbb Q\). Since \(751+193=944\), there is no rational second homology; the saturation argument rules out any hidden integral torsion, so \(H_2=0\) over \(\mathbb Z\). The collapsed complex is \(3\)-dimensional and simply connected, hence \(2\)-connected by the Hurewicz theorem. Its Euler characteristic is \(-6\), so \(H_3\cong\mathbb Z^7\). The Hurewicz and Whitehead theorems now give \(\bigvee^7 S^3\): choose seven sphere maps representing a basis of \(H_3\), yielding a homology equivalence between simply connected CW complexes.

The integral chain in `filling.json` gives \(79\) oriented tetrahedra, each with coefficient \(\pm1\), whose signed simplicial boundary equals the outward-oriented \(44\)-triangle cycle \(z\). This independently exhibits its exact death at this threshold.

**Final two stages.** At squared radius \(16+8\sqrt2\), precisely twelve pairwise disjoint antipodal edges remain absent. Thus the clique complex is the join of twelve two-point sets, the boundary of a twelve-dimensional cross-polytope, homeomorphic to \(S^{11}\). At squared radius \(20+8\sqrt2\) the graph becomes complete, so the complex is a simplex. The possible nonzero homology occurs in mutually distinct degrees at the successive nontrivial stages; together with the marked identity maps through the sphere stages, this proves the asserted entire integral barcode.

## Verification
Run `python3 verify_rhombicuboctahedron_euclidean.py` in the directory containing `collapse_certificate.json`, `rank_certificate.json`, and `filling.json`. No external Python packages are required. The verifier reconstructs coordinates and all simplices from first principles, checks the \(44\)-triangle fundamental cycle with exact arithmetic in \(\mathbb Z[\sqrt2]\), independently replays all \(5484\) elementary collapses, checks the simple-connectivity edge-reduction premise, verifies all \(751\) unit pivots and the maximal \(193\) rank of the second boundary, and confirms that the \(79\)-tetrahedron chain has precisely the claimed oriented boundary. The execution result is preserved in `verify_output.txt` and must be reproducible from the serialized package. In the larger penultimate stage, the argument uses the exact missing-edge matching, without attempting to enumerate its exponentially many faces.

## Relationship to prior work
Saleh, Titz Mite and Witzel (first public February 28, 2023) determine Vietoris–Rips homotopy types of the **five Platonic solids** and expressly identify Archimedean solids as a natural further direction. Their theorem and relevant text were inspected; they do not settle this Archimedean rhombicuboctahedron. Saleh's 2023 dissertation was searched for the polyhedron and its contents inspected; its listed finite-polytope classifications address Platonic and higher-dimensional examples.

A directly related published result, *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere* (published-finding corpus record dated October 11, 2026), already proves \(\bigvee^{17}S^1\) at graph-distance one and a \(252\)-pair collapse onto **the same geometric surface** at graph-distance two. These portions are explicitly prior knowledge, not new claims. Its metric is shortest-path distance along the graph, and the result expressly leaves the death threshold of the two-sphere class open. At one Euclidean shell, its scale-two graph-metric complex coincides with the present third Euclidean stage (the identical \(638\)-face complex), so the previously published \(252\)-collapse is covered and not presented as original. The new contribution is the complete **Euclidean chordal-distance** filtration, especially the additional sphere-preserving shell, the integral \(79\)-tetrahedron filling, the next-stage seven-three-sphere wedge with an integral unit-pivot certificate, and the final exact persistence intervals.

A separate Euclidean cuboctahedron classification concerns \(12\), not \(24\), vertices, and does not imply this filtration. Published searches under the polyhedron's alternate name *small rhombicuboctahedron*, the graph and metric aliases, and the specific homotopy multiplicity did not identify stronger coverage. This is a comparison of mathematical statements and objects, not a claim that keyword absence proves global novelty.

## Limitations
The result is confined to the exact regular Euclidean realization given here; no perturbation stability beyond ordinary persistent-homology stability theorems, no integral symmetry-module splitting, and no minimality of any recorded collapse length is claimed. The integral proof relies on fully finite, replayable certificates; it does not replace a human-independent scientific review. An equivalent computation in unindexed literature remains possible. The statement is about homotopy types and homology persistence maps, not a preferred homotopy equivalence natural in the filtration parameter.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first posted 2023-02-28); *Innovations in Incidence Geometry* 21 (2024), 17–34, DOI 10.2140/iig.2024.21.17. Primary MSC 55N31. https://arxiv.org/pdf/2302.14388
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation, 2023, DOI 10.22029/jlupub-17950. https://jlupub.ub.uni-giessen.de/bitstreams/34b835ec-c58f-4735-8982-4e822628bd74/download
3. *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere*, published mathematical record, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-explicit-scale-two-rips-collapse-onto-the-rhombicuboctahedral--333648c8216c
4. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, published mathematical record, October 4, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e
