# Canonical unit-cube generators for scale-two lattice-box Vietoris–Rips complexes

## Finding
For all integers \(a,b,c\ge1\), set
\[
B_{a,b,c}=\{0,\ldots,a\}\times\{0,\ldots,b\}\times\{0,\ldots,c\}\subset\mathbb Z^3,
\qquad K_{a,b,c}=\operatorname{VR}_{\le2}(B_{a,b,c}).
\]
Use Manhattan distance \(d_1(p,q)=\sum_{i=1}^3|p_i-q_i|\). Then
\[
K_{a,b,c}\simeq\bigvee^{abc}S^3,
\qquad\widetilde H_3(K_{a,b,c};\mathbb Z)=\bigoplus_{0\le i<a,\,0\le j<b,\,0\le k<c}\mathbb Z[z_{i,j,k}].
\]
Here \(z_{i,j,k}\) is the oriented fundamental cycle of the induced scale-two Rips subcomplex on the eight vertices of the unit cube with lower corner \((i,j,k)\). Its homotopy type is \(S^3\), the boundary of a four-dimensional cross-polytope. The displayed homology decomposition is an **integral basis**, not just a rank count. The unit-cube generators are compatible with inclusions of boxes.

For the infinite lattice the same generators give
\[
\widetilde H_3\bigl(\operatorname{VR}_{\le2}(\mathbb Z^3);\mathbb Z\bigr)
=\bigoplus_{u\in\mathbb Z^3}\mathbb Z[z_u].
\]
The lattice isometry group \(\mathbb Z^3\rtimes((C_2)^3\rtimes S_3)\) acts by signed permutations of the unit-cube basis: translations simply permute the generators, each coordinate inversion has sign \(+1\), and a permutation of the three coordinate axes has sign equal to its parity. Thus translations act by their integral regular representation, extended by the coordinate-permutation sign character.

## Assumptions and scope
The complex is the **flag complex** on all lattice points of the box whose pairwise Manhattan distances are at most two; the metric is inherited from \(\mathbb Z^3\), not a periodic metric. The dimensions \(a,b,c\) count unit intervals along each coordinate, not numbers of vertices. All claims use ordinary integral homology, and all inclusions refer to coordinate-aligned box inclusions. In the infinite case homology means finite-support simplicial chains.

## Proof
**1. Homology concentration by retraction.** Put \(M=\max\{3,a,b,c\}\). The coordinatewise clamp \(p\mapsto(\min(p_1,a),\min(p_2,b),\min(p_3,c))\) from \(\{0,\ldots,M\}^3\) to \(B_{a,b,c}\) is one-Lipschitz for Manhattan distance, hence induces a simplicial retraction of inclusive scale-two Rips complexes. Theorem 4.13 of Gupta–Sarkar–Shukla (2025) proves that the source, for \(M\ge3\), is homotopy equivalent to a finite wedge of three-spheres, although its number of summands is left as an unspecified \(\nu_M\) with a lower bound. Retracts induce injections on all integral homology. Consequently \(\widetilde H_i(K_{a,b,c};\mathbb Z)=0\) for \(i\ne3\), and \(H_3\) is torsion-free.

**2. Exact Euler characteristic by a finite local identity.** Every nonempty simplex has a unique coordinatewise minimum \(u\). Since the pairwise Manhattan diameter is at most two, each vertex \(v\) of the simplex satisfies \(0\le v_i-u_i\le2\). Put \(d_i=\min\{2,a_i-u_i\}\), where \((a_1,a_2,a_3)=(a,b,c)\). Define
\[
w(d_1,d_2,d_3)=\sum_{\substack{\varnothing\ne\sigma\subseteq\prod_{i=1}^3\{0,\ldots,d_i\}\\
\operatorname{diam}_{d_1}(\sigma)\le2,\;\min\sigma=(0,0,0)}}(-1)^{|\sigma|-1}.
\]
The finite **twenty-seven-case identity** is
\[
w(d)=\begin{cases}1,&d=(0,0,0),\\-1,&d_1,d_2,d_3\ge1,\\0,&\text{otherwise},\end{cases}
\qquad d_i\in\{0,1,2\}.
\]
For clarity, each summand is enumerated exactly by the finite recurrence: list all vertices of the \(27\)-point-or-smaller local box, recursively enumerate subsets in increasing vertex order, append a vertex only if its distance from all earlier vertices is at most two, and retain precisely those cliques with all three coordinatewise minima zero. The included executable `verify.py` performs this complete local enumeration, checks all \(27\) identities, and independently enumerates full complexes for six nontrivial boxes. This is a finite exact computation, not a sampled experiment. Every original simplex occurs at exactly one coordinatewise minimum, hence
\[
\chi(K_{a,b,c})=\sum_{u\in B_{a,b,c}}w\bigl(\min(2,a-u_1),\min(2,b-u_2),\min(2,c-u_3)\bigr)=1-abc.
\]
There is one maximal-corner contribution \(+1\), and \(abc\) lower corners with room for a positive step in all three directions, each contributing \(-1\). As the connected complex has homology concentrated in degree three,
\[\operatorname{rank}H_3(K_{a,b,c};\mathbb Z)=abc.\]

