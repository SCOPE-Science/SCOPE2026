# A sharp sliding-connectivity threshold for minimum zero-forcing sets of path complements

## Finding
For each integer \(n\ge5\), let \(G_n=\overline{P_n}\) be the complement of the path with labelled vertex set \(\{0,1,\ldots,n-1\}\), where distinct vertices are adjacent exactly when their labels differ by at least two. Let \(\mathcal Z_n\) be the graph of all minimum ordinary zero-forcing sets in \(G_n\), with adjacency when precisely one initially blue vertex is replaced by another. Let \(\mathcal S_n\) retain only replacements along edges of \(G_n\). Then:

1. The minimum zero-forcing number is \(n-3\), and there are exactly \((n-3)^2+1\) minimum sets. These two numerical facts were previously known; they are included to specify the state space, not as novelty claims.
2. At \(n=5\), \(\mathcal Z_5\cong C_5\) while \(\mathcal S_5\cong K_2\sqcup3K_1\).
3. For every \(n\ge6\), **both** reconfiguration graphs are connected, and their exact edge counts are
   \[
   |E(\mathcal Z_n)|=\frac{n^3-3n^2-32n+126}{2},\qquad
   |E(\mathcal S_n)|=\frac{n^3-5n^2-22n+118}{2}.
   \]
   Consequently, exactly \(n^2-5n+4\) otherwise legal one-token replacements are prohibited by the physical adjacency requirement. The fraction of prohibited moves among all exchange moves tends to zero as \(n\to\infty\).

The new claim concerns **reconfiguration connectivity and exact transition counts**, including the sharp five-vertex exception. It does not claim the minimum forcing number or number of minimum sets as new.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. A blue vertex with exactly one white neighbor in \(G_n\) may color that neighbor blue; the initial blue set is *zero forcing* if all vertices can eventually become blue. Reconfiguration always preserves both zero-forcing feasibility and minimum cardinality. An unrestricted exchange replaces one blue vertex by any different white vertex; an adjacent slide requires that the replaced and replacement vertices be adjacent in the original \(G_n\). The corresponding three-vertex **white complements** are convenient state labels: replacing blue vertex \(v\) by blue vertex \(u\) changes white set \(T\) to \((T\setminus\{u\})\cup\{v\}\), with the same adjacency restriction \(|u-v|\ge2\) for a slide.

## Proof
**Lemma 1 (exact state criterion).** A three-element white set \(T\subseteq\{0,\ldots,n-1\}\), for \(n\ge5\), has zero-forcing blue complement if and only if
\[
\exists a\in\{0,\ldots,n-3\}:\quad a,a+2\in T,\quad a+1\notin T.
\]
If four or more vertices are initially white, a blue vertex would require at least three neighbors among them in the original path in order to have at most one white neighbor in its complement. This is impossible, as a path vertex has degree at most two. Hence no forcing set has fewer than \(n-3\) blue vertices. For three white vertices, an initial force is possible precisely when a blue center \(a+1\) has the two original-path neighbors \(a,a+2\) white, and forces the third white vertex. After that force, only \(a,a+2\) remain white. One of the path positions \(a-1\) or \(a+3\) exists (since \(n\ge5\)), is now blue, and is adjacent in the path to exactly one of the remaining whites, so it forces the other in the complement. The final white vertex has a blue neighbor in the complement and is forced. Thus the criterion is sufficient, and the degree bound makes it necessary.

There are \((n-2)(n-3)\) incidences between a valid white triple and a designated witness pair \(\{a,a+2\}\): choose \(a\) in \(n-2\) ways and a third white vertex avoiding \(a,a+1,a+2\) in \(n-3\) ways. A triple contains two witness pairs exactly when it is \(\{a,a+2,a+4\}\), of which there are \(n-4\). No triple has three witness pairs. Inclusion-exclusion therefore yields \((n-2)(n-3)-(n-4)=(n-3)^2+1\) distinct minima.

**Lemma 2 (exact transitions).** For \(0\le a<b<n\), let \(K_{ab}\) be the set of all third labels \(c\) making \(\{a,b,c\}\) a valid white triple. With all sets intersected with \(\{0,\ldots,n-1\}\), these completion sets are exactly
\[
K_{ab}=\begin{cases}
\{a-2,b+2\}\cap[0,n-1],& b-a=1,\\
[0,n-1]\setminus\{a,a+1,b\},& b-a=2,\\
\{a-2,a+2,b-2,b+2\}\cap[0,n-1],&b-a\ge3.
\end{cases}
\]
In the final case the displayed members are distinct from \(a,b\); repetitions, if any, are treated set-theoretically. Here \([0,n-1]\) means the integer labels in that interval. This follows directly from Lemma 1: a witness pair either is \(\{a,b\}\) or consists of the third vertex together with one of \(a,b\).

