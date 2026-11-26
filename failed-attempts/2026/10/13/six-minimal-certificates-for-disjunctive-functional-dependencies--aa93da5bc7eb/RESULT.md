# Six minimal certificates for disjunctive functional dependencies

## Finding

Consider the quantifier-free dependence-logic formula
\[
\varphi=\operatorname{dep}(x,y)\vee\operatorname{dep}(x,z).
\]
Its violations admit **exactly six** minimal, color-preserving incidence patterns. These are a three-edge matching; a four-cycle; a path with four edges and center on the right, and its transpose; two disjoint two-edge stars with centers on the left, and their transpose. Here left vertices represent values of \(y\), right vertices represent values of \(z\); transposing interchanges colors. All six patterns genuinely occur and are minimal under deletion of assignments. Every violation contains one of these certificates on three or four assignments; the cutoff four is sharp.

For a complete \(p\)-by-\(q\) incidence fiber, the **exact numbers** of distinct minimal violating three-assignment and four-assignment subteams are
\[
A_3(p,q)=6\binom{p}{3}\binom{q}{3},
\]
\[
A_4(p,q)=\binom{p}{2}\binom{q}{2}
+6\left(\binom{p}{2}\binom{q}{3}+\binom{p}{3}\binom{q}{2}
+\binom{p}{2}\binom{q}{4}+\binom{p}{4}\binom{q}{2}\right).
\]
Binomial coefficients are zero when the lower index exceeds the upper index. These counts concern subteams, not graph embeddings counted with automorphism multiplicity.

## Assumptions and scope

A **team** is a finite set of assignments into an arbitrary set, with \(x,y,z\) distinct among the team variables. The dependence atom \(\operatorname{dep}(x,y)\) holds precisely when assignments agreeing on \(x\) agree on \(y\). Lax split disjunction means \(T\models\alpha\vee\beta\) if there exist \(T_1,T_2\subseteq T\) with \(T=T_1\cup T_2\) satisfying the corresponding atoms. Since dependence atoms are downward closed, one may take a disjoint split. Extra assignment variables do not affect satisfaction.

Fix any value \(a\) taken by \(x\). Let \(G_a=(Y_a,Z_a,E_a)\) be the simple bipartite graph with left values \(Y_a=\{s(y):s(x)=a\}\), right values \(Z_a=\{s(z):s(x)=a\}\) and edges \(E_a=\{(s(y),s(z)):s(x)=a\}\). Duplicate projections are coalesced, although multiple full assignments may project to the same edge. A colored graph embedding preserves left/right vertex classes and edge incidence, but may ignore additional host edges. A subteam is **minimal bad** if it violates \(\varphi\) and every proper subteam satisfies it.

The six forbidden edge sets are shown below using locally renamed left/right values; all labels within a displayed edge set are literal vertex labels, not assignment values fixed in advance.

| Pattern | Colored edges |
| --- | --- |
| Three-edge matching | \(\{(0,0),(1,1),(2,2)\}\) |
| Four-cycle | \(\{(0,0),(0,1),(1,0),(1,1)\}\) |
| Four-edge path, two left vertices | \(\{(0,0),(0,1),(1,0),(1,2)\}\) |
| Four-edge path, three left vertices | \(\{(0,0),(1,0),(0,1),(2,1)\}\) |
| Two disjoint left-centered two-edge stars | \(\{(0,0),(0,1),(1,2),(1,3)\}\) |
| Two disjoint right-centered two-edge stars | \(\{(0,0),(1,0),(2,1),(3,1)\}\) |

## Proof

**Step 1 — mixed vertex covers.** On a fixed \(x\)-fiber, a dependence-respecting split consists of a subteam with a single \(y\)-value and a subteam with a single \(z\)-value. Thus its graph has all edges incident with one left vertex or one right vertex. Conversely such two vertices yield a split: put every row with the selected \(y\)-value into the first part and every remaining row into the second, which then has the selected \(z\)-value. A nonempty fiber satisfying either atom alone is also covered in this way, by choosing any unused opposite vertex. The different \(x\)-fibers can be split independently. It follows that \(T\models\varphi\) exactly when every \(G_a\) has a vertex cover comprising one left and one right vertex.

**Step 2 — a four-edge witness.** Suppose a nonempty bipartite graph has no such mixed vertex cover. It has two disjoint edges \((a,b)\) and \((c,d)\): otherwise all edges meet a fixed edge, so the fixed edge's two endpoints would cover them. Any mixed two-vertex cover of those two disjoint edges is either \(\{a,d\}\) or \(\{c,b\}\), where the first coordinate denotes a left vertex. Because neither candidate covers the entire graph, choose one edge uncovered by the first pair and one uncovered by the second. The chosen two disjoint edges and these at most two additional edges already lack a mixed cover. Consequently every minimal bad projected edge set has three or four edges. Two edges are always covered by one endpoint of the first and the opposite-colored endpoint of the second.

