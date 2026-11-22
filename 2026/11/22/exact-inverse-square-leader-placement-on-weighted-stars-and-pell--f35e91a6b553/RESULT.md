# Exact inverse-square leader placement on weighted stars and Pell-type ties

## Finding
Let an undirected weighted star have hub \(0\), leaves \(1,\ldots,m\), \(m\ge2\), and strictly positive edge conductances ordered as \(0<w_1\le\cdots\le w_m\). Let \(L\) denote its weighted combinatorial Laplacian. For exactly \(1\le k\le m\) perfectly grounded leaders \(S\), with followers \(F=\{0,\ldots,m\}\setminus S\), minimize the **inverse-square grounded spectral trace**
\[
J_2(S)=\operatorname{tr}\!\left((L_{FF})^{-2}\right).
\]
Put
\[
P_k=\sum_{i=1}^{k}w_i,\qquad A_k=\sum_{i=k+1}^{m}\frac1{w_i},\qquad B_k=\sum_{i=k+1}^{m}\frac1{w_i^2},\qquad r=m-k.
\]
Then the exact global minimum is
\[
\boxed{\min_{|S|=k}J_2(S)=\min\left\{C_k,D_k\right\},\quad
C_k=B_k+\frac1{w_k^2},\quad
D_k=B_k+\frac{2A_k}{P_k}+\frac{(r+1)^2}{P_k^2}.}
\]
Every minimizing set has one of precisely two forms, allowing arbitrary tie-breaking among equal conductances:

* the hub together with the \(k-1\) weakest-conductance leaves, attaining \(C_k\);
* the \(k\) weakest-conductance leaves without the hub, attaining \(D_k\).

The hub-free choice is strictly better exactly when
\[
\boxed{P_k^2-2A_kw_k^2P_k-(r+1)^2w_k^2>0,}
\]
and the reverse strict inequality forces hub selection. Equality gives both types, and no other types. Sorting once and forming prefix/suffix sums computes exact optimal values and sets for every budget in \(O(m\log m)\) real-arithmetic comparisons/operations. For \(k=m+1\), grounding all vertices gives cost zero.

For unit conductances, the hub-free type is optimal if and only if
\[
2k^2+2k\ge m^2+2m+1.
\]
Strict inequality gives only hub-free sets; the reverse gives only hub-containing sets. Thus the switch occurs near \(k/m=1/\sqrt2\), rather than the approximately one-half leader budget for the corresponding inverse-first-power cost. Equal-cost ties occur for infinitely many exact integer pairs and **only** for
\[
\boxed{2k+1=u_j,\quad m+1=v_j,\quad u_j+v_j\sqrt2=(3+2\sqrt2)^j,\quad j\ge2.}
\]
The first ties are \((m,k)=(11,8),(69,49),(407,288)\).

## Assumptions and scope
The weights are arbitrary finite positive conductances; no normalization, equal-weight restriction or bounded ratio is imposed. The grounded Laplacian \(L_{FF}\) is the principal submatrix retaining follower vertices and original weighted degrees; it is positive definite whenever at least one leader is selected. The objective is the unnormalized sum of the squares of the reciprocals of its eigenvalues. Multiplicative noise-model conventions do not alter optimal sets. Leaders are perfectly grounded, not finite-gain or noise-corrupted. Ties in sorted conductances permit relabeling among equal-weight leaves. Complexity refers to exact real arithmetic, not bit complexity. The empty follower matrix has objective zero.

## Proof
**1. Leader set containing the hub.** If \(0\in S\), the follower Laplacian is diagonal with entries \(w_i\) for ungrounded leaves. Hence \(J_2(S)=\sum_{i\in F}w_i^{-2}\), minimized precisely by grounding \(k-1\) weakest leaves in addition to the hub. Its value is \(C_k\).

