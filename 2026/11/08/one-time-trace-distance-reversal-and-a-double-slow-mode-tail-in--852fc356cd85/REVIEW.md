# Self-review

## Correctness — PASS

The theorem is a statement about a precisely specified diagonal pure-death cascade, not a claim about generic quantum states. Independent exponential holding times give an exact absorption-time representation. The endpoint-rate coincidence \(\lambda_1=\lambda_N=\Gamma N\), with all intermediate rates strictly larger, yields a two-pole Erlang tail for the fully inverted initial state and a single-pole tail for intermediate starts. The coefficient \(m(N-1)/(N-m)\) follows by finite telescoping. Log-concavity of exponential convolutions implies the initial-state survival has increasing hazard; conditioning on the independent extra holding times proves a strictly increasing fully-excited/intermediate survival ratio, giving the unique trace-distance crossing. Mean-energy comparison uses the exact first-state dominance of late-time survivors. The accompanying finite-state test program passed its deterministic tests; the global assertions rely on the proof rather than those samples.

**Remaining mathematical limits:** The proof does not establish uniqueness for the mean-energy crossing. Late-time estimates are for each fixed \(N\), and do not support a uniform large-system time-scale claim. Additional physical channels fall outside the defined generator.

## Originality — PASS, with material priority risk

The exact Dicke rates and numerical examples of two-diagnostic reversal for \(6\leq N\leq60\) belong to Santos et al. (arXiv:2609.25359, September 21, 2026). General exact population propagators and birth-death holding-time calculations are prior techniques; notably Holzinger and Genes (arXiv:2409.19040) and Poddar et al. (arXiv:2610.37665) supply much broader population-solution frameworks. Neither the checked abstracts nor the accessible preceding claims explicitly give the uniform all-size **single crossing** of trace distance, its mixture-weight generalization and its exact inverse-time coefficient. Those are the limited incremental assertions reviewed here, not new dynamics or new propagator methods. Accessible search results do not prove global priority. The five-page motivating preprint's complete text was not obtainable from arXiv or identified open-access routes, and institutional retrieval was unavailable; the possibility that an uninspected section already proves these comparisons remains a substantive residual risk.

## Value — PASS

The published physical example exhibits a surprising crossing numerically for finitely many sizes, so knowing whether that crossing is inevitable, unique and accompanied by a computable late-time ratio is a natural finite-size and asymptotic gap. The result proves all three facts for trace distance, identifies the mechanism as a repeated slow endpoint mode and gives an energy-crossing guarantee under the physically meaningful initial-order criterion. The independent-emitter control rules out the same phenomenon when collective enhancement is removed. The classification concerns a motivated full preparation family, not an arbitrary single-size calculation; it does not promise general nonlinear or experimental consequences.

## Relevant sources and disclosure

Primary motivating source: M. G. H. Santos et al., *Superradiant Mpemba Relaxation in a Dicke Ladder*, https://arxiv.org/abs/2609.25359 (abstract and metadata accessible; full preprint inaccessible). General exact solution sources: R. Holzinger and C. Genes, https://arxiv.org/abs/2409.19040, and A. Poddar et al., https://arxiv.org/abs/2610.37665 (accessible abstracts, not complete comparative proofs). General mathematical ingredient: marginal log-concavity of Prékopa. The scope restriction and source-access risks are stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
