---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct diagonalization of the 4-by-4 Hamiltonian gives the stated Gibbs X-state. Wootters' formula reduces positivity exactly to \(J\sinh(\eta/T)/\eta>e^{-J_z/T}\), \(\eta=\sqrt{J^2+b^2}\). Since \(x\cosh x-\sinh x>0\) for \(x>0\), \(\sinh x/x\) is strictly increasing, proving the one-threshold topology and the monotone \(J_z\)-dependence. Dominant hyperbolic terms give \(C\sim J/\eta\sim J/|b|\). A fresh independent matrix replay agreed with the closed formula to about \(5.4\times10^{-12}\) over a representative grid and produced \(|b|C/J=0.99875,0.99980,0.99995\) at \(|b|=20,50,100\).

## originality

FAIL

The scientific correction is correct, but the final mathematical claim is already implied by the exact Gibbs/concurrence formula in the 2005 source from which the submission starts. Once that prior formula is written in terms of \(\eta=\sqrt{J^2+b^2}\), the absence of an upper cutoff follows from the textbook derivative of \(\sinh x/x\), and the reciprocal tail follows immediately from standard hyperbolic asymptotics. The source's prose interprets its own formula incorrectly, but implication-level auditing treats an elementary consequence of an already published exact formula as covered; a contradictory verbal conclusion does not make the formula's routine consequences original.

## value

PASS

Correcting a published qualitative phase-boundary interpretation is substantively useful: it changes 'entanglement dies above a finite inhomogeneity' into a one-sided activation law with a positive algebraic tail. The motivation is therefore strong even though the derivation is too directly implied by the prior exact formula to satisfy originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
