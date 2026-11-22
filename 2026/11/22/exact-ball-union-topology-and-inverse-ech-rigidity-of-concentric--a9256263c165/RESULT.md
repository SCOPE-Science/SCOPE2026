# Exact ball-union topology and inverse Čech rigidity of concentric bicentric tetrahedra

## Finding
Let \(\Delta\subset\mathbb R^3\) be a nondegenerate tetrahedron with circumradius \(1\) and coincident circumcenter and incenter at the origin. Write \(h\in(0,1/3]\) for its inradius and \(n_0,\ldots,n_3\) for its outward unit facet normals. Define the four **outer-ball centers**
\[
 c_i=\frac{n_i}{\sqrt{1-h^2}},\qquad \rho=\frac{h}{\sqrt{1-h^2}},
\]
which are the four unit-ball centers in the construction of Nour [1]. Put \(U_s=\bigcup_{i=0}^3\overline B(c_i,s)\), for \(s\ge0\), and \(W_q=U_1\cup\overline B(0,q)\), for \(q\ge0\).

There are three explicitly determined, possibly equal, numbers \(0<d_1\le d_2\le d_3<1\), the half-lengths of the three opposite-edge pairs of the center tetrahedron, such that the **complete nonzero Čech persistence barcode** of the offsets \(U_s\), over every coefficient field, is
\[
\begin{array}{c|l}
 H_0 & [0,\infty),\quad 2[0,d_1),\quad [0,d_2)\\
 H_1 & [d_2,1),\quad 2[d_3,1)\\
 H_2 & [1,L)
\end{array},\qquad
 L=\sqrt{\frac{d_1^2+d_2^2+d_3^2}{2}}=\frac1{\sqrt{1-h^2}}.
\]
Here \(k[I]\) means \(k\) copies of interval \(I\), and all higher-degree bars are absent. This convention includes equality cases; intervals of length zero are omitted. At \(s=1\), the four outer unit balls have the homotopy type of \(S^2\), with precisely one bounded complement component.

**Sharp spherical-core transition:**
\[
\widetilde H_2(W_q;\mathbb Z)\ne0\quad(0\le q<\rho),
\qquad W_q\simeq\{\mathrm{point}\}\quad(q\ge\rho),
\]
so the origin-centered ball used in [1] has exactly the smallest radius that eliminates the outer four balls' two-dimensional void. Furthermore, the barcode recovers the full congruence class of \(\Delta\). In fact, putting \(S=d_1^2+d_2^2+d_3^2\), the quantities
\[
 A_i^2=\frac{S}{2}-d_i^2>0,\qquad
 h^2=1-\frac2S,\qquad
 a_i^2=\frac{S/2-1}{A_i^2}
\]
recover, up to permutation, the three positive box half-axes \(a_i\) of \(\Delta\), whose four vertices are alternating corners \((\pm a_1,\pm a_2,\pm a_3)\) of a rectangular box. In particular the critical core radius is itself determined from the three earlier edge-intersection scales:
\[
\boxed{\rho=\sqrt{\frac{d_1^2+d_2^2+d_3^2}{2}-1}.}
\]

## Assumptions and scope
All balls are closed Euclidean balls, with radius \(s\) for the offset filtration and fixed radius \(1\) for the four outer balls in \(W_q\). The tetrahedron is required to have coincident **interior** incenter and circumcenter and to be nondegenerate. The statement is specific to three-dimensional Euclidean ball arrangements of the displayed type and makes no claim for arbitrary four-site clouds, arbitrary five-ball unions, or simplices in other dimensions. The barcode is with the closed-ball convention, so a class dying at \(r\) is absent at \(r\).

