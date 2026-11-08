# Minimum isolating sets and three-step reconfiguration in \(\operatorname{KG}(n,2)\)

## Finding

For every integer \(n\ge5\), put \(G_n=\operatorname{KG}(n,2)\). Its vertices are the two-element subsets of \([n]\), adjacent when disjoint. A set \(S\subseteq V(G_n)\) is **isolating** when the graph induced by \(V(G_n)\setminus N_{G_n}[S]\) contains no edge. The vertex set of \(G_n\) is canonically the edge set of \(K_n\); hence a set of three Kneser vertices is a three-edge simple graph on \([n]\).

**Theorem.** The minimum isolating size is \(\iota(G_n)=3\), and every minimum isolating set corresponds precisely to a three-edge graph of one of four types: \(K_3\), \(K_{1,3}\), \(P_3\sqcup K_2\), or \(3K_2\), with arbitrary additional isolated vertices. Equivalently, every triple of distinct edges of \(K_n\) is minimum isolating **except** a three-edge path \(P_4\). Consequently the number of minimum isolating sets is
\[
 b_n=\binom{\binom n2}{3}-12\binom n4.
\]

Let \(\mathcal I_n\) be the simple graph with all minimum isolating sets as vertices, and adjacent states \(S,T\) exactly when \(|S\triangle T|=2\). Then \(\mathcal I_n\) is connected, with
\[
 \operatorname{diam}(\mathcal I_n)=3\qquad(n\ge5).
\]
Writing \(m=\binom n2\), its permitted edge patterns have the following counts and degrees:

| Three-edge type | Number of configurations | Degree in \(\mathcal I_n\) |
| --- | ---: | ---: |
| \(K_3\) | \(\binom n3\) | \(3\binom{n-2}{2}\) |
| \(K_{1,3}\) | \(n\binom{n-1}{3}\) | \(3\binom{n-2}{2}\) |
| \(P_3\sqcup K_2\) | \(n\binom{n-1}{2}\binom{n-3}{2}\) | \((3n^2-7n-22)/2\) |
| \(3K_2\) (only \(n\ge6\)) | \(15\binom n6\) | \((3n^2-3n-42)/2\) |

For example, the configuration counts for \(n=5,6,7,8\) are \(60,275,910,2436\), and the corresponding numbers of reconfiguration edges are \(270,2880,16800,68670\). Moreover, the natural embedding \(\mathcal I_n\subseteq J(\binom n2,3)\) into the Johnson graph is **not** distance preserving.

## Assumptions and scope

Graphs are finite, simple and undirected. The order parameter \(n\) is any integer at least five. The path \(P_4\) denotes exactly three edges on four distinct vertices, whereas \(P_3\) denotes two consecutive edges on three vertices. Isolated vertices of the associated three-edge graph are ignored in its type. Two Kneser vertices are adjacent precisely when their underlying edges of \(K_n\) are vertex-disjoint. A move exchanges one selected Kneser vertex for any different unselected Kneser vertex; no adjacency restriction on the exchanged vertices is imposed.

The original numerical isolation number for the Petersen graph \(\operatorname{KG}(5,2)\) is explicitly recorded in Caro--Hansberg (2015) and is **not** claimed as new. The contribution here is the all-order complete structure, number and degrees of all minimum configurations, and the three-step mobility theorem.

## Proof

**1. No set of size at most two isolates.** By monotonicity of the isolating property it suffices to rule out two-element selections. If the selected edges of \(K_n\) are disjoint, say \(ab,cd\), then the unselected Kneser vertices \(ac,bd\) each intersect both selected edges but are disjoint from each other. Thus they survive outside the closed neighborhood and are adjacent in \(G_n\). If the selected edges meet, say \(ab,ac\), choose \(d\notin\{a,b,c\}\); the unselected Kneser vertices \(bc,ad\) survive and are disjoint. Hence \(\iota(G_n)\ge3\).

**2. The four permitted shapes.** Suppose three distinct edges \(F\) are selected. A Kneser vertex is outside \(N[F]\) precisely when its two-element subset is not selected and intersects each selected edge. A three-edge simple graph, after removing isolated vertices, is one of \(K_3,K_{1,3},P_3\sqcup K_2,3K_2,P_4\). For a triangle, any two-set meeting all three triangle edges is one of the three selected edges, so no vertex survives. For three disjoint edges, a two-set cannot meet all three, so no vertex survives. For the star with edges \(ab,ac,ad\), the surviving edges are exactly \(ax\) with \(x\notin\{a,b,c,d\}\), hence pairwise intersect. For \(P_3\sqcup K_2\), say edges \(ab,ac,de\) on five distinct endpoints, the surviving edges are precisely \(ad,ae\), again intersecting. For \(P_4\), say selected edges \(ab,bc,cd\), the unselected edges \(ac,bd\) both meet all three selected edges yet are disjoint. Hence exactly the four stated shapes isolate, and every such triple is minimum.

**3. Exact count and degree types.** A labelled four-subset supports \(4!/2=12\) copies of the three-edge path \(P_4\). As every triple of distinct edges has exactly one type, subtraction gives \(b_n=\binom{m}{3}-12\binom n4\). Directly counting the four permitted shapes gives the rows in the table. In the full Johnson graph \(J(m,3)\), every triple has degree \(3(m-3)\). A replacement is illegal exactly when the new triple is a \(P_4\). When deleting one edge from a star or triangle, the remaining two-edge path has exactly \(2(n-3)\) extensions to a \(P_4\), giving \(6(n-3)\) illegal moves. When deleting one edge from a three-edge matching, the two surviving disjoint edges admit four joining edges producing a \(P_4\), giving twelve illegal moves. For a \(P_3\sqcup K_2\), deleting the isolated edge allows \(2(n-3)\) illegal extensions, while deleting either of the two adjacent edges allows four, for \(2n+2\) forbidden moves. Subtracting these values from \(3(m-3)\) gives all displayed degrees.

