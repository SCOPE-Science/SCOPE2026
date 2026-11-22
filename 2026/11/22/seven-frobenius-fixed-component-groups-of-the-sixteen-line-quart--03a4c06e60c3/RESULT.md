# Seven Frobenius-fixed component groups of the sixteen-line quartic del Pezzo boundary

## Finding

Let \(k=\mathbb F_q\) be a finite field. Suppose \(Z\subset\mathbb P^2_k\) is a geometrically reduced degree-five étale subscheme whose five geometric points have no three collinear. Put \(S=\operatorname{Bl}_Z\mathbb P^2_k\), a smooth degree-four del Pezzo surface, and let \(D\) be the reduced union of all sixteen geometric \((-1)\)-curves. The divisor \(D\) is defined over \(k\).

The resulting connected nodal curve has sixteen geometric rational components, forty geometric ordinary nodes, and arithmetic genus \(25\). Let \(\Gamma\) be its geometric dual graph and \(K(\Gamma)\) its integral graph critical group. The Frobenius permutation of the five exceptional base points has cycle type \(\lambda\vdash5\). With \(C_m=\mathbb Z/m\mathbb Z\), the complete seven-case classification of **Frobenius-fixed critical groups** is:

| \(\lambda\) | \(K(\Gamma)^{\operatorname{Frob}_q}\) |
|---|---|
| \((1,1,1,1,1)\) | \(C_4^4\oplus C_8\oplus C_{32}^4\) |
| \((2,1,1,1)\) | \(C_4^2\oplus C_8\oplus C_{32}^3\) |
| \((2,2,1)\) | \(C_4^2\oplus C_8\oplus C_{32}^2\) |
| \((3,1,1)\) | \(C_8\oplus C_{32}^2\) |
| \((3,2)\) | \(C_8\oplus C_{32}\) |
| \((4,1)\) | \(C_2\oplus C_4\oplus C_{32}\) |
| \((5)\) | \(C_8\) |

If \(D\) is the special fiber of a proper regular semistable one-parameter smoothing over \(k[[t]]\), with geometric node thickness one, and \(J\) is the Jacobian of its smooth generic fiber, these groups are precisely the finite abelian groups of \(k\)-rational points of the Néron component group scheme \(\Phi_J\):
\[
\Phi_J(k)\simeq K(\Gamma)^{\operatorname{Frob}_q}.
\]
This applies to any such smoothing, without assuming that the individual components of the special fiber are split over \(k\).

In particular, cycle types \((3,2)\) and \((4,1)\) both yield \(256\) rational components, but their groups are **not isomorphic**: \(C_8\oplus C_{32}\) versus \(C_2\oplus C_4\oplus C_{32}\). The seven orders are, in the table order, \(2^{31},2^{22},2^{17},2^{13},2^8,2^8,2^3\).

## Assumptions and scope

The five points are geometrically distinct, étale over \(k\), and no three lie on a geometric line. The seven rows classify actions arising from permuting **these five blowup points**; they do not exhaust all \(W(D_5)\)-twists of a general degree-four del Pezzo surface. No assumption is made that every cycle type is realized over every cardinality \(q\). The Néron interpretation requires a proper regular semistable smoothing with unit node thicknesses, not just an arbitrary deformation or a nonregular model. The purely geometric critical-group and Frobenius-fixed calculations do not require a smoothing.

## Proof

**1. Geometry and graph.** Over \(\bar k\), write \(H\) for the pullback of a line and \(E_i\) for the five exceptional divisors, numbered \(i=0,\ldots,4\). The sixteen negative curves are
\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (0\leq i<j\leq4),\qquad Q=2H-\sum_{i=0}^4E_i.
\]
The five-point conic \(Q\) is smooth: a reducible conic through five points would put three on one of its lines. Use \(H^2=1\), \(E_i^2=-1\), \(H E_i=0\) and \(E_i E_j=0\) for distinct indices. Intersections between distinct negative curves are exactly: \(E_i\) meets \(Q\) and the four \(L_{ij}\) containing \(i\); distinct \(L_{ij}\) and \(L_{ab}\) meet if and only if their index pairs are disjoint. All other pairs are disjoint. No three curves meet at one point: a three-clique is impossible in this graph, since two lines through a fixed blown-up point cannot meet each other, and three pairwise disjoint two-element subsets would need six base labels.

