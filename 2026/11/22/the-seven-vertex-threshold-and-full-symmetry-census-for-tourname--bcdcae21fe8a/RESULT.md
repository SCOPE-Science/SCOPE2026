# The seven-vertex threshold and full symmetry census for tournament extension rank three

## Finding

Take the rank of a finite tournament relative to the class of all finite tournaments, as in the one-point-extension definition of López-Callejas and Navarro-Castillo. The least possible host order with rank at least three is **seven**. Exactly \(1{,}503{,}216\) of the \(2^{21}\) labelled seven-vertex tournaments attain this rank; up to isomorphism, exactly \(313\) of the \(456\) seven-vertex tournaments attain it.

Among those \(313\) classes, the automorphism group has order \(1\), \(3\), \(5\), \(7\), or \(21\), in respectively \(292\), \(17\), \(2\), \(1\), and \(1\) cases. These classes all have rank **exactly** three, not merely rank at least three.

The seven-point existence example is already established in the 2026 rank paper; the threshold lower bound and complete symmetry census are the contributions here.

## Assumptions and scope

A tournament is a finite set \(V\) with exactly one arc \(u\to v\) or \(v\to u\) for each distinct pair. Write \(\operatorname{rk}_T(F)\) for the rank of the induced tournament on a *specified* vertex subset \(F\subseteq V\), computed relative to all finite tournaments by the recursion:

\[\operatorname{rk}_T(F)\ge0\quad\text{always},\]

and \(\operatorname{rk}_T(F)\ge k+1\) when every orientation pattern for a fresh vertex over \(F\) is realized by some \(w\in V\setminus F\) for which \(\operatorname{rk}_T(F\cup\{w\})\ge k\). The rank of \(T\) is \(\operatorname{rk}_T(\varnothing)\). In an orientation pattern each \(u\in F\) specifies either \(w\to u\) or \(u\to w\); there are exactly \(2^{|F|}\) patterns. Only finite hosts and finite integer rank thresholds are used here. Different copies of isomorphic marked substructures may have different relative ranks.

For labelled enumeration, vertices are \(0,\ldots,6\). The \(21\) ordered pairs \((i,j)\) with \(i<j\) are listed lexicographically; bit \(e\) of an integer code is one exactly when \(i\to j\). Every tournament appears exactly once among the codes \(0,\ldots,2^{21}-1\).

## Proof

**A three-round reduction.** For any two distinct vertices \(a,b\), define the two-point extension-type set

\[P_T(a,b)=\{(\mathbf1_{w\to a},\mathbf1_{w\to b}):w\in V\setminus\{a,b\}\}.\]

By the defining recursion, \(\operatorname{rk}_T(\{a,b\})\ge1\) if and only if \(|P_T(a,b)|=4\). Therefore \(\operatorname{rk}(T)\ge3\) if and only if some vertex \(a\) has **both** an out-neighbor \(b\) and an in-neighbor \(c\) satisfying

\[|P_T(a,b)|=|P_T(a,c)|=4.\tag{1}\]

Indeed, \(\operatorname{rk}_T(\varnothing)\ge3\) is equivalent to the existence of a singleton \(\{a\}\) of rank at least two. Its two possible one-point extensions must each admit a rank-one realization; these realizations are exactly \(b\) and \(c\) in (1). This equivalence is used in every computational test.

**The sharp lower bound.** The pair-type condition needs at least four other vertices; thus fewer than six vertices cannot have rank three. Suppose a six-vertex tournament satisfies (1). The four vertices outside \(\{a,b\}\) must realize the four patterns once each. Since \(a\to b\), exactly two of those four are out-neighbors of \(a\), forcing the out-degree of \(a\) to be \(3\). Similarly, since \(c\to a\), exactly two vertices outside \(\{a,c\}\) are out-neighbors of \(a\) and \(a\not\to c\), forcing its out-degree to be \(2\), a contradiction. Hence at least seven vertices are necessary.

**Existence.** The tournament \(H_3\) with \(2^3-1=7\) vertices and rank three was already constructed and proved in Theorem 5.4 of López-Callejas--Navarro-Castillo (2026). For an independent explicit witness under the code convention above, code \(17\) satisfies (1) with \(a=3\), \(b=0\), and \(c=5\): \(3\to0\), \(5\to3\), and the four possible pairs \((\mathbf1_{w\to3},\mathbf1_{w\to0})\) and \((\mathbf1_{w\to3},\mathbf1_{w\to5})\) each occur among the other five vertices. Both directions of the singleton extension thus survive two more rounds.

