# Edge-open-packing polynomials and the parity obstruction for rook graphs

## Finding

Let \(m,n\ge2\) be integers and let \(R_{m,n}=K_m\square K_n\) be the graph with cells \((r,c)\), where two distinct cells are adjacent exactly when they have the same row or the same column. An **edge-open packing** is an edge set \(B\) in which no distinct selected edges are joined by a third edge of the ambient graph. We include the empty set in the following enumerator, although some definitions require nonempty packings:

\[
E_{m,n}(z)=\sum_{B\text{ edge-open packing of }R_{m,n}}z^{|B|}.
\]

Every such \(B\) has a **unique** decomposition into components with mutually disjoint sets of used rows and mutually disjoint sets of used columns. The components are (H) a horizontal one-edge component using one row and two columns, (V) a vertical one-edge component using two rows and one column, and (L) an induced two-edge path with perpendicular edges using two rows and two columns. Conversely, every collection of these components with disjoint row and column supports gives an edge-open packing.

With \((a)_{\underline b}=a!/(a-b)!\) for \(0\le b\le a\), the complete polynomial is

\[
\boxed{E_{m,n}(z)=\sum_{\substack{h,v,\ell\ge0\\ h+2v+2\ell\le m\\2h+v+2\ell\le n}}
\frac{(m)_{\underline{h+2v+2\ell}}(n)_{\underline{2h+v+2\ell}}}{2^{h+v}h!v!\ell!}\,z^{h+v+2\ell}.}
\]

Equivalently, the *two-sort labelled* exponential generating function is

\[
\boxed{\sum_{m,n\ge0} E_{m,n}(z)\frac{x^m}{m!}\frac{y^n}{n!}
=\exp\left(x+y+\frac z2(xy^2+x^2y)+z^2x^2y^2\right).}
\]

For all \(m,n\ge2\), the maximum packing size is

\[
\boxed{\rho_e^o(R_{m,n})=\min(m,n)-\mathbf{1}_{\{m=n\text{ odd}\}}.}
\]

The count of maximum packings is also explicit. By symmetry assume \(m\le n\). When \(m<n\), it equals

\[
\boxed{m!\sum_{\substack{0\le h\le\min(m,n-m)\\h\equiv m\pmod 2}}
\frac{(n)_{\underline{m+h}}}{2^h h!\big((m-h)/2\big)!}.}
\]

When \(m=n=2q\), it equals \((m!)^2/q!\). When \(m=n=2q+1\) (so \(q\ge1\)), it equals

\[
\boxed{(m!)^2\left(\frac1{q!}+\frac1{4(q-1)!}\right).}
\]

For example, \(E_{3,4}(z)=1+30z+126z^2+72z^3\), while \(E_{3,3}(z)=1+18z+45z^2\). Thus the odd square board has a genuine one-edge deficit.

## Assumptions and scope

All graphs are finite, simple, and undirected. Rows and columns, hence graph vertices and graph edges, are labelled. The sum distinguishes edge subsets of the same graph, without quotienting by row/column symmetries. An edge joining endpoints of two selected edges must be *distinct* from those two selected edges. The zero-edge set contributes the constant coefficient \(1\). The analytic generating function identity may be extended formally to \(m,n\ge0\) using the same labelled-component definition, while the extremal theorem is stated for \(m,n\ge2\).

## Proof

**1. All components are H, V, or L.** Take an edge-open packing \(B\). If two selected edges share a cell and lie in the same row, then their two other endpoints are adjacent, and that third horizontal edge is forbidden. The same holds for two selected vertical edges in one column. Thus any two distinct selected edges sharing an endpoint must be perpendicular. If three selected edges were in one connected component of the selected-edge subgraph, either two would be parallel at a common endpoint, or the three would contain a selected length-three edge walk whose middle edge is a forbidden third edge joining the first and third selected edges. Hence each nontrivial component consists of just one selected edge (H or V) or two perpendicular selected edges sharing a pivot (L).

The endpoints of an L are three cells in a \(2\)-by-\(2\) rectangle; the two nonpivot cells are diagonally opposite and nonadjacent. Thus an L is induced. Endpoints of distinct selected components cannot be adjacent, since that ambient edge would join a selected edge of one component to a selected edge of the other and be a forbidden third edge. In a rook graph any shared row or shared column would create such an adjacency. Consequently the component supports are pairwise disjoint both in rows and in columns. Conversely, two edges within an L have no forbidden third edge, and components using disjoint rows and columns have no cross-component adjacency. This proves necessity, sufficiency, and uniqueness of the structural decomposition.

**2. Counting labelled blocks.** Suppose \(h\) components are H, \(v\) are V, and \(\ell\) are L. They use \(a=h+2v+2\ell\) distinct rows and \(b=2h+v+2\ell\) distinct columns, and contain \(t=h+v+2\ell\) selected edges. To form labelled components, use ordered allocations of \(a\) rows and \(b\) columns, divide by permutations of the \(h,v,\ell\) indistinguishable components, and divide by the internal swaps of the two columns of each H, the two rows of each V, and both pairs of an L. Each L has four possible pivots, canceling its four internal swaps. The resulting count is exactly

