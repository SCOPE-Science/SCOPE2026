# Split integral next-to-top matching homology under arbitrary even-order edge insertions

## Finding

For every integer \(m\ge3\), and all finite simple graphs \(G\subseteq H\) on the **same** vertex set of exactly \(2m\) labeled vertices, write \(\mathcal M(G)\) for the simplicial complex whose vertices are graph edges and whose simplices are nonempty matchings (with the usual empty face included abstractly). The natural simplicial inclusion induces a split injection

\[
\widetilde H_{m-2}(\mathcal M(G);\mathbb Z)
\hookrightarrow
\widetilde H_{m-2}(\mathcal M(H);\mathbb Z).
\]

Both groups and the cokernel are free abelian. For every finite chain of edge inclusions on this vertex set, the integral persistence module in degree \(m-2\) admits a basis adapted simultaneously to all stages: no class dies or becomes a nonprimitive multiple.

For \(H=K_8\) and \(G=K_8-F\) where \(F=\{\{0,1\},\{2,3\},\{4,5\},\{6,7\}\}\), the inclusion is a primitive embedding \(\mathbb Z^{79}\hookrightarrow\mathbb Z^{132}\), and its homotopy cofiber (equivalently the topological quotient) is

\[
\mathcal M(K_8)/\mathcal M(K_8-F)\simeq\bigvee^{53}S^2.
\]

The persistence degree is sharp: for \(G=C_6\sqcup2K_1\subseteq K_8\), degree-one reduced integral homology maps from \(\mathbb Z^2\) to zero.

## Assumptions and scope

Graphs are finite, simple, undirected and share a fixed even-sized vertex set. Their edge sets need not be complete, connected, spanning in the edge sense or even contain perfect matchings. The matching complex is the ordinary edge-set complex, **not** the perfect-matching extendibility complex or the non-matching complex. Homology is reduced integral simplicial homology; for the statement only degrees \(m-2\), with \(m\ge3\), are asserted. A cofiber is the quotient of a simplicial complex by its included subcomplex.

## Proof

**Relative collapse lemma.** Put \(A=\mathcal M(G)\), \(B=\mathcal M(H)\). Every \(m-1\)-simplex of \(B\), if one exists, has exactly \(m\) graph edges, so is a perfect matching \(\sigma\) on the common \(2m\) vertices and has dimension \(m-1\). Every matching \(\tau\) with \(m-1\) edges leaves exactly two graph vertices uncovered. At most one graph edge can complete it to a perfect matching; hence \(\tau\) is contained in at most one \((m-1)\)-simplex of \(B\).

For each \((m-1)\)-simplex \(\sigma\) lying in \(B\setminus A\), choose one edge \(e\in\sigma\setminus E(G)\), and choose a different edge \(f\in\sigma\) (possible for \(m\ge3\)). Then \(\tau=\sigma\setminus\{f\}\) contains \(e\), hence lies in \(B\setminus A\). It is a free codimension-one face of \(\sigma\), by the unique-completion property. The pairs \((\tau,\sigma)\) for different missing perfect matchings are disjoint (a shared \(\tau\) would contradict uniqueness); all can be removed by elementary simplicial collapses *relative to \(A\)*, in any order. Denote the resulting complex by \(B'\supseteq A\). The inclusion of pairs \((B',A)\to(B,A)\) is a homotopy equivalence of pairs, and **every relative** \((m-1)\)-simplex has disappeared. A top-dimensional simplex already in \(A\) is not removed.

Consequently \(C_{m-1}(B',A;\mathbb Z)=0\), so \(H_{m-1}(B,A;\mathbb Z)=0\). Further, \(H_{m-2}(B,A;\mathbb Z)\) is isomorphic to a subgroup of the free relative chain group \(C_{m-2}(B',A;\mathbb Z)\), hence is free. The long exact sequence of the pair \((B,A)\) now reads in the relevant range

\[
0\longrightarrow\widetilde H_{m-2}(A;\mathbb Z)
\xrightarrow{\iota_*}\widetilde H_{m-2}(B;\mathbb Z)
\longrightarrow H_{m-2}(B,A;\mathbb Z).
\]

