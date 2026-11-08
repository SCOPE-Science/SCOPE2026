# A sharp static–online gap for uniform triple partitions

## Finding

For every integer \(m\ge2\), let \(V\) be a labeled set of size \(3m\). Let \(\mathcal T_m\) consist of all partitions of \(V\) into exactly \(m\) **unordered blocks of size three**. Regard each partition as a Boolean function on the query domain \(\binom V2\), assigning value one to \(\{u,v\}\) precisely when its endpoints lie in the same block. Then

\[
\operatorname{VCdim}(\mathcal T_m)=2m-2,
\qquad
\operatorname{Ldim}(\mathcal T_m)=2m-1.
\]

For \(m=1\), both dimensions are zero. Thus, for every \(m\ge2\), the adaptive Littlestone dimension is strictly greater than the nonadaptive VC dimension, with an exact gap of one. A stronger witness property is proved below: a fixed set of \(2m-2\) queries has **at least two distinct realizing partitions for every possible labeling**.

## Assumptions and scope

All vertices are distinct and labeled, all blocks have cardinality exactly three, and the order of blocks is immaterial. All pair queries are available; the two queried vertices are distinct. A support is VC-shattered when all its binary labelings occur among the traces of \(\mathcal T_m\). The Littlestone dimension is the maximum depth of a complete binary tree whose internal nodes are pair queries and for which every root-to-leaf sequence of query answers is realized by a partition in the class. A complete tree may use different pair queries at different nodes. Finite partitions alone are studied: no probabilistic or noisy oracle is assumed. The claim does **not** concern arbitrary set partitions, partitions into blocks of varying sizes, or worst-case numbers of queries required to identify a partition exactly.

## Proof

**1. The VC upper bound.** Let \(S\subseteq\binom V2\) be shattered. The all-positive trace is realized by some partition \(\pi\) into \(m\) triples. Thus every edge of \(S\) lies within one of these triples. A triple cannot contain all three possible edges of \(S\): labeling two of them positive and the third negative contradicts transitivity of same-block membership. Hence every block contributes at most two query edges. If \(|S|\ge2m-1\), the preceding restrictions leave only the profiles \((2,\ldots,2)\) or \((2,\ldots,2,1)\) for the numbers of queried edges in the \(m\) blocks. In the first profile, make one edge negative and all the others positive. The remaining positive edges force \(m-1\) complete triples; the three leftover vertices must form the final triple, so the negative edge is impossible. In the second profile, make the sole queried edge in the last block negative and every other edge positive; the other \(m-1\) complete triples again force the remaining three vertices to form one block. Both profiles contradict shattering. Therefore \(|S|\le2m-2\).

**2. A shattered support with \(2m-2\) queries.** Divide \(V\) into \(m\) triples. On \(m-1\) of them, write the three vertices as \((a,b,c)\) and query \(\{a,b\}\) and \(\{b,c\}\); leave the remaining triple completely unqueried. Denote the query set by \(S_0\). Given an arbitrary labeling of \(S_0\), keep every queried triple with both queries positive as one block. Each of the other, or *broken*, queried triples can be split into a pair \(P\) and a singleton \(s\), so that positive queries remain inside \(P\) and negative queries run between \(P\) and \(s\): use \((P,s)=(\{a,b\},c)\) for answers \((1,0)\), \((\{b,c\},a)\) for \((0,1)\), and \((\{a,c\},b)\) for \((0,0)\). If no triple is broken, use the initial partition. If one is broken, put its pair with one vertex of the unqueried triple, and put its singleton with the other two unqueried vertices. If \(r\ge2\) queried triples are broken, list their pairs and singletons as \((P_1,s_1),\ldots,(P_r,s_r)\); make blocks \(P_j\cup\{s_{j+1}\}\) with cyclic indices, and keep the unqueried triple intact. All blocks have size three; every negative query crosses blocks. Thus all \(2^{2m-2}\) labelings are realized and \(\operatorname{VCdim}\ge2m-2\).

**3. The Littlestone upper bound.** Suppose a complete mistake tree of depth \(2m\) existed. Follow the positive answer at each of its first \(2m-1\) nodes. Because the negative answer must also be possible at every node, no newly queried pair can have endpoints already connected by earlier positive queried edges; such a pair would be forced positive. The positive-edge graph on this branch is therefore a forest. At the end of these \(2m-1\) positive answers, some partition into triples still realizes them. Inside each of its \(m\) triples the forest has at most two edges. There are \(2m-1\) edges in total, so exactly \(m-1\) triples each contain two positive edges, and the final triple contains one. Each two-edge component identifies a whole triple; the last three unassigned vertices are consequently forced to make the final block. The version space after \(2m-1\) answers has exactly one partition. It cannot realize both answers at the next internal query, a contradiction. Therefore \(\operatorname{Ldim}\le2m-1\).

**4. A strongly shattered support with \(2m-2\) queries.** Again divide \(V\) into \(m\) triples. Query two consecutive edges of a three-vertex path in each of \(m-2\) triples; in each of the remaining two triples query just one edge. Call the set \(S_1\). We show that each labeling of \(S_1\) is realized by **at least two** distinct triple partitions.

