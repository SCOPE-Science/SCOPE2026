# Exact hub-abandonment threshold for noise-free leaders on friendship graphs

## Finding

Let \(F_m=K_1\vee(mK_2)\), the simple unweighted friendship graph with one common hub and \(m\ge2\) triangular petals. With exactly \(1\le k\le2m\) noise-free leaders, minimize the unnormalized grounded-Laplacian inverse trace
\[
J(S)=\operatorname{tr}\big(L_{V\setminus S,V\setminus S}^{-1}\big),\qquad |S|=k.
\]
Define \(T=2m+1\). Every globally optimal leader set is characterized as follows.

* **Hub regime:** If \(3k<T\), every optimum contains the hub and chooses exactly one outer vertex from each of \(k-1\) distinct petals; no other vertices are selected. Its objective is \(J_*=(8m-5k+5)/6\), and there are exactly \(\binom{m}{k-1}2^{k-1}\) such sets.
* **Threshold:** If \(3k=T\), both the preceding hub pattern and the following hub-free pattern are optimal, and no others are. This tie is possible exactly when \(m\equiv1\pmod3\) (with \(m\ge4\)); the objective is \((8m-5k+5)/6\). The number of optima is \(\binom{m}{k-1}2^{k-1}+\binom{m}{k}2^k\).
* **Hub-free regime:** If \(3k>T\), no optimum contains the hub. For \(k\le m\), choose one outer vertex in each of \(k\) distinct petals. For \(m\le k\le2m\), select both outer vertices from \(k-m\) petals and one outer vertex from each remaining petal. For \(k\le m\) the optimal objective and number of sets are
\[
J_* = \frac{8m-5k-7}{6}+\frac{4m+2}{3k},\qquad N_* =\binom{m}{k}2^k.
\]
For \(m\le k\le2m\) they are
\[
J_* = \frac{2m-k}{2}+\frac{2m-k+4}{2(2m+k)},\qquad N_* =\binom{m}{2m-k}2^{2m-k}.
\]
The two formulas agree at \(k=m\). All characterizations are up to independent interchanges of the two vertices within each petal and permutations of the petals.

For example, on \(F_5\), every optimal three-leader set contains the hub, but every optimal four-leader set excludes it. Thus no optimal three-leader set is a subset of any optimal four-leader set.

## Assumptions and scope

Edges have unit conductance. The hub is adjacent to both vertices in each of \(m\) disjoint outer pairs, and the vertices within each pair are adjacent. Leaders are perfectly pinned, followers experience identical independent unit-intensity state disturbances, and the performance objective is the trace above, with no extra factor of \(1/2\). The claim quantifies over every integer \(m\ge2\), every integer \(k\) satisfying \(1\le k\le2m\), and every \(k\)-subset of vertices. For any nonempty leader set on this connected graph, the grounded matrix is positive definite.

## Proof

Write \(h\in\{0,1\}\) for whether the hub is selected. Let \(t_j\) denote the number of triangular petals containing exactly \(j\) selected outer vertices, for \(j=0,1,2\). Then
\[
t_0+t_1+t_2=m,\qquad h+t_1+2t_2=k.
\]
Every leader set has such a profile; all sets with the same profile have identical objective by graph symmetry.

**1. Exact objective for arbitrary profiles.** If the hub is selected, a petal with two followers contributes the inverse trace of \(\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix}\), namely \(4/3\); a petal with one follower contributes \(1/2\). Petals with no followers contribute zero. Thus
\[
J_1(t_0,t_1,t_2)=\frac43t_0+\frac12t_1.
\]
If the hub remains a follower, write the grounded matrix as \(\begin{psmallmatrix}2m&-u^T\\-u&D\end{psmallmatrix}\). Here \(D\) is block diagonal, containing \(t_0\) copies of \(\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix}\) and \(t_1\) copies of \((2)\); \(u\) is the vector of ones on all remaining outer vertices. The corresponding block identities are
\[
\operatorname{tr}(D^{-1})=\frac43t_0+\frac12t_1,\quad
u=u^TD^{-1}u=2t_0+\frac12t_1,\quad
u_2=u^TD^{-2}u=2t_0+\frac14t_1.
\]
The Schur complement is \(s=2m-\nu=\frac32t_1+2t_2>0\), because \(k\ge1\) and \(h=0\) require at least one selected outer vertex. The block inverse formula gives the exact trace
\[
J_0(t_0,t_1,t_2)=\frac43t_0+\frac12t_1+\frac{1+2t_0+t_1/4}{\frac32t_1+2t_2}.
\]

