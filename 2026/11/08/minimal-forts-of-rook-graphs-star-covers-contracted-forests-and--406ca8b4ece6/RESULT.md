# Minimal forts of rook graphs: star covers, contracted forests, and nonspanning cycles

## Finding
For every pair of integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\). A **fort** is a nonempty vertex subset \(F\) for which every vertex outside \(F\) has a number of neighbors in \(F\) different from one. Let \(\mathcal{F}_{m,n}(z)=\sum_{F\text{ inclusion-minimal fort}}z^{|F|}\).

Every inclusion-minimal fort corresponds, under the line-graph identification, to precisely one of the following edge sets \(H\) in the complete bipartite graph with left class \(A\) of size \(m\) and right class \(B\) of size \(n\):

1. A spanning star forest (with components being single edges or stars with at least two edges), except that an oriented forest consisting exclusively of stars centered in one class, all having at least two edges and at least one having three or more edges, is excluded.
2. An edge set covering all of \(B\) but not all of \(A\), such that every vertex of \(B\) has degree two in \(H\), and the multigraph on \(A\) obtained by replacing each \(B\)-vertex with an edge between its two neighbors is a forest. The transposed configurations are included.
3. A single simple even cycle, using at least two vertices of each class but not all vertices of both classes simultaneously.

The three families are disjoint and exhaust all inclusion-minimal forts. In family 2, parallel edges in the contracted multigraph are not allowed (they instead belong to family 3 as four-cycles).

An exact two-variable labeled generating function follows. Introduce formal variables \(x,y,z\), and define
\[
A=x(e^{yz}-1-yz),\quad B=y(e^{xz}-1-xz),\quad U=xyz^2,
\]
\[
T(x,y,z)=\sum_{k\ge2}\frac{k^{k-2}}{k!}x^k y^{k-1}z^{2k-2},\qquad
C(U)=\sum_{k\ge2}\frac{U^k}{2k}.
\]
Then, taking formal power-series coefficients,
\[
\boxed{\mathcal{F}_{m,n}(z)=m!n![x^m y^n]Q(x,y,z)}
\]
where
\[
\begin{aligned}
Q={}&\exp(xyz+A+B)-\bigl(e^A-e^{xy^2z^2/2}\bigr)-\bigl(e^B-e^{yx^2z^2/2}\bigr)\\
&+(e^x-1)(e^{T(x,y,z)}-1)+(e^y-1)(e^{T(y,x,z)}-1)\\
&+(e^{x+y}-1)C(U).
\end{aligned}
\]
All coefficients of \(\mathcal{F}_{m,n}\) are nonnegative integers, despite the subtraction in the expression for \(Q\).

A sharp thin-board specialization exhibits unbounded gaps: for every \(n\ge5\),
\[
\boxed{\mathcal{F}_{2,n}(z)=\left(6\binom n4+6\binom n3+\binom n2\right)z^4+2nz^n.}
\]
Thus the only inclusion-minimal fort cardinalities of \(R_{2,n}\) are \(4\) and \(n\). For \(n\ge6\), none of the \(n-5\) intervening cardinalities \(5,6,\ldots,n-1\) occurs.

## Assumptions and scope
All graphs are finite, simple, and undirected; \(m,n\ge2\) and board cells are labeled by pairs \((a,b)\in A\times B\). A fort is nonempty and is **inclusion-minimal** when it contains no proper nonempty fort; minimality is not merely a single-vertex deletion condition. The contracted multigraph in family 2 may in general carry parallel edges before testing whether it is a forest; a two-edge parallel cycle corresponds to a four-cycle of \(K_{m,n}\). Empty components and their labels are handled through the labeled exponential generating function.

## Proof
**Neighbor identity and degree criterion.** Write \(H\subseteq E(K_{m,n})\) for the selected edges. An unselected cell \((a,b)\) has precisely \(d_H(a)+d_H(b)\) selected neighbors, since its row and column selections are disjoint. Hence \(H\ne\varnothing\) represents a fort exactly when no unselected cell has one endpoint of degree zero and the other of degree one. Equivalently, with \(A_i=\{a:d_H(a)=i\}\) and \(B_i=\{b:d_H(b)=i\}\),
\[
A_0\ne\varnothing\implies B_1=\varnothing,\qquad B_0\ne\varnothing\implies A_1=\varnothing.
\]
(The zero/one combinations correspond to unselected cells automatically.) We split by whether the degree-zero sets are empty.

