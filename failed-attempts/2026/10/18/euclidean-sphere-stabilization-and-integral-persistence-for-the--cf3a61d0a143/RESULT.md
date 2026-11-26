# Euclidean sphere stabilization and integral persistence for the truncated-octahedral Rips filtration

## Finding
Let \(P\subset\mathbb R^3\) be the set of the \(24\) signed coordinate permutations of \((0,1,2)\), with its **ambient Euclidean distance**, and put \(K_r=\operatorname{VR}_{\le r}(P)\). Then for every real \(0\le r<\sqrt{14}\),
\[
K_r\simeq
\begin{cases}
\bigsqcup^{24}\mathrm{pt},&0\le r<\sqrt2,\\
\bigvee^{13}S^1,&\sqrt2\le r<2,\\
\bigvee^{7}S^1,&2\le r<\sqrt6,\\
\bigvee^{9}S^2,&\sqrt6\le r<\sqrt8,\\
S^2,&\sqrt8\le r<\sqrt{14}.
\end{cases}
\]
Both inclusions \(K_{\sqrt8}\hookrightarrow K_{\sqrt{10}}\hookrightarrow K_{\sqrt{12}}\) are integral homology isomorphisms and homotopy equivalences. The natural map
\[
H_2(K_{\sqrt6};\mathbb Z)\cong\mathbb Z^9
\longrightarrow H_2(K_{\sqrt8};\mathbb Z)\cong\mathbb Z
\]
is surjective, with free kernel of rank \(8\). Thus eight degree-two persistence classes die at \(\sqrt8\), while one born at \(\sqrt6\) survives through all \(r<\sqrt{14}\). Its death after this cutoff is not determined here. In degree one there are six bars \([\sqrt2,2)\) and seven bars \([\sqrt2,\sqrt6)\); there are no other positive-dimensional bars within the stated range.

## Assumptions and scope
All distances are the **unrescaled Euclidean chord distances**, not shortest-path distances on the polyhedron's edge graph. A nonempty subset of \(P\) is a simplex of \(K_r\) precisely if every pair is at distance at most \(r\). The ten positive squared pairwise distances are \(2,4,6,8,10,12,14,16,18,20\). The conclusion covers exactly the six finite Rips stages at squared thresholds \(2,4,6,8,10,12\), as well as the discrete stage before \(\sqrt2\). There is no claim at or above \(\sqrt{14}\). The main new phenomenon is that the geometric sphere appears already at the *first* of the three Euclidean subdivisions of the graph-distance-three shell.

## Proof
**1. Complete finite Morse certificates.** Order the vertices lexicographically by their integer coordinates. Construct every clique of the graph whose edges satisfy \(\|u-v\|^2\le t\). The exact nonempty face vectors, with \(t=r^2\), are
\[
\begin{array}{c|l|r|l}
t &(f_0,f_1,\ldots)&\text{Morse pairs}&\text{critical dimensions and counts}\\\hline
2&(24,36)&23&0:1,\ 1:13\\
4&(24,48,24,6)&47&0:1,\ 1:7\\
6&(24,96,112,30)&126&0:1,\ 2:9\\
8&(24,120,208,150,48,8)&278&0:1,\ 2:1\\
10&(24,144,328,342,168,32)&518&0:1,\ 2:1\\
12&(24,168,472,618,384,92)&878&0:1,\ 2:1.
\end{array}
\]
For each threshold, `certificate.json` specifies every matched pair of cells. The self-contained `verify.py` independently rebuilds all faces, verifies each pair is a codimension-one inclusion and no cell is matched twice, and checks **acyclicity of the entire oriented Hasse diagram**, not merely of an algorithm that generated the matching. The resulting acyclic Forman matchings give CW models with exactly the indicated critical cells. One critical vertex and only critical one-cells give a wedge of circles; one critical vertex and only critical two-cells give a wedge of two-spheres. This proves all stagewise integral homotopy types without extrapolation from numerical homology.

**2. A common geometric integral generator.** The polytope \(Q=\operatorname{conv}(P)\) is the truncated octahedron containing the origin in its interior. Its fourteen facets comprise six square sections \(x_i=\pm2\) and eight hexagonal sections \(\varepsilon_1x_1+\varepsilon_2x_2+\varepsilon_3x_3=3\) for \(\varepsilon_i\in\{\pm1\}\). Triangulate each square by one diagonal. For each cyclically ordered hexagon \((v_0,\ldots,v_5)\), take the central triangle \((v_0,v_2,v_4)\) and the three triangles \((v_0,v_1,v_2)\), \((v_2,v_3,v_4)\), \((v_4,v_5,v_0)\). The resulting triangulated boundary \(B\) has face vector \((24,66,44)\), is homeomorphic to \(S^2\), and every edge of \(B\) has squared length at most \(6\). Thus \(B\subseteq K_{\sqrt6}\subseteq K_{\sqrt8}\subseteq K_{\sqrt{10}}\subseteq K_{\sqrt{12}}\).