**2. Best profile with the hub present.** At fixed \(k\), replacing a completely selected petal and an empty petal by two singly selected petals preserves leader count and changes the trace from \(4/3\) to \(1\), a strict reduction of \(1/3\). Consequently the unique minimizing count profile has \(t_1=k-1,t_2=0\) if \(k-1\le m\), and \(t_0=0,t_1=2m-k+1\) otherwise. The corresponding values are
\[
H_{m,k}=\begin{cases}
\dfrac{8m-5k+5}{6},&1\le k\le m+1,\\[3pt]
\dfrac{2m-k+1}{2},&m+1\le k\le2m.
\end{cases}
\]
Both branches agree at \(k=m+1\).

**3. Best profile without the hub.** Eliminating \(t_0,t_2\) using the count constraints yields
\[
J_0=\frac{4m}{3}-\frac{2k}{3}-\frac{t_1}{6}+
\frac{1+2m-k-3t_1/4}{k+t_1/2}.
\]
At fixed positive \(m,k\) the derivative with respect to real \(t_1\), wherever the denominator is positive, is
\[
\frac{\partial J_0}{\partial t_1}=-\frac16-
\frac{m+1/2+k/4}{(k+t_1/2)^2}<0.
\]
The maximum feasible integral \(t_1\), respecting parity, is \(\min\{k,2m-k\}\). Thus the hub-free optimum uses one selected vertex per chosen petal until every petal is touched, then fills additional petals. Substitution yields exactly the two stated hub-free formulas.

**4. Exact comparison.** When \(1\le k\le m\), subtraction gives
\[
J_{\mathrm{out}}-H_{m,k}=\frac{4m+2-6k}{3k}.
\]
Its sign is positive, zero, or negative exactly as \(3k\) is below, equal to, or above \(2m+1\). For \(m+1\le k\le2m\), subtraction gives
\[
J_{\mathrm{out}}-H_{m,k}=\frac{2-k}{2m+k}<0
\]
since \(m\ge2\). This establishes the claimed sharp regime partition. Strictness of the exchange and derivative arguments excludes every other profile; the binomial counts follow by selecting petals and one of two vertices in each partially selected petal. At the tie, the two types of optimal sets are disjoint because exactly one type contains the hub. The strict nonnesting example follows immediately.

## Verification

Run `python verify_friendship.py` with Python 3 and no third-party dependencies. The program independently forms every grounded matrix, uses exact `fractions.Fraction` Gauss–Jordan inversion, compares with the arbitrary-profile Schur formula, and checks all optimal sets and counts for \(2\le m\le5\) and every \(1\le k\le2m\). It additionally enumerates all admissible count profiles for \(2\le m\le31\) and checks the minimizing profile, objective and boundary. Completed checks: 2,712 exact grounded-matrix comparisons, 28 exhaustive leader budgets, 11,900 exact count-profile checks and one nonnesting witness. These finite tests verify implementations and small instances; the proof above, not finite enumeration, establishes the full infinite family.

## Relationship to prior work

The noise-free leader-selection criterion \(\operatorname{tr}(L_{FF}^{-1})\) and the general possibility of nonnested optimal leader sets were developed in the earlier optimization and joint-centrality literature. The present result derives a closed-form global optimizer for **every** budget on the friendship graph, with a specific hub-abandonment threshold and a count of all optimal sets. Existing path/cycle special cases and general semidefinite relaxations do not give this classification. Other studies address windmill-type consensus coherence; see the limitations concerning incomplete full-text comparison.

## Limitations

The theorem is only for simple, unweighted friendship graphs, perfectly pinned leaders, and the exact grounded inverse-trace objective. It does not cover general windmills with larger clique petals, weighted edges, noisy leader measurements, directed graphs, or arbitrary dynamic controllers. The exact mathematical claim has been self-checked with a standalone exact-arithmetic program but has not received independent mathematical validation. A closely related 2020 windmill-coherence paper was identifiable by its abstract but not available in full text; this creates a genuine residual publication-priority risk, rather than evidence that its contents do not cover the theorem.

## References

1. M. Fardad, F. Lin and M. R. Jovanović, "Algorithms for Leader Selection in Large Dynamical Networks: Noise-Free Leaders," IEEE CDC-ECC (2011), https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/2266.pdf.
2. K. E. Fitch and N. E. Leonard, "Joint Centrality Distinguishes Optimal Leaders in Noisy Networks," first public arXiv version July 7, 2014, https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon and K. Dyagilev, "Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations," first public arXiv version December 20, 2014, https://arxiv.org/abs/1412.6595.
4. W. Sun, Y. Li and S. Liu, "Noisy consensus dynamics in windmill-type graphs," *Chaos* 30 (2020), 123131, https://doi.org/10.1063/5.0020696. Full text not inspected; bibliographic abstract inspected.
