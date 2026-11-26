# Five-slide extremals and a radius-four/diameter-five split for Kneser power-domination triples

## Finding

**Theorem.** Fix an integer \(n\ge8\), and let \(G_n=\operatorname{KG}(n,2)\), with vertices the unordered pairs of \([n]\), adjacent if and only if their pairs are disjoint. Let \(R_n\) have as vertices the *minimum power-dominating sets* of \(G_n\), with an edge for exchanging one selected pair for one unselected pair that is adjacent in \(G_n\), keeping a minimum power-dominating set. Then \(R_n\) is connected, with
\[
\operatorname{rad}(R_n)=4,\qquad\operatorname{diam}(R_n)=5.
\]
For two configurations \(S,T\), form the bipartite graph \(B(S,T)\) with left class \(S\), right class \(T\), and edge \(e_Lf_R\) when \(e\cap f=\varnothing\) as subsets of \([n]\). Write \(\nu(S,T)\) for its maximum matching size. Then the **sharp distance-five criterion** is
\[
d_{R_n}(S,T)=5\quad\Longleftrightarrow\quad S\cap T=\varnothing\ \text{and}\ \nu(S,T)\le1.
\]
Every minimum configuration consists of three distinct edges of the complete graph on \([n]\) *without a common endpoint*. The four types, their counts, degrees in \(R_n\) and eccentricities, are:

| Ground-edge type | Number | Slide degree | Eccentricity |
| --- | --- | --- | --- |
| Triangle \(K_3\) | \(\binom n3\) | \(3\binom{n-3}{2}\) | 4 |
| Three-edge path \(P_4\) | \(12\binom n4\) | \(3\binom{n-3}{2}+n-3\) | 5 |
| Two-edge path plus one disjoint edge \(P_3\sqcup K_2\) | \(30\binom n5\) | \(3\binom{n-3}{2}+2(n-4)\) | 5 |
| Three disjoint edges \(3K_2\) | \(15\binom n6\) | \(3\binom{n-3}{2}+3(n-5)\) | 5 |

Consequently
\[
|V(R_n)|=\binom{\binom n2}{3}-n\binom{n-1}{3},
\]
and the edge count is one-half the sum of (orbit size times the corresponding degree) in the table. The underlying minimum power-domination triple classification is known; the claims here concern its **adjacency-restricted relocation graph**, distances and precise extremals.

## Assumptions and scope

Graphs are simple, finite and undirected, with the *disjointness* Kneser adjacency, not the complement/triangular adjacency. Given a selected set \(S\), power domination first observes \(N_{G_n}[S]\) and then repeatedly makes the standard zero-forcing observation: an observed vertex with exactly one unobserved neighbor observes that neighbor. Minimum means minimum cardinality, not merely inclusion-minimal. A token slide replaces one selected vertex by an unselected **adjacent** vertex of the original \(G_n\), preserving feasibility and cardinality. The bipartite graph \(B(S,T)\) uses separate left and right copies, even when the two configurations intersect. No unproved structural claim for higher-subset Kneser graphs is made.

## Proof

**1. Configuration classification (known premise [1]).** The unobserved pairs after the closed-neighborhood phase are exactly the unselected pairs meeting every selected pair. If all selected pairs share a ground endpoint \(a\), then at least \(n-4\ge4\) unselected spokes at \(a\) remain unobserved (for one, two or three selected pairs). Any observed vertex either contains \(a\), and sees no such spoke, or avoids \(a\), and is adjacent in the Kneser graph to all but at most two such spokes. The only observed vertices containing \(a\) in this situation are selected pairs, which have no unobserved neighbors. Hence zero forcing cannot start. For two disjoint selected pairs \(ab,cd\), the four unobserved pairs are the cross pairs between \(\{a,b\}\) and \(\{c,d\}\). Any observed vertex is disjoint from one of the two selected pairs and so is adjacent to zero or at least two cross pairs. The empty selection observes nothing. Thus fewer than three pairs never suffice.

A nonstar triple is a triangle, a three-edge path, a two-edge path plus an isolated edge, or a three-edge matching. A triangle and a three-edge matching leave no unobserved pairs. For the path \(ab,bc,cd\), the two unobserved pairs are \(ac,bd\); for \(ab,bc,de\), they are \(bd,be\). For a fresh label \(x\) outside the respective support, the observed pair \(ax\) in the first case and \(dx\) in the second is adjacent to exactly one unobserved pair. Once that pair is forced, the remaining unobserved vertex has an observed Kneser neighbor and is forced. This proves the claimed domain of minimum configurations without requiring a separate classification of larger feasible sets.

