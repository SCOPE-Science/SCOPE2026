# Eight rank-three theories of finite Kneser graphs and the sharp Rado threshold

## Finding
Fix integers \(1\le k\le n\). The **Kneser graph** \(\mathrm{KG}(n,k)\) has as vertices all \(k\)-element subsets of \(\{1,\ldots,n\}\); distinct vertices are adjacent precisely when they are disjoint. In the pure simple-graph language with equality, write \(G\equiv_3 H\) when the two graphs agree on every first-order sentence of quantifier rank at most three.

**Theorem.** Exactly **eight** \(\equiv_3\)-classes occur among finite Kneser graphs. The parameter conditions, mutually disjoint and exhaustive, and their smallest representatives within this family are:

| Class | Exact parameter condition | Smallest representative | Vertices |
| --- | --- | --- | ---: |
| Singleton | \(k=n\) | \(\mathrm{KG}(1,1)\) | 1 |
| Two-vertex clique | \(k=1,n=2\) | \(\mathrm{KG}(2,1)\) | 2 |
| Larger cliques | \(k=1,n\ge3\) | \(\mathrm{KG}(3,1)\) | 3 |
| Larger edgeless graphs | \(1<k<n<2k\) | \(\mathrm{KG}(3,2)\) | 3 |
| Nontrivial matchings | \(k\ge2,n=2k\) | \(\mathrm{KG}(4,2)\) | 6 |
| Mixed nonedge extension | \(k\ge3,2k+1\le n\le3k-2\) | \(\mathrm{KG}(7,3)\) | 35 |
| Uniform triangle-free extension | \(k\ge2,n=3k-1\) | \(\mathrm{KG}(5,2)\) | 10 |
| Full two-point extension | \(k\ge2,n\ge3k\) | \(\mathrm{KG}(6,2)\) | 15 |

In the last class every pair of distinct vertices admits a third vertex with each of the four possible adjacency signatures. Consequently, for \(k\ge2\) with \(n\ge2k+1\),
\[
\mathrm{KG}(n,k)\equiv_3 R\quad\Longleftrightarrow\quad n\ge3k,
\]
where \(R\) is the countable Rado graph. The first Kneser representative has \(\binom62=15\) vertices. This is **not** the smallest finite two-existentially-closed graph among all simple graphs.

## Assumptions and scope
The language has one symmetric irreflexive adjacency relation and equality, with unbounded variables but quantifier rank bounded by three. No counting or additional predicates are allowed. The domain is nonempty and consists of the distinct \(k\)-subsets of a labelled \(n\)-set; the classification concerns the resulting unlabelled graphs. All integer parameter boundaries in the table are inclusive as written. Rank-three equivalence is not graph isomorphism and does not imply agreement at rank four or higher.

For distinct vertices \(a,b\), let \(e(a,b)\in\{0,1\}\) denote adjacency and define their **third-vertex profile**
\[
P(a,b)=\{(e(a,z),e(b,z)):z\notin\{a,b\}\}\subseteq\{0,1\}^{2}.
\]
Write \(P_0=\{(0,0),(0,1),(1,0)\}\) and \(P_1=P_0\cup\{(1,1)\}\). Let \(\mathcal S(G)\) comprise, for each value \(e\), the set of profiles of ordered distinct pairs having adjacency value \(e\). Empty categories are explicitly absent. This is a set of *profiles*, not a list of multiplicities.

## Proof
**1. Three-round invariant.** For nonempty vertex-transitive simple graphs, \(G\equiv_3H\) if and only if \(\mathcal S(G)=\mathcal S(H)\). First suppose these data agree. In a three-round Ehrenfeucht–Fraïssé game, Duplicator answers the first vertex arbitrarily. By transitivity, the possible second-vertex adjacency types and associated third-vertex profiles are the same at all first vertices. Duplicator responds to the second vertex by a vertex with the same adjacency type and profile. On the third round, she repeats a vertex if Spoiler repeats one, or otherwise realizes the same one of the four adjacency patterns, which the matching profile guarantees. This also works when Spoiler changes which graph is played.

