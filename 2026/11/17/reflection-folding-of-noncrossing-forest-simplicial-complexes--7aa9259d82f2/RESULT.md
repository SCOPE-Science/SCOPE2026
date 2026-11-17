# Reflection folding of noncrossing-forest simplicial complexes

## Finding
For each integer \(m\ge2\), put \(n=2m\), label the vertices of a strictly convex \(n\)-gon cyclically by \(0,1,\ldots,n-1\), and let \(\mathcal N_n\) be the simplicial complex whose vertices are unordered polygon-vertex pairs and whose faces form acyclic straight-line graphs without proper chord crossings. Polygon sides are permitted. The reflection \(\sigma(i)=1-i\pmod n\) has its axis through the midpoints of the sides \(\{0,1\}\) and \(\{m,m+1\}\). Then

\[
|\mathcal N_{2m}|^{\langle\sigma\rangle}\cong_{\mathrm{PL}}|\mathcal N_{m+1}|.
\]

The map comes from a **simplicial isomorphism** between the complex on admissible reflection edge orbits and \(\mathcal N_{m+1}\). In particular, putting \(k=m+1-t\), the number of faces with \(t\) orbit-barycenter vertices is

\[
F_{m,t}=\frac{1}{2(m+1)-k}\binom{m+1}{k-1}\binom{3(m+1)-2k-1}{m+1-k},\qquad 0\le t\le m.
\]

The fixed space has a triangulation of dimension \(m-1\), and this formula gives its complete face vector in that triangulation. The count is an application of the existing ordinary noncrossing-forest enumeration, not a new enumeration theorem in its own right.

## Assumptions and scope
An edge is an unordered pair of distinct polygon vertices. Edges incident at a common endpoint do **not** properly cross. A graph is a forest if it contains no simple cycle; isolated vertices are allowed. Each face of \(\mathcal N_n\) is a set of edges and determines a simplex in the usual geometric realization. The group acts by permuting edge coordinates. A fixed point is a point of the realization, not merely a face fixed setwise. The homeomorphism is of piecewise-linear spaces, with the standard orbit-barycenter triangulation on the fixed side. The assertion requires the **edge-midpoint-axis** reflection of an even polygon.

## Proof
**1. Exact orbit list.** Let \(V=\{0,1,\ldots,m\}\). For \(2\le j\le m\), set \(u_j=m+2-j\) and \(\ell_j=m+j-1\). Hence the upper half has vertex labels \(1,u_m,u_{m-1},\ldots,u_2\), in increasing circular order, and the lower half has \(0,\ell_m,\ell_{m-1},\ldots,\ell_2\), in decreasing circular order. The reflection exchanges \(u_j\) with \(\ell_j\) and \(0\) with \(1\). Define the lift of every edge in the smaller polygon by

\[
\begin{array}{c|c}
\text{small edge}&\text{reflection orbit of large edges}\\
\{0,1\}&\{\{0,1\}\}\\
\{1,j\}\ (j\ge2)&\{\{u_j,\ell_j\}\}\\
\{0,j\}\ (j\ge2)&\{\{0,\ell_j\},\{1,u_j\}\}\\
\{i,j\}\ (2\le i<j)&\{\{u_i,u_j\},\{\ell_i,\ell_j\}\}.
\end{array}
\]

These \(\binom{m+1}{2}\) orbits are individually noncrossing and acyclic. Every other orbit consists of two chords whose endpoints alternate around the original polygon, so its two chords properly cross; hence it cannot occur in a fixed face. This classification follows by distinguishing edges lying inside one semicircle, axis-perpendicular edges joining a reflected pair, edges incident with \(0\) or \(1\), and remaining edges crossing the axis.

**2. Proper crossings.** For two distinct edges of the smaller polygon, their lifted edge-orbits have a proper crossing if and only if the smaller edges cross. This is a direct alternating-endpoints test, using the circular orders described above. To make the boundary cases explicit, call the four edge types in the preceding table \(A,B_j,C_j,D_{ij}\). Type \(A\) crosses none. The nontrivial cross-type conditions are: \(B_i\) and \(C_j\) cross exactly when \(j<i\); either \(B_s\) or \(C_s\) crosses \(D_{ij}\) exactly when \(i<s<j\); and two \(D\)-edges cross exactly when their four endpoints alternate. Two edges of the same \(B\) type-family, two of the same \(C\) family, or a \(B_i\) with another \(B_j\) never properly cross; the remaining same-type cases are precisely the smaller polygon criterion. These tests also cover shared endpoints: their lifts do not introduce a new proper crossing. No metric feature of a regular polygon is used beyond convexity and the reflection pairing.