## Proof
**1. Orthogonal-box form.** A tetrahedron with coincident incenter and circumcenter is equifacial (a disphenoid) [3]. Thus, up to an orthogonal transformation and relabeling, its vertices are the four alternating sign corners
\[
 u_0=(a,b,c),\quad u_1=(a,-b,-c),\quad u_2=(-a,b,-c),\quad u_3=(-a,-b,c),
\]
with \(a,b,c>0\) and \(a^2+b^2+c^2=1\). The plane of the face opposite \(u_i\) has outward normal proportional to the coordinatewise negative reciprocal of \(u_i\)'s signs. Consequently
\[
 h^{-2}=a^{-2}+b^{-2}+c^{-2},\qquad
 c_i=-\frac{h}{\sqrt{1-h^2}}
 \left(\frac{(u_i)_1}{a^2},\frac{(u_i)_2}{b^2},\frac{(u_i)_3}{c^2}\right).
\]
The centers \(c_i\) are therefore the alternating corners of a second centered rectangular box, of positive half-axes
\[
 A=\frac{h}{a\sqrt{1-h^2}},\quad
 B=\frac{h}{b\sqrt{1-h^2}},\quad
 C=\frac{h}{c\sqrt{1-h^2}}.
\]
In particular, \(\sum_i c_i=0\) and each \(\|c_i\|^2=A^2+B^2+C^2=L^2=1/(1-h^2)=1+\rho^2>1\).

**2. Exact simplex birth radii.** The six center-pair distances appear in three opposite equal pairs. Their half-lengths are \(\sqrt{A^2+B^2}\), \(\sqrt{A^2+C^2}\), \(\sqrt{B^2+C^2}\), in sorted order \(d_1,d_2,d_3\). Equivalently, their squares, as an unordered multiset, are
\[
 \left\{\frac{1-h^2/a^2}{1-h^2},\frac{1-h^2/b^2}{1-h^2},\frac{1-h^2/c^2}{1-h^2}\right\}.
\]
Every one lies strictly between zero and one because \(h^2<\min\{a^2,b^2,c^2\}\) and \(a^2,b^2,c^2<1\). Hence all six edges of the four-site Čech complex have appeared strictly before \(s=1\).

Let \(p_i=\rho u_i\). The identities \(\|p_i-c_j\|=1\) and \(\langle p_i,c_j-p_i\rangle=0\), for \(j\ne i\), are direct substitutions, and are also precisely the contact identities in [1, Lemma 2.2]. Thus \(p_i\) is the planar circumcenter of the triangle formed by the three centers \(c_j\), \(j\ne i\), with circumradius \(1\). Every such triangle is acute: its three squared side lengths are \(4d_1^2,4d_2^2,4d_3^2\), and \(d_j^2+d_k^2-d_i^2=2A_i^2>0\) after matching each coordinate axis with its opposite-edge pair. Hence \(p_i\) is strictly inside its face triangle. Writing it as a strictly positive barycentric combination \(p_i=\sum_{j\ne i}\lambda_jc_j\), for arbitrary \(x\) one obtains
\[
 \sum_{j\ne i}\lambda_j\|x-c_j\|^2
 =\|x-p_i\|^2+\sum_{j\ne i}\lambda_j\|p_i-c_j\|^2
 =\|x-p_i\|^2+1.
\]
Therefore the intersection of those **three unit balls is exactly the singleton** \(\{p_i\}\). Since the triangle is acute, the three balls have no common intersection for smaller equal radius, and do intersect for every radius at least \(1\).

For all four centers, their centroid is zero and their squared norm equals \(L^2\), so
\[
 \frac14\sum_{j=0}^3\|x-c_j\|^2=\|x\|^2+L^2.
\]
Four radius-\(s\) balls therefore have empty common intersection if \(s<L\), and intersect at \(x=0\) if \(s\ge L\). These determine all sixteen simplex-entry thresholds of the four-vertex Čech nerve: four vertices at zero, opposite edge pairs at \(d_1,d_2,d_3\), all four triangles at \(1\), and the tetrahedron at \(L\).

**3. Topology and barcode.** At these successive scales the Čech nerve is, omitting empty stages caused by tied thresholds, four isolated vertices, two disjoint edges, a four-cycle, the complete graph \(K_4\), the boundary of a tetrahedron, and the full tetrahedron. These have Betti vectors (degrees \(0,1,2\)) respectively \((4,0,0),(2,0,0),(1,1,0),(1,3,0),(1,0,1),(1,0,0)\). The inclusions are the displayed canonical graph/face additions, so the stated interval pairings follow; equivalently, the first edge pair merges two components, the second connects the remaining two components while creating one loop, and the third creates two more loops. At radius \(1\), four triangular faces kill all loops and create one \(2\)-sphere; at \(L\), the tetrahedron kills that sphere. The nerve theorem for convex ball covers identifies the topology and inclusion-induced persistence of the nerves with the offsets \(U_s\), over any field. These complexes also have torsion-free integral homology.