**Step 3 — the three-edge case.** Fix two disjoint edges as above. To defeat both cross-pair covers with only one remaining edge, that edge must avoid both left endpoints and both right endpoints. Hence it is disjoint from both selected edges. The unique colored type is the three-edge matching.

**Step 4 — the four-edge case.** A minimal bad graph with four edges contains no three-edge matching, since that would be a proper bad subgraph. It has matching number exactly two: it has two disjoint edges, and three independent ones are excluded. By König's finite bipartite matching–vertex-cover theorem, the graph has a vertex cover of two vertices. A mixed cover does not exist, so this cover must have both vertices on one color class. Suppose they are left vertices. Each must have degree at least two, for if one had degree at most one the other left vertex together with the right endpoint of that possible edge would give a mixed cover. As the graph has exactly four edges, both degrees are exactly two. Their two right-neighborhoods intersect in exactly zero, one, or two vertices. These yield, respectively, two disjoint left-centered two-edge stars, a four-edge path with two left and three right vertices, or a four-cycle. A right-side two-vertex cover yields the color-transposed possibilities. The four-cycle is self-transpose, giving five four-edge colored types. Every listed pattern fails mixed-cover existence, while deleting any edge makes the two-star degrees \((2,1)\) in one of the two cover classes (or leaves a smaller matching); a mixed cover then exists. Thus all six are minimal and pairwise different under color-preserving isomorphisms.

**Step 5 — transfer to teams.** Any offending graph pattern selects three or four distinct projected edges in one \(x\)-fiber, hence distinct assignments realizing those edges. The selected rows form a bad subteam. Conversely a minimal bad subteam must lie in one fiber and cannot contain two rows with identical \((x,y,z)\)-projections: removing a duplicate would not change the set of projected edges or truth. Thus the graph list classifies minimal bad subteams up to projection. The six cases are realizable by taking one assignment per displayed edge with a constant \(x\)-value.

**Step 6 — complete-fiber enumeration.** A three-edge matching is specified by three left vertices, three right vertices, and one of six bijections. A four-cycle is specified by two vertices of each color. Each colored four-edge path has two vertices on one side and three on the other: choose the shared endpoint of degree two on the three-vertex side in three ways, then match the remaining two endpoints to the two vertices on the other side in two ways, for multiplicity six. Each pair of disjoint same-side two-edge stars uses two vertices on the center side and four distinct vertices on the other, of which a chosen pair attaches to the first center in six ways. Adding these five four-edge contributions proves both formulas.

## Verification

The accompanying `verify_six_obstructions.py` uses only Python's standard library. Run `python3 verify_six_obstructions.py`. It independently generates all embeddings of the six displayed patterns into a labeled bipartite \(4\)-by-\(4\) vertex set; checks mixed cover existence against forbidden-pattern containment for **all \(65{,}536\)** possible edge sets; checks that every inclusion-minimal failing graph belongs to the list; and verifies the two enumerative formulas on every complete rectangle of side sizes one through four. The output is `VERIFY_OK`. The labeled minimal-obstruction counts at four by four are 96 three-edge and 396 four-edge cases. This finite computation tests the argument; the proof above establishes the theorem without assuming exhaustive search at larger sizes.

## Relationship to prior work

Fröhlich, Kolaitis and Meier proved in their 2025 preprint (and 2026 CSL article), Theorem 22, that this very disjunction has coherence level four and supplied one minimal four-row counterexample. That theorem **already implies** the four-row witness bound; neither that bound nor first-order definability is claimed as new. Their result does not state the six color-preserving minimal forbidden graph types or the complete-fiber counting polynomials. The matching/cover analysis above refines the witness theorem into a complete minimal-obstruction catalogue. Barlag and collaborators' 2026 coherence study gives broader background on first-order rewritability and coherence. We do not claim its general characterizations or the published complexity trichotomy as new results.

## Limitations

Only this fixed two-atom disjunction (with common determinant) is classified; no implication problem for arbitrary dependence-logic formulas is solved. The result is a complete classification of **projected** minimal witnesses, not of the number of repairs, labeled full teams with extra variables, or the arity-generalized implication problem. The use of König's theorem is for a four-edge finite bipartite graph. Independent validation of novelty has not been performed. It remains possible that an equivalent forbidden-graph catalogue appears in work using database or bipartite-cover vocabulary, including material not accessible in the full 2026 coherence preprint.

## References

1. N. Fröhlich, P. G. Kolaitis, A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146 (first public 22 August 2025); CSL 2026, DOI:10.4230/LIPIcs.CSL.2026.10. Theorem 22 and Section 4.
2. T. Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (first public 29 May 2026), abstract and article record.
3. D. König, finite bipartite matching–vertex-cover theorem (standard graph-theoretic result).
