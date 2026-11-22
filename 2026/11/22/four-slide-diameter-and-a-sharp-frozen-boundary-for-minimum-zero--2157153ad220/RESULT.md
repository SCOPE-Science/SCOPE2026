# Four-slide diameter and a sharp frozen boundary for minimum zero forcing on complements of cycles

## Finding

Let \(G_n=\overline{C_n}\), where \(C_n\) is the labelled cycle on \(n\ge6\) vertices. Let \(\mathcal S_n\) have one vertex for every minimum *ordinary* zero-forcing set \(B\subseteq V(G_n)\), with two such sets joined precisely when \(B'=B-\{u\}+\{v\}\) for an edge \(uv\) of \(G_n\). Thus one blue sensor slides along one *original graph edge* while every intermediate sensor set remains minimum zero forcing. For every \(n\ge7\), the graph \(\mathcal S_n\) is connected and has diameter exactly four. For \(n\ge9\), its complete order and edge enumeration is

\[
|V(\mathcal S_n)|=n(n-4),\qquad
|E(\mathcal S_n)|=\frac{n(n-6)(n+3)}2,\qquad
\operatorname{diam}(\mathcal S_n)=4.
\]

At the two smaller connected orders, \((|V|,|E|,\operatorname{diam})=(21,42,4)\) for \(n=7\) and \((32,92,4)\) for \(n=8\). There is a sharp disconnected boundary at \(n=6\): \(\mathcal S_6\) consists of a connected 12-vertex component and two isolated vertices, with 14 total vertices and 18 edges. For all \(n\ge7\), arbitrary replacements are unnecessary for connectivity; even under the local slide restriction, no two optimal solutions are more than four legal moves apart.

The scalar zero-forcing number \(Z(G_n)=n-3\), the count of its minimum zero-forcing sets, and the prior unrestricted-exchange geometry are background results and are **not** claimed as new. The novelty asserted here is the local-slide transition, edge enumeration, and constant sharp diameter.

## Assumptions and scope

All graphs are finite, simple and undirected. The underlying labelled cycle has vertices \(0,1,\ldots,n-1\), with arithmetic modulo \(n\). Two distinct vertices are adjacent in \(G_n\) exactly when they are not consecutive in \(C_n\). In ordinary zero forcing, a blue vertex with exactly one white neighbor forces that neighbor blue, until no further force exists. Sets are minimum by cardinality, not merely inclusion-minimal. The reconfiguration step slides one blue vertex to an unoccupied neighbor in \(G_n\) without ever leaving the class of minimum sets. This definition differs from token jumping, where the removed and inserted vertices need not be adjacent.

It is useful to complement the blue set \(B\) to its three white vertices \(W=V(G_n)\setminus B\). A slide \(B\to B'\) then exchanges exactly one member of \(W\) with one of \(W'\), also along an edge of \(G_n\). For \(n\ge7\), the valid white triples are precisely those that contain a pair at cyclic distance two but are not themselves three consecutive cyclic vertices. This equivalent characterization is used for the elementary edge count and for the finite certificate, but the independent checker validates the forcing rule directly rather than assuming the characterization.

## Proof

**1. Minimum sets and the valid-three-whites predicate.** If at least four vertices are white, each blue vertex has at least two white neighbors in \(G_n\), since it is nonadjacent to only two other vertices. Thus an initial blue set of size at most \(n-4\) cannot force anything. With three whites \(W\), a first force is possible exactly when an initially blue vertex \(v\) has its two \(C_n\)-neighbors in \(W\). Equivalently \(W\) contains a cyclic-distance-two pair with its midpoint outside \(W\). Once the first force succeeds, exactly two whites remain. For \(n\ge7\), their open cycle neighborhoods can be distinguished by a currently blue vertex, which therefore forces one white in \(G_n\), and the last white then has a blue neighbor and is forced. Consequently the above first-force condition is necessary and sufficient. Among three distinct vertices, its failure despite containing a distance-two pair means that every such pair has its midpoint in \(W\), which occurs precisely when \(W\) is three consecutive cyclic vertices. This rederives the known description only to make this proof self-contained.

**2. Count legal slides by their retained white pair.** For any fixed two-white set \(P=\{a,b\}\), let \(A(P)\) comprise the possible third white vertices \(x\) for which \(P\cup\{x\}\) is valid. Two such configurations are adjacent under an arbitrary exchange iff they share this retained pair \(P\); they are adjacent under a slide iff the two third vertices are *not* consecutive along \(C_n\). Thus every slide edge is counted once by

\[
|E(\mathcal S_n)|=\sum_{P\in\binom{V(C_n)}2}
\left(\binom{|A(P)|}{2}-e_{C_n}(A(P))\right),
\]

where \(e_{C_n}(A(P))\) counts edges of the underlying cycle induced by \(A(P)\). For \(n\ge9\), elementary inspection of the allowed third position gives the following five distance classes (cyclic distance in \(C_n\)): for distance \(1,2,3,4,\ge5\), the values of \(|A(P)|\) are \(2,n-3,4,3,4\), respectively. There are \(n\) pairs of each distance \(1,2,3,4\), and the remaining \(\binom n2-4n\) pairs have greater distance. Therefore the total number of *unrestricted* exchange edges, counted here only as an intermediate quantity, is

\[
\sum_P \binom{|A(P)|}{2}=n\left(\binom n2-11\right).
\]

The number of prohibited exchanges (the third vertices are consecutive in \(C_n\)) is exactly \(n(n-2)\). To see this, for \(n\ge11\), a distance-two pair contributes \(n-4\) prohibited third-position pairs, each distance-three pair contributes one, each distance-five pair contributes one, and no other pair contributes any. There are \(n\) pairs in each of these three distance classes. At \(n=10\), each of the five antipodal distance-five pairs contributes two rather than one, giving the same total; at \(n=9\), distance-four pairs supply the last \(n\) forbidden moves instead of distance-five pairs. The total remains \(n(n-4)+n+n=n(n-2)\) throughout \(n\ge9\). Subtraction yields the displayed formula

\[
|E(\mathcal S_n)|=n\left(\binom n2-11\right)-n(n-2)
=\frac{n(n-6)(n+3)}2.
\]

The exceptional values \(n=6,7,8\) are established by direct labelled exhaustive checking, including each actual legal edge; `verify_small.py` reproduces those values without using the third-position formula.

**3. An exact bounded model for all shortest paths.** Take any two successful white triples \(W,T\), with union \(U=W\cup T\). If they differ, \(4\le m=|U|\le6\). Arrange the \(m\) sites of \(U\) around the cycle and write their \(m\) positive clockwise gaps as \(g_0,\ldots,g_{m-1}\). Replacing each gap \(g_i\) by \(\min(g_i,7)\), and rotating the list cyclically to its lexicographically least representative, preserves all adjacency and cyclic-distance-two relations between the sites of \(U\). More importantly, those relations are still preserved after inserting any one auxiliary site at cyclic distance at most two from a member of \(U\): on a gap of length at least seven, the two radius-two endpoint neighborhoods remain separated by at least three edges. Hence both the validity of *every* three-white intermediate set using the six original sites and at most one such auxiliary site, and the legality of *every* slide between them, are unchanged by this compression. Expansion of gaps larger than seven lifts any certified path back to the original cycle.

The resulting finite set of canonical profiles is completely exhausted by \(m\in\{4,5,6\}\), \(g_i\in\{1,\ldots,7\}\), \(\sum_i g_i\ge7\), and cyclically lexicographically minimal gap lists. `profile_certificate.cpp` iterates these profiles and all unordered pairs of valid three-subsets \(W,T\) whose union consists of all \(m\) marked sites. It finds, in every case, a legal path of length at most four using only the marked sites and, when needed, one auxiliary site within cycle distance two. There are exactly **23,659** canonical profiles and **10,713** eligible configuration pairs. A human-readable 10,713-row path certificate is embedded as `gap_certificate.tsv`; for each case its line states the gap list, source and target bitmasks, optional auxiliary site and the complete intermediate-state sequence.

The separately implemented `verify_gap_certificate.py` independently regenerates *every* canonical gap profile and eligible source-target pair, checks that the 10,713 certificate lines cover them exactly once, and checks each path through literal ordinary-zero-forcing simulation and direct adjacency tests in the relevant graph complement. It reports `all_paths_at_most_four=PASS`. This finite check is sufficient for the **unbounded** domain by the compression-and-lifting argument just given; it is not an inference from checking finitely many consecutive cycle orders. Together the certificate and lifting prove that \(\mathcal S_n\) is connected with diameter at most four for every \(n\ge7\).

**4. Four moves are sometimes necessary.** At \(n=7\), choose \(W=\{0,2,4\}\) and \(T=\{1,5,6\}\). For all \(n\ge8\), choose \(W=\{0,2,4\}\) and \(T=\{1,3,5\}\). All chosen triples are valid, and each source and target is disjoint. Therefore any path of three single-position swaps must replace each initial site by a target site, without any auxiliary site or repeated replacement. The 36 possible orders and bijections can be checked directly against the ordinary forcing condition; none is valid. For \(n\ge8\), the adjacency and distance-two pattern on the six specified sites is unchanged as \(n\) grows, so the check at \(n=8\) is sufficient for the entire infinite range. `verify_lower_bound.py` explicitly checks this and the \(n=7\) boundary. Thus the diameter is at least four, completing the sharp equality for every \(n\ge7\).

**5. The disconnected small-order boundary.** Direct enumeration of the \(\binom63=20\) three-white subsets gives 14 successful triples. The local slide graph has 18 edges, one 12-state component, and two isolated states, as checked by direct zero-forcing simulation and breadth-first search in `verify_small.py`. This is the sharp failure at six vertices.

## Verification

From a standard Python 3 installation and a C++17 compiler, in one directory containing the supplied artifacts, run:

```bash
g++ -O3 -std=c++17 profile_certificate.cpp -o profile_certificate
./profile_certificate > gap_certificate_replay.tsv
cmp gap_certificate.tsv gap_certificate_replay.tsv
python3 verify_gap_certificate.py
python3 verify_small.py
python3 verify_lower_bound.py
```

The certificate generator must finish with `profiles=23659`, `cases=10713`, `failed=0`. The checker must print `VALID_CERTIFICATE profiles=23659 eligible_pairs=10713 all_paths_at_most_four=PASS`; direct enumeration covers all \(6\le n\le18\), including every vertex-pair shortest distance, and prints `ALL_DIRECT_SMALL_ORDER_CHECKS_PASS`; the lower-bound checker prints `LOWER_BOUND_CERTIFICATE_PASS`. The certificate's states are bitmasks: bits \(0\) through \(m-1\) correspond to marked sites, and optional bit \(m\) to the auxiliary vertex. The scripts and data are fully included and do not fetch external dependencies. The case enumeration covers the unlimited parameter domain through the proved gap compression, rather than by extrapolating a measured pattern.

## Relationship to prior work

Geneson, Haas and Hogben introduced the zero-forcing reconfiguration graph defined by unrestricted replacement of one member of a minimum zero-forcing set; its vertex-replacement condition is not the adjacency-constrained slide rule studied here. Curl, Fallat, Moruzzi, Reinhart and Young determined the minimum ordinary zero-forcing number for relevant graph complements, including cycle complements. Two earlier published mathematical results, *Zero-forcing polynomials of complements of paths and cycles* and *Ten-cycle signatures in minimum zero-forcing exchange graphs of two-factor complements*, provide the exact minimum-set classification and the unrestricted jump count and diameter. None of those already obtained counts or classifications is asserted as novel here. The present result removes exactly \(n(n-2)\) forbidden jumps for \(n\ge9\) and proves that the resulting genuinely local reconfiguration graph remains connected of sharp diameter four. The adjacency restriction cannot be inferred from unrestricted diameter three without further analysis.

## Limitations

The theorem is specific to complements of single cycles, not complements of arbitrary disjoint unions of cycles, complements of paths, nor zero-forcing variants such as skew or positive-semidefinite zero forcing. Its infinite-range diameter proof relies on an explicitly included finite exhaustive gap certificate plus a separately proved preservation lemma; external independent scientific validation has not been performed. Although relevant primary sources and indexed mathematical results were compared, unindexed historically equivalent theorems remain a residual originality risk. The exact radius and full all-pairs distance distributions in the infinite family are not claimed.

## References

1. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first submitted 1 September 2020. https://arxiv.org/abs/2009.00220
2. E. Curl, S. Fallat, R. Moruzzi Jr., C. Reinhart and D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932, first submitted 8 June 2022. https://arxiv.org/abs/2206.03932
3. *Zero-forcing polynomials of complements of paths and cycles*, prior published exact classification of minimum sets and their cardinality enumerator (2026).
4. *Ten-cycle signatures in minimum zero-forcing exchange graphs of two-factor complements*, prior published classification of unrestricted single-token exchanges and their metric (2026).
5. N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642 (2025), relevant distinction between forcing variants. https://arxiv.org/abs/2501.03642
