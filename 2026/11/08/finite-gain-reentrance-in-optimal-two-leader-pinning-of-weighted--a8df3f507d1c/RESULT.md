# Finite-gain reentrance in optimal two-leader pinning of weighted friendship networks

## Finding

Let \(m\ge2\) be an integer. Consider the weighted friendship network \(F_m\) consisting of \(m\) edge-disjoint triangles sharing one hub. Each hub-to-outer edge has conductance \(1\), and each edge joining the two outer vertices within one triangle has conductance \(r>0\). Exactly two distinct vertices receive equal finite pinning gain \(k>0\). Among all two-vertex sets \(S\), minimize the **unscaled** inverse trace
\[
J(S)=\operatorname{tr}\left[(L+k\operatorname{diag}(\mathbf1_S))^{-1}\right],
\]
where \(L\) is the weighted graph Laplacian.

Denote by **H** a hub–outer pair, by **D** two outer vertices in different triangles, and by **S** two outer vertices in the same triangle. Every S-pair is strictly worse than every D-pair (when compared at fixed parameters). Define
\[
\begin{aligned}
P_2(k,r)&=(k^2+1)+(-k^2-8k+1)r-(5k^2+26k+8)r^2-(k+6)(3k+2)r^3,\\
P_3(k,r)&=(3k^2+4k+3)+(5k^2+8k+11)r+(k-4)(k-2)r^2-(k^2+12k+4)r^3.
\end{aligned}
\]
For each \(m\in\{2,3\}\) and every \(k>0\), the polynomial \(P_m(k,\cdot)\) has exactly one positive root \(r_m(k)\). If \(0<r<r_m(k)\), precisely the \(2m\) H-pairs minimize \(J\); if \(r>r_m(k)\), precisely the \(2m(m-1)\) D-pairs minimize it. At equality both classes (a total of \(2m^2\) sets) minimize \(J\). For **every** \(m\ge4\), only the \(2m\) H-pairs minimize \(J\), for all \(k,r>0\).

The optimal placement can be *reentrant* as a function of the pinning gain. At \(m=2\) and \(r=1/4\), H is optimal for
\[
0<k<\frac{126-24\sqrt{26}}{25}\quad\text{or}\quad k>\frac{126+24\sqrt{26}}{25},
\]
whereas D is optimal strictly between these two bounds. Each equality gives a tie.

## Assumptions and scope

The graph has \(2m+1\) vertices: a unique hub and \(m\) unordered pairs of outer vertices. No other edges exist. The conductances are positive, the hub-to-outer value is normalized to \(1\), both selected pinning gains are \(k\), and noise acts with equal unit intensity at every vertex. The objective is the full inverse trace, including both pinned vertices; the corresponding steady-state variance is one half of it. All parameters \(m,r,k\) are unrestricted within the stated domain. No claim concerns unequal pin gains, different triangle weights, or more than two leaders.

## Proof

The automorphism group gives exactly three unordered two-vertex-set orbits: H, D, S. The pinned Laplacian is positive definite because the graph is connected and the diagonal pinning is nonzero.

Order the hub first and group each triangle's two outer vertices into a module. For \(i,j\in\{0,1\}\), a module with gains \(ik,jk\) has block
\[
A_{ij}=\begin{pmatrix}1+r+ik&-r\\-r&1+r+jk\end{pmatrix}.
\]
Write \(t(A)=\operatorname{tr}(A^{-1})\), \(b(A)=\mathbf1^\top A^{-1}\mathbf1\), and \(c(A)=\mathbf1^\top A^{-2}\mathbf1\), with \(\mathbf1=(1,1)^\top\). Let \(A_0=A_{00}\), \(A_1=A_{10}\), and \(A_2=A_{11}\). Direct \(2\)-by-\(2\) inversion yields
\[
\begin{array}{c|ccc}
& t&b&c\\ \hline
A_0&2(1+r)/(1+2r)&2&2\\
A_1&(2+2r+k)/d&(2+4r+k)/d&((1+2r)^2+(1+2r+k)^2)/d^2\\
A_2&2(1+r+k)/((1+k)(1+k+2r))&2/(1+k)&2/(1+k)^2
\end{array}
\]
where \(d=1+2r+k(1+r)\). If the hub has pin indicator \(h\in\{0,1\}\), Schur-complement inversion gives
\[
J=\sum_\nu t(A_\nu)+\frac{1+\sum_\nu c(A_\nu)}{2m+kh-\sum_\nu b(A_\nu)}.
\]
The denominator is strictly positive, being the Schur complement of a positive-definite pinned Laplacian. Consequently, the three exact objectives \(J_H,J_D,J_S\) arise respectively from \((h;A_1,A_0^{m-1})=(1;A_1,A_0^{m-1})\), \((0;A_1,A_1,A_0^{m-2})\), and \((0;A_2,A_0^{m-1})\). This identity is also a closed exact formula for the minimum in every regime by taking the stated optimum class.

