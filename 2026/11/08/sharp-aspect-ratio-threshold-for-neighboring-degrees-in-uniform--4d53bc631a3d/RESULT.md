# Sharp aspect-ratio threshold for neighboring degrees in uniform rook-graph spanning trees

## Finding
For integers \(m,n\ge2\), let \(G=K_m\square K_n\) be the Cartesian product of complete graphs, with vertex set \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\). Sample a spanning tree \(T\) uniformly among all spanning trees of \(G\). For \(u=(0,0)\) and \(v=(0,1)\), write \(D_u=\deg_T(u)\) and \(D_v=\deg_T(v)\). Then

\[
\operatorname{Cov}(D_u,D_v)=\frac{2m^3n-m^2n^3-m^2n^2+m^2n+2m^2-mn^2+2n^2}{m^2n^2(m+n)^2}.
\]

The covariance is strictly positive **exactly when** \(m\ge\binom{n+1}{2}\), is zero **only at** \((m,n)=(2,2)\), and is strictly negative at all other integer pairs \(m,n\ge2\) below that threshold. For edges in the other coordinate direction, interchange \(m\) and \(n\). In particular, neighboring vertex degrees can be positively correlated even though indicators of distinct tree edges are negatively correlated.

For any fixed \(c>0\) and sequences with \(m/n^2\to c\),
\[
n^3\operatorname{Cov}(D_u,D_v)\longrightarrow\frac{2c-1}{c^2}.
\]
The exact integer threshold resolves the critical \(c=1/2\) boundary at finer resolution.

## Assumptions and scope
Here \(K_m\square K_n\) has an edge between distinct vertices exactly when one coordinate is equal and the other differs. Every graph considered is finite, connected, unweighted and simple. \(T\) is uniform, with no root or conditioning. The vertices \(u,v\) are adjacent by changing the \(K_n\)-coordinate; graph automorphisms make the choice of labels immaterial. The stated threshold concerns \(m,n\in\mathbb Z\) with \(m,n\ge2\). The limiting statement allows arbitrary integer sequences satisfying \(n\to\infty\) and \(m/n^2\to c>0\).

## Proof
Write \(P_r=J_r/r\) and \(Q_r=I_r-P_r\). The graph Laplacian on \(\mathbb R^{m}\otimes\mathbb R^n\) is
\[
L=mQ_m\otimes I_n+nI_m\otimes Q_n.
\]
The three nonconstant spectral blocks are \(Q_m\otimes P_n\), \(P_m\otimes Q_n\), and \(Q_m\otimes Q_n\), with eigenvalues \(m,n,m+n\), respectively. Thus the Moore–Penrose inverse is
\[
G=L^+=\frac{Q_m\otimes P_n}{m}+\frac{P_m\otimes Q_n}{n}+\frac{Q_m\otimes Q_n}{m+n}.
\]
For vertices \(x=(a,b)\), \(y=(c,d)\), defining \(A=\mathbf1_{a=c}-1/m\) and \(B=\mathbf1_{b=d}-1/n\), the entries simplify to \(G(x,y)=A/(mn)+B/(mn)+AB/(m+n)\).

For oriented edges \(e=(x,y)\) and \(f=(z,w)\), let \(K(e,f)=G(x,z)-G(x,w)-G(y,z)+G(y,w)\). The finite transfer-current identity implies \(\mathbb P(e\in T)=K(e,e)\) and \(\operatorname{Cov}(\mathbf1_{e\in T},\mathbf1_{f\in T})=-K(e,f)^2\) for distinct unoriented edges. For the same edge the variance is \(K(e,e)-K(e,e)^2\). Consequently, for \(u\ne v\),
\[
\operatorname{Cov}(D_u,D_v)=\mathbf1_{u\sim v}K(uv,uv)-\sum_{e\ni u}\sum_{f\ni v}K(e,f)^2.
\]
The formula is orientation independent. Its first term is necessary because the edge \(uv\) is counted in both degrees.

Orient all incident edges outward from their marked vertices. Group the edges at \(u\) into \(A_i:u\to(i,0)\) for \(1\le i<m\), the shared edge \(B_1:u\to v\), and \(B_j:u\to(0,j)\) for \(2\le j<n\). Group the edges at \(v\) into \(C_k:v\to(k,1)\) for \(1\le k<m\), the reverse shared edge \(D_0:v\to u\), and \(D_l:v\to(0,l)\) for \(2\le l<n\). Substitution in \(G(x,y)\) gives the following complete transfer-current table. The entry \(\eta=(n+1)/(n(m+n))\) abbreviates a positive rational quantity.

| Pair | Transfer current | Number of ordered pairs |
| --- | --- | --- |
| \(A_i,C_i\) | \(2/[m(m+n)]\) | \(m-1\) |
| \(A_i,C_k\), \(i\ne k\) | \(1/[m(m+n)]\) | \((m-1)(m-2)\) |
| \(A_i,D_0\) and \(B_1,C_k\) | \(-1/(m+n)\) | \(2(m-1)\) |
| \(B_1,D_0\) | \(-2\eta\) | \(1\) |
| \(B_1,D_l\), \(B_j,D_0\) | \(-\eta\) | \(2(n-2)\) |
| \(B_j,D_j\) | \(+\eta\) | \(n-2\) |
| All other pairs | \(0\) | remainder |

