# Two integral symmetry characters of hexagonal bouquets

## Finding
For every integer \(m\ge 2\), form the graph \(B_m\) from \(m\) disjoint six-cycles by identifying one specified vertex from each cycle to a common vertex \(v\). Let \(X_m=\operatorname{Ind}(B_m)\), the simplicial complex of independent vertex sets. Then
\[
X_m\simeq S^m\vee S^{2m-1}.
\]
The graph automorphism group is \(G_m=(C_2)^m\rtimes S_m\), with each \(C_2\) reflecting one cycle through \(v\), and \(S_m\) permuting cycles. For \(g=(\epsilon,\pi)\), where \(\epsilon_i\in\{0,1\}\) records the reflection of the \(i\)-th source cycle, its action on **integral** reduced homology is completely determined by
\[
\widetilde H_q(X_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z_{\operatorname{sgn}\pi},&q=m,\\
\mathbb Z_{(-1)^{\sum_i\epsilon_i}},&q=2m-1,\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(\mathbb Z_\chi\) denotes a rank-one integer representation on which \(g\) acts by multiplication by \(\chi(g)\). The two characters are distinct: local reflections reverse the upper homology but preserve the lower; transpositions of cycles do the opposite. In particular, \(\widetilde H_*(|X_m|/G_m;\mathbb Q)=0\) in all degrees.

## Assumptions and scope
Each six-cycle has vertices \(v,x_{i,1},\ldots,x_{i,5}\) in cyclic order, with the edges between successive vertices and the closing edge \(x_{i,5}v\); cycles intersect only at \(v\). All complexes are ordinary abstract independence complexes, with their geometric realizations used for homotopy statements. Homology is reduced and integral unless otherwise marked. The statement covers **every** integer \(m\ge2\), not only the finite values used in verification. At \(m=1\), the two asserted degrees coincide and a different representation statement is needed, so that case is excluded.

## Proof
**1. The exact deletion/link decomposition.** Set \(A_m=\operatorname{Ind}(B_m-v)\) and \(L_m=\operatorname{Ind}(B_m-N[v])\). An independent set either avoids \(v\) or includes \(v\), hence
\[
X_m=A_m\cup(v*L_m),\qquad A_m\cap(v*L_m)=L_m.
\]
The deletion leaves \(m\) vertex-disjoint copies of the five-vertex path \(P_5\), and closed-neighborhood deletion leaves \(m\) copies of the three-vertex path \(P_3\). Independence complexes of disjoint unions are joins, so **exactly**
\[
A_m=\operatorname{Ind}(P_5)^{*m},\qquad L_m=\operatorname{Ind}(P_3)^{*m}.
\]

**2. The two building blocks.** The independent sets of \(P_3\) give one edge on its two endpoints and an isolated middle vertex. Thus \(\operatorname{Ind}(P_3)\simeq S^0\), with generator of \(\widetilde H_0\) given by the isolated vertex minus either endpoint. Under reversal of the path, this generator is fixed because the two endpoints lie in the same connected component. The independent sets of \(P_5\) give a complex with exactly one triangle on vertices \(\{1,3,5\}\), plus the four edges \(\{1,4\},\{4,2\},\{2,5\},\{5,1\}\). Remove the triangle with its free edge \(\{1,3\}\), then remove the edge \(\{3,5\}\) with its now-free vertex \(3\). The remaining four-cycle is a simplicial circle. Its oriented generator can be represented by the loop \(1\to4\to2\to5\to1\). Reversal \(j\mapsto6-j\) reverses the orientation of this loop, hence acts by \(-1\) on \(H_1\).

**3. Homotopy and integral homology.** Joins of the displayed homotopy spheres give
\[
A_m\simeq S^{2m-1},\qquad L_m\simeq S^{m-1}.
\]
For \(m\ge2\), every map \(L_m\to A_m\) is nullhomotopic: after homotopy equivalences this is a map \(S^{m-1}\to S^{2m-1}\), and \(\pi_{m-1}(S^{2m-1})=0\). The pushout of the simplicial cofibration \(L_m\hookrightarrow A_m\) with a cone is its mapping cone; the nullhomotopic attachment gives
\[
X_m\simeq A_m\vee\Sigma L_m\simeq S^{2m-1}\vee S^m.
\]
The integral long exact sequence of the pair \((X_m,A_m)\) has natural connecting map \(\widetilde H_m(X_m)\cong\widetilde H_{m-1}(L_m)\) and natural inclusion isomorphism \(\widetilde H_{2m-1}(A_m)\cong\widetilde H_{2m-1}(X_m)\), because \(m\ge2\) makes the two degrees distinct. These are isomorphisms of integral \(G_m\)-modules, even though no equivariant wedge splitting is asserted.

**4. Group characters and signs.** The common vertex \(v\) has degree \(2m>2\), so it is the unique vertex of this degree. Removing it recovers the \(m\) disjoint five-vertex paths. An automorphism therefore permutes those paths and may independently reverse each one; every such operation extends to the original graph. This proves \(\operatorname{Aut}(B_m)= (C_2)^m\rtimes S_m\). The top class of \(A_m\) is the join product of \(m\) degree-one classes. Reversing any factor multiplies it by \(-1\); transposing two degree-one factors multiplies a join class by \((-1)^{(1+1)(1+1)}=+1\). Thus its character is \((-1)^{\sum_i\epsilon_i}\). For \(L_m\), each degree-zero factor is fixed by its reflection and interchanging two factors gives \((-1)^{(0+1)(0+1)}=-1\). The character on \(\widetilde H_{m-1}(L_m)\), and therefore on \(\widetilde H_m(X_m)\), is \(\operatorname{sgn}\pi\). These signs are integral, not merely rational traces.

**5. The quotient consequence.** Both rank-one characters are nontrivial for \(m\ge2\): a single cycle reflection acts by \(-1\) upstairs, and a transposition acts by \(-1\) downstairs. Both invariant subspaces therefore vanish. Rational transfer for the finite group action (after barycentric subdivision if necessary) identifies rational homology of the orbit space with invariant rational homology, giving the final claim.

## Verification
A standalone standard-library Python verifier is included as `verify.py`, with its actual output in `verification_output.txt`. It enumerates every independent face for \(m=2,3,4\), computes signed augmented Lefschetz traces of all \(8\) automorphisms for \(m=2\), all \(48\) for \(m=3\), and \(72\) selected actions for \(m=4\). Independent full mod-two boundary-rank calculations for \(m=2,3\) give the predicted two homology degrees and ranks. The verifier ends `VERIFY_OK`. The all-parameter proof uses the exact deletion/link pushout and join signs, **not** an extrapolation from these finite tests.

## Relationship to prior work
Daundkar, Panja and Prasad (first public March 15, 2023; arXiv:2303.08798) study independence complexes of graph wedges and establish broad sphere-wedge results, including general wedge-of-cycle settings (Section 3, Theorems 3.5–3.6). Their paper does **not** identify the full local-reflection-and-cycle-permutation action on integral homology. For direct comparison, their displayed link description uses \(\operatorname{Ind}(P_{n-2})\) for a cycle, while in the present vertex-count convention deleting the center and its two neighbors leaves the \((n-3)\)-vertex path. Accordingly no specific homotopy formula from that description is assumed here; the proof above constructs and verifies both exact subcomplexes. The classical path independence-complex homotopy calculation is also standard (Kozlov, 1999); the contribution is the complete integral symmetry module and two-degree classification in this natural infinite family.

The closest indexed comparisons concern matching complexes of Dutch windmills, independence complexes of linear hexagon chains, and nonequivariant wedge-of-graphs results. None of those statements implies the two displayed rank-one \(G_m\)-characters. Equivalent unindexed work is a residual originality risk.

## Limitations
No equivariant homotopy wedge splitting is claimed. No integral homology of the quotient (where group stabilizers may matter) is claimed. The rational quotient statement follows by transfer. The finite verification samples only \(m=2,3,4\), while the proof applies to all \(m\ge2\). The novelty comparison is limited to the explicitly inspected accessible literature and search results; it does not constitute a global uniqueness certificate.

## References
1. N. Daundkar, S. Panja, S. Prasad, *Independence complexes of wedge of graphs*, arXiv:2303.08798v2, first public 2023-03-15. https://arxiv.org/html/2303.08798v2
2. D. N. Kozlov, *Complexes of directed trees*, J. Combin. Theory A 88 (1999), 112–122 (path and cycle independence-complex homotopy calculations).
3. K. Okura, *On the homotopy type of the polyhedral join over the independence complex of a forest*, arXiv:2303.11984, 2023, background on nonequivariant polyhedral joins. https://arxiv.org/abs/2303.11984