\[
\frac{(m)_{\underline a}(n)_{\underline b}}{2^{h+v}h!v!\ell!}.
\]

Summing over the feasible nonnegative integers proves the displayed polynomial. Equivalently, one unused row contributes \(x\), one unused column \(y\), H contributes \(zxy^2/2\), V contributes \(zx^2y/2\), and L contributes \(z^2x^2y^2\) to a two-sort labelled set construction. The exponential formula gives the bivariate generating function.

**3. The sharp maximum.** For each collection of types \((h,v,\ell)\), its number \(t\) of selected edges and row/column supports satisfy

\[
a=t+v\le m,\qquad b=t+h\le n.\]

Therefore \(t\le\min(m,n)\). Assume \(m\le n\). If \(m\) is even, \(m/2\) disjoint L components give \(t=m\). If \(m\) is odd and \(n\ge m+1\), take \((m-1)/2\) disjoint L components and one H component: this uses \(m\) rows and \(m+1\) columns and gives \(t=m\). If \(m=n\) is odd and \(t=m\), the equalities force \(h=v=0\), whence \(m=2\ell\), impossible. But \((m-1)/2\) L components give \(t=m-1\). Symmetry proves the full extremal formula.

**4. Exactly counting the maximum packings.** If \(m<n\) and \(t=m\), equality \(a=t+v=m\) forces \(v=0\). Therefore \(h+2\ell=m\), with \(h\le n-m\); substitution into the coefficient formula gives the first displayed maximum-multiplicity sum. If \(m=n\) is even and \(t=m\), both \(h\) and \(v\) vanish, giving \(\ell=m/2\) and \((m!)^2/(m/2)!\) configurations. If \(m=n=2q+1\) and \(t=m-1\), the support inequalities give \(h,v\le1\), while \(h+v+2\ell=m-1\) is even. The only possibilities are \((h,v,\ell)=(0,0,q)\) and \((1,1,q-1)\). Applying the coefficient formula to these two mutually exclusive types gives the last multiplicity formula. This completes the proof.

## Verification

The accompanying `verify.py` independently constructs rook-graph edges and tests every pair of selected edges using the literal forbidden-**third**-edge relation. It enumerates all compatible edge families recursively, without using the structural decomposition, then compares their full size distributions against the factorial formula. It also checks the maximum and maximum-multiplicity formulas. The recorded reproducible command is `python3 verify.py`.

The executed checker returned `VERIFY_OK`: all coefficients agreed for the 15 unordered parameter pairs with \(2\le m\le n\le6\), involving \(852443\) distinct compatible edge sets in aggregate. Another \(261\) parameter profiles with \(2\le m\le19\) and \(m\le n\le24\) satisfied the extremal identities using exact integer arithmetic. These finite checks corroborate, rather than replace, the unrestricted proof.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan introduced edge-open packing and determined the parameter for paths, cycles, complete multipartite graphs and other families; their observation that selected edges induce a union of stars is used as background, but does not supply an enumeration for rook graphs [1]. Brešar and Samadi analyzed complexity and general bounds, including the link to injective edge coloring [2]. Brešar, Dravec, Hedžet and Samadi investigated edge-open packing in graph products and established general Cartesian-product bounds in their Section 5 [3]. Those inequalities do not specify the exact count of *every* edge-open packing of \(K_m\square K_n\), nor the parity-dependent sharp optimum and its multiplicity. The current proof is a product-specific classification and two-sort labelled enumeration; it makes no claim of inventing the underlying star-forest characterization or general product-bound framework.

A related article by Priyamvada and Panda studies injective edge-coloring bounds for graph products [4]. An injective edge coloring partitions the ambient edge set into edge-open packings, but an upper bound on its number of colors does not determine the number of possible individual color classes. Only this paper's accessible abstract and bibliographic description were available; its full text was not inspected, so any further overlap remains a specific uncertainty.

## Limitations

The formula concerns labelled, two-dimensional rook graphs and the standard edge-open-packing definition. It does not give the injective edge chromatic index, a count of full injective edge colorings, or an analogous formula for higher-dimensional Hamming graphs. The polynomial includes the empty set by convention. The novelty comparison is limited to the identified literature and accessible research records; equivalent results under induced-star-forest, injective edge-color-class or line-graph terminology might have escaped indexing. No independent mathematical audit is claimed.

## References

[1] G. Chelladurai, K. Kalimuthu, S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776. https://doi.org/10.1051/ro/2022171 . Open text: https://www.numdam.org/item/10.1051/ro/2022171.pdf .

[2] B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1, first public 2024-03-01. https://arxiv.org/abs/2403.00750 .

[3] B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020, first public 2024-06-06. https://arxiv.org/abs/2406.04020 .

[4] Priyamvada and B. S. Panda, *Injective edge coloring of some standard graph products*, Discrete Mathematics, Algorithms and Applications **16** (2024), article 2350041. https://doi.org/10.1142/S1793830923500416 .
