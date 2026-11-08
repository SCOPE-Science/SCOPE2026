# Exact central-section polygon probabilities of the regular truncated cube

## Finding
Let \(K\subset\mathbb R^3\) be the regular truncated cube with vertex set consisting of every coordinate permutation of \((\pm(\sqrt2-1),\pm1,\pm1)\), with independent signs. Let \(U\) be uniform on the unit sphere and let \(N(U)\) be the number of vertices of the planar convex polygon \(K\cap U^\perp\). Set
\[
\alpha=\arccos\frac{7-4\sqrt2}{17},\qquad
\beta=\arccos\frac{5+2\sqrt2}{17},\qquad
\gamma=\arccos\frac{3+8\sqrt2}{17}.
\]
Then \(N(U)\) takes exactly four values with positive probability, and its complete law is
\[
\begin{aligned}
\Pr(N=4)&=3-\frac{6\alpha}{\pi},\\
\Pr(N=6)&=4+\frac{6\alpha-12\beta-12\gamma}{\pi},\\
\Pr(N=8)&=-12+\frac{6\alpha+24\beta+6\gamma}{\pi},\\
\Pr(N=10)&=6+\frac{-6\alpha-12\beta+6\gamma}{\pi}.
\end{aligned}
\]
In the order \(4,6,8,10\), the probabilities are approximately \(0.1510526933\), \(0.5002272883\), \(0.2813973563\), and \(0.0673226622\). A finer geometric classification shows that the twelve great circles induced by antipodal vertex pairs partition the normal sphere into exactly \(134\) convex spherical cells: \(6\) cells of section type four, \(32\) of type six, \(72\) of type eight, and \(24\) of type ten.

## Assumptions and scope
The body is the single regular truncated cube specified above, up to any overall positive similarity. The plane is **central**, through the cube's origin, and its unoriented normal has the rotation-invariant probability distribution. At the measure-zero set of orientations in which the plane contains a polyhedron vertex, we do not assign a polygon type; the probability law is unchanged. No claim is made for translated planes, nonregular truncations, or other Archimedean solids. In this normalization there are \(24\) vertices and \(36\) edges of squared length \(12-8\sqrt2\).

## Proof
**1. Section vertices and critical great circles.** Put \(t=\sqrt2-1\). The vertex representation equals the halfspace description \(K=[-1,1]^3\cap\{x:|x_1|+|x_2|+|x_3|\le 2+t\}\): it is a cube with all eight corners equally truncated. It has twelve residual cube-edge segments of length \(2t\) and twenty-four new triangular-face edges of length \(\sqrt2(1-t)=2t\), giving exactly \(36\) edges. Each of the \(36\) edges \([v,w]\) meets a generic central plane in its relative interior if and only if \((U\cdot v)(U\cdot w)<0\). Since the body is convex and every nondegenerate plane-section vertex arises on one crossed edge, \(N(U)\) is exactly the number of edges with opposite endpoint signs. The \(24\) vertices form \(12\) antipodal pairs; choose one representative normal \(n_i\) from each pair. The sign of \(U\cdot n_i\) changes precisely along its great circle. Consequently \(N(U)\) is constant on each open chamber cut out by these twelve circles.

**2. Complete finite chamber enumeration.** Arithmetic is exact in \(\mathbb Q(\sqrt2)\). There are \(\binom{12}{2}=66\) distinct pairs of great circles, each giving two antipodal crossing points; all \(132\) crossing points lie on exactly two circles (the bundled exact verifier tests the nonzero cross products and the absence of triple incidences). Euler's formula for a connected arrangement of transverse great circles yields \(132+2=134\) faces. To enumerate every face, at each crossing \(c\) of circles \(i,j\), take the four infinitesimal sign-sector witnesses represented concretely by \(10^5c\pm n_i\pm n_j\), taking the chosen representative \(c\) as the raw cross product. Exact comparisons verify that these witnesses lie in the four expected sectors and never on another circle. The \(528\) witnesses produce exactly \(134\) distinct twelve-bit sign patterns, hence enumerate all faces by the Euler count. Every face is a geodesically convex intersection of signed hemispheres and has its vertices among the crossing points whose other ten signs satisfy its inequalities.

**3. Exact cell geometry.** All \(n_i\) have squared length \(5-2\sqrt2\). At a corner meeting signed halfspaces \(\varepsilon_i U\cdot n_i\ge0\) and \(\varepsilon_j U\cdot n_j\ge0\), the interior spherical angle is \(\pi-\arccos\bigl(\varepsilon_i\varepsilon_j(n_i\cdot n_j)/(5-2\sqrt2)\bigr)\). Rationalizing the denominator gives only the signed values \(\pm\cos\alpha\), \(\pm\cos\beta\), and \(\pm\cos\gamma\). All face-sign patterns, endpoint edge-crossing tests, and corner-normal cosines are enumerated exactly by the bundled verifier; the resulting full, finite table is:

