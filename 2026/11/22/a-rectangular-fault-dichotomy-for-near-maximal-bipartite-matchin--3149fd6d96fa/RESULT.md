# A rectangular-fault dichotomy for near-maximal bipartite matching complexes

## Finding
Fix any integer \(n\ge2\). Label the edges of the balanced complete bipartite graph \(K_{n,n}\) by \((i,j)\), with \(i,j\in[n]\). For every **nonempty proper** edge-fault set \(F\subsetneq[n]\times[n]\), let \(R\) and \(C\) be, respectively, its sets of row and column endpoints. Let \(X_F=M_{n-1}(K_{n,n}-F)\), where a simplex is a selection of *remaining* edges of maximum selected degree at most \(n-1\).

**Theorem (all fault arrangements).** The space \(|X_F|\) is noncontractible precisely when the fault set fills its entire row-column bounding rectangle, \(F=R\times C\). In that case it is an integral homotopy sphere:
\[
|X_F|\simeq S^{d},\qquad
 d=n^2-|R||C|-2n+|R|+|C|-1
   =(n-1)^2-1-(|R|-1)(|C|-1).
\]
When \(F\subsetneq R\times C\), the abstract complex \(X_F\) is a **simplicial cone**, hence contractible. In particular, all nonempty proper rectangular faults have exactly one integral reduced homology generator in degree \(d\) and no other reduced homology, while every nonrectangular fault has zero reduced homology in every degree.

For example, removal of two edges sharing a vertex preserves the sphere dimension of the intact complex, whereas removal of two vertex-disjoint edges yields a cone. Rectangles of size \(a\times b\) lower the sphere dimension by exactly \((a-1)(b-1)\).

## Assumptions and scope
The graph is finite, simple, undirected, and bipartite. Degree refers to degree in the **selected** edge subset of the surviving graph, not the faulted graph's own degree. The parameter is fixed at \(n-1\), regardless of how many edges were removed. All cases with \(1\le |F|\le n^2-1\) are covered, including faults meeting every row, every column, or both except that the completely deleted graph is excluded. The geometric realization is interpreted in the ordinary way, and all homotopy equivalences are nonequivariant. The formula \(S^0\) has its usual two-component meaning.

## Proof
**1. Describe all minimal forbidden faces.** An intact row (respectively, column) is a row (respectively, column) meeting no deleted edge. Exactly the rows outside \(R\) and columns outside \(C\) remain intact. In the surviving graph, each intact vertex has exactly \(n\) incident edges, while each vertex meeting a fault has degree at most \(n-1\). Therefore a selected edge set violates the matching-degree constraint precisely when it contains the full \(n\)-element star of an intact row or intact column. Write \(S_v\) for these \(t=2n-|R|-|C|\) stars. They are the only minimal nonfaces of \(X_F\).

**2. A missing entry inside the bounding rectangle makes a cone.** Since \(F\subseteq R\times C\) by definition, nonrectangular means there exists \(e=(i,j)\in(R\times C)\setminus F\). Both endpoints of \(e\) have already lost an edge, so neither is an intact vertex. Thus \(e\) lies in none of the forbidden stars \(S_v\). For every simplex \(\sigma\) the union \(\sigma\cup\{e\}\) is still a simplex. The edge-vertex \(e\) is a cone apex, proving contractibility.

