# Complete Euclidean Vietoris–Rips homotopy filtration of the rhombic dodecahedron

## Finding
Let \(P\subset\mathbb R^3\) consist of the fourteen points
\[
P=\{(\varepsilon_1,\varepsilon_2,\varepsilon_3):\varepsilon_i\in\{-1,1\}\}\cup\{\pm2e_1,\pm2e_2,\pm2e_3\}.
\]
These are the vertices of the regular rhombic dodecahedron of edge length \(\sqrt3\). For every real \(r\ge0\), the **inclusive** Vietoris–Rips complex, whose nonempty simplices are subsets of diameter at most \(r\), has the following integral homotopy type:
\[
\boxed{\operatorname{VR}_{\le r}(P)\simeq
\begin{cases}
\bigvee^{13}S^0,&0\le r<\sqrt3,\\
\bigvee^{11}S^1,&\sqrt3\le r<2,\\
S^2,&2\le r<2\sqrt2,\\
S^3,&2\sqrt2\le r<\sqrt{11},\\
S^6,&\sqrt{11}\le r<2\sqrt3,\\
\ast,&r\ge2\sqrt3.
\end{cases}}
\]
Equivalently, the only nonzero **reduced** integral persistence intervals are thirteen in degree zero on \([0,\sqrt3)\), eleven in degree one on \([\sqrt3,2)\), and a single interval each in degrees two, three, and six on \([2,2\sqrt2)\), \([2\sqrt2,\sqrt{11})\), and \([\sqrt{11},2\sqrt3)\), respectively. The conclusion holds over every coefficient field as well.

## Assumptions and scope
The metric is the ordinary Euclidean distance **between the fourteen displayed vertices**, not graph shortest-path, intrinsic surface distance, or a sample of the entire boundary. The convention includes simplices whose diameter equals the threshold. The edge length is fixed at \(\sqrt3\); scaling the model uniformly scales every endpoint. A zero-fold wedge is not used: the first stage consists of fourteen isolated vertices.

## Proof
**Exact distance shells.** The squared distances of distinct vertices take precisely the values \(3,4,8,11,12,16\), with unordered-pair multiplicities \(24,12,24,24,4,3\). For a cube corner \(\varepsilon\) and an axial vertex \(2s e_i\), the squared distance is \(3\) when \(\varepsilon_i=s\) and \(11\) otherwise. Between two cube corners, the squared distance is four times their Hamming distance. Two distinct axial vertices lie at squared distance \(8\) if their axes differ and \(16\) if they are opposite. Thus there are no other changes in the filtration.

**Squared threshold \(3\).** The 24 short edges are exactly the incidences of cube corners with their three signed coordinate facets. They form the connected, bipartite, fourteen-vertex rhombic-dodecahedral graph. This graph has no triangles and has cycle rank \(24-14+1=11\); it is homotopy equivalent to eleven circles.

**Squared threshold \(4\).** Twelve cube-corner edges are added, each spanning a short diagonal of one of the twelve rhombic facets. Every rhombic facet is consequently split into two triangles, and these are precisely the 24 triangles in the flag complex: any triangle must contain one axial vertex and two cube corners. No tetrahedra occur. Hence the complex is the triangulated boundary of the convex rhombic dodecahedron and is homeomorphic to \(S^2\).

**Squared threshold \(8\).** The induced complex on the eight cube corners contains every possible edge except the four pairs of antipodal corners. Therefore it is the join of four copies of \(S^0\), namely a triangulated \(S^3\). To show that the full fourteen-vertex complex has this same integral homotopy type, remove the six axial vertices in the order \((-2,0,0),(2,0,0),(0,-2,0),(0,2,0),(0,0,-2),(0,0,2)\), exactly as listed after the cube vertices in the certificate. At each removal, the link of the axial vertex in the remaining complex is simplicially collapsible to a point. The successive link-face counts are \(39,39,23,23,15,15\), and explicit link collapses take \(19,19,11,11,7,7\) pairs, respectively. If a link collapses by pairs \((\sigma,\tau)\) to vertex \(w\), the star of the removed vertex \(v\) collapses **relative to the deletion** by pairs \((v\cup\sigma,v\cup\tau)\), followed by \((\{v\},\{v,w\})\). The supplied 80-pair certificate lists these actual global elementary collapses; the standalone checker reconstructs every face and verifies that each lower face has exactly one proper containing face at the instant of removal. The final subcomplex is exactly the eight-corner cross-polytope boundary. Elementary collapses preserve integral homotopy type, so this stage is \(S^3\).

