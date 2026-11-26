# A two-threshold response of graph Hodge endpoint norms to a missing clique edge

## Finding
For every integer \(N\ge3\), let \(G_N=K_N-\{01\}\) be the unweighted complete graph with precisely the edge joining distinguished vertices \(0,1\) removed. Give its real edge space the usual coordinate \(\ell_1\) and \(\ell_\infty\) norms. For any orientation, write \(D\) for the vertex-edge incidence matrix and \(L=DD^{\mathsf T}\). The canonical Euclidean-orthogonal cut and cycle projections are
\[
Q=D^{\mathsf T}L^+D,\qquad P=I-Q.
\]
For \(N=3\), the remaining graph is a tree, so \(\|Q\|_1=\|Q\|_\infty=1\) and \(\|P\|_1=\|P\|_\infty=0\). For all \(N\ge4\), the **exact** induced endpoint norms are
\[
\boxed{\|Q\|_1=\|Q\|_\infty=2-\frac2N+\frac{(N-4)_+}{N(N-2)}}
\]
and
\[
\boxed{\|P\|_1=\|P\|_\infty=3-\frac6N+\frac{(N-6)_+}{N(N-2)}},
\qquad t_+=\max\{t,0\}.
\]
In contrast, on the intact clique \(K_N\) these norms are \(2-2/N\) and \(3-6/N\) for \(N\ge3\). Therefore deleting one edge strictly raises the cut norm exactly when \(N\ge5\) and strictly raises the cycle norm exactly when \(N\ge7\). For \(N=4\) both norms are unchanged, while for \(N=5,6\) only the cut norm increases. At \(N=3\) both norms decrease.

The maximizing columns undergo distinct transitions. The remaining edges fall into two automorphism classes: **incident edges**, meeting one endpoint of the deleted edge, and **remote edges**, meeting neither. For the cut projection, both edge classes tie at \(N=4\), while incident columns strictly maximize when \(N\ge5\). For the cycle projection, remote columns strictly maximize for \(4\le N\le5\), both classes tie at \(N=6\), and incident columns strictly maximize for \(N\ge7\). At \(N=3\), all cycle columns vanish and only incident edges survive.

## Assumptions and scope
All graphs are simple, unweighted and connected. The parameter \(N\) ranges through integers \(N\ge3\). The norms are induced on real edge-coordinate spaces; the projections are orthogonal only for the standard Euclidean inner product. This result does not minimize norms over all nonorthogonal projections. Because \(Q,P\) are symmetric real matrices, their induced \(\ell_1\) and \(\ell_\infty\) norms coincide and equal their largest absolute column sums.

## Proof
Write \(d=e_0-e_1\in\mathbb R^N\), and let \(\mathbf1\) be the constant vector. On \(\mathbf1^\perp\), the complete-graph Laplacian equals \(NI\). Deleting the edge \(01\) changes the Laplacian to \(L=NI-dd^{\mathsf T}\) on that subspace. Since \(\|d\|_2^2=2<N\), the rank-one inverse formula yields
\[
L^+=\frac1N\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}N\right)+\frac{dd^{\mathsf T}}{N(N-2)}.
\]
For an edge \(e=uv\), put \(b_e=e_u-e_v\). The entries of its cut-projector column are, up to the irrelevant orientation signs, the voltage drops \(\langle b_f,L^+b_e\rangle\), where \(f\) ranges over all remaining edges. The diagonal is its effective resistance \(r_e=b_e^{\mathsf T}L^+b_e\).

First take a remote edge, with both endpoints outside \(\{0,1\}\). Then \(d^{\mathsf T}b_e=0\), so \(L^+b_e=b_e/N\). The edge \(01\), which is omitted, would have carried zero voltage drop. The remote cut-column sum and diagonal are consequently
\[
q_B=\frac{2(N-1)}N,\qquad r_B=\frac2N.
\]
Such an edge exists only when \(N\ge4\).

Next take an incident edge \(e=0x\), where \(x\notin\{0,1\}\). Multiplying the stated inverse by \(b_e\), its potential takes the four values
\[
f(0)=\frac{N-1}{N(N-2)},\quad f(1)=-\frac1{N(N-2)},\quad f(x)=-\frac1N,\quad f(y)=0\ \text{for all remaining }y.
\]
The absolute drops along the edges are: \((2N-3)/(N(N-2))\) on \(0x\); \((N-1)/(N(N-2))\) on each of the \(N-3\) edges \(0y\); \((N-3)/(N(N-2))\) on \(1x\); \(1/(N(N-2))\) on each of the \(N-3\) edges \(1y\); and \(1/N\) on each of the \(N-3\) edges \(xy\). Other drops vanish. Their sum and the diagonal are exactly
\[
q_A=2-\frac1{N-2},\qquad r_A=\frac{2N-3}{N(N-2)}.
\]
For every surviving edge, \(0<r_e\le1\), and the cycle-projection column sum equals
\[
p_e=|1-r_e|+\sum_{f\ne e}|Q_{fe}|=1+q_e-2r_e.
\]
Therefore the two cycle-column values are
\[
p_A=3-\frac6N+\frac{N-6}{N(N-2)},\qquad p_B=3-\frac6N.
\]
The exact orbit differences factor as
\[
q_A-q_B=\frac{N-4}{N(N-2)},\qquad p_A-p_B=\frac{N-6}{N(N-2)}.
\]
Taking the maximum of the two existing column values proves both norm formulas and all maximizing-class and threshold statements for \(N\ge4\). The graph \(G_3\) is a two-edge tree; on a tree the cut space is the full edge space. This gives the separate \(N=3\) assertion and completes the proof.

## Verification
The included standalone `checker.py` constructs the grounded graph Laplacian, solves voltage equations using exact rational Gaussian elimination, and computes **every** projector column for each integer \(3\le N\le11\). Its completed run returned `DELETED_CLIQUE_EXACT_RATIONAL_OK graph_sizes=9 columns= 210`. Each column was checked against the correct incident/remote rational formula, and maxima were compared. These finite tests are independent checks of the displayed formulas, not a proof for unbounded \(N\); the rank-one inverse and orbit classification above supply the latter.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023, arXiv:2305.12582) develop invariant cycle-space projections and transportation-cost connections, concentrating their explicit classifications on tori and Hamming graphs. Their general cycle/cut-space framework supplies context but does not give the two threshold formulas for a clique with a deleted edge. Their 2020 study of diamond and Laakso graphs (arXiv:2007.07949) concerns other graph families. General effective-resistance and transfer-current techniques furnish ingredients for this computation; the claimed new statement is the **simultaneous closed-form two-threshold norm and extremizer classification across all graph orders**, not the rank-one inverse identity itself.

## Limitations
The assertion concerns canonical Euclidean-orthogonal projections only, not the least norm among arbitrary projections. It does not treat weighted missing edges, multiple deleted edges, or other complete multipartite graphs. Small-parameter classifications may be covered by existing finite graph tables; the unbounded sharp transition statement is the distinctive asserted contribution. The exact elementary calculation does not establish that no equivalent result exists in specialized electrical-network literature; independent review is not performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 2023-05-21. In particular the introduction, Section 1.1, Proposition 8 and Section 2.1.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949, first posted 2020-07-15.