**3. Canonical primitive generators.** For a unit cube \(u+\{0,1\}^3\), the scale-two Rips complex contains every possible edge except the four antipodal distance-three pairs. It is the join of four copies of \(S^0\), hence \(S^3\). Orient its fundamental cycle as the product of the four ordered vertex-pair differences. Translate the even-parity tetrahedron
\[
T_u=u+\{(0,0,0),(0,1,1),(1,0,1),(1,1,0)\}.
\]
It is a maximal simplex not only in its unit cube but also in the entire lattice Rips complex. Indeed, for any point \(x\in\mathbb Z^3\), the sum of its Manhattan distances to those four tetrahedron vertices is
\[
2\sum_{i=1}^3\bigl(|x_i-u_i|+|x_i-u_i-1|\bigr).
\]
This sum is at least \(6\), and a point outside the unit cube contributes at least \(10\), violating the four simultaneous bounds of two (whose total would be at most eight). Within the cube, each odd-parity vertex lies at distance three from one even vertex. Therefore a point within two of all tetrahedron vertices must be one of them. Thus no four-simplex contains \(T_u\), so evaluating the coefficient of \(T_u\) on oriented three-cycles kills boundaries. The coefficient of \(T_u\) in \(z_u\) is \(\pm1\), while it is zero in \(z_v\) for every other unit cube \(v\ne u\). These coefficient functionals certify that all \(abc\) classes are primitive and independent. Since the free rank is exactly \(abc\), they are a basis.

**4. Homotopy.** Every length-two edge is homotopic through a triangular face to two unit-step edges. Every lattice grid loop in a rectangular box contracts by adjacent elementary-square moves; the boundary of each unit square is filled by two scale-two Rips triangles. Hence \(\pi_1(K_{a,b,c})=0\). The homology concentration and simple connectivity imply two-connectivity by the Hurewicz theorem. Representatives of the displayed integral basis define a map \(\bigvee^{abc}S^3\to K_{a,b,c}\) inducing an isomorphism on all integral homology groups. The homological Whitehead theorem for simply connected CW complexes makes this a homotopy equivalence.

**5. Infinite lattice and symmetry.** Every finite simplicial chain in \(\operatorname{VR}_{\le2}(\mathbb Z^3)\) lies in a finite box, and the box generators are preserved under inclusions, so the filtered union has precisely the direct-sum basis indexed by all unit cubes. A lattice translation moves each local fundamental cycle to the corresponding translated cube. An axis permutation acts on the oriented join of four antipodal zero-spheres by the parity sign of that permutation, while a reflection in a coordinate axis acts with positive sign. This last sign statement follows by applying the induced vertex permutations to the \(16\) oriented tetrahedra of the cross-polytope boundary; the included verifier checks all \(48\) signed coordinate permutations. The signs are constant for all cubes, establishing the asserted integral module action.

## Verification
Run `python3 verify.py` in the extracted directory. It uses the Python standard library only. `verification_output.txt` is the output from a clean executable run. The checker exhausts all \(27\) local Euler weights, verifies the Euler formula on six independently enumerated box complexes, checks the oriented \(16\)-tetrahedron cycle and its zero boundary, compares its action under every one of the \(48\) signed axis permutations, and checks parity-tetrahedron maximality directly in dimensions three through six. The higher-dimensional maximality statement is also established algebraically above; no finite enumeration is used in place of a general proof. The homology concentration input is the explicitly cited published preprint theorem, not an inferred computational claim.

## Relationship to prior work
Gupta, Sarkar and Shukla (2025, Theorem 4.13) proved that inclusive scale-two Rips complexes of finite, equal-sided integer-lattice cubes are wedges of three-spheres but left the number of summands as \(\nu_M\) with a lower bound. Their Theorem 4.15 proves a countably infinite three-sphere wedge in the full integer lattice without an integral translation-equivariant basis. The present result supplies the exact \(abc\) rank for **all finite rectangular three-dimensional boxes**, an explicit primitive basis compatible with inclusions, and the full integral geometric symmetry action on that basis. It does not claim the known general wedge concentration or the known local cross-polytope observation as new. Adamaszek and Adams (2021) computed the sphere multiplicities for **binary hypercubes** with Hamming distance, which do not encompass rectangular lattice boxes of arbitrary side length.

## Limitations
The statement concerns three-dimensional coordinate-aligned boxes at exactly scale two and the resulting infinite three-dimensional lattice. It does not imply a similar \(abc\) formula for higher-dimensional lattice boxes, for other Rips scales, for periodic tori, or for Euclidean rather than Manhattan distance. The integral-module conclusion describes homology, not a group-equivariant wedge decomposition of spaces. The finite identity is given with executable exhaustive verification so its computation can be independently replayed.

## References
1. R. K. Gupta, S. Sarkar and S. Shukla, *On the Vietoris-Rips Complexes of Integer Lattices*, arXiv:2511.04238v1 (first public version 2025-11-06), especially Theorems 4.13–4.15 and Lemma 4.1. https://arxiv.org/abs/2511.04238
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first version 2021-03-01, especially Theorem 1. https://arxiv.org/abs/2103.01040
