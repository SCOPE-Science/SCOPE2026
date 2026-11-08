# Exact six-leader controllability census and symmetry orbits of the Heawood incidence graph

## Finding

For the unit-edge point–line incidence graph of **every existing finite projective plane** of order \(q\ge2\), the minimum number of independently controlled vertex coordinates for Laplacian consensus dynamics is exactly \(q^2+q\). Every minimum-size leader set is characterized by a nonsingular square point–line incidence matrix specified below.

For the canonical order-two projective plane (the fourteen-vertex **Heawood graph**), exactly \(1890\) of the \(\binom{14}{6}=3003\) six-vertex leader sets are controllable. They form exactly \(14\) orbits under the full automorphism group of order \(336\). Their orbit sizes are \(14,28,28,56,84\), eight copies of \(168\), and \(336\).

The number of controllable sets with \(k=0,1,\ldots,6\) selected point vertices (and \(6-k\) selected line vertices) is respectively \(7,84,420,868,420,84,7\). These counts refer to distinct subsets of the fourteen explicitly labeled vertices, not to abstract graph isomorphism types.

## Assumptions and scope

Let \(\mathcal P\) be any finite projective plane of order \(q\ge2\). Write \(v=q^2+q+1\), and let \(N\in\{0,1\}^{v\times v}\) be its point-by-line incidence matrix, with \(N_{ij}=1\) exactly when point \(i\) lies on line \(j\). Every line and every point has \(q+1\) incidences. Every two distinct points lie on exactly one common line. Thus \(NN^{\mathsf T}=qI_v+J_v\) and \(N\mathbf1=(q+1)\mathbf1\).

The graph \(H\) has \(2v\) vertices, divided into \(v\) point vertices and \(v\) line vertices; each incident point–line pair is joined by an undirected edge of conductance one. Its Laplacian is
\[
L=\begin{pmatrix}(q+1)I_v&-N\\-N^{\mathsf T}&(q+1)I_v\end{pmatrix}.
\]
Given a subset \(S\) of the \(2v\) vertices, \(E_S\) denotes the column-selection matrix consisting of independent standard coordinate columns for exactly those vertices. The controlled system is \(\dot z=-Lz+E_Su\) over real numbers, with no actuator-gain, robustness, or energy constraints.

For \(|S|=v-1\), define the \(v\times v\) matrix \(R_S\): its first row is \(\mathbf1^{\mathsf T}\); for each selected point \(i\), append the standard coordinate row \(e_i^{\mathsf T}\); for each selected line \(j\), append the row \(N_{\cdot j}^{\mathsf T}\). Row ordering does not affect nonsingularity.

## Proof

**1. Spectral decomposition.** The projective-plane identity \(NN^{\mathsf T}=qI+J\) has eigenvalue \((q+1)^2\) on \(\mathbf1\) and eigenvalue \(q\) on its \((v-1)\)-dimensional orthogonal complement \(W=\mathbf1^\perp\). Therefore \(N\) is invertible and the real Laplacian has precisely four distinct eigenvalues,
\[
0,\quad 2(q+1),\quad q+1-\sqrt q,\quad q+1+\sqrt q,
\]
with respective multiplicities \(1,1,v-1,v-1\). For \(x\in W\), an eigenvector for \(q+1-\sqrt q\) is \((x,N^{\mathsf T}x/\sqrt q)\), and for \(q+1+\sqrt q\) it is \((x,-N^{\mathsf T}x/\sqrt q)\). The remaining eigendirections are \((\mathbf1,\mathbf1)\) and \((\mathbf1,-\mathbf1)\).

**2. Minimum size.** The PBH condition for the real symmetric pair \((-L,E_S)\) is that no nonzero eigenvector of \(L\) vanish on every coordinate in \(S\). An eigenspace of dimension \(v-1\) requires at least \(v-1\) selected coordinate functionals. Conversely, selecting any \(v-1\) point vertices succeeds: a vector \(x\in W\) vanishing on those vertices has support on at most one point, hence has coordinate sum zero only when \(x=0\). Both one-dimensional eigendirections have nonzero coordinates on all vertices. Consequently the minimum is \(v-1=q^2+q\).

**3. All minimum placements.** For either eigenspace of multiplicity \(v-1\), the vanishing condition on the selected vertices is exactly \(x\in W\) together with \(x_i=0\) for each selected point and \(N_{\cdot j}^{\mathsf T}x=0\) for each selected line. The two signs and the nonzero factor \(\sqrt q\) have no effect on this kernel. Thus the two PBH requirements are simultaneously equivalent to \(\ker R_S=\{0\}\). The one-dimensional eigenspaces automatically pass because \(S\) is nonempty. Since \(R_S\) is square, controllability is equivalent to \(\det R_S\ne0\). This is an exact necessary-and-sufficient criterion for all minimum-size placements in every existing finite projective plane.

