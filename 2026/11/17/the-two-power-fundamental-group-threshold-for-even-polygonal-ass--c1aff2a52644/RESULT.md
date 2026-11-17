# The two-power fundamental-group threshold for even polygonal associahedral symmetry quotients

## Finding
For each even integer \(n\ge6\), let \(K_n\) be the simplicial complex whose vertices are diagonals of a convex regular \(n\)-gon and whose simplices are collections of pairwise noncrossing diagonals. Its geometric realization is an \((n-4)\)-sphere. The dihedral group
\[
D_n=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle
\]
acts by \(r(i)=i+1\) and \(s(i)=-i\) on polygon labels modulo \(n\).

**Theorem (complete even-size orbit-space fundamental-group classification, with supporting fixed-space formulas).** Write \(C_q=\langle r^{n/q}\rangle\) for each divisor \(q\mid n\), and \(D_{q,a}=\langle r^{n/q},r^as\rangle\), where \(0\le a<n/q\). Every subgroup of \(D_n\) is of one of these forms. Put \(m=n/q\), and
\[
f(m,a)=\#\{j\in\mathbb Z/m\mathbb Z:2j\equiv a\pmod m\}=
\begin{cases}
1,&m\text{ odd},\\
2,&m\text{ even and }a\text{ even},\\
0,&m\text{ even and }a\text{ odd}.
\end{cases}
\]
With the convention \(S^{-1}=\varnothing\), all the *actual geometric fixed-point spaces* have the following homeomorphism types:
\[
|K_n|^{C_q}\cong
\begin{cases}S^{n-4},&q=1,\\ S^{m-2},&q>1,\end{cases}
\]
\[
|K_n|^{D_{q,a}}\cong
\begin{cases}
S^{(n+f(n,a))/2-3},&q=1,\\
S^{(m+f(m,a))/2-2},&q>1.
\end{cases}
\]
Furthermore the ordinary topological orbit-space fundamental group is
\[
\pi_1(|K_n|/H)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&H=C_n\text{ and }n=2^e\text{ with }e\ge3,\\
1,&\text{for every other subgroup }H\le D_n.
\end{cases}
\]
The same formula holds for \(H_1(|K_n|/H;\mathbb Z)\), with trivial first homology interpreted as zero. In particular, a nontrivial fundamental group is possible **only** for the full rotation quotient of a polygon with a power-of-two number of vertices; adding any reflection kills it.

## Assumptions and scope
The group acts on diagonal labels, and the quotient is the ordinary quotient of geometric realizations, not the abstract complex on orbit vertices. The reflection \(s\) fixes label zero. In the notation \(D_{q,a}\), the parameter \(a\) is chosen modulo \(m=n/q\). The fixed-point expressions are about simultaneous fixed points of the entire subgroup; such a space can be empty even though individual generating reflections each fix points. Every stated assertion is restricted to **even** \(n\ge6\); odd polygon sizes are excluded from the novelty claim because their harmonic representation models overlap existing nonmatching-complex classifications.

## Proof
**1. Equivariant representation sphere.** Regard the regular polygon vertices as \(A=\{(\cos(2\pi i/n),\sin(2\pi i/n)):0\le i<n\}\). Its secondary polytope \(\Sigma(A)\) is a convex \((n-3)\)-dimensional associahedron: faces correspond to polygonal subdivisions, and the face poset of its polar is the noncrossing-diagonal complex. The construction is natural under the dihedral permutations of the coordinates. The affine hull of \(\Sigma(A)\), translated to the origin, is exactly
\[
V_n=\bigl\{x\in\mathbb R^n:\sum_i x_i=0,\ \sum_i x_i\cos(2\pi i/n)=0,\ \sum_i x_i\sin(2\pi i/n)=0\bigr\}.
\]
This is the orthogonal complement of the constant and planar first-harmonic subrepresentations in the permutation representation on polygon vertices. The centroid of all vertices of the full-dimensional polytope is a dihedrally fixed interior point. Radial projection about that centroid identifies its boundary equivariantly with the unit sphere \(S(V_n)\). Polar duality, using the invariant Euclidean inner product, identifies the boundary of the polar with \(|K_n|\) equivariantly. Consequently
\[
|K_n|\cong_{D_n} S(V_n),\qquad \dim_{\mathbb R}V_n=n-3.
\]
In particular this sphere is simply connected for every \(n\ge6\). This use of the secondary-polytope construction is classical; the new claim concerns the complete subgroup orbit-space fundamental groups.

