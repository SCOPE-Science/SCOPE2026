# Sharp clique bound and two-pencil structure in the two-read single-deletion graph

## Finding
Let \(q\ge 2\) and \(n\ge 2\). Define the two-read one-deletion reconstruction graph \(G_{q,n}\) on \(\Sigma_q^n\): two distinct length-\(n\) words are adjacent precisely when their sets of **distinct** one-deletion descendants have intersection of size two. Then
\[
\boxed{\omega(G_{q,n})=\lfloor n/2\rfloor+1.}
\]
There is also a complete local description of every clique. Fix an arbitrary vertex \(x\) in a clique \(K\). Each other vertex of \(K\) is obtained from \(x\) by switching the two alternating phases on a uniquely determined interval of length at least two. The resulting interval family is one of the following:

1. **One pencil.** All intervals share a left endpoint, or all share a right endpoint; distinct opposite endpoints are separated by at least two positions.
2. **Two adjacent pencils.** For some boundary between positions \(b\) and \(b+1\), every interval either ends at \(b\) or begins at \(b+1\). The base word has \(x_b=x_{b+1}\). All these intervals alternate between the same unordered pair of distinct symbols, and opposite endpoints in each pencil are separated by at least two positions.

Conversely, either specified pattern of actual alternating intervals produces a clique when the stated conditions hold. For clique size at most two the one-pencil description is understood in the evident degenerate sense. The statement holds for every alphabet size and does not assume a binary code.

## Assumptions and scope
Write \(D_1(x)=\{x_1\cdots x_{i-1}x_{i+1}\cdots x_n:1\le i\le n\}\), with duplicates discarded. An interval \(I=[a,b]\subseteq[1,n]\) is *alternating for \(x\)* if \(b-a+1\ge2\), and there are distinct \(u,v\in\Sigma_q\) for which \(x_a\cdots x_b=uvuv\cdots\). Define \(T_I(x)\) by replacing that substring with \(vuvu\cdots\), leaving every other coordinate unchanged. The length and all integer boundaries are literal. A clique means every two distinct vertices are adjacent, and its size counts words, not deletion occurrences.

We use the established Type-A characterization of two distinct common one-deletion descendants [1]: for distinct words \(x,y\), one has \(|D_1(x)\cap D_1(y)|=2\) exactly when \(y=T_I(x)\) for a unique alternating interval \(I\) of length at least two. Uniqueness holds because \(I\) is precisely the first-to-last differing interval.

## Proof
**Step 1 (two alternating intervals).** Fix \(x\), and let \(I,J\) be distinct alternating intervals for \(x\). We claim that \(T_I(x)\) and \(T_J(x)\) are adjacent exactly under either of the following conditions:

(a) \(I,J\) have the same left or same right endpoint, and their other endpoints differ by at least two; or

(b) they are disjoint and immediately consecutive, say \(I=[a,b]\) and \(J=[b+1,c]\), with \(x_b=x_{b+1}\) and the same unordered alternating symbol pair on both intervals.

To prove this, compare the two toggled words coordinate by coordinate. If \(I\) and \(J\) overlap in two or more positions, they use the same unordered pair of symbols, determined by any two consecutive overlap coordinates. In their overlap the toggles agree, while off the overlap exactly one toggles. Thus the difference set is the symmetric difference of the intervals. This is one interval only when the two intervals share an endpoint. In that case its length is the difference of their opposite endpoints; the two resulting words alternate oppositely on this difference interval exactly when that length is at least two.

If \(I\) and \(J\) meet in precisely one position \(b\), their neighboring source symbols are \(u=x_{b-1}\), \(v=x_b\), and \(w=x_{b+1}\), with \(u\ne v\) and \(v\ne w\). If \(u=w\), the toggles agree at \(b\), leaving disjoint differing blocks on its two sides. If \(u\ne w\), the toggles differ throughout the union, but one toggled word has consecutive entries \(v,u,w\) in positions \(b-1,b,b+1\), which cannot alternate because \(v\ne w\). Hence such a pair cannot be adjacent.

If \(I,J\) are separated by at least one unused coordinate, their toggles differ in separated blocks, so adjacency is impossible. Finally, if they are disjoint and immediately consecutive, then the two toggles differ throughout \([a,c]\). Their restrictions are opposite alternating phases across the concatenated interval precisely when the source pair used on the left agrees with the source pair used on the right and \(x_b=x_{b+1}\): at the boundary the toggle changes only one of the two runs, making its two symbols alternate across the join. This proves the claim using the Type-A characterization.

**Step 2 (clique interval classification).** Fix \(x\in K\), and let \(\mathcal F\) be the distinct alternating intervals representing the other vertices. By Step 1 any pair of members of \(\mathcal F\) either shares an endpoint or consists of immediately adjacent disjoint intervals satisfying (b).

