# Weight-two translation fixed spaces of scale-three hypercube Vietoris–Rips complexes

## Finding

Give the binary cube \(Q_n=\{0,1\}^n\) its Hamming metric. Let \(X_n=\operatorname{VR}_{\le3}(Q_n)\) be the **inclusive** distance-three Vietoris–Rips complex. Let \(\tau\) translate by any binary vector of weight exactly two. Then \(|X_n|^{\langle\tau\rangle}\) is contractible for \(n=2,3\). For every \(n\ge4\), write \(m=n-2\) and
\[
V_m=2^m,\qquad E_m=m2^{m-1},\qquad F_m=\binom{m}{2}2^{m-2}.
\]
The **integral homotopy classification** is
\[
\boxed{|X_n|^{\langle\tau\rangle}\simeq
  \bigvee^{V_m-E_m+F_m-1}S^2\ \vee\ \bigvee^{F_m}S^3.}
\]
Here a zero-summand wedge contributes no summand. In particular the types for \(n=4,5,6,7,8\) are respectively \(S^3\), \(S^2\vee6S^3\), \(7S^2\vee24S^3\), \(31S^2\vee80S^3\), and \(111S^2\vee240S^3\), where \(aS^j\) abbreviates a wedge of \(a\) copies of \(S^j\).

## Assumptions and scope

All complexes are finite and their geometric realizations use the ordinary topological simplicial realization. A simplex in \(X_n\) is a set of binary vectors with **all** pairwise Hamming distances at most three. We take the pointwise fixed space in the geometric realization, not a quotient of the abstract vertex set and not a Borel construction. By permuting coordinates, it suffices to flip the first two coordinates. The theorem applies to every integer \(n\ge2\); no field coefficients or stable-range hypotheses are imposed.

## Proof

**1. Exact orbit description.** Put \(m=n-2\), so the original vertices are \((u,y)\) with \(u\in\{0,1\}^2\) and \(y\in Q_m\). The two types of \(\tau\)-orbits above each \(y\) are
\[
A_y=\{(00,y),(11,y)\},\qquad
B_y=\{(01,y),(10,y)\}.
\]
Each orbit itself has diameter two and hence is a simplex. For a finite simplicial complex with a finite group acting simplicially, a point is fixed precisely when its barycentric coordinates are constant along each vertex orbit. Therefore the pointwise fixed space is **homeomorphic** to the realization of the complex \(K_m\) whose vertices are these two orbit types, and whose faces are collections of orbits whose union is an original simplex. Pairwise diameter checks suffice because \(X_n\) is flag.

If \(d=d_{Q_m}(y,z)\), the maximum distance between points of \(A_y,A_z\) (and similarly \(B_y,B_z\)) is \(d+2\), and the maximum between points of \(A_y,B_z\) is \(d+1\). Consequently the orbit-compatibility graph has exactly the edges
\[
A_yA_z,\ B_yB_z\quad\Longleftrightarrow\quad d(y,z)=1,
\qquad A_yB_z\quad\Longleftrightarrow\quad d(y,z)\le2,
\]
where distinct endpoints are required for same-type edges and \(A_yB_y\) is present. Its clique complex is \(K_m\). When \(m=0\) this is a single edge; when \(m=1\) it is a tetrahedron. Both realizations are contractible.

**2. Square blocks cover all faces.** Assume \(m\ge2\). For each two-dimensional cubical face \(S\subset Q_m\) (four vertices forming a square), let \(B_S\) be the full subcomplex of \(K_m\) on the eight orbit vertices \(A_y,B_y\) with \(y\in S\). The same-type induced graphs in \(S\) are both four-cycles; every cross-type pair in \(S\) is compatible. Thus
\[
B_S=C_4*C_4\cong S^1*S^1\cong S^3.
\]
These blocks cover every face of \(K_m\). Indeed, no clique contains more than two vertices of type \(A\) or more than two of type \(B\), and when two same-type vertices occur their underlying cube points differ in one coordinate. Two cross-compatible singletons differ in at most two coordinates. A same-type edge and a cross-type vertex occupy at most two changing coordinates: if the same-type edge is in direction \(i\), and the third point has \(w\) differing coordinates outside \(i\), the maximum of the two cross distances is \(w+1\le2\). For two edges, of directions \(i,j\), if \(i\ne j\), the largest cross distance is \(w+2\le2\), with \(w\) the number of other varying coordinates; if \(i=j\), that maximum is \(w+1\le2\). Thus all underlying points lie in a two-face. Every smaller face is included in such a two-face because \(m\ge2\).

