# Sharp greedy-PAV score spectrum on cyclic two-approval elections

## Finding

For every integer \(n\ge3\), consider an election with candidates \(c_i\) and unit-weight voters \(v_i\), indexed cyclically by \(i\in\mathbb Z/n\mathbb Z\), where voter \(v_i\) approves exactly \(\{c_{i-1},c_i\}\). For every committee cardinality \(1\le k\le n\), let \(\mathcal G_{n,k}\) comprise all committees obtainable by sequential (greedy) proportional approval voting, retaining **every** possible tie resolution. Let the harmonic PAV score be \(F(W)=\sum_i H_{|W\cap\{c_{i-1},c_i\}|}\), where \(H_0=0\), \(H_1=1\), and \(H_2=3/2\).

Put
\[
 c=\lceil n/3\rceil,\qquad q=\min\{k,n-k\},\qquad J_{n,k}=\max\{0,q-c\},\qquad F^*_{n,k}=2k-\tfrac12\max\{0,2k-n\}.
\]
Then \(F^*_{n,k}\) is the unrestricted optimal PAV score, and the **complete set of greedy-PAV score values** is
\[
 \boxed{\{F(W):W\in\mathcal G_{n,k}\}=\{F^*_{n,k}-j/2: j=0,1,\ldots,J_{n,k}\}.}
\]
In particular every tie resolution satisfies
\[
 \boxed{F(W)\ge\tfrac{11}{12}F^*_{n,k}},
\]
with equality possible **if and only if** \(n\) is a positive multiple of six and \(k=n/2\), under a suitable tie resolution. At \(n=6\), \(k=3\), the optimal and worst-greedy scores are respectively \(6\) and \(11/2\). For \(n=3,4,5,7\), all greedy committees at all sizes are PAV-optimal.

## Assumptions and scope

All \(n\) voters have unit weight and every voter approves exactly the two incident candidates on the cycle. The approval incidence is precisely a cycle; no additional approvals, voters, or candidates are allowed. The committee size \(k\) is prescribed, and sequential PAV repeatedly adds a candidate with the largest increase in the *same* harmonic PAV objective. The theorem concerns the set of possible scores across all internal tie resolutions, not a fixed deterministic tie-breaking rule. Every displayed equality uses literal cyclic adjacency, with the case \(n=3\) the ordinary triangle. The original optimization has no constraints beyond committee cardinality.

## Proof

**1. The score is controlled by adjacent selected pairs.** Let \(A(W)\) be the number of rim edges \(\{c_i,c_{i+1}\}\) whose two endpoints belong to \(W\). Each selected candidate contributes once to each of two approving voters, so the sum of approval counts is \(2|W|\). A voter approving two selected candidates contributes \(3/2\), rather than the \(2\) counted in that sum. Consequently
\[
 F(W)=2|W|-\frac{A(W)}2.\tag{1}
\]
At size \(k\), every one of the \(n-k\) unselected vertices can break at most one run of selected vertices. Equivalently, every selected vertex has two cyclic edges and at least \(2k-n\) edges must have both endpoints selected, hence
\[
 A(W)\ge\max\{0,2k-n\}.\tag{2}
\]
For \(k\le\lfloor n/2\rfloor\), an independent subset of \(k\) cycle vertices achieves zero. For larger \(k\), select the complement of an independent subset of \(n-k\) vertices; every unselected vertex then destroys exactly two edges, giving \(A(W)=2k-n\). Thus equality in (2) is attained and (1) proves the formula for \(F^*_{n,k}\).

**2. Greedy first completes a maximal independent set.** At a partial committee \(W\), adding an unselected \(c_i\) changes \(A(W)\) by the number \(d_W(i)\in\{0,1,2\}\) of its two selected cyclic neighbors. Equation (1) gives the exact marginal
\[
 F(W\cup\{c_i\})-F(W)=2-\frac{d_W(i)}2.\tag{3}
\]
While an unselected candidate has no selected neighbor, all greedy choices have zero selected neighbors. Hence the initially selected candidates form an independent set; this phase ends at some *maximal* independent set \(M\) of size \(m\). Conversely, each maximal independent set \(M\) can be reached by choosing its elements in any order, since all have marginal \(2\) until \(M\) is complete.

For a maximal independent set on a cycle, every gap between consecutive chosen vertices contains **one or two** unchosen vertices. If \(x\) of its \(m\) gaps contain two vertices, then \(n=2m+x\) with \(0\le x\le m\). Therefore
\[
 \lceil n/3\rceil\le m\le\lfloor n/2\rfloor.\tag{4}
\]
Conversely for every integer \(m\) in (4), set \(x=n-2m\); a cyclic concatenation of \(x\) gaps of length two and \(m-x\) gaps of length one produces such a maximal independent set. Therefore **every** \(m\) in (4) occurs in some tie branch.

