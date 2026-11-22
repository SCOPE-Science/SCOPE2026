# Parity-defect plateaux and entropy-selected coexistence in four-state Potts bipyramids

## Finding

For each integer \(n\ge6\), let \(B_n=\overline{K_2}\vee C_n\) be the bipyramid: two **nonadjacent** distinguished apices, each connected to all \(n\) vertices of a labeled cycle, together with all cycle edges. Give each vertex a classical Potts spin in \(\{0,1,2,3\}\), with color \(0\) favored by a nonnegative field. For uniform antiferromagnetic penalty \(J>0\) and field \(H\ge0\), define
\[
\mathcal H(\sigma)=J\sum_{uv\in E(B_n)}\mathbf1\{\sigma_u=\sigma_v\}-H\sum_{v\in V(B_n)}\mathbf1\{\sigma_v=0\},\qquad x=H/J.
\]
The following is the **complete exact ground-state energy and labeled ground-state degeneracy** for every real \(x\ge0\) and every \(n\ge6\). Let \(L_n=F_{n-1}+F_{n+1}\) be the Lucas number, equivalently the number of independent vertex sets of \(C_n\), and put
\[
D_n=3\bigl(2^n+(-1)^n\bigr)+6L_n.
\]
If \(n\ge6\) is even, the energy, divided by \(J\), and degeneracy are
\[
\begin{array}{c|c|c}
\text{field}& E_{\min}/J & g_n\\\hline
x=0&0&4(2^n+2)+24\\
0<x<2&-nx/2&6\,2^{n/2}+12\\
x=2&-n&D_n\\
2<x<n&n(1-x)&9\\
x=n&n(1-n)&16\\
x>n&3n-(n+2)x&1
\end{array}
\]
If \(n\ge7\) is odd, the complete table is
\[
\begin{array}{c|c|c}
\text{field}& E_{\min}/J & g_n\\\hline
x=0&0&4(2^n-2)\\
0<x<1&-\frac{n-1}{2}x&3n\,2^{(n-1)/2}\\
x=1&-\frac{n-1}{2}&n\bigl(6\,2^{(n-1)/2}+6\bigr)\\
1<x<2&1-\frac{n+1}{2}x&n\bigl(3\,2^{(n-1)/2}+6\bigr)\\
x=2&-n&D_n\\
2<x<n&n(1-x)&9\\
x=n&n(1-n)&16\\
x>n&3n-(n+2)x&1
\end{array}
\]
In particular, **odd rim parity inserts a genuine extra field threshold at \(H=J\)** that is absent for even rim length. At \(H=2J\), all ground states have nonfavored apices and the nonfavored rim sites are an arbitrary independent set \(R\subseteq C_n\). For each such \(R\), there are exactly \(3\cdot2^{|R|}+6\) labeled spin assignments. Consequently, as \(n\to\infty\) through either parity, this critical field has residual entropy per rim vertex \(\log2\), and the fraction of favored rim sites in a uniformly chosen critical ground configuration tends in probability to \(2/3\). This is strictly between the limiting fractions \(1/2\) immediately below and \(1\) immediately above \(H=2J\).

## Assumptions and scope

The two apices are **not** adjacent. The cycle has vertices \(0,1,\ldots,n-1\) in cyclic order; all spins and vertices are labeled. Every graph edge is counted once. There are four colors and exactly one preferred color. The field is uniform and nonnegative; the exchange penalty is fixed finite \(J>0\). All degeneracies count individual color assignments, including permutations of nonfavored colors. Even-length members are Eulerian plane triangulations (all rim degrees are four, both apex degrees are even); odd-length members have two odd-degree apices. The thermodynamic statements concern exactly the zero-temperature field slice \(H=2J\), not a positive-temperature singularity.

## Proof

Write \(S\) for all vertices colored \(0\), let \(t\in\{0,1,2\}\) be the number of favorite-colored apices, \(k\in\{0,\dots,n\}\) the number of favorite-colored rim vertices, and \(p\) the number of rim edges both of whose endpoints belong to \(S\). Monochromatic edges between favorite vertices alone contribute \(tk+p\), so
\[
\mathcal H/J\ \ge\ p+tk-x(k+t).
\]
Every cyclic binary word with \(k\) occupied sites has at least
\[
p_{\min}(k)=\max\{0,2k-n\}
\]
adjacent occupied pairs: its \(n-k\) vacancies can cover at most \(2(n-k)\) cycle edges. The lower bound is achieved for \(k\le\lfloor n/2\rfloor\) by an independent occupied set, and for \(k\ge\lceil n/2\rceil\) by an independent vacant set.

