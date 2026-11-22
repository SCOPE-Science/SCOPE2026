# Sharp extinction-control budgets on bidirectionally dispersing habitat networks

## Finding

**Theorem (edgewise extinction-budget bound and its exactness boundary).** Consider a finite connected habitat network with \(n\ge 2\) patches. Each undirected edge \(\{i,j\}\) permits positive migration in both directions, at rates \(m_{ij}>0\) from \(i\) to \(j\) and \(m_{ji}>0\) from \(j\) to \(i\). All patches have the same intrinsic per-capita growth \(r>0\), arbitrary crowding coefficients \(c_i>0\), and independently chosen constant harvesting mortalities \(h_i\ge 0\). Let \(H=\sum_i h_i\). The smallest \(H\) guaranteeing extinction from **every nonnegative initial population** satisfies

\[
 H_{\min}\ge nr-\sum_{\{i,j\}\in E}(\sqrt{m_{ij}}-\sqrt{m_{ji}})^2.
\]

Equality is possible **if and only if** the directional edge ratios are cycle-consistent and the numbers

\[
 h_i^*=r+\sum_{j\sim i}\sqrt{m_{ij}m_{ji}}-\sum_{j\sim i}m_{ij}
\]

are nonnegative for every patch. In that event \(h^*\) is the **unique** minimizing control, and extinction holds even though the linearized Perron eigenvalue equals zero. Cycle consistency means that, on every directed traversal of an undirected cycle, the product of forward/backward migration-rate ratios equals one.

Every bidirectionally dispersing **tree** automatically satisfies cycle consistency. In particular, put

\[
 r_c=\max_i\left(\sum_{j\sim i}m_{ij}-\sum_{j\sim i}\sqrt{m_{ij}m_{ji}}\right).
\]

For every \(r\ge r_c\) with \(r>0\), the displayed exact cost and unique allocation hold on the tree. On a tree with unequal migration directions the minimum is strictly below the uniformly spread control cost \(nr\).

**Complete two-patch low-growth boundary.** Suppose the migration rate from patch 1 to patch 2 is \(a>0\), and the reverse rate is \(b>0\). Define \(q=\sqrt{ab}\) and \(r_c=\max(a,b)-q\). If \(r\ge r_c\), the unique optimum is

\[
(h_1,h_2)=(r+q-a,\,r+q-b),\qquad H_{\min}=2r-(\sqrt a-\sqrt b)^2.
\]

If \(a>b\) and \(0<r<r_c\), the unique optimum is \(h_1=0\) and

\[
 h_2=H_{\min}=\frac{r(a+b-r)}{a-r}.
\]

If \(b>a\), swap the patch labels and \(a,b\) in the last formula. Thus there is a sharp switch from harvesting only the net downstream patch at low growth to harvesting both patches at higher growth.

**A circulation obstruction.** On three patches arranged in a cycle with clockwise migration rate \(a>0\) and counterclockwise rate \(b>0\) on each edge, the unique minimum is \(H_{\min}=3r\), attained by \(h_1=h_2=h_3=r\), for every \(r>0\). For \(a\ne b\), this exceeds the edgewise bound by precisely \(3(\sqrt a-\sqrt b)^2\). Circulation can therefore destroy the directional-dispersal saving possible on trees; ignoring cycle consistency would produce a false prediction.

## Assumptions and scope

The nonlinear population model is the conservative-migration logistic metapopulation system

\[
 \dot u_i=u_i(r-h_i-c_i u_i)+\sum_{j\sim i}\bigl(m_{ji}u_j-m_{ij}u_i\bigr),
 \qquad i=1,\dots,n.
\]

All migration rates along an existing edge are strictly positive in both directions; absent edges have no migration; the undirected support is connected. Harvesting is a **constant additional per-capita mortality**, not quota extraction or time-dependent control. The optimization is over nonnegative rates \(h_i\) with an equal unit cost per unit rate. Extinction means \(u_i(t)\to0\) for every patch and every initially nonnegative population vector. Crowding parameters are arbitrary positive numbers and do not enter the optimal cost, although they affect the transient dynamics.

The displayed edgewise lower bound may be negative at very small growth and is only informative as an exact budget in its stated feasibility regime. The separate two-patch formulas handle all strictly positive growth rates. No uniqueness claim is made for optimal controls outside the equality regime on general cyclic networks.

## Proof

**1. Nonlinear extinction criterion, including equality.** Define the column-conservative migration matrix \(A\) by \(A_{ji}=m_{ij}\) when \(i\ne j\), and \(A_{ii}=-\sum_{j\sim i}m_{ij}\). Let \(B=A+rI-\operatorname{diag}(h)\). Since \(B\) is an irreducible Metzler matrix, its spectral abscissa \(s(B)\) is a simple real eigenvalue with positive left and right eigenvectors. If \(s(B)\le0\), choose a positive left Perron vector \(w\), let \(V=\sum_iw_i u_i\), and use the nonlinear equations to obtain

