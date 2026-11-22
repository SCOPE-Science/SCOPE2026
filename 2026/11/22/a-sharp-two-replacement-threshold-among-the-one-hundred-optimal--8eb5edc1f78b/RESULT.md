# A sharp two-replacement threshold among the one hundred optimal semitotal dominating sets of the Desargues graph

## Finding

**Theorem.** Let \(D\) be the Desargues graph, equivalently the generalized Petersen graph \(\operatorname{GP}(10,3)\) or the bipartite Kneser graph \(H(5,2)\). Its semitotal domination number is \(\gamma_{t2}(D)=6\), and it has **exactly 100** minimum semitotal dominating sets. All 100 contain three vertices from each bipartition shore. They consist of three orbits under the full graph automorphism group \(S_5\times C_2\), of sizes \(10,30,60\). Exactly 70 of these sets induce no edges, while the remaining 30 each induce one edge.

Let \(\mathcal R_k\) be the graph whose vertices are the 100 optimal six-sets and whose edges join distinct sets \(A,B\) precisely if \(|A\setminus B|=|B\setminus A|\le k\). Thus a move simultaneously replaces at most \(k\) selected vertices, without changing the cardinality or requiring nonoptimal intermediate configurations. **Every optimum is isolated in \(\mathcal R_1\); the graph \(\mathcal R_2\) is connected and has exactly 570 edges, radius four and diameter four.** Consequently its sharp connectivity threshold is \(k_{\mathrm{conn}}=2\).

The degree and all-sources distance-shell distributions of \(\mathcal R_2\), one shell for each orbit, are as follows. The shell at index zero is the initial configuration.

| Orbit size | Induced edges per six-set | Two-replacement degree | Distance shells (0 through 4) |
|---:|---:|---:|---|
| 10 | 0 | 12 | \((1,12,42,42,3)\) |
| 30 | 1 | 8 | \((1,8,46,44,1)\) |
| 60 | 0 | 13 | \((1,13,44,40,2)\) |

The parameter, its general degree-based bound, and the symmetry of the Desargues graph are existing mathematical background; **the claim here is the complete optimum census and its exact optimal-exchange geometry**, not the definition or general bound.

## Assumptions and scope

All graphs are finite, simple and undirected, and shortest-path distances are measured in the original graph. A **semitotal dominating set** \(S\subseteq V(D)\) is an ordinary dominating set (every vertex lies in some closed neighborhood \(N[s]\), \(s\in S\)), such that for every \(s\in S\) there is a distinct \(t\in S\) with \(d_D(s,t)\le2\). The latter condition is *not* total domination: distinct selected vertices may be at distance exactly two.

For an explicit complete combinatorial model, set \(U=\{0,1,2,3,4\}\). There are ten left vertices \(L_e\) indexed by two-element subsets \(e\subset U\), and ten right vertices \(R_f\) indexed by three-element subsets \(f\subset U\). Join \(L_e\) to \(R_f\) if and only if \(e\subset f\). Label each shore lexicographically. This construction has 20 vertices and degree three, and is isomorphic to the standard \(\operatorname{GP}(10,3)\) model, whose 20 vertices are \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\) and \(v_i v_{i+3}\). The independent verifier supplies and checks a complete vertex-level isomorphism between the models.

A one-replacement edge joins two optimum six-sets with five common vertices. A two-replacement edge joins two optimum six-sets with either five or four common vertices; the theorem proves the former possibility does not arise. Exchanges are unordered, with all 100 sets treated as distinct labeled configurations. The graph-theoretic diameter refers to \(\mathcal R_2\), not the disconnected \(\mathcal R_1\).

## Proof

**1. Lower bound.** The general semitotal-degree inequality of Goddard, Henning and McPillan [1, Lemma 3] gives \(\gamma_{t2}(G)\ge2|V(G)|/(2\Delta(G)+1)\). Here \(|V(D)|=20\) and \(\Delta(D)=3\), so \(\gamma_{t2}(D)\ge\lceil40/7\rceil=6\). Independently of that published inequality, both standalone verifiers check that none of the \(\binom{20}{5}=15{,}504\) five-subsets dominates \(D\); by monotonicity, there is then no smaller dominating set either. The explicit six-sets in Step 2 are semitotal dominating sets, hence equality holds. The numerical minimum itself is not presented as an independent structural novelty.

**2. Exact finite membership predicate.** For each of the \(\binom{20}{6}=38{,}760\) candidate six-subsets \(S\), evaluate the following necessary and sufficient condition:
\[
\bigcup_{s\in S}N[s]=V(D)
\quad\text{and}\quad
\forall s\in S\ \exists t\in S\setminus\{s\}:d_D(s,t)\le2.
\]
The two independent complete verifiers apply this predicate, respectively using integer closed-neighborhood and distance-two masks on the Petersen representation and explicit neighborhood sets and breadth-first distances on the subset-incidence representation. Both find exactly 130 ordinary dominating six-sets, of which exactly 100 satisfy the extra semitotal witness condition. Every one of those 100 has three vertices on each shore. The six-set census is exhaustive, rather than a sample or an inference from graph symmetry.

**3. Full symmetry-orbit classification.** Every permutation of the five underlying labels induces an automorphism of the subset-incidence graph. Complementing each two-subset or three-subset in \(U\) exchanges the shores and preserves incidence. Together these form the 240-element group \(S_5\times C_2\), known to be the full automorphism group of the Desargues graph [3]. For each of the 100 sets, applying these 240 maps and grouping identical images yields exactly three disjoint orbits, of sizes \(10,30,60\), which cover all 100 enumerated solutions. Concrete representatives, writing a six-set as selected two-subsets followed by selected three-subsets, are:

