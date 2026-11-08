# Integral dihedral homology of the eleven-point biplane Vietoris–Rips complex

## Finding
Let \(Q=\{1,3,4,5,9\}\subset\mathbb Z/11\mathbb Z\), let \(B_i=i+Q\), and let \(G\) be the bipartite incidence graph on eleven points \(p\) and eleven blocks \(B_i\), with \(p\sim B_i\) if and only if \(p-i\in Q\). Give \(G\) the shortest-path metric and put \(K_r=\operatorname{VR}_{\le r}(G)\).

The integral homotopy types of the filtration are
\[
K_r\simeq\begin{cases}
\text{22 discrete points},&0\le r<1,\\
\bigvee^{34}S^1,&1\le r<2,\\
\bigvee^{21}S^3,&2\le r<3,\\
\text{point},&r\ge3.
\end{cases}
\]
The reduced integral barcode consists of 21 intervals \([0,1)\) in degree zero, 34 intervals \([1,2)\) in degree one, and 21 intervals \([2,3)\) in degree three. There are no other bars.

More importantly, the 22-element dihedral group \(D_{22}=\langle s,d\mid s^{11}=d^2=1,\ dsd=s^{-1}\rangle\) acts on the scale-two complex by \(s(p)=p+1\), \(s(B_i)=B_{i+1}\), \(d(p)=B_{-p}\), and \(d(B_i)=-i\). The character of its action on \(H_3(K_2;\mathbb Q)\) is
\[
\chi(1)=21,\qquad \chi(s^a)=-1\ \ (1\le a\le10),\qquad \chi(s^a d)=1\ \ (0\le a\le10).
\]
Let \(W\) be the unique ten-dimensional irreducible rational representation of \(D_{22}\) on which nonidentity rotations have trace \(-1\) and reflections have trace zero. Then
\[
H_3(K_2;\mathbb Q)\cong \mathbf1\oplus W^{\oplus2}.
\]
In particular the incidence duality \(d\) has \(+1\)- and \(-1\)-eigenspace dimensions 11 and 10, respectively. This part-swapping symmetry representation is not determined by a point-only block-complex homotopy or character calculation.

## Assumptions and scope
The explicit symmetric \(2\)-\((11,5,2)\) design is defined by the eleven cyclic translates of \(Q\). Its eleven blocks have five points each, each point belongs to five blocks, any two points belong to exactly two blocks, and any two distinct blocks intersect in exactly two points. These are verified exactly by the accompanying certificate; the design is the classical eleven-point biplane. Graph vertices are distinguished point and block copies of residue classes, and all incidence edges have length one. The Rips convention includes pairs at exactly the specified radius. The graph has diameter three. The new symmetry statement is for the indicated subgroup \(D_{22}\) of graph automorphisms, not a claim about every irreducible constituent of the full automorphism group.

## Proof
**Metric and simplices.** Distinct vertices on the same side are at distance two, because any two points occur in two blocks and any two blocks meet in two points. Opposite-side vertices have distance one if incident and three otherwise. Therefore \(K_1\) is exactly \(G\) and \(K_3\) is a simplex. Since \(G\) has 22 vertices and 55 edges, its graph-cycle rank is \(55-22+1=34\). Hence \(K_1\simeq\bigvee^{34}S^1\).

At radius two, a pure point set and a pure block set are always simplices. Every mixed clique with only one block is contained in its point-neighborhood cone, and dually for one point; if there are at least two points and two blocks, the \(\lambda=2\) property forces precisely two of each. Thus \(K_2\) has exactly 79 maximal simplices: the two pure ten-simplices, the 22 five-dimensional point/block neighborhood simplices, and the 55 tetrahedra \(T_{pr}=\{p,r,B_i,B_j\}\), where \(i,j\) are the two blocks through the point pair \(\{p,r\}\).

