# Triangle-edge criterion for two-direction edge general position in independence flip graphs

## Finding
Let \(H=(V,E)\) be any finite simple graph with \(|V|=n\ge2\). Its **independence flip graph** \(\mathcal I(H)\) has as vertices all independent subsets of \(V\), with an edge between sets that differ by adding or deleting exactly one vertex. Let \(\Theta_i\) be the collection of all its edges that toggle \(i\in V\). An edge set is **in edge general position** when no shortest path contains three of its edges; **maximal** always means inclusion-maximal rather than maximum cardinality.

**Theorem.** For distinct \(i,j\in V\), \(\Theta_i\cup\Theta_j\) is an edge-general-position set, and
\[
\Theta_i\cup\Theta_j\text{ is inclusion-maximal}\quad\Longleftrightarrow\quad N_H(i)\cap N_H(j)=\varnothing\text{ or }ij\notin E(H).
\]
Equivalently, the union is maximal exactly when \(ij\) is not an edge in any triangle of \(H\). Each \(\Theta_i\) is nonempty, and distinct unions are different. Thus if \(t_\triangle(H)\) denotes the number of edges of \(H\) belonging to at least one triangle, exactly
\[
\binom n2-t_\triangle(H)
\]
of these two-class unions are maximal. In particular **all** such unions are maximal if and only if \(H\) is triangle-free.

## Assumptions and scope
The graph \(H\) may be disconnected and may have isolated vertices, but is finite, simple and loopless, with at least two vertices. The flip graph includes the empty independent set, and vertices are *all* independent subsets, not just maximal independent sets. The theorem does not characterize other maximal edge-general-position sets or compute the maximum edge-general-position number. The neighborhoods \(N_H(i)\) are open.

## Proof
**Isometric embedding and the coordinate classes.** Give each independent set its binary incidence vector. If \(A,B\) are independent, delete the members of \(A\setminus B\), then insert the members of \(B\setminus A\). Every intermediate set is independent; the walk has length \(|A\triangle B|\), which is the lower bound from the Hamming cube. Consequently
\[
d_{\mathcal I(H)}(A,B)=|A\triangle B|.
\]
Every shortest path therefore toggles each coordinate at most once. The classes \(\Theta_i\) are exactly the coordinate (Djoković–Winkler) classes of this partial cube, and are nonempty because \(\varnothing\) and \(\{i\}\) are adjacent. Since a shortest path uses at most one edge of any given class, \(\Theta_i\cup\Theta_j\) is always in edge general position.

**Sufficiency.** Fix distinct \(i,j\) such that either they are nonadjacent or they are adjacent with no common neighbor. Consider any edge not in their two classes. Write its endpoints as \(S\) and \(S\cup\{k\}\), where \(k\notin\{i,j\}\), \(S\) is independent and \(S\cup\{k\}\) is independent. We construct a shortest path through this prescribed edge and one edge from each of \(\Theta_i,\Theta_j\). A walk that toggles every coordinate at most once is shortest by the established distance identity.

If \(ij\notin E(H)\), start at \(S\cup\{k\}\), delete \(k\) (using the prescribed edge), delete every element of \(S\), and finally insert those members of \(\{i,j\}\) that were not in \(S\). The last set is independent because \(ij\notin E(H)\). Both coordinates \(i,j\) are toggled exactly once, either by deletion or by insertion, and no coordinate is repeated.

Now suppose \(ij\in E(H)\) but \(N_H(i)\cap N_H(j)=\varnothing\). The set \(S\) contains at most one of \(i,j\). If \(i\in S\) (the case \(j\in S\) is symmetric), start at \(S\cup\{k\}\); delete \(k\), then delete all members of \(N_H(j)\cap S\), including \(i\); then insert \(j\). All intermediate sets are independent, and no coordinate is toggled twice.

It remains to treat \(i,j\notin S\). Since \(k\) is not a common neighbor of \(i,j\), interchange their names if necessary to arrange \(kj\notin E(H)\). Write \(A=N_H(i)\cap S\) and \(B=N_H(j)\cap S\). By the no-common-neighbor assumption, \(A\cap B=\varnothing\). Start with the independent set \((S\setminus A)\cup\{i\}\); delete \(i\), insert all elements of \(A\), and arrive at \(S\). Next insert \(k\), traversing the prescribed edge, delete all elements of \(B\), and insert \(j\). Every intermediate set is independent: the final insertion is allowed because \(j\) is nonadjacent to \(k\), and the remaining members of \(S\) avoid \(N_H(j)\). Each coordinate is toggled only once, using \(A\cap B=\varnothing\). This shortest path traverses the given third-class edge and both selected classes. Hence adding ANY outside edge destroys edge general position; the union is inclusion-maximal.