**3. Forests.** For an arbitrary edge subset \(E\subseteq\binom V2\), let \(G=(V,E)\) and let \(G_0=G-\{1\}\) be the graph obtained by deleting vertex \(1\). The lifted graph is two disjoint copies of \(G_0\), one in each semicircle, together with one connecting rung joining the two copies of vertex \(v\in V\setminus\{1\}\) for each edge \(\{1,v\}\in E\). This includes the side \(\{0,1\}\) as the rung at \(v=0\). Consequently, the lift is acyclic exactly when \(G_0\) is acyclic and no component of \(G_0\) contains two distinct vertices incident with \(1\) in \(G\): two such rungs would close a cycle along their two copies of the same path. The same two conditions characterize acyclicity of \(G\), so acyclicity is preserved and reflected for *every* edge subset.

**4. Simplicial and PL identifications.** Steps 1–3 prove that the explicit bijection from smaller edges to permissible reflected edge orbits preserves and reflects both face conditions: absence of proper crossings and acyclicity. It is thus an isomorphism of abstract simplicial complexes. In barycentric coordinates of \(|\mathcal N_{2m}|\), a point is reflection-fixed precisely when its coefficients are constant on each reflection orbit of edges. The support of such a point is a union of admissible orbits; assigning its orbit masses to corresponding orbit-barycenter vertices is a simplexwise-affine homeomorphism with the inverse spreading each orbit mass equally over its original members. This is a PL homeomorphism and proves the assertion.

**5. Face numbers.** A forest with \(t\) edges on \(m+1\) vertices has \(k=m+1-t\) components. Applying the established closed count of ordinary noncrossing forests with \(k\) components gives the stated formula. This step uses no extrapolation or finite verification.

## Verification
The standalone `verify_folding.py` checks the orbit classification and all pairwise proper-crossing conditions for \(2\le m\le12\) (9,009 unordered pairs), exhaustively tests the forest-lift equivalence for all edge subsets at \(2\le m\le6\) (including 2,097,152 subsets at \(m=6\)), and enumerates all ordinary face vectors for \(3\le m+1\le8\), checking the closed counting formula and face-by-face lift admissibility. Run `python3 verify_folding.py` using only the Python standard library. The logged output in `verification_output.txt` is reproducible. Finite checks corroborate the universal arguments in Steps 1–4, but cannot prove them for unbounded \(m\).

## Relationship to prior work
Jonsson's *Simplicial Complexes of Graphs* treats noncrossing forests as an established simplicial graph complex and their ordinary topology (Chapter 16, Section 16.4). Kluge's 2011 preprint, subsequently published in 2012, proves cyclic sieving for rotation-invariant noncrossing forests and reproduces the ordinary exact component-count formula, which is used here. Neither of those **inspected portions** establishes the reflection-axis orbit-barycenter simplicial isomorphism or the geometric fixed-point PL result. Rotation-fixed *forests as a finite set* is not the same as the geometric reflection-fixed space of the *whole simplicial complex*. A full comparison with Jonsson's entire Section 16.4 could not be completed; this is an explicit priority limitation, not a claim that the uninspected text lacks related results.

## Limitations
The theorem is restricted to even polygons and their side-midpoint-axis involution, not odd polygons, the other even-polygon reflection class, all dihedral subgroups, or quotient spaces. The count applies to the specific orbit-barycenter triangulation, not arbitrary triangulations. A historical source on the same underlying complex was available only through its bibliographic and chapter descriptions; an equivalent older equivariant formulation cannot be ruled out by a failed search. Independent mathematical review remains unperformed.

## References
1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, Chapter 16, Section 16.4, pp. 226–229; DOI 10.1007/978-3-540-75859-4_16. Physical edition first published November 15, 2007; a doctoral thesis precursor is dated May 2005 (precise public day not established). Publisher content summary: https://link.springer.com/book/10.1007/978-3-540-75859-4 .
2. S. Kluge, *The Cyclic Sieving Phenomenon for Non-Crossing Forests*, arXiv:1106.0992 (public June 6, 2011); *Electronic Journal of Combinatorics* 19(3) (2012), #P1, DOI 10.37236/2419. Open-access full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p1/pdf/ .
