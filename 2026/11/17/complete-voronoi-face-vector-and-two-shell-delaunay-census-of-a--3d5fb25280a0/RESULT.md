# Complete Voronoi face vector and two-shell Delaunay census of a five-dimensional nonlattice packing

## Finding
Let
\[
D_5=\{z\in\mathbb Z^5:\textstyle\sum_{i=1}^5z_i\equiv0\pmod 2\},\quad
 t=(1/2,1/2,1/2,1/2,1/2),\quad X=D_5\cup(D_5+t),
\]
and equip \(\mathbb R^5\) with the Euclidean metric given in the displayed coordinates by
\[
q(x)=x_1^2+x_2^2+x_3^2+x_4^2+\frac4{15}x_5^2.
\]
Write \(V\) for the closed nearest-site Voronoi cell of \(0\in X\), and let \(f_k(V)\) count its faces of dimension \(k\).

**Theorem.** The cell \(V\) is a *simple* five-polytope with exactly **74 facets**, all induced by distinct nearest-site vectors, and complete face vector
\[
\boxed{(f_0,f_1,f_2,f_3,f_4)=(864,2160,1872,648,74).}
\]
Its vertices lie on exactly two quadratic-radius shells:
\[
\boxed{\#\{v\in\operatorname{vert}V:q(v)=27/50\}=576,\qquad
\#\{v:q(v)=481/900\}=288.}
\]
Every Voronoi vertex has precisely five other equidistant nearest sites, so the entire dual Delaunay tiling consists of nondegenerate five-simplices. Modulo the translation lattice \(D_5\), there are exactly **192 simplices of squared circumradius \(27/50\)** and **96 of squared circumradius \(481/900\)**, with coordinate determinants respectively \(1\) and \(1/2\), and coordinate volumes respectively \(1/120\) and \(1/240\). Thus the two Delaunay families occupy exactly \(4/5\) and \(1/5\) of five-dimensional volume. The first, deepest-hole count and its \(4/5\) fraction are known from an earlier result; the completion to *all* simplices, the shallower shell, and the complete Voronoi face vector are the claims added here.

More precisely, the 74 facets split into five nearest-site orbits. In the table, “facet vertices” means vertices incident to any one facet of that type.

| Site-vector type | Number of facets | Squared site norm | Facet vertices |
| --- | ---: | ---: | ---: |
| \(\pm2e_5\) | 2 | \(16/15\) | 96 |
| Half-integral vectors with first four coordinates \(\pm1/2\) and fifth coordinate \(\pm1/2\), subject to the parity coset | 16 | \(16/15\) | 120 |
| \(\pm e_i\pm e_5\), \(1\le i\le4\) | 16 | \(19/15\) | 84 |
| Half-integral vectors with first four coordinates \(\pm1/2\) and fifth coordinate \(\pm3/2\), subject to the parity coset | 16 | \(8/5\) | 30 |
| \(\pm e_i\pm e_j\), \(1\le i<j\le4\) | 24 | \(2\) | 16 |

## Assumptions and scope
The point set \(X\), the quadratic form \(q\), and the lattice period \(D_5\) are fixed. Ordinary geometric volumes are measured after the Euclidean change of variables \(x\mapsto(x_1,x_2,x_3,x_4,2x_5/\sqrt{15})\). Coordinate volumes and all ratios stated here are unchanged by the common Jacobian. The quoted squared covering radius \(27/50\), and a containing twelve-halfspace chamber polytope, originate in Ahrend--Dutour Sikirić (2026); the accompanying checker independently verifies the needed finite containment and tightness facts.

The theorem does not assert that this two-periodic packing is globally optimal among all periodic sets. It concerns the exact local Voronoi and Delaunay combinatorics of one specified configuration.

## Proof
**1. A finite complete set of potential Voronoi neighbors.** Write \(\langle x,y\rangle_q=\sum_{i=1}^4x_i y_i+(4/15)x_5y_5\). The bisector condition for a competing site \(s\in X\setminus\{0\}\) is
\[
2\langle x,s\rangle_q\le q(s).
\]
The covering-radius value \(\max_{x\in V}q(x)=27/50\) implies that any actual facet site must satisfy \(q(s)\le4(27/50)=54/25\), by Cauchy--Schwarz at a point on its bisector. Independently of invoking that value, Step 2 below verifies a chamber containment within this ball, which supplies the same truncation. Exact coordinate and parity enumeration in the two cosets gives precisely 74 nonzero sites in that metric ball: 18 of norm squared \(16/15\), 16 of \(19/15\), 16 of \(8/5\), and 24 of \(2\). They are exactly the five families displayed above.

**2. Exact fundamental chamber.** The site stabilizer contains all permutations of the first four coordinates and all five-coordinate sign changes of even parity. It has order \(4!2^4=384\), preserves \(X\) and \(q\), and takes any point into the chamber \(\mathcal C=\{x_1\ge x_2\ge x_3\ge x_4\ge0\}\), with fifth coordinate \(z\) unrestricted. Consider the twelve-halfspace polytope \(P\subset\mathcal C\) defined by
\[
\begin{gathered}
-1\le z\le1,\quad
15(x_1+x_2+x_3-x_4)-4z\le16,\\
5(x_1+x_2+x_3+x_4)-4z\le8,\quad
15(x_1+x_2+x_3+x_4)+4z\le16,\\
30x_1-8z\le19,\quad30x_1+8z\le19,\quad x_1+x_2\le1,\\
x_1\ge x_2\ge x_3\ge x_4\ge0.
\end{gathered}
\]
The eight non-chamber inequalities are genuine bisectors of sites of \(X\), so \(V\cap\mathcal C\subseteq P\). All \(\binom{12}{5}=792\) five-constraint systems are examined by exact rational elimination; 455 have nonsingular matrices and exactly 41 distinct feasible vertices result. Checking each of these 41 vertices establishes simultaneously (i) \(q(x)\le27/50\) and (ii) all 74 finite bisector inequalities. By convexity of the quadratic form, (i) holds throughout \(P\); by linearity, (ii) holds throughout \(P\). For any site \(s\) excluded from the 74-site set, \(q(s)>54/25\). At every \(x\in P\), the triangle inequality gives \(\sqrt{q(x-s)}>\sqrt{q(x)}\), hence such a site cannot cut \(P\). Consequently **\(P=V\cap\mathcal C\)**, not merely an outer approximation.

**3. Vertex and facet certificates.** At each of the 41 vertices of \(P\), form the matrix of gradients of *tight genuine site-bisectors*, excluding artificial chamber walls. Exactly six points have gradient rank five; they are
\[
\begin{aligned}
 &(11/30,11/30,1/15,0,-1),\quad(11/30,11/30,1/15,0,1),\\
 &(13/30,13/30,1/15,1/15,-3/4),\\
 &(1/2,13/30,2/15,2/15,-1/2),\\
 &(17/30,13/30,1/15,1/15,-1/4),\\
 &(19/30,11/30,1/15,0,0).
\end{aligned}
\]
These are exactly the genuine \(V\)-vertices in \(\mathcal C\); each has precisely five tight site-bisectors with independent gradients. Applying the 384 chamber symmetries and deduplicating exact rational coordinates gives 864 distinct vertices, all simple. Of these, 576 have squared radius \(27/50\) and 288 have \(481/900\). For each of the 74 candidate site vectors, the corresponding equality hyperplane contains five affinely independent vertices from this complete list, proving that **every candidate defines a genuine facet**. The five type-specific vertex-incidence counts in the table follow by exact incidence enumeration.

At each simple vertex precisely five facets meet. Every face of codimension \(j\) is uniquely the intersection of its \(j\) containing facets, and conversely every subset of \(j\) facets incident at a vertex defines a face of that codimension. Deduplicating these facet-index subsets for \(j=1,2,3,4,5\) gives respectively \(74,648,1872,2160,864\) faces. This proves the full face vector without relying on numerical convex hull routines.

**4. Delaunay dual and the two volume types.** The origin plus the five other nearest sites at any Voronoi vertex is a nondegenerate Delaunay simplex: exact determinants are \(\pm1\) for all 576 outer-shell vertices and \(\pm1/2\) for all 288 inner-shell vertices. Since the site stabilizer is transitive on the two site cosets up to a translation and reflection \(x\mapsto t-x\), every site has the same incidence counts. A lattice period of \(D_5\) contains two sites, while each Delaunay five-simplex has six vertices. Counting incidents modulo \(D_5\) therefore gives
\[
N_{\mathrm{outer}}=\frac{2\cdot576}{6}=192,\qquad
N_{\mathrm{inner}}=\frac{2\cdot288}{6}=96.
\]
A five-simplex whose coordinate edge-determinant has magnitude \(d\) has coordinate volume \(d/5!\). The normalized \(D_5\)-period has coordinate volume \(2\), and the two volumes sum to \(192/120+96/240=2\). Their volume fractions are \(4/5\) and \(1/5\). All Voronoi vertices are simple, so the dual Delaunay decomposition has only these simplices and no nonsimplicial full-dimensional cells.

## Verification
Run `python3 verify_voronoi.py` in the directory containing this result. The complete standard-library checker constructs the two cosets within the rigorous \(54/25\) norm cutoff, solves every one of the 792 candidate chamber bases with exact fractions, verifies the 41 feasible chamber vertices and their radius and bisector bounds, generates the entire 864-vertex group orbit, checks all actual site incidences and face-subset counts, proves affine rank four for each of the 74 facets, and checks all 864 Delaunay determinants. It prints `EXACT_VORONOI_CERTIFICATE_OK` and the exact face-vector, norm-shell, and Delaunay counts. No floating-point approximation is used in the certificate; the finite calculation is a complete enumeration given the analytic cutoff and symmetry argument.

## Relationship to prior work
Ahrend and Dutour Sikirić, arXiv:2609.30513v1, introduce the exact two-periodic configuration, establish its packing and covering radii, and enumerate 41 vertices of a twelve-halfspace *containing chamber polytope*. That 41-vertex list is not a list of actual Voronoi vertices, and their paper does not give the 74-facet Voronoi cell, the complete face vector, the lower radius shell, or a complete Delaunay tessellation census. A subsequent published result, *A single deepest-hole orbit and four-fifths Delaunay volume in a five-dimensional two-periodic set*, establishes the 576 deepest Voronoi vertices incident to each site and the 192 maximal-circumradius simplices occupying \(4/5\) of volume. The theorem above credits those facts and adds the missing shallower 288 vertices, simplicity of **all** vertices, full facet and face structure, and the 96 remaining Delaunay simplices of half determinant. A separate published result identifies the optimum within the one-parameter diagonal family of forms, not this face lattice. General Delone/Voronoi duality yields structural principles but none of these exact combinatorial data without checking this particular configuration.

## Limitations
The classification is only at the particular diagonal metric \(\operatorname{diag}(1,1,1,1,4/15)\). It does not describe how combinatorial types change under metric perturbations. The calculations are exact and fully reproducible. An apparently related companion note cited in the initiating paper, *Non-lattice periodic point sets for the packing-covering problem: ties, structure and search*, was not found in accessible full text, leaving a specific residual historical-priority risk. Unindexed computational classifications may also exist.

## References
1. Sven Ahrend and Mathieu Dutour Sikirić, *A non-lattice periodic point set beating the optimal lattice packing-covering constant in dimension five*, arXiv:2609.30513v1, first public 2026-09-24, https://arxiv.org/abs/2609.30513.
2. *A single deepest-hole orbit and four-fifths Delaunay volume in a five-dimensional two-periodic set*, published record 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-single-deepest-hole-orbit-and-four-fifths-delaunay-volume-in-a--7bcf4c028169/RESULT.md.
3. *Exact optimizer on the \(D_5^+\) diagonal packing-covering ray*, published record 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-optimizer-on-the-d-5-diagonal-packing-covering-ray--cad41b90f045/RESULT.md.
4. Achill Schürmann and Frank Vallentin, *Computational approaches to lattice packing and covering problems*, Discrete & Computational Geometry 35 (2006), 73–116, https://arxiv.org/abs/math/0403272.
