# The 164-level tetrahedral volume spectrum and maximal grand-cell tetrahedra of the regular 600-cell

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and let \(H\subset\mathbb R^4\) be the regular 600-cell of circumradius one. For every unordered four-element subset of its 120 vertices, let \(V\) be the intrinsic Euclidean 3-volume of the tetrahedron they span (zero for affine dependence).

**Complete finite classification.** Across all \(\binom{120}{4}=8{,}214{,}570\) subsets, exactly 164 distinct values of \(V^2\) occur. Every squared volume has the form \((A+B\varphi)/2304\) with integral \(A,B\); the complete exact frequency table appears in `verification/SPECTRUM.csv`, with columns \(A,B,\mathrm{multiplicity}\). The table includes 72,570 zero-volume subsets and is ordered by decreasing squared volume.

**Extremal theorem.** The largest volume of *any* tetrahedron whose four points lie anywhere in the convex body \(H\) is
\[
V_{\max}=\frac{\varphi^3}{6\sqrt2}.
\]
Exactly 600 **vertex-supported** tetrahedra attain it; all are regular, with each edge length \(\varphi\). Their edge, triangle and tetrahedron incidence numbers are respectively 720, 1200 and 600; each such edge belongs to 5 maximal tetrahedra, and each triangle to 2. These are the known cells of the regular star polytope called the *grand 600-cell*, here characterized by a volume extremum. No uniqueness statement is made about tetrahedra with nonvertex points.

The **second-largest vertex-supported** volume is
\[
V_{\mathrm{next}}=\frac{\sqrt{10+15\varphi}}{12},
\]
attained by exactly 3,600 four-vertex subsets. The sharp squared-volume gap between the largest and next-largest vertex-supported levels is \(\varphi/144\).

## Assumptions and scope

Work in standard Euclidean \(\mathbb R^4\) with the 600-cell centered at zero and of circumradius one. Its vertex set is the union of 8 signed coordinate-unit vectors, 16 vectors \((\pm1,\pm1,\pm1,\pm1)/2\), and 96 vectors obtained by even coordinate permutations of \((0,\pm1,\pm\varphi,\pm\varphi^{-1})/2\), with arbitrary independent nonzero signs. Four-vertex tetrahedra have intrinsic 3-volume, not four-dimensional content. A regular 600-cell's full symmetry group acts transitively on its 120 vertices; equivalently, its unit-quaternion realization is closed under left multiplication.

## Proof

**1. Exact volume encoding.** Represent each coordinate as \((a+b\varphi)/2\), \(a,b\in\mathbb Z\). For four vertices \(p,q,r,s\), set \(X=(q-p,r-p,s-p)\) and \(G=X^\top X\). The tetrahedron satisfies \(36V^2=\det G\). Since \(\varphi^2=\varphi+1\), exact multiplication in \(\mathbb Z[\varphi]\) uses
\[
(a+b\varphi)(c+d\varphi)=(ac+bd)+(ad+bc+bd)\varphi.
\]
The unscaled doubled-coordinate vectors have Gram determinant \(A+B\varphi\); the actual determinant is \((A+B\varphi)/64\), hence \(V^2=(A+B\varphi)/2304\). Exact ordering is decided without floating point: the sign of \(a+b\varphi\) is the sign of \((2a+b)+b\sqrt5\), determined by integer squaring after examining signs.

**2. Exhaustive anchored reduction.** Vertex-transitivity allows a first vertex to be fixed at \(p=(1,0,0,0)\). There are exactly \(\binom{119}{3}=273{,}819\) distinct triples of remaining vertices. The accompanying standalone code constructs all 120 distinct normalized vertices, computes each anchored Gram determinant in the quadratic integer ring, and independently recomputes it by the four 3-by-3 Cauchy–Binet minors. It checks all triples, not a sample. Its exact counts are 164 distinct determinant pairs, a unique highest pair \((A,B)=(160,256)\) with 20 anchored tetrahedra, and a unique next pair \((160,240)\) with 120 anchored tetrahedra. Every anchored tetrahedron corresponds, by transitivity, to \(120/4=30\) distinct full-set tetrahedra. Thus there are 600 maximizers and 3,600 runners-up, with all spectrum multiplicities equal to 30 times the anchored multiplicities. The code matches every count against the provided full table, whose multiplicities sum to \(\binom{120}{4}\).

