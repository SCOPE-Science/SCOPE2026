# Frobenius-fixed Petersen component groups of the ten-curve quintic del Pezzo boundary

## Finding
Let \(k=\mathbb F_q\) be any finite field, let \(S/k\) be any smooth del Pezzo surface of degree five, and let \(D\subset S\) be the reduced divisor consisting of all ten geometric \((-1)\)-curves. Let \(\Gamma\) be the geometric dual graph and \(K(\Gamma)=\operatorname{Div}^0(\Gamma)/\operatorname{im}\Delta\) its critical group. Geometric Frobenius on the ten curves is described, up to conjugacy, by a permutation \(\sigma\in S_5\) of five labels. The **complete** classification of the fixed integral groups is as follows; \(C_m=\mathbb Z/m\mathbb Z\).

| Frobenius cycle type on five labels | \(K(\Gamma)^{\sigma}\) | Order |
| --- | --- | ---: |
| \((1,1,1,1,1)\) | \(C_2\oplus C_{10}^3\) | 2000 |
| \((2,1,1,1)\) | \(C_{10}^2\) | 100 |
| \((2,2,1)\) | \(C_2\oplus C_{10}\) | 20 |
| \((3,1,1)\) | \(C_5\) | 5 |
| \((3,2)\) | \(0\) | 1 |
| \((4,1)\) | \(C_2\) | 2 |
| \((5)\) | \(C_5\) | 5 |

Here fixed points mean the kernel of \(\sigma-1\) **on the integral critical group**, not the fixed part of its rational Laplacian eigenspaces, the connected generalized Jacobian, or the quotient graph's critical group. In particular the mixed cycle type \((3,2)\) has trivial fixed critical group although the geometric critical group has order 2000. The two types \((3,1,1)\) and \((5)\) have isomorphic fixed groups.

For any proper regular semistable smoothing over a henselian discrete valuation ring with residue field \(k\), special fiber \(D\), and geometric node thickness one, the geometric Jacobian Néron component group is \(K(\Gamma)\) with the stated Frobenius action. Consequently the seven rows also describe the \(k\)-rational points of that finite étale component group scheme. This last interpretation is conditional on the existence of such a smoothing; the graph-theoretic classification itself is unconditional.

## Assumptions and scope
The surface is smooth, geometrically integral, and has \(K_S^2=5\). No characteristic restriction is imposed. Over \(\bar k\), its ten exceptional curves \(E_{ij}\) are indexed by unordered pairs \(\{i,j\}\subset\{1,2,3,4,5\}\). Distinct curves intersect transversely in one point precisely when the pairs are disjoint. This gives the Petersen graph \(KG(5,2)\), with ten vertices, fifteen edges, and degree three at each vertex; there are no triple intersections. The geometric divisor \(D\) is therefore a stable nodal curve of arithmetic genus \(15-10+1=6\). It is intrinsic and Frobenius-stable, even when individual components are not defined over \(k\). On the blowup of four points in \(\mathbb P^2\), summing the four exceptional curves and six strict line transforms also gives \(D\sim-2K_S\).

A smooth quintic del Pezzo surface over a finite field is a twist of the split one; the Frobenius action on its geometric exceptional curves is a conjugacy class in the natural \(S_5\). The seven displayed partitions exhaust those classes. The assertions are about the full ten-component boundary, not a chosen pentagon or a selected blowdown presentation.

## Proof
**1. Integral presentation.** Order the graph vertices lexicographically as the ten two-element subsets of \(\{0,1,2,3,4\}\). Write \(L=3I-A\), where \(A_{uv}=1\) if the subsets \(u,v\) are disjoint and is zero otherwise. Delete the last row and column (the vertex \(\{3,4\}\)), obtaining a \(9\times9\) matrix \(R\). Under the basis of degree-zero divisors \(b_j=e_j-e_9\), the columns of \(R\) present the image of the graph Laplacian. Thus \(K(\Gamma)\cong\mathbb Z^9/R\mathbb Z^9\). Exact fraction-free elimination gives \(\det R=2000=2^4 5^3\). The explicit integral matrix \(Q\) in `verify_petersen_frobenius.py` satisfies \(RQ=10I_9\), proving that \(10\) annihilates \(K(\Gamma)\). Direct rank reduction gives \(\operatorname{rank}_{\mathbb F_2}R=5\) and \(\operatorname{rank}_{\mathbb F_5}R=6\). Consequently
\[
K(\Gamma)\cong C_2^4\oplus C_5^3\cong C_2\oplus C_{10}^3.
\]
In particular both primary parts are elementary abelian, a fact needed for the subsequent fixed-group argument.

**2. The action when the deleted vertex moves.** If \(\pi\) is the induced permutation of ten vertices from \(\sigma\in S_5\), its action in the degree-zero basis is the integer matrix
\[
T_{ij}={\mathbf{1}}_{\{i=\pi(j)\}}-{\mathbf{1}}_{\{i=\pi(9)\}},\qquad 0\leq i,j\leq8.
\]
This formula, unlike naively permuting a reduced Laplacian, incorporates movement of the deleted vertex. It descends to the cokernel because \(\sigma\) is a graph automorphism. The provided certificate also checks the integral identity \(R^{-1}TR\in M_9(\mathbb Z)\) for every cycle representative, so there is no implicit rational-only descent.

