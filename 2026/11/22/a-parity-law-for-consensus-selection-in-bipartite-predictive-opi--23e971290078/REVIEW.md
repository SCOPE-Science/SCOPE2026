# Scientific review: bipartite predictive-loop parity law

## Correctness

PASS. The finite-step Friedkin--Johnsen response is the stochastic matrix \(\Psi_K=\sum_{r=0}^{K-1}(\Lambda W)^r(I-\Lambda)+(\Lambda W)^K\). Reciprocal bipartite edges ensure that the two part-restricted degree-distribution rows form a closed invariant left space, where the dynamics reduce exactly to a two-state stochastic response. The identity \(H^2=abI\) proves an even-round stationary measure independent of the number of pairs of steps and gives the different odd-round measure. Primitive stochastic convergence, not numerical simulation, establishes the high-platform-susceptibility consensus selection. The star example follows by exact substitution. The accompanying standard-library checker independently compared full stochastic matrices and resolvent fixed points with the closed formula on 4,752 rational test cases. Its finite checks corroborate but cannot replace the general argument.

## Originality

PASS with bounded historical-priority risk. The originating work [1] supplies the general finite-round model and resolvent, not the bipartite all-graph parity classification or hub-size-independent selection. The closest indexed result [2] proves a stationary-weight contraction for the infinite-peer-round operator; its stationary weights agree with the even-round specialization here and are credited. [2] explicitly excludes finite peer-relaxation lengths. A related FJ Green-operator study [3] considers boundary-value influence without repeated platform feedback. Searches for reciprocal bipartite parity, odd/even peer-step consensus selection, graph-independent class weights, and finite-round predictive opinion loops yielded no stronger coverage in the materially inspected sources. Algebraic consequence of existing model equations alone is not a claim of independent model invention. Unindexed or incompletely accessible work could affect priority.

## Value

PASS. A natural, experimentally meaningful choice—the number of peer updates between successive prediction deployments—alters which community's opinion determines eventual consensus, nonmonotonically in that count. The theorem solves this dependence for every connected reciprocal bipartite graph of any size and edge arrangement, establishes sharp odd/even separation and rate, and quantifies how a single hub can outweigh arbitrarily many leaves. These are structural consequences relevant to influence assessment, not a cosmetic numerical example or an arbitrary parameter slice.

## Closest literature and limitations

[1] J. Wu, R. Abebe and C. Mendler--Dünner, *Opinion Dynamics in Learning Systems / Reaching a Consensus in Predictive Loops*, arXiv:2603.12137v1 (2026-03-12), https://arxiv.org/abs/2603.12137 .

[2] *Invariant-weight polarization contraction and a minimal counterexample in predictive opinion loops*, publicly indexed result (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-invariant-weight-polarization-contraction-and-a-minimal-countere--1f26affbf64c .

[3] M. Boudourides, *Boundary-Value Friedkin--Johnsen Dynamics and Influence-Based Centralities on Networks*, arXiv:2602.08704, https://arxiv.org/abs/2602.08704 .

The claim assumes deterministic perfect prediction, a connected reciprocal bipartite graph and constant peer susceptibility within each part. It does not cover arbitrary asymmetric networks, heterogeneous susceptibility inside parts, or empirical platform behavior. Independent historical-priority review is outstanding.

Self-review: passed. Independent audit: not yet performed.
