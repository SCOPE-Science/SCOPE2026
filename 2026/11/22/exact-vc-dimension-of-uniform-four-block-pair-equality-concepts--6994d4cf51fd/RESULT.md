# Exact VC dimension of uniform four-block pair-equality concepts

## Finding

Let \(m\ge 1\) be an integer and let \(V\) be a labeled set of cardinality \(4m\). The concept class \(\mathcal Q_m\) consists of every partition of \(V\) into exactly \(m\) unordered blocks of **exactly four vertices**, with the binary query \(\{u,v\}\in\binom V2\) labeled one precisely when \(u\) and \(v\) belong to the same block. The exact static shattering dimension is

\[
\boxed{\operatorname{VCdim}(\mathcal Q_m)=\begin{cases}0,&m=1,\\3m-2,&m\ge2.\end{cases}}
\]

For every \(m\ge2\) an explicit fixed query support of \(3m-2\) pairs realizes **all** its \(2^{3m-2}\) Boolean labelings. The construction requires resolving exactly two small Hall-capacity exceptions, both of which are realizable by a different grouping. No claim about the adaptive Littlestone dimension or the complete shattering polynomial is made.

## Assumptions and scope

Blocks are unordered, all ground vertices are labeled and distinct, and every block has cardinality exactly four. Queries are *distinct unordered pairs* of vertices. The same partition may realize more than one query-support witness but the support is shattered only if every one of its possible assignments of zero or one occurs among traces of the class. The empty support is always shattered because the concept class is nonempty. The proof below applies to all integers \(m\ge2\), including the two-block boundary, although previous two-block results already cover that boundary by specialization.

## Proof

**Upper bound by saturation of four-block forests.** If a query set \(S\subseteq\binom V2\) is shattered, there exists a four-block partition \(\pi\) realizing its all-positive labeling. Every queried edge is therefore internal to one of the \(m\) blocks. The subgraph of \(S\) within any block is a forest: if it contained a cycle, labeling one cycle edge zero and all other edges of the cycle one would contradict transitivity of equality. A forest on four vertices has at most three edges, so \(|S|\le3m\). Suppose \(|S|\ge3m-1\). Necessarily at least \(m-1\) blocks contain three queried edges; their positive-edge forests are spanning trees of their four-vertex blocks. There is an edge \(e\in S\) in the remaining block (also when every block has three edges). Assign zero to \(e\) and one to all other edges of \(S\). The spanning positive trees force each of the other \(m-1\) complete four-vertex blocks to remain intact in any realizing partition. The last four vertices must constitute the final block, forcing both endpoints of \(e\) to be equivalent, a contradiction. Hence \(|S|\le3m-2\).

**An explicit candidate support.** Divide \(V\) into \(m\) nominated four-vertex groups \(B_i=\{c_i,a_i,b_i,d_i\}\), for \(1\le i\le m\). In the first \(m-2\) groups query the three edges \(c_ia_i,c_ib_i,c_id_i\). In each of the last two groups query only \(c_ia_i,c_ib_i\) and leave \(d_i\) unqueried. Call the union \(S_*\). It has \(3(m-2)+4=3m-2\) pairs (the expression is valid when \(m=2\), with no full-star groups).

**Packing arbitrary prescribed labels.** Fix any binary labeling of \(S_*\). For each group \(i\), let \(G_i\) be its center \(c_i\) together with all queried leaves whose queried edge receives one; the negative leaves form \(R_i\). Let \(s_i=4-|G_i|\) be the number of vacancies in a proposed final block containing \(G_i\), and put \(\varepsilon_i=0\) for \(i\le m-2\) and \(\varepsilon_i=1\) for the last two groups. Then \(|R_i|=s_i-\varepsilon_i\). The two last-group unqueried leaves form a set \(F\) of two freely assignable tokens. Thus the disjoint token collection \(F\sqcup\bigsqcup_iR_i\) has exactly \(\sum_i s_i\) vertices. To realize the labeling it suffices to fill the vacancies of each block \(G_i\) with these tokens, subject only to each token from \(R_i\) being forbidden from rejoining its own core \(G_i\). Each token in \(F\) may go to any core.

Form a bipartite graph from tokens to individual unit vacancies. A token from \(R_j\) is adjacent to every vacancy outside block \(j\); free tokens are adjacent to every vacancy. By Hall's marriage theorem, a perfect assignment exists if and only if every set of unit vacancies has at least as many neighboring tokens. If vacancies belong to two or more different cores, **every token** is adjacent to at least one of those cores, so Hall is automatic. If they belong to just core \(i\), the strongest condition is

\[
 s_i\le \sum_j s_j-|R_i|\quad\Longleftrightarrow\quad 2s_i\le\sum_j s_j+\varepsilon_i.
\]

Hence if these \(m\) inequalities hold, a partition into four-blocks realizing every queried label exists. Indeed, each core is inside one final block, no negative leaf returns to its own core, and all vertices are used exactly once.

**The first exceptional capacity profile.** Suppose one of the Hall inequalities fails for a full-star group \(i\le m-2\). Every full-star \(s_i\) lies in \(\{0,1,2,3\}\), and both deficient groups always satisfy \(s_{m-1},s_m\ge1\). Hence failure forces \(s_i=3\), every other full-star capacity equal to zero, and both last-group capacities equal to one. The three queried leaves \(x,y,z\) of group \(i\) are negative relative to \(c_i\); the two last-group cores \(G_{m-1},G_m\) each have three vertices, with free leaves \(d_{m-1},d_m\). Retain each other full-star group as an intact block and use these three new blocks:

