# Exact Euclidean Vietoris–Rips persistence of the uniform hexagonal antiprism

## Finding

Let \(P\subset\mathbb R^3\) be the twelve vertices of the unit-edge uniform hexagonal antiprism, with the ordinary Euclidean metric. Write \(K_r=\operatorname{VR}_{\le r}(P)\), so an arbitrary nonempty vertex subset is a face exactly when all its pairwise Euclidean distances are at most \(r\). Set
\[
\rho_1=1,\qquad \rho_2=\sqrt{1+\sqrt3},\qquad
\rho_3=\sqrt3,\qquad \rho_4=2,\qquad
\rho_5=\sqrt{1+2\sqrt3}.
\]
These thresholds are strictly increasing. The entire integral homotopy filtration is
\[
K_r\simeq\begin{cases}
\bigvee^{11}S^0,&0\le r<\rho_1,\\
S^1,&\rho_1\le r<\rho_2,\\
S^1,&\rho_2\le r<\rho_3,\\
\bigvee^3S^2,&\rho_3\le r<\rho_4,\\
\bigvee^2S^3,&\rho_4\le r<\rho_5,\\
\ast,&r\ge\rho_5.
\end{cases}
\]
The first line means twelve isolated points. This determines the reduced **integral persistence** as well: the eleven degree-zero bars die at \(\rho_1\); the unique degree-one bar is \([\rho_1,\rho_3)\), crossing \(\rho_2\) with an isomorphism; there are three degree-two bars \([\rho_3,\rho_4)\), and two degree-three bars \([\rho_4,\rho_5)\). No other reduced integral bars occur. All nonzero groups are free abelian.

## Assumptions and scope

Use the cyclic indices \(i=0,\ldots,5\), read modulo six, and define
\[
T_i=(\cos(\pi i/3),\sin(\pi i/3),h/2),\quad
B_i=(\cos(\pi i/3+\pi/6),\sin(\pi i/3+\pi/6),-h/2),
\qquad h^2=\sqrt3-1.
\]
Thus each horizontal hexagon has circumradius one, horizontal side length one, and the two nearest cross-layer edges also have length one. The convex hull is the uniform hexagonal antiprism, with twelve equilateral triangular side faces and two regular hexagonal caps. In the reproducibility files the labels \(0,\ldots,5\) mean \(T_0,\ldots,T_5\), while \(6,\ldots,11\) mean \(B_0,\ldots,B_5\). All distance thresholds are inclusive. No assertion concerns arbitrary deformations, surface-geodesic metrics, or the continuous point set on the solid's boundary.

## Proof

**1. Exact metric shells.** Within one hexagonal ring, squared pairwise distances are \(1,3,4\), according to cyclic separations one, two and three. Between a top and a bottom vertex, the cosine rule gives
\[
\lVert T_i-B_j\rVert^2
=1+\sqrt3-2\cos\!\left(\frac{(2(i-j)-1)\pi}{6}\right)
\in\{1,1+\sqrt3,1+2\sqrt3\}.
\]
The five squared-distance shells \(1,1+\sqrt3,3,4,1+2\sqrt3\) contain respectively \(24,12,12,6,12\) unordered pairs, exhausting all \(\binom{12}{2}=66\) pairs. Consequently there are exactly five nontrivial filtration events.

**2. Two initial circles, and persistence.** Exhaustively enumerating complete subgraphs yields face vectors (including vertices) \((12,24,12)\) at \(\rho_1\) and \((12,36,36,12)\) at \(\rho_2\). The exact free-face deletion certificate in `collapse_certificate.json` removes respectively 18 and 43 codimension-one pairs, reducing the two complexes to simple cycles of six and five edges. The companion `verify.py` reconstructs all faces and independently checks the unique-coface condition at each deletion. Hence both stages have integral homotopy type \(S^1\).

It is important that the induced map between their first homology groups is an **isomorphism**, not merely a nonzero rational map. Give top vertex \(T_i\) angular index \(2i\pmod{12}\) and bottom vertex \(B_i\) index \(2i+1\pmod{12}\). Every edge at \(\rho_2\) has a unique signed short angular displacement \(\delta\in\{-3,-2,-1,1,2,3\}\). On every triangle the three displacements sum to zero: the sum is divisible by twelve but has absolute value at most nine. For an integral edge cycle the sum of displacements is divisible by twelve, so its winding \(\frac1{12}\sum\delta\) is an integer homology functional. The oriented top hexagonal ring has winding one. It is a generator of the first homology of the \(\rho_1\) stage (by the first collapse) and of the \(\rho_2\) stage (because the latter is a circle and it has winding one). Thus inclusion acts by \(\pm1\).

