# Scientific review: saturated-hub Kemeny optimization on wheels

## Correctness — PASS

The claim quantifies over every rim order at least three and **all** connected symmetric stochastic kernels on the fixed wheel. The normalized inverse-trace representation makes strict convexity and unrestricted rotational averaging valid; a full Fourier decomposition gives one radial and \(m-1\) rim eigenvalues. After setting the rim holding to zero, the derivative of the remaining scalar objective is strictly negative throughout the admissible spoke interval by a uniform, explicit bound. The endpoint therefore produces the unique global optimum. The Poisson-kernel identity gives both exact Kemeny values; its exponentially small root terms justify the asymptotic factor. `verify_wheel.py` passed 138 independent finite calculations. Finite checks are not the proof.

## Originality — PASS on available evidence, with residual risk

The relevant general literature establishes symmetric stochastic graph optimization for SLEM (Boyd–Diaconis–Xiao, 2004) and convex inverse-trace Kemeny optimization (Patel–Agharkar–Bullo, 2014/2015); neither inspected primary treatment derives the wheel-specific per-vertex-capacity optimum. Zhang et al. (2012) optimize network topology for degree-normalized walks, not the transition matrix on a fixed wheel. A highly relevant published wheel resistance-design record was read in full: it treats total priced conductance, not row-stochastic edge capacity. Generic spectral and convex optimization tools are not claimed as novel. Unindexed equivalent wheel formulas and a possible reduction in other reversible-chain literature remain residual risks; search absence is not a proof of priority.

## Value — PASS

The theorem supplies a complete all-order optimizer with a sharp resource-allocation statement: the hub's probability budget must saturate and neither hub nor rim ever holds. The exact standard maximum-degree comparator suffers a diverging \(\sqrt{m}\) relative Kemeny penalty with a sharp coefficient. This identifies a concrete failure mode of a familiar stochastic-design heuristic and a nontrivial scaling change, rather than an arbitrary numerical slice.

## Scientific limitations

No theorem is claimed for fixed edge-conductance budgets, prescribed nonuniform stationary distributions, nonreversible chains, or other stochastic objectives. Exhaustive publication priority is unresolved; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