**3. Exact fixed-group formula.** For \(p=2,5\), the natural quotient \(K(\Gamma)/pK(\Gamma)\) is canonically isomorphic to the elementary \(p\)-primary subgroup. Reducing the integral presentation and induced action modulo \(p\), we obtain
\[
\dim_{\mathbb F_p}K(\Gamma)^{\sigma}[p]
=9-\operatorname{rank}_{\mathbb F_p}\left[\,R\mid T-I_9\,\right].
\]
Indeed the image of \(T-I_9\) on \(\mathbb F_p^9/\operatorname{im}R\) has dimension \(\operatorname{rank}[R\mid T-I_9]-\operatorname{rank}R\). Subtracting it from \(9-\operatorname{rank}R\) gives the formula. This argument computes actual fixed elements, not coinvariants or averaged eigenspaces.

**4. Exhaustive conjugacy-class computation.** The exact modular ranks of the augmented matrices, obtained using the lexicographic vertices and representative cycles in the certificate, are:

| Cycle type | rank modulo 2 | rank modulo 5 | Fixed 2-rank | Fixed 5-rank |
| --- | ---: | ---: | ---: | ---: |
| \((1,1,1,1,1)\) | 5 | 6 | 4 | 3 |
| \((2,1,1,1)\) | 7 | 7 | 2 | 2 |
| \((2,2,1)\) | 7 | 8 | 2 | 1 |
| \((3,1,1)\) | 9 | 8 | 0 | 1 |
| \((3,2)\) | 9 | 9 | 0 | 0 |
| \((4,1)\) | 8 | 9 | 1 | 0 |
| \((5)\) | 9 | 8 | 0 | 1 |

There are exactly seven conjugacy classes of \(S_5\). The module action is by conjugation under relabeling, so one representative of each class suffices. An elementary \(p\)-group of dimension \(d\) is \(C_p^d\); recombining the two coprime primary parts gives precisely the seven groups stated above.

## Verification
Run `python verify_petersen_frobenius.py` (Python 3, standard library only). It reconstructs the graph from two-subset disjointness, checks fifteen edges, the exact determinant, the explicit \(RQ=10I\) certificate, the primary ranks, integral descent of each action, and all fourteen augmented ranks. Its success terminator is `PETERSEN_FROBENIUS_COMPONENT_GROUPS_EXACT_OK`.

As an independent computational route, run `python verify_petersen_enumeration.py` (Python 3 with SymPy). Hermite normal form yields a 2000-element transversal of \(\mathbb Z^9/R\mathbb Z^9\). The program explicitly applies all seven permutations to every class, counts fixed classes and the elements annihilated by two and five. Its terminal marker is `PETERSEN_FROBENIUS_HERMITE_ENUMERATION_OK`. This second calculation does not use the modular-rank formula. These are finite exact certificates for a complete finite classification, not samples extrapolated to an infinite family.

## Relationship to prior work
Roulleau (2010) treats the degree-five del Pezzo surface and the complete ten-curve branch divisor; González-Sánchez, Harrison, Polo-Blanco and Schicho (2010) identify the \(S_5\) exceptional-curve action and classify its twists. Candelas, de la Ossa, van Geemen and van Straten (2012, Appendix 6.1) explicitly give the Petersen intersection graph. Ducey, Hill and Sin (2017 preprint, Theorem 4.1) determine the **nonequivariant** critical group of the entire family \(KG(n,2)\), which in this case gives \(C_2\oplus C_{10}^3\). These facts are antecedents, not novel parts of this result.

The new claim is the seven-case **integral Frobenius-fixed subgroup** table for the natural degree-five del Pezzo boundary and its conditional arithmetic component-group interpretation. Knowing the abstract Smith form or rational \(S_5\)-character does not by itself determine the action on the finite group. A separately published calculation of an index-two map between the Petersen cycle lattice and \(\bigwedge^2 A_4\) concerns the **connected generalized Jacobian** and does not state or imply the seven fixed discriminant groups without the additional integral monodromy pairing and calculations. A complete seven-case description of the connected Picard torus, if given, would concern different arithmetic groups. Absence of an exact match in targeted literature searches is not a proof of historical priority.

## Limitations
The theorem is limited to the full ten-curve boundary on degree-five del Pezzo surfaces, with its natural \(S_5\)-actions. It does not classify component groups for other divisors, change the known nonequivariant critical group, describe the rational-point groups of the connected generalized Jacobian, or assert that all proposed smoothings exist over every finite field. For the Néron interpretation, regular semistability and thickness one are indispensable. Earlier literature indexed under chip-firing, Galois discriminant lattices, or arithmetic sandpile terminology might contain an equivalent fixed-group table; specialist historical review is outstanding. No independent mathematical validation is asserted.

## References
1. X. Roulleau, *The Fano surface of the Fermat cubic threefold, the del Pezzo surface of degree 5 and a ball quotient*, arXiv:1001.5111, first posted 2010-01-28. https://arxiv.org/abs/1001.5111
2. J. González-Sánchez, M. Harrison, I. Polo-Blanco, J. Schicho, *Algorithms for Del Pezzo Surfaces of Degree 5*, arXiv:1009.4044, first posted 2010-09-21, Section 4. https://arxiv.org/abs/1009.4044
3. P. Candelas, X. de la Ossa, B. van Geemen, D. van Straten, *Lines on the Dwork Pencil of Quintic Threefolds*, arXiv:1206.4961, first posted 2012-06-21, Appendix 6.1. https://arxiv.org/abs/1206.4961
4. J. E. Ducey, I. Hill, P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set*, arXiv:1707.09115, first posted 2017-07-28, Theorem 4.1. https://arxiv.org/abs/1707.09115
5. J. Love, L. Taylor, *An arithmetic variant of Raynaud's theorem*, arXiv:2009.10284, first posted 2020-09-22. https://arxiv.org/abs/2009.10284
6. *A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice*, public research result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-primitive-index-two-map-from-the-exterior-square-root-lattice--88a956595fd2