The cokernel of \(\iota_*\) injects into a free abelian group, so is free. Thus \(\iota_*\) is injective with a direct-summand image. Applying the same free-face argument to every top simplex of an individual matching complex removes all its \((m-1)\)-simplices, leaving a complex of dimension at most \(m-2\); its homology in that degree is the kernel of a boundary from a free chain group and is therefore free. For a finite nested filtration, these saturated inclusions form a chain of saturated sublattices inside the final free homology group. Successively choosing bases for their free successive quotients yields a simultaneously adapted basis (not canonically). This proves all universal statements.

**Eight-vertex cofiber.** With \(F\) as in the Finding, the standalone exact verifier enumerates 512 and 763 nonempty faces of \(\mathcal M(K_8-F)\) and \(\mathcal M(K_8)\). Two complete acyclic discrete-Morse matchings leave respectively only one critical vertex and 79 two-cells, or one critical vertex and 132 two-cells. Such CW complexes are wedges of two-spheres. The just-proved primitive inclusion therefore has matrix equivalent over the integers to the standard inclusion \(\mathbb Z^{79}\hookrightarrow\mathbb Z^{132}\), whose associated map between these simply connected sphere wedges is homotopic, after homotopy self-equivalences, to the inclusion of the first 79 wedge summands. Its mapping cofiber is \(\bigvee^{53}S^2\). The script separately verifies all 45 relative free-face pairs for absent top simplices; the uniform proof above, rather than finite testing, establishes the theorem for every \(m\).

**Sharp lower-degree failure.** The matching complex of the six-cycle, with two additional isolated graph vertices, has exactly six zero-simplices, nine one-simplices, and two triangles. Its triangles each contain a free edge, and both can be collapsed; the resulting graph is connected with seven edges and six vertices, so its first integral homology is \(\mathbb Z^2\). The eight-vertex complete matching complex is a wedge of 132 two-spheres, with zero first homology. Thus inclusion fails to be injective one degree below the theorem.

## Verification

Run `python verify.py` using only the Python standard library. It reconstructs all matching faces, validates every oriented Hasse cover and full acyclicity of both deterministic Morse matchings (1,368 and 2,100 covers), their critical-face histograms, all 45 relative collapse witnesses, and the cycle-complex sharpness face vector and connectivity. The supplied `verification_output.txt` is the actual recorded output of the embedded script; counts alone are not used as proof of the universal result.

## Relationship to prior work

Mondal–Mukherjee–Saha (first posted 2023) explicitly give the homotopy type and 132 two-spheres of the complete eight-vertex matching complex. A previously published separate finite classification determines the 79-sphere type after deleting four independent graph edges. Neither individual homotopy type specifies the homology map between them; two free groups of those ranks can have nonprimitive or even noninjective connecting maps. Jonsson's 2008/2012 *Exact Sequences* gives the one-edge long exact sequence for complete matching complexes and states in Conjecture 6.2 that a stronger all-degree short exact sequence should split. Here only the even-order **degree \(m-2\) split-injectivity**, for arbitrary graph edge inclusions, is proved; the conjectured all-degree surjectivity and splitting are **not** claimed. The lower-degree failure does not contradict the complete-graph conjecture, because its source is a different graph. Comparable non-matching and perfect-matching extendibility filtrations concern distinct simplicial complexes.

## Limitations

No statement is made for odd graph order, lower homological degrees, equivariant splittings, canonical bar generators, or a general formula for the rank of the cokernel. The eight-vertex cofiber decomposition uses the established integral split-inclusion and finite exact matchings. The result has not undergone independent scientific audit; an unindexed or otherwise inaccessible equivalent general theorem remains a bibliographic risk.

## References

1. A. Mondal, S. Mukherjee and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, first posted 2023-05-04, particularly Example 3.3 for \(\mathcal M(K_8)\). https://arxiv.org/abs/2305.02973
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, J. Combin. Theory Ser. A 115 (2008), 1504–1526; accessible preprint arXiv:1203.5641, Section 3.4 and Conjecture 6.2. https://arxiv.org/abs/1203.5641
3. *A 79-sphere matching complex after perfect-matching deletion from \(K_8\)*, previously published calculation (2026): this provides the source's nonequivariant homotopy type, not the induced integral map. https://github.com/published-finding corpus/2026