**3. Three two-spheres.** At \(\rho_3\), the face vector is \((12,48,76,48,12)\). The independent certificate removes 65 free pairs and leaves a connected, two-dimensional subcomplex with face vector \((12,31,23)\), hence Euler characteristic four. To verify its fundamental group, start with the preceding circle stage. Every newly inserted edge is a two-step chord of a horizontal hexagon and bounds a new triangle together with two older consecutive edges; therefore the map on fundamental groups from the preceding stage is surjective. Its generator, the top ring, becomes null-homotopic: the four triangles with vertex sets \((0,1,2)\), \((0,2,4)\), \((2,3,4)\), \((0,4,5)\) form a disk with the top hexagon as boundary. Thus the new complex is simply connected. A connected simply connected two-dimensional finite CW complex with Euler characteristic four has free second homology of rank three and is homotopy equivalent to a wedge of three two-spheres. Indeed, the Hurewicz isomorphism supplies three sphere maps that induce an integral homology isomorphism; the homological Whitehead theorem makes their wedge a homotopy equivalence.

**4. Two three-spheres from a forbidden twelve-cycle.** At \(\rho_4\), all pairs except those with squared distance \(1+2\sqrt3\) are present. The twelve missing edges form a single cycle, every vertex having exactly two missing neighbors and the missing-edge graph being connected. Therefore the clique complex of the allowed graph is **exactly** the independence complex \(\operatorname{Ind}(C_{12})\) of a twelve-cycle. The classical cycle-independence recurrence \(\operatorname{Ind}(C_n)\simeq\Sigma\operatorname{Ind}(C_{n-3})\) (in the appropriate range) and \(\operatorname{Ind}(C_3)\simeq S^0\vee S^0\) give three suspensions and thus
\[
K_{\rho_4}\cong\operatorname{Ind}(C_{12})\simeq S^3\vee S^3.
\]
This well-established independence-complex theorem is explicitly prior work, not a newly claimed result. The face vector \((12,54,112,105,36,2)\) and the missing-edge graph are independently verified by `verify.py`.

**5. Contractibility and all maps.** When \(\rho_5\) is reached, all sixty-six edges are present and the Rips complex is the eleven-simplex. No further distance shells exist. The sole map between consecutive nonzero positive-degree homology groups is the degree-one map from step 2, already proved to be an integral isomorphism. All other maps into a later nonzero degree group vanish because their source is zero in that degree or because the intermediate stage has zero homology in that degree. This proves all asserted interval endpoints and maps, including the zero-degree death at the first connected scale.

## Verification

The packaged files `collapse_certificate.json`, `verify.py`, and `verification_output.txt` give a self-contained, standard-library-only exact combinatorial replay. The verifier recomputes the 66 Euclidean pairwise distances (checking against the symbolic shell classifications), enumerates all nonempty cliques in every stage, verifies each elementary collapse with an actual unique coface at the moment of removal, checks the angular winding cocycle, validates the four-triangle filling, and identifies the complement twelve-cycle. It separately calculates boundary-matrix ranks over \(\mathbb F_2\), finding reduced nonzero Betti ranks \(1,1,3,2\) in degrees \(1,1,2,3\) at the four nontrivial preterminal stages. The integral homotopy proof uses actual simplicial collapses, the fundamental-group argument, and the established integral cycle-independence theorem, rather than inferring integral results from field-rank experiments.

## Relationship to prior work

Saleh, Titz Mite and Witzel [1] classify Vietoris–Rips complexes of vertex sets of **Platonic** solids and explicitly identify Archimedean solids as a plausible extension; their theorem does not cover the hexagonal antiprism. The present object is a uniform antiprism, with ordinary Euclidean rather than graph-shortest-path distances.

The final noncontractible stage has a previously known abstract homotopy type by the cycle-independence recurrence, as discussed by Adamaszek [2] and recalled by Przytycki and Silvero [3]. Its occurrence as the penultimate Euclidean Rips stage follows from the new exact distance-shell identification; only the complete Euclidean antiprism filtration, its intermediate \(\bigvee^3S^2\) stage, and its persistence maps are offered as additions. Earlier Rips classifications of other polyhedra, even with identical Betti counts, do not imply this object's exact metric filtration without a metric or simplicial isomorphism, neither of which is present here.

## Limitations

This is a finite twelve-point classification, not a theorem for all antiprisms. The integral homotopy equivalences are nonequivariant; no representation-valued barcode or integral symmetry-module decomposition is asserted. Bibliographic searches cannot rule out an equivalent unindexed calculation, and no independent external mathematical audit has been performed. The verification program tests the explicitly finite stages and certificates; the infinite topological statements additionally rely on the mathematical arguments above and on the cited classical independence-complex result.

## References

[1] N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, first submitted February 28, 2023, arXiv:2302.14388v1, https://arxiv.org/abs/2302.14388 .

[2] M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, https://arxiv.org/abs/1106.6250 . (The introductory discussion records Kozlov's classical cycle recurrence.)

[3] J. H. Przytycki, M. Silvero, *Khovanov homology, wedges of spheres and complexity*, 2024, Proposition 3.6(3), https://doi.org/10.1007/s13398-024-01594-z .
