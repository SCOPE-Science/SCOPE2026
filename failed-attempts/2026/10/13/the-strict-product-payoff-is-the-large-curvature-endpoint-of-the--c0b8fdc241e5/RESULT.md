# The strict product payoff is the large-curvature endpoint of the power-law public-goods model
## Finding
Tang and Rao use binary strategies \(s_i\in\{0,1\}\) and the three-player payoff
\[
u_{i,\gamma}^{(3)}(i,j,k)=3\alpha r\left(\frac{S_{ijk}}3\right)^\gamma-s_i,
\qquad S_{ijk}=s_i+s_j+s_k.
\]
Section 6 replaces the collective-return term by the strict product payoff
\[
u_{i,\mathrm{prod}}^{(3)}(i,j,k)=3\alpha r\,s_i s_j s_k-s_i.
\]
On the binary state space these are not unrelated functional forms: the latter is exactly the \(\gamma\to\infty\) endpoint of the former.

Uniformly over all eight triad configurations,
\[
\left|u_{i,\gamma}^{(3)}-u_{i,\mathrm{prod}}^{(3)}\right|
\le3\alpha r\left(\frac23\right)^\gamma.
\]
Writing
\[
q_*=\max_i\frac{d_i^{(3)}}{d_i^{(2)}+d_i^{(3)}},
\]
the source's normalized total payoff satisfies
\[
\max_i|U_i^\gamma-U_i^\infty|
\le3\alpha r q_*\left(\frac23\right)^\gamma.
\]
The source's Fermi update and mutation rule then give
\[
\sup_x\|P_\gamma(x,\cdot)-P_\infty(x,\cdot)\|_{\mathrm{TV}}
\le
\min\!\left\{1,\frac32\alpha r q_*\left(\frac23\right)^\gamma\right\}.
\]
Consequently every fixed finite-time law converges to the strict-product law, and for positive mutation the unique stationary law converges as well.

This does not refute the reported bistability or discontinuous transition. It sharpens the interpretation of the Section 6 comparison: mathematically it is a boundary-point test within the original normalized power-law family.

## Assumptions and scope
The hypergraph is finite, every player has at least one game and a nonempty model-player set, and
\[
\alpha>0,\qquad r>0,\qquad 0<\mu<1.
\]
The source uses \(\mu=0.002\). One Markov step means one focal-player Fermi update followed by mutation. The same hypergraph and focal/model selection rule are used for all \(\gamma\).

The theorem is finite-\(N\). It does not exchange \(N\to\infty\) with \(\gamma\to\infty\), does not prove a thermodynamic phase transition, and does not claim that \(\gamma=2\) is numerically close to the product endpoint.

## Proof
For \(S\in\{0,1,2,3\}\),
\[
\lim_{\gamma\to\infty}(S/3)^\gamma=\mathbf 1_{\{S=3\}}.
\]
For binary strategies,
\[
\mathbf 1_{\{S=3\}}=s_i s_j s_k.
\]
The largest error among \(S<3\) occurs at \(S=2\), so
\[
\left|(S/3)^\gamma-s_i s_j s_k\right|\le(2/3)^\gamma.
\]
This proves the triad-payoff bound.

The pairwise payoff is unchanged. Equation (4) averages all game contributions, hence
\[
|U_i^\gamma-U_i^\infty|
\le
\frac{d_i^{(3)}}{d_i^{(2)}+d_i^{(3)}}3\alpha r(2/3)^\gamma.
\]
Let \(B_\gamma=3\alpha r q_*(2/3)^\gamma\). A focal/model payoff gap changes by at most \(2B_\gamma\). For
\[
F(z)=\frac1{1+e^z},
\]
we have \(|F'(z)|\le1/4\), so
\[
|W_\gamma-W_\infty|\le B_\gamma/2.
\]
Conditioning on a focal/model pair, the only changed Bernoulli parameter is this imitation probability. The common mutation channel is a total-variation contraction, and mixing over the same pair-selection rule cannot enlarge the maximum conditional distance. This gives the one-step bound.

Telescoping Markov kernels and total-variation contraction yield
\[
\|\delta_xP_\gamma^t-\delta_xP_\infty^t\|_{\mathrm{TV}}
\le t\varepsilon_\gamma.
\]
The bound is capped by one.

With \(0<\mu<1\), any selected player's bit can change with positive probability, and a positive self-transition also exists. Under nonempty partner sets, every binary configuration communicates with every other by single-site changes; the finite chain is irreducible and aperiodic. Thus each kernel has a unique stationary law. Since \(P_\gamma\to P_\infty\) entrywise, any subsequential limit of \(\pi_\gamma\) is stationary for \(P_\infty\), so uniqueness forces \(\pi_\gamma\to\pi_\infty\).

## Verification
The bundled `verification/verify.py` exhausts the eight binary triad states and checks the sharp mixed-state error bound. It also constructs the full one-update transition matrices for a three-player test hypergraph using the source's normalized payoff, Fermi rule, and mutation step, then checks the row-wise total-variation estimate for several increasing \(\gamma\).

The finite computation is a replay of the algebra. The arbitrary-hypergraph theorem follows from the uniform payoff estimate, the global \(1/4\) Lipschitz bound for the Fermi map, and finite-state Markov-chain uniqueness.

## Relationship to prior work
The motivating article explicitly presents the strict product payoff as a different functional form motivated by complementary cooperation, and reports the same first-order-like behavior found for convex power-law returns. Its own formulas imply the exact endpoint relation
\[
s_i s_j s_k=\lim_{\gamma\to\infty}\left(\frac{s_i+s_j+s_k}{3}\right)^\gamma.
\]
The full text does not state this nesting or its stochastic-dynamics consequence.

Civilini et al. established explosive cooperation and bistability from higher-order interactions. Llabrés et al. studied nonlinear higher-order public-goods games and found that transition type changes with nonlinearity. These are broader precedents for abrupt cooperation transitions; they do not supply the source-specific payoff-family endpoint theorem stated here.

## Limitations
The one-step estimate controls fixed finite horizons but is not a system-size-uniform mixing theorem. Stationary convergence is proved for each fixed finite hypergraph with positive mutation.

The endpoint identity is mathematically simple once the two formulas are juxtaposed. Its scientific value here is source-specific: it changes the interpretation of a dedicated robustness experiment and extends the identity from local payoffs to the complete finite stochastic process.

The result does not challenge the source's numerical evidence for bistability, hysteresis, cascade-like triad growth, or the economic interpretation of complementary cooperation.

## References
1. F. Tang, W. Rao, “Curvature of Collective Returns Reshapes the Cooperation Transitions in Higher-Order Public Goods Games,” Axioms 15 (2026), 617. DOI: 10.3390/axioms15080617.
2. A. Civilini, O. Sadekar, F. Battiston, J. Gómez-Gardeñes, V. Latora, “Explosive Cooperation in Social Dilemmas on Higher-Order Networks,” Physical Review Letters 132 (2024), 167401. DOI: 10.1103/PhysRevLett.132.167401.
3. J. Llabrés, O. Sadekar, F. Malizia, F. Battiston, “Emergence of cooperation in nonlinear higher-order public goods games,” Physical Review E 114 (2026), 034316. DOI: 10.1103/54zg-75zk.
