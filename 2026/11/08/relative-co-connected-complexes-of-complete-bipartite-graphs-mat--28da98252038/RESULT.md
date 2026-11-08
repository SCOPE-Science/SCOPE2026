# Relative co-connected complexes of complete bipartite graphs: matroid structure, homotopy and symmetry

## Finding
For integers \(a,b\ge 2\), let \(G=K_{a,b}\) with vertex shores \(L,R\). Fix a nonempty proper vertex set \(A\), put \(U=(L\cup R)\setminus A\), \(M=|U|\ge2\), and choose \(1\le r\le M-1\). Set \(k=M-r\), so \(1\le k\le M-1\). The relative \(r\)-co-connected complex \(X=\Sigma_r(A,G)\) has facets \(U\setminus F\) for the \(r\)-subsets \(F\subseteq U\) for which \(G[A\cup F]\) is connected.

In all cases \(X\) is the rank-\(k\) truncation of a partition-matroid independence complex. In particular, it is pure, vertex decomposable, shellable, and has integral homotopy type \(\bigvee^{\beta}S^{k-1}\). All reduced integral homology outside degree \(k-1\) vanishes and \(\widetilde H_{k-1}(X;\mathbb Z)\cong\mathbb Z^{\beta}\). Explicitly, with \(\binom{s}{j}=0\) whenever \(s<0\) or \(j<0\) or \(j>s\),

\[
\beta=\begin{cases}
\binom{M-1}{k},& A\cap L\ne\varnothing\text{ and }A\cap R\ne\varnothing,\\[2pt]
\binom{M-1}{k}-\binom{a-|A|-1}{k-b},& A\subseteq L,\\[2pt]
\binom{M-1}{k}-\binom{b-|A|-1}{k-a},& A\subseteq R.
\end{cases}
\]