| Number of cells | Section vertices | Spherical cell sides | Cell spherical area |
| ---: | ---: | ---: | --- |
| 6 | 4 | 4 | \(2\pi-4\alpha\) |
| 24 | 6 | 5 | \(2\alpha-2\beta-\gamma\) |
| 8 | 6 | 6 | \(2\pi-3\alpha-3\gamma\) |
| 48 | 8 | 3 | \(\alpha+\beta+\gamma-\pi\) |
| 24 | 8 | 4 | \(2\beta-\alpha-\gamma\) |
| 24 | 10 | 4 | \(\pi+\gamma-2\beta-\alpha\) |

For completeness, the signed normal-cosine lists before application of spherical excess are, in table order: four copies of \(+\cos\alpha\); two copies of \(-\cos\alpha\), two of \(+\cos\beta\), one of \(+\cos\gamma\); three of \(+\cos\alpha\), three of \(+\cos\gamma\); one each of \(-\cos\alpha,-\cos\beta,-\cos\gamma\); one \(+\cos\alpha\), two \(-\cos\beta\), one \(+\cos\gamma\); and one \(+\cos\alpha\), two \(+\cos\beta\), one \(-\cos\gamma\). For a spherical \(k\)-gon the area is \(2\pi\) minus the sum of the \(k\) arccosines of these signed cosines, by Girard's theorem; this proves the six area expressions without numerical integration.

**4. Haar probabilities.** Divide the total area of all cells of each section type by the sphere's area \(4\pi\). Summing the relevant table rows and simplifying yields all four displayed probabilities. The total is exactly one. Every listed cell has strictly positive area (as certified from the explicit trigonometric values), so no section type disappears.

**5. Independent exact expectation identity.** Every one of the 36 edges connects vertices of equal squared norm \(5-2\sqrt2\), with normalized endpoint dot product \((3+8\sqrt2)/17=\cos\gamma\). A Haar-uniform normal separates the two endpoints with probability \(\gamma/\pi\) (a spherical lune). Linearity of expectation independently gives \(\mathbb E[N]=36\gamma/\pi\), which agrees identically with the four probabilities above.

## Verification
The included standalone `verify_exact.py` uses only Python's standard library to execute all comparisons in \(\mathbb Z[\sqrt2]\); floating-point calculations occur **only after** exact face classification and are used for displaying spherical areas and probabilities. It verifies 24 distinct vertices, 36 minimal-distance edges, 132 unique circle crossings with no triple incidences, 134 distinct sign chambers, and all six rows of the cell table. The program reports total area divided by \(4\pi\) agreeing with one to numerical precision.

An independent `verify_simulation.py` uses NumPy to sample 500,000 Haar directions and counts crossed edges directly. The resulting empirical probabilities are \(0.151326,0.500214,0.280938,0.067522\), with maximum absolute discrepancy below \(0.00046\). It also verifies the expected vertex-count identity numerically. This simulation is corroborating evidence, not the completeness proof; the exhaustive exact 134-cell classification and spherical-excess argument provide the finite proof.

Reproduction: run `python verify_exact.py`, then optionally `python verify_simulation.py` with NumPy installed. No external files, solver licenses, or downloads are needed.

## Relationship to prior work
Lonke, *On random sections of the cube*, first public arXiv version 1998-12-21, derives expected face counts for central random sections of cubes, not the complete four-point polygon-type distribution of the regular truncated cube. Finch, *Width Distributions for Convex Regular Polyhedra*, first public version 2011-10-04, studies width moments of the cube and tetrahedron rather than this section-type law. Earlier stereological literature, including Socha's *Random plane section of a polyhedron*, studies different sampling models and sectional angular quantities. The Archimedean solid's 24-vertex, 36-edge coordinates are standard. The present exact cell-area classification and resulting probabilities have not been identified in the inspected statements; this is a best-knowledge originality comparison, not a guarantee of historical priority.

## Limitations
The theorem is for **central Haar-uniform planes only**. A random affine plane under a translation-invariant line/plane measure requires a separate choice of offset distribution and has a different law. The proof is an exhaustive exact finite-algebra certificate for this particular polyhedron; no universal formula for arbitrary truncated cubes is inferred. No independent audit or mathematical validation has been performed. Published generic arrangement methods could implicitly permit computation of this special case, although no earlier explicit four-probability result was identified in the checked sources.

## References
1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1, first posted 1998-12-21. https://arxiv.org/abs/math/9812123
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, first posted 2011-10-04. https://arxiv.org/abs/1110.0671
3. M. Socha, *Random plane section of a polyhedron*, Acta Stereologica 7 (1988). https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf
4. E. W. Weisstein, *Truncated Cube*, MathWorld. https://mathworld.wolfram.com/TruncatedCube.html
5. Exact geometric enumeration and independent simulation: `verify_exact.py`, `verify_simulation.py` (included).
