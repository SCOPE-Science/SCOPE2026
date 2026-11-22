# Point-line obstruction in the maximal-independent-set shattering complex of the Heawood graph

## Finding
Let \(H\) be the fourteen-vertex Heawood graph, the incidence graph of the Fano plane \(\operatorname{PG}(2,2)\). Its Boolean concepts are **all inclusion-maximal independent vertex sets** (equivalently, all independent dominating sets). A query is an individual vertex of \(H\); a support \(S\subseteq V(H)\) is shattered when, for every \(T\subseteq S\), some concept \(C\) satisfies \(C\cap S=T\).

**Complete classification.** A support is shattered if and only if it is independent and either (i) has at most three vertices, or (ii) has four vertices and contains both a point-vertex and a line-vertex. No support of five or more vertices is shattered. Thus the shattering face polynomial is
\[
\Phi_H(z)=1+14z+70z^2+154z^3+77z^4,
\qquad \operatorname{VCdim}=4.
\]
The complex is **nonpure**. Its inclusion-maximal shattered supports are precisely 14 triples (the seven Fano lines viewed as point triples and their seven dual line pencils) and 77 mixed independent quadruples. Under the 336 automorphisms of \(H\), these 91 facets form exactly three orbits: a triple orbit of size 14, and quadruple orbits of sizes 21 and 56. This is a complete finite classification, not a general statement about other incidence graphs or arbitrary cubic graphs.

## Assumptions and scope
Use the nonzero vectors of \(\mathbb F_2^3\) as seven points, numbered \(P_0,\dots,P_6\) by the respective binary vectors \(1,\dots,7\). The seven lines \(L_0,\dots,L_6\), with indices starting at zero, are

| Line | Point indices |
|---|---|
| \(L_0\) | 0, 1, 2 |
| \(L_1\) | 0, 3, 4 |
| \(L_2\) | 0, 5, 6 |
| \(L_3\) | 1, 3, 5 |
| \(L_4\) | 1, 4, 6 |
| \(L_5\) | 2, 3, 6 |
| \(L_6\) | 2, 4, 5 |

There is an edge between \(P_i\) and \(L_j\) exactly when \(i\) belongs to the displayed triple for \(L_j\). No edges join vertices in the same shore. An independent support is a collection of points and lines with no incidences between selected points and selected lines. Independent domination is **not** the same as ordinary domination or as selection of maximum-cardinality independent sets; the concept class contains all inclusion-maximal independent sets of different sizes.

## Proof
**Step 1: all concepts.** Write \(\mathcal P\) and \(\mathcal L\) for the full point and line shores. An independent vertex set is inclusion-maximal if and only if it dominates every vertex outside it. For a chosen point set \(A\), any maximal independent set must include every line disjoint from \(A\). Apply the Fano axioms: two points lie on exactly one line; two lines meet at exactly one point; every line has three points; every point lies on three lines. The only possibilities are:

* \(\mathcal P\) and \(\mathcal L\), both of size seven;
* \(D_p=\{P_p\}\cup\{L_j:P_p\notin L_j\}\), one for each point \(p\), of size five;
* \(R_j=\{L_j\}\cup\{P_p:P_p\notin L_j\}\), one for each line \(j\), of size five;
* \(M_{p,q}=\{P_p,P_q\}\cup\{L_j:P_p,P_q\notin L_j\}\), one for each unordered pair of distinct points, of size four.

Indeed, with zero, one, or two points these are forced, and direct incidence shows domination. With three points, the at-most-one line disjoint from them cannot dominate the four unselected points; with four points a disjoint line exists only when the four form the complement of that line, giving \(R_j\). With five or six points no line is disjoint, leaving unselected points undominated; with seven points only \(\mathcal P\) remains. Hence there are \(2+7+7+21=37\) concepts, with cardinality enumerator \(21x^4+14x^5+2x^7\).

**Step 2: independence and the upper obstruction.** Every concept is independent, so the trace that selects all of \(S\) forces \(S\) itself to be independent. No monochromatic four-point support can be shattered. For a four-point set \(X\subseteq\mathcal P\) containing a complete Fano-line triple \(T\), a concept cannot realize exactly \(T\) on \(X\): \(\mathcal P\) also includes the fourth point; a concept \(R_j\) excludes at least one member of \(T\) (every projective line meets every other); and the other concept types contain at most two points. If \(X\) contains no Fano-line triple, it is the complement of a unique Fano line \(L_j\). For any three-subset \(T\) of \(X\), exactly one Fano line is disjoint from \(T\), namely \(L_j\), so the only size-four point shore of a concept containing \(T\) is all of \(X\); again the trace selecting \(T\) while excluding the fourth point is impossible. Duality gives the same conclusion for four line-vertices. Finally, an independent five-vertex set contains at least four vertices on the same shore: two chosen lines have five distinct incident points, so they cannot coexist with three chosen point-vertices (and dually). Every larger shattered support would contain a shattered independent five-set, a contradiction. Thus any shattered support has size at most four, and a shattered four-set is mixed.

