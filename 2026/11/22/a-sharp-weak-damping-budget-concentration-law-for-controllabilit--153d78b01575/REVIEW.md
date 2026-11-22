# Self-review

## Correctness — PASS

The model is a real finite feedforward system of order \(n\ge3\) with strictly positive leakage \(\mu\), rate budget \(S\), positive transitions and a single upstream input. The exact impulse responses have lower-triangular exponential coefficients; their Gramian is a congruence of a Cauchy matrix. Cancellation of all Vandermonde factors gives the closed product formula at distinct rates, and continuity covers repeated rates. Every optimizer is interior; exchanging and separating rates forces strict upstream order. Uniform strong-damping expansion, weak-damping denominator bounds, compactness, and strict convexity of the log-sum-exp denominator prove both allocations and the sharp power-law constant. An independently implemented exact Lyapunov recurrence checked 125 rational examples, including repeated rates. Those finite checks support but do not replace the analytic all-dimensional proof.

## Originality — PASS on inspected evidence, qualified

Pasqualetti, Zampieri and Bullo (arXiv:1308.1201) treat network controllability metrics, while Summers, Cortesi and Lygeros (arXiv:1404.7665) optimize log-determinant over actuator sets. Becker et al. (arXiv:1902.04195) design edge weights for different spectral Gramian constraints. Accessible public result comparisons include directed ring actuator placement and cyclic spectral-abscissa allocation, which do not imply the present D-optimal directed-path rate hierarchy. The known Cauchy determinant is a proof tool, not an originality claim. The earlier three-node *undirected* star allocation uses symmetric Laplacian dynamics and neither implies the one-way chain result nor its arbitrary-dimensional concentration law. Search limitations remain: relevant older or unindexed control-design sources might contain an equivalent result; no independent priority audit has occurred.

## Value — PASS

The precise object and determinant criterion are natural for a budget-limited feedforward network. The theorem provides an exact finite-damping order of optimal investments and two distinct universal limiting allocations. Its weak-damping singular concentration upgrades the optimal Gramian determinant from a fixed-design \(\mu^{-1}\) law to \(\mu^{-(n-1)}\) for every dimension, quantifying a nontrivial volume-versus-rate-robustness effect. It does not imply optimal worst-case actuation energy or provide a numerical stability guarantee.

## Limitations and verification state

The proof excludes feedback networks, multiple inputs, other Gramian criteria and finite-horizon Gramians. It does not claim finite-leakage uniqueness. The exact-arithmetic script is reproducible with standard Python, but it cannot certify every real parameter by enumeration.

Self-review: passed. Independent audit: not yet performed.