Suppose first that no intervals in \(\mathcal F\) are disjoint. View intervals as edges between their left endpoints and right endpoints in an abstract bipartite graph. Every two edges share a vertex; because its graph is bipartite, all edges of any family of size at least three share one vertex. (The same conclusion is immediate for one or two intervals.) Thus all intervals have a common left or right endpoint. By Step 1, all distinct free endpoints are separated by at least two. This is the one-pencil case.

Otherwise choose disjoint members \(I=[a,b]\) and \(J=[b+1,c]\). Their adjacency forces the common two-symbol alphabet and \(x_b=x_{b+1}\) by Step 1. Every third interval \(H\) must be adjacent in the sense of Step 1 to each of \(I,J\). If it meets both intervals, the shared-endpoint rule forces \(H=[a,c]\); that is not alternating for \(x\) because it contains adjacent equal source symbols at \(b,b+1\). If \(H\) meets only \(I\), adjacency with \(J\) forces it to end at \(b\), and similarly any interval meeting only \(J\) must begin at \(b+1\). An interval meeting neither cannot be adjacent to both. Therefore all members end at \(b\) or begin at \(b+1\), and their alternating pairs coincide because each contains the last or first two positions of \(I\) or \(J\). Pairwise adjacency inside each side enforces spacing at least two between free endpoints. This is the two-pencil case. Step 1 proves the converse for both patterns.

**Step 3 (sharp bound).** In a one-pencil family with fixed left endpoint \(a\), the right endpoints lie in \(\{a+1,\ldots,n\}\) with spacing at least two, giving at most \(\lceil(n-a)/2\rceil\le \lfloor n/2\rfloor\) intervals. The symmetric bound holds for a fixed right endpoint. In a two-pencil family at boundary \(b\), the left pencil has at most \(\lfloor b/2\rfloor\) intervals, and the right pencil at most \(\lfloor(n-b)/2\rfloor\). Their sum is at most \(\lfloor n/2\rfloor\). Including the chosen base vertex gives \(|K|\le\lfloor n/2\rfloor+1\).

For sharpness, take \(x=(0101\cdots)\in\Sigma_q^n\) using two symbols of the alphabet. For \(k=1,\ldots,\lfloor n/2\rfloor\), toggle the prefix \([1,2k]\). The resulting \(\lfloor n/2\rfloor\) words and \(x\) are all distinct. Any two of the toggled words differ precisely on an alternating interval of even length at least two, while every toggled word is adjacent to \(x\). These words form a clique of size \(\lfloor n/2\rfloor+1\), completing the proof.

## Verification
The accompanying `checker.py` independently constructs all distinct one-deletion descendant sets and joins words when exactly two distinct descendants are common. It separately constructs all alternating-interval edges and confirms the two edge sets agree; it exhaustively lists maximal cliques, verifies their sizes, and verifies the explicit extremal clique. The exact completed parameter ranges are binary \(2\le n\le9\), ternary \(2\le n\le6\), and four-symbol \(2\le n\le4\). A separate enumeration of every maximal clique relative to every root confirmed the one/two-pencil interval classification in all those ranges.

Run `python checker.py` after installing Python 3 and NetworkX (`pip install networkx`). These computations test finite cases only; the universal assertion follows from the interval proof above together with the published Type-A characterization.

## Relationship to prior work
Cai, Kiah, Nguyen, and Yaakobi [1] establish the Type-A pairwise criterion and construct two-read reconstruction codes. Chrisnata, Kiah, and Yaakobi [2, Section IV, Lemma 7] use families of binary cliques of size \(\ell\) on blocks of length \(2\ell\) to bound reconstruction-code redundancy. Their result gives lower constructions for certain cliques; it does not state the universal upper bound or the classification of all clique interval families established here. A published exact-edge-count calculation for this same graph characterizes each edge and computes its total number, but counting edges does not by itself determine the clique number or characterize arbitrary clique families [3]. Wang, Li, and Fu [4] study larger numbers of deletions and extremal ball intersections; the graph here uses exactly one deletion and simultaneous two-read ambiguity.

## Limitations
The result determines maximum clique size and an anchored local classification, not optimal independence numbers, clique-cover numbers, or a classification up to graph automorphism of maximum cliques. The theorem uses a previously established, independently published characterization of pairwise two-read confusability. Finite computation cannot substitute for the all-length argument. Independent review and exhaustive historical-priority certification are not claimed; differently indexed earlier equivalent clique work may exist.

## References
1. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (2020), https://arxiv.org/abs/2001.01376 .
2. J. Chrisnata, H. M. Kiah, and E. Yaakobi, *Correcting Deletions With Multiple Reads*, IEEE Transactions on Information Theory 68(11), 7141–7158 (2022), DOI: 10.1109/TIT.2022.3184868; https://yaakobi.net.technion.ac.il/files/2024/02/75_Multiple_Reads_Deletions_IT22.pdf .
3. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91 .
4. X. Wang, H. Li, and F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first posted September 15, 2026, https://arxiv.org/abs/2609.16837 .
