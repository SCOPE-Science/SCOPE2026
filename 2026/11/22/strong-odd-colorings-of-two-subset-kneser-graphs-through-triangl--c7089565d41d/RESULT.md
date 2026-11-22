# Strong odd colorings of two-subset Kneser graphs through triangle packings

## Finding

For every integer \(n\ge 5\), the strong odd chromatic number of the Kneser graph \(G_n=\mathrm{KG}(n,2)\), whose vertices are the edges of \(K_n\) and whose adjacency is disjointness, is

\[
\chi_{\mathrm{so}}(G_n)=
\begin{cases}
\dfrac{n(n-1)}6,&n\equiv1,3\pmod6,\\[2pt]
\dfrac{n(n-1)+16}6,&n\equiv5\pmod6,\\[2pt]
1+\dfrac{(n-1)(n-2)}6,&n\equiv2,4\pmod6,\\[2pt]
1+\dfrac{(n-1)(n-2)+16}6,&n\equiv0\pmod6.
\end{cases}
\]

There is an exact classification of all optimal *unlabeled* color partitions, meaning color names are disregarded. For odd \(n\), select any maximum edge-disjoint triangle packing of \(K_n\); each packed triangle is one color class, and each uncovered edge is a singleton color class. For even \(n\ge8\), choose a vertex \(c\) of \(K_n\), give the entire star at \(c\) one color, then use a maximum triangle packing of \(K_{n-1}=K_n-c\) and singleton classes for its uncovered edges. For \(n=6\), both these types attain the optimum: the no-star type using a maximum triangle packing of \(K_6\), and the full-star type using a maximum triangle packing of \(K_5\). These exhaust all optimal partitions. The \(n=5\) scalar value \(6\) is previously known; the general formula and partition classification are the contribution here.

## Assumptions and scope

All graphs are simple, finite and undirected. A *strong odd coloring* is a proper vertex coloring in which, for every vertex \(v\) and every color, the number of neighbors of \(v\) carrying that color is either zero or odd. The neighborhood is *open*. A color class of \(G_n\) corresponds to an intersecting family of edges in \(K_n\). A triangle packing is a family of triangles of \(K_n\) whose edge sets are disjoint. A maximum packing has the largest possible number of triangles, and its *leave* is the set of edges not covered by packed triangles.

The graphs \(G_n\) are considered for all integers \(n\ge5\), and only the minimum number of colors and the corresponding partitions are claimed; no count of named optimal colorings or enumeration of maximum triangle packings is asserted.

## Proof

**1. Determine every permissible color class.** A nonempty independent set of \(G_n\) is a pairwise-intersecting collection \(F\) of edges of \(K_n\). If its size is at least three, either all edges have a common endpoint, or exactly three edges form a triangle. Indeed, if \(ab,ac\in F\) and a third edge does not contain \(a\), it must be \(bc\), and any edge meeting all three triangle edges is one of these edges (for \(n\ge5\)). Thus each \(F\) is a star subfamily or a three-edge triangle.

For a star subfamily of size \(t\ge2\), centered at \(a\) with leaf set \(T\), an edge \(uv\) not incident with \(a\) has \(t-|\{u,v\}\cap T|\) neighbors belonging to that color class. If \(t=2\), two nonleaves can be chosen because \(n\ge5\), producing the forbidden even positive count \(2\). If \(3\le t<n-1\), choose one leaf and one nonleaf to obtain \(t-1\); for odd \(t\) this is an even positive count. For even \(t\ge4\), choose two leaves to obtain the even positive count \(t-2\). Therefore there are no permitted proper star subfamilies of cardinality at least two. A full star has \(t=n-1\), and every edge disjoint from its center has exactly \(n-3\) neighbors of that color; this is odd precisely when \(n\) is even. A triangle class passes the rule because an edge of \(K_n\) is disjoint from exactly \(0\), \(1\) or \(3\) of its three edges. A singleton passes trivially. Consequently, the complete permitted color-class list is: singleton edges, full triangles, and (for even \(n\)) full stars.

**2. Reduce colorings to a packing problem.** At most one full star occurs in a partition, since any two full stars overlap in one edge. Without a full star, using \(t\) triangle classes and singleton colors on all remaining edges yields exactly \(\binom n2-2t\) colors. Thus the optimum within this type is \(\binom n2-2P(n)\), where \(P(v)\) is the maximum number of edge-disjoint triangles of \(K_v\). When \(n\) is even and a full star is chosen, the complement of its edges is \(K_{n-1}\), and the minimum becomes \(1+\binom{n-1}2-2P(n-1)\). Every maximizing packing produces a valid coloring, and equality forces the packed triangles to be maximum. This proves all optimizer-structure assertions once the better of the two costs is identified.

