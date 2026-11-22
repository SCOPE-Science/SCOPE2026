# A sharp proper conflict-free colouring surcharge and witness-defect spectrum of two-subset Kneser graphs

## Finding

For integers \(n\ge5\), let \(KG(n,2)\) be the graph whose vertices are the two-element subsets of \([n]\), with two vertices adjacent when the corresponding subsets are disjoint. A *proper conflict-free colouring* is a proper vertex colouring such that every vertex of positive degree has an open-neighbourhood colour of multiplicity exactly one. The precise chromatic surcharge is

\[
\chi_{\mathrm{pcf}}(KG(n,2))=n-1=\chi(KG(n,2))+1.
\]

A stronger, enumerative statement concerns *all* ordinary optimal \((n-2)\)-colourings, not only those meeting the extra constraint. Write \(b(c)\) for the number of vertices with no colour occurring exactly once in their open neighbourhood, and put \(s=n-3\). Among proper colourings using a fixed, **named** palette of exactly \(n-2\) colours, there are precisely

\[
N_0(n)=\binom n3(n-2)!\,s\,2^{\binom{s-1}{2}}
\]

with \(b(c)=\binom s2\), and precisely

\[
N_1(n)=\binom n3(n-2)!\left(2^{\binom s2}-s2^{\binom{s-1}{2}}\right)
\]

with \(b(c)=\binom s2+3\). The second term vanishes at \(n=5\) and is positive for every \(n\ge6\). These are the only possible defect values. Dividing the counts by \((n-2)!\) gives counts of colour partitions (unlabelled colours). For completeness, \(KG(4,2)\) is a union of three edges and has proper conflict-free chromatic number two; \(KG(3,2)\) is edgeless and has ordinary chromatic number one.

## Assumptions and scope

All graphs are finite, simple and undirected; colourings are total, not partial, and colour multiplicities refer to *open* neighbourhoods. The principal two formulas require \(n\ge5\); each of the \(n-2\) palette colours must occur, as ordinary chromatic optimality forces this. A tournament means an orientation of every edge of a complete graph. Its indegree at a vertex counts arrows entering that vertex. The designation of each colour is significant only in the named-colour counts.

## Proof

**1. All ordinary optimum colourings are tournament-labelled triangle partitions.** An independent set of \(KG(n,2)\) is a pairwise-intersecting family of edges of \(K_n\). Every such family is either contained in a star (edges incident with one ground point), or is exactly the three edges of a triangle. Indeed, two intersecting edges share a ground point \(v\); an edge avoiding \(v\) and meeting both is forced to connect their other two endpoints, yielding the triangle, which cannot be enlarged. By the established equality \(\chi(KG(n,2))=n-2\), an optimal colouring partitions \(E(K_n)\) into exactly \(n-2\) star or triangle classes.

Choose a centre for every star class, choosing either endpoint for a singleton edge class if necessary. Two different star classes cannot be centred at the same ground point: merging them would remain a proper colouring with fewer than \(n-2\) colours. Let \(t\) be the number of triangle classes. Then the \(n-2-t\) distinct star centres leave \(t+2\) ground points with no star centred there. Every one of the \(\binom{t+2}{2}\) edges among those noncentres belongs to a triangle class. Each of the \(t\) triangle classes contains only three edges, whence \(\binom{t+2}{2}\le3t\), equivalently \((t-1)(t-2)\le0\). Consequently \(t\in\{1,2\}\). If \(t=2\), the four noncentres require all six edges of their \(K_4\) to be partitioned into two edge-disjoint triangles. Any two triangles on four vertices have a common edge, a contradiction. Therefore \(t=1\). The three noncentres form a set \(T\) and their triangle is exactly the unique triangle colour class.

Write \(S=[n]\setminus T\), so \(|S|=s=n-3\). Each \(v\in S\) is the centre of exactly one star class; its three edges to \(T\) must lie in that class. Every edge of \(K_n\) with both endpoints in \(S\) must be assigned to one of its endpoint stars. Direct that edge toward the star receiving it. This constructs an arbitrary tournament \(D\) on the labelled ground set \(S\); conversely each choice of \(T\), tournament \(D\), and bijection from the \(s+1=n-2\) classes to the named palette gives a unique ordinary optimum colouring. The count of all such colourings is \(\binom n3(n-2)!2^{\binom s2}\). This star–triangle fact is compatible with, and independently derivable from, Daneshpajouh's established triangle rigidity theorem, which is cited below; it is not asserted as a new theorem in isolation.

**2. The exact failed-witness set.** Consider a two-subset \(e\) of \([n]\), regarded as a graph vertex. If \(e\subset S\), the triangle class contributes exactly three neighbours (all three triangle edges are disjoint from \(e\)); every star class with centre outside \(e\) contributes at least three neighbours, one through each point of \(T\); a star centred in \(e\) contributes zero. Thus none of its neighbouring colours occurs once. All \(\binom s2\) vertices of this type fail.

If \(e\) meets \(T\) and \(S\) once each, exactly one of the three triangle edges avoids \(e\), so its unique triangle colour is a witness. Finally, if \(e\subset T\), the triangle class contributes zero neighbours and a star with centre \(v\in S\) contributes exactly \(1+\operatorname{indeg}_D(v)\) neighbours: its one edge from \(v\) to the remaining point of \(T\), plus each of the \(\operatorname{indeg}_D(v)\) edges oriented into \(v\). Therefore all three vertices of \(\binom T2\) have a unique-colour witness if and only if \(D\) has a vertex of indegree zero; otherwise all three fail. This proves the two possible values for \(b(c)\).

