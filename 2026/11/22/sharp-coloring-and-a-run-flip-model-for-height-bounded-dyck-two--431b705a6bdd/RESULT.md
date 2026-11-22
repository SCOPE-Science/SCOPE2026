# Sharp coloring and a run-flip model for height-bounded Dyck two-read deletion graphs

## Finding
Let \(\mathcal D_n^{(H)}\) be all binary Dyck words of semilength \(n\ge1\) whose prefix heights never exceed \(H\ge1\). Define a graph \(G_n^{(H)}\) by joining distinct words when their **sets** of one-deletion descendants have at least two distinct words in common. The following statements hold for all such parameters.

1. For \(H=1\) the graph has one vertex; for every \(H\ge2\),
\[
\chi(G_n^{(H)})=\omega(G_n^{(H)})=n.
\]
For all heights, the one-position sum modulo \(n\) gives a proper vertex coloring. Each color is a two-read zero-error code; the equality is about the *minimum number of codes in a partition*, not the largest individual code.
2. The height-at-most-two graph is isomorphic to a binary **constant-block-flip graph** on \(n-1\) bits: distinct vectors are adjacent if and only if their differences form one nonempty consecutive interval on which the first vector is constant (and the second is its complement).
3. If the maximal constant-run lengths of a vector are \(r_1,\ldots,r_t\), its degree is \(\sum_{i=1}^t\binom{r_i+1}{2}\), so the maximum degree is \(\binom n2\), with two maximizers when \(n\ge2\). The exact number of edges is
\[
|E(G_n^{(2)})|=(n-2)2^{n-1}+1.
\]
(The right-hand side is zero at \(n=1\).)
4. The component-count coloring on the height-two source has classes of sizes \(\binom{n-1}{j-1}\) for \(1\le j\le n\). For \(n\ge5\), an induced five-cycle exists in \(G_n^{(2)}\), hence \(G_n^{(H)}\) with \(H\ge2\) need not be perfect.

## Assumptions and scope
The symbols \(1\) and \(0\) are up- and down-steps. A Dyck word has \(n\) ones, \(n\) zeros, all prefix heights nonnegative, final height zero, and maximum prefix height at most \(H\). Deleting exactly one symbol produces a **set** of distinct length-\(2n-1\) words; two distinct common descendants, not two deletion positions yielding the same descendant, trigger adjacency. Graphs are simple and undirected. The height ceiling is inclusive. A primitive component is a nonempty Dyck excursion between successive returns to height zero. The \(n=1\) and \(H=1\) boundary cases are included. These graphs model two-read deletion reconstruction only, not arbitrary deletion multiplicities or optimal individual code sizes.

## Proof
**A. Pairwise deletion ambiguity lemma (published).** A result of Cai, Kiah, Nguyen and Yaakobi (2020, Proposition 9) establishes that two distinct equal-length binary words have two distinct common one-deletion descendants precisely when their first-to-last differing substring is a pair of opposite phases of a binary alternating word of length at least two, with all other positions identical. Their deletion-ball intersection has at most two distinct members. For equal-content Dyck words, flipping an odd-length alternating interval changes the one-count, so any confusable pair necessarily differs on an even-length alternating interval of length \(2\ell\), where \(\ell\ge1\). This published lemma is used, not claimed as new.

**B. Optimal coloring at any allowed height.** Define \(S(w)=\sum_{i:w_i=1} i\), using one-indexed positions, and color \(w\) by \(S(w)\pmod n\). For an adjacent pair, the alternating interval has length \(2\ell\); shifting its one-positions from the odd to even local sites (or vice versa) changes \(S\) by exactly \(\ell\) or \(-\ell\). The case \(\ell=n\) would invert the entire word and force one source to start with \(0\), impossible for a Dyck word. Hence \(1\le\ell\le n-1\), and the residues differ; this gives \(\chi\le n\). If \(n=1\), the single Dyck word makes the assertion immediate. For \(H\ge2\), the following \(n\) words provide a clique: for \(j=0,1,\ldots,n-1\), take
\[
w_j=1(10)^j(01)^{n-1-j}0.
\]
They all have maximal height at most two. For any two distinct indices, the intervening changed pair-blocks form one even alternating interval with complementary phases, so the published lemma makes them adjacent. Thus \(\omega\ge n\), forcing \(\chi=\omega=n\). With \(H=1\), the sole word is \((10)^n\), hence both invariants are one.

**C. Exact model for height two.** A Dyck path of height at most two is uniquely
\[
w(b)=1\,B_{b_1}\cdots B_{b_{n-1}}\,0,
\quad B_0=10,\quad B_1=01,
\qquad b\in\{0,1\}^{n-1}.
\]
Indeed, the first step must be up and the last down. Between those boundary steps the height is always either one or two, and every two successive steps must return to height one, so each two-step block is \(10\) or \(01\); conversely every such concatenation is Dyck with height at most two. When \(b\) and \(b'\) differ at index \(i\), both sites of block \(i\) differ, and when they agree neither site differs. Therefore the first-to-last difference interval is exactly the union of the pair-blocks from the first to the last changed indices. That interval is an opposite-phase alternating pair if and only if all these indices change and all the source pair-blocks have the same orientation, equivalently \(b\) is constant on one nonempty consecutive interval and \(b'\) flips precisely it. This proves the graph isomorphism without relying on a numerical coincidence.

