# Simplicial orientations and the full flip-degree enumerator of complete bipartite graphs

## Finding

Let \(K_{m,n}\) be the complete bipartite graph with two fixed, individually labelled vertex classes of sizes \(m,n\ge1\). Let \(\mathcal A_{m,n}\) have one vertex for every acyclic orientation of \(K_{m,n}\), and join two orientations if reversing exactly one edge preserves acyclicity. Define its degree polynomial by
\[
D_{m,n}(t)=\sum_{\omega\in V(\mathcal A_{m,n})}t^{\deg_{\mathcal A_{m,n}}(\omega)}.
\]

**Theorem.** Every acyclic orientation has a unique ordered sequence of nonempty, alternately coloured blocks \(W_1,\ldots,W_r\): each block consists entirely of vertices from one bipartition class, and a cross-edge points from its earlier block to its later block. Set \(s_i=|W_i|\). Its number of legal single-edge reversals is precisely
\[
\deg_{\mathcal A_{m,n}}(\omega)=\sum_{i=1}^{r-1}s_i s_{i+1}.
\]
Consequently \(D_{m,n}(t)\) is given by the finite, explicit block-size formula
\[
D_{m,n}(t)=\sum_{r=2}^{m+n}\ \sum_{\substack{c_1,\ldots,c_r\in\{A,B\}\\c_i\ne c_{i+1}}}\ \sum_{\substack{s_1,\ldots,s_r\ge1\\ \sum_{c_i=A}s_i=m\\\sum_{c_i=B}s_i=n}}\frac{m!n!}{s_1!\cdots s_r!}\ t^{\sum_{i=1}^{r-1}s_i s_{i+1}}.
\]

For \(m,n\ge2\), put \(p=\min\{m,n\}\), \(q=\max\{m,n\}\), and \((a)_k=a!/(a-k)!\) for \(0\le k\le a\). Then the minimum vertex degree is \(m+n-1\); the number of vertices attaining it is exactly
\[
S_{m,n}=2\sum_{k=1}^{p-1}(m)_k(n)_k+p!(q)_{p-1}\bigl(2^{q-p+1}-2\bigr).
\]
For \(\min\{m,n\}=1\), the graph \(K_{m,n}\) is a star and every one of its \(2^{mn}\) orientations has degree \(mn=m+n-1\).

The degree polynomial for the entire infinite family \(K_{2,n}\), \(n\ge1\), simplifies to
\[
\boxed{D_{2,n}(t)=2^n t^{2n}+2\sum_{j=1}^{n}\binom nj2^{n-j}t^{n+j}.}
\]
For \(n\ge2\), exactly \(n2^n\) of its \(2\cdot3^n-2^n\) orientations have the minimum degree \(n+1\); their proportion is asymptotic to \(\frac n2(\frac23)^n\). These minimum-degree orientations are exactly the *simple vertices* of the \((m+n-1)\)-dimensional graphical zonotope of \(K_{m,n}\). In particular, the proportion of simple vertices for the balanced family \(K_{n,n}\) tends to zero as \(n\to\infty\).

## Assumptions and scope

All graphs are finite, simple and individually labelled; orientations are distinct whenever any named edge has opposite direction. An edge reversal is allowed only when the resulting orientation remains acyclic. The degree polynomial counts vertices with multiplicity and does **not** count degree classes up to graph automorphisms. The graphical zonotope is the Minkowski sum of the edge segments \([e_u,e_v]\) in \(\mathbb R^{m+n}\); it has affine dimension \(m+n-1\) because \(K_{m,n}\) is connected. A vertex of a \(d\)-dimensional polytope is *simple* precisely when it has \(d\) neighbours in the one-skeleton.

## Proof

**Canonical blocks.** An acyclic orientation has a topological ordering. Group consecutive vertices from the same bipartition class into maximal blocks. The direction of every cross-edge is from the earlier to the later block. The block sequence is independent of the chosen topological ordering: two vertices of the same part belong to the same block if and only if their edges toward every vertex of the other part have identical directions. Distinct such classes are linearly ordered by inclusion of their forward-neighbour sets, since otherwise two conflicting \(2\times2\) patterns create a directed four-cycle. Between two consecutive classes from one part lies a nonempty class from the opposite part. Hence there is a unique ordered alternation. Conversely, every such ordered alternation defines an acyclic orientation.

**Which edges flip.** A cross-edge connecting nonconsecutive blocks has its endpoints at indices differing by an odd integer at least three. Choosing any vertex from each intervening block gives a directed path of length at least three from its tail to its head. Flipping this edge would close a directed cycle. An edge between consecutive blocks cannot have another directed path from its tail to its head, since every directed edge strictly increases its block index, and there is no intervening block. Therefore its reversal remains acyclic. All and only consecutive-block edges flip, proving the degree formula.

**Full enumerator.** For each alternating colour pattern and positive block sizes summing to \(m\) and \(n\) in their respective colours, distributing the labelled vertices among the ordered blocks gives \(m!n!/(s_1!\cdots s_r!)\) distinct orientations. The canonical form prevents double counting. Summing the degree weights gives the displayed finite polynomial.

**Simplicial orientations.** The undirected graph consisting of consecutive-block edges is connected: it is the blow-up of a path by nonempty vertex classes. Thus its number of edges is at least \(m+n-1\). Equality holds precisely when this graph is a tree. If some internal block contains two vertices, both have a neighbour in each neighbouring block, producing a four-cycle. If two adjacent blocks both contain at least two vertices, their complete bipartite joining also contains a four-cycle. Conversely, if every internal block is a singleton, each end block is attached to one singleton and the whole graph is a tree. For \(m,n\ge2\), a two-block sequence cannot be a tree, so its length is at least four.