**Contractible core and attaching chains.** Let \(A\) be the union of the pure point simplex and every block-neighborhood cone \(\{B_i\}*\Delta(B_i)\). Every block vertex is an apex of its unique cone in \(A\), so \(A\) simplicially collapses onto the pure point simplex. Let \(B\) be the analogous union of the pure block simplex and the point-neighborhood cones; it collapses onto the pure block simplex. Their intersection is literally the original incidence graph \(G\). As both pieces are contractible and their inclusions are cofibrations, their union \(U=A\cup B\simeq\Sigma G\simeq\bigvee^{34}S^2\). Exactly the 55 tetrahedra \(T_{pr}\) remain to be attached, all along complete boundary two-spheres lying in \(U\).

The canonical Mayer–Vietoris isomorphism \(H_2(U;\mathbb Z)\cong H_1(G;\mathbb Z)\) sends the attaching class of \(T_{pr}\) to the oriented incidence four-cycle \(p-B_i-r-B_j-p\), with edge coefficients \((1,-1,1,-1)\). Form the 34-by-55 integral matrix \(M\) with one row per non-tree incidence edge of a rooted breadth-first spanning tree of \(G\), and one column per four-cycle, ordered by point pairs \(p<r\). Each tree chord is a coordinate for the integral cycle lattice. In the reproducible vertex/edge order described by `verify_biplane_dihedral.py`, the 34 columns of zero-based indices

`27,38,4,40,39,41,22,28,32,7,51,24,15,43,46,18,45,33,3,14,8,29,11,35,10,13,47,44,19,25,49,53,6,26`

form a 34-by-34 submatrix of determinant exactly \(-1\), computed with integer fraction-free elimination. They therefore give a unimodular basis of \(H_2(U;\mathbb Z)\) and, by the Hurewicz theorem, of \(\pi_2(U)\). Attach the corresponding 34 tetrahedral three-cells first. The resulting simply connected CW complex has trivial reduced integral homology: its cellular three-to-two boundary is an isomorphism, while it has no other positive-degree cellular homology. It is consequently contractible by the homological Whitehead theorem. Each of the remaining 21 three-cells then attaches to this contractible subcomplex by a null-homotopic map. Hence \(K_2\simeq\bigvee^{21}S^3\) integrally. This proves the full filtration and the integral barcode without extrapolating from finite-field calculations.

**Dihedral action and exact character.** Let \(s\) shift both sides by one and let \(d\) exchange the sides via negation. Direct substitution in \(p-i\in Q\) proves both preserve incidence, and \(d^2=1\), \(dsd=s^{-1}\). Thus they act simplicially on \(K_2\). For any automorphism \(g\), the simplicial Lefschetz number is
\[
L(g)=\sum_{\sigma:g\sigma=\sigma}(-1)^{\dim\sigma}\operatorname{sgn}(g\vert_{\sigma}).
\]
Since only ordinary \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{21}\) survive, \(L(g)=1-\chi(g)\). Every nonidentity \(s^a\) acts freely on points and freely on blocks, so its only setwise fixed nonempty simplices are the two pure ten-simplices. Each contributes \(+1\); therefore \(L(s^a)=2\) and \(\chi(s^a)=-1\).

The involution \(d\) pairs every point with a block. An invariant simplex can only be a union of exchanged pairs. Its fixed edges are precisely \(\{p,B_{-p}\}\) for \(2p\in Q\): there are five. Each edge is reversed by \(d\), contributing chain-trace \(-1\) in dimension one. Its invariant tetrahedra correspond exactly to pairs \(\{p,r\}\) among \(\{2,6,7,8,10\}\) with \(p+r\in Q\): these five pairs are \(\{2,7\},\{2,10\},\{6,8\},\{6,10\},\{7,8\}\). Each tetrahedron undergoes two transpositions, contributing \(+1\) in dimension three. There are no other invariant simplices. Hence \(L(d)=(-1)(-5)+(-1)(+5)=0\), so \(\chi(d)=1\). Every \(s^a d\) is conjugate to \(d\), because two is invertible modulo eleven, and has the same trace. The displayed character follows.

Finally, the unique ten-dimensional irreducible rational representation \(W\) of \(D_{22}\) is the rational sum of the five two-dimensional complex rotation characters. Its traces are ten at identity, minus one at nonidentity rotations, and zero at reflections. The character \(\mathbf1\oplus2W\) matches all 22 values; Maschke semisimplicity yields the decomposition. For the order-two map \(d\), the dimensions of the two rational eigenspaces are \((21+1)/2=11\) and \((21-1)/2=10\).

