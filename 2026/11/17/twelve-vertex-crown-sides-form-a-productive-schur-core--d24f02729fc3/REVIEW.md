# Self-review

## Correctness — PASS
The exact cited variational formula and compression-monotonicity reduce the infinite operator-norm optimization to a single test weight. The root chain pinches to a two-by-two Hermitian matrix with trace norm \(\sqrt{d^2+4c^2}\). Every other chain pinches to a traceless two-by-two block with trace norm \(2c\). Substitution yields the displayed \(L\), and the two radical lower squares, integer power bound, and rational identity prove \(L-2S>496253/189120000\). The standalone file `verify_certificate.py` verifies every exact integer/rational step. Limits: no optimality, full norm computation, or converse for smaller cores.

## Originality — PASS
Levene, arXiv:2611.08419v1, proves a productive tensor-product core and only reports numerical evidence for a larger crown; it gives an exact variational formula, but not the strict \(n=12\) productivity inequality. Two accessible earlier crown-core results cover \(n\ge15\) and \(n\ge13\) and do not imply \(n=12\). Searches of the published mathematical findings index for the exact 12-crown, matching-deleted bipartite core, Schur idempotent attached trees, and variational trace-norm certificates returned no claim covering the new case. The related decomposition paper arXiv:2607.14316 does not imply it. Remaining risk: unpublished or unindexed equivalent certificates.

## Mathematical value — PASS
Productivity is the enabling property in Levene's construction of entire intervals of idempotent Schur multiplier norms. The twelve-by-twelve crown is a simple uniform core on the same number of vertices as the previously certified tensor-product core, and extends the proven crown family below the earlier threshold \(n\ge13\). Crossing the strict threshold \(2\), rather than the size of the numerical gap, is the structural invariant; it is not a mere refinement of an already known \(n=12\) result.

Self-review: passed. Independent audit: not yet performed.
