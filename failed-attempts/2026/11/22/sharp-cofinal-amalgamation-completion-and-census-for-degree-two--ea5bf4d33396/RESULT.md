# Sharp cofinal-amalgamation completion and census for degree-two graphs

## Finding

Let \(\mathcal K_2\) be the age of all finite simple undirected graphs of maximum degree at most two, with **induced-subgraph embeddings**. A finite member \(A\) is an amalgamation base in \(\mathcal K_2\) if and only if each of its components is a cycle (allowing the empty union). Thus \(\mathcal K_2\) has the cofinal amalgamation property but not the amalgamation property.

Write \(k\) for the number of path components with at least two vertices and \(i\) for the number of isolated vertices of \(A\). Let \(\mu(A)\) be the least number of *new* vertices in an induced extension of \(A\) that is an amalgamation base. Then

\[
\mu(A)=\begin{cases}
0,&k=i=0,\\
2,&k=0,\ i=1,\\
k+i,&\text{otherwise}.
\end{cases}
\]

This bound is attained with no new components except cycles containing the original path components. A complete, exact census is available at this minimum. Let \(r=k+i\). In the nonexceptional case \(r\ge1\), fix distinct labels for the \(r\) new vertices, fix every original vertex and edge, and count extensions as distinct labelled graphs. Put \(s=2k+i\) and set \(d_a=1\) on the \(2k\) old path endpoints and \(d_a=2\) on the \(i\) old isolated vertices. The exact number \(T_{k,i}\) of minimum-size amalgamation-base extensions is

\[
T_{k,i}= [x_1^{d_1}\cdots x_s^{d_s}]\left(\sum_{1\le a<b\le s}x_ax_b\right)^r.
\]

The cases \(r=0\) and \((k,i)=(0,1)\) each have one labelled optimum. The coefficient depends on the multiset of deficits, not the individual nontrivial path lengths. For example, \(T_{2,0}=6\), \(T_{1,1}=2\), and \(T_{0,3}=6\).

The associated countable cofinal Fraïssé limit is the disjoint union of countably many cycles of *each* finite length at least three, and is computably categorical.

## Assumptions and scope

An induced embedding preserves adjacency and nonadjacency on the embedded vertex set. A *span* consists of induced embeddings of a finite base into two graphs in \(\mathcal K_2\). An *amalgam* is a graph in \(\mathcal K_2\) admitting compatible induced embeddings of both legs; these embeddings may identify additional vertices outside the base. An *amalgamation base* has an amalgam for every span rooted at it. Cofinal amalgamation means that every member induced-embeds in some amalgamation base. All graphs considered are finite unless the countable limit is explicitly mentioned. The ambient language is a single symmetric irreflexive adjacency relation.

The completion census fixes the original labelled graph, uses a prescribed set of distinctly labelled new vertices, and counts graphs, not isomorphism types or embeddings. Existing old-old nonedges remain nonedges; no loops or multiedges are allowed. When \(s=0\), the coefficient formula is not invoked.

## Proof

**1. Characterization of amalgamation bases.** If \(A\) is a union of cycles, each original vertex has both available degree slots occupied. An induced supergraph therefore contains each component of \(A\) as an unchanged whole connected component. Given any two induced extensions of \(A\), identify exactly the copies of \(A\) and freely unite the remaining components: the resulting graph still has maximum degree two and is an amalgam.

Conversely, suppose \(A\) has a path component on \(h\ge2\) vertices. It extends inducedly to a cycle of length \(h+1\) (by adjoining one vertex connected to both endpoints), and also to a cycle of length \(h+2\) (by adjoining two vertices joined in a path between the endpoints). Leave the other components unchanged in both extensions. In every graph of maximum degree two, an embedded saturated cycle is a whole connected component; these two incompatible cycle lengths cannot both be the connected component containing the fixed old path, so no amalgam exists. If \(A\) contains an isolated vertex, instead complete it to a triangle and a quadrilateral in the two extensions. The same obstruction applies. Hence all and only unions of cycles are amalgamation bases.

**2. Sharp size of a cofinal completion.** Every old nontrivial path endpoint requires one additional incident edge; every old isolated vertex requires two. Exactly \(2k+2i=2r\) incidences are missing at old vertices. Since the induced copy of \(A\) cannot gain old-old edges, all missing incidences must be supplied by edges from old to new vertices. Each new vertex can support at most two such incidences. Therefore every two-regular induced extension needs at least \(r\) new vertices. If \(k=0,i=1\), just one new vertex would give the isolated old vertex only one distinct new neighbor, so at least two new vertices are needed. The empty-defect case is already an amalgamation base.

