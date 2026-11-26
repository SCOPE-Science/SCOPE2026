# The full wreath-product homology character of three particles on \(K_{3,3}\)

## Finding
Let \(G=K_{3,3}\), with vertex parts \(L=\{0,1,2\}\) and \(R=\{3,4,5\}\) and all nine edges between parts. Let \(X=\operatorname{UConf}_3(|G|)\) denote the space of unordered sets of three pairwise distinct points in the underlying topological graph. Its graph-automorphism group is \(W=(S_3\times S_3)\rtimes C_2\), with 72 elements. Let \(V\) be the rational two-dimensional standard representation of \(S_3\), and \(\varepsilon\) its sign character. Let \(T^-\) denote the unique extension of \(V\boxtimes V\) on which the canonical interchange of the vertex parts acts as minus tensor-factor flip. The complete rational graded representation is
\[
H_0(X;\mathbb Q)\cong\mathbb Q,\quad
H_1(X;\mathbb Q)\cong T^-,\quad
H_2(X;\mathbb Q)\cong T^-\oplus\operatorname{Ind}_{S_3\times S_3}^{W}(\varepsilon\boxtimes V),
\quad H_q(X;\mathbb Q)=0\ (q\ge3).
\]
Thus the rational Betti vector is \((1,4,8)\). In particular the full symmetry group fixes no positive-degree rational homology; its quotient \(X/W\) has vanishing reduced rational homology.

## Assumptions and scope
The graph is the ordinary six-vertex, nine-edge complete bipartite graph; particles are indistinguishable, collision-free and allowed in edge interiors. All representations and homology groups in the theorem use rational coefficients. The part-exchange involution is \(s(i)=i+3\) for \(0\le i\le2\), \(s(i)=i-3\) for \(3\le i\le5\). Elements acting separately on both sides comprise \(H=S_3\times S_3\). There is no assertion concerning integral \(H_2\)-torsion or ring structure.

## Proof
**Chain model and ranks.** Use the reduced Świątkowski complex of weight three, computing the unordered graph-configuration homology by its comparison theorem. Choose, at each trivalent vertex, a reference incident half-edge \(h_0\) and two differences \(h_1-h_0,h_2-h_0\). The weight-three degree-\(q\) group has basis the choices of \(q\) vertices and one of their two differences at each, multiplied by a degree-\((3-q)\) monomial in nine edge variables. The differential deletes each chosen difference with alternating sign and replaces it by the difference of its two corresponding edge variables. The chain dimensions in degrees zero through three are exactly \((165,540,540,160)\), and exhaustive integer checks show \(\partial^2=0\). Exact finite-field elimination modulo both 101 and 103 gives differential ranks \((164,372,160)\); each is a rigorous lower bound for its rational rank.

Here the bounds force equality over \(\mathbb Q\), not merely over the finite fields. The first differential has rank at most 164 because each boundary has augmentation zero in the 165-dimensional degree-zero space. The third differential has rank at most 160 by its domain dimension. To bound the second, note that the particle-sum/Abel–Jacobi map on loops sends \(H_1(X;\mathbb Q)\) onto \(H_1(G;\mathbb Q)\). Indeed, the latter has a basis of four cycles consisting of rectangles through the fixed left vertex 0 and right vertex 3; for each rectangle, the two vertices not on it are joined by an edge disjoint from the rectangle. Fix two distinct particles in the interior of that complementary edge and move the third around the rectangle. These are collision-free loops projecting onto the four basis graph cycles. Therefore \(\dim H_1(X;\mathbb Q)\ge4\), so \(\operatorname{rank}_{\mathbb Q}\partial_2\le540-164-4=372\). Thus all three rational ranks equal the computed modular ranks, establishing the rational Betti vector \((1,4,8,0)\).

**First-homology representation.** The particle-sum map is natural under all 72 graph automorphisms. Since it is surjective between four-dimensional rational spaces, it identifies \(H_1(X;\mathbb Q)\) with \(H_1(G;\mathbb Q)\) equivariantly. The latter is the standard-by-standard tensor product \(V\boxtimes V\): it is the kernel of the edge-to-vertex cellular boundary, and interchanging left and right parts reverses oriented edges, acting as minus tensor flip. Hence \(H_1(X;\mathbb Q)\cong T^-\).

