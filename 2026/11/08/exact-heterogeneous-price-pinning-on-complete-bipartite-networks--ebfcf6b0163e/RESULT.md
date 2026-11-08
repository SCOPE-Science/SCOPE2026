# Exact heterogeneous-price pinning on complete bipartite networks

## Finding

Let \(K_{p,q}\) be the unit-conductance complete bipartite graph, where \(p,q\ge 2\). Give its first part independent positive prices \(\alpha_1,\ldots,\alpha_p\), and its second part independent positive prices \(\beta_1,\ldots,\beta_q\). At budget \(B>0\), maximize the smallest eigenvalue of the pinned Laplacian:
\[
\Lambda(B)=\max_{u_i,v_j\ge0\,;\,\sum_i\alpha_i u_i+\sum_j\beta_j v_j\le B}
\lambda_{\min}\!\left(L_{K_{p,q}}+\operatorname{diag}(u_1,\ldots,u_p,v_1,\ldots,v_q)\right).
\]

**Theorem.** For every such instance, the optimizer is unique and spends the entire budget. It is given *exactly by two nested one-dimensional monotone root equations*, with no matrix optimization. For a target rate \(t>0\), define, for \(c>0\),
\[
\begin{aligned}
X_i(c,t)&=\max\{q-t,c/\sqrt{\alpha_i}\},\\
A(c,t)&=\sum_{i=1}^{p}X_i(c,t)^{-1},\\
d(c,t)&=cA(c,t),\\
Y_j(c,t)&=\max\{p-t,d(c,t)/\sqrt{\beta_j}\},\\
H_t(c)&=A(c,t)\sum_{j=1}^{q}Y_j(c,t)^{-1}.
\end{aligned}
\]
There is a **unique** positive root \(c_t\) of \(H_t(c)=1\). Put \(d_t=d(c_t,t)\) and
\[
u_i(t)=\max\{0,t-q+c_t/\sqrt{\alpha_i}\},\qquad
v_j(t)=\max\{0,t-p+d_t/\sqrt{\beta_j}\}.
\]
Then
\[
F(t)=\sum_i\alpha_i u_i(t)+\sum_j\beta_j v_j(t)
\]
is continuous, strictly increasing from \(F(0+)=0\) to infinity. The unique solution \(t=\Lambda(B)\) of \(F(t)=B\) yields the unique optimal gains \(u_i(t),v_j(t)\).

**Price-ordered support.** For every budget, the active actuators in each part form a cheapest-price prefix (equal-price vertices have equal gains). If the globally cheapest vertex has a strictly smaller price than every other vertex, it is the only active vertex at all sufficiently small positive budgets.

**Exact terminal affine law.** Write
\[
T_\alpha=\sum_i\sqrt{\alpha_i},\quad T_\beta=\sum_j\sqrt{\beta_j},\quad P_\alpha=\sum_i\alpha_i,\quad P_\beta=\sum_j\beta_j,
\]
and
\[
t_{\mathrm{all}}=\max\left\{0,\ q-\frac{T_\beta}{\sqrt{\max_i\alpha_i}},\ p-\frac{T_\alpha}{\sqrt{\max_j\beta_j}}\right\}.
\]
For every \(t\ge t_{\mathrm{all}}\), the optimal gains have the explicit form
\[
u_i(t)=t-q+\frac{T_\beta}{\sqrt{\alpha_i}},\qquad
v_j(t)=t-p+\frac{T_\alpha}{\sqrt{\beta_j}},
\]
and
\[
\boxed{F(t)=(P_\alpha+P_\beta)t-qP_\alpha-pP_\beta+2T_\alpha T_\beta.}
\]
Here the displayed gains are nonnegative at equality and all strictly positive for \(t>t_{\mathrm{all}}\); thus the optimal rate is exactly affine in sufficiently large budgets.

**Closed two-price transition.** If every first-part price equals \(\alpha\) and every second-part price equals \(\beta>\alpha\), set \(r=\sqrt{\alpha/\beta}\), \(t_*=p(1-r)\), and
\[
B_*=p\alpha\frac{t_*(p+q-t_*)}{p-t_*}.
\]
For \(0<B\le B_*\), only the first part is pinned, every first-part gain is \(B/(p\alpha)\), and the optimal rate is
\[
\Lambda(B)=\frac{p+q+B/(p\alpha)-\sqrt{(q+B/(p\alpha)-p)^2+4pq}}{2}.
\]
For \(B\ge B_*\), both parts obey the explicit gains above, and
\[
\boxed{\Lambda(B)=\frac{B+pq(\sqrt\beta-\sqrt\alpha)^2}{p\alpha+q\beta}.}
\]
The branches agree at \(B_*\). For \(\beta<\alpha\), interchange the two parts; for \(\alpha=\beta\), all gains equal \(B/(\alpha(p+q))\).

## Assumptions and scope

