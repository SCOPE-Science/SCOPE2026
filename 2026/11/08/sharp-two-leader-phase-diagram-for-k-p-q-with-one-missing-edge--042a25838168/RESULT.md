# Sharp two-leader phase diagram for \(K_{p,q}\) with one missing edge

## Finding
Let \(G_{p,q}\) be the unit-conductance complete bipartite graph on disjoint parts \(A=\{a_0,\ldots,a_{p-1}\}\), \(B=\{b_0,\ldots,b_{q-1}\}\), except the edge \(a_0b_0\) is removed. For all integers \(3\le p\le q\), select exactly two vertices \(S\) as noise-free leaders and put \(F=V\setminus S\), \(J(S)=\operatorname{tr}(L_{FF}^{-1})\), with \(L\) the unscaled combinatorial Laplacian.

**Complete optimizer classification:**

* If \(p=3\) and \(3\le q\le6\), or \((p,q)=(4,4)\) or \((5,5)\), the unique optimal pair is \(\{a_0,b_0\}\), the two nonadjacent endpoints of the deleted edge.
* For all other \(3\le p\le q\), the optimal pairs are precisely \(\{a_i,a_j\}\) with \(1\le i<j\le p-1\), and additionally the pairs \(\{b_i,b_j\}\) with \(1\le i<j\le q-1\) if \(p=q\ge6\).

The optimal-set counts are respectively \(1\), \(\binom{p-1}{2}\), and \(2\binom{p-1}{2}\). Define
\[
J_{\mathrm{def}}(p,q)=\frac{(p+q-2)(p^2+pq-p+q^2-q)}{pq(p+q-1)},
\]
\[
J_{\mathrm{ord}}(p,q)=\frac{3p^2+pq-6p+2q^2-2q}{2pq}+\frac{p^2+q^2-q}{pq(p-1)(q-1)}.
\]
The exact minimum is \(J_{\mathrm{def}}\) in the first regime and \(J_{\mathrm{ord}}\) in the second. All omitted alternatives are strictly worse. For example \(J_{\mathrm{def}}(3,6)=21/8\) is better than \(J_{\mathrm{ord}}(3,6)=79/30\), but at \((p,q)=(3,7)\) the best pair consists of the two ordinary vertices in the smaller part and has objective \(35/12\), strictly below \(184/63\) for the deleted-edge endpoints.

## Assumptions and scope
Graphs are undirected, simple, connected and unweighted. The deleted edge is the only missing bipartite edge. The budget is exactly two, the partition sizes satisfy \(3\le p\le q\), noise-free leader coordinates are removed from the dynamics, and no factor of \(1/2\) is included in \(J\). The statement is not about stochastic leaders, more than two leaders, or arbitrary deleted matchings.

## Proof
1. **Eight pair classes.** Write \(A^\circ=A\setminus\{a_0\}\), \(B^\circ=B\setminus\{b_0\}\). Every unordered two-leader set is equivalent under permutations of \(A^\circ\) and \(B^\circ\) to one of \(\{a_0,b_0\}\), \(\{a_0,a_i\}\), \(\{a_i,a_j\}\), \(\{b_0,b_i\}\), \(\{b_i,b_j\}\), \(\{a_0,b_i\}\), \(\{a_i,b_0\}\), \(\{a_i,b_j\}\), with indices positive and distinct where needed. All eight types exist when \(p,q\ge3\).

2. **Exact inverse under one edge deletion.** Suppose \(a\) leaders lie in \(A\), \(b=2-a\) in \(B\), and put \(s=p-a\), \(t=q-b\), \(\Delta=pq-st=aq+bp-ab>0\). For the undeleted biclique the grounded matrix \(M_0\) is invertible and
\[
 M_0^{-1}=\begin{pmatrix}
q^{-1}I_s+\frac{t}{q\Delta}\mathbf1_s\mathbf1_s^T&\Delta^{-1}\mathbf1_s\mathbf1_t^T\\
\Delta^{-1}\mathbf1_t\mathbf1_s^T&p^{-1}I_t+\frac{s}{p\Delta}\mathbf1_t\mathbf1_t^T
\end{pmatrix}.
\]
This follows by multiplication with \(M_0=\begin{psmallmatrix}qI_s&-\mathbf1_s\mathbf1_t^T\\-\mathbf1_t\mathbf1_s^T&pI_t\end{psmallmatrix}\). In particular, \(\operatorname{tr}M_0^{-1}=s/q+t/p+st(p+q)/(pq\Delta)\).

