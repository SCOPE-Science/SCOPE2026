# Adjacency spectrum and orthogonal prefix modes of free left regular band commuting graphs

## Finding

Let \(B_n\) be the free left regular band with identity on \(n\ge1\) generators. Its elements are all words with pairwise distinct letters from \(\{1,\ldots,n\}\), including the empty word; multiplication appends, to the first word, only those letters in the second word not already present. Let \(\Gamma_n\) be the simple, loopless graph on **all** elements of \(B_n\), with two distinct elements adjacent precisely when they commute. Define, for each integer \(k\ge1\), the explicit \((k+1)\)-square matrix \(H_k=(h_{ij})_{0\le i,j\le k}\) by
\[
h_{ij}=\begin{cases}
0,&i=j,\\
1,&i>j,\\
\dfrac{(k-i)!}{(k-j)!},&i<j,
\end{cases}
\qquad P_k(z)=\det(zI_{k+1}-H_k).
\]
Then the **entire adjacency characteristic polynomial**, including every eigenvalue multiplicity, is
\[
\boxed{\chi_{\Gamma_n}(z)=P_n(z)\prod_{k=1}^{n-1}P_k(z)^{\,k n!/(k+1)!}.}\tag{1}
\]
More precisely, the real adjacency representation has an explicit orthogonal, invariant decomposition into one copy of \(H_n\), and exactly \(k n!/(k+1)!\) copies of \(H_k\) for each \(1\le k<n\). The matrices are symmetrizable and hence have real eigenvalues.