**2. Orbit sizes and slide degrees.** Ground-set permutations preserve both power domination and the allowed move. The four listed types are exactly the four orbits. A triangle is determined by three labels; a three-edge path has twelve labelled placements on a four-element support; a two-edge path and a disjoint edge have thirty on a five-element support; and three disjoint edges have fifteen perfect matchings on a six-element support. These give the four counts in the theorem.

For any selected pair \(e\), there are \(\binom{n-2}{2}\) pairs disjoint from it, before excluding occupied endpoints and moves into a prohibited three-star. Across the three choices of \(e\), the numbers of invalid moves in the four orbit types are respectively \(3(n-3)\), \(2+2(n-4)\), \(4+(n-5)\), and \(6\). These follow by examining the two edges retained after deleting each selected edge: a new pair makes a three-star precisely when both retained edges meet in a unique endpoint, and the new pair contains that endpoint; occupied pairs are separately excluded. Subtracting from \(3\binom{n-2}{2}\) yields the displayed degrees. Summing the four orbit counts and degrees proves the vertex and edge enumerators.

**3. The universal finite-support reduction.** Any two three-pair configurations use at most twelve ground-set labels in their union. If \(n\ge12\), relabel these labels into \([12]\), retaining their equality/disjointness relationships. Every allowed move between triples whose ground pairs are supported inside \([12]\) remains an allowed move in \(G_n\), and every intermediate nonstar triple remains power dominating for \(n\ge8\). Thus any upper bound on distances *between all pairs* of feasible states in \(R_{12}\) also applies for every higher \(n\). Likewise, a path of length at most four in \(R_{12}\), established for the relabelled endpoints when they have the nondeficient matching property, lifts to a path in \(R_n\). For \(8\le n\le11\), no reduction is needed. The finite checks below therefore prove universal upper bounds rather than merely suggesting them experimentally.

**4. Complete finite certificate for the upper bound and the extremal converse.** Both bundled independent checkers verify, for each of the five values \(8\le n\le12\), all triples of \(\binom n2\) ground pairs and discard exactly those having a common ground endpoint. Ground-set permutations act transitively on each of the four explicit types, so it suffices to choose one source from each type. The first checker explicitly constructs the entire slide adjacency graph and runs breadth-first search from all four representatives. For every state reached it tests whether the distance is five exactly when the source and target are disjoint as *configurations* and the bipartite source-target disjointness graph has matching number at most one. It verifies reachability of **every** feasible target, eccentricity four for the triangle representative, and eccentricity five for each of the other three representatives. The second independently encodes states as bitsets, generates slide-neighbor layers without the first program, and checks that the entire depth-five layer equals exactly the targets having the matching deficit. It additionally performs the original power-domination process on every candidate set of size at most three for \(8\le n\le10\). Their source code, exact output and dependency-free commands are in the package. By Step 3 these checks give the all-order upper bounds: every distance is at most five, and at most four if the configurations intersect, if the direct matching has size at least two, or if one endpoint is a triangle.

**5. A noncomputational distance-five obstruction.** Suppose \(S\cap T=\varnothing\) and a sequence moves three indistinguishable tokens from \(S\) onto \(T\) in at most four slides. Because no token can start at its final vertex, each token must move at least once. Consequently at least two tokens move **exactly once**: up to permutation the only possible positive move-count profiles are \((1,1,1)\) and \((1,1,2)\). These two moves directly connect distinct initial occupied vertices to distinct target vertices along edges of the original Kneser graph. They form a two-edge matching in \(B(S,T)\). Therefore if \(\nu(S,T)\le1\), at least five slides are necessary. Combining with Step 4 proves the biconditional.

**6. Sharp eccentricities and radius.** Example configurations (writing \(01\) for the unordered pair \(\{0,1\}\)) demonstrate the lower bounds and remain valid for every \(n\ge8\):

