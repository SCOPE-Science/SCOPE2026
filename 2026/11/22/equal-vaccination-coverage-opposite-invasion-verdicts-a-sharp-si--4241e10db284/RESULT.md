# Equal vaccination coverage, opposite invasion verdicts: a sharp six-vertex construction

## Finding

Consider the deterministic microscopic Markov-chain approximation (MMCA) of the opinion–vaccination–infection process in Roy, Shekhar, Ghosh, Kapitaniak and Hens (2026), on a connected, simple, undirected graph. **Theorem.** If a sign assignment \(s_i\in\{-1,1\}\) has a strict majority of same-sign neighbors at every vertex, then the model has a strictly saturated disease-free equilibrium with opinions \(O_i=s_i\), infected probabilities \(I_i=0\), and vaccinated probabilities \(V_i=(1+s_i)/[2(1+\phi)]\). This equilibrium is locally exponentially stable if \(\lambda\rho(A[G_-])<\alpha\), and is linearly invasion-unstable if \(\lambda\rho(A[G_-])>\alpha\). Here \(G_-\) is the subgraph induced by the negative-opinion vertices, and \(A[G_-]\) is its adjacency matrix. No conclusion at equality is asserted.

For two distinct strictly saturated, mixed-sign equilibria to occur on a connected graph, **six vertices are necessary**. Six suffice even when both equilibria have identical mean opinion and mean vaccination coverage but opposite epidemic-invasion verdicts: take a triangle attached by a single bridge to the middle vertex of a three-vertex path, and place all negative opinions first on the triangle and then on the path. With \(\alpha=\phi=1/2\), \(\lambda=3/10\), \(\epsilon=1/2\), and \(\omega=4/5\), the former disease-free equilibrium has an invasion multiplier \(11/10>1\), while the latter is locally exponentially attracting, with infection multiplier \(1/2+3\sqrt2/10<1\). Both have mean vaccinated probability \(1/3\) and mean opinion zero.

This discrepancy can be made arbitrarily large in the **ratio of exact local invasion thresholds** while the two states remain on the *same connected graph* and have *the same average vaccination coverage*: join a clique of order \(m\) to the interior vertex of a path of order \(m\), for every integer \(m\ge3\). Opposite uniform opinion signs on the two communities give thresholds
\[
\lambda_{\mathrm{clique}}^*=\frac{\alpha}{m-1},\qquad
\lambda_{\mathrm{path}}^*=\frac{\alpha}{2\cos(\pi/(m+1))},
\qquad
\frac{\lambda_{\mathrm{path}}^*}{\lambda_{\mathrm{clique}}^*}
=\frac{m-1}{2\cos(\pi/(m+1))}\longrightarrow\infty.
\]
The conclusion concerns local invasion of the deterministic MMCA, not stochastic outbreak probability.

## Assumptions and scope

Take a connected, loopless, undirected graph \(G=(\mathcal V,E)\) with \(n\ge2\) vertices, adjacency matrix \(A\), and degrees \(d_i\ge1\). The continuous opinions satisfy \(O_i\in[-1,1]\). The epidemic state has infected and vaccinated probabilities \(I_i,V_i\ge0\) with \(I_i+V_i\le1\), and susceptible probability \(S_i=1-I_i-V_i\). Assume \(0<\alpha,\phi,\lambda<1\), \(\epsilon>0\), and finite \(\omega\ge0\).

The node dynamics, with the source's clipping of opinions, are
\[
\begin{aligned}
O_i^+&=\operatorname{clip}_{[-1,1]}\!\left(O_i+\frac{\epsilon}{d_i}\sum_jA_{ij}O_j+\frac{\omega}{d_i}\sum_jA_{ij}I_j\right),\\
\gamma_i&=\frac{1+O_i}{2},\qquad
q_i=1-\prod_j(1-\lambda A_{ij}I_j),\\
I_i^+&=(1-\alpha)I_i+S_i(1-\gamma_i)q_i,\\
V_i^+&=(1-\phi)V_i+S_i\gamma_i.
\end{aligned}
\]
These are the semi-analytical equations, not statements about almost-sure trajectories of the underlying random-node system. Whether vaccination uses the current or just-updated opinion does not change the linearization at the strictly saturated states because opinion clipping is locally constant there. No equality-case stability is claimed.