Conversely, every exact profile \(P\) of a distinct pair of adjacency type \(e\) is described by a formula with two free variables and quantifier rank one: require \(e(a,b)=e\), require a third distinct vertex of each pattern in \(P\), and prohibit every pattern not in \(P\). Existentially quantifying the pair gives a rank-three sentence. A profile missing from the other graph therefore distinguishes the graphs. This proof explicitly handles pair absence and quantifier alternation, not merely existence of some three-vertex induced subgraph.

**2. Kneser pair calculation.** By symmetry, an ordered distinct pair \(a,b\) is characterized by \(t=|a\cap b|\), where \(0\le t\le k-1\). Such a pair exists if and only if \(k-t\le n-k\). It is an edge exactly when \(t=0\). If \(k\ge2\) and \(n\ge2k+1\), then for *every* distinct pair the three patterns \((0,0),(0,1),(1,0)\) occur. For example, to obtain a vertex adjacent to \(a\) but not to \(b\), choose a \(k\)-subset outside \(a\) containing an element of \(b\setminus a\) when the pair overlaps; for a disjoint pair, take \(k-1\) elements of \(b\) and one of the nonempty complement of \(a\cup b\). The symmetric pattern is analogous. To obtain \((0,0)\), take a set meeting both \(a\) and \(b\), choosing one common element when there is one, or one from each side in the disjoint case; enough unused elements exist to keep it distinct from both endpoints. These choices work even for \(k=2\) and \(n=2k+1\).

The remaining pattern \((1,1)\) means that the third \(k\)-set is disjoint from \(a\cup b\), and so occurs if and only if
\[
 n-|a\cup b|=n-2k+t\ge k,\quad\text{equivalently }\quad n\ge3k-t.
\]
Accordingly, for \(k\ge2,n\ge2k+1\), every edge pair has profile \(P_1\) exactly when \(n\ge3k\), otherwise \(P_0\). A nonedge pair with intersection size \(t\in\{1,\ldots,k-1\}\) has \(P_1\) exactly when \(n\ge3k-t\); otherwise it has \(P_0\). All such nonedge intersection sizes occur because \(n\ge2k+1\).

**3. The eight cases.** When \(k=n\) the graph has one vertex. When \(k=1\), it is the complete graph on \(n\) vertices and gives the two-vertex and at-least-three-vertex cases separately. If \(1<k<n<2k\), no two \(k\)-sets are disjoint, and \(\binom nk\ge3\). If \(n=2k,k\ge2\), each \(k\)-set has exactly its complement as neighbor: the graph is a perfect matching on \(\binom{2k}k\ge6\) vertices. Its edge pair profile is \(\{(0,0)\}\), while its nonedge pair profile is \(P_0\), since there are at least three matching edges.

For \(n\ge2k+1,k\ge2\), the calculation in step 2 yields exactly three alternatives before the triangle threshold: if \(2k+1\le n\le3k-2\), nonedge pairs attain *both* \(P_0\) and \(P_1\); if \(n=3k-1\), all nonedge pairs have \(P_1\) but edge pairs have \(P_0\); if \(n\ge3k\), all edge and nonedge pairs have \(P_1\). The mixed interval is nonempty exactly when \(k\ge3\). Thus these give the remaining three table rows.

The eight resulting signatures are pairwise distinct. Explicitly: the singleton has no pair; the two-vertex clique has an edge pair with an empty third-vertex profile; a larger clique has only edge pairs, with profile \(\{(1,1)\}\); a larger edgeless graph has only nonedge pairs, with profile \(\{(0,0)\}\); a matching has both types but no common neighbor for either; and the last three cases differ according to the presence of an edge-pair \((1,1)\) witness and whether every, some, or only a subset of nonedge pairs have such a witness. Step 1 turns these signatures into the exact logical classification.