The integral top-homology symmetry module is determined as follows. Let \(H=\mathfrak S_{L\setminus A}\times\mathfrak S_{R\setminus A}\), acting by vertex permutations that preserve shores and fix \(A\) pointwise. For any finite set \(S\), let \(W_S=\ker(\mathbb Z[S]\xrightarrow{\sum}\mathbb Z)\), its integral augmentation lattice. In the mixed-shore case there is a natural \(H\)-equivariant isomorphism
\[\widetilde H_{k-1}(X;\mathbb Z)\cong\bigwedge^{k}W_U.\]
When \(A\subseteq L\), writing \(L'=L\setminus A\), there is a canonical exact sequence of integral \(H\)-modules
\[
0\longrightarrow\widetilde H_{k-1}(X;\mathbb Z)\longrightarrow\bigwedge^kW_U
\longrightarrow\operatorname{sgn}_R\otimes\bigwedge^{k-b}W_{L'}\longrightarrow0.
\]
The last term is zero for \(k<b\). When \(A\subseteq R\), exchange \(L,R\), giving \(\operatorname{sgn}_L\otimes\bigwedge^{k-a}W_{R'}\). No splitting over \(\mathbb Z\) is asserted. These sequences give the entire rational character: if \(g\) permutes a nonempty finite set \(S\), then
\[
\operatorname{tr}\left(g\mid\bigwedge^j(W_S\otimes\mathbb Q)\right)
=[t^j]\frac{\prod_{C\in\mathrm{cyc}(g|_S)}(1-(-t)^{|C|})}{1+t}.
\]
The character of top homology is the exterior-power character on \(U\), minus the sign-twisted exterior-power character of the corresponding last term (if present).

## Assumptions and scope
The graph is simple, undirected, and complete bipartite. The fixed root \(A\) is nonempty, and its induced graph need **not** be connected: this notably includes every root consisting of at least two vertices from one shore. The full range \(1\le r<M\) and every shore size \(a,b\ge2\) are included. Homotopy and integral homology are unreduced except where a tilde is explicit. A wedge with zero spheres is interpreted as a point; for \(k=1\), a wedge of \(\beta\) copies of \(S^0\) consists of \(\beta+1\) points.

## Proof
**1. Exact identification of the faces.** Suppose first that \(A\) meets both shores. Then \(G[A\cup F]\) is connected for every \(F\subseteq U\). Thus all \(k\)-subsets of \(U\) are facets, and \(X\) is the rank-\(k\) uniform matroid complex.

Now suppose \(A\subseteq L\) is nonempty. A nonempty induced subgraph of \(K_{a,b}\) is connected precisely when it meets both shores, or consists of one vertex. Because \(A\ne\varnothing\), the condition \(G[A\cup F]\) connected is exactly \(F\cap R\ne\varnothing\). Hence its complementary facet \(U\setminus F\) does not contain all \(b\) vertices of \(R\). Every subset \(\sigma\subseteq U\) of cardinality at most \(k\) with \(|\sigma\cap R|\le b-1\) extends to an admissible \(k\)-set: the available partition capacity is \(|L\setminus A|+(b-1)=M-1\ge k\). Consequently
\[
X=\{\sigma\subseteq U: |\sigma|\le k,\;|\sigma\cap R|\le b-1\}.
\]
This is the rank-\(k\) truncation of the partition matroid having full capacity on \(L\setminus A\) and capacity \(b-1\) on \(R\). The case \(A\subseteq R\) follows by interchanging shores.

**2. Homotopy and homological concentration.** Independence complexes of matroids are pure vertex decomposable: deletion and link of any non-coloop are independence complexes of deletion and contraction, with the appropriate rank conditions, so the property follows inductively. Their pure shellings attach cells only in top dimension. It follows that \(X\simeq\bigvee^{\beta}S^{k-1}\), with free integral reduced homology concentrated in that dimension (including the standard zero-dimensional interpretation).

**3. Relative chains and integral symmetry.** Let \(S\) denote the full \((k-1)\)-skeleton of the simplex on \(U\), viewed as an oriented augmented chain complex. Identifying a face \(\{u_1<\cdots<u_j\}\) with \(u_1\wedge\cdots\wedge u_j\), its boundary contracts with the all-ones functional \(\varepsilon:\mathbb Z[U]\to\mathbb Z\). Since \(\varepsilon\) is a split surjection, the kernel of the top boundary is canonically \(\bigwedge^k W_U\). The other reduced homology groups of \(S\) are zero.

In the case \(A\subseteq L\), the quotient relative chain complex \(C_*(S,X;\mathbb Z)\) is freely generated by oriented subsets that contain all of \(R\). Choosing an ordering with \(R\) first, this quotient is exactly the augmented, truncated simplex chain complex on \(L'=L\setminus A\), shifted by \(b\) vertices, with the orientation factor \(\operatorname{sgn}_R\). Boundary terms removing a vertex of \(R\) vanish in the quotient; the remaining boundary is the ordinary augmented boundary on \(L'\). It follows that the only possible relative homology is in degree \(k-1\), where it is
\[
\widetilde H_{k-1}(S,X;\mathbb Z)
\cong\operatorname{sgn}_R\otimes\bigwedge^{k-b}W_{L'}
\]
if \(k\ge b\), and zero otherwise. This statement also covers the vanishing exterior powers in degenerate parameter ranges. The long exact sequence of the pair \((S,X)\), together with the homological concentration established in step 2, gives the stated short exact sequence, integrally and equivariantly. Swapping shores handles \(A\subseteq R\).

**4. Ranks and character.** For nonempty \(S\), the augmentation lattice \(W_S\) has rank \(|S|-1\), including rank zero for \(|S|=1\). For \(S=\varnothing\), its kernel definition gives the zero lattice; the stated character-generating formula is only used for nonempty \(S\). Taking ranks in the exact sequences yields the binomial expressions for \(\beta\). A permutation of \(S\) with cycles \(C\) has exterior-power determinant polynomial \(\prod_C(1-(-t)^{|C|})\) on \(\mathbb Q[S]\). Dividing out the trivial summand contributes \((1+t)^{-1}\), proving the character formula. The short exact sequences determine the difference of characters without asserting an integral direct-sum decomposition.

## Verification
The standalone script `verify_relative.py` reconstructs the defining faces by direct induced-subgraph connectivity, independently constructs the partition-matroid model, calculates the reduced Euler characteristic, checks mod-two chain ranks, and checks signed simplicial Lefschetz characters against the exterior-power formula. Its recorded output, reproduced by executing the packaged source, is:

```
CASES_OK=916 HOMOLOGY_MOD2_OK=875 EQUIVARIANT_TRACES_OK=916
ALL_VERIFY_OK
```

The loops include \(2\le a,b\le5\), all possible root-shore counts, all admissible \(r\), with additional unrooted control cases. The finite tests corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work
Deshpande, Roy and Sawant introduced \(\Sigma_r(A,G)\) in 2025 and established a vertex-decomposability theorem under the hypothesis that \(G[A]\) is connected and nonempty. The present result agrees with that theorem when the root meets both shores or is a singleton, and extends the conclusion to **disconnected roots** in complete bipartite graphs. Its new calculations are the exact matroid model, integral wedge multiplicities, and full stabilizer representation exact sequence. Deshpande and Singh earlier computed higher-independence homotopy types for complete multipartite graphs, a related but **unrooted** setting; that result does not already give the claimed relative, root-dependent modules. Standard matroid shellability and exterior-algebra techniques are explicitly used rather than presented as new.

## Limitations
No claim is made for arbitrary graphs, empty roots, complete multipartite graphs of more than two shores, or integral splitting of the displayed equivariant short exact sequences. Publication priority cannot exclude unindexed equivalents or a broader theorem whose specialization implies these formulas. The finite program does not certify the infinite theorem; the written proof does. Independent mathematical audit has not been performed.

## References
1. P. Deshpande, A. Roy and R. Sawant, *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710 (first public version, October 29, 2025), https://arxiv.org/abs/2510.25710 .
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (2020), https://arxiv.org/abs/2001.05448 .
3. A. Björner, *The homology and shellability of matroids and geometric lattices*, in *Matroid Applications*, Cambridge University Press (1992), standard shellability and homotopy results for matroid complexes.