Every vertex has degree five, so \(\Gamma\) has sixteen vertices and forty edges. It is connected since \(Q\) meets every \(E_i\), and every \(L_{ij}\) meets two \(E\)'s. Therefore \(p_a(D)=40-16+1=25\), also confirmed by \(D\sim-4K_S\) and adjunction \((D^2+D K_S)/2+1=25\). All components are rational and meet in five ordinary nodes each, so \(D\) is stable.

**2. Frobenius-equivariant critical group.** The geometric Laplacian \(L=5I-A\) acts on \(\mathbb Z^{16}\); put
\[
K(\Gamma)=\ker\bigl(\deg:\operatorname{coker}L\longrightarrow\mathbb Z\bigr).
\]
The geometric conic \(Q\) is the unique conic through all five blowup points and is therefore Frobenius-fixed. Consequently \([Q]\in\operatorname{coker}L\) gives a Frobenius-equivariant splitting of the degree map, and
\[
\operatorname{coker}L\simeq K(\Gamma)\oplus\mathbb Z
\]
as modules for Frobenius. Let \(\sigma\) be the permutation induced on all sixteen vertices. The canonical perfect symmetric graph monodromy pairing, defined from \(L\) and hence invariant under graph automorphisms, identifies \(K(\Gamma)^\sigma\) with the character dual of the coinvariants \(K(\Gamma)_\sigma\). Thus the fixed and coinvariant groups have the same abstract invariant factors.

**3. Orbit reduction over integers.** Let \(O_1,\ldots,O_r\) be the vertex orbits under \(\sigma\), with \(O_r=\{Q\}\), and choose representatives \(y_j\in O_j\). The full orbit coinvariant Laplacian is the integer matrix
\[
 B_{ij}=\sum_{x\in O_i}L_{x,y_j}.
\]
This is generally **not** an unweighted quotient-graph Laplacian. Each column of \(B\) sums to zero. Moreover, \(B(|O_1|,\ldots,|O_r|)^T=0\); since \(|O_r|=1\), its last column is an integer linear combination of the first \(r-1\). After eliminating the fixed \(Q\) coordinate using the degree map, the \((r-1)\)-square matrix \(M=B_{1\leq i,j<r}\) is an integral presentation matrix for \(K(\Gamma)_\sigma\). Hence
\[
K(\Gamma)^\sigma\simeq\bigl(\operatorname{coker}M\bigr)^\vee
\]
(noncanonically as abstract finite abelian groups). This reduction is exact over \(\mathbb Z\) even when \(\sigma\) has even order.

**4. Seven exact Smith calculations.** Enumerate the seven conjugacy classes of \(S_5\) via their partitions. Apply each permutation to \(E_i,L_{ij},Q\), form its vertex orbits and the matrix \(M\) above. The following table records every nonunit Smith invariant and the absolute determinant; no prime other than two occurs.

| Cycle type | Nonunit Smith factors of \(M\) | \(|\det M|\) |
|---|---|---|
| \((1,1,1,1,1)\) | \(4,4,4,4,8,32,32,32,32\) | \(2^{31}\) |
| \((2,1,1,1)\) | \(4,4,8,32,32,32\) | \(2^{22}\) |
| \((2,2,1)\) | \(4,4,8,32,32\) | \(2^{17}\) |
| \((3,1,1)\) | \(8,32,32\) | \(2^{13}\) |
| \((3,2)\) | \(8,32\) | \(2^8\) |
| \((4,1)\) | \(2,4,32\) | \(2^8\) |
| \((5)\) | \(8\) | \(2^3\) |