**Rank cannot exceed three on seven vertices.** Rank at least four would imply a three-vertex marked subset of rank at least one, hence one which realizes all \(2^3=8\) orientation patterns among unmarked vertices. That would require at least \(3+8=11\) vertices. Thus every seven-vertex rank-at-least-three host has rank exactly three.

**Labelled and unlabelled complete census.** The standalone source `verify.cpp` enumerates all \(2^{21}\) tournament codes, applies (1), and obtains \(1{,}503{,}216\) labelled rank-three hosts. To pass to isomorphism types, the source enumerates all \(7!=5040\) vertex permutations and relabels each adjacency code. It marks each entire orbit and counts one representative per orbit; the automorphism-group order is \(5040\) divided by the orbit size. This yields exactly \(456\) orbits in all, \(313\) satisfying (1), and the following disjoint census:

| Automorphism-group order | Rank-three classes | Below-rank-three classes |
|---:|---:|---:|
| 1 | 292 | 107 |
| 3 | 17 | 30 |
| 5 | 2 | 2 |
| 7 | 1 | 0 |
| 9 | 0 | 4 |
| 21 | 1 | 0 |

The orbit-stabilizer identity independently checks the labelled rank-three tally:

\[292\cdot5040+17\cdot1680+2\cdot1008+720+240=1{,}503{,}216.\]

The rank-negative orbit weights total \(593{,}936\), and together the two labelled totals equal \(2^{21}\). The \(456\) overall isomorphism classes independently agree with the published tournament catalogue of Brendan McKay.

## Verification

Compile `verify.cpp` with a C++17 compiler and execute the binary. The program exhaustively checks the criterion for every labelled tournament of orders one through seven, enumerates all relabelling orbits at seven vertices, checks the complete automorphism-order table above, and prints `ALL_CHECKS_OK`. It explicitly checks that its first rank-three code is \(17\).

The independent script `independent_check.py` implements the three-round rank recursion directly instead of using criterion (1), comparing the two predicates for all tournaments through order five and 1,000 reproducible sampled masks each at orders six and seven (fixed seed 771). This is a cross-check of the reduction, not an exhaustive certificate at six or seven; the C++ scan and orbit enumeration are exhaustive there. No downloaded tables are used as input to the calculation.

## Relationship to prior work

López-Callejas and Navarro-Castillo, *A rank function for Fraïssé classes and the rank property* (first posted April 15, 2026), Definition 2.3 and Section 5, introduce the extension rank and establish \(\operatorname{rk}(H_t)=t\) for tournaments \(H_t\) on \(2^t-1\) vertices. **The seven-vertex upper bound is prior work**, not a new discovery. Their Section 5 does not give a classification or complete rank census of the seven-vertex tournaments, and its construction alone does not prove the six-vertex lower bound.

Brendan McKay's independent database lists \(456\) nonisomorphic seven-vertex tournaments without classifying them by extension rank. Related published work on rank-three onset in *undirected* finite graphs concerns a different class of one-point-extension types and does not provide this directed-tournament enumeration. Related published directed colour-refinement counts are for a different invariant and cannot determine these rank classes. Thus the present full orbit census is not inferred from either type of table.

## Limitations

Historical novelty is assessed relative to inspected literature and accessible public records; an earlier unindexed calculation of the same rank-census statistic remains possible. The exhaustive numerical assertion is conditional on the stated bit encoding and the supplied source being executed as provided. The proof of the criterion and lower bound is mathematical; enumeration of all \(2^{21}\) codes and orbits is an exact finite computation, not a statement about larger tournaments or countably infinite tournaments. The source's group order distribution does not classify the detailed isomorphism structures of those groups, only their sizes. No independent peer validation is claimed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461 (first public April 15, 2026), especially Definition 2.3, Lemma 5.3 and Theorem 5.4. https://arxiv.org/abs/2604.14461 and https://arxiv.org/html/2604.14461
2. B. D. McKay, *Combinatorial Data: Digraphs / Tournaments*, seven-vertex catalogue (456 nonisomorphic tournaments). https://users.cecs.anu.edu.au/~bdm/data/digraphs.html
