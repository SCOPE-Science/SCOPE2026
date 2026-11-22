# Exact palette-run relaxation and first-entry distribution for cyclic contact dynamics on complete graphs

## Finding

Let \(q\ge4\) and \(n\ge2\) be integers. For synchronous \(q\)-color cyclic successor-contact dynamics on the labelled complete graph \(K_n\), let \(\tau(x)\) be the first nonnegative time at which the **complete vertex coloring** enters a temporal cycle. The following determine every individual clock, all finite-size clock populations, and the entire recurrent sector.

If all \(q\) colors are initially represented, then \(\tau(x)=0\) and the primitive period is exactly \(q\). Otherwise, arrange the occupied initial colors around their directed color circle, and let \(L(x)\) be the largest maximal run of consecutive occupied colors. Then
\[
\tau(x)=L(x)-1,
\]
and the resulting temporal period is one. Consequently \(\tau(x)\le q-2\); if \(n\ge q-1\), equality occurs for exactly
\[
q(q-1)!\,\left\{\begin{matrix}n\\q-1\end{matrix}\right\}
\]
labelled colorings, where the braces denote a Stirling number of the second kind. If \(n<q-1\) no coloring attains this bound. Exactly \(q!\left\{\begin{matrix}n\\q\end{matrix}\right\}\) colorings are on primitive \(q\)-cycles; thus they form \((q-1)!\left\{\begin{matrix}n\\q\end{matrix}\right\}\) different temporal cycles. All other states eventually become fixed.

For \(1\le r\le q-1\), define the \((r+1)\)-square polynomial matrix \(T_r(y)\) indexed by \(0,\ldots,r\) through the transitions
\[
(T_r(y))_{j,0}=1\ (0\le j\le r),\qquad
(T_r(y))_{j,j+1}=y\ (0\le j<r),
\]
with every other entry zero. Let \(A_{q,n}(t)=\#\{x:\tau(x)\le t\}\), with the natural one-vertex convention \(A_{q,1}(t)=q\) for the generating series. For each integer \(0\le t\le q-2\) and every \(n\ge2\), the exact exponential generating function is
\[
\boxed{\sum_{n\ge1}A_{q,n}(t)\frac{z^n}{n!}
=\operatorname{tr}\big(T_{t+1}(e^z-1)^q\big)
+(e^z-1)^q-1.}
\]
The minus one merely removes the empty zero-vertex assignment; it can be omitted when extracting positive-degree coefficients. The exact population of first-entry time \(t\) is \(A_{q,n}(t)-A_{q,n}(t-1)\), with \(A_{q,n}(-1)=0\).

For fixed \(q\), if the initial colors are independent and uniform and the initial palette is **not full**, then
\[
\Pr\big(\tau=q-2\mid \text{initial palette not full}\big)
=1-O_q\!\left(\left(\frac{q-2}{q-1}\right)^n\right)
\quad(n\to\infty).
\]
Thus the most delayed nonoscillatory relaxation becomes conditionally typical even though deficient palettes themselves are rare.

## Assumptions and scope

The color set is the directed cyclic palette \(\mathbb Z/q\mathbb Z\). At integer time \(s\), a vertex of color \(c\) advances to \(c+1\pmod q\) exactly when it has a **distinct** neighbor currently of successor color. All vertices update simultaneously. The graph is the ordinary simple complete graph; there are no loops, thresholds above one, or asynchronous updates. Initial vertex colorings are labelled assignments. A temporal cycle includes fixed points. A maximal occupied-color run is computed cyclically; the empty palette never arises when \(n\ge2\), and the full palette is treated separately rather than given a cyclic run length. The results apply to every integer pair \((q,n)\) in the stated domain, not only to experimentally tested small cases.

## Proof

**Support erosion.** Let \(S_s\subseteq\mathbb Z/q\mathbb Z\) be the occupied colors at time \(s\). A color \(c\) is occupied at time \(s+1\) precisely when \(c\in S_s\) and \(c+1\notin S_s\) (some sites stay at \(c\)), or \(c-1,c\in S_s\) (some sites of predecessor color advance to \(c\)). In particular, \(S_{s+1}\subseteq S_s\). If \(S_s\) is proper, every maximal occupied run \(\{a,a+1,\ldots,b\}\) becomes \(\{a+1,\ldots,b\}\) if it has length at least two, and becomes the same singleton \(\{b\}\) if it has length one. The key point is that the terminal color \(b\) has no successor present, so cannot disappear, while every nonterminal surviving color has a predecessor feeding it. Different runs remain disjoint and cannot merge.

After exactly \(L(x)-1\) updates, all occupied runs have become singletons; no successor pair remains, so no vertex can update again. At each earlier time some run has length at least two, and the support strictly shrinks, so the complete state cannot already be periodic. This proves the clock and fixed-sector formula. When \(S_0\) is the full palette, every vertex sees a successor color elsewhere and advances at each step. The color translation by one has order exactly \(q\) on any nonempty coloring, proving immediate primitive period \(q\).

**Sharp layer and recurrent orbits.** The only proper supports having longest run \(q-1\) are the \(q\) palettes missing exactly one color. For each, every color must be used, giving the surjection count \((q-1)!\left\{\begin{matrix}n\\q-1\end{matrix}\right\}\). A full palette contributes \(q!\left\{\begin{matrix}n\\q\end{matrix}\right\}\) assignments, partitioned into orbits of size \(q\). No proper-palette coloring with a consecutive occupied pair is recurrent because its occupied support shrinks strictly.

**Exact distribution.** Record a support subset as a length-\(q\) cyclic binary word, where one means occupied. Its maximal occupied run is at most \(r\) iff the unique cyclic progression of the trailing-one length belongs to state space \(\{0,\ldots,r\}\) and follows \(T_r\). Reading an absent color sends any state to zero, and reading an occupied color sends \(j\) to \(j+1\) with weight \(y\), forbidden if \(j=r\). A word containing at least one zero has exactly one consistent cyclic state labelling, so \(\operatorname{tr}(T_r(y)^q)\) counts all proper support subsets with occupied-color weight \(y\); the all-one support is excluded for \(r<q\). For any fixed subset of \(k\) chosen colors, the exponential generating function of assignments of labelled vertices **using every chosen color** is \((e^z-1)^k\). Substitute \(y=e^z-1\), then add the full-palette term \((e^z-1)^q\). Subtract the constant contribution of the empty palette. Since the first-entry time for a proper subset is its longest run minus one, this is exactly the claimed generating function. Differences recover individual layers.

**Conditional concentration.** For fixed \(q\), all deficient palettes together account for \(q(q-1)^n+O_q((q-2)^n)\) labelled assignments by inclusion-exclusion. Exactly-one-missing palettes, and hence maximal-delay assignments, number \(q(q-1)^n+O_q((q-2)^n)\). Their ratio gives the displayed conditional estimate.

## Verification

Two standalone Python 3 standard-library programs are included. `verify_direct.py` independently computes complete-state functional-graph first-entry times and primitive periods on all \(20\) pairs \(4\le q\le7\), \(2\le n\le6\), totaling \(218210\) initial colorings. It compares every state against the run-length prediction. `verify_transfer.py` compares every coefficient of the polynomial transfer with brute force cyclic support-subset enumeration for \(4\le q\le9\) and all cutoffs, then checks surjection identities for \(2\le n\le9\). Both programs completed without assertion failure; their full outputs are packaged. Such finite checks corroborate but do not replace the all-size proof above.

## Relationship to prior work

Fisch, Gravner and Griffeath (arXiv:patt-sol/9304001, first publicly deposited 1993-04-02) introduce general cyclic/contact excitable cellular automata and discuss spatially distributed wave phenomena; only the abstract and original HTML note were available for inspection here. Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, 2016-10-24), sections 1, 2 and 6.1, define the general contact rule, establish three-color results on arbitrary graphs, and explicitly distinguish the challenges for at least four colors; the inspected text does not provide the complete-graph all-color entry-time formula.