For a fixed \(t\), the minimum of \(p_{\min}(k)+tk-x(k+t)\) occurs at a breakpoint of this piecewise-linear function in \(k\). Put \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\), and \(\epsilon=n\bmod2\). Only \(k\in\{0,a,b,n\}\) need be compared, with duplicate breakpoints identified when \(n\) is even. The corresponding three-apex-sector candidate table (columns \(t=0,1,2\)) is
\[
\begin{array}{c|ccc}
k& t=0&t=1&t=2\\\hline
0&0&-x&-2x\\
a&-ax&a-(a+1)x&2a-(a+2)x\\
b&\epsilon-bx&\epsilon+b-(b+1)x&\epsilon+2b-(b+2)x\\
n&n-nx&2n-(n+1)x&3n-(n+2)x
\end{array}
\]
A comparison of these finitely many affine functions gives the lower envelope
\[
E_{\min}/J=\begin{cases}
-\frac n2x,&n\text{ even},\ 0\le x\le2,\\
-\frac{n-1}2x,&n\text{ odd},\ 0\le x\le1,\\
1-\frac{n+1}2x,&n\text{ odd},\ 1\le x\le2,\\
n-nx,&2\le x\le n,\\
3n-(n+2)x,&x\ge n.
\end{cases}
\]
This envelope comparison can be checked without extrapolation: on each displayed interval, subtract the proposed affine branch from each candidate in the table, and check nonnegativity at both interval endpoints; for \(x\ge n\), the last line has maximal occupied-vertex slope and is tied at \(x=n\). The stated lower bounds on \(n\) rule out extra apex-sector crossings. The minimizers at strict positive fields always have \(t=0\) and \(k>0\) until \(x=n\), and then \(k=n\), with all apex sectors coexisting at \(x=n\). Whenever \(t=0\) and \(k>0\) with the stipulated optimal occupied/vacant patterns, the nonfavored rim vertices induce a union of paths. Both apices may be given one nonfavored color and the remaining rim vertices properly colored with the other two; therefore these lower bounds are **attainable**. For \(x>n\), making every vertex favored attains the final branch. Hence the envelope is the true energy, not merely a formal lower bound.

It remains to count *all* equality cases. At \(x=0\), every proper four-coloring is a ground state. If both apices share a color, there are four choices and the rim has the chromatic polynomial \(P(C_n,3)=2^n+2(-1)^n\) colorings. If the apices differ, there are twelve ordered choices and \(P(C_n,2)=1+(-1)^n\) rim colorings. This yields the first rows.

For positive fields below \(x=2\), the apices are nonfavored. On an even rim, the favorite sites occupy one of the two alternating sublattices. The remaining \(n/2\) rim sites have no mutual edges. The apex colors may coincide (three choices, then two possible colors for each remaining rim vertex) or differ (six ordered choices, then one color per remaining rim vertex). This gives \(2(3\,2^{n/2}+6)\). On an odd rim, the low-field interval \(0<x<1\) selects \(k=(n-1)/2\) favorite sites in an independent maximum set (\(n\) possible such sets). The remaining \((n+1)/2\) rim vertices induce exactly one edge and isolated sites; the apices must share one of three nonfavored colors and the two other nonfavored colors give \(2^{(n-1)/2}\) proper colorings. At \(1<x<2\), the favorite sites are the complement of a maximum independent set and number \((n+1)/2\), leaving \((n-1)/2\) isolated nonfavorite rim sites. There are \(n\) arrangements, each contributing \(3\,2^{(n-1)/2}+6\). At \(x=1\), these two disjoint sectors coexist, giving the stated sum.

At \(x=2\), equality in the cycle bound requires that the *nonfavorite* rim set \(R\) be independent. All apices remain nonfavorite; they can have the same nonfavorite color in three ways, permitting \(2^{|R|}\) assignments of the other two colors to \(R\), or distinct nonfavorite colors in six ways, forcing each vertex of \(R\) to use the third color. Hence
\[
g_n(2)=3I(C_n,2)+6I(C_n,1),\qquad
I(C_n,z)=\sum_{R\subseteq V(C_n)\,\text{independent}}z^{|R|}.
\]
The cycle independence polynomial satisfies \(I(C_n,2)=2^n+(-1)^n\) and \(I(C_n,1)=L_n\), by the cyclic two-state transfer eigenvalues \((1\pm\sqrt{1+4z})/2\). For \(2<x<n\), all rim vertices are favored, while each apex independently takes one of three nonfavorite colors, giving nine states. At \(x=n\), each apex can instead be any of the four colors at no energy change, giving sixteen states. Thereafter only the all-favorite configuration remains.