Every unrestricted exchange edge has a **unique** common two-element white subset, so
\[
|E(\mathcal Z_n)|=\sum_{0\le a<b<n}\binom{|K_{ab}|}{2}.
\]
The only unrestricted edges missing from the sliding graph are those whose exchanged third labels are consecutive in the original path. Writing \(c_{ab}=|\{c:c,c+1\in K_{ab}\}|\), we obtain
\[
|E(\mathcal S_n)|=\sum_{a<b}\left(\binom{|K_{ab}|}{2}-c_{ab}\right).
\]
The completion table shows that \(c_{ab}=0\) unless \(b-a\in\{2,3,5\}\). For distance two, \(c_{ab}=n-4\) at the two endpoint positions and \(c_{ab}=n-5\) at all other positions, giving total \((n-4)(n-3)\). For distances three and five the respective totals are \(n-3\) and \(n-5\). Thus, for \(n\ge6\),
\[
\sum_{a<b}c_{ab}=(n-4)(n-3)+(n-3)+(n-5)=n^2-5n+4.
\]
For completeness, when \(n\ge9\), grouping the unrestricted sum by differences \(b-a=1,2,3,4,\ge5\) gives, respectively,
\[
n-5,\quad (n-2)\binom{n-3}{2},\quad 6n-30,\quad 3n-20,\quad 3n^2-39n+130.
\]
Their sum is \((n^3-3n^2-32n+126)/2\). At \(n=6,7,8\), the same five grouped contributions are, respectively, \((1,12,7,0,1)\), \((2,30,12,2,3)\), and \((3,60,18,4,10)\), which yield the stated cubic formula. Subtraction proves the sliding formula.

**Lemma 3 (sharp connectivity threshold).** For each \(0\le a\le n-3\), define the fibre
\[
F_a=\{\{a,a+2,t\}:t\notin\{a,a+1,a+2\}\}.
\]
All valid states are in at least one fibre. Holding the pair \(a,a+2\) fixed, the allowed sliding exchanges of the third vertex form the complement of the induced subgraph of the original path on its \(n-3\) allowed positions. When \(n\ge7\), this is connected: the complement of an induced linear forest on at least four vertices is connected, since a disconnected complement would force an original-path complete bipartite cut of minimum part sizes \((1,3)\) or \((2,2)\), impossible respectively by maximum degree two or acyclicity.

Fibres \(F_a\) and \(F_{a+2}\) overlap in state \(\{a,a+2,a+4\}\) whenever \(a+4<n\). Hence the even-indexed fibres form a connected chain and the odd-indexed fibres form another. They are joined by the legal slide
\[
\{0,2,3\}\longleftrightarrow\{0,3,5\},
\]
which links \(F_0\) to \(F_3\) because \(|5-2|=3\). Therefore \(\mathcal S_n\) is connected for \(n\ge7\).

At \(n=6\), the only disconnected individual fibres are \(F_0\) (the otherwise separated state \(\{0,2,4\}\) also lies in the connected fibre \(F_2\)) and \(F_3\) (the state \(\{1,3,5\}\) also lies in \(F_1\)). The remaining fibre connections and the same cross-parity slide connect all ten states. At \(n=5\), the five states are \(\{0,1,3\},\{0,2,3\},\{0,2,4\},\{1,2,4\},\{1,3,4\}\). Their only slide joins \(\{0,1,3\}\) with \(\{1,3,4\}\), whereas their unrestricted exchange graph is a five-cycle. This proves all connectivity assertions. Since \(\mathcal S_n\) is a spanning subgraph of \(\mathcal Z_n\), the latter is connected for every \(n\ge6\).

## Verification
Two standalone, dependency-free programs are included. `checker_direct.py` applies the original zero-forcing rule to all candidate white triples and all smaller blue sets for \(5\le n\le12\), builds both relocation graphs, checks the exact edge formulas and the connected-component sizes. `checker_structural.py` independently enumerates admissible triples from the local witness condition, validates the pair-completion table, the two edge formulas and the fibre membership for \(5\le n\le60\). The direct checker checks its smallest-cardinality lower bound independently, while the proof above establishes it for every \(n\). Invoke `python checker_direct.py` and `python checker_structural.py` from the extracted package directory.

## Relationship to prior work
Geneson, Haas and Hogben's *Reconfiguration graphs of zero forcing sets* (arXiv:2009.00220, publicly available September 1, 2020) defines one-vertex exchange graphs and proves general properties, but does not classify the reconfiguration of path complements. Curl, Fallat, Moruzzi, Reinhart and Young's *On the zero forcing number of the complement of graphs with forbidden subgraphs* (arXiv:2206.03932, June 8, 2022) establishes the minimum number for complements of nonstar trees; it does not give the relocation transition formulas. Previously indexed *Zero-forcing polynomials of complements of paths and cycles* and *Minimal-fort hypergraphs and zero-forcing polynomials of \(\overline{P_n}\)* give the minimum-state count, which this result explicitly treats as prior work. The present theorem adds a distinct all-order reconfiguration connectivity threshold and exact transition enumeration. An equivalent result in unindexed literature cannot be excluded.

## Limitations
The result is restricted to standard ordinary zero forcing on complements of **paths**, not all tree complements. No general exact diameter formula is established or claimed. The historical novelty judgment is best-knowledge, based on the indexed comparisons and inspected primary texts described above; the full text behind some index records could not be accessed. The proof is mathematical and all-order, but has not received independent human or external mathematical audit.

## References
1. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (first submitted 2020-09-01), https://arxiv.org/html/2009.00220v1.
2. E. Curl, S. Fallat, R. Moruzzi Jr., C. Reinhart, D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932 (first submitted 2022-06-08), https://arxiv.org/abs/2206.03932.
3. *Zero-forcing polynomials of complements of paths and cycles*, indexed public mathematical finding (2026-10-18), consulted for prior state-count coverage.
4. *Minimal-fort hypergraphs and zero-forcing polynomials of \(\overline{P_n}\)*, indexed public mathematical finding (2026-11-02), consulted for prior state-count coverage.