**4. Sharp finite thresholds and the Rado comparison.** The Rado graph realizes all four adjacency patterns over every distinct pair and has both edges and nonedges. Its pair signatures agree with the last class. Conversely, for \(2k+1\le n<3k\), every disjoint pair lacks a common neighbor, a rank-three detectable failure. The smallest permitted \(k\) for this class is \(2\), and then \(n=6\); monotonicity of \(\binom nk\) in the admissible parameter region makes \(\mathrm{KG}(6,2)\) the smallest Kneser representative. The mixed class starts at \(k=3,n=7\) and hence first occurs on \(\binom73=35\) vertices. The other minimal representatives follow immediately from their rows.

## Verification
The accompanying standalone `checker.py` enumerates exact adjacency signatures for every allowed parameter pair with \(1\le n\le17\) and \(\binom nk\le6000\), totaling 138 cases. It compares the result with the closed profile formula, checks every pair-orbit profile for all eight minimal representatives, and verifies the sharp boundary categories for several values of \(k\). It returned `KNESER_RANK3_ALL_FINITE_CHECKS_OK cases= 138 classes= 8 largest_bruteforce_vertices= 5005`. Enumeration of representatives and bounded parameters does **not** constitute the all-parameter proof; the arbitrary-parameter set construction and EF lemma above supply that proof. To reproduce, run `python checker.py` using Python's standard library.

## Relationship to prior work
Benediktsson, Macpherson and Adler (arXiv:2610.40054, first submitted October 29, 2026) study the complete limit theory of *Johnson graphs* and suggest examination of further set-defined graph families. Their adjacency is the exchange of one element; Kneser adjacency instead means disjointness. Their limit theorem and axiomatization do not state or imply the eight-case Kneser rank-three classification.

Voronov, Dergachev, Zhukovskii and Neopryatnaya (2021) do employ Kneser graphs and Ehrenfeucht games as witnesses in a different descriptive-complexity problem: minimum first-order variable counts for subgraph containment. Their Kneser comparisons imply some bounded-variable indistinguishability instances in the mixed regime; those special instances are not asserted new. Their main theorems do not classify the complete rank-three theories of every Kneser parameter pair or identify all sharp boundaries here.

The existing literature on two-existentially-closed graphs includes many small models, and a 2025 paper classifies critical Cayley and vertex-transitive examples in specified order ranges. The last class here is exactly the two-point extension property within the Kneser family. The independent claim is the **global eight-class logical classification with exact Kneser thresholds**, not the definition of two-existential closure or the general existence of such graphs.

## Limitations
Only finite \(\mathrm{KG}(n,k)\) with \(1\le k\le n\) are covered. The Rado comparison is restricted to rank three; these finite graphs do not satisfy the full first-order theory of the Rado graph. The smallest-vertex assertions hold only inside the Kneser family. The general existence and enumeration of two-existentially-closed graphs are known topics and are not claimed as discoveries. Earlier literature on Kneser graphs in logic and generic graph extension axioms may contain equivalent partial results; historical priority is not independently certified. No independent mathematical audit has been conducted.

## References
1. B. G. Benediktsson, D. Macpherson, I. Adler, *Model Theory of Johnson Graphs*, arXiv:2610.40054 (first submitted 2026-10-29), https://arxiv.org/abs/2610.40054.
2. V. A. Voronov, E. A. Dergachev, M. E. Zhukovskii, A. M. Neopryatnaya, *First-Order Complexity of Subgraph Isomorphism via Kneser Graphs*, Mat. Zametki 109 (2021), 36–46, https://doi.org/10.4213/mzm12784.
3. *Existentially Closed Critical Cayley Graphs*, Ars Combinatoria 164 (2025), https://combinatorialpress.com/ars-articles/volume-164/existentially-closed-critical-cayley-graphs/.
4. A. Ehrenfeucht, *An application of games to the completeness problem for formalized theories*, Fundamenta Mathematicae 49 (1961), 129–141.