**Both classes fully covered.** Then every selected edge set is a fort. A minimal fort must therefore be a minimal edge cover. In any minimal edge cover each selected edge has a degree-one endpoint, since otherwise that edge can be removed while retaining a cover. Thus every component is a star, including the single-edge star. Conversely a spanning star forest is minimal as an edge cover; any proper subfort cannot still cover both classes.

Suppose a proper nonempty subset \(J\) of such a forest is a fort and no longer covers both classes. It cannot have an isolated vertex in each class: any remaining star edge would have a degree-one endpoint, contradicting the degree criterion. If \(J\) has an unused vertex of \(B\) but none of \(A\), every vertex of \(A\) must have degree at least two in \(J\); this forces all original star components to be centered in \(A\), each center of initial degree at least two. In this situation a proper fort exists if and only if at least one center initially had degree at least three: remove one of its leaf edges. If instead all centers had degree exactly two, removing any edge creates a degree-one \(A\)-vertex, so no proper fort exists. The transposed argument treats an unused vertex of \(A\). This proves family 1, including its precise exclusions.

**Exactly one class incompletely covered.** Suppose \(A_0\ne\varnothing\) and \(B_0=\varnothing\). Then the degree criterion gives \(d_H(b)\ge2\) for every \(b\in B\). If some degree exceeds two, deleting an incident edge still leaves every \(B\)-degree at least two, produces another fort, and contradicts minimality. Therefore each \(b\) has degree exactly two. Contract each \(b\) to an edge joining its two distinct neighbors in \(A\); the resulting labeled-edge multigraph \(M\) has \(n\) edges.

For a proper nonempty \(J\subset H\), if every vertex of \(B\) remains incident, all its degrees must still be at least two, forcing \(J=H\). Otherwise some vertex of \(B\) becomes isolated, and since \(A_0\ne\varnothing\) remains, the fort criterion forces every surviving degree in both classes to be at least two. In particular, each \(B\)-vertex has either zero or two incident selected edges, so \(J\) comes from a proper nonempty edge-submultigraph of \(M\) having no degree-one vertices. Every such multigraph contains a cycle; conversely any cycle of \(M\) gives a fort. Thus \(H\) is minimal precisely when \(M\) is a forest or when \(M\) itself is a single cycle. The cycle case, including two parallel edges (a four-cycle), is collected in family 3. Interchanging \(A,B\) gives family 2 in the other orientation.

**Both classes incompletely covered.** If \(A_0,B_0\ne\varnothing\), every nonisolated vertex of \(H\) has degree at least two. Any nonempty such bipartite graph contains a cycle, and the edges of any one cycle form a fort because the original unused vertices remain in both classes. Minimality therefore forces \(H\) to be exactly that cycle. Conversely a proper nonempty edge subset of a cycle has a degree-one vertex. If both classes have unused original vertices, the original isolated vertex opposite that degree-one vertex violates the fort criterion. If the cycle covers precisely one entire class, the contraction argument in the preceding paragraph applies: the corresponding multigraph is exactly one cycle and has no proper nonempty submultigraph of minimum positive degree at least two. Thus these cycles are minimal as well. A cycle covering both classes is not minimal because deleting one edge preserves coverage of both classes. Hence family 3 consists exactly of nonspanning (on the full bipartition) simple even cycles.

**Counting.** The exponential \(\exp(xyz+A+B)\) encodes spanning star forests: a single-edge component contributes \(xyz\), an \(A\)-centered \(k\)-edge star contributes \(xy^kz^k/k!\) for \(k\ge2\), and likewise on the other side. The excluded oriented star forests have EGFs \(e^A-e^{xy^2z^2/2}\) and \(e^B-e^{yx^2z^2/2}\).

