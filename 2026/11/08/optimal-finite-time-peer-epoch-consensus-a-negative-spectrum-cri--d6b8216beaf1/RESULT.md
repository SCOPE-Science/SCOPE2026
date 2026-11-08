# Optimal finite-time peer-epoch consensus: a negative-spectrum criterion and a graph-support obstruction

## Finding

Let \(W\) be any irreducible reversible stochastic matrix on \(n\geq2\) states, with stationary distribution \(\pi\). An opinion vector undergoes successive homogeneous finite Friedkin–Johnsen peer epochs, each resetting its anchor to the current opinions:
\[
 x_{t+1}=\Psi_{K_t}(\alpha_t,W)x_t,\qquad
 \Psi_K(\alpha,W)=(\alpha W)^K+(1-\alpha)\sum_{j=0}^{K-1}(\alpha W)^j,
\]
where every \(K_t\) is a positive integer and every \(0<\alpha_t<1\). The integer horizons and scalar susceptibilities may vary between epochs and may even depend on past opinions.

**Exact spectral controllability and optimal outer-epoch count.** Let \(\mu_1=1>\mu_2\geq\cdots\geq\mu_n\geq-1\) be the eigenvalues of \(W\), including multiplicity. A finite schedule takes *every initial opinion vector* to consensus if and only if \(\mu_2<0\). When this holds, the least possible number of outer epochs is precisely
\[
 r=\big|\{\mu_2,\ldots,\mu_n\}\big|,
\]
where braces count distinct values. An optimal schedule uses \(r\) epochs, each with just one inner peer step \(K_t=1\), and for each distinct nonconstant eigenvalue \(\mu\) selects \(\alpha_t=1/(1-\mu)\). The resulting product is exactly \(\mathbf1\pi^{\mathsf T}\). Longer finite inner horizons cannot reduce \(r\); even horizons can never annihilate a spectral mode.

**Topology obstruction.** If two different states \(u,v\) have neither directed transition between them (equivalently \(W_{uv}=W_{vu}=0\)), then \(\mu_2\geq\min\{W_{uu},W_{vv}\}\geq0\), so no finite schedule exists, even with history-adaptive choices. For a connected simple undirected \(d\)-regular graph, \(W=A/d\) therefore admits universal exact finite-epoch consensus **if and only if the graph is complete**. On \(K_n\), a single odd horizon \(K\) works at exactly one susceptibility solving
\[
 1-\alpha=\frac{n}{(n-1)^{K+1}}\alpha^{K+1};
\]
no even horizon works. In particular, the one-step choice is \(\alpha=(n-1)/n\).

## Assumptions and scope

The state space is \(\mathbb R^n\); negative or unbounded initial opinions are permitted mathematically, although the averaging updates preserve every initial interval. Irreducibility means the transition graph is connected in the Markov sense. Reversibility means \(\pi_iW_{ij}=\pi_jW_{ji}\), with \(\pi_i>0\) and \(\sum_i\pi_i=1\). No mixing, positivity of diagonal entries, regularity, or symmetry in the original coordinates is required for the spectral theorem. Each epoch uses the *same fixed* \(W\) and a *single shared* susceptibility \(\alpha_t\); resetting anchors and taking finite \(K_t\) are essential. This describes a deterministic linear opinion process under perfect-feedback anchoring, not the general heterogeneous or imperfect-prediction formulation. A successful schedule must work for all initial vectors; for adaptive schedules, the lower bound additionally holds for every initial vector with nonzero components in all nonconstant eigenspaces.

## Proof

1. **Common reversible eigenbasis.** With \(D=\mathrm{diag}(\pi)\), the similarity transform \(S=D^{1/2}WD^{-1/2}\) is symmetric. Irreducibility makes the eigenvalue \(1\) simple. Since \(W\) is stochastic, all real eigenvalues lie in \([-1,1]\). The spectral projection at \(1\) in the original coordinates equals \(\mathbf1\pi^{\mathsf T}\). Every peer-epoch operator is a polynomial in \(W\), and all epochs preserve these eigenspaces.

2. **Exactly one possible killed spectral value per epoch.** On a \(\mu\)-eigenspace, the epoch multiplier is
\[
 f_K(\mu;\alpha)
  =(1-\alpha)\sum_{j=0}^{K-1}(\alpha\mu)^j+(\alpha\mu)^K
  =\frac{1-\alpha+\alpha^{K+1}\mu^K(1-\mu)}{1-\alpha\mu}.
\]
Its denominator is strictly positive for \(0<\alpha<1\) and \(-1\leq\mu\leq1\). For \(\mu\geq0\), the numerator is strictly positive. For even \(K\), the numerator is positive for *every* \(\mu\). For odd \(K\), a zero is possible only at \(\mu=-q<0\), and is equivalent to
\[
 1-\alpha=\alpha^{K+1}q^K(1+q).
\]
For fixed \(K\) and \(\alpha\), the right side strictly increases with \(q>0\), so at most one distinct negative eigenvalue can be killed. Conversely, for every \(0<q\leq1\) and odd \(K\), its right side strictly increases with \(\alpha\in(0,1)\) while the left decreases; exactly one \(\alpha\in(0,1)\) kills \(-q\). For \(K=1\), that value is \(1/(1+q)\).

