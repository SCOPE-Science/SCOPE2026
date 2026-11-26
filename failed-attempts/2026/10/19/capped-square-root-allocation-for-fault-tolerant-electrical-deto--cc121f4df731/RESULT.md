# Capped square-root allocation for fault-tolerant electrical detours on cactus networks

## Finding

Consider any finite connected bridgeless cactus graph, in which every edge belongs to exactly one simple cycle. Give every edge \(e\) a strictly positive price \(c_e\) and a freely chosen strictly positive conductance \(w_e\), under a linear budget \(\sum_e c_e w_e=B>0\). After the failure of an edge \(e=uv\), the effective resistance between its former endpoints is \(R_{uv}(G-e)\), with all surviving conductances unchanged. The robust design objective is

\[
\min_{w_e>0,\;\sum_e c_e w_e=B}\ \max_{e=uv\in E(G)}R_{uv}(G-e).
\]

The unique globally optimal design has the following closed form for **arbitrary heterogeneous positive prices**. Index the edge-disjoint cycles by \(C_1,\ldots,C_s\). For each cycle \(C_j\), let \(T_j\) be the unique positive solution of

\[
\sum_{e\in C_j}\left(1-\frac{c_e}{T_j}\right)_+=1,
\qquad (z)_+=\max\{z,0\},
\]

and put

\[
H_j=\sum_{e\in C_j}\sqrt{\max\{c_e,T_j\}}-\sqrt{T_j},
\quad S=\sum_{j=1}^s H_j^2.
\]

Then the exact optimal worst-failure resistance and every optimal edge conductance are

\[
\boxed{D_*=\frac{S}{B}},\qquad
\boxed{w_e^*=\frac{BH_j}{S\sqrt{\max\{c_e,T_j\}}}\quad(e\in C_j).}
\]

Every cycle contributes the same worst detour resistance \(D_*\), and the expenditure on a cycle is exactly \(BH_j^2/S\). The solution is unique, even if the graph or prices have no symmetry.

In particular, for a single \(n\)-cycle, \(n\ge3\), whose edges have prices \(1,\ldots,1,t\), all optimal conductances are equal throughout the nontrivial price interval

\[
0<t\le\frac{n-1}{n-2}.
\]

When \(t>(n-1)/(n-2)\), the exceptional edge instead has strictly smaller conductance, with the optimal resistance level

\[
D_* = \frac{\bigl(\sqrt{(n-1)(n-2)}+\sqrt{t}\bigr)^2}{B}.
\]

Below and at the threshold, \(D_*=(n-1)(n-1+t)/B\). Thus an initially higher-priced link can retain the same optimal conductance as cheaper links until a sharp cost threshold is crossed.

## Assumptions and scope

The graph is finite, connected, undirected, and bridgeless; all its blocks are simple cycles. Different cycles may meet at articulation vertices but share no edge. Each original edge can fail individually. Only the resistance between the *endpoints of the failed edge* is measured; this is not a maximum over all vertex pairs or a total Kirchhoff index. Conductances and budget are strictly positive. No conductances are readjusted after failure. The price coefficients \(c_e\) are arbitrary strictly positive real numbers. The budget is linear in conductances. Trees with bridges are excluded: deleting a bridge disconnects its endpoints and gives infinite resistance. The theorem makes no claim for graphs whose cycles overlap in edges, simultaneous failures, nonlinear prices, or different robustness objectives.

The threshold equation is explicitly computable: sort the prices on a cycle, \(c_{(1)}\le\cdots\le c_{(n)}\). Choose any \(k\in\{2,\ldots,n\}\) for which

\[
c_{(k)}\le T=\frac{\sum_{i=1}^k c_{(i)}}{k-1}\le c_{(k+1)},
\]

with \(c_{(n+1)}=+\infty\). Such a \(k\) exists, and the resulting \(T\) is unique. Equalities in the ordering do not change the solution. At least two prices are strictly below \(T\).

## Proof

**1. Electrical reduction.** Let \(e=uv\) lie on cycle \(C_j\). Deleting \(e\) leaves one simple alternative path from \(u\) to \(v\), namely \(C_j\setminus\{e\}\). Every other cycle is connected to this path, if at all, through a cut vertex. Kirchhoff's node law implies that no current enters any such pendant component under a unit current injection at \(u\) and extraction at \(v\). Hence the replacement-path electrical resistance is exactly

\[
R_{uv}(G-e)=\sum_{f\in C_j\setminus\{e\}}\frac1{w_f}.
\]

Thus the complete objective is the maximum, over cycles, of these local detour sums.

**2. A one-cycle unit-detour expenditure problem.** Fix a cycle of length \(n\ge3\) with prices \(c_i>0\), and write its edge resistances \(r_i=1/w_i>0\). Minimize

\[
F(r)=\sum_{i=1}^n\frac{c_i}{r_i}
\quad\text{subject to}\quad
\sum_{j\ne i}r_j\le1\quad(1\le i\le n).
\]

