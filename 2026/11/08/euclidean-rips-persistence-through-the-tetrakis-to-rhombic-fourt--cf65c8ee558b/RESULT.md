# Euclidean Rips persistence through the tetrakis-to-rhombic fourteen-point family

## Finding
Fix a real parameter \(3/2\le t\le2\). Consider the fourteen-point Euclidean metric space
\[
P_t=\{(\pm1,\pm1,\pm1)\}\cup\{\pm t e_1,\pm t e_2,\pm t e_3\}\subset\mathbb R^3.
\]
The endpoints are the standard vertex realizations of the tetrakis hexahedron (\(t=3/2\)) and rhombic dodecahedron (\(t=2\)). Define
\[
a(t)=\sqrt{t^2-2t+3},\qquad e(t)=\sqrt{t^2+2t+3},\qquad
\delta(t)=\min\{2t,2\sqrt3\}.
\]
For the *inclusive* Euclidean Vietoris–Rips complex, with a simplex present when every pairwise distance is at most \(r\), the complete **integral homotopy-type filtration** is
\[
\operatorname{VR}_{\le r}(P_t)\simeq
\begin{cases}
\bigvee^{13}S^0,&0\le r<a(t),\\
\bigvee^{11}S^1,&a(t)\le r<2,\\
S^2,&2\le r<2\sqrt2,\\
S^3,&2\sqrt2\le r<e(t),\\
S^6,&e(t)\le r<\delta(t),\\
\ast,&r\ge\delta(t).
\end{cases}
\]
The positive-degree **integral persistence** consists of exactly eleven degree-one bars \([a(t),2)\), one degree-two bar \([2,2\sqrt2)\), one degree-three bar \([2\sqrt2,e(t))\), and one degree-six bar \([e(t),\delta(t))\). Reduced degree-zero persistence has thirteen bars \([0,a(t))\); ordinary degree zero also has one permanent bar. All homology is torsion-free. These are genuine inclusion-induced bars, not merely lists of Betti numbers.

The death mechanism of the six-dimensional class changes at the exact geometric parameter \(t=\sqrt3\). For \(t<\sqrt3\), all three antipodal *axial* pairs become adjacent at once, and the six axial vertices span a simplex; for \(t>\sqrt3\), all four *corner* antipodal pairs become adjacent at once, and the eight corners span a simplex. At equality both kinds appear simultaneously. Thus the homology ranks have a stable pattern across the entire interpolation, while the combinatorial event terminating the final sphere changes type.

## Assumptions and scope
All distances are ambient Euclidean distances, not graph shortest-path distances. The vertices are the fourteen distinct points displayed above, without generic-position perturbations. Parameter endpoints and all filtration thresholds are included on the left. Results apply for every real \(t\) in the closed interval, including \(t=2\) where two distance shells merge and \(t=\sqrt3\) where two death shells merge. Nothing is claimed for parameters outside this interval, for continuous polyhedral surfaces, or for other metrics.

## Proof
Every unordered pair of vertices belongs to exactly one of seven distance classes. The squared distances and multiplicities are
\[
\begin{array}{c|c|c}
\text{pair type}&\text{squared distance}&\text{number}\ \hline
\text{axis--corner (matching sign)}&t^2-2t+3&24\\
\text{cube edges}&4&12\\
\text{orthogonal axis pairs}&2t^2&12\\
\text{cube face diagonals}&8&12\\
\text{axis--corner (opposite sign)}&t^2+2t+3&24\\
\text{antipodal axes}&4t^2&3\\
\text{antipodal cube corners}&12&4
\end{array}
\]
For \(3/2\le t\le2\) these classes occur in the order just displayed, except that the last two may interchange at \(t=\sqrt3\) and the third and fourth coincide at \(t=2\). Indeed \(t^2-2t+3<4<2t^2\le8<t^2+2t+3<\min\{4t^2,12\}\) on this interval; the non-strict inequality is only at \(t=2\). The final comparison is \(4t^2\lessgtr12\) according as \(t\lessgtr\sqrt3\). Thus the abstract complexes between critical values are independent of \(t\), except for coincident or exchanged last shells.

At the first shell there are fourteen vertices and twenty-four edges, forming a connected graph, hence a wedge of eleven circles. At the second shell, the twenty-four triangles are precisely those of the boundary of the tetrakis-hexahedral combinatorial sphere: twelve cube edges each border two distinct axial pyramid faces. Direct incidence and vertex-link checks show a connected closed triangulated two-manifold of Euler characteristic two, hence \(S^2\).