**3. Thickened cubical one-skeleton.** For each edge \(e=\{y,z\}\) of \(Q_m\), let \(D_e\) be the four-vertex simplex on \(A_y,B_y,A_z,B_z\), and put \(D_m=\bigcup_e D_e\). On \(D_m\), summing the barycentric masses at \(A_y,B_y\) defines a piecewise-linear map to the ordinary cubical one-skeleton \(Q_m^{(1)}\). Its section sends a cube vertex \(y\) to the midpoint of \(A_yB_y\). A straight-line homotopy inside each \(D_e\) is compatible on intersections and gives a strong deformation retraction
\[
D_m\searrow Q_m^{(1)}.
\]
For each square \(S\), its intersection \(E_S=B_S\cap D_m\) is the union of the four edge tetrahedra around the boundary of \(S\); the same deformation retracts \(E_S\) onto the square's boundary circle. In particular \(E_S\simeq S^1\), and the inclusion \(E_S\hookrightarrow B_S\simeq S^3\) is null-homotopic. Moreover any distinct square blocks meet only over a common cube edge, vertex, or not at all. All such intersections lie in \(D_m\); hence a newly adjoined \(B_S\) meets the union of previously adjoined blocks and \(D_m\) **exactly** in \(E_S\).

**4. Integral wedge splitting.** The gluing maps are cofibrations of finite complexes. The standard homotopy-pushout splitting for a null map \(E_S\to B_S\) gives
\[
Z\cup_{E_S}B_S\ \simeq\
  (Z\cup_{E_S}\operatorname{Cone}(E_S))\vee B_S,
\]
with the natural map from the pre-existing subcomplex \(Z\) supported on the first wedge factor, up to homotopy. Apply this successively to all square blocks, using the preceding exact-intersection property. We obtain
\[
K_m\simeq Y_m\vee\bigvee^{F_m}S^3,
\]
where \(Y_m\) is obtained from \(D_m\) by coning off every \(E_S\). The pairwise compatible deformation retractions from step 3 and homotopy pushout invariance identify \(Y_m\) with the cubical two-skeleton \(Q_m^{(2)}\): each cone fills exactly the corresponding square boundary.

The cubical \(m\)-cube is contractible, and its cells of dimensions greater than two do not affect fundamental groups; hence \(Q_m^{(2)}\) is simply connected. It is a finite two-dimensional CW complex with \(V_m\) vertices, \(E_m\) edges, and \(F_m\) squares. Its reduced integral second homology is therefore free of rank \(V_m-E_m+F_m-1\), with no other reduced homology. Hurewicz supplies spherical representatives of a basis, and the homological Whitehead theorem gives
\[
Q_m^{(2)}\simeq\bigvee^{V_m-E_m+F_m-1}S^2.
\]
Combining the displayed equivalences proves the stated integral homotopy type, uniformly for \(m\ge2\). For \(m=2\) the two-sphere multiplicity is zero and the single block is \(S^3\); for \(m=0,1\) the preceding simplex computations give the exceptions. \(\square\)

## Verification

The standalone Python 3 script `verify.py` checks \(n=2,3,4,5,6,7,8\) by reconstructing orbit pairs directly from original Hamming distances, comparing every predicted orbit-compatibility edge, enumerating the entire flag complex independently, and (for \(m\ge2\)) checking equality with the union of all square blocks. It then computes all reduced mod-two Betti numbers from actual simplicial boundary matrices using exact binary elimination, comparing them with the displayed integral ranks. The largest tested complex has 128 orbit vertices, 9,600 nonempty faces, and reduced Betti ranks 111 in degree two and 240 in degree three. Run `python3 verify.py`. The recorded output is in `verification_output.json` and reports `WEIGHT_TWO_FIXED_SPACE_CHECKS_OK`.

These finite calculations do not prove the unrestricted theorem or integral torsion-freeness. Those follow from the geometric decomposition in the proof.

## Relationship to prior work

Galetto, Montaño and Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions* (arXiv:2606.20784v1, first public date 2026-06-23), determine the ordinary characteristic-zero homology representations of the hyperoctahedral action, including scale three. Their Theorem 6.2 and Section 8 address ordinary homology and a spectral-sequence filtration, not the pointwise fixed-space homotopy type. The present orbit-fixed calculation cannot be read off from the ordinary character or from the ambient Betti numbers.

Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs* (arXiv:2305.07084v1, 2023-05-11), Theorem 24, gives the nonequivariant integral homotopy type of the full scale-three hypercube Rips complex; this is a different object from its geometric translation-fixed subspace. Related cube-neighborhood-complex calculations obtain a two-sphere rank equal to the Euler rank of the cubical two-skeleton, but neither that rank nor a nonequivariant complex identifies the additional \(F_m\) three-sphere fixed-point summands.

## Limitations

The result is for a single translation flipping **exactly two** coordinates and for inclusive Hamming scale three. It makes no claim about other translation weights, arbitrary subgroups, maps between subgroup-fixed spaces, an integral symmetry representation on ambient homology, or the full equivariant homotopy type. Literature searches cannot establish absolute novelty; unindexed or subsequently published equivalent work remains a residual risk. Independent mathematical audit has not been performed.

## References

1. Federico Galetto, Jonathan Montaño, Zoe Wellner. *Homology of Vietoris–Rips complexes of hypercube graphs via group actions.* arXiv:2606.20784v1, 2026-06-23. https://arxiv.org/abs/2606.20784
2. Ziqin Feng. *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs.* arXiv:2305.07084v1, 2023-05-11. https://arxiv.org/abs/2305.07084
3. Michał Adamaszek and Henry Adams. *On Vietoris–Rips complexes of hypercube graphs.* arXiv:2103.01040, 2021-03-01. https://arxiv.org/abs/2103.01040
