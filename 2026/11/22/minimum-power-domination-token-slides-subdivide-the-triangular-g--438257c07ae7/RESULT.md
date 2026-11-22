# Minimum power-domination token slides subdivide the triangular graph

## Finding
For every integer \(n\ge3\), let \(H_n\) be obtained from the labelled complete graph \(K_n\) by replacing every edge with a path of length two. A **power dominating set** is a collection of selected vertices whose closed neighborhood initially becomes observed, followed by repeated observations of a unique unobserved neighbor of any observed vertex. Let \(\mathcal R_n\) have as vertices all *minimum-cardinality* power dominating sets of \(H_n\); two configurations are adjacent only when exactly one selected vertex is moved to an unselected neighbor along an edge of \(H_n\), and the resulting configuration remains a minimum power dominating set.

Write \(J(n,2)=L(K_n)\) for the triangular graph with vertices the unordered pairs from \([n]\), and with two pairs adjacent precisely when they share one label. Let \(\operatorname{Sub}(J(n,2))\) mean the graph obtained by subdividing **every edge once** (not its line graph). Then
\[
\boxed{\mathcal R_n\cong\operatorname{Sub}(J(n,2)),\qquad \operatorname{diam}(\mathcal R_n)=\min\{n,6\}.}
\]
The isomorphism respects the original labels of \(K_n\) and is given explicitly below. Moreover,
\[
\gamma_P(H_n)=n-2,\qquad |V(\mathcal R_n)|=\frac{n(n-1)^2}{2},\qquad |E(\mathcal R_n)|=n(n-1)(n-2).
\]
For \(n\ge4\), precisely \(\binom n2\) reconfiguration vertices have degree \(2(n-2)\), and precisely \(3\binom n3\) have degree two. When \(n=3\), all six vertices have degree two and \(\mathcal R_3\cong C_6\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled. Original vertices of \(H_n\) are \(v_i\) for \(i\in[n]\); each original pair \(\{i,j\}\) has a distinct degree-two subdivision vertex \(w_{ij}\) adjacent just to \(v_i\) and \(v_j\). A selected set \(S\) is power dominating if its initially observed set is the closed neighborhood \(N[S]\), after which the ordinary unique-unobserved-neighbor forcing rule eventually observes all vertices. No intermediate nonminimum configuration is allowed. A token slide, rather than a token jump, requires the removed and added vertices to be adjacent **in \(H_n\)**.

## Proof
**1. Exact power-domination criterion.** For any selected \(S\), put \(A=\{i:v_i\in S\}\), \(U=[n]\setminus A\), and let \(F_S\) be the simple graph on \(U\) with an edge \(ij\) exactly when the subdivision vertex \(w_{ij}\) is **not** selected. Then
\[
S\text{ power dominates }H_n\quad\Longleftrightarrow\quad F_S\text{ is a forest}. \tag{1}
\]
If \(F_S\) has a cycle, every subdivision vertex corresponding to that cycle starts unobserved: it is neither selected nor adjacent to a selected original vertex. The only way to force such a vertex is from an incident original vertex, but every original vertex on the cycle has at least two still-unobserved cycle subdivision neighbors. Hence no cycle subdivision vertex can ever be forced, proving necessity.

Suppose \(F_S\) is acyclic. If \(A\ne\varnothing\), choose \(a\in A\). Every unselected original vertex \(v_u\) is forced from the observed \(w_{au}\) if it was not observed initially: the other neighbor \(v_a\) of \(w_{au}\) is already observed. Thus all originals become observed. All subdivision vertices outside \(F_S\) are either selected or adjacent to a selected original; after all originals are observed, remaining unobserved subdivision vertices are exactly edges of the forest \(F_S\). Repeatedly using a leaf of the remaining forest forces its unique unobserved incident subdivision vertex, deleting that forest edge, until none remain.

If \(A=\varnothing\), then \(F_S\) is a forest on all \(n\ge3\) labels. Every vertex of degree at most one in \(F_S\) is incident to at least \(n-2\ge1\) selected subdivision vertices and so is initially observed. For each tree component, these observed leaves force their incident unobserved subdivision vertices; these in turn force the adjacent original vertices if necessary. Inductively peel leaf edges. Every remaining original vertex and edge subdivision vertex is eventually observed. This proves (1), including the boundary case where the selected set contains no original vertices.

**2. Inclusion-minimal configurations.** A power dominating set is inclusion-minimal precisely when there is an \(r\)-element subset \(U\subseteq[n]\) with \(r\ge2\) and a labelled spanning tree \(T\) on \(U\) such that
\[
S=\{v_a:a\in[n]\setminus U\}\ \cup\ \{w_{ij}:\{i,j\}\subset U,\ ij\notin E(T)\}.\tag{2}
\]
Indeed, a selected subdivision vertex incident to a selected original vertex can be deleted without changing \(F_S\), so no such vertex occurs in a minimal set. If the forest \(F_S\) has more than one component, any selected subdivision vertex across two components can be deleted, adding one edge without creating a cycle. Thus \(F_S\) must be a tree whenever \(r\ge2\). For \(r=0,1\), removal of an original vertex preserves the forest condition, so these cases are not minimal. Conversely, in (2), removing a selected subdivision vertex adds an edge to the tree and creates a cycle. Removing a selected original vertex \(v_a\) adds \(a\) and every \(a-u\) edge to the forest on \(U\), creating a triangle with any existing edge of \(T\). Hence (2) is exactly the set of inclusion-minimal solutions, by (1).

The set (2) has size \(n-2+\binom{r-2}{2}\). This minimum equals \(n-2\) exactly for \(r=2\) or \(r=3\). Therefore the minimum configurations are of two explicit kinds:

* **Pair type:** \(P_{ij}=\{v_a:a\notin\{i,j\}\}\), indexed by unordered pairs \(\{i,j\}\).
* **Triple-edge type:** \(Q_{ij\mid k}=\{v_a:a\notin\{i,j,k\}\}\cup\{w_{ij}\}\), indexed by distinct \(i,j,k\) with \(\{i,j\}\) unordered.

There are \(\binom n2\) and \(3\binom n3\) of these, respectively. This establishes the minimum and the stated number of vertices.

**3. Every permitted slide.** Original vertices of \(H_n\) are adjacent only to subdivision vertices. Hence a slide between two pair-type configurations is impossible; a slide between two triple-edge configurations is also impossible (either it would introduce two selected subdivision vertices or would remove the sole selected subdivision vertex and yield a pair type). A slide from \(P_{ab}\) to \(Q_{ij\mid k}\) is possible exactly when \(\{a,b\}\) is one of \(\{i,k\}\) and \(\{j,k\}\): in the first case it moves the selected original \(v_j\) to \(w_{ij}\), and in the second it moves \(v_i\) to \(w_{ij}\). The missing pair \(\{i,j\}\) does not give a slide because the original \(v_k\) is nonadjacent to \(w_{ij}\).

Map \(P_{ab}\) to the \(J(n,2)\) vertex \(\{a,b\}\); map \(Q_{ij\mid k}\) to the new vertex subdividing the \(J(n,2)\) edge between \(\{i,k\}\) and \(\{j,k\}\). Every edge of \(J(n,2)\) has a unique such representation, and the preceding slide criterion matches exactly its two incidences. This gives the claimed graph isomorphism, counts \(2\binom n2(n-2)\) edges, and degrees.

**4. Sharp diameter.** In \(J(n,2)\) the distance between distinct pair vertices \(p,q\) is \(2-|p\cap q|\) (equal to one or two), so the diameter of its full subdivision is at most six. For \(n=3\), \(J(3,2)=K_3\), whose subdivision is \(C_6\), diameter three. For \(n=4\), every two triples of labels intersect in at least two labels, so any two subdivided Johnson edges have adjacent or coincident endpoints; any pair vertex also shares a label with an endpoint of each Johnson edge. Thus all distances are at most four, attained between the subdividing vertices of the two Johnson edges \((12,13)\) and \((24,34)\), giving diameter four. For \(n=5\), any two triples intersect, so any two subdivided Johnson edges have endpoints at distance at most one; hence subdivision-to-subdivision distances are at most four. However the pair vertex \(\{4,5\}\) is at distance five from the subdividing vertex of the Johnson edge \((12,13)\). Thus the diameter is five. For \(n\ge6\), choose Johnson edges \((12,13)\) and \((45,46)\). Their endpoint pairs are disjoint, each at distance two in \(J(n,2)\), so their subdividing vertices have distance six. The general six bound is sharp, proving \(\operatorname{diam}=\min\{n,6\}\).

## Verification
`verify_power.cpp` independently evaluates every initial sensor subset of \(H_n\) by direct closed-neighborhood propagation and tests (1) and (2) for \(n=3,4,5\), covering \(64+1024+32768=33856\) subsets. It reports `VERIFY_OK`, minimum sizes \(1,2,3\), and minimum-set counts \(6,18,40\).

`verify_slides.py` constructs the two minimum-set types (2) and independently derives every legal slide from the actual adjacency relation of \(H_n\). It compares the complete slide edge set to the explicit Johnson-subdivision incidences and computes all-pairs distances for each \(3\le n\le8\), returning `SLIDES_OK`. `verify_polynomials.py` separately enumerates labelled forests to check the intermediate power-domination counts and the Cayley-number minimum-set formula for \(n=3,4,5\), returning `POLYNOMIAL_OK`. Reproduction: compile the C++ source with `g++ -std=c++17 -O3 verify_power.cpp -o verify_power` and execute it; also run `python3 verify_slides.py` and `python3 verify_polynomials.py` from the extracted artifact directory. All computations are finite corroboration; the four proof stages above establish the theorem for all integers \(n\ge3\).

## Relationship to prior work
Brimkov, Patel, Suriyanarayana and Teich (2018) define and systematically study the ordinary power-domination polynomial. Their full-text Section 4 treats complete graphs, cycles, paths, stars, threshold graphs, and related constructions, not this fully edge-subdivided family or its optimum token slides. Kniahnitskaya and collaborators (2022) count power-dominating subsets on complete rooted trees, a different graph class. Bjorkman and collaborators (2026) define minimum-power-domination token jumps and illustrate slides, with explicit classifications for complete and complete bipartite graphs, paths, cycles and wheels; their full text does not give the family here.

A published fort classification for once-subdivided complete graphs identifies cycle-subdivision forts. Together with the established zero-forcing/fort duality this substantially **covers the supporting forest obstruction** used in Step 1 and can be used to derive the minimum configurations in Step 2. Neither those prior fort statements nor the inspected power-domination reconfiguration work supplies the **new claimed object**: the exact graph isomorphism for *adjacency-restricted* motion of optimum sensors, or its sharp all-order distance/diameter law. The present result does not claim its forest criterion or the definition of power domination as a separate independent discovery.

## Limitations
The theorem is restricted to the graph obtained by subdividing **every** edge of a complete graph exactly once and to minimum cardinality, ordinary power domination. It does not describe token-jump distances, feasibility of intermediate larger sensor configurations, or arbitrary graph subdivisions. No independent mathematical audit has been performed. Publication priority is provisional: unindexed work or reconfiguration classifications under equivalent naming could cover the same slide graph, and a general fort classification already implies important supporting lemmas.

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (2018-05-28). https://arxiv.org/html/1805.10984v1
2. S. Kniahnitskaya, M. Ortiz, O. Ramirez, K. Shultis, and H. Whitlatch, *Counting Power Domination Sets in Complete m-ary Trees*, arXiv:2201.09111 (2022-01-22). https://arxiv.org/abs/2201.09111
3. B. Bjorkman and coauthors, *Power Domination Reconfiguration*, La Matematica (published 2026-01-13), DOI:10.1007/s44007-025-00187-5. https://link.springer.com/article/10.1007/s44007-025-00187-5
4. *Minimal forts of the once-subdivided complete graph: cycles, exceptional stars, and gaps* (publicly indexed 2026 result; original statement and proof inspected); its minimal-fort theorem is acknowledged for the forest obstruction underlying the present slide classification.
