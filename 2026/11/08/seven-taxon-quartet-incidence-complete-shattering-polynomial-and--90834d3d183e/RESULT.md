# Seven-taxon quartet incidence: complete shattering polynomial and extremal orbit census

## Finding

Let \(L=\{0,1,2,3,4,5,6\}\). Let \(\mathcal T_7\) consist of all unrooted, unweighted, binary phylogenetic trees with leaf set \(L\) (all nonleaf vertices have degree three). A *quartet query* is an unordered pairing \(ab\mid cd\) of four different leaves, asking whether the paths between \(a,b\) and between \(c,d\) are vertex-disjoint in the unknown tree. Write \(\mathcal Q_7\) for all \(105\) such queries, and \(C_T\subseteq\mathcal Q_7\) for the queries displayed by \(T\). A support \(S\subseteq\mathcal Q_7\) is *shattered* when every subset \(R\subseteq S\) equals \(C_T\cap S\) for some \(T\in\mathcal T_7\).

**Theorem (exact finite classification).** The full shattered-support polynomial is
\[
\Phi_7(z)=\sum_{S\text{ shattered}}z^{|S|}
=1+105z+5355z^2+171045z^3+3305610z^4+1586970z^5+8820z^6.
\]
Thus \(\operatorname{VCdim}(\{C_T:T\in\mathcal T_7\})=6\). The \(8820\) six-query shattered supports form **exactly three** orbits under relabeling by \(S_7\), of cardinalities \(1260,2520,5040\).

The smaller-taxon values for the same binary one-versus-rest quartet-query concept class are \(1,2,3\) on \(4,5,6\) leaves respectively. The seven-taxon increase from \(3\) to \(6\) is therefore a genuine first small-order change in this statistic, not a change of query semantics.

## Assumptions and scope

There are \((2\cdot7-5)!!=945\) labeled unrooted binary phylogenetic trees on seven leaves. For each four-element leaf subset, exactly three quartet queries exist; hence \(|\mathcal Q_7|=3\binom74=105\). These are **binary indicators of individual resolved quartets**: for each query, positive means that exact resolution is displayed, and negative permits *either* of the other two resolutions. This is not the multiclass Natarajan-shattering condition, which fixes two alternative responses for each queried four-set. Multiple queries on a single four-set are distinct coordinates, though no two of them can both be positive in one tree.

Only \(4\le |L|\le7\) is addressed computationally; the theorem and full polynomial concern seven leaves. There is no claimed formula for general leaf number or for Natarajan dimension.

## Proof

**1. Complete representation of the tree class.** Root an unrooted binary tree at the leaf labeled \(0\), discard that leaf and regard its adjacent vertex as a root with two children. The remaining six labeled leaves form a full rooted binary hierarchy. Each nonsingleton cluster other than the full six-leaf set is exactly the side not containing \(0\) of a nontrivial edge split. Enumerate all such hierarchies recursively: partition any nonsingleton leaf set into two nonempty parts, require its least leaf in the first part to suppress child-order duplication, and recurse independently on both parts. There are exactly \(945\) distinct four-split sets. A separate generation procedure inserts leaves one by one into edges of unrooted trees and obtains precisely the same \(945\) sets.

**2. Exact quartet incidence.** Represent a nontrivial split by the seven-bit integer whose set bits are its leaves on the side excluding \(0\). A tree displays \(ab\mid cd\) exactly when one of its split masks puts \(a,b\) together on one side and \(c,d\) together on the other. An independent calculation via tree distances verifies the equivalent strict four-point inequalities
\[
d(a,b)+d(c,d)<d(a,c)+d(b,d),\quad
d(a,b)+d(c,d)<d(a,d)+d(b,c)
\]
for every tree and every query. Each query is displayed by \(315\) of the \(945\) trees. These two independent constructions verify the entire \(945\)-by-\(105\) incidence matrix on which the exhaustive search rests.

**3. Symmetry-complete exhaustive shattering count.** Label the queries in increasing order by their sorted four-set and, within each four-set \(a<b<c<d\), in the order \(ab\mid cd\), \(ac\mid bd\), \(ad\mid bc\). The first query is \(q_0=01\mid23\). The symmetric group \(S_7\) acts transitively on the \(105\) quartet queries. Accordingly, it suffices to enumerate all shattered supports containing \(q_0\) and then double-count incidences between a support and its member queries.

