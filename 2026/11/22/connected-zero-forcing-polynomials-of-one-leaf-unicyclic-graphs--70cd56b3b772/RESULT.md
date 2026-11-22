# Connected zero-forcing polynomials of one-leaf unicyclic graphs

## Finding

Let \(T_{c,t}\) be the finite simple graph consisting of a cycle of length \(c\ge3\), with a path of \(t\ge1\) additional vertices attached at one cycle vertex. Every connected unicyclic graph with exactly one degree-one vertex is isomorphic to one such \(T_{c,t}\). Write
\[
Z_C(T_{c,t};z)=\sum_{S\subseteq V(T_{c,t})\atop T_{c,t}[S]\text{ connected and }S\text{ zero forcing}}z^{|S|}.
\]
Then the complete connected zero-forcing polynomial is
\[
\boxed{Z_C(T_{c,t};z)=\sum_{q=2}^{c-1}z^q\left(c-q+q\sum_{j=0}^{t}z^j\right)+z^c\sum_{j=0}^{t}z^j.}
\]
Its nonzero coefficient sequence, in increasing degree, is always unimodal. More sharply, it is log-concave **if and only if** \(t=1\) or \(c\in\{3,4\}\). In every remaining case, log-concavity already fails at the second nonzero coefficient:
\[
[z^2]Z_C=c,\quad [z^3]Z_C=c+2,\quad [z^4]Z_C=c+5,
\qquad (c+2)^2-c(c+5)=4-c<0
\]
for \(c\ge5\) and \(t\ge2\).

The smallest connected forcing sets have size two and there are exactly \(c\) of them. The total number of connected forcing sets is
\[
Z_C(T_{c,t};1)=\binom{c-1}{2}+(t+1)\binom c2.
\]

## Assumptions and scope

All graphs are finite, undirected, and simple. Initially selected vertices are blue; a blue vertex with exactly one white neighbor may turn that neighbor blue. A set is *zero forcing* if some sequence of such forces colors every vertex. It is *connected* if the induced graph on the initial set is connected. Empty sets are not counted.

For \(T_{c,t}\), label cycle vertices \(v_0,v_1,\ldots,v_{c-1}\) in cyclic order, with the pendant path \(v_0,w_1,\ldots,w_t\). A *cycle interval* is a cyclically consecutive collection of cycle vertices, with a full cycle treated as one interval. A *tail prefix* is \(\{w_1,\ldots,w_j\}\), for \(0\le j\le t\). The exponent of \(z\) counts vertices, not forcing moves. The empty polynomial coefficients below degree two are omitted when discussing unimodality and log-concavity.

## Proof

**One-leaf classification.** Remove the cycle edges of a connected unicyclic graph. The remaining components are trees rooted at cycle vertices. Every nontrivial rooted component contains at least one graph leaf away from the cycle. Thus a graph with exactly one leaf has exactly one nontrivial attached component; that rooted tree must be a path, for any branching would produce at least two leaves. Hence the family above exhausts the stipulated one-leaf unicyclic graphs.

**Necessary initial-set shape.** Suppose a connected initial set \(S\) has no cycle vertex. Its forces can reach the attachment vertex at most, after which two white cycle neighbors prevent any force into the cycle. If \(S\) contains just one cycle vertex, connectivity excludes tail vertices unless that vertex is \(v_0\), and in either case the two directions around the otherwise white cycle cannot be started. Hence \(S\) must contain at least two cycle vertices. As \(S\) induces a connected subgraph and the tail is attached at only \(v_0\), the cycle vertices of \(S\) form a nonempty consecutive cycle interval of size \(q\ge2\); if not the whole cycle, the complement is a single unselected cycle interval. Any selected tail vertices necessarily form a prefix, and a nonempty prefix is possible only if \(v_0\in S\).

**Sufficiency of every listed shape.** For a proper cycle interval containing \(v_0\), choose a blue boundary vertex different from \(v_0\) and force successively along the unselected cycle arc; each forcing vertex away from the hub has only one white neighbor. Once the cycle is blue, \(v_0\) forces the unselected suffix of the pendant path. For an interval avoiding \(v_0\), propagate from both ends through the unselected cycle arc, stopping when \(v_0\) is the sole white cycle vertex; one blue cycle neighbor then forces \(v_0\), which can force the tail. If the full cycle is initially blue, the unselected tail suffix is forced directly. Thus every connected set with the classified shape is zero forcing, irrespective of the chosen tail-prefix length.

