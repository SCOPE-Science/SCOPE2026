# The sharp second tetrahedron-volume shell of the regular dodecahedron

## Finding

Write \(\varphi=(1+\sqrt5)/2\). Realize the regular dodecahedron \(D\) with its twenty vertices
\[
\mathcal V=\{(\pm1,\pm1,\pm1),\ (0,\pm\varphi,\pm\varphi^{-1}),\ (\pm\varphi^{-1},0,\pm\varphi),\ (\pm\varphi,\pm\varphi^{-1},0)\},
\]
where all signs in each coordinate family are independent. For every four-element vertex subset \(S\subset\mathcal V\), put \(d(S)=6\operatorname{vol}_3(\operatorname{conv}S)\), including \(d(S)=0\) for coplanar subsets. The exact, **complete** distribution is:

| \(d(S)\) | Number of four-element subsets |
|:---|---:|
| \(0\) | 495 |
| \(8-4\varphi\) | 320 |
| \(4\varphi-4\) | 900 |
| \(4\) | 1110 |
| \(8\varphi-8\) | 120 |
| \(4\varphi\) | 900 |
| \(8\) | 400 |
| \(8\varphi-4\) | 150 |
| \(4+4\varphi\) | 320 |
| \(8\varphi\) | 120 |
| \(16\) | 10 |

The values appear in **strictly increasing** order. Consequently the greatest vertex-supported tetrahedral volume is \(8/3\), attained by the ten classically known regular tetrahedra of edge length \(2\sqrt2\). **The new second-largest distinct volume** is
\[
\boxed{V_2=\frac{4\varphi}{3}},
\]
attained by exactly \(120\) unordered vertex tetrahedra. Each of those and only those has the unordered six squared edge lengths
\[
\boxed{\{4,\underbrace{8,8,8,8}_{\text{four edges}},\ 4+4\varphi\}}.
\]
The exact gap to the maximal shell is
\[
\boxed{\frac83-\frac{4\varphi}{3}=\frac{4(2-\varphi)}3>0}.
\]
These are statements about tetrahedra whose four vertices are selected from the **twenty vertices** of \(D\). The complete volume spectrum does **not** extend to continuously variable vertices in \(D\).

## Assumptions and scope

The Euclidean metric is the ordinary one on \(\mathbb R^3\). The coordinate normalization is as displayed; the dodecahedron edge length is \(2/\varphi\). Each unordered four-element subset is counted exactly once. Zero-volume configurations are included in the distribution, though they are not nondegenerate tetrahedra. A uniform similarity scaling by \(s>0\) scales every displayed volume by \(s^3\). No second-best claim is made among all tetrahedra with vertices allowed to move continuously on the faces, edges, or interior of \(D\).

## Proof

**Exact coordinate and arithmetic reduction.** The displayed twenty points are the standard coordinate model of a regular dodecahedron. Put \(\varphi^2=\varphi+1\) and represent \(a+b\varphi\) by \((a,b)\in\mathbb Z^2\). Their ring product is
\[
(a,b)(c,d)=(ac+bd,ad+bc+bd).
\]
This is an exact representation: \(a+b\varphi=0\) only when \(a=b=0\). An exact sign test compares \(A+b\sqrt5\) with zero, where \(A=2a+b\), using the signs of \(A,b\) and the integer \(A^2-5b^2\); there is no numerical tolerance.

**Exhaustive finite certificate.** Fix the deterministic index order defined by the accompanying `check.py`: first the eight cube-coordinate vertices in lexicographic sign order, then for each of four lexicographic sign pairs append the three cyclic coordinate forms. For each \(0\le i<j<k<\ell<20\), calculate
\[
D_{ijkl}=\det(v_j-v_i,v_k-v_i,v_\ell-v_i),\qquad d_{ijkl}=|D_{ijkl}|.
\]
The checker enumerates the entire finite domain of \(\binom{20}{4}=4845\) choices. It calculates all determinants by exact ring operations, performs exact comparisons of the eleven distinct determinant magnitudes, and constructs the complete histogram shown above. This is a finite exhaustive calculation, not extrapolation from sampling. As a separate arithmetic identity check on every quadruple, it forms the \(3\times3\) Gram matrix of the three difference vectors and verifies \(\det(\mathrm{Gram})=D_{ijkl}^2\) exactly in \(\mathbb Z[\varphi]\). Thus the determinant calculation is cross-checked by a different polynomial expression.

