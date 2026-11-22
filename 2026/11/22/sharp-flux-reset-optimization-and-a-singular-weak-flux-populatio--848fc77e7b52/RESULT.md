# Sharp flux–reset optimization and a singular weak-flux population imbalance in a quantum triangle

## Finding

Consider a single coherently hopping particle on a three-site ring, with magnetic phase \(\Phi\) and whole-state Poisson resetting to site \(0\). For each hopping amplitude \(J>0\), reset rate \(r>0\), and real \(\Phi\), let \(u=r/J\), \(s=\sin\Phi\), and
\[
Q(u,s)=u^2(u^2+9)^2+108s^2.
\]
The unique stationary site populations obey
\[
\boxed{p_1-p_2=-\frac{12u(u^2+3)s}{Q(u,s)}}.
\]
For \(s\ne0\), the absolute directional imbalance has exactly one optimal positive reset rate \(r_*(\Phi)=J\sqrt{x_*(s^2)}\), where \(x_*(h)\) is the unique positive root of
\[
F(x,h)=x^4+11x^3+27x^2+(81-108h)x-108h.
\]
Its optimized value increases strictly with \(|s|\in(0,1]\). The global optimum over all fluxes and positive reset rates is reached exactly when \(\Phi\equiv\pi/2\) or \(3\pi/2\pmod{2\pi}\), at
\[
\frac{r_*}{J}=\sqrt{\frac{\sqrt{73}-5}{2}},\qquad
\max_{r>0,\Phi\in\mathbb R}|p_1-p_2|=0.243061210127578\ldots .
\]
At vanishing but nonzero flux, the rate optimizer tends to zero linearly while the optimized bias remains finite:
\[
\frac{r_*(\Phi)}{J}=\frac{2}{\sqrt3}|\sin\Phi|+O(|\sin\Phi|^3),\qquad
\lim_{\substack{|\sin\Phi|\to0\\\sin\Phi\ne0}}
\max_{r>0}|p_1-p_2|=\frac{1}{3\sqrt3}.
\]
Exactly at \(\sin\Phi=0\), however, \(p_1=p_2\) for every \(r>0\). Thus flux removal and reset-rate optimization do not commute.

## Assumptions and scope

In the orthonormal site basis \(|0\rangle,|1\rangle,|2\rangle\) and units \(\hbar=1\), fix the Hermitian Hamiltonian
\[
H=J\begin{pmatrix}0&1&e^{i\Phi}\\1&0&1\\e^{-i\Phi}&1&0\end{pmatrix}.
\]
The gauge-invariant directed product of hopping amplitudes around the triangle has phase \(\Phi\), up to orientation. Reset events form a state-independent Poisson process of intensity \(r\); each replaces the full density matrix by \(|0\rangle\langle0|\). The ensemble evolution is
\[
\dot\rho=-i[H,\rho]+r\bigl(|0\rangle\langle0|-\rho\bigr).
\]
The observable is the difference of the two non-reset *site occupation probabilities*, not the circulation/current through an edge. There is no site loss, projective detection, classical hopping, additional dephasing, or time-dependent driving.

## Proof

**1. Existence, uniqueness, and exact populations.** Writing \(A=|0\rangle\langle0|\), the unique stationary density matrix is
\[
\rho_*=r\int_0^\infty e^{-rt}e^{-iHt}A e^{iHt}\,dt.
\]
This converges in trace norm, is positive semidefinite with unit trace, and solves \((r+i\operatorname{ad}_H)\rho_*=rA\). Uniqueness follows because the matrix units in an eigenbasis of the Hermitian \(H\) have eigenvalues \(r+i(E_j-E_k)\ne0\) under this operator.

To evaluate the diagonal, divide by \(J\), set \(z=e^{i\Phi}\), and order the nine matrix entries row by row. The resolvent linear system \(K\operatorname{vec}\rho_*=u\operatorname{vec}A\) has coefficients
\[
K_{(ij),(k\ell)}=u\delta_{ik}\delta_{j\ell}+i(H/J)_{ik}\delta_{j\ell}-i\delta_{ik}(H/J)_{\ell j}.
\]
Direct exact elimination gives \(\det K=u^3Q(u,s)\), together with
\[
\begin{aligned}
p_0&=\frac{u^6+14u^4+45u^2+36s^2}{Q(u,s)},\\
p_1&=\frac{2u^4+18u^2+36s^2-6u(u^2+3)s}{Q(u,s)},\\
p_2&=\frac{2u^4+18u^2+36s^2+6u(u^2+3)s}{Q(u,s)}.
\end{aligned}
\]
These expressions sum to one. Their exact resolvent identities can be reproduced by `python verify_chiral_trimer.py`, which also checks the determinant and independently solves the complex matrix equation numerically.