**2. Leader set without the hub.** Let \(S\) consist of \(k\) leaves, and write \(U\) for the remaining \(r=m-k\) leaves, \(W=\sum_{i\in S}w_i>0\). With the hub listed first, the follower Laplacian is an arrowhead matrix. Eliminating its leaf block gives hub Schur complement exactly \(W\), so direct block inversion yields
\[
(L_{FF})^{-1}=\operatorname{diag}\left(0,\left\{\frac1{w_i}\right\}_{i\in U}\right)+\frac1W\mathbf1_{r+1}\mathbf1_{r+1}^{\mathsf T}.
\]
Squaring and tracing, including \(r=0\), gives the exact identity
\[
\boxed{J_2(S)=\sum_{i\in U}\frac1{w_i^2}+\frac2W\sum_{i\in U}\frac1{w_i}+\frac{(r+1)^2}{W^2}.}\tag{1}
\]

**3. A strict two-action dominance lemma.** Suppose \(1\le k<m\), a hub-free leader set \(S\) includes a leaf of conductance \(b\) while an ungrounded leaf has smaller conductance \(a<b\). Choose \(a\) to be the smallest ungrounded conductance and \(b\) the largest selected one. Put \(r=m-k\ge1\), \(W=b+t\), and \(c=r+1\). If \(W\le cb\), replace the selected leaf of weight \(b\) by the hub. The previously ungrounded leaves stay ungrounded and the \(b\)-leaf becomes an additional follower. The new cost is \(\sum_{i\in U}w_i^{-2}+b^{-2}\), strictly below the old cost in (1), because \(c^2/W^2\ge b^{-2}\) and the remaining reciprocal-sum term in (1) is positive.

Otherwise \(t>rb\). Let \(A_0=\sum_{i\in U\setminus\{a\}}w_i^{-1}\le(r-1)/a\). Swap the selected \(b\)-leaf for the unselected \(a\)-leaf. Writing \(\Delta\) for new minus old inverse-square trace, exact subtraction from (1) gives
\[
\frac{\Delta}{b-a}=-\frac{a+b}{a^2b^2}
+\frac{2(A_0-t/(ab))}{(t+a)(t+b)}
+\frac{c^2(2t+a+b)}{(t+a)^2(t+b)^2}.\tag{2}
\]
The middle term is strictly negative because \(A_0\le(r-1)/a<t/(ab)\). Moreover \(t+b>(r+1)b=cb\) and \(t+a>a+b\), so the last positive term is strictly smaller than
\[
\frac1{b^2}\left(\frac2{a+b}+\frac{b-a}{(a+b)^2}\right)
=\frac{a+3b}{b^2(a+b)^2}
<\frac{a+b}{a^2b^2}.
\]
The last strict inequality follows by multiplying through by the positive denominators: \((a+b)^3-a^2(a+3b)=3ab^2+b^3>0\). Therefore \(\Delta<0\). In both cases \(S\) has a strictly better feasible alternative.

For \(k=1\), (1) shows that grounding a leaf \(j\) costs \(\sum_{i\ne j}w_i^{-2}+2w_j^{-1}\sum_{i\ne j}w_i^{-1}+m^2w_j^{-2}\), exceeding grounding the hub by the strictly positive amount \(2w_j^{-1}\sum_{i\ne j}w_i^{-1}+(m^2-1)w_j^{-2}\). For \(k=m\), the hub-free set is necessarily all leaves. Thus every optimal hub-free set for any \(k\) consists of the \(k\) weakest conductances, up to ties: otherwise the lemma gives a strict improvement. Formula (1) at this set is \(D_k\), proving the global two-candidate theorem. No unexamined symmetry or relaxation assumption was used.

**4. Threshold, complexity, and integer ties.** Subtracting the candidates gives \(C_k-D_k=w_k^{-2}-2A_k/P_k-c^2/P_k^2\), whose sign is exactly that of the boxed polynomial after multiplying by the positive quantity \(w_k^2P_k^2\). Prefix sums of the \(w_i\) and suffix sums of \(w_i^{-1}\) and \(w_i^{-2}\) yield both candidates for all budgets after one sort.

