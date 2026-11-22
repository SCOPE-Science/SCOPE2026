# Mathematical review

## Correctness — PASS
A half-line compression is identified explicitly for each parity. The bilateral two-periodic edge is computed by Floquet analysis. In the enhanced-edge regime, the larger root of the quadratic supplies an explicit positive square-summable eigenvector; the ground-state identity proves no larger spectral value exists. The opposite regime follows by positive-form domination plus preservation of the periodic essential edge. Comparing the two quadratic roots yields the necessary and sufficient convergence criterion, while truncating the positive eigenvector gives the exponential error bound. The algebraic identities and representative finite sections were checked with `check.py`. Finite tests are not an infinite proof.

## Originality — PASS (qualified)
The 2011 constant-background bilateral formula is a strict special case. The 2022 determinantal method treats fixed finite patterns. The 2026 alternating-tail paper computes exact finite-position threshold conditions but not the explicit pair of distinct remote-defect limits or their convergence classification. Published-record and own-ledger searches, including moving one-spike and periodic weighted-shift aliases, did not yield a statement that implies the complete theorem. The independent Jacobi/SSH defect literature is the main residual risk: an equivalent upper-band defect eigenvalue might have been published under different terminology.

## Mathematical value — PASS
The natural defect-escape operation normally suggests convergence of operator invariants to a bulk quantity. Here an exact phase transition shows complete convergence can fail although the exceptional edge goes to infinity. The complete parity-dependent classification, explicit upper eigenvalues, and quantitative rates resolve a well-posed operator invariant rather than a specially selected numerical case.

## Prior-work and scope limitations
References and implication comparisons are given in `RESULT.md` and `AUDIT.json`. The homogeneous case and the finite-depth threshold are not claimed to be new. The result does not address higher-period tails, multiple defects, or a parameter-uniform rate near threshold. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
