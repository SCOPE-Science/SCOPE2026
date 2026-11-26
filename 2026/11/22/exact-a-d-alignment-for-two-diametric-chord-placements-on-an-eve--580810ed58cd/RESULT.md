# Exact A–D alignment for two diametric chord placements on an even cycle

## Finding

Let \(C_{2m}\) denote the undirected cycle on vertices \(0,1,\ldots,2m-1\) with unit edge conductances. For an integer \(m\ge2\) choose two **distinct diameters** \(e_0=\{0,m\}\) and \(e_t=\{t,t+m\}\), \(1\le t<m\), also with unit conductance. Write \(G_{m,t}=C_{2m}+e_0+e_t\), and let \(x=t(m-t)\). Here \(\tau(G)\) is the number of spanning trees and \(K(G)=\sum_{u<v}R_{uv}(G)\) is the Kirchhoff index (total effective resistance).

Then the **exact two-objective design laws** are
\[
\tau(G_{m,t})=2m(m+1+x), \qquad
K(C_{2m})-K(G_{m,t})=\frac m6\frac{m(m^2+2)+(m^2+4)x+4x^2}{m+1+x}.
\]
Both the spanning-tree count and the reduction in total effective resistance increase **strictly** with \(x\ge0\). Consequently, within the entire family of pairs of distinct diameters, the optimizers of the two objectives are **identical**: exactly \(t=\lfloor m/2\rfloor\) or \(t=\lceil m/2\rceil\), with duplicate equivalent values counted only once. These choices place the four chord endpoints as evenly around the ring as the parity permits.

As \(m\to\infty\), a balanced choice gives a total-resistance improvement asymptotic to \(m^3/3\); adjacent diameters, \(t=1\), give \(m^3/6\). Thus balanced placement doubles the leading total-resistance improvement compared with two immediately adjacent diameters. The spanning-tree-count ratio between balanced and adjacent placement is asymptotic to \(m/8\).

## Assumptions and scope

All edges of both the base cycle and the two new chords have unit positive conductance. The vertex labels are modulo \(2m\). Each permitted chord spans **exactly** half the cycle, and each of the two chord pairs is distinct. The optimization is discrete over \(t\in\{1,\ldots,m-1\}\), not over arbitrary non-diametric chords, weighted chord lengths, or conductance budgets. The \(m=2\) case has a single feasible relative separation.

## Proof

Let \(L\) denote the Laplacian of the unit cycle, \(b_0=\mathbf e_0-\mathbf e_m\), and \(b_t=\mathbf e_t-\mathbf e_{t+m}\). On the zero-sum subspace \(\mathbf1^\perp\), \(L\) is invertible. Write \(U=[b_0,b_t]\) and \(P=L^+\). The unit-diameter dipole potential is explicitly
\[
(Pb_0)_j=\frac m4-\frac12\min\{j,2m-j\},\quad 0\le j<2m,
\]
which is verified by applying the cycle Laplacian and checking its zero mean. Write \(g=Pb_0\); its shift by \(t\) is \(Pb_t\) and \(g_{j+m}=-g_j\). Taking endpoint differences gives
\[
U^TPU=\begin{pmatrix}m/2&(m-2t)/2\\(m-2t)/2&m/2\end{pmatrix}.
\]
To compute the other matrix, put \(S_t=\sum_{j=0}^{2m-1}g_jg_{j-t}\), with indices taken modulo \(2m\). Summing squares gives \(S_0=m(m^2+2)/24\), and \(S_m=-S_0\). Since \(Lg=b_0\), for \(1\le t<m\) we have \(2S_t-S_{t-1}-S_{t+1}=g_t-g_{t+m}=(m-2t)/2\). The cubic \((m-2t)(m^2+2+2t(m-t))/24\) obeys this difference equation and these two endpoint values; uniqueness follows because the difference of two solutions has constant first difference and vanishes at both endpoints. Thus the Gram matrix of \(Pb_0,Pb_t\) is
\[
U^TP^2U=\begin{pmatrix}
 m(m^2+2)/24&(m-2t)(m^2+2+2x)/24\\
 (m-2t)(m^2+2+2x)/24&m(m^2+2)/24
\end{pmatrix}.
\]
These identities include \(t=1\) and both parity boundaries. The two-edge determinant factor is
\[
\det(I_2+U^TPU)=(1+m/2)^2-((m-2t)/2)^2=m+1+x.
\]
The matrix-tree theorem and the determinant lemma therefore imply \(\tau(G_{m,t})=\tau(C_{2m})\det(I_2+U^TPU)=2m(m+1+x)\).

For the resistance objective, \(K(G)=2m\operatorname{tr}(L_G^+)\). Apply the Woodbury identity on \(\mathbf1^\perp\) to \(L_G=L+UU^T\). This yields
\[
K(C_{2m})-K(G_{m,t})=2m\operatorname{tr}\big((I_2+U^TPU)^{-1}U^TP^2U\big).
\]
Substitution of the preceding \(2\times2\) matrices and collecting terms with \(x=t(m-t)\) gives the displayed closed rational formula.

Set \(F_m(x)=[m(m^2+2)+(m^2+4)x+4x^2]/(m+1+x)\). Its derivative is
\[
F_m'(x)=\frac{m^2+2m+4+8(m+1)x+4x^2}{(m+1+x)^2}>0
\]
for \(m\ge2\), \(x\ge0\). Strict increase and the discrete concavity of \(t(m-t)\) establish every equality case. Finally \(t=1\) gives \(x=m-1\), while balanced \(t\) gives \(x=m^2/4+O(1)\). Substitution proves the stated leading powers and constants.

## Verification

The included `check.py` independently constructs each augmented graph's integer Laplacian, computes its exact spanning-tree count by a rational Gaussian determinant, and derives its exact Kirchhoff index from a grounded Laplacian inverse. Every admissible \(t\) for \(2\le m\le9\) is checked against both closed formulas with exact fractions. The script also checks the two optimizer sets over this finite test range. These tests are illustrative and do not replace the preceding all-size proof.

## Relationship to prior work

Ghosh, Boyd and Saberi formulate total-effective-resistance minimization and give the Laplacian-pseudoinverse trace identity. Khosoussi, Sukhatme, Huang and Dissanayake formulate edge augmentation by maximizing weighted spanning-tree count and use the log-determinant objective. The present claim concerns their **joint** exact behavior on the explicitly restricted family of two distinct diameters of an even unit cycle. The general objective formulations do not themselves imply the displayed two-chord rational identity or its complete discrete equality classification without additional graph-specific calculation.

## Limitations

The theorem is deliberately confined to pairs of equal-weight **diametric** chords. It does **not** establish global optimality when arbitrary non-diametric chords are eligible, nor does it establish a general equivalence of A- and D-optimal network design. Although two published general frameworks and related indexed graph-design results were searched and compared, no literature search rules out all unindexed equivalent formulae. Independent expert audit and publication-priority assessment remain outstanding.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* 50(1), 37–66 (2008), doi:10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
2. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, “Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs,” arXiv:1604.01116, initially submitted 2016-04-05. https://arxiv.org/abs/1604.01116