A tournament has *at most one* indegree-zero vertex. To count tournaments that have one, choose that vertex in \(s\) ways, orient each edge incident to it away from it, and orient the remaining \(\binom{s-1}{2}\) edges independently. The number is \(s2^{\binom{s-1}{2}}\). Subtracting from all \(2^{\binom s2}\) tournaments and multiplying by the choices of \(T\) and the colour-label permutations gives \(N_0(n)\) and \(N_1(n)\) exactly. For \(s\ge3\) a directed cycle on three vertices with the remaining edges oriented suitably gives a tournament with no indegree-zero vertex, so the second count is positive; for \(s=2\) every tournament has an indegree-zero vertex.

**3. Sharp proper conflict-free surcharge.** For \(s\ge2\), \(\binom s2>0\); hence no ordinary optimal \((n-2)\)-colouring is proper conflict-free. Colour a graph vertex \(\{a,b\}\), where \(a<b\), by \(a\). This uses precisely \(n-1\) colours and is proper: two disjoint edges cannot share their minimum endpoint. To verify the unique-neighbour condition, consider any graph vertex \(e\). If \(e\) is disjoint from \(\{n-1,n\}\), the class of colour \(n-1\), consisting only of \(\{n-1,n\}\), is a witness. Otherwise, if \(e\) contains exactly one of \(n-1,n\) and avoids \(n-2\), the class of colour \(n-2\), consisting of \(\{n-2,n-1\}\) and \(\{n-2,n\}\), has exactly one member disjoint from \(e\). In the remaining cases \(e\) is either \(\{n-1,n\}\) or contains \(n-2\) together with one of \(n-1,n\); colour \(n-3\), with edges to \(n-2,n-1,n\), contributes exactly one disjoint edge. Because \(n\ge5\), this last colour exists. Thus \(n-1\) colours suffice, completing the proof.

## Verification

A standalone pure-Python checker (`verify.py`) performs **independent** exhaustive backtracking over all normalized ordinary optimal proper colourings for \(n=5,6,7\), directly computes the number of failed neighbourhood witnesses, and compares the full histogram against the two symbolic counts (after removing the \((n-2)!\) named-colour factor). The observed unlabelled defect histograms are, respectively, \(\{1:20\}\), \(\{3:120,6:40\}\), and \(\{6:1120,9:1120\}\). The same checker independently constructs and validates the claimed \((n-1)\)-colour solution for every \(5\le n\le30\), and checks the two exceptional small graphs. Running `python3 verify.py` produces `VERIFY_OK` with no third-party dependencies. These finite experiments corroborate, and do not replace, the unrestricted combinatorial argument above.

## Relationship to prior work

The ordinary \(n-2\) Kneser chromatic number is classical (Lovász). Daneshpajouh, *On the number of star-shaped classes in optimal colorings of Kneser graphs* (first released January 14, 2022), proves the triangle rigidity of optimal star–triangle partitions; the classification is credited and reproduced here to make the new witness-defect count self-contained. Das and Santra, *Proper Conflict-Free Coloring of Undirected Path, Chordal Bipartite, and Strongly Chordal Graphs* (first released November 4, 2026), motivates the proper open-neighbourhood condition but proves results for different graph classes. Bhyravarapu et al., *Conflict-Free Coloring: Graphs of Bounded Clique Width and Intersection Graphs* (first released May 18, 2021), treat Kneser graphs for a partially coloured nonproper conflict-free variant, so their bounds are not a direct covering statement. The new result concerns the proper all-vertex variant, including the sharp one-colour surcharge and complete optimal-ordinary-colouring failure histogram.

## Limitations

This is a theorem for the two-subset Kneser family only. The known structural classification is credited rather than claimed as novel by itself. No statement is made about higher-uniformity Kneser graphs, arbitrary proper colouring palettes above \(n-2\), or the partially coloured conflict-free model. The literature comparison is necessarily subject to unindexed or otherwise unavailable work, and independent mathematical review has not been performed.

## References

1. Gautam K. Das and Kamal Santra, *Proper Conflict-Free Coloring of Undirected Path, Chordal Bipartite, and Strongly Chordal Graphs*, arXiv:2611.08534, first public version 2026-11-04. https://arxiv.org/abs/2611.08534
2. Hamid Reza Daneshpajouh, *On the number of star-shaped classes in optimal colorings of Kneser graphs*, arXiv:2201.05605, first public version 2022-01-14; *Journal of Graph Theory* 105 (2024), 230–238. https://arxiv.org/abs/2201.05605
3. Yair Caro, Mirko Petruševski and Riste Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2201.04330 (background and terminology). https://arxiv.org/abs/2203.01088
4. Sriram Bhyravarapu, Tim A. Hartmann, Hung P. Hoang, Subrahmanyam Kalyanasundaram and I. Vinod Reddy, *Conflict-Free Coloring: Graphs of Bounded Clique Width and Intersection Graphs*, arXiv:2105.08693, first public version 2021-05-18. https://arxiv.org/abs/2105.08693
5. László Lovász, *Kneser's conjecture, chromatic number, and homotopy*, *Journal of Combinatorial Theory, Series A* 25 (1978), 319–324.
