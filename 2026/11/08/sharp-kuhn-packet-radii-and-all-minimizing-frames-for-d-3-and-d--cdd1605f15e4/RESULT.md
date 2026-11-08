# Sharp Kuhn-packet radii and all minimizing frames for \(D_3\) and \(D_3^*\)

## Finding
For the Euclidean unit ball \(B_2^3\), the face-centered-cubic (FCC) root lattice and its body-centered-cubic (BCC) dual satisfy
\[
\kappa(B_2^3,D_3)=\mu(B_2^3,D_3)=1,\qquad
\kappa(B_2^3,D_3^*)=\mu(B_2^3,D_3^*)=\frac{\sqrt5}{4}.
\]
Here \(\mu\) is the classical Euclidean lattice covering radius and \(\kappa\) is the original common-independent-frame Kuhn-packet radius. The entire optimizer set is finite and rigid: there are exactly **24 unordered FCC frames** and **8 unordered BCC frames**. In the FCC case the optimal triples consist of three root vectors having squared norms \(2\) and pairwise inner products \(\{-1,-1,0\}\). In the BCC case each vector has coordinates \((\pm\tfrac12,\pm\tfrac12,\pm\tfrac12)\), with every pairwise inner product \(-\tfrac14\). Every optimal frame is a basis of its respective lattice. As an ordered triple, each of the 24 or 8 unordered frames has six permutations, all defining the same packet.

## Assumptions and scope
Work in the standard Euclidean \(\mathbb R^3\) and write
\[
D_3=\{(z_1,z_2,z_3)\in\mathbb Z^3:z_1+z_2+z_3\equiv0\pmod2\},\quad
D_3^*=\mathbb Z^3\cup\bigl(\mathbb Z^3+(\tfrac12,\tfrac12,\tfrac12)\bigr).
\]
A *frame* is any linearly independent triple \(\mathbf b=(b_1,b_2,b_3)\) of lattice vectors; it is **not** assumed to generate the entire lattice. For every permutation \(\sigma\) of \(\{1,2,3\}\), form the permutation tetrahedron
\[
\Delta_\sigma(\mathbf b)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_1+b_2+b_3\}.
\]
Let \(r_2(S)=\min_c\max_{x\in S}\|x-c\|_2\), and define
\[
\kappa(B_2^3,\Lambda)=\inf_{\mathbf b\in\Lambda^3\;\mathrm{independent}}\;\max_\sigma r_2(\Delta_\sigma(\mathbf b)).
\]
The permutation maximum makes the order of a frame immaterial. In contrast, the BCC calculations below temporarily use the doubled lattice \(L=2D_3^*=2\mathbb Z^3\cup((1,1,1)+2\mathbb Z^3)\); lengths in \(L\) are exactly twice the lengths in \(D_3^*\).

## Proof
**1. A necessary subset-sum inequality.** If all permutation tetrahedra of a frame fit into Euclidean balls of radius \(R\), every nonempty subset \(I\subseteq\{1,2,3\}\) obeys
\[
\left\|\sum_{i\in I}b_i\right\|_2\le2R.\tag{1}
\]
Indeed, choose an ordering beginning with the indices in \(I\): both \(0\) and the indicated partial sum are vertices of its tetrahedron, so their distance cannot exceed the ball diameter. This applies to independent frames of *any* lattice index.

**2. FCC necessary classification.** Take \(R=1\). The nonzero vectors of \(D_3\) with squared norm at most \(4\) consist exactly of twelve roots \((\pm1,\pm1,0)\) and their coordinate permutations, of squared norm \(2\), and six coordinate-axis vectors \(\pm2e_j\), of squared norm \(4\). Suppose a candidate frame contains \(a=2e_1\) (coordinate signs and order cause no loss). Every other independent candidate vector must be a root with first coordinate \(-1\), since \(\|a+b\|_2^2\le4\). The two other roots then have sum with first coordinate \(-2\), and \(\|b+c\|_2^2\le4\) forces \(b+c=-a\), a linear dependence. Hence every candidate vector is a root.

For distinct independent roots, (1) forces every off-diagonal Gram entry to be \(-1\) or \(0\), and the squared norm of the triple sum forces at least one \(-1\). If exactly one off-diagonal entry is \(-1\), the Gram determinant is \(6\), impossible because it equals the square of the integer determinant of the frame matrix. If all three are \(-1\), the Gram determinant is \(0\), contradicting independence. Thus exactly two entries are \(-1\) and one is \(0\). The Gram determinant is \(4\), so these frames have determinant magnitude \(2\), the covolume of \(D_3\).

There are exactly \(12\) unordered orthogonal pairs among the twelve roots (each root has precisely two orthogonal root partners). For each orthogonal pair, precisely two roots have inner product \(-1\) with both members. The unique orthogonal pair in every eligible triple therefore gives \(12\cdot2=24\) unordered frames.

**3. FCC sufficiency and packet radii.** Write the frame as \(u,v,w\), where \(u\cdot v=0\) and \(u\cdot w=v\cdot w=-1\). Its member norms are all \(\sqrt2\). For the four permutations in which \(u,v\) appear consecutively, the tetrahedron contains a pair of vertices separated by \(u+v\), of norm \(2\); the midpoint of this diameter is at squared distance \(1\) from all four vertices. Thus each such tetrahedron has minimum enclosing radius \(1\). For the other two permutations, all six edges have squared length \(2\): the tetrahedra are regular, with squared minimum enclosing radius \(3/4\). The packet maximum is exactly \(1\). In particular \((u,v,w)=((1,1,0),(1,-1,0),(-1,0,1))\) attains it. Step 2 proves that **no other independent frame** can have packet radius at most \(1\), and hence establishes the exact minimum and all equality frames.

