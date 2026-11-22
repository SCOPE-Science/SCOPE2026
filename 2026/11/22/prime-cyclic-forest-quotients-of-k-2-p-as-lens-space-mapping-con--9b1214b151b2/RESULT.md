# Prime cyclic forest quotients of \(K_{2,p}\) as lens-space mapping cones

## Finding
Let \(p\ge3\) be an odd prime. Let \(X_p\) be the graphic-matroid independence complex of the complete bipartite graph \(K_{2,p}\): its simplices are precisely the cycle-free subsets of the \(2p\) graph edges. The cyclic group \(C_p\) rotates the \(p\) degree-two vertices while fixing the two degree-\(p\) vertices, and \(Y_p=|X_p|/C_p\) is the **ordinary geometric orbit space** (not a fixed-point space or homotopy quotient).

Let \(L_p=L^{p-2}(p;1,2,\ldots,(p-1)/2)\) be the generalized lens space, the quotient of the unit sphere in the direct sum of the nontrivial real two-dimensional rotation representations of \(C_p\) by their simultaneous cyclic action. Write \(\pi_p:S^{p-2}\to L_p\) for this free \(p\)-fold covering. With \(\Sigma\) the unreduced suspension and \(\operatorname{Cof}\) the mapping cone, there is a homeomorphism
\[
Y_p\cong\operatorname{Cof}(\Sigma\pi_p).
\]
In particular, \(Y_p\) is simply connected, and its **entire reduced integral homology** is
\[
\widetilde H_j(Y_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z/p\mathbb Z,&j\in\{2,4,\ldots,p-1\},\\
0,&\text{every other }j.
\end{cases}
\]
Thus, while \(X_p\simeq\bigvee^{p-1}S^p\) has torsion-free homology, its cyclic quotient has order-\(p\) torsion in precisely \((p-1)/2\) different positive degrees. The smallest cases have \(\widetilde H_2(Y_3)\cong\mathbb Z/3\mathbb Z\) and \(\widetilde H_2(Y_5)\cong\widetilde H_4(Y_5)\cong\mathbb Z/5\mathbb Z\).

## Assumptions and scope
The graph has hubs \(u,v\), leaves indexed by \(i\in\mathbb Z/p\mathbb Z\), and edges \(a_i=\{u,i\}\), \(b_i=\{v,i\}\). The generator \(g\in C_p\) acts by \(a_i\mapsto a_{i+1}\) and \(b_i\mapsto b_{i+1}\). The lens-space weights \(1,\ldots,(p-1)/2\) refer to complex eigenlines for this particular generator; reversing the generator changes the coordinate description but not the asserted orbit space. All homology groups use integer coefficients. No assertion is made for composite \(p\), for other subgroups, or for induced-forest vertex complexes.

## Proof
**1. The two-hub four-cycle criterion.** Every simple cycle in \(K_{2,p}\) has length four and uses both edges incident to each of two distinct leaves. Consequently a forest may contain both \(a_i,b_i\) for at most one index \(i\), and every such edge subset is a forest.

**2. An equivariant union of balls.** Let \(S_i^0\) be the zero-dimensional simplicial complex with vertices \(a_i,b_i\), and set
\[
Q=\mathop{*}_{i\in\mathbb Z/p\mathbb Z}S_i^0,
\qquad
B_i=\Delta(\{a_i,b_i\})*\mathop{*}_{j\ne i}S_j^0.
\]
The cross-polytope boundary \(Q\) is a PL sphere of dimension \(p-1\). Each \(B_i\) is a PL \(p\)-ball, with full boundary \(Q\), and \(B_i\cap B_j=Q\) for distinct indices. The criterion in Step 1 proves the simplicial equalities \(X_p=\bigcup_i B_i\). The rotation group fixes \(Q\) setwise and permutes the \(p\) balls freely and transitively. Therefore the orbit space identifies all the ball interiors with exactly one \(p\)-ball, attached to \(|Q|/C_p\) by the quotient of its boundary map \(q:|Q|\to |Q|/C_p\):
\[
Y_p\cong(|Q|/C_p)\cup_q D^p=\operatorname{Cof}(q).
\]
This is an actual homeomorphism of the orbit spaces and an explicit attaching-map model; the ball interiors have no nontrivial stabilizers.

**3. The quotient boundary is a suspended lens space.** Map the two vertices \(a_i,b_i\) of the cross-polytope to \(+e_i,-e_i\) and project its boundary radially onto the unit sphere \(S(\mathbb R^p)\). This is \(C_p\)-equivariant, with the action cyclically permuting coordinates. Split the real representation orthogonally as \(\mathbb R^p=\mathbb R\mathbf1\oplus V\), where \(V=\{(x_i):\sum_i x_i=0\}\). For the specified odd prime, the Fourier decomposition gives
\[
V\cong_{\mathbb R[C_p]}\bigoplus_{k=1}^{(p-1)/2}\mathbb C_k,
\qquad g\cdot z=\exp(2\pi i k/p)z\quad\text{on }\mathbb C_k.
\]
Every nonidentity element has no nonzero fixed vector in \(V\), so \(C_p\) acts freely on \(S(V)\cong S^{p-2}\), with quotient precisely \(L_p\). The standard latitude presentation \(S(\mathbb R\oplus V)\cong\Sigma S(V)\) is equivariant (the summand \(\mathbb R\mathbf1\) is fixed). Hence \(|Q|/C_p\cong\Sigma L_p\) and the quotient map \(q\) identifies with \(\Sigma\pi_p\). Step 2 proves the claimed mapping-cone model.

**4. Integral homology and the attaching degree.** The lens space \(L_p\), of odd dimension \(p-2\), has a CW decomposition with one cell in every dimension \(0,1,\ldots,p-2\); its integer cellular differentials are multiplication by \(p\) in positive even degrees and zero in odd degrees. After unreduced suspension, collapse the evident 1-cell spanning tree, obtaining one cell in each dimension \(2,3,\ldots,p-1\), with differential multiplication by \(p\) in odd degrees \(3,5,\ldots,p-2\). Since \(p\) is odd, the coordinate cycle acts orientation-preservingly on the cross-polytope sphere. A generic orbit has exactly \(p\) points, and the covering \(S(V)\to L_p\) has topological degree \(p\). Thus the suspended attaching map \(\Sigma\pi_p:S^{p-1}\to\Sigma L_p\) has degree \(p\) on top integer homology. Its mapping cone introduces one \(p\)-cell whose differential is multiplication by \(p\) into the degree-\(p-1\) cell. The cellular chain complex consequently has a copy of \(\mathbb Z\) in every degree \(2\) through \(p\), with multiplication by \(p\) from each odd-degree cell onto the preceding even-degree cell and zero differentials otherwise. Its reduced homology is exactly the displayed family of \(\mathbb Z/p\mathbb Z\) groups. Finally \(L_p\) is connected, so \(\Sigma L_p\) is simply connected; attaching the \(p\)-cell for \(p\ge3\) does not change its fundamental group.

## Verification
The standalone `verify.py` enumerates all four-state edge configurations for \(p=3,5\) and independently tests acyclicity with union-find; the forest criterion and face counts \(54\) and \(648\) are confirmed. It then independently constructs the barycentric chain complex of \(|Q|/C_p\), forming face-flag orbits under the cyclic action, checks all integer boundary compositions, and calculates ranks over \(\mathbb F_p\) and \(\mathbb F_{101}\). The respective quotient-base chain ranks are \((10,24,16)\) and \((50,528,1632,1920,768)\). The computed Betti vectors are \((1,0,1)\) over both fields for \(p=3\); for \(p=5\), they are \((1,0,1,1,1)\) over \(\mathbb F_5\) and \((1,0,0,0,1)\) over \(\mathbb F_{101}\). These checks agree with the suspended-lens model. The generic-degree-\(p\) attaching calculation and the infinite-prime conclusion are established by the proof, not inferred from these finite checks. `verification_output.txt` records the actual output.

## Relationship to prior work
Matroid shellability gives the sphere-wedge homotopy type of the **unquotiented** forest complex; the 2007 monograph of Jonsson supplies the surrounding graph-complex framework, and Kook's paper (public online 9 March 2006) studies homology of coned graphic matroids. Kook and Lee's 2018 Sections 3 and 5 give the complete-bipartite Möbius coinvariant, top-dimensional homology bases, and restricted symmetric-group actions, not orbit-space integral homology. Moci and Pezzoli's 2020/2021 Sections 4 and 6 develop equivariant matroid homology representations, also not integral orbit-space topology.

A directly relevant previously published computation, *The full integral automorphism module of the \(K_{2,n}\) forest complex* (published-finding corpus, 8 November 2026), already presents the cross-polytope-boundary/multiple-ball decomposition in Step 2 and identifies the full integral homology representation. **That structural decomposition is prior work and is not claimed as new here.** Its stated quotient result is only rational acyclicity for the **full** automorphism group. The present result instead identifies the explicit ordinary prime-cycle **quotient attaching map** as the suspended covering of a weighted lens space and determines every previously unresolved positive-degree **integral torsion group**. The prior homology representation alone does not determine these groups; the additional orbit-space and lens-space analysis is essential. An equivalent implicit corollary of a broader unindexed equivariant classification remains a novelty risk.

## Limitations
This theorem is restricted to odd primes, the specified rotating-leaf action, and ordinary quotient topology; it does not determine ring operations, all homotopy groups, or composite-width quotients. A mapping cone of a lens-space cover is not asserted to be a wedge of Moore spaces: integral homology alone cannot justify such a splitting. The source comparisons and finite computations are not an independent review or an exhaustive priority search.

## References
1. W. Kook, *The homology of the cycle matroid of a coned graph*, European Journal of Combinatorics 28 (2007), 734–741, doi:10.1016/j.ejc.2006.01.001 (available online 9 March 2006).
2. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer (eBook first published 10 December 2007), doi:10.1007/978-3-540-75859-4.
3. W. Kook and K.-J. Lee, *Möbius coinvariants and bipartite edge-rooted forests*, European Journal of Combinatorics 71 (2018), 180–193, https://www.math.snu.ac.kr/~woongkook/201806MC.pdf, Theorems 5.3, 5.5.
4. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, https://arxiv.org/html/2001.03760v3, particularly Section 6.
5. *The full integral automorphism module of the \(K_{2,n}\) forest complex*, published-finding corpus (8 November 2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-full-integral-automorphism-module-of-the-k-2-n-forest-comple--85376ba6b470/RESULT.md.
6. *Lens space*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Lens_space (standard definition and integral homology calculation).