For a sign configuration \(s\), define the neighbor-majority margin \(h_i=s_i\sum_jA_{ij}s_j\). The hypothesis is \(h_i>0\) for **every** vertex, not merely a non-strict majority. For clarity, strictly saturated means that the *unclipped* opinion update lies strictly past the appropriate endpoint at the equilibrium; it does not mean that every possible binary opinion equilibrium obeys this condition.

## Proof

**1. Strict clipping and equilibrium.** Put \(O=s\), \(I=0\). At vertex \(i\), the pre-clipping opinion is \(s_i+\epsilon d_i^{-1}\sum_jA_{ij}s_j\), whose signed excess beyond \(s_i\) is \(\epsilon h_i/d_i>0\). Since the graph and parameters are finite, these inequalities persist in an open neighborhood of the proposed state. Throughout that neighborhood the opinion output is identically \(s\). Thus the local opinion Jacobian is zero; this remains true with the risk-perception term. The vaccination propensity is \(\gamma_i=(1+s_i)/2\), which is zero or one. At zero infection, the vaccination equation reads \(V_i^+=(1-\phi)V_i+(1-V_i)\gamma_i\). Its unique fixed value is \(V_i=\gamma_i/(\phi+\gamma_i)\), giving the formula in the statement. Infection remains zero because \(q_i=0\).

**2. Infection linearization and full local stability.** Let \(D\) be diagonal with \(D_{ii}=1\) for \(s_i=-1\) and zero otherwise. Since \(q_i=\lambda\sum_jA_{ij}I_j+O(\|I\|^2)\), the infected block of the local Jacobian is
\[
J_I=(1-\alpha)\mathbf 1+\lambda DA.
\]
(The bold \(\mathbf 1\) here denotes the identity matrix, not the all-ones matrix.) After ordering negative-opinion vertices first, \(DA\) has diagonal blocks \(A[G_-]\) and zero; its off-diagonal block does not affect the eigenvalues. The vaccinated block has multipliers \(1-\phi\) on negative vertices and \(-\phi\) on positive vertices: for the latter, \(V_i^+=1-I_i-\phi V_i\) at fixed \(\gamma_i=1\). The opinion block is zero. Dependence of vaccination on infection only contributes off-diagonal blocks, because infection feedback vanishes to first order in \(V\) or \(O\) at zero infection. Hence the full Jacobian is block triangular with these blocks.

Since \(A[G_-]\) is symmetric, its eigenvalues lie between \(-\rho(A[G_-])\) and \(\rho(A[G_-])\). Under \(\lambda\rho(A[G_-])<\alpha\), the largest infected eigenvalue is below one, and the smallest is at least \(1-\alpha-\lambda\rho(A[G_-])>1-2\alpha>-1\). All other multipliers have absolute value below one because \(0<\alpha,\phi<1\). The map is continuously differentiable on the stated neighborhood (no clipping boundary is met), so the fixed point is locally exponentially attracting on the physical state space. If \(\lambda\rho(A[G_-])>\alpha\), a nonnegative Perron eigenvector in the negative community gives an infected eigenvalue above one, hence a feasible linear invasion direction and instability. The case of an empty negative set has radius zero and is covered by the stable case.

**3. Sharp graph-size obstruction.** If both signs occur on a connected graph, each sign class has a vertex incident to an edge connecting it to the opposite sign. At such a vertex, strict same-sign majority requires at least two *distinct* same-sign neighbors. Therefore each sign class contains at least three vertices, so \(n\ge6\). This argument proves necessity without relying on a finite graph census.

**4. Explicit smallest example.** Label the triangle \(\{0,1,2\}\) and the path \(3-4-5\), with bridge \(0-4\). Every triangle vertex has two same-sign neighbors (the bridge endpoint has just one opposite neighbor). Every path vertex has at least one same-sign neighbor, and its middle vertex has two same-sign and one opposite neighbor. Thus either choice of uniform opposite community signs has all \(h_i>0\). In one choice \(G_-=K_3\), with adjacency radius \(2\); in the other \(G_-=P_3\), with adjacency radius \(\sqrt2\). With the stated exact parameters,
\[
(1-\alpha)+\lambda\rho(K_3)=\tfrac{11}{10}>1,
\qquad (1-\alpha)+\lambda\rho(P_3)=\tfrac12+\tfrac{3\sqrt2}{10}<1
\]
because \(18<25\). Each equilibrium has exactly three positive-opinion and three negative-opinion vertices. Positive-opinion vertices have \(V_i=2/3\); negative ones have \(V_i=0\), so both mean vaccination fractions are \(1/3\). The vaccinated block is strictly contracting at either state and the opinion map is locally constant, thus the latter state is genuinely stable in all coordinates.