The objective is strictly convex on the positive orthant; the feasible linear inequalities admit a strictly feasible positive point. Define \(T\) by the stated scalar threshold equation. To prove existence and uniqueness, note that \(\sum_i(1-c_i/T)_+\) is continuous and strictly increasing from zero to \(n\) once \(T\) exceeds the smallest price; because \(n\ge3\), it crosses one exactly once. Its value can reach one only when at least two terms are positive. Put \(q_i=\sqrt{\max\{c_i,T\}}\) and \(H=\sum_iq_i-\sqrt T\). Define

\[
r_i^*=\frac{q_i}{H},\qquad
\nu_i=H^2\left(1-\frac{c_i}{T}\right)_+.
\]

Because \(q_i\ge\sqrt T\), \(\sum_{j\ne i}r_j^*\le1\), with equality exactly for \(c_i\le T\). The multipliers are nonnegative and complementary. Since \(\sum_i\nu_i=H^2\), stationarity for every edge is

\[
\frac{c_i}{(r_i^*)^2}
=H^2\frac{c_i}{\max\{c_i,T\}}
=\sum_{j\ne i}\nu_j.
\]

These are precisely the Karush–Kuhn–Tucker equations of the strictly convex optimization problem, with its affine constraints and Slater point; hence \(r^*\) is its unique global minimizer. Moreover, the threshold identity implies

\[
\sum_{i:c_i<T}c_i=(k-1)T,
\quad k=|\{i:c_i<T\}|,
\]

so

\[
\sum_i\frac{c_i}{q_i}
=(k-1)\sqrt T+\sum_{i:c_i\ge T}\sqrt{c_i}
=H.
\]

Therefore the minimum expenditure under unit worst-detour bound is \(F(r^*)=H^2\). By homogeneous scaling, imposing worst detour \(\le d\) instead gives the unique minimum expenditure \(H^2/d\), attained at \(r_i=dq_i/H\), or conductance \(w_i=H/(dq_i)\).

**3. Global optimum and uniqueness.** For any feasible design whose global worst detour is \(d>0\), the expenditure on cycle \(j\) is at least \(H_j^2/d\). The cycles partition the edges, so

\[
B=\sum_e c_ew_e\ge\sum_{j=1}^s\frac{H_j^2}{d}=\frac{S}{d}.
\]

Consequently \(d\ge S/B\). Taking \(d=S/B\), and on each cycle taking its unique minimum-expenditure allocation from step 2, attains the bound with total budget exactly \(B\). This yields the asserted conductance formula. Equality in the budget bound forces equality for every cycle and therefore its unique one-cycle solution: the global optimizer is unique. Because at least two edges on each cycle satisfy \(c_e<T_j\), at least one failed edge in every cycle attains detour \(d\).

**4. A sharp equal-conductance interval.** On an \(n\)-cycle with prices \(1\) on \(n-1\) edges and \(t\) on one edge, every edge has \(c_i\le T\) precisely when \(t\le(n-1)/(n-2)\). In that regime \(T=(n-1+t)/(n-1)\), so all \(q_i=\sqrt T\) and the unique allocation is equal conductance \(B/(n-1+t)\). Above this regime the exceptional edge has \(c_i=t>T=(n-1)/(n-2)\), while the others have \(c_i<T\), yielding the two displayed optimal-value formulas. The formulas agree at the threshold.

## Verification

The companion self-contained program `verification.py` reconstructs explicit cactus Laplacians, deletes every edge and independently calculates failed-endpoint effective resistances using a grounded rank-one correction. It also solves the normalized one-cycle convex problem independently using numerical constrained optimization, compares arbitrary asymmetric competitors, and checks threshold equations and budgets for heterogeneous prices. The program passed 945 checks when run with Python, NumPy, SciPy and NetworkX. These finite checks are not a substitute for the general convex/KKT proof above. Run: `python verification.py`.

## Relationship to prior work

Ghosh, Boyd and Saberi [1] develop the convex optimization of total and maximum effective resistance on fixed networks. Their maximum effective resistance concerns intact-network node pairs, rather than the post-deletion detour between each failed edge's endpoints; it therefore does not yield the capped square-root or cactus-budget allocation formulas above. Johnson and Chertkov [2] study general worst-single-line-failure network design, a closer robust-optimization formulation; their investigated objectives involve power-flow dissipation, and the inspected formulation does not provide these exact cactus formulas or the equal-conductance pricing threshold. Suliman and Weinstein [3] optimize maximum effective resistance on intact edges via Lewis weights, a different resistance functional; the present criterion requires removal of the edge before resistance is measured. These general references motivate the gap without implying that a failed bibliographic search proves novelty.

## Limitations

The result does not address overlapping cycles, bridges, failure of multiple edges, or all-pairs post-outage resistance. The formulas are proven only for a linear sum of conductance prices and strictly positive conductances; no physical interpretation of prices beyond this optimization model is assumed. Originality remains subject to possible equivalent results under replacement-path design, electrical-network robustness or convex resource allocation terminology, including unindexed literature.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66 (2008), doi:10.1137/050645452. Open manuscript: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf .
2. J. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285, first submitted 13 April 2010. https://arxiv.org/abs/1004.2285 .
3. M. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966, 2023. https://arxiv.org/abs/2302.05966 .