For any current shattered prefix of \(k\) queries, maintain its \(2^k\) nonempty classes of trees with equal binary answer vectors. An additional query preserves shattering **if and only if** it splits every class into a nonempty positive class and a nonempty negative class. This is both necessary and sufficient from the definition of traces. Enumerate candidate queries in strictly increasing index order. Every shattered support containing \(q_0\) is reached exactly once because each of its subsets is shattered. The exhaustive search yields, by support size \(k=1,\ldots,7\),
\[
(M_1,M_2,M_3,M_4,M_5,M_6,M_7)
=(1,102,4887,125928,75570,504,0).
\]
Here \(M_k\) counts the shattered \(k\)-supports containing \(q_0\); the search visits \(206992\) prefixes. Double-counting \((S,q)\) with \(q\in S\) gives the global coefficient \(f_k=105M_k/k\). Substitution gives the displayed polynomial. Since shattering is downward closed, \(M_7=0\) excludes every support of size at least seven.

**4. Explicit lower-bound trace certificate.** The six queries at indices \((0,21,42,54,76,82)\) are
\[
01\mid23,\quad 01\mid45,\quad 02\mid46,\quad
03\mid56,\quad 15\mid26,\quad 14\mid36.
\]
The companion `WITNESSES.json` supplies for each of the \(64\) binary answer vectors a four-split hierarchy realizing it. The verifier reconstructs and checks all \(64\) of these witnesses. Thus existence of a shattered six-query support is independently checkable, rather than inferred only from the enumeration count.

**5. Extremal-orbit census.** Take the \(504\) size-six supports containing \(q_0\). For each smallest as-yet-unclassified support, apply all \(5040\) leaf permutations, canonically relabel the queries, and intersect the resulting orbit with supports containing \(q_0\). The three intersections have sizes \(72,144,288\); the corresponding full orbit sizes are \(1260,2520,5040\). They are disjoint, exhaust all \(504\) canonical-query supports, and their full sizes sum to \(8820\). This proves both the orbit count and the precise orbit spectrum.

## Verification

Run `python3 CHECKER.py` using Python's standard library. It independently constructs all trees by rooted hierarchies and by unrooted edge insertion, compares split-based and distance-based quartet truth values on every tree/query pair, exhaustively enumerates shattered supports containing the canonical query, checks the double-counting identities, checks all orbit sizes under \(S_7\), and validates all \(64\) explicit six-query witnesses. It also directly enumerates the smaller \(4\)-, \(5\)-, and \(6\)-leaf cases through the first forbidden face size.

The expected marker is `QUARTET7_PASS trees=945 queries=105 searched=206992`; the expected coefficient vector is `1,105,5355,171045,3305610,1586970,8820,0`. The argument is an **exhaustive finite proof**, not an extrapolation of a small sample. Each enumeration step and its symmetry reduction are justified above, and a separately generated incidence matrix checks the central computation.

## Relationship to prior work

Quartet compatibility, definitive quartet systems, and phylogenetic tree reconstruction are classical. Dowden's work on minimal definitive quartet sets concerns uniqueness of a tree realizing **positive** quartet constraints; it does not imply realization of all \(2^k\) positive/negative answer patterns, nor a complete shattering polynomial. Hellmuth–Schaller–Stadler study compatibility of partitions with trees and split systems rather than binary quartet-query traces. Avdiukhin and collaborators study multiclass hierarchical tree learning (particularly rooted triplets), including Natarajan/Littlestone dimensions; their stated results do not determine this seven-leaf one-versus-rest quartet trace complex. The more recent Arvanitakis–Chatziafratis–Luo–Makarychev work proves order-of-growth bounds for multiclass quartet Natarajan dimension; these bounds likewise do not determine the exact binary seven-leaf polynomial or its extremal orbits.

The novelty claim is limited to the **joint exact binary polynomial and extremal-orbit census** stated above; basic quartet definitions, hierarchy enumeration, tree-distance criteria, and classical phylogenetic results are not claimed as new.

## Limitations

This is a finite seven-leaf theorem; no extension to arbitrary taxon counts is proved. It does not characterize all inclusion-maximal lower-dimensional shattered faces, only all supports by cardinality and all maximum-cardinality ones up to relabeling. The absence of an identified prior tabulation is not proof of historical priority. Source coverage is limited to the named accessible literature and actual database searches; an earlier equivalent computation under different terminology remains possible. Independent mathematical audit has not been performed.

## References

- M. Hellmuth, D. Schaller, P. F. Stadler, *Compatibility of Partitions with Trees, Hierarchies, and Split Systems* (first public 2021-04-29), arXiv:2104.14146.
- D. Avdiukhin, G. Yaroslavtsev, D. Vainstein, O. Fischer, S. Das, F. Mirza, *Tree Learning: Optimal Algorithms and Sample Complexity* (first public 2023-02-09), arXiv:2302.04492; AAAI 2023, DOI:10.1609/aaai.v37i6.25822.
- C. Dowden, *On the maximum size of minimal definitive quartet sets* (2011), arXiv:1101.5302.
- D. Arvanitakis, V. Chatziafratis, Y. Luo, K. Makarychev, *Optimal Phylogenetic Reconstruction from Sampled Quartets* (2026), arXiv:2604.17461.