\[
G_{m-1}\cup\{c_i\},\qquad G_m\cup\{x\},\qquad \{y,z,d_{m-1},d_m\}.
\]

They have size four and realize every answer: the two last-group queried pairs are positive, while each of \(x,y,z\) is separated from \(c_i\).

**The second exceptional capacity profile.** If a Hall inequality fails at one deficient group \(i\in\{m-1,m\}\), then \(s_i\le3\), the other deficient group \(j\) has \(s_j\ge1\), and all full-star capacities are nonnegative. Failure forces \(s_i=3\), \(s_j=1\), and all full-star capacities zero. Now the two queried leaves \(x,y\) of group \(i\) are negative, its center is \(c_i\), and \(G_j\) is a positive three-vertex core. Keep all full-star groups as intact blocks and replace the two deficient groups by

\[
G_j\cup\{c_i\},\qquad\{x,y,d_{m-1},d_m\}.
\]

Both have size four. The required negative edges from \(c_i\) to \(x,y\) cross blocks, and the positive pairs of \(G_j\) remain in the same block. These are all possible Hall failures because any failure requires capacity three and the indicated minimum capacity contributions from the other distinguished groups. Therefore every labeling on \(S_*\) is realizable. This proves \(\operatorname{VCdim}(\mathcal Q_m)\ge3m-2\). Together with the upper bound, equality follows for all \(m\ge2\).

For \(m=1\) only the indiscrete partition into one four-element block exists. Every query is constantly positive, so its VC dimension is zero.

## Verification

The self-contained Python program `VERIFY.py` has no nonstandard dependencies. It constructs a realizing partition for every one of the \(2^{3m-2}\) labelings on \(S_*\) for each \(m=2,3,4,5\), checking disjointness, exact block size, complete vertex coverage, and all pair-query labels. Separately, it **independently enumerates all** 35 partitions into two fours and all 5775 partitions into three fours, checking that their trace sets on \(S_*\) have exactly 16 and 128 elements. For the two-block case it also enumerates all 26,040 five-query supports lying in an all-positive hypothesis and checks each fails shattering. Run `python3 VERIFY.py` and compare its standard output with `verification_output.txt`.

These are finite checks only. The Hall theorem and capacity-exception classification above prove the formula for every \(m\).

## Relationship to prior work

Bressan, Cesa-Bianchi, Paudice and Vitale (2019), in their VC-based treatment of pairwise similarity queries, explicitly allow partitions with no restriction on the number or size of clusters. Their unrestricted-partition bounds do not imply the constrained equality above. Liu and Mukherjee (first public 2021; COLT 2022) study the number of oracle queries needed to identify a partition, which is distinct from static VC dimension.

A previously published result, *A sharp static–online gap for uniform triple partitions*, determines the VC and Littlestone dimensions for **three-vertex** blocks; it neither states nor implies the four-vertex theorem from its hypotheses. *Forest size profiles determine shattering by fixed-cardinality cuts* studies exactly **two** prescribed-size blocks; this already covers the two-block \(m=2\) boundary but not an unbounded number of equal four-vertex blocks. *Shattering complexes and maximal-face spectra of size-capped equivalence relations* and *Refinement-closed partition concepts* allow variable-sized blocks, respectively bounded above or refinement closed. Their positive-forest sufficiency arguments cannot guarantee an exact four-vertex block partition for every answer string. The present proof resolves this exact-cardinality obstruction by a Hall matching and explicit exceptional rearrangements. Relevant source full texts, not just titles, were compared.

## Limitations

No adaptive Littlestone dimension or full shattering polynomial is claimed. The theorem is not a classification for arbitrary fixed block size, and the two-block case overlaps with known exact two-block results. The proof uses Hall's classical marriage theorem. Searches of accessible publications and indexed research cannot certify global historical priority; independent proof audit is not yet performed.

## References

1. M. Bressan, N. Cesa-Bianchi, A. Paudice and F. Vitale, *Correlation Clustering with Adaptive Similarity Queries*, arXiv:1905.11902v1, first public 2019-05-28, Sections 1 and 5. https://arxiv.org/html/1905.11902v3
2. X. Liu and S. Mukherjee, *Tight query complexity bounds for learning graph partitions*, arXiv:2112.07897v1, first public 2021-12-15; COLT 2022, https://proceedings.mlr.press/v178/liu22a.html
3. *A sharp static–online gap for uniform triple partitions*, published published-finding corpus record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-static-online-gap-for-uniform-triple-partitions--165fac9eb392/RESULT.md
4. *Forest size profiles determine shattering by fixed-cardinality cuts*, published published-finding corpus record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-forest-size-profiles-determine-shattering-by-fixed-cardinality-c--e71e3de9534e/RESULT.md
5. *Shattering complexes and maximal-face spectra of size-capped equivalence relations*, published published-finding corpus record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-shattering-complexes-and-maximal-face-spectra-of-size-capped-equ--8b7b35a2f27d/RESULT.md
6. *Refinement-closed partition concepts: exact shattering supports, online dimension, and coloring quotients*, published published-finding corpus record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-refinement-closed-partition-concepts-exact-shattering-supports-o--2203ea0ddc4a/RESULT.md