At the third shell (twelve orthogonal axial edges), the complex has face vector \((14,48,56,20)\). The complete explicit list of **32 elementary simplicial collapse pairs** in `collapse_certificate.json` retracts it *onto the preceding boundary two-sphere*. The included `verify.py` independently checks that each lower face has the stated unique cofacet at the time of removal and that exactly the earlier complex remains. Thus the inclusion of the boundary sphere into this otherwise three-dimensional thickening is a homotopy equivalence; the two-dimensional persistence class survives this intermediate shell.

At the fourth shell (twelve corner face-diagonal edges), the complex has face vector \((14,60,100,60,6)\). Another **80 exact elementary collapses** retract it onto the induced complex on the eight cube corners. Every two corners are adjacent except when opposite, so this target is the join of four two-point sets, homeomorphic to \(S^3\).

At the fifth shell, all axial--corner pairs are adjacent, and the only missing edges are three axial-antipodal pairs and four cube-antipodal pairs. The flag complex is therefore the join of seven copies of \(S^0\), hence \(S^6\). This is a genuine combinatorial sphere, not a conclusion from rational Betti numbers.

At the earlier of the last two shells, either all six axes span a simplex or all eight corners span a simplex. Since every cross-type edge is already present, the full complex has a cone factor in either case and is contractible thereafter. These stages exhaust all possible simplicial changes.

For the persistence assertion, all nonzero reduced homology groups are free abelian and occur in distinct dimensions at successive essential stages. The only adjacent stages with the same nonzero positive-degree homology are the two-sphere stage and its axial-edge thickening; the relative collapse gives a homotopy inverse to their inclusion. All other interval deaths are forced by zero homology in that degree at the next stage. The connected graph at the first shell kills the thirteen reduced degree-zero classes, and no later stage can revive them. This proves the entire stated integral barcode.

## Verification
The reproducible artifacts `verify.py` and `collapse_certificate.json` use integer coordinates at \(t=3/2\), scaled uniformly by two. Thus their exact squared-distance shells are \(9,16,18,32,33,36,48\). The verifier enumerates all nonempty subsets of fourteen vertices and independently constructs their flag complexes at these thresholds. It checks the stage face vectors, connectivity of the twenty-four-edge graph, all vertex links and edge incidences of the two-sphere, the exact 32 and 80 collapse pairs, the cross-polytope join descriptions, and the cone after axial-antipodal edges appear. It also computes independent simplicial boundary ranks over \(\mathbb F_2\) at all five nontrivial stages. `verification_output.txt` contains the actual execution result.

The uniform-parameter proof is algebraic: the seven squared-distance expressions above have no additional ordering changes on the stated closed interval, so the one exact integer model checks every combinatorial type needed throughout. The collapse certificate and the geometric identifications, rather than sampled numeric barcodes, establish integral homotopy and persistence.

## Relationship to prior work
Saleh, Titz Mite, and Witzel (arXiv:2302.14388, first posted 2023-02-28) classify Vietoris–Rips homotopy types for the five **Platonic** solids; their introduction explicitly discusses extending the program to other solid families. The present two-orbit, fourteen-vertex Catalan interpolation is not one of their five regular-solid vertex sets. Saleh's 2023 thesis likewise concentrates its homotopy classification on Platonic solids (Chapter 3). Its separate experiments on Catalan solids concern, among other spaces, a different 32-vertex rhombic triacontahedron and a disdyakis triacontahedron, not this fourteen-point family. Chapter 4 treats higher-dimensional polytopes.

The special case \(t=2\) is the rhombic-dodecahedral endpoint and its individual Euclidean homotopy filtration has been previously determined. No novelty is claimed for the endpoint alone. The claim here is the **continuum-wide exact integral persistence formula**, including the additional axial-thickening stage when \(t<2\), the homotopy equivalence across that stage, and the phase change in the final death mechanism at \(t=\sqrt3\). Graph-metric results for the distinct 24-vertex truncated-octahedral solid, and Euclidean results for the 12-vertex cuboctahedron, do not determine this two-orbit parameter family.

## Limitations
Only the fourteen prescribed vertices and \(3/2\le t\le2\) are covered. The exact homotopy types do not provide a classification of the full symmetry representations on homology or the behavior under arbitrary nonsymmetric perturbations. The numerical checker tests one rational representative of each abstract shell; the uniform result additionally relies on the symbolic ordering argument in the proof. Literature searches and the inspected primary texts do not establish a proof of absolute publication priority; equivalent unindexed work remains possible.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first public version 2023-02-28), https://arxiv.org/abs/2302.14388.
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation, Justus Liebig University Giessen (2023), DOI:10.22029/jlupub-17950.
3. *Tetrakis hexahedron*, standard Catalan-solid coordinates and duality with the truncated octahedron, https://en.wikipedia.org/wiki/Tetrakis_hexahedron (geometry reference only).
