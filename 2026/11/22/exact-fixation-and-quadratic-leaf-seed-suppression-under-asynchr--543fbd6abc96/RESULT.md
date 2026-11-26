# Exact fixation and quadratic leaf-seed suppression under asynchronous closed-neighborhood conformity

## Finding
For the asynchronous, pure-conformity binary imitation process defined below on the star with \(m\geq1\) leaves, the probability of eventual all-cooperator consensus is given exactly for **every** initial condition by an explicit finite product-and-sum. In particular, a single cooperative hub has fixation probability converging to a positive constant, while a single cooperative leaf has fixation probability of order \(m^{-2}\):
\[
\lim_{m\to\infty}H_m=C,\qquad
\lim_{m\to\infty}m^2L_m=2C,\qquad
C=\left[1+e^{1/2}\sqrt{\frac\pi2}\,\operatorname{erf}\!\left(\frac1{\sqrt2}\right)\right]^{-1}
=0.4148196588637697539\ldots.
\]
For comparison, under ordinary unbiased rate-one node-update copying on the same star, the respective single-hub and single-leaf fixation probabilities are \(1/2\) and \(1/(2m)\).

Set \(d=m(m+1)\) and, for integers \(0\leq j\leq m\), define
\[
R_0=1,\qquad R_j=\prod_{t=1}^{j}\frac{d+2(m-t+1)}{d+2t},\qquad
Z_m=1+\sum_{j=1}^{m}\frac{2j}{d}R_j.
\]
If the center has initial state zero and exactly \(k\) leaves have state one, the probability of eventual all-one consensus is
\[
v_k=\frac{1}{Z_m}\sum_{j=1}^{k}\frac{2j}{d}R_j.
\]
If the center has initial state one and \(k\) leaves have state one, that probability is
\[
u_k=v_k+\frac{R_k}{Z_m}.
\]
Consequently \(H_m=u_0=1/Z_m\) and \(L_m=v_1=2R_1/(dZ_m)\). These formulas cover \(0\leq k\leq m\), including the absorbing boundary cases.

## Assumptions and scope
The graph is the fixed, undirected star \(K_{1,m}\), with \(m\geq1\) integer. Each vertex has an independent rate-one exponential revision clock. On revision, a vertex \(i\) uniformly chooses one of its neighbors \(j\), computes the fraction of zero-state vertices in its **closed** neighborhood,
\[
S_i=1-\frac{s_i+\sum_{j\sim i}s_j}{\deg(i)+1},
\]
and imitates the chosen neighbor's binary state with probability \(|S_i-s_j|\); otherwise nothing happens. State one means cooperation and state zero means defection. This is the pure-conformity endpoint of the imitation probability of Manfredi, Vicario, Bilancini and Mastrandrea (2026), with **asynchronous clocks substituted for their simultaneous updating**. Their published heterogeneous-weight experiments require payoff weights strictly between zero and one; no theorem is asserted for those experiments or their synchronous model.

The only randomness is in the updating, clock times and neighbor choices. All claims refer to absorption probabilities of this explicitly specified finite-state continuous-time Markov chain, rather than to economic payoffs, environmental stochasticity or deterministic mean-field dynamics.

## Proof
**Step 1: Exact transition rates and absorption.** Let \(a_i\) be the number of neighbors whose state differs from the current state of vertex \(i\). A sampled discordant neighbor has probability \(a_i/\deg(i)\), and conditional on that selection the imitation probability is \(a_i/(\deg(i)+1)\). Thus the effective rate of flipping vertex \(i\) is
\[
\lambda_i=\frac{a_i^2}{\deg(i)(\deg(i)+1)}.
\]
Describe the state up to leaf permutation by the hub state \(h\in\{0,1\}\) and the number \(k\in\{0,\ldots,m\}\) of cooperating leaves. If \(h=1\), the positive transitions have rates \((h,k)\to(1,k+1)\) at \((m-k)/2\) and \((h,k)\to(0,k)\) at \((m-k)^2/d\). If \(h=0\), the rates are \((h,k)\to(0,k-1)\) at \(k/2\) and \((h,k)\to(1,k)\) at \(k^2/d\). In any nonconsensus configuration, repeated favorable transitions reach either absorbing consensus, so a finite-chain closed communicating class cannot be disjoint from the two consensus states. Absorption occurs almost surely.

**Step 2: Harmonic equations and finite exact solution.** Write \(u_k\) and \(v_k\) for the all-one absorption probability with hub in state one and zero, respectively, and \(w_k=u_k-v_k\). Harmonicity gives, for \(0\leq k<m\),
\[
u_{k+1}-u_k=\frac{2(m-k)}{d}\,w_k,
\]
and, for \(1\leq k\leq m\),
\[
v_k-v_{k-1}=\frac{2k}{d}\,w_k.
\]
The boundary values are \(v_0=0\) and \(u_m=1\). Subtracting successive equations yields
\[
\frac{w_{k+1}}{w_k}=
\frac{d+2(m-k)}{d+2(k+1)},\qquad 0\leq k<m.
\]
Hence \(w_k=w_0R_k\). The finite-product identity \(R_m=1\) follows by reversing numerator indices. Summing the \(v\)-increments and using \(u_m=1=v_m+w_m\) shows \(w_0=Z_m^{-1}\), proving both exact formulas. Uniqueness follows from finite absorbing-chain harmonic uniqueness; no unproved enumeration is required.