**2. Fixed-point dimensions.** For an orthogonal real representation \(V\) and subgroup \(H\), the fixed points of the unit sphere are exactly \(S(V^H)\). In the polygon-label permutation module \(\mathbb R^n\), the dimension of the invariant subspace equals the number of orbits of \(H\) on the vertex labels. The constant line always contributes one invariant dimension. The first-harmonic planar representation has two fixed dimensions for the trivial subgroup, one for a reflection alone, and none for any group containing a nonidentity rotation. Because these three summands split orthogonally, the required dimension of \(V_n^H\) is the vertex-orbit count minus these invariant affine dimensions.

For \(C_1\), the orbit count is \(n\), hence \(\dim V_n^{C_1}=n-3\). For a nontrivial \(C_q\), its \(m=n/q\) orbits of labels are the congruence classes modulo \(m\). Subtracting the constant line gives \(\dim V_n^{C_q}=m-1\).

For \(D_{q,a}\), the \(C_q\) orbits become an \(m\)-point set, on which the residual reflection sends \(j\) to \(a-j\). Its fixed residue classes satisfy \(2j\equiv a\pmod m\), so the total number of orbits is \((m+f(m,a))/2\). If \(q=1\), subtract the constant line and the single invariant axis of reflection on the first harmonic, giving \(\dim V_n^{D_{1,a}}=(n+f(n,a))/2-2\). If \(q>1\), subtract only the constant line, giving \(\dim V_n^{D_{q,a}}=(m+f(m,a))/2-1\). The sphere dimensions in the theorem are one less, and dimension zero produces the declared empty fixed set.

**3. The exact stabilizer criterion.** A nonidentity rotation \(r^b\) generates the subgroup \(C_q\) with \(q=n/\gcd(n,b)\). By Step 2, its fixed-point set is nonempty exactly when \(\gcd(n,b)\ge2\). Every individual reflection \(r^as\) also fixes a point: the fixed dimension \((n+f(n,a))/2-2\) is at least one for even \(n\ge6\). Notice that this statement about *individual* reflections does not assert that an arbitrary reflection-containing subgroup has a common fixed point.

**4. Orbit-space fundamental groups.** Armstrong's theorem for finite actions on a simply connected, locally connected and semilocally simply connected space identifies
\[
\pi_1(S(V_n)/H)\cong H/N_H,
\]
where \(N_H\) is the normal subgroup generated by elements of \(H\) fixing at least one point. If \(H=C_q\) is proper in the full rotation group, its generator \(r^m\) has \(m=n/q\ge2\) and therefore fixes a point. Thus \(N_H=H\). The trivial subgroup is already simply connected.

For the full rotation group \(C_n\), Step 3 says the stabilizing elements are exactly the \(r^b\) with \(\gcd(n,b)\ge2\). If \(n=2^e\), these are precisely the even powers, generating \(\langle r^2\rangle\), so the quotient is \(C_2\). Otherwise, since \(n\) is even and not a power of two, it has an odd prime divisor \(p\). Both \(r^2\) and \(r^p\) fix points and together generate the full rotation group; hence the fundamental group is trivial.