- A triangle source \(\{01,02,12\}\) and target \(\{03,04,15\}\) have disjoint configurations and no three-edge matching of direct slides, forcing distance at least four.
- The three-edge path \(\{01,02,13\}\) and two-edge-path-plus-edge \(\{01,02,34\}\) each have the target \(\{03,04,12\}\) with \(\nu=1\) and no common selected pair. For the three-edge matching \(\{01,23,45\}\) use the target \(\{02,03,12\}\): all target pairs meet both \(01\) and \(23\) and avoid \(45\), so again \(\nu=1\) and there is no common selected pair. In all three cases the distance is at least five by Step 5.

The certificate supplies matching upper bounds for all types in all orders. Thus triangle eccentricity is exactly four, the others exactly five, the radius is four, and the diameter is five.

## Verification

Run `python3 verify_slide_orbits.py` and `python3 verify_independent.py` from the extracted embedded files. Both use Python 3's standard library only. The expected output is exactly stored in `orbit_output.json` and `independent_output.json` (JSON key order immaterial). The programs check every legal move, every vertex and target distance from one source per symmetry orbit for each \(n=8,9,10,11,12\); the second verifies original propagation for all size-at-most-three sets through \(n=10\). There are respectively \(2996,6636,13350,24915,43780\) feasible states, and the numbers of undirected slide edges are \(55650,180306,498330,1221660,2726460\).

The reduction in Step 3 is essential: the computers never enumerate arbitrarily large graphs, but their **complete** order-twelve enumeration, together with symmetry and the twelve-ground-label support theorem, certifies every \(n\ge8\). The finite checks would not imply an infinite conclusion without the proved reduction. The two scripts independently derive the transitions and matching criterion; neither uses external packages or network access.

## Relationship to prior work

[1] already classifies all feasible power-dominating configurations of \(\operatorname{KG}(n,2)\). In particular its nonstar-triple condition and the resulting orbit counts are **not newly discovered** here; the new question is what happens if each sensor must move to an adjacent Kneser vertex while minimum power domination remains intact. The public minimum-isolating-set reconfiguration theorem [2] instead excludes three-edge *paths* (rather than stars) and permits *unrestricted* exchange; its diameter-three and twelve-endpoint certificate do not imply the result here, though the finite-support method is analogous. Bjorkman et al. [3] give general power-domination TAR and token-jumping theory and define slides but do not treat this exact family or its slide distances. Fischer [4] proves token-graph connectivity and diameter results for the **unrestricted full token graph**, containing also the three-star states excluded from this induced optimum graph. The results cannot be substituted for the constrained geodesic or the source-target matching extremality criterion here. Bartier et al. [5] treat sliding **independent sets** in girth-restricted graphs; our feasible triples are neither required to be independent nor in their high-girth setting. Cornet and Torres [6] establish static \(k\)-tuple domination results for Kneser graphs, not this power-domination relocation geometry. Full texts or precisely indicated available portions were inspected as detailed in the accompanying review.

## Limitations

This is an all-order, computer-assisted **finite-certificate proof**: the universal upper bounds depend on independently replayable complete breadth-first searches through order twelve and on the explicit twelve-label reduction. The lower obstruction, orbit types and degrees are symbolic. No simple all-order closed-form pairwise distance expression for distances zero through four is asserted; the exact theorem characterizes the extreme distance five, radius, diameter and orbit eccentricities. There remains the risk that a previously unindexed or differently named equivalent token-graph result exists. Independent external mathematical auditing has not been performed.

## References

1. *Power-domination polynomial and minimal-set dichotomy of two-subset Kneser graphs*, [research record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-power-domination-polynomial-and-minimal-set-dichotomy-of-two-sub--6e981f3b14e6). The state characterization is explicitly prior work.
2. *Minimum isolating sets and three-step reconfiguration in \(\operatorname{KG}(n,2)\)*, [research record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-minimum-isolating-sets-and-three-step-reconfiguration-in-operato--f2da2f07c4da). Different constraint and move rule.
3. B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1 (first posted 2022-01-05), https://arxiv.org/html/2201.01798v1 .
4. J. W. Fischer, *On the connectivity and diameter of Token graphs from a vertex induced sub-graph perspective*, arXiv:2212.14634v1 (2022-12-30), https://arxiv.org/abs/2212.14634 .
5. V. Bartier et al., *Token sliding on graphs of girth five*, arXiv:2205.01009v1 (2022-05-02), https://arxiv.org/abs/2205.01009 .
6. F. Cornet and L. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603 (2023-08-29), https://arxiv.org/abs/2308.15603 .