3. **Necessity, sufficiency, and optimality.** A component in any nonconstant eigenspace persists after any finite number of epochs unless one scalar multiplier is exactly zero. If some nonconstant \(\mu\geq0\) exists, every multiplier there is strictly positive, so selecting an initial vector with a component in that eigenspace disproves universal finite-time consensus, even if later controls depend on observed states. If all nonconstant eigenvalues are strictly negative, apply one \(K=1\) epoch with \(\alpha=1/(1-\mu)\) for each distinct value \(\mu\). Each epoch annihilates its selected eigenspace and preserves the Perron eigenvector, and the total product is \(\mathbf1\pi^{\mathsf T}\). Every successful schedule acting on a generic initial vector with nonzero projection in each nonconstant eigenspace needs at least \(r\) epochs, since the preceding step shows that each epoch kills at most one distinct eigenvalue. This lower bound covers arbitrary finite horizons and adaptive choices.

4. **Nonadjacent-state barrier.** If \(W_{uv}=W_{vu}=0\), the principal \(2\times2\) submatrix of \(S\) indexed by \(u,v\) is \(\mathrm{diag}(W_{uu},W_{vv})\). Cauchy interlacing gives \(\mu_2\geq\min\{W_{uu},W_{vv}\}\geq0\). For \(W=A/d\) with a simple connected regular graph, every noncomplete graph has a nonedge; for the complete graph, \(W=(\mathbf1\mathbf1^{\mathsf T}-I)/(n-1)\) has unique nonconstant eigenvalue \(-1/(n-1)\). Substitute this value into the odd-horizon equation in step 2 to obtain the displayed polynomial, with exactly one admissible root. For \(K=1\), it reduces to \(\alpha=(n-1)/n\). This proves all assertions.

## Verification

A standalone reproducibility script `VERIFY.py` checks the spectral factor formula and stochasticity on **15 nonisomorphic connected regular graphs** with up to seven vertices (360 numerical instances across \(K=1,\ldots,6\) and four susceptibilities). It checks the nonedge obstruction, a weighted complete three-state reversible instance with two distinct negative eigenvalues, unique odd-horizon roots, and an exact rational example with spectrum \(\{1,-1/12,-1/6\}\). In the latter case, the two one-inner-step susceptibilities \(\{12/13,6/7\}\) yield exactly \(\mathbf1\mathbf1^{\mathsf T}/3\), by rational arithmetic. Finite tests illustrate rather than prove the general claims.

## Relationship to prior work

Wu, Abebe, and Mendler-Dünner (2026) introduce the predictive-loop setting and explicitly derive the finite-horizon peer filter's spectral multiplier in Appendix C, Theorem 4. This expression is prior knowledge and is the starting point here; their theorem treats equilibrium decomposition and asymptotic consensus rather than an optimal exact finite-epoch control law under varying horizons. Kibangou (2012), Theorem 1, already gives the spectral polynomial product construction for undirected Laplacian consensus with unrestricted spectral step sizes; the \(K=1\) construction above is a positive-susceptibility specialization, *not* independently claimed as a new general consensus algorithm. The additional statement here is a sharp obstruction and lower bound covering the entire finite-horizon Friedkin–Johnsen filter family, including adaptive horizon and susceptibility choices, with a graph-support consequence for reversible opinions. Hendrickx, Shi, and Johansson (2013) show finite-time averaging is possible on every connected undirected graph when general time-varying positive-diagonal stochastic matrices are allowed; hence the graph-support impossibility here stems from the much narrower scalar-filter protocol, not topology alone. Charalambous and Hadjicostis (2019) also study Laplacian spectral-factor products for directed graphs and should be considered related prior work.

## Limitations

The result is strictly about exact finite-time equalization, not asymptotic convergence or approximate consensus. A noncomplete network may converge arbitrarily close in finite time without reaching exact equality. Finite horizons, strict \(0<\alpha<1\), fixed reversible \(W\), shared susceptibility, and anchor reset are essential; the conclusion does not extend to arbitrary node-specific matrices, changing topology, external steering or nonlinear feedback. The spectral factor and \(K=1\) root construction are existing algebraic ingredients; the claim of contribution is confined to the complete characterization and optimality within the finite-peer-horizon model. Other equivalent formulations of that joint result may exist in unindexed spectral-consensus literature.

## References

- J. Wu, R. Abebe, and C. Mendler-Dünner, *Reaching a Consensus in Predictive Loops*, arXiv:2603.12137, first public version 12 March 2026, especially Appendix C, Theorem 4. https://arxiv.org/abs/2603.12137 ; https://arxiv.org/pdf/2603.12137
- A. Y. Kibangou, *Graph Laplacian based Matrix Design for Finite-Time Distributed Average Consensus*, American Control Conference (2012), Theorem 1, DOI:10.1109/ACC.2012.6315398; HAL record hal-00680344. https://www.researchgate.net/publication/261158607_Graph_Laplacian_based_Matrix_Design_for_Finite-Time_Distributed_Average_Consensus
- J. M. Hendrickx, G. Shi, and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, arXiv:1302.6668, first posted 2013. https://arxiv.org/pdf/1302.6668
- T. Charalambous and C. N. Hadjicostis, *Laplacian-based matrix design for finite-time average consensus in digraphs*, CDC 2018, published 2019, DOI:10.1109/CDC.2018.8619602. https://research.aalto.fi/en/publications/laplacian-based-matrix-design-for-finite-time-average-consensus-i/
- A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, section on Cauchy interlacing of induced subgraphs. https://studylib.net/doc/10499363/spectra-of-graphs-andries-e.-brouwer-willem-h.-haemers