**Squared threshold \(11\).** The only missing edges in the fourteen-vertex graph are the seven mutually disjoint antipodal pairs: four among cube corners and three among axial vertices. Its flag complex is therefore the join of seven copies of \(S^0\), homeomorphic to \(S^6\).

**Squared threshold \(12\) and above.** All eight cube corners are adjacent to each other and to all six axial vertices; in particular, any cube corner is a cone vertex of the entire flag complex. It is contractible. At squared threshold \(16\) the full simplex appears, but the homotopy type does not change.

**Persistence.** Each noncontractible positive-degree stage has reduced integral homology concentrated in a different degree, so all maps between consecutive positive-degree homology groups vanish. The first fourteen components merge into one at \(\sqrt3\). All filtration intervals displayed in the finding follow exactly, with no torsion or extension ambiguity because the homotopy types are proved integrally.

## Verification
Run `python3 verify.py` in the same directory as `collapse_certificate.json`, using Python's standard library. The verifier independently reconstructs all fourteen coordinates and all \(91\) pair distances, enumerates all nonempty simplices at the five nontrivial squared thresholds, checks every one of the 80 elementary collapse pairs against the *current* face set, and confirms the remaining complex has exactly the four antipodal forbidden pairs on eight vertices. It also checks that every vertex link at squared threshold \(4\) is a circle, tests the antipodal decompositions at squared thresholds \(11\) and \(12\), and independently computes the complete reduced mod-two Betti vectors at squared thresholds \(3,4,8,11\).

The face vectors at squared thresholds \(3,4,8,11\) are \((14,24)\), \((14,36,24)\), \((14,60,100,60,6)\), and \((14,84,280,560,672,448,128)\). The corresponding nonzero reduced Betti numbers are \(\widetilde\beta_1=11\), \(\widetilde\beta_2=1\), \(\widetilde\beta_3=1\), and \(\widetilde\beta_6=1\). These field calculations corroborate but do not replace the integral homotopy proof above.

## Relationship to prior work
Saleh, Titz Mite and Witzel (2023) determine the vertex-set Vietoris–Rips complexes of all five **Platonic** solids; their full paper explicitly proposes other solid families as extensions. The rhombic dodecahedron is a **Catalan** solid, not one of their five objects. Saleh's dissertation (2023) contains sampled-sphere experiments involving the distinct **rhombic triacontahedron** of 32 vertices; it does not supply the fourteen-vertex theorem here.

The published complete Euclidean cuboctahedron filtration studies the twelve vertices of the **dual** Archimedean polyhedron. Duality of polyhedra does not preserve vertex distances, vertex number, or Vietoris–Rips complexes, and that statement does not imply the six-stage filtration above. A separate study of the canonical spectral rhombic dodecahedron calculates its precise vertex coordinates and radial shells, but does not establish its Rips homotopy or persistence. General cross-polytope join facts explain the last spherical stage but do not determine the intermediate \(S^3\) collapse.

## Limitations
This is the complete finite-vertex **Euclidean chord-distance** filtration of a fixed regular realization, not a statement about other rhombic dodecahedra, their surfaces, or geometric perturbations. The elementary-collapse certificate is finite, exhaustive, and independently replayable but is not an external formal certification. An unindexed prior classification in alternative terminology cannot be ruled out. No equivariant homotopy or representation-valued persistence is claimed.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, publicly posted 2023-02-28, DOI 10.2140/iig.2024.21.17.
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation, September 2023, DOI 10.22029/jlupub-17950; particularly contents and Chapter 2, including the rhombic-triacontahedron experiment.
3. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, publicly accessible published-finding corpus mathematical research record (2026), `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e`.
4. *The exceptional spectral rhombic dodecahedron is tangential but has two exact vertex shells*, publicly accessible published-finding corpus mathematical research record (2026), `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-exceptional-spectral-rhombic-dodecahedron-is-tangential-but--87310d87ca2a`.
