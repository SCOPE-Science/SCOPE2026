# Induced-isolate inclusion–exclusion for every inclusion-minimal strong total cover

## Finding

Let \(G=(V,E)\) be any finite simple graph, with \(n=|V|\geq1\). A strong total cover selects vertices and edges: each vertex must be selected or incident with a selected edge, and each edge must be selected or have a selected endpoint. A cover is *inclusion-minimal* when deleting any one selected element destroys coverage.

For \(W\subseteq V\), write \(U=V\setminus W\), \(e(W)=|E(G[W])|\), and
\[
I(W)=\{w\in W:N_G(w)\cap W=\varnothing\}.
\]
For every \(w\in I(W)\), put \(d_W(w)=|N_G(w)\cap U|\). Define the receiver candidates
\[
R(W)=\{u\in U:0<|N_G(u)\cap W|\text{ and }N_G(u)\cap W\subseteq I(W)\}.
\]
For \(S\subseteq R(W)\), write \(B_u=N_G(u)\cap W\) and \(B(S)=\bigcup_{u\in S}B_u\). The coefficient
\[
c_G(W)=\sum_{\substack{S\subseteq R(W)\\ B_u\cap B_v=\varnothing\ (u\ne v\in S)}}
(-1)^{|S|}\prod_{w\in I(W)\setminus B(S)}d_W(w)
\]
counts inclusion-minimal covers whose omitted original vertices are exactly \(W\). Thus their complete cardinality polynomial is
\[
\boxed{\mathcal M_G(z)=\sum_{W\subseteq V}c_G(W)\,z^{\,n-|W|+e(W)+|I(W)|}.}
\]
The formula is valid for disconnected graphs and isolated vertices, using the empty-product convention \(1\). It evaluates by at most \(3^n\) induced-subset/receiver-candidate terms and polynomial work per term (with integer arithmetic).

In addition, every inclusion-minimal cover has a unique form
\[
C(W,f)=(V\setminus W)\;\cup\;E(G[W])\;\cup\;\{\{w,f(w)\}:w\in I(W)\},
\]
where \(f:I(W)\to V\setminus W\) satisfies \(f(w)\in N_G(w)\) and, for each \(u\in f(I(W))\), there exists \(w\in N_G(u)\cap W\) such that either \(w\notin I(W)\) or \(f(w)\ne u\). The polynomial and unique normal form are a single enumeration theorem, not assertions of computational tractability in input size.

## Assumptions and scope

All graphs are finite, simple, labelled on their vertex sets, and have at least one vertex. Different choices of \(f\) are counted as different covers precisely when their selected edges differ. Inclusion-minimality, not cardinality optimality, is required. A graph may have isolated vertices; if \(W\) contains any such vertex, its contribution is automatically zero. A sum over no candidates contains its empty term, and an empty product equals one.

## Proof

Fix a cover \(C=X\cup Y\) with selected vertices \(X\subseteq V\) and edges \(Y\subseteq E\), and put \(W=V\setminus X\), \(U=X\). Every edge with both endpoints in \(W\) must belong to \(Y\), since it has no selected endpoint. These are precisely \(E(G[W])\).

Every \(w\in W\setminus I(W)\) is already covered by an edge of \(E(G[W])\). Therefore any selected edge meeting this \(w\) and meeting \(U\) is removable: it is unnecessary for the endpoint \(w\), while its endpoint in \(U\) is already selected and covers the edge itself. Likewise no edge internal to \(U\) can be selected in an inclusion-minimal cover, since both endpoints are already selected. The only additional potentially essential edges lie between \(I(W)\) and \(U\).

An isolated-in-\(G[W]\) vertex \(w\) has no selected endpoint status and no forced edge to another omitted vertex. At least one of its edges to \(U\) must therefore be selected to cover \(w\); more than one would make each redundant. Such a vertex has exactly one selected cross edge, \(\{w,f(w)\}\), with \(f(w)\in N_G(w)\cap U\). These selected cross edges each have the private coverage witness \(w\), and each edge of \(E(G[W])\) is essential because neither endpoint is selected. This proves uniqueness of the edge part given \((W,f)\).