**4. Minimal central core.** At radius \(1\), the outer four-ball nerve is the tetrahedron boundary. For \(q<\rho\), the central ball \(\overline B(0,q)\) misses each of the four singleton triple intersections \(\{p_i\}\). No simplex of dimension three can therefore be added to the five-ball nerve; in particular its original tetrahedral-boundary integral \(2\)-cycle stays nonbounding. Thus \(\widetilde H_2(W_q;\mathbb Z)\ne0\). When \(q\ge\rho\), each proper subset of the four outer balls has an intersection containing some \(p_i\in\overline B(0,q)\), because a proper subset omits at least one index \(i\). The full outer-ball intersection remains empty. The five-ball nerve is now exactly the cone, with apex the central ball, over the tetrahedron-boundary nerve. It is contractible by the nerve theorem. This proves the sharp threshold and its equality case.

**5. Reconstruction.** The edge thresholds satisfy \(d_1^2+d_2^2+d_3^2=2(A^2+B^2+C^2)=2L^2\). Each second-box axis square equals \(L^2-d_i^2\) for the complementary edge pair. Since \(L^2=1/(1-h^2)\), the first-box axis squares are \((L^2-1)/(L^2-d_i^2)\), as claimed. They are positive and sum to one by the concentric-bicentric relation. Thus the barcode determines the original disphenoid up to congruence. Degenerate coincidences of the three thresholds create no ambiguity in these unordered formulas.

## Verification
The accompanying standard-library script `verify.py` independently constructs the facet normals and four outer centers from eight specified plus 200 seeded nonsymmetric positive-box triples. It checks all center-to-contact-point squared distances, acute-face inequalities, metric threshold identities, and binary homology ranks computed from explicit boundary matrices of the four-vertex Čech complexes. All 208 tested configurations passed. These finite checks are supplementary; steps 1–5 constitute the all-parameter proof.

## Relationship to prior work
Nour [1] supplies the five-ball construction, its center-to-sphere contact identities, and the sharp radius of a **ball contained in the union and covering the origin**. That radius is not the central-ball **topological filling threshold** established here. The original work does not state the exact triple-intersection singleton lemma, the all-scale Čech barcode, or recovery of the tetrahedron from that barcode. Standard nerve/alpha-complex theory [2] transports ball-intersection incidence into homology, but supplies neither these specific critical radii nor the reconstruction. Classical disphenoid descriptions [3] provide the geometric coordinate normal form. Previously published sharp volume bounds for concentric bicentric tetrahedra concern a different invariant [4]. The novelty claim is only this particular combined topological/metric classification, not the cited geometric or topological tools.

## Limitations
The result does not classify general four-center Čech filtrations, arbitrary finite unions of balls, or dimensions greater than three. The central-ball threshold concerns balls **centered at the original origin**, not all possible centers. The interval theorem holds over arbitrary coefficient fields; only the torsion-freeness, not a general integral interval-decomposition theorem, is asserted. The complete historical priority of the specific special-case filtration has not been independently certified.

## References
[1] Chadi Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher*, arXiv:2611.14181v1, first public 2026-11-10. https://arxiv.org/abs/2611.14181

[2] Herbert Edelsbrunner and János Pach, *Maximum Betti Numbers of Čech Complexes*, 40th Symposium on Computational Geometry, SoCG 2024, DOI:10.4230/LIPIcs.SoCG.2024.53. https://doi.org/10.4230/LIPIcs.SoCG.2024.53

[3] Classical characterization and rectangular-box normal form of the disphenoid (equifacial tetrahedron); see the survey entry *Disphenoid*. https://en.wikipedia.org/wiki/Disphenoid

[4] *Sharp volume interval for concentric bicentric tetrahedra*, published mathematical research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-volume-interval-for-concentric-bicentric-tetrahedra--3c21c1faa6d8