\[
 \dot V=s(B)V-\sum_i w_ic_i u_i^2
 \le-\frac{\min_i c_i}{\sum_iw_i}V^2.
\]

The last inequality is weighted Cauchy–Schwarz. Positivity invariance and the usual logistic comparison give global nonnegative solutions. The differential inequality shows \(V(t)\to0\) even at \(s(B)=0\), hence all populations vanish. Conversely, if \(s(B)>0\), a small multiple of the positive right Perron vector is a strict positive subsolution, while a sufficiently large constant vector is a supersolution, because the negative quadratic terms dominate. Standard monotone cooperative-system arguments give a strictly positive equilibrium. Thus not every positive initial population becomes extinct. Consequently, extinction from all nonnegative initial states is equivalent to \(s(B)\le0\).

**2. The universal edgewise bound.** For any admissible extinction control, take the positive right Perron eigenvector \(v\) and write \(s=s(B)\le0\). The eigenvector equation gives, for every patch,

\[
 h_i=r+\frac{(Av)_i}{v_i}-s.
\]

Summing and grouping the contribution of each undirected edge yields the *exact identity*

\[
 H=nr-ns+\sum_{\{i,j\}\in E}
 \left(m_{ij}\frac{v_i}{v_j}+m_{ji}\frac{v_j}{v_i}-m_{ij}-m_{ji}\right).
\]

AM–GM on each positive pair gives

\[
 m_{ij}\frac{v_i}{v_j}+m_{ji}\frac{v_j}{v_i}
 \ge2\sqrt{m_{ij}m_{ji}}.
\]

Since \(-ns\ge0\), the asserted bound follows. Equality demands \(s=0\) and, on every edge, \(v_j/v_i=\sqrt{m_{ij}/m_{ji}}\). Such positive ratios exist globally precisely when their products around all cycles equal one. When they exist, substituting into \(h_i=r+(Av)_i/v_i\) yields exactly \(h_i^*\). If all \(h_i^*\ge0\), this control makes \(Bv=0\), hence \(s(B)=0\) by positive Perron–Frobenius theory. Step 1 proves extinction, so the bound is achieved. Every equality control has the same edgewise ratios, hence the same \(v\) up to scale and the same \(h^*\), proving uniqueness.

If cycle consistency fails, the lower bound is **strictly** below the true optimal budget, rather than merely unattained at any particular control. Indeed, fix one coordinate of \(y_i=\log v_i\) to zero. The sum of the edgewise terms is a strictly convex and coercive function of the remaining connected-network coordinates, because each edge contributes a positive combination of exponentials of its coordinate difference. It has a unique finite minimizer. If the cycle ratios are inconsistent, no single \(v\) minimizes every edge term; hence the sum's minimum has a positive gap above the AM–GM lower bound. The same coercivity and the Perron identity rule out approaching equality when cycle consistency holds but a requisite \(h_i^*\) is negative.

**3. Trees and their sharp growth boundary.** A tree has a unique undirected path between any two vertices, so the desired ratios \(v_j/v_i=\sqrt{m_{ij}/m_{ji}}\) define a consistent positive vector recursively from any root. The nonnegativity constraints on \(h_i^*\) are exactly \(r\ge r_c\), giving the tree formula and unique optimum. For at least one unequal edge, \((\sqrt{m_{ij}}-\sqrt{m_{ji}})^2>0\), so its optimum is strictly cheaper than the homogeneous choice \(h_i=r\), which always works since \(s(A)=0\).

**4. Two patches, including the boundary regime.** An optimum has \(s=0\): if it had \(s<0\), continuity and strict monotonicity of the spectral abscissa in any positive harvesting coordinate would allow some positive harvesting rate to be reduced while retaining extinction. Write \(t=v_2/v_1>0\). The two boundary-control equations are

\[
 h_1=r-a+bt,\qquad h_2=r-b+a/t,
 \qquad H=2r-a-b+bt+a/t.
\]

The strictly convex-in-log function \(bt+a/t\) has its unique unconstrained minimum at \(t=\sqrt{a/b}\). This value obeys \(h_1,h_2\ge0\) exactly when \(r\ge\max(a,b)-\sqrt{ab}\). Otherwise the larger outgoing-rate patch must have zero harvesting; for \(a>b\), the admissible minimizer is \(t=(a-r)/b>\sqrt{a/b}\), so \(h_1=0\) and \(h_2=r(a+b-r)/(a-r)\). The swapped case follows symmetrically. Strictness of the scalar minimization proves uniqueness throughout.