Edges have unit conductance, the graph is connected, and each vertex has a separately adjustable *nonnegative diagonal feedback gain*. All prices and the total budget are strictly positive. The matrix \(L\) is the unnormalized symmetric combinatorial Laplacian; the controlled dynamics is \(\dot z=-(L+\operatorname{diag}(u,v))z\). The measured convergence exponent is its *smallest eigenvalue*, not the eigenratio, transient control energy, or the number of independent coordinate input channels. There is no cap on an individual gain. The theorem applies to all integers \(p,q\ge2\) and all positive real price arrays.

## Proof

**1. Exact feasibility at a requested rate.** For fixed \(t>0\), let \(x_i=q+u_i-t\), \(y_j=p+v_j-t\). The matrix \(L+\operatorname{diag}(u,v)-tI\) has diagonal blocks \(\operatorname{diag}(x_i)\), \(\operatorname{diag}(y_j)\) and off-diagonal blocks consisting of \(-1\). Positivity of this matrix forces every \(x_i,y_j\) to be strictly positive: if one vanished, the corresponding \(2\times2\) principal minor across the graph cut would be negative. A Schur complement, followed by the rank-one positive-semidefinite criterion, therefore gives the **equivalence**
\[
\lambda_{\min}(L+\operatorname{diag}(u,v))\ge t
\iff
\left(\sum_i\frac1{x_i}\right)\left(\sum_j\frac1{y_j}\right)\le1.
\]
This equivalence, rather than a relaxation, is the optimization's crucial reduction.

**2. Strictly convex minimum-cost problem.** Minimize \(\sum_i\alpha_i u_i+\sum_j\beta_j v_j\) over nonnegative gains subject to the preceding inequality. Write \(A=\sum_i x_i^{-1}\), \(D=\sum_j y_j^{-1}\) and \(\phi=\log A+\log D\). The constraint is \(\phi\le0\). For every nonzero vector \(h\),
\[
h^\top\nabla^2(\log A)h
=\frac2A\sum_i\frac{h_i^2}{x_i^3}-\frac1{A^2}\left(\sum_i\frac{h_i}{x_i^2}\right)^2
\ge\frac1A\sum_i\frac{h_i^2}{x_i^3}>0,
\]
where Cauchy--Schwarz gives the inequality. The analogous calculation applies to \(\log D\). Hence \(\phi\) is strictly convex in the joint positive variables. Slater's condition holds by taking sufficiently large gains. The cost is coercive on the nonnegative orthant and the feasible set is nonempty; therefore a minimizer exists. Its constraint is tight because with slack one could decrease a positive gain and reduce cost. Two distinct minimizers would have a strictly feasible midpoint of equal cost, an impossibility by the same decrease argument. Thus the minimizer is unique.

**3. Water-filling equations.** Let \(\mu>0\) be the Lagrange multiplier for \(\phi\le0\). KKT stationarity for each positive gain is
\[
\alpha_i=\frac\mu{Ax_i^2},\qquad \beta_j=\frac\mu{Dy_j^2},
\]
and complementary slackness for zero gains yields
\[
x_i=\max\{q-t,c/\sqrt{\alpha_i}\},\quad
 y_j=\max\{p-t,d/\sqrt{\beta_j}\},\quad
c=\sqrt{\mu/A},\quad d=\sqrt{\mu/D}.
\]
Tightness \(AD=1\) implies \(d=cA\), so exactly \(H_t(c)=1\). Conversely, any positive root produces nonnegative gains satisfying all KKT conditions and is the unique minimizer from step 2.

**4. The scalar root is unique.** The function \(A(c,t)\) is continuous and nonincreasing, while \(d(c,t)=cA(c,t)\) is continuous and nondecreasing: each summand \(c/X_i(c,t)\) is the minimum of a nondecreasing linear function and the constant \(\sqrt{\alpha_i}\) (or the constant when \(q\le t\)). Thus \(H_t(c)\) is continuous and nonincreasing. As \(c\downarrow0\), if \(t<\min(p,q)\),
\[
H_t(c)\longrightarrow\frac{pq}{(p-t)(q-t)}>1;
\]
if \(t\ge\min(p,q)\), the limit is infinity. As \(c\to\infty\), \(A(c,t)\sim T_\alpha/c\), \(d(c,t)\to T_\alpha\), and \(H_t(c)\to0\). Once either part activates, its corresponding factor strictly decreases with \(c\); therefore \(H_t\) has a **single** crossing of one. The formula for the unique optimum follows.

