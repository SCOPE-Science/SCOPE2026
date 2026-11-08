# Component decomposition of full strong Morse complexes of complete multipartite graphs

## Finding
Let \(t\ge3\), and let \(G=K_{n_1,\ldots,n_t}\) be a complete multipartite graph with all \(n_i\ge2\). Regard \(G\) as an **unfilled one-dimensional simplicial complex**. Its full strong discrete-Morse matching complex satisfies an *exact simplicial decomposition*
\[
\mathcal{SM}(G)=\coprod_{1\le i<j\le t}\mathcal{SM}(K_{n_i,n_j}),
\]
where the pairwise strong complexes are embedded using directed graph edges with endpoints in their two parts, and the symbol on the right denotes disjoint union of geometric realizations (their abstract complexes share only the obligatory empty face).

Every pair component has the homotopy type
\[
\mathcal{SM}(K_{n_i,n_j})\simeq\bigvee^{2n_i n_j-n_i-n_j+1}S^1.
\]
In particular, the *connected* original graph \(G\) yields a **disconnected** strong matching complex with exactly \(\binom t2\) components. Its full integral reduced homology is
\[
\widetilde H_0\cong\mathbb Z^{\binom t2-1},\qquad H_1\cong\bigoplus_{i<j}\mathbb Z^{2n_i n_j-n_i-n_j+1},\qquad\widetilde H_k=0\ (k\ge2).
\]
If \(\mathcal P\) denotes the set of intrinsic multipartition classes, the natural graph-automorphism representation on zero-dimensional reduced integral homology is canonically
\[
\widetilde H_0\cong\ker\!\left(\mathbb Z\left[\binom{\mathcal P}{2}\right]\overset{\varepsilon}{\longrightarrow}\mathbb Z\right).
\]
It is a permutation augmentation lattice even when equal-sized parts can be exchanged.

## Assumptions and scope
A strong gradient is obtained from a total order on graph vertices as follows: a vertex \(v\) is matched to the edge \(\{u,v\}\) when it has *exactly one* earlier graph neighbor \(u\). Represent the matching pair by the directed arc \(v\to u\). The vertices of \(\mathcal{SM}(G)\) are these possible arcs, and all subsets of gradients over all vertex orders are faces. The graph is not completed to a higher-dimensional clique complex. The parameters are integers satisfying \(t\ge3\) and \(n_i\ge2\) for every part. No uniform upper bound is imposed.

## Proof
**First-two-part support lemma.** Let \(P_i\) be the vertex parts, and fix a total order \(\pi\). Let \(P_a\) contain its first vertex and \(P_b\) the first later vertex outside \(P_a\). Each vertex appearing before this first \(P_b\)-vertex has no earlier neighbors (all those vertices lie in \(P_a\)). Any vertex in a third part \(P_c\) appearing after that point has at least two earlier neighbors, one from \(P_a\) and one from \(P_b\), hence cannot be matched. Moreover, after the first \(P_c\)-vertex, a later vertex from \(P_a\) has at least two earlier neighbors from \(P_b\) and \(P_c\); a later vertex from \(P_b\) has two from \(P_a\) and \(P_c\). Thus every arc in the strong gradient has endpoints in the pair of parts \(P_a,P_b\). This remains true when one of the parts contributes only its first vertex before the other occurs, and when the gradient is empty.

**Conversely every pair gradient occurs.** Fix distinct classes \(P_i,P_j\), and take an arbitrary total order on their union. Extend it to a total order on all vertices by placing every other class afterward. Since both pair sizes are at least two, every vertex in a later class has at least four earlier graph neighbors and contributes no pair. The original gradients from the two classes are unchanged. Consequently the generated face sets agree **exactly**, pair by pair. Different unordered pairs have disjoint directed-arc vertex sets, so the geometric realization is a disjoint union and no face mixes parts belonging to different pairs.

