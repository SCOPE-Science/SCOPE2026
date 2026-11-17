# Integral automorphism modules of vertex-induced forest complexes of complete multipartite graphs

## Finding
For every integer \(k\ge2\) and positive integers \(n_1,\ldots,n_k\), let \(G=K_{n_1,\ldots,n_k}\) have its canonical independent vertex parts \(V_1,\ldots,V_k\). Let \(X=\mathcal F_\infty(G)\) be the simplicial complex of all subsets of vertices whose induced subgraph is a forest. Put \(W_i=\ker(\varepsilon_i:\mathbb Z[V_i]\to\mathbb Z)\), the integral augmentation lattice on the vertices of part \(i\).

The complete **integral graph-automorphism representations** on reduced homology are
\[
\widetilde H_1(X;\mathbb Z)\cong H_1(K_k;\mathbb Z),\qquad
\widetilde H_2(X;\mathbb Z)\cong\bigoplus_{1\le i<j\le k}W_i\otimes_{\mathbb Z}W_j,
\qquad\widetilde H_q(X;\mathbb Z)=0\ (q\ne1,2).
\]
On \(H_1(K_k;\mathbb Z)\), an automorphism acts by its permutation of the parts, including the signs of oriented edges. On the degree-two decomposition it sends the summand attached to an unordered pair of parts to the corresponding new pair, applying the natural vertex permutations. **Interchanging two parts swaps their tensor factors with positive sign.** These actions specify integral lattices, not merely rational characters. The ranks are \(\binom{k-1}{2}\) in degree one and \(\sum_{i<j}(n_i-1)(n_j-1)\) in degree two.

For a graph automorphism \(g\), write \(p\) for its permutation of the \(k\) parts. Let \(F\) be the number of parts fixed by \(p\), let \(E_+\) be the number of unordered pairs with both members fixed individually, and \(E_-\) the number of unordered pairs whose members are exchanged. Then
\[\operatorname{tr}(g\mid \widetilde H_1(X;\mathbb Q))=E_+-E_- -F+1.\]
Writing \(f_i(g)\) for the number of vertices fixed by \(g\) in \(V_i\) when \(p(i)=i\), the degree-two trace is
\[
\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))
=\sum_{\substack{i<j\\p(i)=i,\ p(j)=j}}(f_i(g)-1)(f_j(g)-1)
+\sum_{\substack{i<j\\p(i)=j,\ p(j)=i}}(f_i(g^2)-1).
\]
Here the second summand uses the fixed points of \(g^2\) within \(V_i\), so both formulas hold for all automorphisms, including nontrivial exchanges of equally sized parts.

## Assumptions and scope
The graph is finite, simple and complete multipartite. Each part is nonempty, and \(k\ge2\). The forest condition concerns cycles in the **induced** subgraph on a chosen vertex set, not cycle-free selections of edges. The canonical parts are equivalence classes of nonadjacency, and every automorphism permutes parts of equal size. All representation statements are over \(\mathbb Z\), with rational traces stated separately. No choice of orientation changes the isomorphism class of the module.

## Proof
**1. Characterization of faces.** A vertex subset meeting three different parts creates an induced triangle. A vertex subset meeting two parts in at least two vertices each creates an induced square. Conversely a subset meeting one part induces an edgeless graph, and a subset meeting exactly two parts with just one vertex in one of them induces a star. Therefore a subset is a face exactly when it meets at most one part, or exactly two parts with at least one of the two intersections of size one.

**2. Equivariant pairwise relative chains.** Put \(B=\bigsqcup_i\Delta(V_i)\), the disjoint union of the full simplices on the parts, and let \(X_{ij}=X[V_i\cup V_j]\). Every simplex of \(X\) outside \(B\) meets a unique unordered pair of parts. Its boundary, modulo \(B\), involves only simplices from that same pair. Hence there is an exact isomorphism of cellular chain complexes
\[C_\bullet(X,B;\mathbb Z)\cong\bigoplus_{i<j}C_\bullet(X_{ij},\Delta(V_i)\sqcup\Delta(V_j);\mathbb Z).\]
The decomposition is preserved under every graph automorphism, which may permute the summands.

