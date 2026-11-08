# Eight hexagonal sphere classes and an orientation line in truncated-octahedron Rips persistence

## Finding
Let \(T\) be the truncated-octahedral graph on the 24 signed coordinate permutations of \((0,1,2)\), with two vertices adjacent when their squared Euclidean distance is \(2\). Give its vertex set the **shortest-path graph metric**, and write \(X_r=\operatorname{VR}_{\le r}(T)\) for the inclusive Vietoris–Rips complex. Let \(G\) be the group of all signed permutations of three coordinates (order 48), acting simplicially on all \(X_r\), let \(\varepsilon:G\to\{\pm1\}\) be its determinant character, and let \(\mathcal H=\{\pm1\}^3\) be the eight hexagonal faces indexed by their outward diagonal normals.

The **degree-two rational persistence module with its \(G\)-action** is
\[
H_2(X_{\bullet};\mathbb Q)\;\cong\;\mathbb Q[\mathcal H]\otimes\mathbf I_{[2,3)}\ \oplus\ \mathbb Q_{\varepsilon}\otimes\mathbf I_{[2,4)}.
\]
Here \(\mathbf I_{[a,b)}\) denotes the interval persistence module with value \(\mathbb Q\) for \(a\le r<b\), identity structure maps inside the interval, and zero otherwise. The group acts by its ordinary **unsigned permutation action** on the eight basis vectors of \(\mathbb Q[\mathcal H]\), and through \(\varepsilon\) on the remaining line. In particular, the scale-two-to-three map has rational rank one: the eight local hexagonal classes die at scale three, while the global orientation-character class remains present for \(2\le r<4\) and dies at scale four.

An equivalent character statement, for \(g(x)_j=s_jx_{p(j)}\) with \(p\in S_3\) and \(s_j\in\{\pm1\}\), is
\[
\operatorname{tr}\big(g\mid H_2(X_2;\mathbb Q)\big)
=\operatorname{sgn}(p)\prod_{j=1}^3s_j+\#\{n\in\mathcal H:g(n)=n\},
\qquad
\operatorname{tr}\big(g\mid H_2(X_3;\mathbb Q)\big)
=\operatorname{sgn}(p)\prod_{j=1}^3s_j.
\]
The already published **nonequivariant** homotopy types \(X_2\simeq\bigvee^9S^2\) and \(X_3\simeq S^2\), and the vanishing of degree-two homology at all other graph-metric scales, are used as input and are **not** claimed as new. The mod-two statement that one degree-two class survives from scale two through scale three is also already published [3]; the new assertion is the **precise natural 48-element symmetry representation and its geometric separation into eight hexagonal face classes and the determinant line**.

## Assumptions and scope
Coordinates are exactly the permutations and independent sign changes of \((0,1,2)\); the zero-coordinate sign does not create a new point. Pairs with squared Euclidean separation greater than \(2\) are not graph edges. Only shortest-path distance in the resulting 24-vertex cubic graph defines \(X_r\). The group \(G\) acts by the 48 signed coordinate matrices. The statement is about rational homology and *equivariant persistence maps*, not equivariant homotopy equivalences or an integral splitting of a persistent lattice. The endpoints of the intervals are left-closed and right-open because the diameter bound is inclusive.

For \(n=(n_1,n_2,n_3)\in\mathcal H\), define the hexagonal face vertex set
\[
F_n=\{(n_1q_1,n_2q_2,n_3q_3):(q_1,q_2,q_3)\text{ is a permutation of }(0,1,2)\}.
\]
Its induced graph is a six-cycle. Its six-vertex subcomplex in \(X_2\) is the boundary of an octahedron, since among its 15 pairs exactly the three opposite pairs in the cycle have graph distance \(3\). Let \(z_n\) be a coherently oriented fundamental two-cycle of this octahedral boundary. The orientation can be chosen so that **all** elements of \(G\) carry \(z_n\) to \(z_{gn}\) without a sign.

## Proof
**1. Eight geometric classes.** Number the vertices of any hexagonal face consecutively \(v_0,\ldots,v_5\). The opposite pairs are \((v_0,v_3)\), \((v_1,v_4)\), and \((v_2,v_5)\). A fundamental cycle of its scale-two octahedral boundary is the signed sum of its eight triangles, choosing one vertex from each opposite pair, with alternating product orientation. This is an integral simplicial two-cycle.

The two alternating triangles \(\{v_0,v_2,v_4\}\) and \(\{v_1,v_3,v_5\}\) occur in **no** scale-two tetrahedron. They belong to **no other** hexagonal face. The first assertion means that coefficient extraction on an alternating triangle vanishes on every three-chain boundary; the second distinguishes the eight local classes. The resulting eight independent coefficient functionals pair diagonally with the cycles \([z_n]\), with unit entries. Consequently, they generate a rank-eight direct summand of \(H_2(X_2;\mathbb Z)\) as an abelian group.

For the equivariant orientation, orient the octahedral cycle of the face with normal \((1,1,1)\), then transport it to the remaining faces by the diagonal sign changes. The stabilizer of this base face consists of the six coordinate permutations. Each acts with orientation \(+1\) on its octahedral two-cycle (an exact six-element check, also encoded in `verify.py`). Thus the eight cycles are permuted **without signs** by all 48 elements of \(G\), giving the module \(\mathbb Q[\mathcal H]\).

**2. The ninth class and characters.** The previous complete homotopy classification of these graph-metric Rips stages [2] gives \(H_2(X_2;\mathbb Q)\cong\mathbb Q^9\), \(H_2(X_3;\mathbb Q)\cong\mathbb Q\), and no other positive-degree rational homology at either scale. For each signed coordinate automorphism the simplicial Lefschetz formula evaluates its trace on \(H_2\) as the alternating sum of signs of setwise fixed oriented simplices, less the trace \(1\) on \(H_0\).

