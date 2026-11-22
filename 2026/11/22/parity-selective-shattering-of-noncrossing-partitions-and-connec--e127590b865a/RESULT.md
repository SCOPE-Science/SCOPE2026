# Parity-selective shattering of noncrossing partitions and connected chord diagrams

## Finding

Place \(n\ge3\) labeled points in strictly convex cyclic order. Let \(\mathcal N_n^{\mathrm{odd}}\) and \(\mathcal N_n^{\mathrm{even}}\) comprise, respectively, the noncrossing set partitions with an odd or an even number of blocks. A pair query \(\{i,j\}\) reports whether its endpoints belong to the same block.

**Theorem.** Both parity-restricted concept classes have exact VC dimension
\[
\operatorname{VCdim}(\mathcal N_n^{\mathrm{odd}})
=\operatorname{VCdim}(\mathcal N_n^{\mathrm{even}})=n-2.
\]
More finely, suppose \(n=2m\) with \(m\ge2\), and let \(M\) be *any* perfect matching of the \(2m\) points, regarded as a support of \(m\) pair queries. Construct the crossing graph \(\Gamma(M)\): its vertices are the matching chords, with adjacency when the relative interiors cross. Then
\[
\begin{aligned}
M\text{ is shattered by }\mathcal N_{2m}^{\mathrm{odd}}&\quad\text{for every }M,\\
M\text{ is shattered by }\mathcal N_{2m}^{\mathrm{even}}&\quad\Longleftrightarrow\quad\Gamma(M)\text{ is disconnected}.
\end{aligned}
\]
The two classes have the *same number of concepts* for every even \(n\) (exactly half the Catalan number), but differ on exactly \(c_m\) of the \((2m-1)!!\) perfect-matching supports, where \(c_m\) is the classical number of connected chord diagrams on \(m\) chords. For \(m=2,3,4\), respectively, the total, odd-shattered, even-shattered, and connected counts are
\[
(3,3,2,1),\qquad (15,15,11,4),\qquad (105,105,78,27).
\]
In particular, at six points the two equally large 66-concept strata have different complete three-query counts: \(371\) for even-block concepts and \(375\) for odd-block concepts. This last equality is a finite direct census, not an all-order formula for intermediate face counts.

## Assumptions and scope

A noncrossing partition has no distinct blocks with four cyclically alternating vertices \(a,b,c,d\) such that \(a,c\) lie in one block and \(b,d\) in the other. A support is shattered if each of its \(2^{|S|}\) Boolean labelings is realized by some partition of the stipulated block-number parity. The matching chords have distinct endpoints, whether or not they cross in their interiors; only crossing, *not* mere nesting, creates adjacency in \(\Gamma(M)\). All points are labeled and positioned on a single convex circle. The all-order matching theorem starts at \(m=2\); for \(m=1\) its odd-block assertion fails on the all-negative labeling.

## Proof

**1. Canonical noncrossing closure.** Fix a perfect matching \(M\) and a subset \(T\subseteq M\) of queries assigned answer one. Let \(r(T)\) be the number of connected components of the intersection graph of the chords of \(T\), with \(r(\varnothing)=0\). Put in one partition block all endpoints of the chords in each crossing component of \(T\), leaving every unmatched-by-\(T\) endpoint as a singleton. Denote this partition by \(\pi_T\).

This partition is noncrossing. Indeed, the embedded unions of chords belonging to different crossing components are disjoint connected planar subsets. If the endpoints of two such components interlaced, their respective connected sets would have to intersect by planar separation, forcing a crossing and hence merging their components. No remaining singleton on the circle crosses another block. Conversely, any noncrossing partition realizing the positive equality tests must merge both endpoints of each selected chord and must merge the blocks of every pair of crossing selected chords. By transitivity it coarsens \(\pi_T\). Thus \(\pi_T\) is the unique finest noncrossing partition satisfying all positive tests.

Write \(t=|M\setminus T|\). All negative-query endpoints are singletons in \(\pi_T\), so every assigned negative test is indeed zero. Its block count is exactly
\[
b(T)=2t+r(T).
\]

**2. Adjacent-block parity switch.** In a noncrossing partition, merging the blocks containing two *cyclically consecutive* points from different blocks preserves noncrossing: draw their connecting boundary edge, which crosses no interior block chord. The noncrossing equivalence closure of this new edge merges precisely those two blocks. Such a merger changes the number of blocks by one.

If \(t\ge1\), the cyclic sequence of block labels of \(\pi_T\) has at least \(b(T)\ge2t\) transitions between consecutive boundary vertices (every block contributes at least one cyclic run). At most \(t\) of these transitions are the \(t\) specified negative matching chords: since \(2m\ge4\), a matching edge can coincide with at most one of the \(2m\) distinct polygon sides. Thus at least one transition has consecutive endpoints in different blocks that are **not** a negative-query pair. Merge those blocks. This preserves all assigned test answers and reverses block-count parity. If \(t=0\) but \(r(T)\ge2\), the partition \(\pi_T\) also has adjacent different blocks and no negative tests, so one such merger again flips the parity while preserving all answers.

Consequently every answer pattern has realizations of *both* parities except possibly the all-positive pattern \(T=M\) with connected crossing graph \(\Gamma(M)\). In that exceptional case \(\pi_M\) has one block, and every realization must coarsen it, so exactly the odd-block parity is possible. This proves the perfect-matching classification. In the disconnected all-positive case, \(\pi_M\) has at least two blocks, so the parity switch applies as well.