**5. Budget inversion and ordering.** Increasing a single diagonal gain strictly increases the smallest eigenvalue: the associated normalized smallest-eigenvalue eigenvector is entrywise positive by the irreducible symmetric \(M\)-matrix/Perron--Frobenius theorem, and the Hellmann--Feynman derivative equals the square of its corresponding component. Thus an optimal gain vector uses the whole budget. The minimum target cost \(F(t)\) is continuous by existence, uniqueness and compactness of bounded-cost sublevel sets. For \(0<t_1<t_2\), an optimizer for \(t_2\) is strictly feasible for target \(t_1\), and lowering a positive coordinate slightly reduces its cost; hence \(F(t_1)<F(t_2)\). Its limit is zero as \(t\downarrow0\) (uniform arbitrarily small gains achieve arbitrary small positive target rates), and \(F(t)\to\infty\) since the constant-vector Rayleigh quotient yields \(t\le (\sum_i u_i+\sum_j v_j)/(p+q)\). Consequently the budget root is unique. The max formulas immediately show cheapest-prefix activation within each part. To identify the first active actuator, put \(\rho=\min\{\alpha_i,\beta_j\}\). At \(t=0\), the scalar root function equals one on \(0,q\sqrt{\rho}]\), and is strictly below one immediately beyond \(q\sqrt{\rho}\); continuity and the strict crossing for \(t>0\) imply \(c_t\to q\sqrt{\rho}\) and \(d_t\to p\sqrt{\rho}\) as \(t\downarrow0\). If this cheapest price is unique, all other activation thresholds have a positive separation, so precisely that vertex has a positive gain at sufficiently small targets. (The cases in which the cheapest vertex lies in either bipartition are treated symmetrically.)

**6. High-budget law.** When every gain is positive, the KKT relations give \(A=T_\alpha/c\), \(D=T_\beta/d\), \(d=cA=T_\alpha\), and \(c=dD=T_\beta\). This proves the explicit high-target allocation and cost formula. Exactly the stated condition \(t\ge t_{\mathrm{all}}\) makes that candidate nonnegative; KKT then proves its optimality, including at activation boundaries.

**7. Uniform prices within the two parts.** Unique optimality and within-part permutation symmetry force equal gains inside each part. If \(\alpha<\beta\), the second-part gain remains zero until its KKT inequality becomes equality at \(t_*=p(1-\sqrt{\alpha/\beta})\). Prior to this transition the quotient-space eigenvalue equation gives \((q+a-t)(p-t)=pq\), with gain \(a=t(p+q-t)/(p-t)\). Above it both part gains satisfy the high-target formulas, giving the displayed threshold and affine branch. This proves the full two-price phase diagram, including its equalities.

## Verification

Run `python3 verify_bipartite_pinning.py` with NumPy and SciPy. The program checks independent full-matrix eigenspectra and constrained numerical optimizers for 100 pseudo-random heterogeneous instances, 200 two-price transitions, 196 exact-rational branch/KKT identities, 1,280 ordering comparisons, and 86 additional high-budget identities. A numerical optimizer and finite tests are corroboration only; steps 1--7 give the universal proof. The source file and all required inputs are standalone; no external data are needed.

## Relationship to prior work

Zhou, Zhuo, Liao, Fu and Cai (arXiv:1511.02012, posted 2015-11-06) frame budgeted pinning gain selection as a linear matrix inequality, using numerical optimization for heterogeneous importance weights and deriving an analytic uniform-cost case. The full preprint's optimization and Methods sections do not provide the present two-block rank-one cost reduction, arbitrary independent-price scalar characterization, or the exact two-price transition. Orouskhani, Jalili and Yu (Scientific Reports 6:24252, 2016-04-12) study multiple pinning optimization tasks by a population heuristic, generally measuring an *eigenratio* instead of this smallest-eigenvalue rate; their separate objectives do not give this theorem. Jalili, Sichani and Yu (Physical Review E 91:012803, 2015-01-05) concern driver-node placement and network structure; only abstract-level material was inspected, so possible specialist overlap remains a risk. Jafarizadeh (2022) develops a general equal-price pinned-node budget algorithm and explicit complete-bipartite results when one entire part is pinned and the other is free; its relevant complete-bipartite theorem has no arbitrary independent vertex prices and does not provide the two-sided activation transition. Equal-price global-gain formulas are therefore not asserted as new. Classical Schur complements, KKT theory, and the underlying semidefinite formulation are acknowledged prior mathematical tools, not novelty claims.

## Limitations

The result does not optimize edge conductances, eigenratios, transient control energies, switching schedules, or actuator cardinality with fixed individual gain caps. The scalar root characterization is exact but not an elementary closed formula for arbitrary independent prices. All independent verification is still pending; the proof and checks described above are not an external mathematical certification. Published priority may be affected by specialist sources not available in full text.

## References

1. M.-Y. Zhou, Z. Zhuo, H. Liao, Z.-Q. Fu, and S.-M. Cai, *Enhancing speed of pinning synchronizability: low-degree nodes with high feedback gains*, arXiv:1511.02012v1 (2015-11-06), https://arxiv.org/abs/1511.02012 .
2. Y. Orouskhani, M. Jalili, and X. Yu, *Optimizing Dynamical Network Structure for Pinning Control*, Scientific Reports **6**, 24252 (2016-04-12), https://doi.org/10.1038/srep24252 .
3. M. Jalili, O. A. Sichani, and X. Yu, *Optimal pinning controllability of complex networks: Dependence on network structure*, Physical Review E **91**, 012803 (2015-01-05), https://doi.org/10.1103/PhysRevE.91.012803 .
4. S. Jafarizadeh, *Pinning Control of Dynamical Networks With Optimal Convergence Rate*, IEEE Transactions on Systems, Man, and Cybernetics: Systems **52** (2022), 7160–7172, https://doi.org/10.1109/TSMC.2022.3151222 .