**Sharpness and equality cases.** Exact order comparison shows that the greatest two magnitudes are \(16\) and \(8\varphi\), with respective multiplicities \(10\) and \(120\). The checker independently enumerates six squared pairwise distances for every four-tuple. It verifies the **biconditionals**: \(d(S)=16\) if and only if all six squared edges are \(8\), and \(d(S)=8\varphi\) if and only if the squared-edge multiset is \(\{4,8,8,8,8,4+4\varphi\}\). In particular the second-shell equality characterization is geometric, not a restatement of the volume equation. The gap is positive since \(1<\varphi<2\). Every possible four-element subset is covered; there is no further exceptional case.

**Interpretation of the absolute maximum.** The ten largest tetrahedra are the familiar compound of ten regular tetrahedra inscribed in the dodecahedron. Their existence is classical; the spectrum and next distinct shell are the claims examined here. The greatest volume among **all** tetrahedra contained in \(D\) is also \(8/3\): the signed determinant is separately affine in each of four vertices and hence a convex combination of signed vertex-supported determinants, so its absolute value cannot exceed the vertex-supported maximum. This last observation concerns only the absolute maximum, not the next-largest distinct volume for moving points.

## Verification

Run `python3 check.py` with Python 3 and no third-party packages. The program contains all twenty coordinates, the complete loop bounds, exact \(\mathbb Z[\varphi]\) ring operations, the independent Gram determinant test, the complete expected histogram, exact ordering, and geometric equality characterizations. Its first output line is:

`DODECAHEDRON_TETRAHEDRON_SPECTRUM_PASSED vertices=20 configurations=4845 levels=11 runners_up=120 maxima=10 gram_checks=4845`

The program continues by printing all eleven levels and their example vertex indices. The proof of exhaustive scope is that every four-element subset occurs in `combinations(range(20),4)` exactly once. The derivation of actual Euclidean tetrahedral volumes from determinants is the elementary formula \(V=|\det|/6\).

## Relationship to prior work

Leppmeier's 2019 paper on the dodecahedron as a Voronoi cell studies tetrahedral volumes in an associated **icosahedral sphere-center configuration** (a sphere center and three icosahedron vertices). Its tetrahedra and hypotheses differ from tetrahedra on four vertices of the dodecahedron, and it does not provide this determinant histogram or the runner-up classification. The classical ten regular tetrahedra in the dodecahedron and their compound are not presented as new.

Simon and Timofeyev's 2021 preprint concerns inscribed polytopal partitions with symmetry constraints, not a volume enumeration for the vertices of a fixed regular dodecahedron. The published icosahedron tetrahedron-volume spectrum describes a **twelve-vertex icosahedron**, not a twenty-vertex dodecahedron. The published dodecahedral Rips homology classification uses the ten tetrahedra whose graph-metric vertex pairs all have distance three; it does not imply the second Euclidean determinant shell or full histogram. These comparisons distinguish objects, invariants, and the direction of implication rather than titles alone.

## Limitations

Historical publication priority has not been independently established; an earlier geometric table or an equivalent classification in the classical polyhedral-compound literature may exist. The theorem is a finite exact classification of tetrahedra supported at dodecahedron vertices, not a continuous second-best theorem. The complete proof depends on the accompanying finite exact checker plus the elementary determinant-volume identity; neither a decimal computation nor a presumed continuous finite reduction is used for the second-shell assertion. Independent mathematical audit has not been performed.

## References

1. M. Leppmeier, *The Dodecahedron as a Voronoi Cell and its (minor) importance for the Kepler conjecture*, `arXiv:1904.06108`, first public 2019-04-12, https://arxiv.org/abs/1904.06108; open full text https://epub.uni-bayreuth.de/4313/1/Paper_Dodekaeder_Entwurf_B8.pdf.
2. S. Simon and T. Timofeyev, *Inscribed Tverberg-type partitions for orbit polytopes*, `arXiv:2110.09322`, first public 2021-10-18, https://arxiv.org/abs/2110.09322.
3. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, `arXiv:2302.14388` (2023-02-28), https://arxiv.org/abs/2302.14388, for the known ten graph-theoretically exceptional tetrahedra.
4. *Regular dodecahedron* (classical compound-of-five-cubes and ten-tetrahedra context), https://en.wikipedia.org/wiki/Regular_dodecahedron. 