**3. The greedy marginal sequence is completely determined by \(m\).** At the end of the independent phase, each length-two gap contains two adjacent unchosen candidates, each with exactly one selected neighbor; the length-one gaps contain candidates with two selected neighbors. Equation (3) forces a one-neighbor choice whenever any length-two gap remains. Choosing either member of such a gap makes the other member have two selected neighbors. Thus there are exactly \(x=n-2m\) successive additions with adjacency increment \(1\). All final \(m\) additions have increment \(2\). The total selected-adjacency count after \(k\) steps, including the early independent phase, is
\[
 A_g(k;m)=\begin{cases}
 0,&k\le m,\\
 k-m,&m\le k\le n-m,\\
 2k-n,&n-m\le k\le n.
 \end{cases}\tag{5}
\]
The formulas agree at their shared boundaries. Comparing (5) with (2) yields, in every case,
\[
 A_g(k;m)-\max\{0,2k-n\}=\max\{0,\min(k,n-k)-m\}.\tag{6}
\]
Inserting (6) into (1) shows that the loss in PAV score for a completed maximal independent set of size \(m\) is precisely \(\tfrac12\max\{0,q-m\}\). Every integer \(m\) allowed by (4) is realizable, so the losses are exactly \(j/2\) for every integer \(0\le j\le\max\{0,q-\lceil n/3\rceil\}\). This proves the full spectrum rather than only its endpoints.

**4. The sharp approximation ratio.** The least score has ratio
\[
 \frac{F_{\min}}{F^*}=1-\frac{J_{n,k}}{4k-\max\{0,2k-n\}}.\tag{7}
\]
If \(k\le n/2\), then \(J_{n,k}\le\max\{0,k-n/3\}\) and the fraction in (7) is at most \(1/12\). If \(k\ge n/2\), the fraction equals \(\max\{0,n-k-\lceil n/3\rceil\}/(2k+n)\), a decreasing function of \(k\) wherever positive; its value is bounded by the balanced-point estimate \((n/2-n/3)/(2n)=1/12\). Equality requires \(k=n/2\) and \(\lceil n/3\rceil=n/3\); together with integrality of \(k\), this holds exactly when \(6\mid n\). Construct a maximal independent set of size \(n/3\) by taking every third candidate and complete greedy through \(k=n/2\), attaining the asserted equality. At \(n=6,k=3\), the worst adjacency count is one, giving score \(11/2\) versus the optimal \(6\). Finally, for \(n\in\{3,4,5,7\}\), \(\lceil n/3\rceil=\lfloor n/2\rfloor\), so \(J_{n,k}=0\) for every \(k\).

## Verification

A standalone standard-library enumerator, `verify_cycle_pav.py`, computes harmonic PAV scores from each voter's actual approval count, independently evaluates selected cycle adjacencies, retains all maximizing tie branches at every greedy step, and enumerates every size-\(k\) committee for the true optimum. Its complete execution across \(3\le n\le15\) passed all assertions, including the **entire** predicted score spectrum, the correct values of possible maximal independent-set sizes and the sharp six-cycle witness. It assessed \(9766\) reachable committee states. Run `python verify_cycle_pav.py`. These exhaustive finite experiments are checks, **not** the proof of the result for arbitrary \(n\), which is supplied in the previous section.

## Relationship to prior work

Janeczko and Faliszewski (2023) define Greedy Thiele and its tie-rich outcomes, and explicitly use graph-edge candidates with endpoint-voter approvals in their hardness construction; these **objects and initial matching-style mechanism are prior art**, not asserted new here. Their published theorems treat the computational complexity of counting outcomes rather than the exact range of achieved welfare on cycle-incidence elections. Masařík, Pierczyński and Skowron (2023) supply further general PAV characterization. Lassota and Sornat (2026) show how to optimize Thiele rules when each candidate has at most two approvers, a general condition also true here; that computational optimization result does not assert that **sequential greedy** obtains the complete score interval above or give its sharp ratio. Classical independent domination gives the minimal size \(\lceil n/3\rceil\) of a maximal independent set on a cycle; the present application and exact all-ties PAV welfare comparison are the assessed contribution. General greedy-submodular guarantees are weaker and do not yield this exact tie spectrum.

## Limitations

The score spectrum and \(11/12\) sharp ratio hold only for this equal-weight cyclic two-approval incidence class and standard harmonic PAV. They need not hold under arbitrary voter approvals, unequal weights, a different Thiele scoring sequence or added committee constraints. The finding makes no assertion that an unindexed equivalent statement cannot exist; in particular, the connection to greedy maximal independent sets may have been formulated previously in equivalent graph-language. There has been no independent external mathematical audit.

## References

- P. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting*, arXiv:2305.01769v1 (first posted 2023-05-02). https://arxiv.org/abs/2305.01769 ; especially definitions and the graph-edge reduction in Theorem 4.3.
- T. Masařík, G. Pierczyński and P. Skowron, *A Generalised Theory of Proportionality in Collective Decision Making*, arXiv:2307.06077 (first posted 2023-07-12). https://arxiv.org/abs/2307.06077
- T. Lassota and K. Sornat, *Algorithms for Structured Elections under Thiele Voting Rules*, arXiv:2607.28575 (2026). https://arxiv.org/abs/2607.28575 ; theorem on candidates approved by at most two voters.
- E. Weisstein, *Independent Domination Number*, MathWorld. https://mathworld.wolfram.com/IndependentDominationNumber.html