3. **Exact defect correction.** Let \(w\) be the restriction to follower coordinates of \(e_{a_0}-e_{b_0}\) (so a selected endpoint contributes zero). Because deleting the edge subtracts its incidence outer product, \(M=M_0-ww^T\). The graph remains connected, so \(M\) is positive definite for any nonempty leader set; hence \(1-w^TM_0^{-1}w>0\). Sherman–Morrison gives the exact identity
\[
J(S)=\operatorname{tr}M_0^{-1}+\frac{w^TM_0^{-2}w}{1-w^TM_0^{-1}w}.
\]
Substitution of the entries in step 2 yields eight explicit rational functions \(R_C(p,q)=N_C(p,q)/D_C(p,q)\), one for each pair type \(C\), whose exact integral polynomial coefficients are included in `formulas.json`. That file is numerical data representing the algebraic expressions, not a table of approximate values. Its entries for the defect pair and the ordinary smaller-side pair simplify to \(J_{\mathrm{def}}\) and \(J_{\mathrm{ord}}\) displayed above.

4. **Infinite-domain sign proof.** Each \(D_C\) is strictly positive for \(p,q\ge3\): after substituting \(p=3+X\), \(q=3+Y\), its integer coefficients are nonnegative and its constant term positive. Let \(C_0=\{a_i,a_j\}\) be the ordinary-smaller-side class. For each other class \(C\), form the exact integer polynomial \(P_C=N_C D_{C_0}-N_{C_0}D_C\); its sign equals that of \(R_C-R_{C_0}\). For \(p=6+X\), \(q=6+X+Y\), all coefficients of \(P_C\) are nonnegative for every one of the seven alternatives. For the ordinary-larger-side class, each nonzero monomial contains \(Y\); for the other six competitors the constant term is strictly positive. Consequently \(C_0\) is uniquely optimal when \(p\ge6\), \(q>p\), and ties only with its opposite-side analogue when \(p=q\ge6\).

5. **Three unbounded strips and six boundary cases.** Fix \((p,q_0)=(3,7),(4,5),(5,6)\) and write \(q=q_0+Y\). For each of the seven competitor classes, every coefficient of \(P_C(p,q_0+Y)\) is nonnegative and the constant term strictly positive. Thus the ordinary-smaller-side class is uniquely optimal throughout these strips. Finally direct exact-rational comparison of all eight classes at the six remaining cases \((3,3),(3,4),(3,5),(3,6),(4,4),(5,5)\) gives the unique optimum \(\{a_0,b_0\}\). This exhausts all \(3\le p\le q\).

The polynomial positivity checks are *identities and coefficient-sign arguments over all nonnegative real \(X,Y\)*, not extrapolations from finitely many graph sizes. The included standard-library-only `verify.py` recomputes the rational identities from steps 2–3, recomputes all polynomial products and substitutions, checks every sign coefficient, and separately compares formulas with exact matrix inverses for sample graph sizes.

## Verification
Run `python verify.py` alongside `formulas.json` using Python 3. The verified output was `VERIFY_OK: symbolic coefficient checks 474 exact grounded-matrix comparisons 4155`. All calculations use arbitrary-size integers or fractions. The symbolic portion proves global polynomial identities and nonnegative-coefficient certificates; the finite matrix comparisons independently check the graph-Laplacian normalization and orbit labels. See `VERIFICATION.md` for details.

## Relationship to prior work
Lin, Fardad and Jovanović (arXiv:1302.0450) formulate trace-minimizing noise-free leader selection and provide general relaxations and heuristics, but not a classified optimum for a one-edge-deleted biclique. Fitch and Leonard (arXiv:1407.1569) express optimal sets through joint centrality and obtain exact path and cycle cases; their general graph expression could evaluate this family but does not itself state the eight-class threshold. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) give exact path/ring selection algorithms, which do not directly apply to these dense bipartite graphs. The undeleted biclique has a different symmetry and does not imply the single-defect transition without a fresh rank-one comparison. Literature coverage remains subject to possible equivalent unindexed treatments.

## Limitations
Only budget two and partitions of size at least three are covered. The proof is an exact algebraic classification within this family, not a claim of a general algorithm for arbitrary graphs. The absence of a located equivalent publication is not proof of publication priority. Independent mathematical verification has not been performed.

## References
1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public February 3, 2013), https://arxiv.org/abs/1302.0450.
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public July 7, 2014), https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first public December 20, 2014), https://arxiv.org/abs/1412.6595.