For an even block sequence of length \(2j\), the two end blocks are opposite colours; all \(2j-2\) internal blocks are singletons. The first colour has \(j-1\) ordered singleton blocks and the second colour also has \(j-1\), with the remaining vertices going into the two end blocks. Such orientations exist for \(2\le j\le p\), and both possible starting colours contribute \(2(m)_{j-1}(n)_{j-1}\) orientations.

For an odd block sequence of length \(2j+1\), both ends have the same colour. The opposite colour has exactly \(j\) vertices, all in singleton blocks. Thus \(j=p\) and the end-block colour must be the larger part with \(q>p\). There are \(p!\) orders for the opposite-colour vertices, \((q)_{p-1}\) ways to fill the internal singleton blocks of the larger part, and \(2^{q-p+1}-2\) nontrivial assignments of the remaining vertices between the two nonempty end blocks. Summing both parity cases proves \(S_{m,n}\), including the balanced case where the odd contribution vanishes. For a star all edge directions are independently reversible.

**The \(2\)-by-\(n\) law.** Represent an orientation by a binary \(2\times n\) matrix, with entry one when the edge points from the corresponding size-two-side vertex to the other endpoint. Acyclicity is equivalent to forbidding the simultaneous presence of a column of type \(01\) and one of type \(10\): the two forbidden columns form a directed four-cycle, and any directed cycle in a complete bipartite graph contains a directed four-cycle. If no mixed column occurs, every column is \(00\) or \(11\), giving \(2^n\) orientations of degree \(2n\). Otherwise, choose one of the two possible mixed types; choose \(j\ge1\) mixed columns; and assign either \(00\) or \(11\) to each remaining column. Each mixed column supports two flippable edges, and each unmixed column exactly one, so the degree is \(n+j\). This gives \(2\binom nj 2^{n-j}\) orientations of degree \(n+j\), proving the closed polynomial. Setting \(t=1\) gives the known total \(2\cdot3^n-2^n\), while the coefficient at \(t^{n+1}\) is \(n2^n\).

**Zonotopal consequence.** The standard identification of acyclic orientations with graphical-zonotope vertices sends a legal edge reversal to an edge of the one-skeleton. Its dimension is \(m+n-1\), so the equality case above counts all simple vertices. In the balanced case, \(S_{n,n}=2(n!)^2\sum_{j=1}^{n-1}(j!)^{-2}<4(n!)^2\). The known alternating-block count includes, for \(n\ge2\), at least \(\frac12(n!)^2(n-1)^2\) orientations with \(n-1\) blocks in each side (two ordered decompositions, one two-element block per side). Hence the proportion of simple vertices is at most \(8/(n-1)^2\) and tends to zero.

## Verification

The two standalone standard-library Python programs `verify_blocks.py` and `verify_matrices.py` give independent finite checks. The first enumerates labelled ordered blocks and evaluates the closed simple-vertex formula. The second exhaustively checks \(0/1\) matrices for directed four-cycles and computes all legal bit-flip degrees. Their computations agree on \(K_{2,2}\), \(K_{2,3}\), \(K_{3,3}\), \(K_{3,4}\) and \(K_{4,4}\), including the respective degree-polynomial coefficient arrays. These finite checks support but are not used in place of the proof for arbitrary \(m,n\).

## Relationship to prior work

Cameron, Glass, Rekvényi and Schumacher (2014) established the poly-Bernoulli enumeration of complete-bipartite acyclic orientations and their alternating-block description. Their Section 2.3 already characterizes when an individual edge can be reversed. The block formalism and single-edge criterion are **prior results**, not independently new claims here. Cardinal, Hoang, Merino, Mička and Mütze (2022) explicitly identify flippable arcs with transitive-reduction arcs and the orientation flip graph with the graphical zonotope's one-skeleton. Carballosa, Khera and Reyes (2023) give further complete-multipartite orientation encodings and enumerations. The contribution here is a closed *degree-weighted* specialization for \(K_{2,n}\), the exact all-parameter count/classification of simple vertices, and the full block-size degree enumerator as an organized refinement of the known underlying encoding. In particular, neither a total orientation count nor the expected number of flippable edges identifies the number of minimum-degree orientations.

## Limitations

The weighted polynomial follows from a classical alternating-block parametrization; the claim does not assert a new parametrization or a new general criterion for single-edge flippability. The novelty is a specific enumerative and structural refinement, for which an equivalent formula in unindexed literature is a residual possibility. The result is limited to complete bipartite graphs and their standard single-edge acyclic-orientation flips; it does not claim an analogous formula for general multipartite graphs. Numerical certificates are finite sanity checks, while the theorem for all positive integers rests on the combinatorial proof. No independent scholarly audit has been performed.

## References

1. P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685, first public version 2014-12-11, especially Sections 2.1 and 2.3. https://arxiv.org/abs/1412.3685
2. J. Cardinal, H. P. Hoang, A. Merino, O. Mička and T. Mütze, *Combinatorial generation via permutation languages. V. Acyclic orientations*, arXiv:2212.03915, first public version 2022-12-07, especially Sections 2.2–2.3. https://arxiv.org/html/2212.03915v1
3. W. Carballosa, J. Khera and F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021, first public version 2023-03-16, especially Sections 2–3. https://arxiv.org/html/2303.09021v2