It remains to check essentiality of each selected vertex \(u\in U\). If \(u\notin f(I(W))\), then it is not incident with any selected cross edge, so deleting it leaves \(u\) uncovered. If \(u\in f(I(W))\), deleting it preserves coverage of every original vertex, because \(u\) remains incident to a chosen edge, but it will uncover an edge precisely when there is a cross edge \(\{u,w\}\) to some \(w\in W\) which is *not* selected. This happens exactly when \(w\notin I(W)\) or \(f(w)\ne u\). Thus the displayed receiver essentiality condition is both necessary and sufficient. Each selected element is now known to have a private coverage witness, proving the normal form.

The number of selected elements in every \(C(W,f)\) is \(n-|W|+e(W)+|I(W)|\), independent of \(f\). To count admissible \(f\), begin with the \(\prod_{w\in I(W)}d_W(w)\) possible assignments. A selected receiver \(u\) violates essentiality only if it has no non-isolated-in-\(G[W]\) neighbor among \(W\), and every neighbor in \(W\) is an isolated vertex assigned to \(u\). Thus only \(u\in R(W)\) can be bad, with bad event \(A_u=\{f(w)=u\text{ for every }w\in B_u\}\). Each \(B_u\) is nonempty. For a family \(S\) of bad events, \(\bigcap_{u\in S}A_u\) is impossible unless the nonempty \(B_u\) are pairwise disjoint; otherwise one \(w\) would have two different assigned receivers. If disjoint, the assignments of all vertices of \(B(S)\) are forced and every remaining isolated \(w\) has \(d_W(w)\) choices. Inclusion–exclusion gives exactly \(c_G(W)\). Summing over the unique omitted sets \(W\) proves the polynomial.

There are at most \(\sum_{W\subseteq V}2^{n-|W|}=3^n\) choices of \((W,S)\), with each summand evaluable from the adjacency relation by polynomially many elementary operations; this establishes the stated arithmetic complexity bound. No complexity claim beyond this bound is made.

## Verification

The accompanying `verify.py` independently enumerates *all* subsets of \(V\cup E\), applies the two original coverage clauses, and tests inclusion-minimality by deleting each selected element. This direct oracle was compared to both the receiver-map construction and the inclusion–exclusion expression for all 75 labelled graphs of orders one through four, 24 deterministic five-vertex examples, twelve deterministic six-vertex examples, and complete and path graphs of orders five and six. All 115 comparisons agreed.

The formula alone was also evaluated for a six-cycle, a seven-cycle, and the complete graph on eight vertices. Run `python3 verify.py` to reproduce the tests. The finite experiments support the proof but are not its substitute; exhaustive graph enumeration stops at order four.

## Relationship to prior work

Aprile and Ferrarini introduced strong total covering and proved its exact equivalence with domination in the incidence graph, plus an optimum-cardinality identity involving induced matchings. Those results supply the optimization/duality context but do not state the explicit induced-isolate normal form or inclusion–exclusion polynomial for *all inclusion-minimal* covers. Earlier work by Castelo, Defrain, and Gomes concerns enumeration algorithms for minimal dominating sets in *chordal bipartite* graphs; an arbitrary graph's incidence graph need not be chordal bipartite. The general private-neighbor criterion for minimal domination motivates the essentiality test but does not itself provide the original-vertex induced-isolate coefficient formula without the structural analysis above.

## Limitations

The \(3^n\) bound is an arithmetic-operation upper bound, not a polynomial-time algorithm. It can be slower than specialized methods. Generic minimal-domination theory provides related characterizations, so independent priority checking of the specific explicit formula remains important. Earlier public conference material announced the strong-total-cover definition; its exact public posting date could not be established. This work neither claims an independent audit nor a general output-polynomial enumeration algorithm.

## References

1. M. Aprile and L. Ferrarini, *The Strong Total Cover Problem*, arXiv:2610.23312v1, 16 October 2026. https://arxiv.org/html/2610.23312v1
2. E. Castelo, O. Defrain and G. C. M. Gomes, *Enumerating Minimal Dominating Sets and Variants in Chordal Bipartite Graphs*, arXiv:2502.14611, 2025. https://arxiv.org/abs/2502.14611
3. *Strong Total Cover and Mixed Dominating Set Problems: Polyhedra and Algorithms*, PGMODAYS 2025 conference program, 19 November 2025. https://easychair.org/smart-program/PGMODAYS2025/2025-11-19.html
