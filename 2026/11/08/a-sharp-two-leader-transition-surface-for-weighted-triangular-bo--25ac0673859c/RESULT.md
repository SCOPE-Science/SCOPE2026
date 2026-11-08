# A sharp two-leader transition surface for weighted triangular-book networks

## Finding
Let \(m\ge4\) be an integer. Form a network with hubs \(u,v\), leaves \(z_1,\ldots,z_m\), hub–hub conductance \(c>0\), conductance \(a>0\) on every \(uz_i\), and conductance \(b>0\) on every \(vz_i\), with no other edges. Interchanging the hub names if needed, assume \(a\ge b\). The unweighted underlying graph is the triangular book \(K_{1,1,m}\).

Choose exactly two distinct *noise-free* leaders \(S\). Let \(L\) be the symmetric weighted combinatorial Laplacian, \(F=V\setminus S\), and
\[
J(S)=\operatorname{tr}\bigl((L_{FF})^{-1}\bigr).
\]
Define the sharp threshold
\[
c_*(m,a,b)=\frac{a^2-(m-2)ab+(m-1)b^2}{a+b}.
\]
Then the **complete global minimizer classification**, including all ties, is as follows:

1. If \(0<c<c_*\), the sole optimal pair is \(\{u,v\}\), with minimum \(m/(a+b)\).
2. If \(c=c_*>0\) and \(a>b\), precisely \(\{u,v\}\) and the \(m\) pairs \(\{u,z_i\}\) are optimal. If instead \(a=b\), all \(2m\) hub–leaf pairs also tie with \(\{u,v\}\).
3. If \(c>c_*\) and \(a>b\), precisely the \(m\) pairs \(\{u,z_i\}\) are optimal. If \(a=b\), precisely the \(2m\) hub–leaf pairs are optimal.

The interpretation of \(c_*\le0\) is literal: since \(c>0\), the third case always holds. No pair of two leaves is optimal for any \(m\ge4\) or positive conductances. The minimum in the hub–leaf regime is
\[
J_* = \frac{m-1}{a+b}+
\frac{(a+b)^2+(m-1)b^2}{(a+b)[mab+b^2+c(a+b)]}.
\]
For \(m\ge7\), there is a nonempty range of hub-to-leaf asymmetry for which the hub–leaf regime is optimal for **every** \(c>0\). More exactly, with \(R=a/b\ge1\),
\[
c_*\le0\quad\Longleftrightarrow\quad
\frac{m-2-\sqrt{m^2-8m+8}}2\le R\le
\frac{m-2+\sqrt{m^2-8m+8}}2.
\]
For \(4\le m\le6\), this zero-threshold interval is absent. For example, \(m=7\), \(a=5/2\), \(b=1\) give \(c_*=-1/14\), so every optimal pair consists of the more strongly coupled hub and one leaf at every positive hub–hub conductance.

## Assumptions and scope
All edge conductances are positive reals, the graph has \(m+2\) vertices, \(m\ge4\), and the leader count is exactly two. The Laplacian convention is \(L_{ii}=\sum_{j\ne i}w_{ij}\), \(L_{ij}=-w_{ij}\). Grounding deletes leader rows and columns without renormalizing follower diagonals. Since the weighted graph is connected and at least one vertex is grounded, every \(L_{FF}\) is positive definite. The cost is the trace of its inverse, not the square root, not the entire-network pseudoinverse trace, and not a control-Gramian determinant. A physical steady-state covariance convention may multiply this objective by a constant \(1/2\), which leaves the optimal sets unchanged.

The two hubs are named so that \(a\ge b\). If \(b>a\) initially, interchange \(u,v\) and \(a,b\). Equality of distinct vertex pairs refers to sets, not different orderings.

## Proof
Put \(s=a+b\). Permutations of the leaves preserve every weighted edge. Thus the complete family of unordered two-leader configurations consists of four types: the hub pair \(\{u,v\}\), a pair \(\{u,z_i\}\), a pair \(\{v,z_i\}\), and two leaves \(\{z_i,z_j\}\) with \(i\ne j\). We compute their costs exactly:
\[
\begin{aligned}
J_{uv}&=\frac m s,\\
J_{uz}&=\frac{m-1}{s}+\frac{s^2+(m-1)b^2}{s[mab+b^2+cs]},\\
J_{vz}&=\frac{m-1}{s}+\frac{s^2+(m-1)a^2}{s[mab+a^2+cs]},\\
J_{zz}&=\frac{2(a^2+b^2)+abm(3m-4)+cs(3m-4)}{2s[mab+cs]}.
\end{aligned}
\]
To derive \(J_{uv}\), ground both hubs: every surviving leaf has diagonal \(s\). To derive \(J_{uz}\), ground \(u\) and one leaf: the \(m-1\) remaining leaves give a diagonal block \(sI\), joined by conductance \(b\) to \(v\), whose original degree is \(mb+c\). The scalar Schur complement is \(D=mb+c-(m-1)b^2/s=(mab+b^2+cs)/s\). The block inverse trace is \((m-1)/s+[1+(m-1)b^2/s^2]/D\). Swapping \(a,b\) gives \(J_{vz}\).