**Counting.** For each \(2\le q<c\) there are exactly \(c\) labelled cyclic intervals of size \(q\). Exactly \(q\) contain \(v_0\), allowing each of \(t+1\) tail prefixes, and exactly \(c-q\) avoid \(v_0\), allowing only the empty prefix. The full cycle contributes one configuration per tail-prefix size. Summing their monomials proves the stated polynomial. The degree-two coefficient is \(c\), since its sets are the \(c\) cycle edges. Setting \(z=1\) yields the total count.

**Unimodality.** Define \(a_k=[z^k]Z_C\), extend coefficients by zero outside their support, and put \(b_q=q\) for \(2\le q<c\), \(b_c=1\), and \(b_q=0\) otherwise. Directly from the polynomial,
\[
a_k=(c-k)\mathbf1_{\{2\le k<c\}}+\sum_{j=0}^{t}b_{k-j}.
\]
For \(2\le k\le c-2\), subtraction gives
\[
a_{k+1}-a_k=k-b_{k-t}>0
\]
because \(t\ge1\) and \(b_{k-t}\le k-1\). At \(k=c-1\), the difference is \(-b_{c-1-t}\le0\); for every \(k\ge c\) before the last nonzero coefficient, it is \(-b_{k-t}\le0\). Therefore the nonzero coefficients first strictly increase (possibly through an empty range) and then weakly decrease.

**Sharp log-concavity.** For \(c\ge5\), \(t\ge2\), the first three coefficients are \(c,c+2,c+5\); the displayed strict negative determinant proves non-log-concavity. Conversely, for \(c=3\) the coefficient string is \(3\), repeated \(t+1\) times, followed by \(1\). For \(c=4\) it is \(4\), followed by \(t\) copies of \(6\), then \(4,1\). Both strings satisfy the adjacent log-concavity inequalities. Finally, if \(t=1\) and \(c\ge5\), the sequence is
\[
 c,\ c+2,\ c+3,\ \ldots,\ 2c-2,\ c,\ 1.
\]
The central arithmetic progression has log-concavity differences one; its first boundary difference is \(c+4>0\), and the final two boundary inequalities are immediate from \(c\ge5\). These cases exhaust the conditions.

## Verification

The standalone `VERIFY.py` enumerates every initial vertex subset of \(T_{c,t}\) independently of the structural classification. It checks connectivity by graph traversal and zero forcing by repeatedly applying the original local color-change rule. For all 34 instances with \(3\le c\le9\), \(1\le t\le5\), and \(c+t\le13\), the observed coefficient dictionary equals the proposed polynomial; this covers 46,608 examined subsets. Additional exact arithmetic checks cover all 1,680 parameter pairs with \(3\le c\le50\) and \(1\le t\le35\), confirming the total count and both coefficient-shape statements. Run `python VERIFY.py` with standard Python 3.9 or later; the expected final line is `VERIFY_OK`. The unrestricted statements are established by the proof, not by finite computation.

For example, \(T_{5,2}\) has
\[
Z_C(T_{5,2};z)=5z^2+7z^3+10z^4+8z^5+5z^6+z^7,
\]
which is unimodal and not log-concave because \(7^2<5\cdot10\).

## Relationship to prior work

Mukherjee and Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985 (first posted November 7, 2026), compute connected forcing polynomials for trees and explicitly ask in Problem 5.2 for the unicyclic case. This theorem answers that question for the complete natural class of unicyclic graphs with exactly one pendant vertex. It does not solve the general unicyclic problem.

Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658 (July 3, 2016), establishes the connected forcing **number** of unicyclic graphs and an excluded-cycle-segment lemma. Those facts are consistent with and motivate the classification above, but they do not provide the all-cardinality polynomial or log-concavity boundary.

Newton and Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352 (November 8, 2026), demonstrate nonunimodality in general, including connected forcing. The present one-leaf unicyclic family exhibits a different phenomenon: universal unimodality together with a precise threshold for failure of the stronger log-concavity property. Related previously indexed full-size enumerations for sunlet and wheel graphs concern different graph families; the available index summaries did not yield the formula above. Search-based historical priority remains provisional.

## Limitations

The formula is proved only for simple connected unicyclic graphs with exactly one degree-one vertex, equivalently one pendant path on one cycle. It is not asserted for a graph with several pendant branches, zero pendant vertices, or additional cycles. The criterion concerns the **nonzero** coefficient sequence; no claim of real-rootedness, uniform log-concavity for general unicyclic graphs, or a solution of the full unicyclic classification problem is made. Indexed and accessible published sources were compared but cannot exclude unindexed prior results. Independent mathematical validation has not been performed.

## References

1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985, first version November 7, 2026. https://arxiv.org/abs/2611.10985
2. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658v1, July 3, 2016. https://arxiv.org/html/1607.00658v1
3. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352, November 8, 2026. https://arxiv.org/abs/2611.11352
