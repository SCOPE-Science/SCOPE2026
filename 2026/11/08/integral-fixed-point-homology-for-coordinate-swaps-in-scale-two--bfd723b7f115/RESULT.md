# Integral fixed-point homology for coordinate swaps in scale-two hypercube Rips complexes

## Finding
For an integer \(n\ge 2\), let \(Q_n=\{0,1\}^{n}\) carry Hamming distance, and let \(X_n=\operatorname{VR}(Q_n;2)\) be the inclusive Vietoris–Rips simplicial complex. Let \(\tau\) exchange the first two binary coordinates and put \(F_n=|X_n|^{\langle\tau\rangle}\), the **geometric** fixed-point space of its realization, not merely the subcomplex on fixed vertices. For \(m\ge 0\) set
\[
c_m=\begin{cases}
0,&m\le2,\\
\displaystyle\sum_{i=1}^{m-1}\sum_{j=0}^{i-1}(j+1)(2^{m-2}-2^{i-1}),&m\ge3.
\end{cases}
\]
Then \(F_2\) is contractible. For **every** \(n\ge3\), the space \(F_n\) is connected and simply connected, and its integral reduced homology is completely determined by
\[
\boxed{\widetilde H_q(F_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\,(n-3)2^{n-2}+1},&q=2,\\
\mathbb Z^{\,2c_{n-2}},&q=3,\\
0,&q\ne2,3.
\end{cases}}
\]
In particular there is no integral homology torsion, and for \(n\ge5\) both displayed ranks are nonzero. This is an integral graded-homology result, **not** a claim of a wedge decomposition of \(F_n\).

## Assumptions and scope
A simplex of \(X_n\) is a finite set of binary strings all pairwise at Hamming distance at most \(2\). A geometric fixed point is a point in \(|X_n|\) invariant under the piecewise-linear action of \(\tau\), and can lie at the barycenter of a two-element vertex orbit. Reduced homology is with integral coefficients, with unreduced degree-zero rank one in every nonempty connected case. The claim concerns only a coordinate-transposition involution at inclusive scale two. Coordinates are ordered so that the transposition exchanges the first two; every transposition is conjugate to this one.

The integer \(c_m\) is the known multiplicity of three-spheres in \(\operatorname{VR}(Q_m;2)\), by Adamaszek–Adams [1]. For \(m=0,1,2\), this Rips complex is contractible, and the convention \(c_m=0\) agrees with its positive-degree reduced homology.

## Proof
**1. The orbit-face model.** If a finite group acts simplicially on a complex, a point of a simplex is invariant precisely when its barycentric coefficients are constant on the vertex orbits contained in the simplex. Thus its fixed-point space is canonically piecewise-linearly homeomorphic to the complex whose vertices are orbits \(\mathcal O\) that are themselves simplices and whose faces are collections of orbits whose unions are simplices. This holds without assuming that every vertex is individually fixed. In the present case each orbit has size one or two, and the underlying Rips complex is flag, so the orbit-face complex is determined by pairwise orbit compatibility.

Put \(m=n-2\) and \(V=\{0,1\}^m\). For every \(z\in V\), its three vertex orbits are
\[
A_z=\{(0,0,z)\},\qquad B_z=\{(1,1,z)\},\qquad
C_z=\{(0,1,z),(1,0,z)\}.
\]
Write \(d(z,w)\) for Hamming distance on \(V\). Direct checking of the maximum distance between representatives of two orbits gives the complete compatibility table:
\[
\begin{array}{c|c}
\text{orbit pair}&\text{compatible exactly when}\\\hline
A_z,A_w\text{ or }B_z,B_w&d(z,w)\le2\\
A_z,B_w&z=w\\
A_z,C_w\text{ or }B_z,C_w&d(z,w)\le1\\
C_z,C_w\ (z\ne w)&\text{never}.
\end{array}
\]
Each \(C_z\) is itself an allowed orbit, since its two elements have distance \(2\). These assertions give an explicit combinatorial model \(K\cong_{\rm PL}F_n\).

**2. The two-layer base.** Let \(K_0\subseteq K\) be the induced subcomplex on all \(A_z,B_z\), and set \(N=2^m\). It consists of two copies \(U_m^A,U_m^B\) of \(U_m=\operatorname{VR}(Q_m;2)\), connected by exactly \(N\) cross edges \(A_zB_z\), with no higher-dimensional mixed faces. When \(m\ge1\), both copies are connected and simply connected: they are contractible for \(m\le2\), and by [1] each is homotopy equivalent to \(\bigvee^{c_m}S^3\) when \(m\ge3\). A maximal-tree contraction between these simply connected pieces gives
\[
\pi_1(K_0)\cong\text{free group on }N-1\text{ generators},\quad
H_1(K_0;\mathbb Z)\cong\mathbb Z^{N-1},
\quad H_2(K_0;\mathbb Z)=0,\quad H_3(K_0;\mathbb Z)\cong\mathbb Z^{2c_m}.
\]
All other reduced integral homology groups vanish.

