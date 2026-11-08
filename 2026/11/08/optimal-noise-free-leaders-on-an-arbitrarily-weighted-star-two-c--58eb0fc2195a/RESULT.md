# Optimal noise-free leaders on an arbitrarily weighted star: two candidate sets and a re-entrant hub

## Finding
Let a star have center \(0\), leaves \(1,\ldots,m\), where \(m\ge2\), and strictly positive edge conductances ordered as \(0<w_1\le\cdots\le w_m\). Let \(L\) be its weighted combinatorial Laplacian. For an exact budget of \(1\le k\le m+1\) noise-free leaders, define the unnormalized coherence cost
\[
C(S)=\operatorname{tr}\big((L_{F,F})^{-1}\big),\qquad F=\{0,1,\ldots,m\}\setminus S,
\]
with \(C(S)=0\) if \(F\) is empty. For \(1\le k\le m\), put
\[
P_k=\sum_{i=1}^{k}w_i,\quad
A_k=\sum_{i=k}^{m}\frac1{w_i},\quad
B_k=\sum_{i=k+1}^{m}\frac1{w_i}+\frac{m-k+1}{P_k}.
\]
Empty sums are zero. Then
\[
\boxed{\min_{|S|=k}C(S)=\min\{A_k,B_k\}.}
\]
The value \(A_k\) is attained by taking the center and the \(k-1\) leaves of smallest conductance; \(B_k\) is attained by taking the \(k\) leaves of smallest conductance and leaving the center a follower. In particular, the latter choice wins precisely when \(P_k>(m-k+1)w_k\), the former wins precisely when the inequality is reversed, and both are optimal at equality. For \(k=m+1\), the optimum is zero. Thus a single sort followed by prefix and suffix summation yields exact optimal sets and values **simultaneously at every budget** in \(O(m\log m)\) arithmetic operations/comparisons.

The optimal inclusion of the center need not be monotone in the leader budget. With \(m=8\) and conductances \((1,1,1,1,1,100,100,100)\), the center is absent from every optimal set at \(k=5\), present in every optimal set at \(k=6\), and absent again at \(k=7\). The respective exact optimal costs are \(83/100\), \(3/100\), and \(81/4100\).

## Assumptions and scope
All graphs are undirected weighted stars. Edge weights are positive conductances, not resistances. The center has index \(0\); ties in conductance may be broken arbitrarily when naming the first \(k\) leaves. A leader is removed from the grounded Laplacian, and only followers contribute to the trace. The cost equals twice the total steady-state variance for unit independent follower white-noise intensity, under the usual Ornstein--Uhlenbeck normalization; no extra factor is included in \(C(S)\). The complexity counts exact real arithmetic and comparisons, not bit complexity of input decimals.

## Proof
**1. Center selected.** If \(0\in S\), the follower block is diagonal, with one diagonal entry \(w_i\) for each follower leaf. Consequently \(C(S)=\sum_{i\notin S,\,i\ge1}1/w_i\). For fixed budget \(k\), this is minimized by selecting the \(k-1\) leaves with the smallest conductances. Its minimum is \(A_k\).

**2. Center not selected.** Let \(S\subseteq\{1,\ldots,m\}\), \(|S|=k\), \(W=\sum_{i\in S}w_i>0\), and let \(U=\{1,\ldots,m\}\setminus S\). The grounded block on the center and follower leaves is the arrowhead matrix with center diagonal \(\sum_{i=1}^mw_i\), follower diagonals \(w_i\) and center--leaf entries \(-w_i\). Its Schur complement at the center, after eliminating the follower leaves, is exactly \(W\). Block inversion therefore gives center inverse diagonal \(1/W\) and follower-leaf inverse diagonals \(1/w_i+1/W\). Hence
\[
C(S)=\sum_{i\in U}\frac1{w_i}+\frac{m-k+1}{W}.\tag{1}
\]