For \(r=1,k=1,i=0\), connect the endpoints of the unique path by one new vertex, making a cycle. For \(r=1,k=0,i=1\), use two new vertices to complete the old isolate to a triangle. For \(r\ge2\), orient the \(r\) old unfinished path components arbitrarily (a singleton has the same entrance and exit), arrange them cyclically, and insert one new bridge vertex between each consecutive ordered pair. Each nontrivial path then gains one neighbor at each endpoint, and each singleton gains two *distinct* bridge neighbors. Every old-old nonedge remains a nonedge, and the resulting single cycle has length at least four, even when two singleton components are used. Existing cycle components are unchanged. This achieves the stated minimum.

**3. Enumeration of all minimum-size extensions.** Consider \(r\ge1\), apart from the single-isolate exception. In any optimal extension with exactly \(r\) new vertices, there are precisely \(2r\) old-to-new edges, as demanded by old deficits. Their total degree at the new ends is \(2r\), the entire available new-vertex degree capacity. Hence every new vertex is adjacent to exactly two *distinct* old deficit vertices, there are no new-new edges, and every old deficit vertex \(a\) receives exactly \(d_a\) new neighbors. Conversely, any selection of an unordered old-neighbor pair for each distinctly labelled new vertex that realizes these degrees produces a simple graph all of whose vertices have degree two, thus an amalgamation base. Each assignment contributes exactly one monomial of \(\sum_{a<b}x_ax_b\) for each new-vertex label, so the coefficient of the specified deficit monomial counts precisely all optimal graphs, with no overcounting or missing cases. If no deficits occur, the original graph is the unique zero-new-vertex optimum. If there is a single isolated vertex, its optimal completion is uniquely the triangle on the three fixed labels.

**4. Limit and computability.** Let \(M\) contain infinitely many disjoint copies of each \(C_\ell\) for \(\ell\ge3\). Every member of \(\mathcal K_2\) embeds inducedly in \(M\), since every finite path embeds inducedly in a sufficiently longer cycle. Isomorphisms between finite unions of *whole* cycles extend to automorphisms of \(M\), by permuting the infinitely many components separately at each cycle length and extending the cycle isomorphisms. Thus \(M\) is cofinally ultrahomogeneous with age \(\mathcal K_2\), hence the cofinal Fraïssé limit. In any computable presentation of \(M\), the two neighbors of a given vertex can be found by computable search, and following neighbors traces its finite cycle effectively. The components and their lengths are therefore computably enumerable, allowing an effective isomorphism to a fixed computable copy by matching the \(j\)-th enumerated component of each length. This proves computable categoricity.

## Verification

The standalone Python 3 program `verify.py` independently enumerates all permitted old-new and new-new edge choices on small labelled unions of paths and isolated vertices. It confirms that no completion below the theorem's bound is two-regular and compares the exact number at the bound with a separate dynamic-programming coefficient extraction. The tested \((k,i)\) pairs are \((0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1)\). The program reports `ALL_CHECKS_OK`. These finite checks support, but do not replace, the all-parameter proof above.

## Relationship to prior work

Ackerman, Freer and Mirabi's 2026 paper establishes the general framework, existence and oracle-computability bounds for cofinal Fraïssé limits and illustrates why relational encodings can turn amalgamation into cofinal amalgamation. The present statement instead provides an exact graph-age amalgamation-base characterization, a sharp all-input *minimum-vertex* completion law, a full labelled optimal-completion polynomial, and a direct computably categorical limit in the bounded-degree-two case. None of these exact degree-two formulas follows from its stated general bounds. Krawczyk, Kruckman, Kubiś and Panagiotopoulos study other finite forest and labelled directed graph examples of weak amalgamation, including examples failing cofinal amalgamation, rather than these two-regular completions. A published exact successor-completion theorem on functional digraphs concerns *linear-order successor completion measured in additional edges*, not induced two-regular supergraphs measured in added vertices or their optimum counts.

## Limitations

The claim is restricted to finite simple **undirected** graphs with maximum degree two and **induced embeddings**. Neither arbitrary maximum degree nor non-induced embeddings, directed path completions, arbitrary infinite hosts, or labelled cycle-length enumeration is classified. The coefficient counts optimum graphs with **fixed labelled new vertices** and is not an isomorphism-class count. General historical priority cannot be guaranteed by literature/database search; independent external mathematical validation has not been performed.

## References

- N. Ackerman, C. Freer and M. Mirabi, *On the Computability of Cofinal Fraïssé Limits*, arXiv:2601.22435, first public 2026-01-30, https://arxiv.org/abs/2601.22435.
- A. Krawczyk, A. Kruckman, W. Kubiś and A. Panagiotopoulos, *Examples of weak amalgamation classes*, arXiv:1907.09577, first public 2019-07-22, https://arxiv.org/abs/1907.09577.
- *Optimal exact-successor completion of finite-component path forests*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-optimal-exact-successor-completion-of-finite-component-path-fore--ff194a2cbcef.