For family 2, a tree component on \(k\ge2\) original \(A\)-vertices has \(k^{k-2}\) Cayley trees and \(k-1\) distinct degree-two \(B\)-vertices labeling its edges. Dividing by the two sets of vertex factorials gives the EGF term \(k^{k-2}x^k y^{k-1}z^{2k-2}/k!\). Disjoint union of tree components yields \(e^T\), and at least one isolated vertex of \(A\) contributes the factor \(e^x-1\). The term \(-1\) excludes the empty edge forest. The other orientation is symmetric.

A simple alternating cycle with \(k\ge2\) vertices of each class has \(k!(k-1)!/2\) labeled realizations on fixed labeled sets (also valid for \(k=2\)), so its bivariate EGF term is \((xyz^2)^k/(2k)\). A minimal cycle must leave at least one original vertex unused on either side, giving \(e^{x+y}-1\). Summing the disjoint families proves \(Q\) and the coefficient formula.

**Two-row corollary.** When \(m=2\) and \(n\ge5\), the spanning case consists of selecting one cell in one row and all \(n-1\) remaining columns in the other row, giving \(2n\) forts of size \(n\). Family 2 can only have all two row vertices degree two, with at least one unused column. The contracted graph on the columns has exactly two row-labeled edges, so it is either a path of length two, two disjoint edges, or a two-cycle of parallel edges. These contribute respectively \(6\binom n3\), \(6\binom n4\), and \(\binom n2\) minimal forts, each of size four. There are no further types, proving the formula and cardinality gap.

## Verification
The standalone `verify.py` constructs the rook-graph adjacency from row/column intersections and examines all nonempty subsets on thirteen labeled boards: \((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4)\). Proper-subset minimality is computed using a subset dynamic program independent of the proposed structural classification. A separate exact-rational bivariate labeled-component calculation independently computes all asserted coefficients. Every coefficient matches. It additionally verifies the two-row formula for \(5\le n\le20\) by exact symbolic component enumeration. The output is:

```
VERIFY_OK boards=13 examined_subsets=129155 forts=90253 minimal_forts=2165 coefficientwise=PASS thin_family_n5..20=PASS
```

For reference, \(\mathcal F_{2,5}(z)=100z^4+10z^5\), \(\mathcal F_{2,6}(z)=225z^4+12z^6\), and \(\mathcal F_{3,4}(z)=54z^4+12z^5+24z^6\). Finite tests support, but do not replace, the unrestricted proof above.

## Relationship to prior work
Becker, Cameron, Hanely, Ong, and Previte (arXiv:2404.05963, first public version dated 2024-04-09) study minimal-fort enumeration and general graph constructions. Their reported families and Section 5 constructions do not state this two-parameter rook-graph classification or the labeled counting series. Cameron, Hogben, Kenter, Mojallal, and Schuerger (arXiv:2310.17904, first public version dated 2023-10-27) develop fort hypergraphs and Cartesian-product bounds; those bounds alone do not determine every minimal fort of \(K_m\square K_n\). Mertens (arXiv:2401.00716) studies **ordinary dominating sets** on rook graphs, not forts, so its polynomial cannot be substituted for the fort enumerator. The rook graphs are also line graphs of complete bipartite graphs, whereas a minimal-fort classification for triangular graphs \(L(K_n)\) concerns a different root incidence structure and does not imply this result. Literature search is not a proof of global publication priority; differently named or unindexed equivalent results remain possible.

## Limitations
The result concerns standard forts and inclusion-minimality only, not the entire fort polynomial, the number of zero forcing sets, or their minimality profiles. No asymptotic claim beyond the explicitly proved unbounded two-row cardinality gaps is made. The independent literature comparison cannot guarantee absolute novelty. The finite verifier checks selected parameters only; generality follows from the structural proof.

## References
- P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1 (2024-04-09), https://arxiv.org/abs/2404.05963.
- T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1 (2023-10-27), https://arxiv.org/abs/2310.17904.
- S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (2024-01-01), https://arxiv.org/abs/2401.00716.