Related records include a three-color complete-graph threshold census, a four-color complete-bipartite census and an arbitrary-palette complete-bipartite missing-color wave. Their published summaries do not imply the present complete-graph, all-color first-entry generating function: increasing the number of colors and changing a complete bipartite graph to a complete graph changes the support dynamics. The claim is not that the color-erasure mechanism itself was previously unknown, but that this exact all-palette transient-time enumeration and conditional maximal-delay law are not covered by the inspected statements.

## Limitations

The result concerns a **complete** graph, synchronous successor contact with threshold one, and fixed \(q\) in the asymptotic statement; it does not extend automatically to sparse graphs, nonunit thresholds or asynchronous schedules. The 1993 full paper was inaccessible through its listed HTML/PDF links; a relevant omitted passage or unindexed article could affect historical priority. Accessible record summaries are not full-paper negative certificates. Finite verification is not independent peer review or a proof of uniqueness in the literature.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001v1 (public 1993-04-02), https://arxiv.org/abs/patt-sol/9304001.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public 2016-10-24), https://arxiv.org/html/1610.07320v1.
3. *Complete-graph cyclic dominance: exact orbit census and an arithmetic critical window*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-graph-cyclic-dominance-exact-orbit-census-and-an-arithm--01f472caead4.
4. *A six-cycle resonance and exact ten-class entrance law for four-color cyclic dynamics on complete bipartite graphs*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-six-cycle-resonance-and-exact-ten-class-entrance-law-for-four--c30756688b15.
