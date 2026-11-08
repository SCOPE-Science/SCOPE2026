# A sharp conductance-driven switch of optimal two-leader placement in a one-chord biclique

## Finding

Let \(3\le p\le q\) be integers. Start with the unit-conductance complete bipartite network \(K_{p,q}\), with parts \(A\) and \(B\) of sizes \(p\) and \(q\). Choose two distinct vertices \(u,v\in A\) and insert their formerly absent edge with conductance \(t>0\). Exactly two distinct noise-free leader vertices are chosen, minimizing the unscaled grounded-Laplacian inverse trace
\[
J(S)=\operatorname{tr}\bigl((L_{V\setminus S,V\setminus S})^{-1}\bigr),\qquad |S|=2.
\]
Write \(d=q-p\) and
\[
\begin{aligned}
A_0&=q^2\bigl((p-2)d^2+(2p^2-3p+2)d+2p^2\bigr),\\
A_1&=q\bigl((2p-7)d^2+(4p^2-10p+7)d+p(6p+1)\bigr),\\
A_2&=(p-6)d^2+(2p-3)(p-2)d+4p^2,\\
P_{p,q}(t)&=A_0+A_1t+A_2t^2.
\end{aligned}
\]
Only two kinds of leader pairs can be optimal: **AS**, one of \(u,v\) together with a different vertex of \(A\setminus\{u,v\}\), and **BS**, one of \(u,v\) together with any vertex of \(B\). If \(P_{p,q}(t)>0\), all and only AS pairs optimize; if \(P_{p,q}(t)<0\), all and only BS pairs optimize; if \(P_{p,q}(t)=0\), both types and no others optimize. The respective numbers of optimal pairs are \(2(p-2)\), \(2q\), and \(2(p-2)+2q\).

A positive switching threshold exists **if and only if** one of the following holds:
\[
(p=3,\ q\ge8),\quad(p=4,\ q\ge13),\quad(p=5,\ q\ge31).
\]
In these cases \(A_2<0\) and there is exactly one positive root
\[
t_* = \frac{-A_1-\sqrt{A_1^2-4A_2A_0}}{2A_2}>0.
\]
AS is optimal for \(0<t<t_*\), both types tie at \(t=t_*\), and BS is optimal for \(t>t_*\). For all other \((p,q)\) in the stated domain, AS is uniquely optimal as a placement type for **every** \(t>0\). Thus, a sufficiently strong internal edge moves the second leader across the bipartition only for the three sharply bounded small-part sizes above.

The minimum objective is the smaller of the following two explicit rational functions:
\[
\begin{aligned}
J_{\mathrm{AS}}&=J_0(2,0)-\frac{t(p+q+6)}{2q(2q+3t)},\\
J_{\mathrm{BS}}&=J_0(1,1)-\frac{t\,[p^2+pq^2+2pq-3p+q^3+q^2-4q+2]}{q(p+q-1)[pq+q^2-q+(p+2q-2)t]},\\
J_0(a,b)&=\frac{p-a}{q}+\frac{q-b}{p}+\frac{(p-a)(q-b)(p+q)}{pq\,[pq-(p-a)(q-b)]}.
\end{aligned}
\]
For example, \((p,q)=(3,9)\) has \(t_*=24\), at which both types achieve exactly \(J_*=46/15\).

## Assumptions and scope

All original crossing edges carry conductance one. The inserted same-part edge carries finite, arbitrary positive conductance \(t\), not a normalized stochastic probability. The Laplacian is the symmetric weighted combinatorial Laplacian. Leaders are pinned at their desired trajectories and deleted from the grounded matrix; disturbances act on follower coordinates. The objective deliberately omits the conventional common factor \(1/2\). The theorem applies to every integer \(3\le p\le q\) and all real \(t>0\), including ties; it does not optimize the inserted edge's location or conductance.

## Proof