**4. All-order diameter: finite universal certificate.** Take any ordered pair \((A,B)\) of minimum configurations. Their six listed edges (three in \(A\), three in \(B\), with possible repetition across the lists) have exactly twelve endpoint positions, and are supported on at most twelve distinct graph vertices. Whether a triple is of type \(P_4\), and whether a shortest exchange sequence exists using only edges of \(A\cup B\), depend solely on the equality relation among these twelve endpoint positions, independent of \(n\). Every equivalence relation has a unique restricted-growth representation: the first label is zero and each subsequent label is at most one larger than the previous maximum. There are exactly \(B_{12}=4,213,597\) such patterns.

The self-contained exhaustive checker `verify_patterns.cpp` traverses every one of these patterns. It discards self-loops, repeated edges within either triple, and any initial or target triple inducing \(P_4\). For each of the remaining 500,759 valid ordered patterns, it forms the at most six distinct edges of \(A\cup B\) and uses breadth-first search on the three-edge subsets of this union, with moves replacing one edge and with \(P_4\) states excluded. Every pattern admits a legal path of length at most three; the maximum distance found is three. The checked partition space includes every possible ordered pair in every \(K_n\), with unused ground vertices irrelevant. Therefore all pairs of minimum configurations in \(\mathcal I_n\) have distance at most three, for every \(n\ge5\). This is a finite exhaustive proof of the universally quantified diameter bound, not a finite-size extrapolation.

For the reverse inequality, both \(A=\{01,02,03\}\) and \(B=\{12,14,24\}\) are permitted triples in \(K_n\) for every \(n\ge5\), but share no edge. Each replacement alters only one selected edge, so their distance is at least three. It follows that the diameter is exactly three and the reconfiguration graph is connected.

**5. Non-isometry.** Let \(A=\{01,02,03\}\) and \(B=\{01,14,23\}\). These permitted triples share one edge, so their distance in \(J(m,3)\) is two. Any two-step path would have an intermediate state containing the common edge \(01\), one of \(02,03\), and one of \(14,23\). All four possibilities form a forbidden \(P_4\). Thus the distance in \(\mathcal I_n\) is at least three and, by Step 4, equals three.

## Verification

The standalone programs `verify_direct.py` and `verify_patterns.cpp` and their actual output files `direct_output.txt` and `patterns_output.txt` are bundled alongside this document. Use Python 3 with only the standard library and a C++17 compiler:

```
python3 verify_direct.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_patterns.cpp -o pattern_check
./pattern_check
```

The Python program constructs Kneser adjacency independently, verifies there are no isolating sets smaller than three for \(5\le n\le8\), exhaustively classifies all three-sets, tests degree formulas and all reconfiguration edges, computes every source distance through \(n=7\), and tests connectivity from one source at \(n=8\). The C++ program checks the complete universal twelve-endpoint pattern space, not merely graphs through a bounded order. Its output is `restricted_growth_patterns=4213597`, `valid_pairs=500759`, `pairs_connected_in_at_most_3=500759`, `counterexamples=0`, and `maximum_distance=3`. The two checks have different constructions and do not depend on external files.

## Relationship to prior work

Caro and Hansberg introduced the general isolation-number framework and explicitly stated \(\iota(P)=3\) for the Petersen graph \(P\cong\operatorname{KG}(5,2)\) in Example 2.1 of their 2015 preprint. Their inspected introduction, core definitions and example, graph-family section, and open problems do not present the four-type minimum-set classification, full multiplicity, degree profile, or diameter-three reconfiguration theorem. Boyer and Goddard (2024) study disjoint isolating sets and extremal equality graphs, rather than these Kneser configuration families. The equivalence of isolation and vertex-edge domination is explicitly addressed in their introduction. Source inspection and phrase searches found no matching full theorem, but the absence of a search hit is not proof of historical novelty.

## Limitations

The proof of the diameter bound uses a transparent, finite universal exhaustive certificate rather than a symbolic case-by-case exchange lemma. Correctness therefore depends on the disclosed restricted-growth enumeration and BFS implementation, both of which can be replayed and inspected. The direct Python checks alone cover only the stated finite sizes and do not prove the all-order theorem. The minimum isolation number for the Petersen graph was known; it is not presented as a new numerical result. Results about all minimum configurations for larger Kneser parameters are not claimed. Unindexed or inaccessible prior calculations remain a historical priority risk; independent scholarly review has not occurred.

## References

1. Yair Caro and Adriana Hansberg, *Partial domination—the isolation number of a graph*, arXiv:1504.08055v1, submitted 2015-04-30. https://arxiv.org/abs/1504.08055 . See Section 1.2 and Example 2.1(3).
2. Geoffrey Boyer and Wayne Goddard, *Disjoint isolating sets and graphs with maximum isolation number*, arXiv:2401.03933, first submitted 2024-01-08. https://arxiv.org/abs/2401.03933 . See Introduction, Theorem 2, and Theorem 11.
