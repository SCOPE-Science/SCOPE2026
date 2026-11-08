# Nonpure sphere-wedge total-visibility complexes of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a labelled connected complete multipartite graph, where \(r\ge3\) and every \(n_i\ge1\). Put \(N=\sum_i n_i\), let \(a\) count parts of size at least two, and let \(b=r-a\) count singleton parts. A *total mutual-visibility set* is a subset \(S\subseteq V(G)\) such that every pair of vertices admits a shortest path with all internal vertices outside \(S\). Write \(\mathcal T(G)\) for the simplicial complex of all these subsets, including the empty face.

For \(a\ge1\), its complete face polynomial and its inclusion-maximal-face polynomial are, respectively,
\[
F_G(z)=(1+z)^N-\sum_{i:n_i\ge2}z^{N-n_i}(1+z)^{n_i}+(a-1)z^N,
\]
\[
M_G(z)=b z^{N-1}+\left(\sum_{i<j:\,n_i,n_j\ge2}n_i n_j\right)z^{N-2}.
\]
For \(a=0\), both polynomials are those of the full simplex: \(F_G(z)=(1+z)^N\) and \(M_G(z)=z^N\).

The **integral homotopy type**, for all allowed part sizes, is
\[
\mathcal T(G)\simeq\begin{cases}
\text{a point},&a\le1,\\
\displaystyle\bigvee^{a-1}S^{N-3},&a\ge2.
\end{cases}
\]
Furthermore, \(\mathcal T(G)\) is a matroid independence complex if and only if \(a\le1\) or \(b=0\); it is nonpure precisely when \(a\ge2\) and \(b\ge1\). In that nonpure regime there are simultaneously \(b\) facets of size \(N-1\), and \(\sum_{i<j:n_i,n_j\ge2}n_i n_j\) facets of size \(N-2\), even though every nonzero reduced integral homology group is in degree \(N-3\). This gives an infinite nonpure family with complete labelled enumeration and a single-dimensional free homology group.

## Assumptions and scope
Graphs are finite, simple, undirected, and labelled. Partitions into \(r\ge3\) positive-sized nonempty independent classes are fixed; every two vertices in different classes are adjacent. The simplicial complex contains the empty face, and its reduced integral homology is understood via geometric realization. A polynomial counts labelled faces, not graph isomorphism classes. The statement does not identify dual, ordinary, or outer mutual visibility with total mutual visibility.

Write \(U_i\) for the partite classes with \(|U_i|\ge2\), let \(U\) be their union, and let \(B\) be the set of singleton-part vertices, so \(|B|=b\). The case \(a=0\) is a complete graph. If \(a\ge1\), the complement of a feasible set will be denoted \(C=V(G)\setminus S\).

## Proof
**1. Exact feasibility.** A pair of distinct vertices in different parts is adjacent and hence automatically has an internally empty shortest path. A pair of vertices within the same non-singleton part \(U_i\) has distance two, and its common neighborhood is exactly \(V(G)\setminus U_i\). The pair is visible relative to \(S\) exactly when one such common neighbor lies outside \(S\), or equivalently \(C\not\subseteq U_i\). Thus
\[
S\in\mathcal T(G)\quad\Longleftrightarrow\quad C\not\subseteq U_i\ \text{for each non-singleton class }U_i.
\]
This is necessary and sufficient, since every pair has distance one or two. If there are no non-singleton classes the condition is vacuous.

**2. All faces and facets.** When \(a\ge1\), the forbidden supersets of \(V(G)\setminus U_i\) have generating polynomials \(z^{N-n_i}(1+z)^{n_i}\). For two distinct non-singleton classes the intersection of these forbidden upward families consists only of the full vertex set. Inclusion-exclusion over \(a\) families therefore gives the asserted \(F_G\), with coefficient \(a-1\) at \(z^N\) correcting repeated subtraction. This also includes the boundary \(a=1\).

An inclusion-maximal feasible \(S\) corresponds to an inclusion-minimal complement \(C\) not contained in any non-singleton part. A singleton vertex by itself qualifies, so each of the \(b\) singleton vertices gives one minimal complement. In the absence of singleton vertices, \(C\) must meet at least two different non-singleton classes, and its inclusion-minimal choices are exactly the two-element cross-class pairs. There are \(\sum_{i<j:n_i,n_j\ge2}n_i n_j\) such pairs. These two types exhaust all minimal complements, proving \(M_G\) and the precise purity boundary.

**3. Matroid structure without singleton parts.** Suppose \(a\ge2\) and \(b=0\), so \(U=V(G)\). Define the rank-two partition matroid \(P\) on \(U\) with parallel classes \(U_i\): its bases are the unordered pairs from different classes. By the complement characterization, a set \(S\) is feasible if and only if it is contained in \(U\setminus\{u,v\}\) for at least one basis \(\{u,v\}\) of \(P\). Hence \(\mathcal T(G)\) is precisely the independence complex of the matroid dual \(P^*\). Its rank is \(N-2\), so its independence complex is pure and shellable of dimension \(N-3\). Matroid shellability gives a wedge of spheres of that dimension, possibly with zero summands. Evaluating the full face polynomial at \(z=-1\) shows that its reduced Euler characteristic is \((-1)^{N-3}(a-1)\). Consequently there are exactly \(a-1\) spheres, over the integers:
\[
\mathcal T(G)\simeq\bigvee^{a-1}S^{N-3}.
\]
The same conclusion also follows from the earlier theory of ordinary two-cut complexes: \(\mathcal T(G)\) is the two-cut complex of the disjoint union of cliques on the classes \(U_i\). This relation is explicitly credited below.

