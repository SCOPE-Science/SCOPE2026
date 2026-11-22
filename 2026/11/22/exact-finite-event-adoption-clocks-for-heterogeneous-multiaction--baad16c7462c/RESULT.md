# Exact finite-event adoption clocks for heterogeneous multiaction opinion networks

## Finding
For any finite self-consistent multiaction opinion network with at least four public action levels and a fixed robust seed broadcasting an action \(a\), two extremal outsider trajectories determine exactly which outsiders adopt \(a\) permanently from **every** admissible initial profile. The first time both extremal trajectories express \(a\) at an outsider is its sharp worst-case uniform permanent-adoption time. An event-driven procedure needs at most \(2|B|(L-1)\) individual action-level changes across both extremal trajectories, regardless of how many ordinary time steps separate events. A four-agent rational example gives exact worst-case full adoption time four even though the existing sufficient scalar cascade stops at its seed.

## Assumptions and scope
Let \(V\) be a finite set of \(N\ge2\) agents. Let \(W=(W_{ij})\) be nonnegative with \(\sum_jW_{ij}=1\) and \(W_{ii}=0\), and choose \(0<\alpha_i<1\). Let the ordered action alphabet be \(\mathcal A=\{a_1<\cdots<a_L\}\subset[-1,1]\), with \(L\ge4\). Each quantizer \(q_i:[-1,1]\to\mathcal A\) uses thresholds \(-1<\theta_{i,1}<\cdots<\theta_{i,L-1}<1\), assigning the *higher* action at a threshold: \(q_i(x)=a_k\) for \(\theta_{i,k-1}\le x<\theta_{i,k}\), with conventional infinite endpoint thresholds. Impose self-consistency \(q_i(a_k)=a_k\) for all \(i,k\).

At integer times \(t\ge0\), private opinions evolve by
\[
x_i(t+1)=\alpha_ix_i(t)+(1-\alpha_i)\sum_{j\in V}W_{ij}q_j(x_j(t)).
\]
Fix \(a\in\mathcal A\) and a nonempty **robust seed** \(S\subseteq V\): if all seeds initially express \(a\), they continue expressing \(a\) at every time, independent of other agents' initial opinions. All admissible initial profiles are unrestricted in \([-1,1]\) outside \(S\), and constrained only by \(q_i(x_i(0))=a\) for \(i\in S\). The target is **uniform guaranteed permanent adoption** by an outsider, not eventual convergence of arbitrary nonadopting opinion trajectories. Write \(B=V\setminus S\).

For \(i\in B\), define the frozen-seed map
\[
F_i(z)=\alpha_i z_i+(1-\alpha_i)\left(a\sum_{j\in S}W_{ij}+\sum_{j\in B}W_{ij}q_j(z_j)\right), \qquad z\in[-1,1]^B.
\]
Set \(\ell(0)=(-1)_{i\in B}\), \(u(0)=(1)_{i\in B}\), \(\ell(t+1)=F(\ell(t))\), and \(u(t+1)=F(u(t))\). For each outsider define
\[
T_i=\min\{t\ge0:q_i(\ell_i(t))=q_i(u_i(t))=a\},
\]
with \(\min\varnothing=\infty\).

**Theorem.** The outsider \(i\) adopts \(a\) permanently from every admissible initial profile if and only if \(T_i<\infty\). In that case \(T_i\) is the least uniform time after which all admissible profiles express \(a\) at that agent forever. The full-network least uniform takeover time is \(\max_{i\in B}T_i\) if finite. The extremal action trajectories can be evaluated with a finite event-skipping algorithm using at most \(2|B|(L-1)\) individual action-level transitions in total, including jumps over multiple levels.

## Proof
**Order trapping.** The componentwise map \(F\) is order preserving since the quantizers, weights, and inertia coefficients are nonnegative. Its image lies in \([-1,1]^B\), whence \(\ell(1)\ge\ell(0)\) and \(u(1)\le u(0)\). Induction gives \(\ell(t)\le\ell(t+1)\le u(t+1)\le u(t)\) for all \(t\). Every admissible outsider trajectory obeys \(\ell(t)\le x_B(t)\le u(t)\) by the comparison principle. In particular the lower extremal actions never decrease and the upper extremal actions never increase. Each of their \(|B|\) coordinates changes action level at most \(L-1\) times, hence the stated joint bound. This does not require the original full-system trajectories to converge.

**Necessity, sufficiency, and sharpness of the clock.** Both extreme outsider initializations are admissible because seed broadcasts remain \(a\) by robustness, irrespective of seed private opinions. If both extremal actions at coordinate \(i\) equal \(a\) at time \(T\), every intervening trajectory must then have action \(a\). For later times the lower extremal action cannot fall below \(a\), and the upper extremal action cannot rise above \(a\); since the former remains at most the latter, both remain exactly \(a\), trapping every trajectory forever. Conversely if all admissible trajectories eventually permanently express \(a\) at \(i\), the two extremes do so individually; taking the later of their two finite adoption times gives a common time. If \(t<T_i\), at least one extremal trajectory is not expressing \(a\) at \(i\). Hence no smaller *uniform* guarantee is possible, and \(T_i\) is exact. The statement also covers \(B=\varnothing\), with full action unanimity at time zero.