**1. The unmodified biclique inverse.** Suppose \(a\) leaders lie in \(A\) and \(b\) in \(B\), where \(a+b=2\). Set \(\ell=p-a\), \(r=q-b\), \(\Delta=pq-\ell r>0\). Without the added edge the grounded Laplacian is
\[
Q_0=\begin{pmatrix}qI_\ell&-\mathbf1_\ell\mathbf1_r^\top\\-\mathbf1_r\mathbf1_\ell^\top&pI_r\end{pmatrix}.
\]
Schur complementation gives entries of \(G=Q_0^{-1}\): in its \(A\)-block,
\[
G_{ij}=\frac{\delta_{ij}}q+\frac{r}{q\Delta};
\]
in its \(B\)-block,
\[
G_{ij}=\frac{\delta_{ij}}p+\frac{\ell}{p\Delta};
\]
and every cross-block entry equals \(1/\Delta\). Taking the trace proves the displayed formula for \(J_0(a,b)\).

**2. Exact response to the chord.** When neither \(u\) nor \(v\) is a leader, the chord contributes \(t(e_u-e_v)(e_u-e_v)^\top\) to the grounded matrix. Since \(G(e_u-e_v)=(e_u-e_v)/q\), the Sherman--Morrison trace reduction is exactly
\[
D_{\mathrm{both}}=\frac{2t}{q(q+2t)}.
\]
When exactly one chord endpoint is a leader, say \(u\), the chord contributes \(te_ve_v^\top\). With the above \(G\), its trace reduction is
\[
D_{\mathrm{one}}(a,b)=\frac{t\bigl[q^{-2}+2r/(q^2\Delta)+\ell r^2/(q^2\Delta^2)+r/\Delta^2\bigr]}{1+t[1/q+r/(q\Delta)]}.
\]
When both chord endpoints are leaders the chord contributes nothing. The automorphisms preserving \(\{u,v\}\) yield precisely the six classes SS, AS, AA (present only for \(p\ge4\)), AB, BS, BB. Here S means a chord endpoint, A an ordinary vertex in the \(p\)-part, and B a vertex in the \(q\)-part. Their objective expressions, in that order, are
\[
\begin{array}{lll}
J_{\rm SS}=J_0(2,0),&J_{\rm AS}=J_0(2,0)-D_{\rm one}(2,0),&J_{\rm AA}=J_0(2,0)-D_{\rm both},\\
J_{\rm AB}=J_0(1,1)-D_{\rm both},&J_{\rm BS}=J_0(1,1)-D_{\rm one}(1,1),&J_{\rm BB}=J_0(0,2)-D_{\rm both}.
\end{array}
\]
Substitution yields the explicit \(J_{\mathrm{AS}}\) and \(J_{\mathrm{BS}}\) above.

**3. Elimination of four classes.** The \(A\)-side baseline is no worse than either mixed-side or \(B\)-side placement. Writing \(d=q-p\ge0\), direct substitution gives
\[
J_0(1,1)-J_0(2,0)=\frac{(p-2)d^2+(2p^2-3p+2)d+2p^2}{2pq(p+q-1)}>0,
\]
\[
J_0(0,2)-J_0(2,0)=\frac{d(p+q-4)}{2pq}\ge0.
\]
Furthermore, for all permitted parameters,
\[
D_{\mathrm{one}}(2,0)-D_{\mathrm{both}}=\frac{t[pq+q^2-2q+2(p+q)t]}{2q(q+2t)(2q+3t)}>0.
\]
The strict improvements imply \(J_{\mathrm{AS}}\) is strictly smaller than each of SS, AA, AB, BB (whenever the class exists). Therefore every optimizer belongs to AS or BS.

**4. The unique possible transition.** Simplifying the remaining difference gives the exact identity
\[
J_{\mathrm{BS}}-J_{\mathrm{AS}}=\frac{P_{p,q}(t)}{pq(2q+3t)[pq+q^2-q+(p+2q-2)t]}.
\]
Every factor of the denominator is strictly positive. Also \(A_0>0\). For \(p\ge4\), \(A_1>0\). For \(p=3\), the condition \(A_2\ge0\) forces \(0\le d\le4\), in which range \(A_1>0\). Thus \(A_2\ge0\) implies \(P_{p,q}(t)>0\) for all positive \(t\). If \(A_2<0\), the polynomial starts positive and tends to negative infinity. The product of its roots is \(A_0/A_2<0\), hence it has exactly one positive, simple root and the stated sign change.