No geometric simplex of \(K_{\sqrt{12}}\) contains the origin. Indeed, its maximal cliques have at most six vertices, and the exact verifier checks for each of the \(92\) maximal cliques \(C\) that its vector sum \(s_C=\sum_{v\in C}v\) obeys \(\langle s_C,v\rangle>0\) for every \(v\in C\). Thus all faces lie in open half-spaces through the origin. Radial projection of linear simplex images therefore gives a well-defined continuous map \(p:|K_{\sqrt{12}}|\to S^2\), and similarly on its subcomplexes. On \(B\), radial projection is a homeomorphism \(\partial Q\to S^2\), of degree \(\pm1\).

The Morse results show \(H_2(K_{\sqrt8};\mathbb Z)\), \(H_2(K_{\sqrt{10}};\mathbb Z)\), and \(H_2(K_{\sqrt{12}};\mathbb Z)\) are all \(\mathbb Z\). Since the single common cycle \([B]\) maps by \(p\) to a generator of \(H_2(S^2;\mathbb Z)\), it generates each of these three groups. Therefore their inclusions induce integral homology isomorphisms; moreover all three spaces have homotopy type \(S^2\), so degree \(\pm1\) and Whitehead's theorem make the inclusions homotopy equivalences. The same \([B]\in H_2(K_{\sqrt6};\mathbb Z)\) maps onto a generator at \(\sqrt8\); hence its inclusion map is surjective with kernel \(\mathbb Z^8\).

**3. Earlier first-homology maps.** From squared threshold \(2\) to \(4\), the only new edges are the twelve diagonals of the six square facets. Each is homologous to a two-edge path of original edges by a newly present triangle, so \(H_1(K_{\sqrt2};\mathbb Z)\to H_1(K_2;\mathbb Z)\) is surjective. The Morse ranks \(13\) and \(7\) show six classes die at \(2\). The next complex at \(\sqrt6\) is simply connected, killing the remaining seven. In degree two the nine new classes at \(\sqrt6\) reduce to one at \(\sqrt8\) as proved above. Since the same-model Morse models are integral sphere wedges, no torsion or field-dependent barcode modification is hidden in these ranges.

## Verification
Run `python3 verify.py certificate.json` with Python 3 and no third-party packages. Expected output ends with `RADIAL_SEPARATION_OK` and `VERIFY_OK`. The checker independently enumerates each clique, verifies the six specified face vectors, all \(1,870\) matching pairs, and all \(13,032\) Hasse covers with a full directed acyclicity test. It also identifies the graph-distance shells, constructs the \(44\)-triangle convex-boundary sphere, verifies all boundary edges occur twice and are present by squared threshold \(6\), and certifies positivity of a separating functional on all \(92\) maximal cliques at squared threshold \(12\). Acyclic discrete Morse theory and the explicitly described radial map are the mathematical steps connecting these finite checks to the homotopy and persistence conclusions.

## Relationship to prior work
Adamaszek's work on graph powers explains graph-metric Vietoris–Rips complexes and computes cycle powers, but its graph-distance results do not determine partial **Euclidean** shells for the truncated octahedron. Adamaszek and Adams's 2015 circle result gives exact Rips homotopy and persistence for a different metric space. Saleh, Titz Mite, and Witzel classify Platonic-solid vertex sets, explicitly proposing Archimedean solids as a future direction; the truncated octahedron is Archimedean, not Platonic.

The closely related published calculation *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph* uses the same coordinate vertices, but explicitly equips them with graph shortest-path distance. In fact, the graph-distance-three shell splits under Euclidean squared distance into three nonempty sets of \(24\) pairs each, at \(8\), \(10\), and \(12\). Its known graph-radius-three \(S^2\) stage therefore matches only the last of our three sphere stages; it does not imply the earlier \(\sqrt8\) threshold or either intermediate inclusion equivalence. A separate published four-label permutahedron barcode likewise concerns Kendall adjacent-transposition distance, not Euclidean distance. These are statement-level distinctions, not claims that a literature search proves uniqueness.

## Limitations
The theorem is for this exact finite, unrescaled vertex orbit and the half-open range \(r<\sqrt{14}\). It does not assert death of the surviving sphere at \(\sqrt{14}\), nor provide the later Euclidean homotopy filtration, an equivariant collapse, or an integral decomposition respected by all polyhedral symmetries. The matching certificates are computationally finite but mathematically exhaustive for the stated vertices and thresholds; no claim for higher-dimensional permutahedra is made. Published coverage under terminology not returned by the comparisons remains possible. Independent mathematical review has not been performed.

## References
1. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first public 2011-04-03, particularly the introduction and graph-distance definition.
2. Michał Adamaszek and Henry Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669v1, first public 2015-03-12, especially the homotopy and persistence setup.
3. Nada Saleh, Thomas Titz Mite, and Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28, introduction and Sections 1–4.
4. *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph*, publicly posted finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8.
5. *Complete mod-two Rips persistence of the four-letter permutahedron*, publicly posted finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-mod-two-rips-persistence-of-the-four-letter-permutahedr--5b20bd61b710.