For \(J_{zz}\), ground any two leaves. The remaining \(m-2\) leaves form a block \(sI\). The Schur complement on the two hubs is
\[
T=\begin{pmatrix}ma+c&-c\\-c&mb+c\end{pmatrix}
-\frac{m-2}{s}\begin{pmatrix}a^2&ab\\ab&b^2\end{pmatrix}.
\]
A direct \(2\times2\) calculation yields
\[
\det T=2(mab+cs)>0,\quad
\operatorname{tr}(T^{-1})=\frac{a^2+b^2+mab+cs}{s(mab+cs)},\quad
(a,b)T^{-1}(a,b)^{\mathsf T}=\frac{s}{2}.
\]
Consequently \(J_{zz}=\frac{3(m-2)}{2s}+\operatorname{tr}(T^{-1})\), giving the expression above. These formulas are exact for every real \(a,b,c>0\), not a finite-size extrapolation.

Two-leaf pairs are strictly suboptimal for \(m\ge4\), since
\[
J_{zz}-J_{uv}=
\frac{2(a^2+b^2)+(m-4)[mab+cs]}{2s[mab+cs]}>0.
\]
The stronger hub's hub–leaf configuration crosses the hub pair at the claimed threshold, because
\[
J_{uz}-J_{uv}=
\frac{s(c_*-c)}{s[mab+b^2+cs]}=
\frac{c_*-c}{mab+b^2+cs}.
\]
For the other hub, the corresponding threshold is
\[
c_v=\frac{b^2-(m-2)ab+(m-1)a^2}{s}
=c_*+(m-2)(a-b)\ge c_*.
\]
Therefore when \(c<c_*\), neither hub–leaf type beats \(J_{uv}\). At \(c=c_*\), \(J_{vz}\) ties only if \(a=b\).

To decide the regime \(c>c_*\), subtract the two hub–leaf costs:
\[
J_{uz}-J_{vz}=
\frac{(a-b)P(c)}{[mab+b^2+cs][mab+a^2+cs]},
\quad P(c)=a^2+b^2+ab(m+2-m^2)-(m-1)cs.
\]
The affine function \(P\) is strictly decreasing. At the threshold, even if \(c_*\le0\), algebra gives
\[
P(c_*)=-(m-2)(a^2+2ab+mb^2)<0.
\]
Thus for \(c\ge c_*\), if \(a>b\) then \(J_{uz}<J_{vz}\); if \(a=b\), equality holds by hub symmetry. Together with the strict two-leaf exclusion, this proves all optimality, uniqueness, and tie statements, including the case \(c_*\le0\).

Finally let \(R=a/b\ge1\). Then \(c_*/b=[R^2-(m-2)R+(m-1)]/(R+1)\). Its quadratic numerator has discriminant \(m^2-8m+8\), negative for integers \(4\le m\le6\), positive for integers \(m\ge7\), and two roots exceeding one for the latter range. Hence exactly the stated closed interval makes \(c_*\le0\). This completes the proof.

## Verification
The accompanying Python 3 program `verify.py` uses only standard-library exact rational arithmetic. It constructs every weighted Laplacian from the edge list and computes the inverse trace through Gauss–Jordan elimination without floating-point approximations. It compares all four formulas against every unordered leader pair and verifies the predicted complete optimizer sets for 157 parameter configurations, including exact positive threshold ties, equal and unequal spoke conductances, and the always-hub–leaf regime. The recorded replay output is `VERIFY_OK configurations= 157  exact_pair_matrices= 5814  class_formula_checks= 5814  optimizer_checks= 157  leaf_exclusion_checks= 157`.

The executable checks support reproducibility but do not replace the algebraic proof of the infinite and continuous parameter assertions. The proof's critical strict signs follow from the displayed positive rational expressions.

## Relationship to prior work
Lin, Fardad and Jovanović (arXiv:1302.0450, first public 2013-02-03) formulate the noise-free leader problem using the same grounded inverse-trace objective and develop general convex-relaxation and greedy algorithms. Fitch and Leonard (arXiv:1407.1569, first public 2014-07-07) give an effective-resistance/joint-centrality characterization and explicitly solve path and cycle cases. Patterson, Yi and Zhang (arXiv:1708.06873, first public 2017-08-23) provide resistance formulas and specific path, cycle and tree results. The latter is a relevant *later* comparison, not a source used to date the focal pre-2016 research direction.

Those general formulations can numerically evaluate this graph. In the material inspected, they do not already give the weighted \(K_{1,1,m}\) complete optimum classification, the exclusion of leaf–leaf pairs for \(m\ge4\), the stronger-hub preference, or the positive-weight zero-threshold wedge. The present result depends on evaluating all symmetry classes and proving their rational inequalities, rather than merely citing the generic objective. Earlier accessible research on unweighted quadrilateral books, friendship graphs, and other complete split or multipartite cases has different graph structures and/or objectives and does not imply this weighted three-conductance result.

## Limitations
The theorem assumes identical spoke conductance within each hub's set of incident edges and exactly two noise-free leaders. It does not address independent edge-by-edge spoke heterogeneity, noisy leaders, other numbers of leaders, or directed networks. It does not claim a new general numerical optimization algorithm. Bibliographic comparison does not prove global uniqueness in the literature: an unindexed special-case result, another name for the graph, or a derivation embedded in broader joint-centrality work could still overlap. Independent mathematical and publication-priority verification is not claimed.

## References
1. Fu Lin, Makan Fardad and Mihailo R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public 2013-02-03), https://arxiv.org/abs/1302.0450 .
2. Katherine E. Fitch and Naomi Ehrich Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public 2014-07-07), https://arxiv.org/abs/1407.1569 .
3. Stacy Patterson, Yuhao Yi and Zhongzhi Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (first public 2017-08-23), https://arxiv.org/abs/1708.06873 .