**4. BCC necessary classification.** Scale by two, working in \(L=2D_3^*\). The candidate radius is now \(R=\sqrt5/2\), so (1) requires the squared norm of every nonempty subset sum to be at most \(5\). The nonzero elements of \(L\) satisfying this bound are exactly eight odd-parity cube vertices \((\pm1,\pm1,\pm1)\) of squared norm \(3\) and six even coordinate-axis vectors \(\pm2e_j\) of squared norm \(4\).

If a frame contains \(a=2e_1\), the remaining two independent candidates must be odd cube vertices with first coordinate \(-1\). Requiring their pair sum to have squared norm at most \(5\) forces their other coordinate sums to be \(0\); hence \(b+c=-a\), a contradiction. Thus all candidate vectors are odd cube vertices. Distinct independent such vertices have pairwise inner product \(-1\) or \(1\), while (1) for a two-element sum forces \(-1\). They therefore form a triple from one of the two complementary regular tetrahedra among the eight cube vertices. There are \(2\binom43=8\) unordered frames. Their Gram matrix has diagonal entries \(3\) and off-diagonal entries \(-1\), so its determinant is \(16\). Each has lattice determinant magnitude \(4\), the covolume of \(L\).

**5. BCC sufficiency and packet radii.** For any ordered such triple \((u,v,w)\), consider the four vertices \(p_0=0,p_1=u,p_2=u+v,p_3=u+v+w\). Their centroid is
\[
c=\frac14(p_0+p_1+p_2+p_3)=\frac{3u+2v+w}{4}.
\]
The Gram equations give \(\|p_j-c\|_2^2=5/4\) for each \(j=0,1,2,3\). Because the center is a positive convex combination of the four contact vertices, the enclosing ball of squared radius \(5/4\) is minimal: for any alternative center, the average of its four squared distances increases by the square of its displacement from \(c\). Thus **every** permutation tetrahedron has minimum enclosing radius \(\sqrt5/2\) in doubled coordinates, giving \(\kappa(B_2^3,D_3^*)=\sqrt5/4\) after undoing the factor of two. The triple \((u,v,w)=((1,1,1),(1,-1,-1),(-1,1,-1))\) in doubled coordinates is an explicit optimizer. Step 4 makes the classification exhaustive.

**6. Equality with the ordinary lattice covering radius.** The general packet-to-covering inequality \(\mu(B_2^3,\Lambda)\le\kappa(B_2^3,\Lambda)\) is proved in Xue's Proposition 2.4 [1]. For FCC, the point \((1,0,0)\) has distance exactly \(1\) to \(D_3\). For BCC, the point \((\tfrac12,\tfrac14,0)\) has distance exactly \(\sqrt5/4\) to \(D_3^*\), by separately minimizing distance to \(\mathbb Z^3\) and to \(\mathbb Z^3+(\tfrac12,\tfrac12,\tfrac12)\). These witnesses provide the opposite covering-radius inequalities. Combining them with the packet upper bounds proves both stated equalities.

## Verification
Running `python3 verify_packet.py` with Python 3 and the standard library exhausts the finite candidate lists forced by (1), using integer dot products and determinants. Exact rational arithmetic checks every permitted permutation simplex and its proposed center, without floating-point comparisons. The program reports \(24\) FCC and \(8\) BCC unordered frames; \(96\) FCC packet tetrahedra have squared minimal radius \(1\), \(48\) have \(3/4\), and all \(48\) BCC tetrahedra have squared radius \(5/4\) in doubled coordinates. The analytical classification above proves the unrestricted statement; the program is supplementary reproducibility, not a substitute for the infinite-frame argument.

## Relationship to prior work
Xue [1] introduces the original common-frame packet invariant, proves its comparison with classical lattice covering, and establishes exact values on \(\mathbb Z^d\) for standard balls. It also shows that an *extended* triangulation-based invariant equals the covering radius on every ellipsoid, but the extended equality does not imply equality for the more restrictive **original common-frame** invariant. The present result gives two non-orthogonal, mutually dual three-dimensional lattices where equality nevertheless holds and completely classifies their optimizing frames. The geometry of FCC/BCC Voronoi and Delaunay cells was studied in [2]; cell classification alone does not quantify the infimum over all common lattice frames or list all frames attaining that infimum. No priority claim is made for the classical covering radii or Delaunay geometry.

## Limitations
Only the two specifically normalized three-dimensional lattices and the Euclidean ball are classified. The equality of original packet and classical covering radii does not hold for every lattice or in every dimension. The existence of equivalent older optimizer classifications under different terminology cannot be fully excluded, particularly because [2] could be assessed only from its accessible abstract and metadata. Independent mathematical validation is not claimed.

## References
[1] Fei Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1, first publicly submitted 28 October 2026, especially Definition (1.1), Propositions 2.4 and 6.1 and Section 5. https://arxiv.org/abs/2610.39034

[2] Mehmet Koca, Nazife Özdeş Koca, Abeer Al-Siyabi, and Ramazan Koc, *Explicit Construction of the Voronoi and Delaunay Cells of \(W(A_n)\) and \(W(D_n)\) Lattices and Their Facets*, arXiv:1804.05836, 16 April 2018; Acta Crystallographica A 74 (2018), 499–511. https://arxiv.org/abs/1804.05836