For unit weights \(P_k=k\), \(A_k=m-k=r\), \(B_k=r\), hence \(C_k=r+1\) and \(D_k=r+2r/k+(r+1)^2/k^2\). Their comparison reduces exactly to \(2k^2+2k\gtreqless m^2+2m+1\). The equality becomes \((2k+1)^2-2(m+1)^2=1\). Every positive integral solution of the Pell equation \(u^2-2v^2=1\) is given by \(u+v\sqrt2=(3+2\sqrt2)^j\), \(j\ge1\), by the standard fundamental-unit descent (multiplying by \(3-2\sqrt2\) reduces any solution beyond the least positive one). The \(j=1\) solution has \(m=1\), excluded here, leaving exactly \(j\ge2\). Finally, the real switching budget solves \(k=(\sqrt{2m^2+4m+3}-1)/2\), so its ratio to \(m\) tends to \(1/\sqrt2\).

## Verification
The included `verify.py` is a standalone standard-library exact-rational checker. It constructs actual grounded Laplacians for every tested leader set, inverts them using fraction-valued Gauss–Jordan elimination, compares the inverse-square trace to the arrowhead formula, enumerates all \(k\)-subsets, and compares global minima to the two-candidate expression. It tests unit, strictly ordered, tied, and reproducible heterogeneous rational conductances for \(2\le m\le8\), as well as the integer threshold for \(2\le m<100\). Run `python3 verify.py`; successful output is `VERIFY_OK` with 9,018 exact direct-matrix comparisons, 315 enumerated optimality checks, and 4,949 threshold checks. These are finite diagnostics; the unrestricted theorem is proved by the inequalities above, not by enumeration.

For a concrete separation of objectives, take six unit-weight spokes and four leaders. The inverse-square cost is \(3\) with the hub plus three leaves and \(57/16\) with four leaves, so the former is strictly optimal. For the inverse-first-power cost, these two values are respectively \(3\) and \(11/4\), so four leaves are strictly optimal. This difference is not a normalization effect.

## Relationship to prior work
The grounded-Laplacian leader-selection formulation and the first inverse trace appear in Patterson and Bamieh (2010), Lin–Fardad–Jovanović (arXiv:1302.0450), Fitch–Leonard (arXiv:1407.1569), and Patterson–McGlohon–Dyagilev (arXiv:1412.6595). The first-order result on arbitrarily weighted stars, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-noise-free-leaders-on-an-arbitrarily-weighted-star-two-c--58eb0fc2195a, establishes a different objective and the linear budget threshold \(P_k>(m-k+1)w_k\). Neither its proof nor its threshold implies the inverse-square optimum. The relevant published second-order weighted-star conductance-budget result (https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-scale-price-crossover-for-optimal-second-order-coherence-on--4153ea5f5a8d) optimizes edge conductances, not leader vertices. Prior second-order graph coherence papers generally evaluate fixed graph spectra. The present claim concerns an exact **binary leader-placement** classification, its quadratic threshold, and rare Pell ties. Published-source searches and manuscript inspections identify no result covering this specific combination, but search incompleteness and unindexed equivalent theorems remain risks.

## Limitations
All edges must form a star; the weights are fixed, positive, and undirected. Leaders must be perfectly pinned, and the objective is specifically the squared inverse of the grounded Laplacian. There is no claim for general graphs, inverse powers other than two, finite leader gains, heterogeneous noise intensities, or budget-dependent edge reweighting. The positive-weight exact-real operation bound is not a floating-point stability or bit-complexity guarantee. The model uses an unnormalized trace; physical second-order noise conventions may multiply it by a constant. No independent mathematical audit has been performed. Exhaustive computations on finitely many examples cannot independently certify the theorem over all real weights.

## References
1. S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, Proceedings of the IEEE CDC (2010), https://webee.technion.ac.il/Sites/People/stacyp/papers/patterson_cdc10_leader.pdf.
2. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, first arXiv posting 2013-02-03, https://arxiv.org/abs/1302.0450.
3. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, first arXiv posting 2014-07-07, https://arxiv.org/abs/1407.1569.
4. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, first arXiv posting 2014-12-20, https://arxiv.org/abs/1412.6595.
5. *Optimal noise-free leaders on an arbitrarily weighted star: two candidate sets and a re-entrant hub*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-noise-free-leaders-on-an-arbitrarily-weighted-star-two-c--58eb0fc2195a.
