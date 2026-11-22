# Seven integral Frobenius tori of the Petersen boundary on quintic del Pezzo surfaces

## Finding
Let \(k=\mathbb F_q\) be any finite field, \(X/k\) a smooth degree-five del Pezzo surface, and \(D\) the reduced union of all ten geometric exceptional \((-1)\)-curves. It is a connected stable genus-six nodal curve with ten rational-curve components over \(\bar k\) and fifteen geometric nodes. Its connected generalized Jacobian \(J_D=\operatorname{Pic}^0(D/k)\) is a six-dimensional algebraic \(k\)-torus.

The Frobenius action on the five conic-bundle labels has one of seven partitions. **The following are isomorphisms of \(k\)-tori, not merely isogenies**, and determine the complete abstract finite abelian group of \(k\)-points. In the table \(R_m=\operatorname{Res}_{\mathbb F_{q^m}/k}\mathbb G_m\), \(N_2=\operatorname{Res}^{1}_{\mathbb F_{q^2}/k}\mathbb G_m\), and \(Q_4=\operatorname{Res}_{\mathbb F_{q^2}/k}(\operatorname{Res}^{1}_{\mathbb F_{q^4}/\mathbb F_{q^2}}\mathbb G_m)\). The symbol \(C_m\) denotes a cyclic group of order \(m\).

| Frobenius partition | Integral torus \(J_D\) | Group \(J_D(k)\) |
|---|---|---|
| \(1^5\) | \(\mathbb G_m^6\) | \(C_{q-1}^{6}\) |
| \(2\,1^3\) | \(R_2^3\) | \(C_{q^2-1}^{3}\) |
| \(3\,1^2\) | \(R_3^2\) | \(C_{q^3-1}^{2}\) |
| \(2^2\,1\) | \(R_2^2\times N_2^2\) | \(C_{q^2-1}^{2}\times C_{q+1}^{2}\) |
| \(4\,1\) | \(R_4\times Q_4\) | \(C_{q^4-1}\times C_{q^2+1}\) |
| \(3\,2\) | \(R_6\) | \(C_{q^6-1}\) |
| \(5\) | \(\mathbb G_m\times R_5\) | \(C_{q-1}\times C_{q^5-1}\) |

In particular, for five-label Frobenius cycle type \((3,2)\), the entire six-dimensional generalized Jacobian has **cyclic** \(k\)-points, of order \(q^6-1\). The \((4,1)\) and \((2^2,1)\) cases contain integral norm-one factors that cannot be inferred solely from the rational Frobenius character. These seven types also give exact zeta functions of \(D\) and its open complement in \(X\), including the effect of Frobenius-swapped branches at fixed nodes, as specified below.

## Assumptions and scope
The complete exceptional divisor is used, not an arbitrarily chosen pentagon. The finite-field form \(X\) corresponds to its conjugacy class in the natural \(S_5\) action on five geometric conic bundles; all seven classes are permitted. All components of \(D\) are geometrically \(\mathbb P^1\), every geometric pair of intersecting components meets transversely in exactly one node, and the Petersen intersection graph has ten vertices and fifteen edges. No restriction on the characteristic is imposed.

## Proof
**(1) Torus character lattice.** Let \(P\) be the Petersen graph whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent iff disjoint. The normalization exact sequence for the nodal curve gives the Galois-equivariant integral isomorphism
\[
X^*(J_{D,\bar k})\simeq H_1(P,\mathbb Z)=\ker(\partial:\mathbb Z^{15}\to\mathbb Z^{10}),
\]
with the **signed edge-orientation action** induced by permutation of the five labels. The lattice has rank \(15-10+1=6\). This step uses the integral graph lattice, rather than only a rational or \(\ell\)-adic character representation.

**(2) Explicit unimodular certificates.** Order the ten two-subsets lexicographically; order the fifteen disjoint-pair edges lexicographically and orient each from the lower to the higher vertex index. Choose the spanning tree with edges (in zero-based vertex indices)

```text
(0,7), (0,8), (0,9), (1,5), (1,6), (1,9), (2,4), (2,6), (3,4).
```

Use the six omitted edges, in lexicographic order, as chords. Each oriented chord plus its return path in the tree defines an integral fundamental cycle; those six cycles form a unimodular basis of \(H_1(P,\mathbb Z)\). For the seven representative permutations, the executable certificate `verification/verify_petersen_tori.py` builds their exact \(6\times6\) integer action matrices \(A_\lambda\) and seven explicitly provided integer change-of-basis matrices \(U_\lambda\), then proves
\[
\det U_\lambda=\pm1,\qquad A_\lambda U_\lambda=U_\lambda B_\lambda.
\]
Here \(B_\lambda\) is, respectively, the direct sum of: six fixed rank-one blocks; three cyclic permutation blocks of length two; two of length three; two length-two permutation blocks and two sign blocks; a length-four permutation block and the rotation block \(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\); one length-six permutation block; or one length-five permutation block plus one fixed block. All seven equalities are checked by exact integer matrix multiplication, with unimodular determinants, not by floating-point approximation. Conjugation by a different five-label permutation transports these bases to every element of the same class.