For illustration, the five-cycle has three nontrivial vertex-orbit representatives, and the exact rooted matrix is
\[
M_{(5)}=\begin{pmatrix}5&-2&-2\\-2&3&-1\\-2&-1&3\end{pmatrix}.
\]
Its Smith form is \(\operatorname{diag}(1,1,8)\). For the remaining six cases the accompanying exact verifier reconstructs \(M\) from the curve intersection rules and checks it in two arithmetically independent ways: fraction-free determinant evaluation over \(\mathbb Z\), and valuation-minimal pivot elimination over \(\mathbb Z/256\mathbb Z\). Every pivot has valuation at most five; the determinant is the product of its displayed two-power factors. The modular pivots determine the full two-primary Smith forms, while exact determinant powers of two exclude all odd-primary factors. Thus these finite checks establish the integral Smith forms in the table, not extrapolations from samples.

**5. Component-group interpretation.** For a regular semistable nodal curve with geometric multiplicities and node thicknesses all one, the geometric component group of the Néron model of its Jacobian is the critical group of the geometric dual graph, compatibly with the residue-field Galois action. The finite étale component group scheme has \(k\)-rational points the Frobenius invariants. Applying steps 1–4 gives the stated seven groups for any smoothing in scope.

## Verification

Run `python3 verify.py` with Python 3.8 or later. The program has no third-party dependencies. It reconstructs the sixteen classes and forty edges; checks Laplacian row sums, orbit partitions, integral orbit-matrix row and column relations, each nonzero determinant, and each two-adic Smith sequence using only exact arithmetic. It requires every output group to match the seven values above and terminates with `QUARTIC_DEL_PEZZO_SEVEN_FROBENIUS_COMPONENT_GROUPS_OK`. A separate exact integer Smith normal form calculation was also compared with these outputs for all seven matrices. Neither the verifier nor that comparison substitutes for the geometric graph-identification and descent arguments in the proof.

## Relationship to prior work

The description of degree-four del Pezzo surfaces and their sixteen lines is classical; Hassett–Kresch–Tschinkel discuss the moduli and the five-point blowup and its \(D_5\) symmetry. The ordinary (untwisted) critical group of the Clebsch graph is already tabulated by Tamimi as \(C_4^4\oplus C_8\oplus C_{32}^4\); **the first row here is a prior-work check, not claimed as a new computation**. Shokrieh's general graph monodromy pairing supplies the equivariant duality mechanism, while standard semistable Néron theory supplies the component-group interpretation. The contribution isolated here is the **simultaneous seven-cycle-type Frobenius-fixed integral decomposition** for this natural geometric boundary, particularly the different isomorphism types at equal order \(256\). A related public computation of the five-cycle connected Picard torus concerns a distinct invariant: it does not itself determine Frobenius invariants on the finite Néron component group.

## Limitations

The claims concern only the seven permutation types arising from a chosen five-point blowup, not all Weyl-group arithmetic forms. The groups describe the degree-four del Pezzo boundary or a smoothing with that special fiber and all node thicknesses one; other thicknesses can change the component group. The seven integral calculations and structural proof are self-contained, but historical priority is qualified by the possibility of an unindexed older equivariant critical-group computation. No independent mathematical review is asserted.

## References

1. F. Shokrieh, *The Monodromy Pairing and Discrete Logarithm on the Jacobian of Finite Graphs*, arXiv:0907.4764, originally public July 27, 2009, especially Theorem 3.4. https://arxiv.org/abs/0907.4764
2. B. Hassett, A. Kresch and Y. Tschinkel, *On the Moduli of Degree 4 Del Pezzo Surfaces*, arXiv:1312.6734, originally public December 24, 2013, especially Sections 2 and 4. https://arxiv.org/abs/1312.6734
3. T. Suzuki, *Grothendieck's Pairing on Néron Component Groups: Galois Descent from the Semistable Case*, arXiv:1410.3046, originally public October 12, 2014. https://arxiv.org/abs/1410.3046
4. B. Tamimi, *The Sandpile & Smith Groups of Certain Classes of Graphs*, doctoral thesis, University of Essex (2021), repository deposit August 9, 2022, Table 1.1. https://repository.essex.ac.uk/33230/