Keep every two-edge queried triple labeled \((1,1)\) as a fixed block. Represent each other two-edge queried triple by a pair and singleton as in step 2. Represent each single-edge queried triple by a pair and singleton too: if its queried edge is positive, use that edge as the pair; if negative, put one queried endpoint with the local unqueried vertex as the pair, making the other queried endpoint the singleton. In the negative case there are two choices for which endpoint joins the unqueried vertex. Let \(r\) be the number of represented pair–singleton units; the two single-edge queried triples ensure \(r\ge2\). Any derangement \(\sigma\) of the \(r\) units produces valid triple blocks \(P_j\cup\{s_{\sigma(j)}\}\), since every negative query separates the pair from its local singleton and every positive query stays inside its pair. If \(r\ge3\), the two distinct cyclic shifts by one unit in opposite directions are derangements and give two different partitions. If \(r=2\), no two-edge queried triple is broken. When both single-edge queries are positive, both the identity assignment and the swap of the two singletons are valid and different. Otherwise, choose either of the two pair orientations for one negative single-edge query, and in each case swap the two singletons: these give two distinct valid partitions. This proves the strong witness assertion for all labelings and every \(m\ge2\).

**5. The Littlestone lower bound.** Ask the \(2m-2\) queries in \(S_1\) in a fixed order, creating a complete depth-\(2m-2\) binary tree, which is realizable by step 4. At each leaf there are at least two different triple partitions agreeing on those answers. Distinct partitions disagree on at least one pair \(\{u,v\}\), necessarily outside \(S_1\). Append that pair as the final query at the leaf, with the two distinct partitions witnessing its opposite answers. The resulting complete tree has depth \(2m-1\). Together with step 3 this gives equality.

**6. Boundary.** For \(m=1\) there is only one triple partition of a three-element set, hence every pair query is constant positive and both dimensions vanish.

## Verification

The standalone, dependency-free file `CHECK.py` constructs all triple partitions by recursively placing the least remaining vertex in a triple, computes their full pair-incidence masks, and tests all possibly shattered supports. It exhaustively examines every support contained in an all-positive hypothesis (a necessary condition for shattering), so it cannot omit a shattered support. It independently computes Littlestone depths by a memoized exact binary-tree feasibility recursion and tests the multiplicity of traces on \(S_1\). Run with `python3 CHECK.py`; successful execution prints `TRIPLE_BLOCK_SHATTERING_AND_ONLINE_PASS`.

Exact checked support counts, by support size starting at zero: for \(m=1\), \((1)\); for \(m=2\), \((1,15,105)\); for \(m=3\), \((1,36,630,5040,18900)\), with all later coefficients zero in each case. Independently computed Littlestone dimensions for \(m=2,3\) are \(3,5\). On the strong witness support \(S_1\), the smallest number of realizing partitions per labeling is two for \(m=2,3,4\); the \(m=4\) test is only a strong-support trace test, not a full-support enumeration.

The finite computations are checks, not substitutes for the proof for arbitrary \(m\).

## Relationship to prior work

Bressan, Cesa-Bianchi, Paudice and Vitale (2019), Theorem 6, showed that **all** set partitions of \(n\) vertices, queried by pairwise co-membership, have VC dimension \(n-1\). Their unrestricted class permits arbitrary block sizes. Its forest witness argument does not produce the dimensions here: requiring every block to have size exactly three changes the static dimension to \(2m-2\), and the online dimension is different again. Liu and Mukherjee (first version 2021; COLT 2022) study the worst-case number of same-component membership queries needed to **identify** a partition into a specified number of components, not the worst-case online mistake dimension of uniform triple partitions. Guingona, Kolesnikov, Nierwinski and Soucy (2021) establish VC/Littlestone equality for vector-space zero-set classes, whose assumptions do not include the triple-partition concept class. These comparisons do not assert exhaustive historical priority; related cluster-learning literature may use other terms.

## Limitations

The formulas are restricted to equal-sized three-element blocks. They do not establish dimensions for block size four or for general prescribed block sizes. The work does not assert the exact full shattered-support enumerator for all \(m\), nor an identification-query complexity bound. The available originality evidence is a best-knowledge literature and database comparison rather than an independent priority certification. Independent formal or expert proof verification has not been performed.

## References

1. M. Bressan, N. Cesa-Bianchi, A. Paudice, F. Vitale, *Correlation Clustering with Adaptive Similarity Queries*, arXiv:1905.11902, first posted 2019-05-28, especially Section 5, Theorem 6. https://arxiv.org/abs/1905.11902
2. X. Liu, S. Mukherjee, *Tight query complexity bounds for learning graph partitions*, arXiv:2112.07897, first posted 2021-12-15; Proceedings of COLT (2022), pp. 167–181, Sections 1–2. https://proceedings.mlr.press/v178/liu22a.html
3. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first posted 2021-09-10. https://arxiv.org/abs/2109.04805
