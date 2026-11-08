# Distance spheres of minimum dominating sets in odd triangular graphs

## Finding

For every integer \(k\ge1\), let \(T_{2k+1}=L(K_{2k+1})\) be the triangular graph: vertices of \(T_{2k+1}\) are edges of the complete graph \(K_{2k+1}\), and two vertices are adjacent precisely when their corresponding edges intersect. Consider the graph \(\mathcal R_k\) whose vertices are the minimum dominating sets of \(T_{2k+1}\), with an edge between two such sets exactly when one selected vertex is replaced by one unselected vertex. These are the same adjacencies under token jumping and token sliding.

The graph \(\mathcal R_k\) is connected and vertex-transitive. For any fixed vertex \(M\), define its distance-sphere polynomial \(F_k(x)=\sum_{N\in V(\mathcal R_k)}x^{d_{\mathcal R_k}(M,N)}\). It is independent of the choice of \(M\), and the complete family is determined by

\[
\boxed{\sum_{k\ge0}\frac{F_k(x)}{k!}z^k=\exp\bigl((1-x^2)z\bigr)(1-2xz)^{-1-x/2}.}
\]

Here \(F_0(x)=1\) is the formal initialization. For every \(k\ge1\), the diameter is \(\lfloor3k/2\rfloor\). The number \(A_k\) of vertices at that maximum distance from *each* fixed vertex is

\[
\boxed{A_{2h}=\frac{(2h)!}{h!}\quad(h\ge1),\qquad A_{2h+1}=\frac{(2h+1)!(4h+6)}{3h!}\quad(h\ge0).}
\]

The counts of distance spheres for \(k=1,2,3,4,5\), in increasing order of distance, are respectively \((1,2)\), \((1,4,8,2)\), \((1,6,24,54,20)\), \((1,8,48,204,464,208,12)\), and \((1,10,80,500,2120,4880,2524,280)\). These profiles count *all* pairs by multiplying each coefficient by \((2k+1)!/(2^k k!)\) and dividing by two for unordered distinct pairs.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. A dominating set \(D\) of a graph meets or neighbors every vertex. In a reconfiguration graph, every intermediate set must be dominating and have cardinality exactly the minimum domination number. A token jump changes one vertex of the selected set; a token slide is a jump along an original graph edge.

An edge set of \(K_{2k+1}\) dominates its line graph exactly when at most one vertex of \(K_{2k+1}\) is untouched by its edges. A family of fewer than \(k\) edges leaves at least three untouched vertices and cannot dominate; a family of exactly \(k\) edges dominates only if its edges are pairwise disjoint. Hence the minimum dominating sets are precisely the near-perfect matchings of \(K_{2k+1}\), and there are \((2k+1)!/(2^k k!)\) of them. Replacing one matching edge while staying within near-perfect matchings necessarily means joining its old partner to the unique previously unmatched vertex, freeing the other endpoint. The removed and added edges meet, so token jumping and token sliding coincide with the standard one-edge flip.

## Proof

Fix a starting near-perfect matching \(M\) with \(k\) edges and an arbitrary target near-perfect matching \(N\). Their symmetric difference is the disjoint union of an alternating even path (possibly of length zero) between their two unmatched vertices and alternating even cycles of length at least four. Write \(t=k-|M\cap N|\) and let \(c\) be the number of those nontrivial alternating cycles. The shortest one-flip distance is

\[
 d_{\mathcal R_k}(M,N)=t+c.
\]

For the lower bound, consider the potential \(\Phi(P)=k-|P\cap N|+c(P,N)\) at a current matching \(P\). A one-edge flip can remove only one current matching edge, so the alternating-cycle count can decrease by at most one. If it inserts an edge of \(N\), its previously unmatched endpoint lies on the alternating path of \(P\triangle N\), so the entire insertion and deletion affect that path, not any alternating cycle: the cycle count does not decrease. Consequently one flip decreases \(\Phi\) by at most one. Since \(\Phi(N)=0\), at least \(t+c\) flips are needed.

For the upper bound, flip along the alternating path, starting at the unmatched vertex of \(M\). Each flip inserts the next target edge and removes the next old edge, resolving the path in exactly as many moves as it contains edges of \(M\). The remaining free vertex is now the one unmatched in \(N\). For each remaining alternating cycle containing \(r\ge2\) old matching edges, first attach the free vertex to one endpoint of an old edge, thereby breaking the cycle. Rotate the free position along the target edges of that cycle and finally remove the temporary attachment. This uses exactly \(r+1\) flips and restores the same free vertex, leaving all other components untouched. The total is \(t+c\), proving the equality.

Now treat the \(k\) distinguished edges of \(M\) as labeled atoms. Each target \(N\) partitions the atoms into fixed singleton edges; disjoint alternating cycles, each using \(r\ge2\) atoms; and a unique alternating path using \(r\ge0\) atoms. On a specified set of \(r\) atoms, an alternating cycle has \(2^{r-1}(r-1)!\) possible target matchings, obtained by cyclically ordering the atoms and orienting their endpoint connections. A path has \(2^r r!\) possibilities, obtained by ordering and orienting its atoms. These decompositions are unique. A fixed singleton contributes distance zero, a cycle of size \(r\) contributes \(r+1\), and a path of size \(r\) contributes \(r\).