**Step 3: every mixed independent four-set is shattered.** By the Fano collineation group, mixed independent four-sets have two types: two points and two lines (21 supports), and three points with a disjoint line, together with the dual one-point/three-line case (56 supports). Collineations and point-line duality reduce all traces to two representatives:
\(A=(P_5,P_6,L_0,L_1)\) and \(B=(P_3,P_4,P_5,L_0)\).
The following explicit witness table gives, for each four-bit trace in query order, a concept of Step 1 realizing it. Every entry is a fully defined concept, rather than a numerical experimental estimate.

| Trace | Witness on \(A\) | Witness on \(B\) |
|---|---|---|
| 0000 | \(D_0\) | \(D_0\) |
| 1000 | \(R_4\) | \(R_6\) |
| 0100 | \(R_3\) | \(R_3\) |
| 1100 | \(\mathcal P\) | \(R_2\) |
| 0010 | \(D_3\) | \(R_1\) |
| 1010 | \(M_{3,5}\) | \(R_4\) |
| 0110 | \(M_{3,6}\) | \(R_5\) |
| 1110 | \(R_0\) | \(\mathcal P\) |
| 0001 | \(D_1\) | \(\mathcal L\) |
| 1001 | \(M_{1,5}\) | \(D_3\) |
| 0101 | \(M_{1,6}\) | \(D_4\) |
| 1101 | \(R_1\) | \(M_{3,4}\) |
| 0011 | \(\mathcal L\) | \(D_5\) |
| 1011 | \(D_5\) | \(M_{3,5}\) |
| 0111 | \(D_6\) | \(M_{4,5}\) |
| 1111 | \(M_{5,6}\) | \(R_0\) |

**Step 4: triples and smaller supports.** Every independent triple except a monochromatic complete Fano-line triple or dual pencil extends to a mixed independent four-set. A noncollinear point triple has a unique disjoint line; a two-point/one-line triple has the other line disjoint from those two points; use duality for the symmetric cases. Hence Step 3 shatters all these triples. For the remaining triple \((P_0,P_1,P_2)\), the eight traces in order \(000,100,010,110,001,101,011,111\) are realized by \(\mathcal L,D_0,D_1,R_5,D_2,R_3,R_1,\mathcal P\), respectively. Symmetry covers all seven line triples and seven dual pencils. Every independent pair extends to an independent triple, and every singleton extends to an independent pair, so the classification holds in degrees zero through three.

**Step 5: exact counts and facets.** There are 14 singletons and \(\binom{14}{2}-21=70\) independent pairs. Of the \(\binom{14}{3}=364\) triples, exactly \(21\cdot12-14\binom{3}{2}=210\) contain an incidence edge, leaving \(154\) independent triples. The mixed independent quadruples comprise 21 two-point/two-line sets, 28 three-point/one-line sets, and their 28 duals, totaling 77. All are maximal shattered supports. The 14 monochromatic Fano-line or pencil triples have no mixed independent extension, so they too are facets; all other triples extend to a shattered four-set. The 168 Fano collineations, with duality, form 336 automorphisms. The stabilizer of a line acts transitively on its four off-line points, proving that the three facet types constitute orbits of sizes 14, 21 and 56. This establishes the polynomial, VC dimension and nonpurity.

## Verification
Run `python3 verify_heawood.py` from the directory containing this result and its attached verifier. The program (i) constructs the Fano lines over \(\mathbb F_2^3\), (ii) compares independent-dominating sets obtained by enumerating all \(2^{14}\) vertex subsets with the independent geometric list of 37 concepts, (iii) tests all \(2^{14}\) supports against the exact 37-concept traces and the stated incidence classification, (iv) checks the 91 facets and the 336-automorphism orbit decomposition. The completed check prints `HEAWOOD_MIS_SHATTER_PASS`. These finite tests corroborate the displayed complete proof; no extrapolation from small cases is used.

## Relationship to prior work
Jahari and Alikhani (2018, arXiv:1808.07369, first public 2018-08-21) develop independent-domination polynomials, especially for paths and compound graphs. They count independent dominating sets by size, not all Boolean traces on a given support; their stated theorems do not include this Heawood shattering complex. Perarnau and Perkins (2016, arXiv:1611.01474) identify the Heawood graph as extremal for the ordinary **independence polynomial** among cubic graphs of girth at least five, and explicitly give its coefficients. That counts all independent sets, whose four-element coefficient is 147, unlike the 77 shattered four-sets above. This work credits that independence polynomial and does not reassert it as new. Other related results on maximal-independent-set shattering for cycles and whiskered graphs apply to different graph families; the Heawood graph has degree three everywhere and has no private leaves.

## Limitations
This is an exact result for one canonical 14-vertex graph, not for all generalized polygons or all incidence graphs of projective planes. It does not determine the Littlestone dimension or the homotopy type of the shattering complex. Historical priority is based on the inspected literature and indexed research comparisons; unindexed or inaccessible equivalent enumerations remain possible. The classification and 336-group orbit counts are finite and fully reproducible, but no independent mathematical audit has been performed.

## References
- S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph* (2018), arXiv:1808.07369, https://arxiv.org/abs/1808.07369 (first publicly submitted 2018-08-21).
- G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth* (2016 preprint, 2018 journal), arXiv:1611.01474, https://arxiv.org/abs/1611.01474.