**Homotopy of each pair component.** Here is an explicit argument requiring only \(m,n\ge2\). For classes \(A,B\) of sizes \(m,n\), define the target stars \(S_a=\{b\to a:b\in B\}\) and \(S_b=\{a\to b:a\in A\}\). Every generating gradient is contained in one of these target stars or in a *flap* \(F^A_{a,b}=\{b\to a\}\cup\{a'\to b:a'\in A\setminus\{a\}\}\) or \(F^B_{a,b}=\{a\to b\}\cup\{b'\to a:b'\in B\setminus\{b\}\}\). Indeed, in an ordering the only possible targets are the first vertices of the opposite classes. If both directions appear, the first two distinguished vertices supply the unique arrow in one direction, and the other arrows must come from later vertices in the opposite class before its second vertex appears. Conversely each listed simplex occurs by choosing the corresponding order.

Each flap \(F=\{q\}*T\) has \(T\) a nonempty face of the target star at its other endpoint. Choose \(p\in T\); in descending face size pair off mixed faces \(\{q\}\cup U\) with \(\{q,p\}\cup U\) for all nonempty \(U\subseteq T\setminus\{p\}\). These are elementary simplicial collapses: a mixed face is contained in only one flap, and larger possible cofaces are removed first. This retains the edge \(\{q,p\}\), and preserves all star simplices. Across all flaps, the result is the disjoint collection of \(m+n\) contractible full star simplices joined by two distinct bridge edges per original edge of \(K_{m,n}\). Collapsing each star to a vertex by homotopy equivalence yields the connected multigraph formed by doubling every edge of \(K_{m,n}\). Its cycle rank is \(2mn-(m+n)+1\); therefore the claimed pair-component circle wedge follows integrally.

**Homology and action.** Taking homology of the finite disjoint union gives the asserted integral groups and their vanishing in other dimensions. Graph automorphisms preserve the equivalence relation of being nonadjacent and hence permute the intrinsic part classes, and consequently permute the unordered pairs indexing the connected components. The reduced zero-dimensional cellular chain group is exactly the augmentation kernel of the integral permutation lattice on these components, establishing the displayed equivariant statement.

## Verification
Run `python3 verify.py` with standard Python 3. The standalone program independently enumerates every vertex ordering and all generated gradient faces for the five multipartition-size tuples \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((2,2,2,2)\), and \((3,3,3)\). It separately generates every pairwise star and flap face, asserts exact equality of face sets, checks every generating gradient involves at most one unordered part pair, and verifies that connected-component counts and combinatorial Euler ranks match the claimed formulas. The largest case has \(362{,}880\) orders. The exact output is recorded in `verify_output.txt`. These finite checks do not establish the unrestricted statement; the symbolic support lemma and pairwise collapse above do.

## Relationship to prior work
Knudson and Owens-White (2026) introduce full and pure strong discrete-Morse matching complexes and state classifications for paths, stars, simplices, simplex boundaries and certain cycle complexes. Fernández (2025) establishes the underlying descending-dominance framework and its relation to discrete Morse theory. A previously obtained complete-bipartite strong-complex circle-wedge formula supplies the local model: **its application alone does not imply the multipartite result**, because the exact first-two-part support lemma is additionally needed. The new conclusion is the global component decomposition and resulting disconnectedness and integral zero-dimensional symmetry module, rather than a new computation of bipartite pieces. Ordinary discrete-Morse matching complexes and pure strong complexes are different objects and their published calculations do not imply this exact decomposition.

## Limitations
All part sizes must be at least two. The statement does not address complete multipartite graphs with singleton classes, the pure strong complex, or the ordinary discrete-Morse matching complex. The integral action on positive-dimensional homology is not explicitly decomposed into irreducible representations. The most closely related 2026 preprint was accessible through its dated indexed abstract but not as complete manuscript text for a line-by-line originality comparison. Exact equivalent work in inaccessible or unindexed sources remains a possibility. No independent mathematical validation is claimed.

## References
1. K. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844 (public 2026-09-06), https://arxiv.org/abs/2609.06844.
2. X. L. Fernández, *Strong discrete Morse theory*, arXiv:2504.15729 (public 2025-04-22), https://arxiv.org/abs/2504.15729; full published text at https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/strong-discrete-morse-theory/DD4EB8F8EF04FF8A5CE06F5F58DD7532.