**Necessity.** Suppose \(ij\in E(H)\) and \(k\in N_H(i)\cap N_H(j)\). Let \(e\) be the edge \(\varnothing\)--\(\{k\}\) in \(\mathcal I(H)\), outside the two selected classes. There is no shortest path containing \(e\) and an edge of each of \(\Theta_i\) and \(\Theta_j\). Indeed, on any such shortest path the \(k\)-coordinate is toggled only at \(e\). Oriented \(\varnothing\to\{k\}\), after \(e\) the vertex \(k\) remains present, so neither \(i\) nor \(j\) can be toggled there; both must be deleted before \(e\), forcing the initial independent set to contain adjacent vertices \(i,j\), impossible. Oriented \(\{k\}\to\varnothing\), neither \(i\) nor \(j\) can be toggled before \(e\), and after \(e\) they would both have to be inserted, forcing the final set to contain adjacent \(i,j\), again impossible. Thus \(e\) can be added without creating a three-edge geodesic obstruction, proving nonmaximality.

The two implications prove the theorem. The counting and triangle-free equivalence follow because all \(\binom n2\) distinct coordinate pairs give distinct unions, and the only failing pairs are precisely the edges in triangles. \(\square\)

## Verification
A standalone script `independence_theta_verify.py` constructs every independent-set flip graph explicitly and computes all-pairs distances by breadth-first search. For each pair of coordinate classes, it tests maximality directly: an outside edge lies on a shortest path crossing both chosen coordinates precisely when a pair of endpoints has different values in both coordinates and some orientation of that outside edge satisfies the shortest-path distance equality. The script checks the result for **every labelled simple graph on two, three, four and five vertices**, and for 160 seeded six-vertex graph profiles. The command `python independence_theta_verify.py` returned `VERIFY_OK graph_profiles=1258 tested_pairs=13050 tested_flip_edges=25084 direct_BFS_geodesic_criterion=PASS triangle_edge_boundary=PASS`. This is corroborating finite evidence, not the proof for unbounded graph order.

## Relationship to prior work
Manuel, Prabha and Klavžar (2021, Lemma 3.1) proved that the union of two \(\Theta\)-classes in **any** partial cube is edge-general-position; this supplies the baseline feasibility, not maximality. Klavžar and Tan (2023, Theorem 4.3) proved maximality of the first and last coordinate classes in Fibonacci cubes, and explicitly **state in the paragraph following that theorem** that *all* pairs of Fibonacci-cube coordinate classes are maximal (their full case analysis is omitted). Thus the Fibonacci-cube all-pairs consequence is **already known and is not claimed as novel**. Their Theorem 4.6 addresses first/last classes in Lucas cubes. Tian, Klavžar and Tan (2023/2024) study extremal edge-general-position numbers and block graphs. None of those inspected sources states the present classification **for the flip graph of independent sets of an arbitrary graph**, especially the triangle-edge obstruction and exact pair count. For \(H=P_n\), \(\mathcal I(H)\) is the Fibonacci cube, and for \(H=C_n\), \(n\ge4\), it is the Lucas cube. These are specializations, not separate new claims.

## Limitations
The original-contribution claim is limited to the general necessary-and-sufficient triangle-edge criterion and its exact count for independent-set flip graphs. The known Fibonacci special case and the general partial-cube edge-general-position lemma are prior results. The theorem does not decide maximum-size edge general position, or classify all maximal edge sets; a stronger unindexed characterization from median-graph or hyperplane literature could subsume the criterion. Computational tests cover only the specified finite orders. Independent expert assessment and publication-priority determination have not been performed.

## References
1. S. Klavžar and E. Tan, *Edge general position sets in Fibonacci and Lucas cubes*, arXiv:2304.10114v1, submitted 20 April 2023; Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 120. https://arxiv.org/html/2304.10114v1
2. P. Manuel, R. Prabha, and S. Klavžar, *Edge general position problem*, arXiv:2105.04292v1, submitted 10 May 2021. https://arxiv.org/html/2105.04292v1
3. J. Tian, S. Klavžar, and E. Tan, *Extremal edge general position sets in some graphs*, arXiv:2302.01587v1, submitted 3 February 2023; Graphs and Combinatorics 40 (2024), article 40. https://link.springer.com/article/10.1007/s00373-024-02770-z