**Exact event skipping.** At any extremal time \(t\) when the current outsider action profile is \(c_j=q_j(z_j(t))\), write
\[
b_i=a\sum_{j\in S}W_{ij}+\sum_{j\in B}W_{ij}c_j.
\]
Until the next action change the constant-input recurrence has the exact solution
\[
z_i(t+h)=b_i+(z_i(t)-b_i)\alpha_i^{h},\qquad h=0,1,\ldots.
\]
For the lower trajectory, if the present action level is \(a_k\) with \(k<L\), the next upward transition occurs at the least integer \(h\ge1\) satisfying \(z_i(t+h)\ge\theta_{i,k}\), **provided** \(b_i>\theta_{i,k}\). If this strict inequality fails, that coordinate will never switch while this action profile persists. For the upper trajectory, if its present level is \(a_k\) with \(k>1\), the next downward transition occurs at the least integer \(h\ge1\) satisfying \(z_i(t+h)<\theta_{i,k-1}\), **provided** \(b_i<\theta_{i,k-1}\). These strict feasibility tests cover equality of an asymptote with a threshold: approach from the wrong side does not cross at finite time. Obtain each positive crossing time by monotone integer comparisons (exponential search followed by integer bisection for rational/exact arithmetic); advance all coordinates simultaneously by the smallest such time and recompute actions. If no crossing is feasible, the action profile is permanent. Every event changes at least one action, so the event count is bounded as above and the algorithm terminates; the precise times are recovered, not merely the eventual actions.

**Four-action rational certificate.** Take \(\mathcal A=\{-1,0,9/10,1\}\), four agents, target \(a=0\), seed \(S=\{1,2\}\), \(\alpha_i=1/2\), and
\[
W=\begin{pmatrix}
0&1&0&0\\ 1&0&0&0\\ 2/5&0&0&3/5\\2/5&0&3/5&0
\end{pmatrix}.
\]
Let the threshold triples of agents \(1,2\) be \((-1/2,1/4,19/20)\), of agent \(3\) be \((-4/5,3/10,19/20)\), and of agent \(4\) be \((-3/10,4/5,19/20)\). All satisfy self-consistency. Agents \(1,2\) receive only each other's action zero, so the interval containing zero is preserved and \(S\) is robust. For outsiders \((3,4)\) the lower extremal action profile is \((-1,-1)\) at \(t=0\), \((0,-1)\) at \(t=1\), and \((0,0)\) at \(t=3\); the upper is \((1,1)\) at \(t=0\), \((9/10,9/10)\) at \(t=1\), \((9/10,0)\) at \(t=2\), and \((0,0)\) at \(t=4\). Thus the exact least uniform full action takeover time is \(T=4\). The seed weight is \(2/5\) at each outsider, whereas both have the previously studied sufficient one-threshold admission requirement \(7/10\); that scalar cascade admits neither outsider. The four-action example illustrates that an exact guarantee can be obtained beyond that sufficient cascade, not that a four-action network is the smallest such example.

## Verification
The standalone `quantized_adoption_checker.py` uses exact Python fractions to verify every claimed example action/event time, the seed weight and threshold values, and the sharp time-four boundary. Separately it cross-checks the analytic event-skip algorithm against 260 directly iterated lower/upper rational trajectories, each for 200 updates, across 130 three- and four-level parameter configurations. All tests passed. Run with `python quantized_adoption_checker.py` in a Python 3 environment; no third-party packages are needed. Finite numerical checks are illustrative; the general infinite-horizon statement is established by the order and finite-event proofs above.

## Relationship to prior work
Munif, Couthures, Varma, Lasaulce, and Başar (2026, arXiv:2607.16036v1; first publicly released July 17, 2026) motivate quantized communication via strategic network interaction; we do **not** assert that every quantizer in this theorem is a game equilibrium of that communication model. The later Munif–Couthures–Varma–Lasaulce–Morărescu paper (arXiv:2611.21446v1, November 16, 2026) defines the exact fixed-rule dynamics here and proves map monotonicity, robust seed criteria and a sufficient scalar cascade. It expressly states that for more than two public actions the cascade is only sufficient. These are pre-existing ingredients, not claimed discoveries. The contribution assessed here is the **necessary-and-sufficient, event-finite extremal adoption algorithm and sharp universal initial-state clocks** for all finite alphabets, particularly the four-or-more-action regime, rather than merely another sufficient edge-weight test. Ceragioli and Frasca (2018) analyze a different continuous-time quantized-behavior model.

## Limitations
The result requires a fixed robust seed, synchronous deterministic updates, finite ordered action levels, monotone self-consistent quantizers, and fixed nonnegative stochastic weights. It does not compute whether a given seed is robust (this may be separately tested using known criteria), infer unknown parameters, provide a polynomial bit-complexity guarantee for event times, certify noise-robust guarantees, or establish convergence of arbitrary nonadopting trajectories. Exact event-time evaluation requires exact threshold and parameter comparisons; finite decimal floating-point arithmetic near a threshold can misclassify equality. The July source's complete full text was not obtained for an additional whole-document implication check; the closely relevant November full article was read. Independent external validation has not been performed, and undiscovered historical equivalences remain possible.

## References
1. H. Munif, A. Couthures, V. S. Varma, S. Lasaulce, and T. Başar, *Network-Induced Strategic Communication in Opinion Dynamics*, arXiv:2607.16036v1 (2026), https://arxiv.org/abs/2607.16036.
2. H. Munif, A. Couthures, V. S. Varma, S. Lasaulce, and I.-C. Morărescu, *Robust Action Clusters and Cascades in Opinion Dynamics with Heterogeneous Action Thresholds*, arXiv:2611.21446v1 (2026), https://arxiv.org/html/2611.21446v1.
3. F. Ceragioli and P. Frasca, *Consensus and Disagreement: The Role of Quantized Behaviors in Opinion Dynamics*, SIAM Journal on Control and Optimization (2018), https://doi.org/10.1137/16M1083402.