**4. Singleton parts and the suspension.** Suppose \(a\ge2\) and \(b\ge1\). Let \(K_0\) denote the complex just described on \(U\), and let \(\Delta_U\) and \(\Delta_B\) denote the simplices on \(U\) and \(B\). Let \(\partial\Delta_B\) be the proper-subset complex on \(B\); for \(b=1\) this is the augmented complex \(\{\emptyset\}\). Step 1 gives the literal equality
\[
\mathcal T(G)=(\Delta_U*\partial\Delta_B)\ \cup\ (K_0*\Delta_B),
\]
with intersection \(K_0*\partial\Delta_B\). The first term is a cone because \(U\ne\emptyset\); the second term is a cone because \(B\ne\emptyset\). The standard gluing theorem for two contractible subcomplexes yields the suspension of the intersection. For \(b=1\), the intersection is \(K_0\), giving one suspension. For \(b\ge2\), the boundary of the simplex on \(b\) vertices is \(S^{b-2}\), so the intersection is a \((b-1)\)-fold suspension of \(K_0\), and the gluing adds one more. Therefore
\[
\mathcal T(G)\simeq\Sigma^bK_0\simeq\bigvee^{a-1}S^{(|U|-3)+b}=\bigvee^{a-1}S^{N-3}.
\]
The integral conclusion follows from an actual homotopy equivalence and not from a calculation modulo a prime.

**5. Contractible cases and matroid obstruction.** For \(a=0\), all subsets are feasible and the complex is a simplex, the independence complex of a free matroid. For \(a=1\), every feasible set omits at least one singleton vertex, hence \(\mathcal T(G)=\Delta_U*\partial\Delta_B\). This is a cone (because \(U\ne\emptyset\)) and the independence complex of the direct sum of a free matroid on \(U\) and a uniform matroid of rank \(b-1\) on \(B\). In the remaining case \(a\ge2,b\ge1\), Step 2 gives facets of two distinct sizes; independence complexes of matroids have equicardinal bases, so these complexes cannot be matroidal. Combining all cases proves the matroidality criterion.

## Verification
A standalone Python 3 standard-library verifier is supplied as `verify.py`. It independently constructs the graph, checks all unordered pairs using shortest-path distances with and without forbidden internal vertices, exhaustively enumerates all subsets, and independently compares their face and facet polynomials with the formulas. It also checks basis exchange in the pure all-large-part cases, and computes reduced homology ranks over \(\mathbb F_2\) on small graphs.

Executing `python verify.py` produced:

```text
VERIFY_OK profiles=88 subsets=10764 facets=804 direct_BFS=PASS face_polynomials=PASS maximal_facets=PASS matroid_basis_exchange=5200 homology_mod2_cases=64 PASS
```

Finite computations corroborate the theorem, but do not establish its all-orders or integral homotopy claims. Those rely on the proof above, including the matroid shellability and suspension theorems.

## Relationship to prior work
Cicerone, Di Stefano, Klavžar and Yero introduced total mutual visibility in 2022. Kuziak and Rodríguez-Velázquez subsequently studied its scalar behavior under graph products. Bujtás, Klavžar and Tian's later paper proves a general distance-two common-neighbor test for total visibility (Theorem 5.2), which includes the feasibility test in Step 1 as a specialization, and gives the total visibility polynomial for balanced complete bipartite graphs (Proposition 3.2). Neither this general test nor the balanced bipartite polynomial is claimed independently new here.

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue developed the topology of cut complexes. Their two-cut complex, disjoint-union shellability theorem and general suspension gluing result cover the matroidal, no-singleton topology in Step 3 through an equivalent graph formulation and provide a standard suspension tool used in Step 4. The contribution assessed here is the **combined complete multipartite total-visibility complex classification**, the exact labelled face and facet polynomials for arbitrary part sizes, the sharp singleton-driven matroid/purity boundary, and the resulting nonpure integral sphere-wedge family. Prior general tools are explicitly acknowledged, rather than represented as new lemmas.

## Limitations
The statement applies to finite complete multipartite graphs with at least three parts; it does not assert equivalent properties for arbitrary graphs. The homotopy equivalence determines integral homotopy groups only to the extent implied by a sphere wedge; it does not supply a canonical equivariant decomposition or shelling of the nonpure cases. The mathematical novelty is conditional on the inspected primary literature and targeted searches; differently indexed or unpublished equivalent classifications remain possible. Independent mathematical audit has not been performed.

## References
1. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility in strong products of graphs via total mutual-visibility*, first public preprint 2022-10-14, https://arxiv.org/abs/2210.07835.
2. D. Kuziak, J. A. Rodríguez-Velázquez, *Total Mutual-Visibility in Graphs with Emphasis on Lexicographic and Cartesian Products*, https://arxiv.org/abs/2306.15818.
3. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, https://arxiv.org/abs/2412.03066, especially Proposition 3.2 and Theorem 5.2.
4. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, https://arxiv.org/abs/2304.13675, especially Section 4 and Proposition 4.15.