**3. The links of the orbit vertices.** No simplex contains two different \(C\)-vertices. Consequently \(K\) is obtained from \(K_0\) by coning off the links \(L_z=\operatorname{lk}_K(C_z)\) for all \(z\in V\), and the interiors of these cones are pairwise disjoint. Let \(D_z=\{w\in V:d(z,w)\le1\}\); it contains precisely \(m+1\) points. The link \(L_z\) consists of a full simplex on \(\{A_w:w\in D_z\}\), another full simplex on \(\{B_w:w\in D_z\}\), and precisely \(m+1\) cross edges \(A_wB_w\), one for each \(w\in D_z\). There are no mixed triangles. Therefore, for \(m\ge1\), collapsing the two full simplices separately gives the homotopy equivalence
\[
L_z\simeq\bigvee^{m}S^1,
\quad H_1(L_z;\mathbb Z)\cong\mathbb Z^m,\quad
\widetilde H_j(L_z;\mathbb Z)=0\quad(j\ne1).
\]
By excision for the disjoint cone interiors (or the relative cellular-chain splitting),
\[
H_i(K,K_0;\mathbb Z)\cong\bigoplus_{z\in V}\widetilde H_{i-1}(L_z;\mathbb Z).
\]
Thus the only nonzero relative group is \(H_2(K,K_0;\mathbb Z)\cong\mathbb Z^{mN}\).

**4. The integral connecting map.** Choose paths within each simply connected layer of \(K_0\). An oriented loop in \(L_z\) formed by the two cross edges \(A_zB_z\) and \(A_wB_w\), with \(d(z,w)=1\), represents the difference between their corresponding fundamental-group generators in the graph-of-spaces model. Under the connecting map
\[
\partial:H_2(K,K_0;\mathbb Z)\longrightarrow H_1(K_0;\mathbb Z),
\]
this class maps to the difference of those cross-edge classes. The \(m\)-dimensional cube graph on \(V\) is connected, so differences along its edges generate the entire free group \(H_1(K_0;\mathbb Z)\) of rank \(N-1\). Hence \(\partial\) is surjective over \(\mathbb Z\), not merely over a field. Its kernel is a free abelian group of rank \(mN-(N-1)=(m-1)2^m+1\). The long exact sequence of the pair gives
\[
H_1(K;\mathbb Z)=0,\quad H_2(K;\mathbb Z)\cong\ker\partial,\quad
H_3(K;\mathbb Z)\cong H_3(K_0;\mathbb Z),
\]
with all higher homology zero. The latter isomorphism holds because the relative groups in degrees three and four vanish. For fundamental groups, coning the \(L_z\) kills the normal closures of their image loops; adjacent cross-edge differences normally generate the free group \(\pi_1(K_0)\), again by connectedness of the cube graph. Van Kampen therefore proves \(\pi_1(K)=1\).

**5. The boundary case.** For \(m=0\) (equivalently \(n=2\)), there is one vertex of each type \(A,B,C\). The three orbits together form one simplex in the orbit complex, so \(F_2\cong_{\rm PL}\Delta^2\) is contractible. Substituting \(m=n-2\) in the formulas in Step 4 proves the full claim. \(\square\)

## Verification
The standalone source `verify.py` builds orbit sets directly from coordinate swaps, tests pairwise distances across **all** representatives without using the structural compatibility table, constructs every clique of the resulting orbit-compatibility graph, and computes reduced simplicial homology over \(\mathbb F_2\) by exact bitwise Gaussian elimination. It separately checks the predicted three-type compatibility table and compares the resulting Betti numbers with both integer rank formulas. It exhausts all simplices for \(n=2,3,4,5,6,7\): respectively \(8,27,107,449,1889,7841\) faces counting the empty face. All six cases agree, with reduced Betti pairs \((\beta_2,\beta_3)\) equal to \((0,0),(1,0),(5,0),(17,2),(49,18),(129,98)\). The output ends `ALL_VERIFY_OK cases=6 face_sets=10321`.

These finite field computations corroborate the orbit structure and Betti ranks, but do **not** establish the integral absence of torsion, simple connectivity, or the result for all \(n\). Those conclusions follow instead from the explicit cone-link decomposition, the integral connecting-map generators, and van Kampen in the proof.

## Relationship to prior work
Adamaszek and Adams [1] give the nonequivariant wedge-of-three-spheres theorem and the exact multiplicity \(c_m\), which are **used**, not asserted anew. Bendersky, Elia and Grbić [2] provide connectivity bounds and cohomology constructions for ordinary hypercube Rips complexes; they do not provide this geometric fixed-point calculation. Galetto, Montaño and Wellner [3] compute the characteristic-zero hyperoctahedral representation on the **ambient** Rips homology, and hence constrain fixed-point Euler characteristics via Lefschetz theory, but a character does not determine the integral homology in each degree, torsion, or the fundamental group of a fixed-point space. Existing calculations for hypercube Čech complexes [4] concern a different simplicial complex. Thus the new assertion is the integral fixed-point homology and simple connectivity of the **coordinate-transposition** fixed space, supported by an explicit geometric decomposition, not an ambient rank or a character restatement.

## Limitations
Only a single coordinate transposition at Rips scale exactly \(2\) is classified. Neither arbitrary coordinate-permutation subgroups nor translations composed with permutations are covered. No equivariant homotopy splitting or stronger wedge-of-spheres assertion is claimed. An equivalent result may exist in unindexed literature; this work does not represent independent mathematical certification.

## References
1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public 2021-03-01), Theorem 1 and its proof. https://arxiv.org/abs/2103.01040
2. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705v1 (first public 2026-05-01); open-access article DOI:10.1017/prm.2026.10175, sections 1–5. https://arxiv.org/abs/2605.00705
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first public 2026-06-18), sections 1 and 4–5. https://arxiv.org/abs/2606.20784
4. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (2022), for contrast with the different Čech construction. https://arxiv.org/abs/2212.05871