* Size 10: \(\{23,24,34\}\cup\{012,013,014\}\).
* Size 30: \(\{01,24,34\}\cup\{014,023,123\}\).
* Size 60: \(\{13,24,34\}\cup\{012,014,023\}\).

Here digits are symbols of \(U\), not decimal numbers. By inspecting incidence among the six chosen objects, the 10- and 60-orbit representatives induce zero edges, whereas the 30-orbit representative induces exactly one. These properties are invariant under the group, giving the precise 70/30 partition.

**4. The sharp exchange threshold.** The exhaustive membership list gives a precise finite certificate for comparing all \(\binom{100}{2}=4{,}950\) distinct optimum pairs. Compute \(r(A,B)=6-|A\cap B|\). No pair has \(r(A,B)=1\), so \(\mathcal R_1\) has no edges. Exactly 570 pairs have \(r(A,B)=2\), forming the graph \(\mathcal R_2\). Its degree multiset is 10 copies of 12, 30 copies of eight and 60 copies of 13. An all-sources breadth-first search from every one of its 100 vertices visits all 100 and yields precisely the three shells in the Finding table. Every row sums to 100 and has a positive entry at distance four; thus \(\mathcal R_2\) is connected, every eccentricity is four, and its radius and diameter are both four. This proves the sharp threshold, without assuming connectivity from regularity or from a partial search.

The number 570 is consistent with the independently computed degree sum \((10\cdot12+30\cdot8+60\cdot13)/2=570\). Both implementations construct the edges independently from the six-sets and compare all state pairs, so that identity is a cross-check, not the sole edge-count proof.

## Verification

Run the following commands in the directory containing the two complete embedded source files:

```sh
c++ -O2 -std=c++17 -Wall -Wextra verify_gp.cpp -o verify_gp
./verify_gp
python3 verify_incidence.py
```

Each source prints `VERIFY_OK` after all assertions pass. `verify_gp.cpp` constructs the generalized Petersen model and enumerates all \(2^{20}\) vertex masks, independently excluding all smaller ordinary dominating sets before retaining and checking every six-set using bitwise neighborhood unions. It constructs all 4,950 potential optimum pairs and performs all-sources breadth-first searches. `verify_incidence.py` independently constructs the two-/three-subset incidence model, checks a fixed vertex-level isomorphism, excludes every dominating five-subset and enumerates all 38,760 six-subsets with ordinary set membership and explicit shortest-path computations, and independently checks pairwise exchanges, symmetry orbits, degree distributions and distance shells. Both were run successfully from the supplied sources, and the saved output is recorded in `VERIFICATION.md`.

The computation is a complete finite exhaustive proof for the specific 20-vertex graph, not numerical evidence for an unproved infinite family. No hardware-dependent floating-point arithmetic or third-party libraries are required. The broad prior bound from Step 1 is a mathematically published theorem, not a deduction from the verifier's failed searches.

## Relationship to prior work

Goddard, Henning and McPillan [1] introduced semitotal domination and proved the lower bound used in the proof. Their full published manuscript, including its degree bounds and structural sections, does not present the 100-state Desargues optimum classification or its exchanges. Henning and Marcon [2] characterized inclusion-minimal semitotal dominating sets and proved bounds involving maximum matchings; the available abstract gives no graph-specific enumeration. Its complete text was not available for a definitive comparison, and an earlier consequence hidden in it remains a residual priority risk.

A published 18-vertex **Pappus** graph calculation [4] determines 297 minimum semitotal sets and two one-token exchange graphs, which is a different incidence graph and cannot determine the 100 optimum configurations or sharp two-token exchanges of the Desargues graph. An explicit published **Desargues** graph classification [3] instead counts 1,475 minimum *locating*-dominating eight-sets; its requirement to distinguish signatures outside the set is not the semitotal distance-two requirement. It is used here only as a source for the standard graph model and symmetry group. Neither theorem implies the stated six-set census or two-replacement geometry. Research on total domination or zero forcing of other graphs likewise imposes different predicates and cannot be substituted for this result.

The literature/database comparisons do not establish universal first discovery. They determine the distinction from the specifically inspected prior results and identify plausible remaining priority risks.

## Limitations

This is a complete, finite and computer-assisted classification of only the 20-vertex Desargues graph. It does not give a formula for larger generalized Petersen graphs, arbitrary incidence graphs or additional move rules; no claims about intermediate nonoptimal states are made. Independent external scholarly verification has not occurred. Equivalent unpublished calculations, unindexed tables, and the full uninspected text of [2] could in principle contain part or all of the statement, so chronological originality is not independently certified. The standalone enumerators prove the cardinality and state-graph metric claims only under the exact predicates and finite domain specified here.

## References

1. W. Goddard, M. A. Henning and C. A. McPillan, *Semitotal Domination in Graphs*, Utilitas Mathematica **94** (2014), 67–81. Author-hosted full text: https://people.computing.clemson.edu/~goddard/papers/SemiTDomUtilitas.pdf .
2. M. A. Henning and A. J. Marcon, *On matching and semitotal domination in graphs*, Discrete Mathematics **324** (2014), 13–18. DOI: https://doi.org/10.1016/j.disc.2014.01.021 . Journal bibliography and accessible abstract: https://pure.uj.ac.za/en/publications/on-matching-and-semitotal-domination-in-graphs/ .
3. *All 1,475 minimum locating-dominating sets of the Desargues graph*, published mathematical record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-all-1-475-minimum-locating-dominating-sets-of-the-desargues-grap--d4faf2202a7f . Full `RESULT.md` inspected.
4. *Nine frozen total codes and a mobile semitotal-domination sector of the Pappus graph*, published mathematical record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-nine-frozen-total-codes-and-a-mobile-semitotal-domination-sector--229c8647b6e8 . Full `RESULT.md` inspected.