**Step 3: Uniform product limit.** Since \(d=m(m+1)\), Taylor's estimate \(\log(1+x)=x+O(x^2)\) applies uniformly to each product factor, with \(0\leq x\leq 2/m\). For all \(0\leq k\leq m\), summing the uniform remainders gives
\[
\log R_k=\frac{2}{d}\sum_{j=1}^{k}(m-2j+1)+O(m^{-1})
=\frac{2k(m-k)}{d}+O(m^{-1}).
\]
The error constant is uniform in \(k\), so \(R_{\lfloor mx\rfloor}\to e^{2x(1-x)}\) uniformly in \(x\in[0,1]\). Therefore, by a bounded Riemann sum,
\[
Z_m\to 1+\int_0^1 2x e^{2x(1-x)}\,dx
=1+e^{1/2}\sqrt{\frac\pi2}\operatorname{erf}\!\left(\frac1{\sqrt2}\right).
\]
The integral equals \(\int_0^1e^{2x(1-x)}dx\) by symmetry around \(1/2\). Finally, \(R_1=(d+2m)/(d+2)\to1\), and \(2m^2/d\to2\); the two limits follow.

**Step 4: Classical voter baseline.** In the ordinary rate-one node-update voter process, \(\sum_i\deg(i)s_i\) is a martingale on every finite undirected graph: opposite orientations of each discordant edge have equal contributions after degree weighting. Its terminal values are zero and \(2m\) on a star, giving initial single-hub probability \(m/(2m)=1/2\) and single-leaf probability \(1/(2m)\). The conformity dynamics is nonlinear; this baseline is only a comparison.

## Verification
Run `python3 CHECK.py` using the Python standard library. The checker independently solves the full \(2m\)-state absorbing-chain linear system over exact rational numbers, rather than using the product recurrence, for every \(1\leq m\leq10\). It matches all \(u_k,v_k\) entries exactly and checks monotonicity and the positive hub-influence gap, totaling 295 exact assertions. It also prints finite-size approximations for selected sizes; these finite calculations do not prove the infinite limits. The uniform-product argument in the proof supplies that justification.

## Relationship to prior work
Manfredi, Vicario, Bilancini and Mastrandrea (2026) introduce the closed-neighborhood conformity score in a spatial public-goods game and study **simultaneous** heterogeneous payoff-plus-conformity updating on larger network families. Their model equations, results and appendices were examined; the current result analyzes a distinct asynchronous, pure-conformity boundary process and does not attribute these new calculations to their original synchronous system.

Min and San Miguel (2017) study a coevolving nonlinear voter process whose fixed-graph flip rule is a power of the discordant-neighbor fraction; for nonlinear exponent two, it resembles the present update but has different degree normalization. They investigate network phases, not the stated star fixation formula or the quadratic-vs-linear leaf-seed asymptotics. Castellano, Muñoz and Pastor-Satorras (2009) study the nonlinear voter model, particularly on complete graphs. Kátai-Urbán, Pongrácz and Szabó (2024) study discordant star voting protocols with different selection mechanisms and time-to-consensus results.

An indexed context-dependent voting result on stars gives an order-\(m^{-1}\) leaf effect, not the order-\(m^{-2}\) law here. A separate indexed nonlinear-star result concerns whether an initially dissenting hub converts all leaves **before its first flip**, not the unconditional eventual all-one fixation probability. The available indexed summaries do not establish coverage, and their inaccessible full text is a remaining historical-priority risk; no claim of absolute literature uniqueness is made.

## Limitations
This is a mathematically exact result for the specified asynchronous endpoint model, not for the parent paper's synchronous heterogeneous-payoff dynamics, or for its economically interior parameter range. The result does not assess mixing/consensus time, nonlinear payoff effects, empirical behavioral validity or arbitrary graph families. Finite verification is supplementary only. Independent replication and an independent originality audit remain to be performed.

## References
1. R. Manfredi, E. Vicario, E. Bilancini and R. Mastrandrea, *Public Goods Game on Complex Networks: the interplay between conformity and topology*, arXiv:2607.23131v1 (first public release 2026-07-25), https://arxiv.org/abs/2607.23131.
2. B. Min and M. San Miguel, *Fragmentation transitions in a coevolving nonlinear voter model*, Scientific Reports **7**, 12864 (2017), https://doi.org/10.1038/s41598-017-13047-2.
3. C. Castellano, M. A. Muñoz and R. Pastor-Satorras, *Nonlinear q-voter model*, Physical Review E **80**, 041129 (2009), https://doi.org/10.1103/PhysRevE.80.041129.
4. K. Kátai-Urbán, A. Pongrácz and C. Szabó, *Voting protocols on the star graph*, Acta Scientiarum Mathematicarum **90**, 41–51 (2024), https://doi.org/10.1007/s44146-024-00125-x.