**3. Homology of each pair.** Write \(D_i\) for the zero-dimensional simplicial complex consisting of the vertices of \(V_i\). The forest complex of the complete bipartite subgraph has the exact union
\[X_{ij}=(\Delta(V_i)*D_j)\cup(D_i*\Delta(V_j)),\qquad
(\Delta(V_i)*D_j)\cap(D_i*\Delta(V_j))=D_i*D_j.\]
Each of the two covering subcomplexes is contractible, while their intersection is the connected one-dimensional graph \(K_{n_i,n_j}\), including the contractible star case when a part has size one. The reduced Mayer–Vietoris sequence therefore gives \(\widetilde H_2(X_{ij};\mathbb Z)\cong H_1(K_{n_i,n_j};\mathbb Z)\) and vanishing reduced homology in other degrees. Orient the edges of \(K_{n_i,n_j}\) from \(V_i\) to \(V_j\). Its one-cycle lattice is canonically
\[H_1(K_{n_i,n_j};\mathbb Z)=\ker\bigl(\mathbb Z[V_i]\otimes\mathbb Z[V_j]\to\mathbb Z[V_i]\oplus\mathbb Z[V_j]\bigr)=W_i\otimes W_j.\]
For the last equality, split each augmentation surjectively over \(\mathbb Z\) and inspect the two partial augmentations. Under interchanging the shores, the oriented edge-chain map contributes minus sign, but the Mayer–Vietoris connecting isomorphism also contributes minus sign because it exchanges the two covering subcomplexes. The signs cancel, yielding **positive tensor-factor exchange** on \(H_2(X_{ij})\), including integrally.

**4. Long exact sequence of the pair.** Since each \(X_{ij}\) is connected and has vanishing first homology, the long exact sequence of \((X_{ij},\Delta(V_i)\sqcup\Delta(V_j))\) identifies \(H_1\) of this relative pair with \(\mathbb Z\), generated by a connecting class whose boundary is \([V_j]-[V_i]\) in zero-dimensional homology. Its second relative homology is canonically \(H_2(X_{ij})\), and its other positive relative homology vanishes. Combining with the chain splitting of step 2 gives
\[H_2(X,B)\cong\bigoplus_{i<j}W_i\otimes W_j,\qquad H_1(X,B)\cong\mathbb Z[E(K_k)],\]
where \(\mathbb Z[E(K_k)]\) is the integral oriented-edge chain module. In the long exact sequence for \((X,B)\), the connecting map \(H_1(X,B)\to\widetilde H_0(B)\) is the incidence map of \(K_k\). Since \(H_q(B)=0\) for positive \(q\), its kernel is \(\widetilde H_1(X)\cong H_1(K_k)\), and its degree-two relative group is precisely \(\widetilde H_2(X)\). All constructions commute with permutations of vertices and parts. The vanishing in all remaining dimensions follows from the same relative sequences.

**5. Traces.** The reduced oriented chain complex of \(K_k\) gives \(\operatorname{tr}_{H_1}=\operatorname{tr}_{C_1}-\operatorname{tr}_{C_0}+1\); fixed edges contribute \(+1\) and reversed edges contribute \(-1\). For degree two, any pair of parts moved to another pair contributes zero. For a fixed pair with both parts individually fixed, the trace on the tensor product is the product of the augmentation traces \(f_i(g)-1\) and \(f_j(g)-1\). For an exchanged pair, the positive factor flip has trace equal to the trace of \(g^2\) on \(W_i\), namely \(f_i(g^2)-1\). This proves both character formulas.

## Verification
The standalone `verify.py` enumerates all forest faces and evaluates reduced signed simplicial Lefschetz traces for every automorphism of eight graph instances. The formulas agree for **1,848 automorphisms**. Separately, binary simplicial boundary-matrix reductions verify the predicted homology ranks in seven instances, including mixed-dimensional cases. These checks are finite corroboration, **not** the proof for arbitrary parameters. The preceding natural relative-chain and Mayer–Vietoris argument proves the full infinite statement over the integers. Run `python3 verify.py` and compare with `verification_output.txt`.

## Relationship to prior work
Taylan (2015) introduced the general framework of graph devoid complexes, which includes forbidding induced cycles. Carnero Bravo (2023, updated 2025), Corollary 35 and Theorem 33, already determined the **nonequivariant homotopy types and sphere multiplicities** of these complete multipartite forest complexes. Those classifications are not new here. The present claim is the **integral action of the full graph automorphism group** on the two nonzero reduced homology degrees, including its nontrivial part-interchange signs and all resulting character values. Unlike a sphere-wedge homotopy type, a non-equivariant classification alone does not specify these automorphism modules. Related indexed results on multipartite Čech/Rips complexes and graph Morse complexes concern different simplicial constructions and do not imply this forest-module statement.

## Limitations
The result describes homology representations, not an equivariant homotopy splitting, integral chain-level decomposition of the entire complex, or modular irreducible decomposition. No claim of discovering the known nonequivariant sphere multiplicities is made. Unindexed equivalent equivariant calculations may exist; independent mathematical review has not been performed. The theorem applies to complete multipartite graphs with nonempty parts, not arbitrary graphs.

## References
- D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, first public arXiv version January 27, 2015, arXiv:1501.06754, https://arxiv.org/abs/1501.06754 .
- A. Carnero Bravo, *The Forest Filtration of a Graph*, first public arXiv version July 25, 2023, arXiv:2307.13271, in particular Section 4.2, Theorem 33 and Corollary 35, https://arxiv.org/abs/2307.13271 .