**3. Exact VC dimension for both parities.** For any support \(S\) of pair queries, an ordinary graph cycle forbids shattering: assign all cycle edges but one equality one and the last edge zero. Hence a shattered support is an ordinary forest and has at most \(n-1\) edges. If it has \(n-1\) edges, it is a spanning tree. The all-positive labeling forces a one-block partition, and a labeling with exactly one tree edge negative forces exactly two blocks: the other positive edges form two connected components, and the negative edge prevents their merger. These labelings require opposite parities, so no fixed-parity family can shatter a spanning-tree support. Thus either parity class has VC dimension at most \(n-2\).

For the lower bound take the \(n-2\) successive boundary edges \(\{1,2\},\{2,3\},\ldots,\{n-2,n-1\}\), leaving vertex \(n\) outside this query support. For any positive subset \(T\) of these path edges, its positive-edge connected components yield a noncrossing interval partition realizing all labels, with the unqueried vertex \(n\) alone. Alternatively merge vertex \(n\) with the block containing \(n-1\) along the unqueried boundary edge \(\{n-1,n\}\). This changes the number of blocks by exactly one, preserves noncrossing, and preserves every tested label. Therefore every labeling has realizations of both parities, proving the matching lower bound and the stated VC equality for every \(n\ge3\).

**4. Equal-size parity strata and connected-chord deficit.** The Narayana rank formula for \(n\)-point noncrossing partitions is \(N(n,k)=\binom nk\binom n{k-1}/n\), symmetric under \(k\mapsto n+1-k\). For even \(n\) this involution exchanges odd and even \(k\), so the two concept classes are equinumerous. There are \((2m-1)!!\) perfect matchings on \(2m\) labeled points. Exactly those whose crossing graphs are connected fail even-block shattering, giving the asserted deficit \(c_m\). The values \(c_2=1,c_3=4,c_4=27\) are independently reproduced by complete enumeration below. The connected-chord sequence itself is established prior combinatorics; the new identity is its appearance as the parity-specific shattering deficit.

## Verification

Run `python3 verify_matching_parity.py` (standard Python, no dependencies). It enumerates restricted-growth strings representing all noncrossing partitions, filters by exact block parity, enumerates **every** perfect matching of \(4,6,8\) labeled points, and calculates *all* Boolean traces independently of the structural proof. It also constructs each crossing graph directly and verifies the theorem on all matchings. The output in `verification_output.txt` records the complete totals \((3,15,105)\), connected counts \((1,4,27)\), and all odd/even trace classifications. A separate all-triples test verifies the \(n=6\) face-count contrast \((371,375)\). These are finite corroborations; the arbitrary-size result rests on the four proof steps above.

## Relationship to prior work

Classical Narayana rank enumeration counts noncrossing partitions by block number, and classical connected-chord-diagram theory counts matching crossing graphs. Neither count alone determines equality-query shattering in a fixed parity stratum. Previous unrestricted noncrossing-partition shattering results give a geometric deletion test and \(\operatorname{VCdim}=n-1\) without any block-parity restriction. Their unrestricted all-positive closure lemma is used as a point of comparison; that result does **not** imply that all perfect matchings remain shattered in the odd rank-parity subfamily, nor the crossing-connected exclusion in the even family. Earlier noncrossing-perfect-matching incidence concepts ask whether an edge belongs to a perfect matching, a different domain and concept class. The present result classifies pair-*equality* tests against parity-restricted **set partitions**. The connection to connected chord diagrams here is a precise infinite-family count of missing faces, not a new enumeration of chord diagrams themselves.

## Limitations

The perfect-matching support classification assumes each of the \(2m\) endpoints is queried exactly once. It does not classify all pair-query supports of a given size or compute the full shattering polynomial for arbitrary \(n\). The VC formula does cover both parity classes for all \(n\ge3\). The small-order three-query count is established only at six points. The exact result is a mathematical consequence of the stated lemmas, not independent external certification; historical priority may depend on equivalent restricted-rank partition results outside the inspected sources.

## References

1. Z. Lin and D. Kim, *A combinatorial bijection on \(k\)-noncrossing partitions*, arXiv:1905.10526, first public 2019-05-25, https://arxiv.org/abs/1905.10526 (rank-refined noncrossing background).
2. C. M. Farmer, J. Hallam and C. Smyth, *The Noncrossing Bond Poset of a Graph*, arXiv:2012.07212, https://arxiv.org/abs/2012.07212 (noncrossing lattice and bond-poset background).
3. J. Courtiel, K. Yeats and N. Zeilberger, *Connected chord diagrams and bridgeless maps*, arXiv:1611.04611, https://arxiv.org/abs/1611.04611 (classical connected chord-diagram enumeration; earliest preprint 2016-11-14).
4. P.-H. Balduf, A. Cantwell, K. Ebrahimi-Fard, L. Nabergall, N. Olson-Harris and K. Yeats, *Tubings, chord diagrams, and Dyson–Schwinger equations*, *Journal of the London Mathematical Society* 110 (2024), e70006, https://doi.org/10.1112/jlms.70006 (full-text definitions of crossing and intersection connectivity).
5. *Geometric deletion criterion for shattering by noncrossing partitions*, published published-finding corpus result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-geometric-deletion-criterion-for-shattering-by-noncrossing-parti--f5f99d85cb8a (unrestricted equality-query shattering theorem).