Finally, the first term \(3I(C_n,2)\) dominates \(6I(C_n,1)\) exponentially because \(2>\varphi=(1+\sqrt5)/2\). Thus \(\log g_n(2)/n\to\log2\). The occupied proportion of \(R\) in the dominant hard-core cycle measure with activity \(z=2\) is
\[
\lim_{n\to\infty}\frac{\mathbb E|R|}{n}
=\left.z\frac{d}{dz}\log\frac{1+\sqrt{1+4z}}2\right|_{z=2}=\frac13.
\]
Standard two-state transfer eigenvalue concentration (or a second derivative of the explicit cycle partition polynomial) gives variance \(O(n)\), hence \(|R|/n\to1/3\) in probability. The favored rim proportion is \(1-|R|/n\to2/3\). All statements follow. \(\square\)

## Verification

The standalone file `verify.cpp` exhaustively enumerates all \(4^{n+2}\) labeled Potts configurations for each \(n=6,7,8,9\), without assuming the proposed energy envelope. It independently accumulates the exact minimum number of monochromatic bonds at every favored-color occupation and the associated multiplicity, and compares these with the proven formula at integer fields and several half-integer fields, including every listed boundary. It also directly enumerates independent sets of the cycle and checks the two Lucas-related identities. Compile and run in the artifact directory with `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. Every comparison passed, terminating in `ALL_ENUMERATION_CHECKS_PASSED`. Finite checks support but do not replace the proof for unbounded rim length.

## Relationship to prior work

Four-state Potts antiferromagnets on Eulerian plane triangulations are motivated by Deng, Huang, Jacobsen, Salas, and Sokal (2011), whose full article studies bulk finite-temperature transitions on periodic lattices and a zero-temperature coloring mapping, not the finite \(B_n\) positive-field ground diagram above. Chang and Shrock (2009) derive weighted *proper-coloring* polynomials for a single-hub wheel, and Shrock and Xu (2010) analyze weighted proper colorings of \(K_p\vee C_n\) (with **adjacent** multiple hubs for \(p\ge2\)); both employ an infinite-antiferromagnetic-coupling coloring restriction rather than competing finite exchange and finite field. Neither contains the two-**nonadjacent**-apex field diagram or the parity-induced unit-field plateau. A published three-color **one-hub** wheel classification establishes the analogous \(2J\) and size-scaled crossings, but its wheel topology and two nonfavored-color freedom do not imply the additional \(J\) crossing, the four-color two-apex degeneracies, or the critical \(\log2\) entropy and \(2/3\) favored-site selection. The new result is a finite-graph specialization and does not claim general finite-temperature Potts machinery as new.

## Limitations

The proof requires exactly four named colors, two nonadjacent apices, uniform positive coupling, one uniform favored-color field, and \(n\ge6\). It does not prove a positive-temperature phase transition, universality class, or an infinite-volume Gibbs phase diagram. Since the last crossing grows as \(H=nJ\), full saturation does not occur at a fixed field in the limit of long bipyramids. The comparison literature may contain equivalent unindexed specializations, and independent expert review has not been performed.

## References

- S.-C. Chang and R. Shrock, *Weighted Graph Colorings*, arXiv:0908.2375 (first posted 2009-08-17), https://arxiv.org/abs/0908.2375.
- R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182 (first posted 2010-09-07), https://arxiv.org/abs/1009.1182.
- Y. Deng, Y. Huang, J. L. Jacobsen, J. Salas, A. D. Sokal, *Finite-temperature phase transition in a class of 4-state Potts antiferromagnets*, arXiv:1108.1743 (first posted 2011-08-08), https://arxiv.org/abs/1108.1743.
- *Two magnetic thresholds and Lucas degeneracy on three-state antiferromagnetic Potts wheels*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-magnetic-thresholds-and-lucas-degeneracy-on-three-state-anti--c2a2bf28f112.