Simplifying these three rational functions gives
\[
J_D-J_H=\frac{P_m(k,r)}{2(1+2r)[k(1+r)+2r+1][k(1+r)+4r+2]},
\]
where
\[
\begin{aligned}
P_m(k,r)&=P_4(k,r)+2(m-4)(1+r)[k(1+r)+2r+1]^2,\\
P_4(k,r)&=(k-2)^2r^3+(7k^2+14k+24)r^2\\
&\quad +(11k^2+24k+21)r+(5k^2+8k+5).
\end{aligned}
\]
Substitution of \(m=2,3\) yields exactly the polynomials in the Finding. Since \(P_4>0\) and the increment in \(m\) is strictly positive, \(J_D>J_H\) for all \(m\ge4\).

The remaining pair comparison is
\[
J_S-J_D=\frac{r\,Q_m(k,r)}{2(1+2r)(k+2r+1)[k(1+r)+2r+1]},
\]
with
\[
\begin{aligned}
Q_m={}&2k^2mr+2k^2m+5k^2r+3k^2\\
&+4kmr^2+10kmr+4km+10kr^2+17kr+6k\\
&+8mr^2+8mr+2m+4r^2+4r+1.
\end{aligned}
\]
Every summand of \(Q_m\) is strictly positive. Thus S never minimizes. For \(m=2\), the coefficients of \(P_2\) in descending powers of \(r\) have signs \((-,-,\pm,+)\), and for \(m=3\), those of \(P_3\) have signs \((-,\pm,+,+)\), after deleting any zero coefficient. In both cases Descartes' rule gives exactly one positive root because there is one sign change, and continuity and the opposite signs at \(r=0\) and \(r\to\infty\) prove existence. The sign on each side of that simple root gives the optimizer classes and strictness.

Finally, direct substitution yields \(P_2(k,1/4)=(25k^2-252k+36)/64\), with two distinct positive roots displayed above and positive leading coefficient. This proves the double switch in the optimal placement. Orbit sizes are \(2m\), \(4\binom m2=2m(m-1)\), and \(m\), giving all stated counts.

## Verification

The companion `verification.py` rederives the module formulas symbolically and checks the rational comparison identities, positive coefficients of \(Q_m\), the dependence of \(P_m\) on \(m\), and the reentrance polynomial. It independently builds all pinned Laplacians for \(m=2,\ldots,6\) over an exact-rational grid of positive \(r,k\), and compares their inverse traces against the three formulas. In addition, it checks every unordered leader pair on representative instances at \(m=2,3,4\). All 300 direct representatives and 268 exhaustive pair comparisons passed. No finite test is used as a substitute for the algebraic proof for arbitrary real parameters and all \(m\).

Reproduce by extracting the accompanying file and running `python verification.py` with SymPy installed. The script needs no network access.

## Relationship to prior work

Lin, Fardad, and Jovanović formulated finite-gain (noise-corrupted) leader selection as inverse-trace minimization and developed numerical optimization algorithms. Fitch and Leonard developed two-leader joint-centrality formulas and solved special path and cycle families. Those general statements furnish the underlying objective but do not state or directly evaluate the weighted friendship-graph orbit comparisons, the integer-size cutoff at four petals, or the finite-gain reentrance. The equal-edge, infinite-gain specialization is mathematically much narrower and does not imply the present two-parameter finite-gain classification. The computations and proof are self-contained; literature coverage is not a theorem of novelty.

## Limitations

Only identical hub conductances, identical within-triangle conductances, and equal positive finite gains are treated. The result concerns the inverse-trace criterion, not peak variance or a transient performance objective. The gain-reentrance example is specific to two petals, and no behavior is claimed beyond this model. An equivalent result may exist in unindexed or inaccessible literature. No independent audit has been performed.

## References

- F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public version 2013-02-03), https://arxiv.org/abs/1302.0450.
- K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public version 2014-07-07), https://arxiv.org/abs/1407.1569.
- F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Large Dynamical Networks: Noise-Corrupted Leaders*, IEEE CDC-ECC 2011, doi:10.1109/CDC.2011.6161507, https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/2304.pdf.