**4. The order-two certificate.** Label both the seven points and seven line normals by nonzero three-bit vectors \(1,\ldots,7\), and put \(N_{x,a}=1\) exactly when the ordinary bitwise dot product \(x\cdot a\) is even. This is a projective plane of order two. Label point vertices \(0,\ldots,6\) and line vertices \(7,\ldots,13\), each corresponding to the three-bit labels in increasing order. Enumerate all \(\binom{14}{6}=3003\) subsets \(S\), form their \(7\times7\) matrices \(R_S\), and test exact rank over the prime field \(\mathbb F_{101}\).

The mod-\(101\) test is **equivalent to exact integer nonsingularity**, not a probabilistic proxy: Hadamard's inequality bounds \(|\det R_S|\le\sqrt7(\sqrt3)^6=27\sqrt7<101\), since its first row has norm \(\sqrt7\), and each of the other six rows has norm at most \(\sqrt3\). An integer in this strict interval is zero if and only if its reduction modulo \(101\) is zero. The standalone verifier exhaustively obtains the counts stated in the finding.

**5. Complete symmetry reduction.** The point-side automorphism group acts by all invertible linear maps on \(\mathbb F_2^3\), of which there are \(7\cdot6\cdot4=168\). The corresponding line normal is carried contragrediently, preserving the incidence pairing. There can be no more point-side automorphisms: an ordered noncollinear triple (the three images of a frame) determines all seven points by their line intersections. Because the incidence matrix is symmetric in this model, exchanging point and line vertices is an additional automorphism. Every automorphism of a connected bipartite graph either preserves or swaps its sides; hence the full group has order \(336\). The verifier generates all its elements, computes their orbits on every six-subset, and checks that controllability is constant on each orbit. It finds exactly the following fourteen controllable orbits. Each representative is a zero-based set of vertex labels as defined above.

| Orbit size | Representative |
|---:|:---|
| 14 | `0,1,2,3,4,5` |
| 28 | `0,1,2,7,8,9` |
| 28 | `0,1,3,7,8,10` |
| 56 | `0,1,2,7,8,13` |
| 84 | `0,1,3,9,11,13` |
| 168 | `0,1,2,3,4,7` |
| 168 | `0,1,2,3,7,8` |
| 168 | `0,1,2,3,11,12` |
| 168 | `0,1,3,6,7,8` |
| 168 | `0,1,3,7,8,11` |
| 168 | `0,1,3,7,8,13` |
| 168 | `0,1,3,7,9,12` |
| 168 | `0,1,3,7,9,13` |
| 336 | `0,1,2,3,7,12` |

Their orbit sizes sum to \(1890\). A second independent calculation evaluates, for every one of the \(3003\) subsets, the exact rank over \(\mathbb F_{1009}\) of the full \(14\times24\) controllability block matrix \([E_S,LE_S,L^2E_S,L^3E_S]\), and agrees in all cases with the incidence criterion. Four blocks suffice in characteristic zero because \(L\) has four distinct eigenvalues. This finite-field cross-check is supplementary; the characteristic-zero classification rests on the spectral proof and the determinant bound.

## Verification

Run `python3 verify.py` with Python 3.8 or later; the program uses only the standard library. It constructs the incidence matrix from binary dot products, checks the projective-plane identity, exhaustively tests the \(3003\) leader sets modulo \(101\), constructs all \(336\) graph automorphisms, classifies the orbit sizes, and independently compares every case to a full-Krylov controllability rank computation modulo \(1009\). The program asserts the exact \(1890\) count, the seven selected-point profile, and the fourteen-orbit profile; it raises an exception if any check fails.

## Relationship to prior work

Yuan, Zhao, Di, Wang and Lai (2013) establish the general PBH and maximum-eigenvalue-multiplicity controllability principle. The general lower bound is therefore prior work. The present result supplies a projective-plane-specific exact coordinate-placement criterion and a complete exact census, with symmetry orbits, for the canonical Heawood graph; those numerical and structural conclusions do not follow from the general multiplicity number alone. Monshizadeh, Zhang and Camlibel (2014) analyze zero forcing and controllability over a qualitative family of matrices, not the fixed unit-conductance incidence Laplacian. Dai (2022) studies minimum leader selection in other bipartite families, notably trees and deterministic scale-free networks. An affine-plane incidence-graph result uses a different graph with different eigenstructure; it does not imply the projective-plane count. No assertion of literature-wide uniqueness is made.

## Limitations

The classification assumes one independent standard-coordinate actuator for each selected vertex, exactly uniform unit conductances, and an existing projective plane. It does not assert that projective planes exist at all orders, and it does not optimize control energy, robustness, actuator weights or arbitrary input matrices. The explicit number \(1890\) and fourteen-orbit count concern only the order-two Heawood graph; no general closed formula for the number of placements at larger orders is asserted. Literature searching cannot establish global publication priority; close studies outside the inspected sources may exist.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4, 2447 (first published 12 September 2013), https://doi.org/10.1038/ncomms3447 ; open manuscript https://arxiv.org/abs/1310.5806 .
2. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868 (19 March 2014), https://arxiv.org/abs/1403.4868 .
3. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications (first published 29 October 2022), https://doi.org/10.1049/cth2.12385 .