By the labeled exponential formula, with \(z\) marking atoms and \(x\) marking distance, the enumerator is

\[
 \left(\sum_{r\ge0}(2xz)^r\right)
 \exp\left(z+\sum_{r\ge2}\frac{2^{r-1}}r z^r x^{r+1}\right)
 =\frac{\exp\bigl((1-x^2)z\bigr)}{(1-2xz)^{1+x/2}}.
\]

Every alternating cycle consumes at least two nonshared atoms, hence \(c\le\lfloor t/2\rfloor\) and \(d\le k+\lfloor k/2\rfloor=\lfloor3k/2\rfloor\). This bound is attained using disjoint alternating four-cycles when \(k\) is even; for odd \(k\), use alternating four-cycles plus either a one-atom path or one six-cycle. If \(k=1\), a one-atom path alone suffices.

For \(k=2h\), diametral targets partition all \(k\) atoms into \(h\) two-atom alternating cycles. There are \((2h)!/(2^h h!)\) partitions, each with \(2^h\) target choices, giving \(A_{2h}=(2h)!/h!\). For \(k=2h+1\), diametral targets either have \(h\) two-atom cycles and a one-atom path (\(2(2h+1)!/h!\) choices), or, when \(h\ge1\), have one three-atom cycle and \(h-1\) two-atom cycles, with an empty path (\(4(2h+1)!/(3(h-1)!)\) choices). Their sum yields the stated \(A_{2h+1}\), including \(h=0\) by the first term alone.

## Verification

The standalone `verify_graph.py` enumerates all near-perfect matchings and constructs every legal flip directly, then breadth-first searches from one fixed matching for \(1\le k\le5\). Its distance-sphere outputs agree term-by-term with the theorem. It additionally enumerates every candidate set of size less than or equal to \(k\) in the underlying line graph for \(2k+1\in\{3,5,7,9\}\) and checks the minimum dominating-set count.

Independently, `verify_species.py` implements a component-partition recurrence for alternating cycles and paths rather than constructing any reconfiguration graph. For \(1\le k\le12\), it checks the total number of states, degree, diameter, and antipodal formulas, and for \(1\le k\le5\) the complete distance profiles match the direct graph search. Both verification programs use only the Python standard library. Run `python3 verify_graph.py` and `python3 verify_species.py` in the directory containing these two scripts; recorded results are `verify_graph_output.txt` and `verify_species_output.txt`.

The finite computations are crosschecks of the general proof, not substitutes for it.

## Relationship to prior work

Golovach, Heggernes, Kratsch, and Villanger (2012, arXiv:1208.5345) study enumeration of minimal edge dominating sets, equivalently dominating sets of line graphs, but do not determine this exact minimum-set distance profile. Suzuki, Mouawad, and Nishimura (2014, arXiv:1401.5714) use addition/deletion operations on bounded-size dominating sets, rather than exact-cardinality exchanges.

Aichholzer et al. (2025, arXiv:2508.18457), especially Theorem 4.10 and its proof, establish a distance formula for compatible geometric odd matchings with a crossing-free union. By suitably placing the labeled vertices, this earlier result also implies the distance expression \(t+c\) for complete-graph matchings. **The distance expression and its general diameter bound are used here as context and are not claimed as a new discovery.** The present contribution is the complete labeled distance-sphere enumerator and exact antipodal multiplicities. Brenner et al. (2026, arXiv:2607.04687) establish Hamilton-connectedness of the same one-flip graph, but their stated results do not supply the sphere polynomial or antipodal counts.

## Limitations

The enumerator applies to near-perfect matchings of *complete* odd-order graphs, equivalently minimum dominating sets of odd triangular graphs. It does not describe minimum dominating sets of even triangular graphs or geometric matchings subject to crossing restrictions. The novelty assessment concerns the distance-sphere polynomial and antipodal counts, not the known flip model, its connectivity, or the preexisting geometric distance arguments. Earlier equivalent enumerations may be unindexed; independent scholarly priority review has not been conducted.

## References

1. P. A. Golovach, P. Heggernes, D. Kratsch, Y. Villanger, *Generating All Minimal Edge Dominating Sets with Incremental-Polynomial Delay*, arXiv:1208.5345 (first public version 2012-08-27).
2. A. Suzuki, A. E. Mouawad, N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (2014-01-22).
3. O. Aichholzer et al., *Flipping odd matchings in geometric and combinatorial settings*, arXiv:2508.18457 (2025-08-25), especially Theorem 4.10.
4. S. Brenner et al., *Hamilton paths and cycles in flip graphs of (almost-)perfect matchings*, arXiv:2607.04687 (2026-07-06), especially Theorem 3.