**3. A private-element suspension lemma.** Let a finite simplicial complex \(K\) on ground set \(E\) have precisely the forbidden sets \(S_1,\ldots,S_t\), with \(t\ge1\). Suppose each \(S_i\) contains a distinct private element \(p_i\), contained in no other \(S_j\), and every element of \(E\) belongs to at least one forbidden set. Put \(Q=E\setminus\{p_1,\ldots,p_t\}\) and \(m=|Q|\ge1\). Then
\[
|K|\simeq S^{m-1}.
\]
To prove this, pick \(q\in Q\) and choose a forbidden set \(S_i\) containing \(q\). In the deletion of the simplicial vertex \(q\), the set \(S_i\) can no longer be contained in any face. Because \(p_i\) occurs in no other forbidden set, \(p_i\) is a cone apex of this deletion. The link of \(q\) is defined by the forbidden sets \(S_j\setminus\{q\}\) for all \(j\); their private elements \(p_j\) survive, and their union still contains every surviving element of \(Q\setminus\{q\}\). The vertex-star decomposition \(K=(K\setminus q)\cup(q*\operatorname{lk}_K(q))\), with contractible deletion and contractible star, therefore gives \(|K|\simeq\Sigma|\operatorname{lk}_K(q)|\). Repeat this argument in the links for all \(m\) elements of \(Q\). At the end, the forbidden singletons \(\{p_i\}\) leave only the empty face, representing the usual augmented \((-1)\)-sphere. Each step suspends once, yielding an ordinary \((m-1)\)-sphere. The argument is also valid when \(m=1\): the link has only the empty face and the original complex has two contractible components.

**4. Apply the lemma to full rectangles.** Suppose \(F=R\times C\), with both \(R\) and \(C\) nonempty and \(|F|<n^2\). There is at least one intact row or column, so \(t=2n-|R|-|C|\ge1\). The number of surviving edge-vertices is \(N=n^2-|R||C|\). Choose any \(r_0\in R\) and \(c_0\in C\). For every intact row \(i\notin R\), the surviving edge \((i,c_0)\) belongs to its intact-row star, but not to any intact-column star, and is therefore private. For every intact column \(j\notin C\), the edge \((r_0,j)\) is private to its intact-column star. These \(t\) private edges are distinct. Every surviving edge has at least one endpoint outside \(R\) or outside \(C\), since all of \(R\times C\) was deleted; hence every surviving edge lies in at least one of these stars. The lemma applies with \(m=N-t\). It remains to verify \(m\ge1\): each intact vertex has an \(n\)-edge star, and at most one of its edges is private, so there is at least one nonprivate edge for \(n\ge2\). Consequently \(|X_F|\simeq S^{N-t-1}\), and substitution gives both stated formulas for \(d\). This proves all quantifiers and boundary cases.

## Verification
The standalone standard-library script `verify_rectangular.py` independently builds the full face sets from the original degree constraints. It enumerates every nonempty proper fault subset for \(n=2\) and \(n=3\) (14 and 510 faults), checks that the cone witness or the private-star hypotheses are valid, and computes every reduced mod-two Betti number by exact augmented boundary-matrix elimination. It separately checks all 15 proper size pairs of rectangular faults for \(n=4\) using one canonical labeled representative of each size. Results agree with the theorem: 8 spherical and 6 conical instances for \(n=2\), and 48 spherical and 462 conical instances for \(n=3\). Run with `python3 verify_rectangular.py`. The computations are exhaustive only for the stated finite collections; the unrestricted integral homotopy claim is established by the proof rather than those computations.

## Relationship to prior work
Singh's Theorem 4.2 determines the homotopy sphere \(|M_{n-1}(K_{n,n})|\simeq S^{(n-1)^2-1}\) **with no faults**. The present statement uses his parameter and object but classifies *all nonempty proper edge-removal patterns* and proves a sharp rectangular-versus-conical dichotomy, which the intact theorem does not entail. The prior complete-bipartite fixed-point and orientation-character result concerns the intact complex's action, not edge deletions. The separately published rectangular-fault result on robust **vertex** clique-avoidance complexes uses a different face ground set and a different forbidden-set condition; it does not imply the theorem above for edge-set matching complexes.

## Limitations
The fault set is nonempty and proper; no assertion is made about the geometric realization of the complex \(\{\varnothing\}\) for the empty surviving graph. The theorem fixes degree threshold \(n-1\), and does not extend to other thresholds or general bipartite host graphs. It gives homotopy types and integral homology groups but does not determine natural inclusion maps for distinct fault sets, equivariant homotopy types, or a complete persistence module. Novelty remains subject to literature not found or indexed in the compared sources.

## References
1. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first public version 2020-06-24; Theorem 1.2(2), Theorem 4.2 and §4. https://arxiv.org/abs/2006.13632
2. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154. General bounded-degree framework, not an edge-fault homotopy classification.