**3. Dominance of smallest-conductance leaves.** The case \(k=1\) is immediate: selecting only leaf \(j\) costs \(\sum_{i\ne j}1/w_i+m/w_j\), exceeding the center-only cost \(\sum_i1/w_i\) by \((m-1)/w_j>0\). Assume \(2\le k\le m\). Suppose a leaf-only leader set \(S\) contains a leaf with conductance \(b\) while a nonleader leaf has strictly smaller conductance \(a<b\). Write \(s=\sum_{i\in S}w_i=b+t\), where \(t>0\), and \(c=m-k+1\). Replacing the selected leaf of conductance \(b\) by the center changes the cost by
\[
\Delta_{\mathrm{center}}=\frac1b-\frac cs.
\]
If \(s<cb\), this change is strictly negative. If \(s\ge cb\), instead replace the selected leaf of conductance \(b\) by the unselected leaf of conductance \(a\). Formula (1) shows that this changes the cost by
\[
\Delta_{\mathrm{swap}}=(b-a)\left(\frac{c}{s(t+a)}-\frac1{ab}\right)<0,
\]
because \(c/s\le1/b\), while \(t+a>a\). Thus every leaf-only set containing a strictly larger selected conductance than an unselected one is strictly dominated by some feasible leader set of the same budget. It follows that whenever some global optimum excludes the center, an optimum is obtained from the \(k\) smallest leaf conductances, with only harmless tie freedom. Formula (1) then gives \(B_k\). The center-selected case and leaf-only case exhaust all possibilities.

**4. Threshold, complexity and nonmonotonicity.** Direct subtraction gives \(A_k-B_k=1/w_k-(m-k+1)/P_k\). Since all quantities are positive, the sign is precisely the sign of \(P_k-(m-k+1)w_k\), establishing the stated rule, including ties. All \(A_k,B_k\) are produced from one sorted array, its conductance prefixes and reciprocal-conductance suffixes. For the claimed eight-leaf example, the comparisons are \(P_5=5>4w_5=4\), \(P_6=105<3w_6=300\), and \(P_7=205>2w_7=200\), and substitution gives the three stated rational costs. These inequalities are strict, so the center's inclusion status is forced at each of those three budgets.

## Verification
Run `python3 verify.py` with the standard Python library. The script exactly enumerates all leader subsets for \(m=2,\ldots,9\) on reproducibly selected positive rational conductances (including ties), compares each exhaustive minimum with the two-candidate formula, and independently computes grounded-matrix inverse traces by fraction-valued Gauss--Jordan elimination. It also checks the three strict budget comparisons and rational values in the eight-leaf example. A successful replay prints `VERIFY_OK`, followed by counts of 1,248 exhaustive minima, 4,992 matrix identities and 1,056 budget-threshold checks. This finite replay is not the proof of the general result; the arbitrary-weight proof is above.

## Relationship to prior work
Lin, Fardad and Jovanovic (arXiv:1302.0450) formulate the grounded-Laplacian leader-placement problem and develop SDP relaxations and approximation methods for general networks. Fitch and Leonard (arXiv:1407.1569) give the general joint-centrality framework and exact cases for paths/cycles and small leader budgets. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) provide exact algorithms for arbitrary weighted paths and rings. Patterson, Yi and Zhang (arXiv:1708.06873, later supporting literature) provide resistance-based formulas and results on certain trees. These general tools permit evaluation of a fixed leader set but the inspected claims do not state the two-candidate optimum for *every* positive weighted star and budget, nor the re-entrant center example. The current result relies on a separate dominance argument that compares swaps with center replacement. No priority or uniqueness beyond inspected evidence is asserted.

## Limitations
The theorem applies only to a star with strictly positive edge conductances and exact-budget **noise-free** leaders. It does not optimize topology/edge weights or handle noise-corrupted leaders, heterogeneous follower-noise variances or general branching trees. Tied conductances may give multiple equivalent sets. Exact cost values depend on the chosen normalization of stochastic noise. A search of available literature and published-result records is not proof that no equivalent result exists; older graph-specific work may be missed. No independent mathematical audit has been performed.

## References
1. F. Lin, M. Fardad and M. R. Jovanovic, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, initial arXiv posting 2013-02-03, https://arxiv.org/abs/1302.0450.
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, initial arXiv posting 2014-07-07, https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, initial arXiv posting 2014-12-20, https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, initial arXiv posting 2017-08-23, https://arxiv.org/abs/1708.06873 (post-cutoff comparison only).
