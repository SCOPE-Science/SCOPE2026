# Sharp stationary-mass comparison threshold for nonlinear explicit–implicit–null diffusion

## Finding
Let \(Q\) be the generator of an irreducible finite continuous-time Markov chain with \(n\ge2\) states, row sums zero, and stationary probabilities \(\pi_i>0\). Let \(A>0\). For every differentiable nondecreasing scalar flux \(\phi\colon\mathbb R\to\mathbb R\) with \(\phi(0)=0\) and \(0\le\phi'(s)\le A\) for all \(s\), consider the first-order stabilized explicit–implicit–null (EIN) discretization of \(\dot u=Q\phi(u)\),
\[
T_{\tau,\alpha}(u)
=(I-\tau\alpha Q)^{-1}\bigl[u+\tau Q(\phi(u)-\alpha u)\bigr],
\qquad \tau>0,\ \alpha>0.
\]
The flux is applied coordinatewise. Write \(\pi_{\min}=\min_i\pi_i\) and \(E(u)=\sum_i\pi_i\int_0^{u_i}\phi(s)\,ds\). There are two *exact, generally different* thresholds, quantified uniformly over every positive step size, every starting vector, and every flux in the stated class:

1. **Convex-energy dissipation:** \(E(T_{\tau,\alpha}(u))\le E(u)\) universally if and only if \(\alpha\ge A/2\).
2. **Componentwise comparison:** \(u\le v\Rightarrow T_{\tau,\alpha}(u)\le T_{\tau,\alpha}(v)\) universally if and only if
\[
\boxed{\alpha\ge A(1-\pi_{\min}).}
\]

At the second threshold the update also preserves every componentwise constant bound: if \(a\le u_i\le b\) for all \(i\), then \(a\le (T_{\tau,\alpha}(u))_i\le b\) for all \(i\). In particular it preserves nonnegative data. Both bounds are sharp even when the flux is linear, and both remain valid without detailed balance. Their gap is strictly positive whenever \(\pi_{\min}<1/2\), including every irreducible chain with at least three states.

The critical structural input is the nonreversible resolvent return inequality
\[
\boxed{[(I-tQ)^{-1}]_{ii}\ge\pi_i\quad(t\ge0),\qquad
\lim_{t\to\infty}[(I-tQ)^{-1}]_{ii}=\pi_i.}
\]
The inequality concerns exponential-time resolvent returns, *not* the fixed-time transition probability \([e^{tQ}]_{ii}\), which need not stay above its stationary value for nonreversible chains.

## Assumptions and scope
The generator is in row convention: \(q_{ij}\ge0\) for \(i\ne j\), \(Q\mathbf 1=0\), and the directed positive-rate graph is strongly connected. Then \(\pi^\mathsf T Q=0\), \(\sum_i\pi_i=1\), \(\pi_i>0\). The Markov generator acts on *column* fields; the weighted integral \(\pi^\mathsf T u\), rather than the unweighted sum, is conserved. The scalar flux is \(C^1\) globally, \(\phi(0)=0\), \(0\le\phi'\le A\). All statements hold for every real input state and arbitrary \(\tau>0\); \(\alpha\) is a constant independent of time and state. We require no reversibility, symmetry of \(Q\), graph regularity, or upper bound on jump rates.

The inequalities are sharp for the *entire flux class*. They do not assert that the same numerical value is necessary for a single fixed flux whose actual maximum derivative is substantially smaller than \(A\). The norm used below is \(\|u\|_\pi^2=\sum_i\pi_i u_i^2\).

## Proof
**1. Exact one-step representation.** Put \(t=\tau\alpha\) and \(P_t=(I-tQ)^{-1}\). The EIN equation rearranges to
\[
T_{\tau,\alpha}(u)-u
=\tau Q\bigl[\phi(u)+\alpha(T_{\tau,\alpha}(u)-u)\bigr].
\]
Using \(tP_tQ=P_t-I\), we obtain the exact nonlinear map
\[
T_{\tau,\alpha}(u)
=u+\alpha^{-1}(P_t-I)\phi(u).
\tag{1}
\]
The generator property implies the resolvent representation
\[
P_t=\int_0^\infty e^{-s}e^{stQ}\,ds.
\]
Therefore \(P_t\) is entrywise nonnegative, \(P_t\mathbf1=\mathbf1\), and \(\pi^\mathsf TP_t=\pi^\mathsf T\). Formula (1) preserves all constant fields and the stationary weighted mass \(\pi^\mathsf Tu\).

**2. Dissipativity for possibly directed chains.** For arbitrary real \(z\), stationarity gives
\[
\langle z,Qz\rangle_\pi
=-\tfrac12\sum_{i\ne j}\pi_iq_{ij}(z_i-z_j)^2\le0.
\tag{2}
\]
Indeed expand the right side, use row conservation for the terms \(z_i^2\) and \(\pi^\mathsf TQ=0\) for the terms \(z_j^2\). No detailed balance is used. Set \(w=T_{\tau,\alpha}(u)\), \(d=w-u\), and \(z=\phi(u)+\alpha d\); then \(d=\tau Qz\). By the scalar Taylor bound from \(\phi'\le A\),
\[
\begin{aligned}
E(w)-E(u)
&\le\langle\phi(u),d\rangle_\pi+\tfrac A2\|d\|_\pi^2\\
&=\tau\langle z,Qz\rangle_\pi-(\alpha-A/2)\|d\|_\pi^2\le0
\end{aligned}
\]
when \(\alpha\ge A/2\). To prove *necessity over the flux class*, take \(\phi(s)=As\) and any nonzero \(u\) with \(\pi^\mathsf Tu=0\). Irreducibility implies \(P_tu\to0\) as \(t\to\infty\), so (1) gives \(w\to(1-A/\alpha)u\). The quadratic energy ratio then tends to \((1-A/\alpha)^2>1\) when \(0<\alpha<A/2\). Thus some finite step has greater energy.

**3. The nonreversible resolvent return lemma.** For each \(i\), define \(f=e_i/\pi_i-\mathbf1\). Then \(\pi^\mathsf Tf=0\). For \(t>0\), let \(g=P_tf\), equivalently \(f=(I-tQ)g\). Stationarity and \(\pi^\mathsf TP_t=\pi^\mathsf T\) yield
\[
\frac{(P_t)_{ii}}{\pi_i}-1
=\langle f,P_tf\rangle_\pi
=\|g\|_\pi^2-t\langle Qg,g\rangle_\pi\ge0,
\tag{3}
\]
by (2). This proves \((P_t)_{ii}\ge\pi_i\) for *any* irreducible finite generator. Standard finite-chain ergodicity yields \(e^{sQ}\to\mathbf1\pi^\mathsf T\) as \(s\to\infty\); dominated convergence in the resolvent integral, or the spectral limit of \((I-tQ)^{-1}\), gives \(P_t\to\mathbf1\pi^\mathsf T\) as \(t\to\infty\). Hence \(\inf_{t>0}(P_t)_{ii}=\pi_i\), even though fixed-time transition returns need not decrease monotonically.

**4. Comparison sufficiency.** Differentiating (1) gives for every \(i,j\),
\[
\frac{\partial(T_{\tau,\alpha}(u))_i}{\partial u_j}
=\delta_{ij}+\frac{\phi'(u_j)}\alpha\bigl[(P_t)_{ij}-\delta_{ij}\bigr].
\tag{4}
\]
For \(i\ne j\) these entries are nonnegative. For \(i=j\), (3) implies
\[
\frac{\partial T_i}{\partial u_i}\ge
1-\frac A\alpha(1-\pi_i)\ge0
\]
when \(\alpha\ge A(1-\pi_{\min})\). All Jacobian entries are therefore nonnegative. Integrating the Jacobian along the segment between any ordered inputs gives componentwise monotonicity. Since \(T_{\tau,\alpha}(c\mathbf1)=c\mathbf1\) for every real \(c\), comparison with constant fields proves the maximum principle.

**5. Comparison necessity, with actual negative values.** Suppose \(0<\alpha<A(1-\pi_{\min})\). Choose \(i\) with \(\pi_i=\pi_{\min}\), and choose \(\phi(s)=As\). Formula (4) is now the constant matrix
\[
H_t=\bigl(1-A/\alpha\bigr)I+(A/\alpha)P_t.
\]
Its \(i\)-th diagonal element approaches \(1-(A/\alpha)(1-\pi_i)<0\) as \(t\to\infty\). Thus for some *finite* \(t\), \(H_te_i\) has a negative \(i\)-th coordinate even though \(e_i\ge0\). The same witness shows failure of order preservation and of the maximum principle. This proves necessity without requiring any special chain construction.

For an explicit contrast, on the directed unit-rate three-cycle \(\pi=(1/3,1/3,1/3)\), so the energy threshold is \(A/2\) but the exact comparison threshold is \(2A/3\). At \(\alpha=A/2\), for nonnegative input \(e_1\), the large-step update tends to \((-1/3,2/3,2/3)^\mathsf T\): the method remains convex-energy dissipative at every finite step while eventually producing a negative component. This example demonstrates that energy stability alone does not enforce positivity.

## Verification
Run `python3 verify.py`. The standalone script uses standard-library rational arithmetic to invert resolvents and check stationary distributions, the weighted conservation law, the return inequality, the exact linear update, nonnegative comparison matrices at the predicted threshold, and negative diagonal witnesses below it. Cases include asymmetric two-state chains, a directed three-cycle, an asymmetric strongly connected three-state chain, and a four-state directed chain at several rational step sizes. It also runs deterministic numerical checks on the nonlinear flux \(\phi(s)=3\tanh s\) and potential \(3\log\cosh s\). All finite checks supplement rather than substitute for the analytic proof in arbitrary dimension. Recorded result: 976 passed assertions under Python 3 with no third-party dependencies.

## Relationship to prior work
Wu and Shu, arXiv:2610.34539v1, establish energy stability of first- through third-order EIN schemes for nonlinear degenerate parabolic problems, including first-order stabilization under derivative bounds. Wang, Zhang, Wang and Shu, arXiv:1903.11859, already describe the familiar half-diffusivity energy stabilization requirement for a simplified model. Accordingly the bound \(\alpha\ge A/2\) is **not** presented as novel by itself.

The new assertion is the exact *all-steps, all-fluxes* stationary-mass order-preservation threshold \(\alpha=A(1-\pi_{\min})\) on every irreducible finite, potentially nonreversible Markov generator, together with a proof that the energy criterion and the maximum principle diverge sharply. A prior published result on Crank–Nicolson positivity, *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, obtains the diagonal resolvent test for the Cayley update and sharp reversible-chain thresholds. In our special linear case \(\alpha=A/2\), equation (1) indeed reduces to that Cayley map; this overlap is acknowledged. The present result is not a new Cayley identity: it instead optimizes the free EIN stabilization parameter uniformly over nonlinear monotone fluxes and establishes the nonreversible stationary-mass lower envelope needed for the universal result.

Other literature develops bound-preserving EIN methods with additional sweeping or positivity-correction steps, and positivity-preserving Fokker–Planck penalization. Those different algorithms are not assertions about the sharp unrestricted parameter in the unmodified first-order EIN map. The identified claim has not been independently audited; unindexed prior results under Markov resolvent, monotone splitting, or nonlinear invariant-domain terminology remain a genuine originality risk.

## Limitations
The result concerns only the *first-order* unswept EIN step, finite conservative generators, a single globally Lipschitz nondecreasing scalar flux shared across coordinates, and exact arithmetic. It does not cover general spatial stiffness matrices without the generator sign condition, state-dependent graph weights, different fluxes at different vertices, open-system boundary forcing, or higher-order time integration. Sharpness is universal over all allowed fluxes, not necessarily for every individual flux. No claim of independent expert or formal-machine verification is made. In applications, a bound on \(\phi'\) only along the actual trajectory could permit a less conservative, state-specific parameter.

## References
1. Yue Wu and Chi-Wang Shu, *Energy stability of explicit--implicit--null time discretizations for nonlinear degenerate parabolic equations with state-dependent coefficients*, arXiv:2610.34539v1, first posted 2026-10-25. https://arxiv.org/abs/2610.34539
2. Haijin Wang, Qiang Zhang, Shiping Wang and Chi-Wang Shu, *Local discontinuous Galerkin methods with explicit-implicit-null time discretizations for solving nonlinear diffusion problems*, arXiv:1903.11859, first posted 2019-03-28. https://arxiv.org/abs/1903.11859
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published mathematical record, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a
4. *An efficient high-order bound-preserving explicit-implicit-null time integration for the Richards equation in unsaturated geotechnical media*, 2026. https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2026/04/An-efficient-high-order-bound-preserving-explicit-implicit-null-time.pdf
5. Hamad El Kahza, Luis Chacón, William Taitano, Jingmei Qiu and Jingwei Hu, *A Structure-Preserving Penalization Method for the Single-species Rosenbluth-Fokker-Planck Equation*, arXiv:2601.08006, first posted 2026-01-12. https://arxiv.org/abs/2601.08006