**(3) Integral descent.** The categories of \(k\)-tori and free \(\mathbb Z\)-lattices with continuous Frobenius action are contravariantly equivalent. A length-\(m\) permutation block is the character lattice of \(R_m\); a sign block is the character lattice of \(N_2\); the indicated rotation block is the character lattice of \(Q_4\). The seven integral decompositions follow, including their cyclic factors on \(k\)-points. Equivalently, the finite group of rational torus points has the invariant factors of the integer cokernel of \(qI-A_\lambda\), and the executable verifies agreement with every asserted product decomposition at the sample prime powers \(2,3,4,5,7,8,9,11,16,17,19\). The conceptual block identifications prove the formulas for **all** prime powers.

**(4) Curve and open-complement arithmetic.** For \(n\ge1\), let \(f_n\) count fixed labels of \(F^n\), and let \(v_n,e_n,b_n\) count fixed Petersen vertices, edges, and incident vertex-edge pairs respectively. Each geometric component contributes a \(\mathbb P^1\) over the corresponding extension. Correcting normalization at the nodes gives the exact formula
\[
\#D(\mathbb F_{q^n})=(q^n+1)v_n+e_n-b_n.
\]
The correction \(e_n-b_n\) is essential: a node may be rational while its two geometric branches are exchanged. The surface Picard representation is the five-label permutation representation, so
\[
\#X(\mathbb F_{q^n})=q^{2n}+1+q^n f_n,\quad
\#(X\setminus D)(\mathbb F_{q^n})=q^{2n}+1+q^n f_n-(q^n+1)v_n-e_n+b_n.
\]
More explicitly, if \(c_v(m),c_e(m),c_b(m)\) count the \(m\)-cycle orbits on vertices, edges and half-edges, the full Hasse–Weil zeta function of the reduced curve is
\[
Z_D(T)=\prod_{m\ge1}
(1-T^m)^{-c_v(m)-c_e(m)+c_b(m)}(1-q^mT^m)^{-c_v(m)}.
\]
The zeta function of \(X\setminus D\) is \(Z_X(T)/Z_D(T)\), where \(Z_X(T)=((1-T)(1-q^2T)\prod_{m\ge1}(1-q^mT^m)^{c_f(m)})^{-1}\) and \(c_f(m)\) counts the five-label cycles. The companion data table records all seven orbit profiles and first-extension point-count polynomials.

## Verification
Run `python verification/verify_petersen_tori.py` with Python 3.9 or later and SymPy. Its internal certificate tables contain all seven explicit integral bases. The verifier constructs the graph cycle lattice from first principles, checks the exact signed Frobenius actions, seven unimodular conjugacies, characteristic polynomials, all indicated finite-point cokernels and node-branch orbit profiles. Its expected terminal message is `PETERSEN_SEVEN_INTEGRAL_TORI_VERIFIED`. `data/petersen_tori_seven_types.json` is a machine-readable table of the seven conjugacy classes produced from the verifier.

## Relationship to prior work
Dolgachev–Farb–Looijenga (arXiv:1709.09256, first posted 2017-09-26; journal DOI 10.1007/s40879-018-0231-3) establish the Petersen ten-line divisor, its geometric incidence graph and full \(S_5\) symmetry. González-Sánchez et al. classify arithmetic forms of quintic del Pezzo surfaces. The normalization description of the generalized Jacobian is classical.

The prior published study *A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice* proves an integral \(S_5\)-equivariant index-two embedding and an isogeny of tori. It explicitly does **not** determine every cyclic-Frobenius integral decomposition, every rational torus group structure, or the seven curve/open-complement zeta functions. Its rational character/isogeny cannot, on its own, distinguish the integral norm-one factors. The seven explicit unimodular cyclic bases, all seven exact finite-group decompositions and associated branch-sensitive arithmetic formulas are the additional assertions assessed here.

## Limitations
The theorem concerns the connected generalized Jacobian of the complete nodal exceptional divisor, **not** the Jacobian of a smooth genus-six Wiman–Edge fiber. The group decompositions do not imply a canonical isomorphism between unrelated tori, or identify any preferred arithmetic marking of the five conic bundles. Some first-extension complement point-count polynomials agree for different Frobenius types; the complete integral tori are nevertheless classified by their separately displayed types. Specialist historical literature may contain unindexed equivalent lattice computations; publication priority needs external review. No independent mathematical audit has been performed.

## References
1. I. Dolgachev, B. Farb, E. Looijenga, *Geometry of the Wiman Pencil, I: Algebro-Geometric Aspects*, arXiv:1709.09256 (first posted 2017-09-26), https://arxiv.org/abs/1709.09256; journal version, *European Journal of Mathematics* 4 (2018), 879–930, https://doi.org/10.1007/s40879-018-0231-3.
2. J. González-Sánchez, M. Harrison, I. Polo-Blanco, J. Schicho, *Algorithms for Del Pezzo Surfaces of Degree 5*, arXiv:1009.4044, https://arxiv.org/abs/1009.4044.
3. B. Farb, E. Looijenga, *Geometry of the Wiman–Edge pencil and the Wiman curve*, arXiv:1912.12280, https://arxiv.org/abs/1912.12280.
4. *A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-primitive-index-two-map-from-the-exterior-square-root-lattice--88a956595fd2.