Finally, any subgroup containing a reflection has the form \(D_{q,a}\) and is generated by two reflections \(r^as\) and \(r^{a+m}s\), with their product equal to a rotation generator or its inverse. Each of these reflections has a fixed point by Step 3. Therefore \(N_H=H\) and the orbit-space fundamental group vanishes. This exhausts all subgroups. Abelianizing gives the stated integral first-homology formula.

## Verification
The included standalone Python file `verify_even_associahedron.py` independently computes the number of orbits of each subgroup on polygon vertices, subtracts the fixed affine coordinates, and compares all results against the Fourier description
\[
V_n\cong\mathbb R_{\mathrm{alt}}\oplus\bigoplus_{k=2}^{n/2-1}\mathbb C_k
\]
for even \(n\). The character \(r\) acts by minus one on the alternating line and by \(e^{2\pi i k/n}\) on \(\mathbb C_k\), while \(s\) fixes the alternating line and conjugates each complex coordinate. For all even sizes from 6 through 100, the program checks 5,508 separate cyclic or dihedral fixed-dimension comparisons. It also checks that every individual reflection fixes points and that the full-rotation stabilizing exponents generate an index-two subgroup precisely for powers of two. It is executable with `python3 verify_even_associahedron.py` without additional dependencies. These finite checks corroborate the proof but are not an infinite-parameter proof.

## Relationship to prior work
The classical secondary-polytope construction and Reiner's equivariant fiber-polytope treatment supply the equivariant associahedral sphere and describe invariant secondary polytopes; these are premises, not new findings. The 2002 generalized-associahedron literature supplies the canonical type-A combinatorial realization. Armstrong's theorem supplies the general orbit fundamental-group formula but does not evaluate its stabilizer subgroup for even polygonal associahedra. A published result on dihedral fixed spaces of cyclic nonmatching complexes has an apparently similar harmonic-sphere formalism, but its representation has only paired real harmonic dimensions and does not include the alternating real line of the even-polygon associahedron. A published prime-power fundamental-group dichotomy concerns a different bidirected-polygon multipath complex, not the noncrossing-diagonal complex. Previously recorded lens quotients for *odd prime* polygonal diagonal complexes and graph-associahedral quotients do not imply this even-size all-subgroup formula. The new content is the natural complete even-size, subgroup-by-subgroup fixed-space and fundamental-group classification, especially the sharp power-of-two exceptional family.

## Limitations
No homology in degrees above one, cohomology ring, stable equivariant equivalence beyond the explicitly given homeomorphism, or full homotopy type of nontrivial quotients is asserted. The proof uses standard published polytope and orbit-space theorems; its new arithmetic classification is a specialization of those tools and does not claim to introduce a new general topological method. An equivalent unindexed combination of those tools, or an inaccessible stronger statement about the same even-polygon action, remains a publication-priority risk. Finite numerical verification is not an independent audit.

## References
1. V. Reiner, *Equivariant fiber polytopes*, Documenta Mathematica 7 (2002), pp. 113–132, especially Section 4.1, Proposition 4.2. https://www-users.cse.umn.edu/~reiner/Papers/EFP.pdf
2. F. Chapoton, S. Fomin and A. Zelevinsky, *Polytopal realizations of generalized associahedra*, arXiv:math/0202004, first publicly submitted 2002-02-01. https://arxiv.org/abs/math/0202004
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proceedings of the Cambridge Philosophical Society 61 (1965), pp. 639–646. DOI 10.1017/S0305004100038974. https://wrap.warwick.ac.uk/id/eprint/74313/1/WRAP_Thesis_Armstrong_1966.pdf
4. *Dihedral fixed spaces, lens quotients, and sphere quotients of cyclic nonmatching complexes*, published mathematical research record (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dihedral-fixed-spaces-lens-quotients-and-sphere-quotients-of-cyc--97d699d064c0
5. *Prime-power fundamental groups and unbounded torsion in bidirected-polygon orbit spaces*, published mathematical research record (2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-prime-power-fundamental-groups-and-unbounded-torsion-in-bidirect--019b8ac173fd