**2. Unique reset-rate optimizer.** For \(b=|s|>0\), maximize
\[
f_b(u)=\frac{12bu(u^2+3)}{u^2(u^2+9)^2+108b^2},\quad u>0.
\]
Its derivative has the exact sign identity
\[
\frac{d f_b}{du}=-\frac{36b F(u^2,b^2)}{Q(u,b)^2}.
\]
For \(0<b\le1\), the descending coefficients of \(F(x,b^2)\) have exactly one sign change regardless of the sign of \(81-108b^2\). Descartes' rule therefore gives at most one positive zero. Since \(F(0,b^2)<0\) and \(F(x,b^2)\to\infty\) as \(x\to\infty\), there is exactly one. Also \(f_b(u)\to0\) at both ends of \((0,\infty)\), proving strict increase then strict decrease and unique global optimality.

**3. Optimizing the flux.** At \(u=\sqrt{x_*(b^2)}\), the stationary-point equation gives
\[
108b^2=\frac{x(x^3+11x^2+27x+81)}{x+1},
\]
and consequently
\[
x(x+9)^2-108b^2=\frac{8x^2(x+9)}{x+1}>0.
\]
The partial derivative of \(f_b(u)\) with respect to \(b\) has the sign of \(u^2(u^2+9)^2-108b^2\). Hence it is strictly positive at the unique optimizer. Continuity of the unique positive root and elementary differentiation yield strict increase of the optimized envelope in \(b\). The maximum is thus at \(b=1\). There,
\[
F(x,1)=(x+3)^2(x^2+5x-12),
\]
so the unique positive root is \(x=(\sqrt{73}-5)/2\); substitution gives the displayed maximum.

**4. Noncommuting weak-flux limit.** Set \(h=b^2\). The optimizer equation \(F(x,h)=0\), with \(F_x(0,0)=81\), yields by expansion \(x_*(h)=\frac43h+O(h^2)\). Substituting \(u=\sqrt{x_*(b^2)}\) in \(f_b\) gives \(f_b(u_*)=1/(3\sqrt3)+O(b^2)\). For \(b=0\), the exact population-difference formula is identically zero for all positive \(u\), establishing the claimed singularity.

## Verification

The included `verify_chiral_trimer.py` builds the full \(9\times9\) resolvent from the Hamiltonian, verifies its exact determinant, the population formulas and optimizer derivative symbolically, tests the optimizing polynomial factorization and flux envelope identity, and solves independent complex-valued linear systems at 56 parameter combinations. It executed with 304 independent scalar numerical assertions in addition to the symbolic identities. The uniqueness and singular-limit results are analytical; finite tests are corroboration, not a substitute for proof. Python with `sympy` and `numpy` is sufficient.

## Relationship to prior work

Rose, Touchette, Lesanovsky and Garrahan (2018), particularly their Sec. V.2 and Eqs. (73)–(74), establish the **general** stationary spectral resolvent for coherently hopping systems under full-state Poisson resetting. Wald and Böttcher (2020), Sec. III D, establish related general formulas for quantum walks on unweighted real networks. Those formulas justify the resetting construction, but do not state the magnetic-triangle directional imbalance, its unique optimizer, the full flux optimization, or the singular flux–rate crossover. They are not claimed as new.

Dattagupta, Das and Gupta (2022) examine resetting on an *infinite driven chain* and its localization, not a flux-threaded triangle. Recent work on chiral quantum transport on triangle-unit chains concerns coherent finite-time transfer rather than the stationary Poisson-reset occupation imbalance. Published exact results for **absorbing** chiral quantum triangles or **measurement-based** magnetic-ring return statistics concern different dynamical maps or observables, and do not provide the optimizer here. The general spectral resolvent may make the exact diagonal calculable in principle, so the distinctive assessed contribution is the global optimality and noncommuting weak-flux limit, not the abstract resolvent method.

## Limitations

This theorem is restricted to a single homogeneous three-site ring with one instantaneous full-state reset location. The handedness of \(p_1-p_2\) depends on the choice of site and flux orientation. It does not show that physical circulating current is nonzero, optimize a many-particle protocol, or establish robustness to static disorder, local dephasing, finite reset duration or imperfect preparation. The finite limiting optimized asymmetry requires coordinated tuning \(r/J\asymp|\sin\Phi|\) and should not be interpreted as finite asymmetry at exactly zero flux. Novelty relative to all possible implicit consequences of broad spectral theory still merits independent literature appraisal.

## References

- D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes* (2018), arXiv:1806.01298, https://arxiv.org/abs/1806.01298.
- S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks* (2020), arXiv:2008.00510, https://arxiv.org/abs/2008.00510.
- S. Dattagupta, D. Das and S. Gupta, *Stochastic resets in the context of a tight-binding chain driven by an oscillating field* (2022), arXiv:2209.14117, https://arxiv.org/abs/2209.14117.
- *Enhanced quantum transport in chiral quantum walks*, *Quantum Information Processing* (2024), https://doi.org/10.1007/s11128-024-04331-y.
- *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States* (2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC11508062/.