**3. Use the classical maximum triangle-packing theorem.** The Schönheim maximum-packing theorem gives

\[
P(v)=\frac{\binom v2-L(v)}3,\qquad
L(v)=\begin{cases}
0,&v\equiv1,3\pmod6,\\
v/2,&v\equiv0,2\pmod6,\\
(v+2)/2,&v\equiv4\pmod6,\\
4,&v\equiv5\pmod6.
\end{cases}
\]

Here \(L(v)\) is the smallest possible number of uncovered edges, realized respectively by the empty leave, a one-factor, a tripole, or a four-cycle. This is the cited classical design-theoretic theorem, not a new claim; a complete construction-based exposition is listed below.

For odd \(n\), the no-star value is the only option. For even \(n\), subtracting the full-star cost from the no-star cost yields \((2n-12)/3\), \((2n-4)/3\), and \((2n-2)/3\), respectively, when \(n\equiv0,2,4\pmod6\). The costs tie only for \(n=6\) and the full-star option is strictly better for even \(n\ge8\). Substituting the leave sizes gives the four displayed formulas and exactly the stated optimal partitions. This completes the proof.

## Verification

The attached standalone `checks/check_classes.cpp` enumerates **every** subset of edges of \(K_n\) for \(n=5,6,7\), directly tests independence and all neighborhood parity conditions, checks the three permitted color-class types, and computes a full-set optimal-color partition via subset dynamic programming. It finds \(20,41,56\) admissible nonempty color classes, no counterexamples to the structural lemma, and exact minima \(6,7,7\).

The separately implemented `checks/check_packings.py` formulates maximum triangle packings as a binary integer program, checks exact solver optimality and theoretical leave sizes, constructs both coloring types, and directly checks the disjointness and strong-odd requirements for every underlying edge. The runs \(n=5,6,7,8,9,10\) agree with the formulas. Outputs are in the adjacent `.out` files. These finite checks corroborate, but do not replace, the structural proof and the cited infinite packing theorem.

To reproduce: compile the C++ source with `g++ -std=c++17 -O2 checks/check_classes.cpp -o check_classes && ./check_classes`; execute the Python source with Python 3, NumPy and SciPy available using `python3 checks/check_packings.py`.

## Relationship to prior work

Kwon and Park introduce strong odd coloring and analyze sparse graph bounds; Caro, Petruševski, Škrekovski and Tuza extend the theory to further graph families. Their inspected studies do not state this rank-two Kneser formula or classify its optimal partitions. In later work, Caro et al. prove an odd-independence theorem for general Kneser graphs and explicitly establish the isolated \(\mathrm{KG}(5,2)\) (Petersen) value \(\chi_{\mathrm{so}}=6\), which is credited here. That odd-independence theorem alone does not yield the optimal partitions or the exact color numbers for \(n\ge6\). The maximum triangle-packing leave theorem is classical; the graph-color class characterization and the resulting reduction distinguish the present claim from that design theorem. Searches found no exact antecedent, but this does not establish absolute publication priority.

## Limitations

The result is confined to the graph family \(\mathrm{KG}(n,2)\) for \(n\ge5\) and the ordinary *open-neighborhood* strong odd coloring. It does not cover higher-rank Kneser graphs, and it does not enumerate all named optimum colorings or all maximum triangle packings. Its infinite-order existence statement depends explicitly on the classical Schönheim packing theorem, while the newly established class classification and optimization reduction are proved above. Literature priority remains provisional; no independent external mathematical audit has been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, initial public version January 22, 2024. https://arxiv.org/abs/2401.11653
2. Y. Caro, M. Petruševski, R. Škrekovski and Zs. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, initial public version October 3, 2024. https://arxiv.org/abs/2410.02336
3. Y. Caro, M. Petruševski, R. Škrekovski and Zs. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763, first public September 25, 2025; especially Proposition 14 and Theorem 16. https://arxiv.org/abs/2509.20763
4. J. Schönheim, *On Maximal Systems of \(k\)-Tuples*, *Studia Scientiarum Mathematicarum Hungarica* **1** (1966), 363–368. For an accessible construction-based exposition and the four leave cases, see *4.2. Maximum Packings* (ETSU design theory course notes, revised May 23, 2022), Theorem 4.2.A. https://faculty.etsu.edu/gardnerr/Design-Theory/notes-Design-Theory-LR2/Design-Theory-LR2-4-2.pdf