## Verification
The standard-library-only certificate `verify_biplane_dihedral.py` independently constructs the cyclic difference-set incidence graph; verifies every pairwise design incidence and every shortest-path distance; enumerates all 79 maximal radius-two cliques without using the proof's facet formula; checks the exact 34-by-34 oriented square-cycle determinant \(-1\); enumerates all scale-two simplices and verifies mod-two homology; checks the dihedral relations and preservation of all maximal simplices; and computes the integer signed simplicial Lefschetz traces for all 22 elements. For clarity it reports the full face vector \((22,165,550,935,1034,946,660,330,110,22,2)\) and mod-two Betti vector \((1,0,0,21,0,0,0,0,0,0,0)\). The script has no precomputed group-character output as input and requires no specialized mathematical package. The integral conclusion comes from the verified unimodular minor and the CW argument, not mod-two ranks.

## Relationship to prior work
Brown's archived account establishes the classical biplane and its cyclic difference-set description, not the Vietoris–Rips homotopy or dihedral homology action. White's biplane surface-embedding study concerns embeddings of Cayley graphs on two-manifolds rather than the flag complex of the incidence graph's square. Kawamura studies homology relations among flag complexes of squares of bipartite graphs, but the inspected theorem does not provide this biplane's 34-by-55 attaching map, its degree-three homology, or the part-exchanging dihedral character. Adamaszek studies graph powers more broadly without an equivalent incidence-geometry computation.

A prior accessible finding computes a **different** simplicial complex on the eleven points, generated by the eleven five-element blocks, and its point-preserving symmetry character. Its \(21\) second-sphere summands are acknowledged: they do not themselves specify the radius-two Rips complex on 22 point-and-block vertices or the action of a point–block **duality** on the latter's third homology. In particular the new, explicitly computed duality eigenspace dimensions require an action that is not even defined on that point-only complex. Previous projective-plane and affine-plane incidence-Rips classifications assume pairwise incidence number one, whereas the present biplane has number two and 55 additional tetrahedral cells. Their statements do not imply this group character.

## Limitations
This is the natural dihedral subgroup of order 22, not a claimed full rational decomposition under the entire incidence-graph automorphism group. The result applies only to this explicit finite biplane and the inclusive shortest-path Rips convention; there is no assertion for arbitrary symmetric designs or general biplanes. The proof uses the standard comparison of a union of two contractible simplicial subcomplexes with the suspension of their intersection, cellular attaching maps, and the Lefschetz formula. Its finite integer determinant and exact character computation are reproducible but still warrant external mathematical checking. A prior nonequivariant block-complex result has the same sphere multiplicity one dimension lower; whether a broader natural suspension equivalence is already documented poses a residual priority risk. Unindexed equivalent work cannot be excluded.

## References
Ezra Brown, *The Fabulous (11, 5, 2) Biplane*, Mathematics Magazine 77 (April 2004), 87–100, DOI 10.1080/0025570X.2004.11953234. The source provides month-level publication evidence; no exact April publication day is asserted.

Hugo Pfoertner, OEIS A095028, *An example of a (11,5,2) cyclic difference set*, dated 2004-06-02, https://oeis.org/A095028. This is the earliest independently confirmed **day-precise public source evidence** for the chosen explicit block set; Brown's earlier April 2004 publication is acknowledged separately.

Arthur T. White, *Modelling biplanes on surfaces*, European Journal of Combinatorics 25 (2004), 899–909, DOI 10.1016/j.ejc.2003.05.004.

Kazuhiro Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, Contributions to Discrete Mathematics 6 (2011), 91–100, DOI 10.55016/ojs/cdm.v6i2.62059; published 2011-10-20.

Michal Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first submitted 2011-04-03.

Published projective-plane comparison: *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3.

Published affine-plane comparison: *Affine-plane incidence Rips complexes have two sphere dimensions* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4.