The eigenvalue \(-1\) occurs **once in every factor** and therefore has multiplicity exactly
\[
\boxed{\operatorname{mult}_{\Gamma_n}(-1)=n!.}\tag{2}
\]
Equivalently, for each \(k\ge1\), \(P_k(-1)=0\) and \(P'_k(-1)=-2(k-1)!\). This last identity ensures that an apparent common root cannot hide a larger multiplicity within a factor.

For example, with \(16\) vertices at \(n=3\),
\[
\chi_{\Gamma_3}(z)=(z+1)^6(z-1)^3(z+3)(z^2-4z-7)(z^2-z-4)^2.
\]
For the conventional commuting graph that excludes the central identity, \(n\ge2\), the graph is the disjoint union of \(n\) copies of \(\Gamma_{n-1}\), so its characteristic polynomial is \(\chi_{\Gamma_{n-1}}(z)^n\). This is a consequence of the same prefix decomposition, not a separate theorem.

## Assumptions and scope

The basis set is **not** the set of arbitrary words and **not** a free left legal semigroup without idempotence. All words have distinct letters; multiplication is the standard free left regular band product and obeys \(x^2=x\), \(xyx=xy\). The graph is undirected, simple, and defined by literal commutation of elements in the monoid. Its vertex count is \(N_n=\sum_{d=0}^n n!/(n-d)!\). Adjacency eigenvalues are over \(\mathbb R\), with multiplicities in the ordinary characteristic polynomial. Empty products equal one. The standard noncentral graph excludes only the empty word when \(n\ge2\).

## Proof

**1. Commutation equals prefix comparability.** Write \(u\preceq v\) if \(u\) is a prefix of \(v\). If \(u\preceq v\), then the letters of \(u\) are already present at the start of \(v\), so \(uv=vu=v\). Conversely, if two distinct words \(u,v\) commute, the word \(uv\) begins with \(u\) and the word \(vu\) begins with \(v\); equality forces the shorter to be an initial segment of the longer. Thus \(\Gamma_n\) is the strict ancestor-comparability graph of the rooted *permutation prefix tree*, whose vertices at depth \(d\) have exactly \(n-d\) children.

**2. A complete orthogonal adjacency splitting.** Let \(\mathcal H=\mathbb R^{B_n}\) with the counting inner product. The radial space \(U\) of functions constant on each global depth is invariant, since a vertex of depth \(i\) has exactly one ancestor at each depth \(j<i\) and \((n-i)!/(n-j)!\) descendants at every depth \(j>i\). The adjacency restriction to the depth-value coordinates of \(U\) is \(H_n\). These depth coordinates are not normalized orthogonally, but represent the invariant operator faithfully.

For each vertex \(v\) at depth \(d<n\), write \(b=n-d\) for its number of children and \(k=b-1\). In each child subtree, list its internal levels \(0,\ldots,k\). For any \(a=(a_1,\ldots,a_b)\in\mathbb R^b\) with \(\sum a_j=0\) and any \(f=(f_0,\ldots,f_k)\in\mathbb R^{k+1}\), define a function \(\Phi_{v,a,f}\) equal to \(a_j f_i\) on internal level \(i\) of the \(j\)-th child subtree, and zero off all those child subtrees. Let \(W_v\) be the span of these functions. Because each child subtree has the same number of vertices at a given internal depth, every sum of \(\Phi_{v,a,f}\) across one absolute depth in the descendants of \(v\) is zero. Therefore vertices above \(v\) receive zero adjacency contribution, and vertices outside its descendant cone receive none. Within each child subtree the adjacency operator acts by the same \(H_k\) on \(f\), with coefficient \(a_j\). Hence \(W_v\) is invariant and its adjacency restriction is \(k\) copies of \(H_k\).

The spaces \(U\) and \(W_v\) are pairwise orthogonal: disjoint descendant cones are disjointly supported; for nested cones, every function in the smaller \(W_v\) sums to zero on every internal level of the larger child subtree, while the larger function is constant on each such level. The same cancellation proves orthogonality to \(U\). Finally, the depth-space identity
\[
\dim U+\sum_{d=0}^{n-1}\sum_{|v|=d}\dim W_v
=(n+1)+\sum_{d=0}^{n-1}\frac{n!}{(n-d)!}(n-d-1)(n-d)
=N_n
\]
can be checked by induction on the rooted tree: one radial degree of freedom per level plus \(b-1\) relative child coefficients at every child-subtree level accounts for the full function space. Consequently the displayed orthogonal invariant spaces exhaust \(\mathcal H\).

A vertex at depth \(d=n-k-1\) has \(k+1\) children and its \(W_v\) contributes \(k\) copies of \(H_k\). There are \(n!/(k+1)!\) such vertices. Multiplying the factors of the orthogonal direct sum gives (1). Equivalently, the degree check is
\[
(n+1)+\sum_{k=1}^{n-1}(k+1)\frac{k n!}{(k+1)!}=N_n.
\]

**3. Exact multiplicity at \(-1\).** Put \(M_k=H_k+I\). Its last two rows and its last two columns are identical, so \(P_k(-1)=0\). The leading \(k\times k\) principal minor of \(M_k\) has determinant \((-1)^{k-1}(k-1)!\): replace each of its first \(k-1\) rows by that row minus the next; the resulting rows vanish at and below the original row index and have successive pivots \(k-1,k-2,\ldots,1\) in columns \(1,\ldots,k-1\); expanding down the first column gives the sign. Thus \(\operatorname{rank}M_k=k\), and both right and left kernels are spanned by the last-two-coordinate difference. The only nonzero principal cofactors are the two equal cofactors indexed by the last two coordinates, both \((-1)^{k-1}(k-1)!\). Differentiating the determinant \(P_k(z)=\det(zI-H_k)\) at \(z=-1\) yields
\[
P'_k(-1)=2(-1)^k(-1)^{k-1}(k-1)!=-2(k-1)!\ne0.
\]
Therefore every \(P_k\) contains exactly one \(z+1\) factor. The combined exponent in (1) equals
\[
1+\sum_{k=1}^{n-1}\frac{k n!}{(k+1)!}
=1+n!\sum_{k=1}^{n-1}\left(\frac1{k!}-\frac1{(k+1)!}\right)=n!,
\]
proving (2).

**4. Standard noncentral graph.** For \(n\ge2\), only the empty word commutes with every word (choose a different first letter to witness noncommutation for each nonempty word). After deleting the identity, words with distinct first letters cannot commute, whereas each fixed-first-letter subgraph is isomorphic via removal of its first letter to the full \(\Gamma_{n-1}\). This proves the final assertion.

## Verification

The attached standalone `checker.py` reconstructs the semigroup operation from injective words and tests all ordered products for \(n=1,2,3,4\); it independently computes all adjacency entries and the entire characteristic polynomial at sizes \(2,5,16,65\). It compares these full polynomials with the factorized expression (1), and verifies the noncentral decomposition for \(n\ge2\). Further symbolic checks verify \(P_k(-1)=0\), \(P'_k(-1)=-2(k-1)!\), and the principal-minor formula through \(k=10\), along with full-degree and multiplicity identities through \(n=15\). Output markers are `DIRECT_ALL_PRODUCTS_AND_FULL_CHARPOLY_PASS`, `RADIAL_MINUS_ONE_SIMPLE_AND_MINOR_PASS`, and `DEGREE_AND_MULTIPLICITY_IDENTITIES_PASS`. These finite checks corroborate, but do not substitute for, the exact all-\(n\) proof above. Run `python checker.py` with Python 3 and SymPy installed.

## Relationship to prior work

Saliola [1] gives the free left regular band construction and studies the quiver and Cartan invariants of its semigroup algebra; these are not eigenvalues of the **element-commutation graph**. Brown [2] studies transition spectra of random walks driven by left regular bands, again different operators from the symmetric adjacency operator here. Jacobs, Trevisan, and Tura [3] give a general cotree-based algorithm to locate adjacency eigenvalues of any cograph and recall earlier general cograph results on the multiplicity of \(-1\); those results could independently recover the special \(-1\) count, which is **not claimed as a novel stand-alone observation**. Conde, Dratman, and Grippo [4] prove general spectral exclusion bounds for trivially perfect graphs, including a level-equitable quotient for a complete binary tree and a Schur-complement characteristic-polynomial recursion for general graphs in the class. As a graph, \(\Gamma_n\) belongs to that class. Their generic recursion can in principle compute its polynomial, so the present contribution is **not** a claim of first computability of this spectrum, nor the general rooted-tree characterization. Rather, it is the explicit all-\(n\) semigroup-specific **orthogonal invariant eigenspace decomposition**, its closed factorial-factor multiplicities, and the exact \(n!\) multiplicity of \(-1\), which are not explicitly stated by those inspected results. Work on free *left legal semigroups* without band idempotence concerns a different semigroup variety and different commuting components. Residual risk remains that general cograph spectral-decomposition literature implicitly provides the same branching-mode factorization.

## Limitations

The result concerns the free left regular band (not quotients, weighted products, or more general left legal semigroups). The simple graph includes the empty word; the customary noncentral variant is separately reduced to disjoint copies above. Factor polynomials are given by explicit determinants, not radical closed forms for their individual roots. The assertion does not preclude numerical coincidences among non-\(-1\) roots of distinct factors. The priority comparison is best-knowledge rather than an exhaustive historical originality certificate, and the verification is finite; an independent audit has not been performed.

## References

1. F. V. Saliola, *The Quiver of the Semigroup Algebra of a Left Regular Band*, arXiv:math/0608698v1, first submitted 2006-08-28, https://arxiv.org/abs/math/0608698.
2. K. S. Brown, *Semigroups, Rings, and Markov Chains*, arXiv:math/0006145v1, first submitted 2000-06-20, https://arxiv.org/abs/math/0006145.
3. D. P. Jacobs, V. Trevisan, F. C. Tura, *Eigenvalue Location in Cographs*, arXiv:1609.04477v1, first submitted 2016-09-15, https://arxiv.org/abs/1609.04477.
4. C. M. Conde, E. Dratman, L. N. Grippo, *A Sharp Forbidden Interval for the Nontrivial Adjacency Eigenvalues of Trivially Perfect Graphs*, arXiv:2606.06052v1, first submitted 2026-06-04, https://arxiv.org/abs/2606.06052.