**D. Exact edge and degree enumeration.** If the maximal runs of \(b\) have lengths \(r_i\), exactly \(\binom{r_i+1}{2}\) nonempty intervals lie wholly within run \(i\). Each yields a distinct neighbor and every neighbor arises exactly this way, proving the degree formula. As \(\sum_i r_i=n-1\), the maximum is \(\binom n2\) (all bits constant); for \(n\ge2\) precisely the two constant vectors attain it. An undirected edge corresponds uniquely to its flipped interval of length \(\ell\) together with the unchanged exterior; the interval has \(n-\ell\) possible locations among \(n-1\) bits and the exterior has \(2^{n-1-\ell}\) choices. The two choices of constant bit before flipping specify the same unordered edge, so
\[
|E|=\sum_{\ell=1}^{n-1}(n-\ell)2^{n-1-\ell}=(n-2)2^{n-1}+1.
\]
For \(n=1\), the sum is empty and is zero. The edge-number expression happens to equal a known formula for a different unrestricted binary reconstruction graph at length \(n\); numerical equality does not imply that the graphs or their proofs are the same.

**E. Exact code partitions and an odd hole.** In the displayed encoding, every \(B_1=01\) passes through height zero on its first step, while \(B_0=10\) never reaches height zero in the interior. Thus \(w(b)\) has \(1+\#\{i:b_i=1\}\) primitive components; neighboring vectors change this number by a nonzero amount, so it is a proper \(n\)-coloring. Exactly \(\binom{n-1}{j-1}\) bit vectors have \(j\) components. For \(n\ge5\), take the following five distinct vectors in \(\{0,1\}^{n-1}\), each padded by an identical trailing string of \(n-5\) zeros:
\[
1111,\quad1101,\quad0101,\quad0100,\quad0000.
\]
Consecutive vectors (including the final and first) differ by flipping one constant block. Every nonconsecutive pair has differences that are either nonconsecutive or span a source block with mixed symbols, hence is not adjacent. They therefore induce \(C_5\), which has clique number two and chromatic number three. The ambient height-two graph is not perfect for all \(n\ge5\), despite its own equality \(\chi=\omega=n\). This also supplies an induced odd hole in every higher-ceiling graph because the height-two source forms an induced subgraph.

## Verification
Run `python3 verify_decks.py` and `python3 verify_structure.py` using Python 3 standard library only. The first verifier constructs distinct deletion balls directly for every Dyck word through semilength eight, checks all pairs at each semilength against the position-sum coloring, verifies the height-two encoding, checks all height-two edges against the constant-run flip rule, and checks edge totals. The second independently enumerates the bit-vector model through dimension eleven and checks the degrees, edge formula, equal-weight independence, explicit \(n\)-clique, and induced five-cycle. All assertions passed on the stated ranges. These finite tests are consistency checks, not a proof for unbounded \(n\); the universal claims follow from Parts A–E.

## Relationship to prior work
Sala, Gabrys, Schoeny and Dolecek (public preprint 2016) formulated exact reconstruction with synchronization codes, mainly for insertion channels. Cai, Kiah, Nguyen and Yaakobi (2020) proved the alternating-interval intersection criterion used in Part A; their broader reconstruction constructions do not directly give the height-restricted graph isomorphism, edge partition, or sharp chromatic number. Published exact-edge and maximum-clique formulas for the unrestricted binary deletion-confusability graph count different ambient vertex sets. A separately published unrestricted-binary graph result already uses a triangular run-length degree formula on maximal one-runs of its XOR-difference word; that formula is an antecedent, but it is not the same as the height-two graph degree formula on runs of both bits. A published Dyck-restricted graph result enumerates edges and its largest degree *without* a height ceiling and does not establish the height-two constant-block model or the chromatic number. Separately known fixed-Hamming-weight coloring results give an upper bound \(n+1\) for the semilength-\(n\) Dyck subset, which is not sharp here. The present sharper \(n\)-coloring exploits the forbidden first/last symbol flip and the explicit height-two clique; the checksum method is adapted from the known classical construction and is not independently novel. The simple edge-count expression numerically coincides with a previously recorded unrestricted-binary formula, so only the graph interpretation and combined structural statement are proposed as new.

## Limitations
This establishes the optimal **number** of disjoint two-read codebooks covering the Dyck language, not the maximum number of codewords in any single one. It gives a full degree statistic only at height at most two, not the unrestricted Dyck graph. The published pairwise-deletion lemma is assumed. An unindexed earlier graph-theoretic equivalence may subsume part of the result. No independent mathematical audit was performed.

## References
1. F. Sala, R. Gabrys, C. Schoeny and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, first public preprint 2016-04-11, arXiv:1604.03000, https://arxiv.org/html/1604.03000v2.
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, Definition 8 and Proposition 9, https://arxiv.org/html/2001.01376v2.
3. *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*, available as a published mathematical record in the published-finding corpus corpus (2026).
4. *Sharp clique bound and two-pencil structure in the two-read single-deletion graph*, published mathematical record (2026).
5. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published mathematical record (2026).