Finally, the quadratic coefficient is
\[
A_2=(p-6)d^2+(2p-3)(p-2)d+4p^2.
\]
It is strictly positive for \(p\ge6\). For \(p=3\) it factors as \(-3(d-4)(d+3)\); for \(p=4\) it is \(-2d^2+10d+64\); and for \(p=5\) it factors as \(-(d-25)(d+4)\). Since \(d\) is a nonnegative integer, \(A_2<0\) is equivalent to precisely the three size regimes in the statement. This proves all optimality, strictness and tie assertions.

## Verification

Run the included standard-library-only Python program with `python verify.py`. It constructs independent exact rational grounded matrices, inverts them by Gauss--Jordan elimination, compares every two-leader placement to the derived class formulas in finite test grids, and checks the polynomial identity and optimizer classification on a larger parameter grid. It reports 2,696 exact matrix comparisons and 2,610 exact formula/optimizer checks, including the positive threshold \((p,q,t)=(3,9,24)\) and all three size-boundary regimes. These finite tests check algebra but are not substitutes for the preceding proof for all integer sizes and positive real conductances.

## Relationship to prior work

Lin, Fardad and Jovanović formulate the noise-free leader problem via the trace of an inverse grounded Laplacian and develop general optimization algorithms [1]. Fitch and Leonard obtain a general two-leader characterization via joint centrality, with explicit solved examples on paths and cycles [2]. Patterson, McGlohon and Dyagilev treat efficient exact leader selection for weighted paths and rings [3]. The exact one-intrapart-edge biclique placement phase diagram and its three sharp imbalance boundaries are not stated in the inspected texts. The general joint-centrality formula is compatible with, but does not already evaluate, the rational inequalities or critical conductances above. Patterson, Yi and Zhang provide a resistance-distance method with explicit special cases for cycles, paths and trees [5]; their displayed classifications do not evaluate this augmented biclique. Zhou and coauthors optimize a *different* objective, the smallest grounded-Laplacian eigenvalue, by choosing edges for a fixed leader set [4].

At zero added conductance the classes with two leaders in the smaller part are tied (and in balanced bicliques, the symmetric opposite-part placements tie as well). The theorem resolves all strictly positive conductances and distinguishes a phase transition impossible to infer merely from that zero-weight limit. No claim of a universal novelty certificate is made.

## Limitations

This is a closed-form result for exactly two noise-free leaders on one particular weighted defect of \(K_{p,q}\). It does not classify larger budgets, noisy leaders, multiple added edges or alternate optimization criteria. A complete publication-priority search of all unindexed and inaccessible sources has not been established, so equivalent prior descriptions remain possible. Verification is exact in the listed finite tests but does not independently certify the infinite proof.

## References

1. Fu Lin, Makan Fardad, Mihailo R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, first arXiv public version 3 February 2013, https://arxiv.org/abs/1302.0450.
2. Katherine E. Fitch and Naomi Ehrich Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, first arXiv public version 7 July 2014, https://arxiv.org/abs/1407.1569.
3. Stacy Patterson, Neil McGlohon and Kirill Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, first arXiv public version 20 December 2014, https://arxiv.org/abs/1412.6595.
4. Xiaotian Zhou, Haoxin Sun, Wei Li and Zhongzhi Zhang, *Optimization on the smallest eigenvalue of grounded Laplacian matrix via edge addition*, first arXiv public version 29 September 2023, https://arxiv.org/abs/2309.17019.
5. Stacy Patterson, Yuhao Yi and Zhongzhi Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, first arXiv public version 23 August 2017, https://arxiv.org/abs/1708.06873.
