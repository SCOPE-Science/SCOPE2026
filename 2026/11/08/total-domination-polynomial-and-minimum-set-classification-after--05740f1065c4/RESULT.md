# Total-domination polynomial and minimum-set classification after one deletion from a triangular graph

## Finding

For an integer \(n\ge4\), let \(J(n,2)\) have as vertices the two-element subsets of \([n]=\{1,\ldots,n\}\), with adjacency when the subsets share exactly one element. Fix a vertex \(v=\{a,b\}\), and write \(X_n=J(n,2)-v\). Let \(P_n(z)=\sum_D z^{|D|}\), where \(D\) ranges over **total dominating sets** of \(X_n\): every vertex of \(X_n\), including those in \(D\), must have a distinct adjacent vertex in \(D\).

Define the formal exponential generating series and its coefficient polynomials
\[
H(x,z)=\exp\!\left(-x-\frac{zx^2}{2}\right)
\sum_{j\ge0}(1+z)^{\binom j2}\frac{x^j}{j!},
\qquad h_j(z)=j![x^j]H(x,z),
\]
with \(h_0(z)=1\). Put \(T_n(z)=h_n(z)+n h_{n-1}(z)\) and \(N=\binom n2\). Then the **entire total-domination polynomial**, for every \(n\ge4\), is
\[
\boxed{P_n(z)=T_n(z)-\frac{z}{N}T'_n(z)+h_{n-2}(z).}
\]
The formula is an identity of polynomials with nonnegative integer coefficients; the displayed rational factor is coefficientwise integral after combination because of edge transitivity.

The exact minimum is
\[
\boxed{\gamma_t(X_n)=\left\lceil\frac{2(n-2)}3\right\rceil.}
\]
Consequently, relative to the known value \(\gamma_t(J(n,2))=\lceil2(n-1)/3\rceil\), deletion lowers the minimum by one precisely when \(n\equiv0,2\pmod3\); it leaves the minimum unchanged when \(n\equiv1\pmod3\).

All minimum sets are classified by the graph \(F\) whose edges are the selected two-element subsets and whose vertex set is \([n]\). Denote a tree on \(r\) vertices by an \(r\)-tree, and a three-vertex path by \(P_3\). In the following, distinct components use disjoint labelled vertices, and isolated vertices are explicitly specified.

* For \(n=3k\), \(k\ge2\), the isolated vertices of \(F\) are exactly \(a,b\), and its nontrivial components are one arbitrary \(4\)-tree and \(k-2\) copies of \(P_3\).
* For \(n=3k+2\), \(k\ge1\), the isolated vertices are exactly \(a,b\), and the nontrivial components are \(k\) copies of \(P_3\).
* For \(n=3k+1\), \(k\ge1\), there are two disjoint possibilities: (I) exactly one isolated vertex and \(k\) copies of \(P_3\), with \(ab\notin E(F)\); (II) exactly the two isolated vertices \(a,b\), with either one \(5\)-tree and \(k-2\) copies of \(P_3\) (possible for \(k\ge2\)), or two \(4\)-trees and \(k-3\) copies of \(P_3\) (possible for \(k\ge3\)).

Conversely, every listed selected-edge graph gives a minimum total dominating set of \(X_n\). Here \(ab\notin E(F)\) is necessary because \(ab\) is not a vertex of \(X_n\).

Let \(M_n\) count minimum sets on the labelled vertices of \(X_n\). For \(k\ge2\),
\[
M_{3k}=\frac{(3k-2)!\,16}{4!\,2^{k-2}(k-2)!};
\qquad M_{3k+2}=\frac{(3k)!}{2^k k!}\quad(k\ge1).
\]
For \(n=3k+1\), define \(B_1=0\), \(B_2=125\), and for \(k\ge3\) define
\[
B_k=(3k-1)!\left(
\frac{125}{5!\,2^{k-2}(k-2)!}+
\frac{16^2}{2!(4!)^2\,2^{k-3}(k-3)!}
\right).
\]
Then for every \(k\ge1\),
\[
\boxed{M_{3k+1}=\frac{(3k+1)!}{2^k k!}
\left(1-\frac{2k}{\binom{3k+1}{2}}\right)+B_k.}
\]
The successive values \(M_n\) for \(n=4,5,\ldots,10\) are \(8,3,16,635,90,1680,95480\).

## Assumptions and scope

The graphs are finite, simple, undirected, and labelled by \([n]\); all total-domination conditions use **open** neighborhoods. Exactly one vertex of \(J(n,2)\) is removed, corresponding to the missing edge \(ab\) of \(K_n\). Vertex transitivity makes the polynomial and the counts independent of the choice of \(a,b\). The result covers every integer \(n\ge4\), with no limiting or generic-position assumptions. Graph families and source terms in the generating function are treated formally, not analytically.

## Proof

**1. Translation to selected edges.** The canonical isomorphisms \(J(n,2)=L(K_n)\) and \(X_n=L(K_n-ab)\) identify a set \(D\) with an edge set \(F\subseteq E(K_n)\setminus\{ab\}\). Write \(I(F)\) for the vertices of \([n]\) incident with no selected edge. A selected edge has a selected adjacent edge exactly when its component in the graph \(([n],F)\) is not a solitary \(K_2\) component. An unselected edge \(uv\ne ab\) is dominated exactly when at least one of \(u,v\) is not in \(I(F)\). Therefore \(F\) totally dominates \(X_n\) precisely when it has no \(K_2\) component and \(I(F)\) is empty, a singleton, or exactly \(\{a,b\}\). The last possibility is valid because \(ab\) is the only absent edge among the possible pairs of isolated vertices.

**2. All-size polynomial.** For a graph on labelled \(j\) vertices, each of its \(\binom j2\) possible edges contributes either \(1\) or \(z\), so the weighted sum over all such graphs is \((1+z)^{\binom j2}\). The exponential formula for decomposing labelled graphs into connected components shows that multiplying its exponential generating series by \(\exp(-x-zx^2/2)\) removes exactly the connected components of type \(K_1\) and \(K_2\), counted with respective weights \(x\) and \(zx^2/2\). Thus \(h_j(z)\) counts graphs on \(j\) labelled vertices with neither of those component types.

The original graph \(J(n,2)\) has a total dominating set exactly when \(F\) has no \(K_2\) component and at most one isolated vertex. Its polynomial is consequently \(T_n(z)=h_n(z)+n h_{n-1}(z)\). By symmetry of the \(N=\binom n2\) edges of \(K_n\), the weighted sum of those total dominating edge sets containing a fixed edge \(ab\) is \(zT'_n(z)/N\): each selected set of size \(s\) contributes incidence to exactly \(s\) of the \(N\) possible edges. Hence the old total dominating sets that avoid \(ab\) have polynomial \(T_n(z)-zT'_n(z)/N\).

The additional sets that become total dominating only after removing the vertex \(ab\) have exactly \(I(F)=\{a,b\}\). All their selected edges are on the remaining \(n-2\) labels, with no isolated vertex or \(K_2\) component there; their polynomial is \(h_{n-2}(z)\). This class is disjoint from the old total dominating sets. Summing the two classes proves the polynomial identity.

**3. Minimum and classification.** Suppose \(F\) has \(s\) selected edges, \(r\) incident vertices, \(c\) nontrivial connected components, and total cycle rank \(q\ge0\). Since no component is \(K_2\), each component has at least two selected edges; thus \(c\le\lfloor s/2\rfloor\). The identity \(r=s+c-q\) gives \(r\le s+\lfloor s/2\rfloor\). The isolate characterization forces \(r\ge n-2\), so \(s\ge\lceil2(n-2)/3\rceil\).

If \(n=3k\) and \(s=2k-1\), then \(r\le3k-2=n-2\). Necessarily \(r=3k-2\), \(c=k-1\), and \(q=0\). The components are trees; the surplus of one edge over the two-edge baseline per component gives exactly one \(4\)-tree and \(k-2\) copies of \(P_3\), with isolates \(a,b\).

If \(n=3k+2\) and \(s=2k\), then \(r\le3k=n-2\), so the same reasoning forces \(c=k\), \(q=0\), and precisely \(k\) copies of \(P_3\), again with isolates \(a,b\).

If \(n=3k+1\) and \(s=2k\), then \(r\le3k=n-1\). With one isolated vertex, \(r=3k\), so \(c=k\), \(q=0\), and all components are \(P_3\). Such a set is legal only if it does not select \(ab\). With two isolated vertices they must be \(a,b\), and \(r=3k-1\). We have \(c-q=k-1\). The alternative \(c=k\) would force all components to have exactly two edges and hence \(q=0\), contradicting \(c-q=k-1\). Thus \(c=k-1\), \(q=0\), and there are two surplus edges relative to \(k-1\) two-edge components: one \(5\)-tree or two \(4\)-trees, with the remaining components \(P_3\). These alternatives require the stated lower bounds on \(k\).

Every displayed forest meets the isolate and no-\(K_2\) conditions and has exactly the lower-bound number of edges. They exist for all \(n\ge4\): at \(n=4\), choose a single isolated vertex and one \(P_3\) avoiding \(ab\). Therefore all cases are attained, and no additional minimizers occur.

**4. Counting.** The numbers of trees on three, four, and five fixed labels are, by Cayley's formula, respectively \(3\), \(16\), and \(125\). Standard labelled-component partitioning gives the formulas for \(n\equiv0,2\pmod3\) and the two-isolate contribution \(B_k\) for \(n\equiv1\pmod3\).

For the remaining \(n=3k+1\) class, the original optimal sets comprise one isolated vertex and \(k\) copies of \(P_3\), numbering \((3k+1)!/(2^kk!)\). Each has \(2k\) selected edges. Transitivity of \(K_n\) on its edges implies that the fraction of these sets avoiding the prescribed edge \(ab\) is \(1-2k/\binom{3k+1}{2}\). This proves the asserted count and finishes the classification.

## Verification

The accompanying standalone file `verify.py` uses only the standard library. It independently computes the coefficient polynomials by decomposing all labelled graphs into forbidden components \(K_1,K_2\), then compares them with **direct exhaustive total-neighborhood checks** on all \(2^{\binom n2-1}\) candidate edge subsets for every \(4\le n\le7\). It also exhaustively checks cardinalities \(\gamma_t(X_n)-1\) and \(\gamma_t(X_n)\) for \(n=8,9\), and compares the tree enumeration against the computed polynomial for \(4\le n\le9\). The run reports `VERIFY_OK`. These finite checks corroborate the argument; the statements for arbitrary \(n\) follow from the proof above.

## Relationship to prior work

Cornet, Dravec and Torres established \(\gamma_t(J(n,2))=\lceil2(n-1)/3\rceil\) for the undeleted triangular graph in their 2026 paper; their Theorem 14 and proof address that scalar invariant, not the full vertex-deleted total-domination polynomial. Already in 2018, OEIS A304561 recorded the complete counts and underlying component types of minimum total dominating sets of the **undeleted** triangular graph; OEIS A303048 recorded all-size total domination counts for that graph. Those results are acknowledged and are not claimed as new here. The new statement concerns \(J(n,2)-v\), whose additional two-isolate configurations and exact polynomial are absent from those undeleted-graph statements. The basic translation to line-graph total edge domination and the labelled graph exponential formula are standard tools.

## Limitations

The formulas treat deletion of exactly one vertex from \(J(n,2)\), not arbitrary multiple deletions or \(J(n,k)\) with \(k\ge3\). The result does not give independent historical priority guarantees: equivalent statements could exist in unindexed literature. The finite verifier does not constitute an infinite proof or independent mathematical certification.

## References

1. M. G. Cornet, T. Dravec and P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675 (first submitted 2026-10-03), especially Theorem 14. https://arxiv.org/abs/2610.04675
2. OEIS A304561, *Number of minimum total dominating sets in the n-triangular (Johnson) graph*, E. W. Weisstein and A. Howroyd (2018). https://oeis.org/A304561
3. OEIS A303048, *Number of total dominating sets in the n-triangular (Johnson) graph*, E. W. Weisstein and A. Howroyd (2018). https://oeis.org/A303048
4. Z. Pan, Y. Yang, X. Li and S.-J. Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431 (2019). https://arxiv.org/abs/1910.02431