The exact complete fixed-simplex calculations give the identities
\[
L_g(X_2)-1=\varepsilon(g)+\#\operatorname{Fix}_{\mathcal H}(g),
\qquad L_g(X_3)-1=\varepsilon(g)
\]
for **every one of the 48 elements**; the enumerated face vectors are \((24,96,112,30)\) at scale two and \((24,168,472,618,384,92)\) at scale three. Thus the one-dimensional quotient of scale-two homology by the eight-face permutation submodule has character \(\varepsilon\), and scale-three homology itself has character \(\varepsilon\). The characteristic-zero representations split by Maschke's theorem, proving the two claimed module identifications.

**3. The scale-two-to-three inclusion.** At scale three, all six vertices of each \(F_n\) form a simplex, so every \(z_n\) bounds: the rank-eight face submodule lies in the inclusion kernel. The nonzero mod-two inclusion was already calculated for this exact graph under its four-letter permutahedral presentation [3]; the supplied certificate independently reconstructs that calculation to identify the transition in the present geometric-cycle model. The complete mod-two boundary ranks at scale two are \(\operatorname{rank}\partial_2=73\) and \(\operatorname{rank}\partial_3=30\); at scale three they are \(145\) and \(326\). A basis of all 39 mod-two two-cycles at scale two, embedded in the scale-three triangle chain group and reduced against **all 618 tetrahedral boundaries**, increases the scale-three boundary span by exactly one. A representative witness has 20 triangles. Thus the induced map \(H_2(X_2;\mathbb F_2)\to H_2(X_3;\mathbb F_2)\) has rank one.

The known sphere-wedge homotopy types [2] give torsion-free integral second homology and vanishing first homology at both stages; reduction modulo two therefore identifies these mod-two groups with the reductions of integral second homology. Nonzero mod-two image forces a nonzero rational map, and the rational target is one-dimensional. Its kernel is exactly the eight-dimensional face submodule. Its quotient and target both carry \(\varepsilon\), so the induced rational map is an equivariant isomorphism on that orientation line after choosing a basis.

**4. Persistence endpoints.** At scales below two, the underlying complex is a discrete set or the graph \(T\), hence has no second homology. The published classification [2] shows the scale-four complex has homology only in degrees four and five; degree-two homology is zero from scale four onward. Combining these facts with the rank-one transition at scale three proves the displayed interval decomposition.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library. It reconstructs the 24 coordinates, 36 edges, all shortest paths and every simplex at scales two and three; enumerates the entire signed-coordinate group of order 48; constructs all eight oriented hexagonal sphere cycles; checks their boundary, unique alternating triangles, and unsigned symmetry permutation action; computes every signed Lefschetz trace; and independently constructs all mod-two two-cycles and three-boundaries to calculate the actual inclusion-map rank. Run `python3 verify.py`. The recorded expected output is `verification_output.txt`, which ends with `VERIFIED_OK`.

The finite certificate is exhaustive on these specifically defined finite complexes; it does not claim to prove any infinite-family result. The use of the published nonequivariant homotopy classification is explicit and indispensable for upgrading the mod-two inclusion information to the rational character-valued persistence statement.

## Relationship to prior work
Saleh, Titz Mite and Witzel [1] classified Vietoris–Rips complexes of Platonic solids and explicitly proposed Archimedean solids as a next setting. Their complete preprint was inspected; it neither treats the truncated octahedron nor its symmetry persistence.

The already published classification [2] treats **this exact graph and metric** and determines the nonequivariant homotopy types at every graph-distance scale. Its full result and proof were inspected: it does not specify the 48-element rational homology characters or identify the eight canonical local hexagonal cycles as an unsigned permutation submodule. A second published calculation [3] treats the isomorphic **four-letter permutahedral graph**, determines the full mod-two barcode, and explicitly obtains **rank one** for the second-homology inclusion from scale two to three. Hence that numerical map rank and the interval multiplicities are **prior knowledge**, not independent novelty, even when combined with [2] to recover the rational rank. What neither classification establishes, individually or jointly, is the 48-element equivariant module structure or the geometric identification of the eight classes killed by the map.

Galetto, Montaño and Wellner [4] study analogous symmetry modules for the Rips complexes of **binary hypercube graphs**, not for the truncated octahedron (which is the rank-four permutahedral graph, not a hypercube). Their vanishing-inclusion result in that different family cannot imply the nonzero map here. The two equivalent models (signed coordinate permutations and the adjacent-swap Cayley graph of \(S_4\)) were compared, together with second graph powers, signed octahedral symmetry, equivariant persistent homology and hexagon-face sphere representatives.

## Limitations
This is an exact finite graph result, not a classification of all Archimedean solids, arbitrary permutahedra, or all degrees of the truncated-octahedron persistence module. The rational persistence splitting need not extend to a canonical integral equivariant splitting. Computation in characteristic two detects nonvanishing of the rational transition because the prior wedge results guarantee freeness; without those hypotheses, that inference would not be justified. An unindexed equivalent equivariant character or geometric-cycle calculation remains an originality risk; the nonequivariant and mod-two numerical persistence results are expressly attributed to prior sources.

## References
1. Nada Saleh, Thomas Titz Mite, Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, publicly posted 2023-02-28, https://arxiv.org/pdf/2302.14388.
2. *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph*, public mathematical record dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8, especially RESULT.md.
3. *Complete mod-two Rips persistence of the four-letter permutahedron*, public mathematical record dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-mod-two-rips-persistence-of-the-four-letter-permutahedr--5b20bd61b710, especially RESULT.md.
4. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1, publicly posted 2026-06-18, https://arxiv.org/abs/2606.20784.