**5. Family and divergence.** For each integer \(m\ge3\), form the same bridge from one clique vertex of \(K_m\) to an interior vertex of \(P_m\). At each bridge endpoint there are respectively \(m-1\ge2\) and two same-sign neighbors versus one opposite; all other vertices have only same-sign neighbors. Thus both opposite sign choices satisfy the strict clipping condition, with exactly half the vertices positive in either state. The induced negative graph is respectively \(K_m\) or \(P_m\). Their adjacency radii are \(m-1\) and \(2\cos(\pi/(m+1))\), the latter obtained by the sine eigenvectors of a path. Both thresholds are \(\lambda^*=\alpha/\rho\), with \(m-1>2\cos(\pi/(m+1))\) for all \(m\ge3\). The ratio diverges because its numerator increases without bound while the denominator tends to two. For \(0<\alpha<1\), both thresholds lie within the admissible per-contact range, and a \(\lambda\) strictly between them produces opposite invasion verdicts.

## Verification

Run `python3 checker.py` using Python 3 standard library. The independent finite computations exhaust all connected labelled simple graphs of at most five vertices as a corroboration of the analytical size lower bound, verify the strict sign margins on the \(m=3,\dots,50\) family, reconstruct both six-vertex disease-free fixed points, verify their common coverage, and compare finite differences with the two exact invasion eigenvalues. The code's finite ranges do not prove the infinite assertions; those rest on the preceding graph and matrix arguments.

## Relationship to prior work

Roy et al. (2026, version 1) provide the coupled clipped-opinion MMCA and analyze the all-negative-opinion threshold \(\lambda_c=\alpha/\rho(A)\) and the all-positive vaccination limit \(1/(1+\phi)\). Neither analysis distinguishes the two endogenous strictly polarized equilibria on one graph or supplies the sharp six-vertex and unbounded-threshold-ratio conclusions. The general role of susceptibility-weighted spectra is established in Preciado et al. (2013), and the general danger of spatially clustered vaccine refusal at fixed coverage was demonstrated by Salathé and Bonhoeffer (2008). Neither general phenomenon is claimed novel here; the result is the exact endogenous-opinion construction, strict local stability classification and minimality in this specified MMCA. Xu and Ishii (2024) study a different polar-opinion update and derive related reproduction-number criteria; their disease-free consensus dynamics do not imply strict, mixed, clipped local-majority fixed points of the present opinion map.

## Limitations

The construction uses a shared social/contact graph, homogeneous transmission and recovery probabilities, a deterministic node-marginal approximation, and strictly saturated binary opinions. The six-vertex minimality is **only within the mixed-sign, strictly saturated class**, not a universal lower bound for all opinion patterns or epidemic models. The result compares local linear invasion at existing disease-free equilibria; it does not prove a global attraction basin for the unstable state, existence of a nonlinear endemic equilibrium, stochastic outbreak probabilities, or asymptotic behavior at threshold equality. The general spectral-invasion comparison and qualitative fixed-coverage clustering mechanism were already known; the novelty claim is narrower and remains subject to independent historical review.

## References

1. A. Roy, U. Shekhar, S. Ghosh, T. Kapitaniak and C. Hens, *Opinion-Driven Vaccination and Epidemic Dynamics on Heterogeneous Networks*, arXiv:2603.24403v1 (first posted March 25, 2026), https://arxiv.org/html/2603.24403v1 (model equations (1)–(8), epidemic threshold, vaccination saturation).
2. Q. Xu and H. Ishii, *On a Discrete-Time Networked SIV Epidemic Model with Polar Opinion Dynamics*, arXiv:2401.04556 (2024), https://arxiv.org/abs/2401.04556.
3. V. M. Preciado, M. Zargham, C. Enyioha, A. Jadbabaie and G. J. Pappas, *Optimal Vaccine Allocation to Control Epidemic Outbreaks in Arbitrary Networks*, arXiv:1303.3984 (2013), https://arxiv.org/abs/1303.3984.
4. M. Salathé and S. Bonhoeffer, *The effect of opinion clustering on disease outbreaks*, *Journal of the Royal Society Interface* 5 (2008), 1505–1508, https://doi.org/10.1098/rsif.2008.0271.