**5. The biased three-cycle.** Orient each of three edges clockwise with rate \(a\) and counterclockwise with rate \(b\). For any Perron vector, let \(d_i=\log(v_i/v_{i+1})\), cyclically indexed, so \(\sum_i d_i=0\). The edge sum in Step 2 is

\[
 \sum_{i=1}^3\bigl(ae^{d_i}+be^{-d_i}-a-b\bigr)\ge0
\]

by Jensen's inequality, with equality only when all \(d_i=0\). Thus every extinction control has \(H\ge3r\), and equality uniquely requires \(v\) constant and \(h_i=r\). This control has \(B=A\) and \(s(A)=0\); Step 1 establishes nonlinear extinction. The edgewise AM–GM lower bound is \(3r-3(\sqrt a-\sqrt b)^2\), completing the circulation comparison.

## Verification

An exact rational three-patch example has migration rates \(m_{12}=9\), \(m_{21}=1\), \(m_{23}=4\), \(m_{32}=1\), and intrinsic growth \(r=7\). The optimal allocation is

\[
 (h_1^*,h_2^*,h_3^*)=(1,7,8),\quad
 H_{\min}=16<21=nr,
 \quad v=(1,3,6).
\]

The exact integer migration and growth-harvest matrix is

\[
 B=\begin{pmatrix}-3&1&0\\9&-5&1\\0&4&-2\end{pmatrix},
 \qquad Bv=0.
\]

Since \(v\) is strictly positive, zero is the principal linear eigenvalue; the nonlinear crowding terms give global extinction. The saving \(21-16=5\) equals \((3-1)^2+(2-1)^2\).

The included standalone `check.py` uses only the Python standard library. Its exact rational tests verify the formulas and positive eigenvector identities on 400 randomized bidirectional trees (2–11 vertices), 35 two-patch parameter configurations across both branches, and the three-cycle counterexample. Execute with `python check.py`. These tests catch algebraic mistakes; the general result rests on the analytical proof, not finite enumeration.

## Relationship to prior work

Nguyen, Shuai, Tang, Veprauskas, Wu and Zhou (2026) analyze optimal allocation under a fixed total harvesting effort for maximum biomass and sustainable yield. They explicitly list **minimum total harvesting effort for extinction** among further questions, but do not give the budget formulas, unique tree allocation, or directed-cycle obstruction proved here. The present problem uses their conservative migration and logistic crowding equations while changing the objective.

Preciado, Zargham, Enyioha, Jadbabaie and Pappas (2013) already give a general geometric-programming framework for cost-optimal protection of positive network spreading systems. Therefore neither optimal diagonal stabilization nor Perron-based allocation is claimed as new. Their broader numerical optimization framework informs the proof; the specific additions assessed here are an exact ecological budget in elementary edge data, a precise feasibility threshold and unique patch controls on every bidirectional tree, an all-growth two-patch active-set classification, and a sharp cycle-consistency boundary with a counterexample to applying local edge savings indiscriminately. These exact statements are not present in the inspected works, although the technique is closely related to classical matrix balancing and their generic optimization machinery.

## Limitations

The result assumes continuous-time deterministic logistic growth, bidirectional positive rates on each existing edge, connected support, linear unit costs in per-capita mortality, and constant controls. Its ``minimum'' is an eradication objective, not a recommended fisheries policy. No guarantee is claimed against stochastic reinvasion, external recruitment, seasonal forcing, density-dependent migration, or harvest quotas. For trees at growth below the stated threshold, only the full two-patch case is explicitly classified. The full historical priority of elementary closed-form specializations of positive-system resource allocation has not been independently established.

## References

1. Nguyen, T. D., Shuai, Z., Tang, T., Veprauskas, A., Wu, Y., and Zhou, Y. (2026). *Optimal Harvesting in Stream Networks: Maximizing Biomass and Yield*. arXiv:2602.05071v1, publicly posted 4 February 2026. https://arxiv.org/abs/2602.05071 ; Bulletin of Mathematical Biology 88, article 91. https://doi.org/10.1007/s11538-026-01658-8
2. Preciado, V. M., Zargham, M., Enyioha, C., Jadbabaie, A., and Pappas, G. J. (2013). *Optimal Resource Allocation for Network Protection Against Spreading Processes*. arXiv:1309.6270. https://arxiv.org/abs/1309.6270
3. The Perron–Frobenius theorem, weighted Cauchy–Schwarz, AM–GM, and Jensen's inequality are used in their standard forms; no new general-purpose matrix-optimization theorem is claimed.