For the shared edge, \(p=K(uv,uv)=2\eta=2(n+1)/(n(m+n))\). Squaring and summing the table yields
\[
S:=\sum_{e\ni u}\sum_{f\ni v}K(e,f)^2
=\frac{(m-1)(m+2)}{m^2(m+n)^2}+\frac{2(m-1)}{(m+n)^2}+\frac{(3n-2)(n+1)^2}{n^2(m+n)^2}.
\]
The covariance is \(p-S\). Combining over the positive denominator \(m^2n^2(m+n)^2\) yields the numerator
\[
N(m,n)=2nm^3-(n^3+n^2-n-2)m^2-n^2m+2n^2.
\]

For \(n=2\), \(N(m,2)=4(m-1)(m-2)(m+1)\), so the only zero in the allowed range is \(m=2\), and the covariance is positive for all \(m\ge3\). For each integer \(n\ge3\), the coefficient signs of the cubic in \(m\) are \(+,-,-,+\), so Descartes' rule gives at most two positive real zeros, with multiplicity. As \(N(0,n)>0\), \(N(2,n)=-4(n-2)(n^2+3n+1)<0\), and \(N(m,n)\to+\infty\) when \(m\to\infty\), there are exactly two positive zeros, one in \((0,2)\) and one in \((2,\infty)\); the sign changes only once on \([2,\infty)\). Put \(t=n(n+1)/2\). Direct exact substitution gives
\[
N(t-1,n)=-\frac{(n-2)(n^4+4n^3+3n^2-4n+4)}4<0,
\qquad
N(t,n)=\frac{n^2(n^3+2n^2+3n+10)}4>0.
\]
The polynomial in the first parentheses is strictly positive for every \(n\ge3\). Because \(t\) is an integer and the larger zero is unique, the integer sign threshold is exactly \(m=t\). Finally, substituting \(m\sim cn^2\) in numerator and denominator gives the stated scaling limit. This completes all cases.

## Verification
The included \(verify.py\) is standalone standard-library Python and recomputes the covariance using the spectral Green kernel independently of the simplified rational expression, tests the integer sign threshold, and exhaustively enumerates spanning trees for \((m,n)=(2,2),(2,3),(3,2),(2,4),(3,3)\). It also verifies the two threshold-substitution identities over a finite set of dimensions. Execute \(python3\,\texttt{verify.py}\). Its exact-arithmetic checks passed with output \(\texttt{VERIFY\_OK 313 exact assertions}\). These finite computations are checks, not a substitute for the symbolic proof above.

## Relationship to prior work
The transfer-current/determinantal identity is classical (Burton–Pemantle). General negative correlation of *distinct edge indicators* does not determine the covariance of two vertex degrees, since adjacent degrees share one edge. General spanning-tree marginal formulas leave the rectangular-product Green-kernel specialization, the explicit polynomial and the exact triangular-number sign threshold to be evaluated. Hladký–Nachmias–Tran investigate local limits of USTs on dense graphs; their one-root asymptotics do not give this exact finite two-vertex sign boundary. Huh–Schröter–Wang examine edge/basis correlation bounds, not this vertex-degree sign classification. Rapoport (2025) gives full joint degree prescriptions for general finite graphs but not the evaluated rook-graph sign threshold. A related graph-theoretic study of rook graphs by Speeter concerns gonality rather than random spanning trees.

## Limitations
The theorem concerns only unweighted rook graphs and pairs of vertices adjacent in the ambient graph. It does not assert signs for weighted spanning trees or arbitrary graph products, and it does not compute the full joint degree distribution. The exact formula may be obtainable by specializing general determinantal identities; absence of the same explicit threshold from the inspected sources is not a proof of historical novelty. Independent mathematical validation has not been performed.

## References
- R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability 21 (1993), 1329–1371, freely accessible manuscript: https://www2.math.upenn.edu/~pemantle/papers/burton.pdf .
- J. Hladký, A. Nachmias and T. Tran, *The local limit of the uniform spanning tree on dense graphs*, arXiv:1711.09788, first publicly posted 2017-11-27: https://arxiv.org/abs/1711.09788 .
- J. Huh, B. Schröter and B. Wang, *Correlation bounds for fields and matroids*, arXiv:1806.02675, first publicly posted 2018-06-07: https://arxiv.org/abs/1806.02675 .
- N. Speeter, *Methods of Computing Graph Gonalities*, University of Kentucky dissertation (2023), https://uknowledge.uky.edu/math_etds/104/ .
- A. Rapoport, *Correlations in Uniform Spanning Trees: a Fermionic Approach*, Journal of Statistical Physics 192 (2025), article 145, published 2025-10-18, https://doi.org/10.1007/s10955-025-03510-0 .