**Second-homology representation.** For any graph automorphism \(g\), take the alternating trace of its induced maps on the finite reduced chain groups. The resulting Lefschetz number equals \(1-\chi_1(g)+\chi_2(g)\), since homology above degree two vanishes. Each matrix trace is a finite signed count: an edge monomial must be fixed, its selected vertices must map to the same set, and the coefficient of the original ordered half-edge-difference tensor in its image is multiplied by the permutation sign. The accompanying script implements these rules directly for every element. Write \(v(\sigma)=\#\operatorname{Fix}(\sigma)-1\) and \(e(\sigma)=\operatorname{sgn}(\sigma)\) for \(\sigma\in S_3\). The exact result is
\[
\begin{aligned}
\chi_1(\sigma,\tau)&=v(\sigma)v(\tau),\\
\chi_2(\sigma,\tau)&=v(\sigma)v(\tau)+e(\sigma)v(\tau)+v(\sigma)e(\tau),\\
\chi_1(s(\sigma,\tau))&=\chi_2(s(\sigma,\tau))=-v(\tau\sigma).
\end{aligned}
\]
The first term of \(\chi_2\) is the character of \(T^-\). The remaining terms are the restriction to \(H\) of \(\operatorname{Ind}_H^W(\varepsilon\boxtimes V)\); its character vanishes on the other coset, since \(H\) is normal. Thus the stated direct-sum decomposition follows from equality of rational characters in characteristic zero. Averaging either positive-degree character over \(W\) gives zero. Rational homology of a finite simplicial-group quotient is the invariant part; therefore the reduced rational homology of \(X/W\) vanishes.

## Verification
Run `python3 k33_research.py` and `python3 cubical_crosscheck.py` from the same directory using Python 3 (only the standard library is needed). The first computes exact combinatorial boundaries, tests every degree-two and degree-three boundary composition, computes ranks over two finite fields and verifies the displayed characters for all 72 automorphisms. The second reconstructs the unordered Abrams cubical complex after inserting one bivalent midpoint into each original edge (15 vertices, 18 edges), giving independent cell dimensions \((455,1404,1386,432)\) and modulo-101 differential ranks \((454,946,432)\). It tests \(\partial^2=0\) on all positive-dimensional composable cells and matches the two chain models' 72 Lefschetz numbers exactly. See the accompanying saved program outputs. The rank-over-\(\mathbb Q\) argument above is essential; modular computations by themselves would not establish rational ranks.

## Relationship to prior work
Ko–Park, *Characteristics of graph braid groups* (arXiv:1101.2648v1, posted 2011-01-13), Theorem 3.16, gives the first integral homology of graph braid groups, including the torsion phenomenon for nonplanar graphs, but does not give this degree-two automorphism character. The chain model and its naturality come from Świątkowski and the detailed comparison theorem of An–Drummond-Cole–Knudsen, *Subdivisional Spaces and Graph Braid Groups* (arXiv:1708.02351, especially Theorem 4.5 and the reduced model). Ramos–Yun, *Computing stable homology representations of graph configuration spaces* (arXiv:2606.13813v1, §§3–4), addresses two-particle complete-bipartite families and three-particle complete-graph families, not three particles on \(K_{3,3}\) with the full wreath-product action. The present statement refines ranks and general chain models by identifying the complete finite symmetry character.

## Limitations
Only rational homology and the full rational symmetry action are established. In particular no claim is made concerning integral torsion in second homology, the ring structure, or any stable representation beyond this graph. Although the compared sources do not supply the same degree-two character, prior unindexed computations might already imply it. The calculation is internally reproducible but has not received external mathematical verification.

## References
1. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (2011-01-13), especially Theorem 3.16. https://arxiv.org/abs/1101.2648
2. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, arXiv:1708.02351 (2017), Theorem 4.5 and §4. https://arxiv.org/abs/1708.02351
3. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (2026-06-11), §§3.3 and 4. https://arxiv.org/abs/2606.13813
4. J. Świątkowski, *Estimates for homological dimension of configuration spaces of graphs*, Colloq. Math. 89 (2001), 69–79 (original chain-model background).