**3. Regularity and star-cell incidence.** The code checks that all six squared edge lengths of every anchored maximum equal \(1+\varphi=\varphi^2\). By transitivity this holds for all 600 vertex-supported maximizers. The exact Gram value is \((160+256\varphi)/64=(5+8\varphi)/2=\varphi^6/2\), giving \(V_{\max}^2=\varphi^6/72\). An independent graph construction joins pairs of vertices at squared distance \(\varphi^2\). Exact enumeration gives a 12-regular graph with precisely 600 four-cliques; these contain exactly 720 edges (5 cliques each) and 1,200 triangles (2 cliques each). This reproduces the grand 600-cell's classical incidence counts without presuming its volume extremality.

**4. Any contained tetrahedron.** For fixed choices of three of the points, the map of the fourth point to the tetrahedron's 3-volume is the norm of an affine vector (the exterior product of three edge vectors), divided by six. It is convex on \(H\), so its maximum occurs at some vertex of \(H\). Replacing the four points successively by vertices does not decrease volume. Therefore the exhaustive vertex bound holds for all tetrahedra contained in \(H\). This argument guarantees vertex-supported maximizers but does not classify possible nonvertex equality cases.

**5. Second level.** The next exact determinant pair is \((160,240)\), yielding \(V^2=(10+15\varphi)/144\). Its squared separation from \(\varphi^6/72\) is exactly \(\varphi/144\). No statement is asserted about a runner-up among arbitrary nonvertex tetrahedra, where volumes can vary continuously toward the maximum.

## Verification

Run `python verification/check_600cell.py` in the directory containing this document and the `verification` folder. This uses the Python standard library only, independently checks Gram versus Cauchy–Binet for all 273,819 anchored triples, verifies all 164 multiplicities against `verification/SPECTRUM.csv`, confirms the grand-cell clique incidence data, and checks the two exact top determinant pairs. It prints `600CELL_TETRA_EXACT_PASS` on success. It never substitutes random sampling or floating-point comparison for exact ordering.

## Relationship to prior work

The regular 600-cell, its 120 unit-icosian vertices, symmetry and its 600 small tetrahedral boundary cells are classical. Denney et al., *The Geometry of H4 Polytopes* (arXiv:1912.06156v1, 2019), describe its quaternionic symmetries and 24-cell structures, not the 164-value tetrahedral volume spectrum or the largest contained tetrahedron theorem. The grand 600-cell (regular star polytope \(\{3,3,5/2\}\)) and its 600 regular tetrahedral cells are also classical; their existence and incidence counts are not claimed as new. The additional statement here is that those cells are **exactly the vertex-supported global volume maximizers**, together with a complete frequency spectrum, sharp next vertex-supported value, and unrestricted volume bound. Results on **four-dimensional four-simplices** with five vertices of the 600-cell concern a different determinant and do not imply these three-dimensional four-vertex claims.

## Limitations

Historical priority remains provisional because books on regular star 4-polytopes and all historical tables have not been exhaustively inspected. The proof is a finite exhaustive exact-arithmetic certificate plus the analytical vertex reduction; the checker and table are essential evidence. There is no classification here of nonvertex equality cases for maximal contained tetrahedra. This finding has no independent mathematical audit.

## References

1. T. Denney, D. Hooker, D. Johnson, T. Robinson, M. Butler, S. Claiborne, *The Geometry of H4 Polytopes*, arXiv:1912.06156v1 (first public posting 2019-12-12), especially sections 1, 2, and 7. https://arxiv.org/pdf/1912.06156
2. H. S. M. Coxeter, *Regular Polytopes*, third edition, Dover, 1973; cited for classical regular and star polytope background, with no claim of full-text verification here.
3. J. H. Conway, H. Burgiel, C. Goodman-Strauss, *The Symmetries of Things*, 2008, chapter 26, for regular star-polytopes; cited for classical context, with no claim of full-text verification here.
4. *Grand 600-cell*, descriptive entry and referenced background, https://en.wikipedia.org/wiki/Grand_600-cell (checked 2026-11-09).
