---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite-state voter generator was constructed independently of the backward coalescent argument. The reproducibility command is `python3 verify_voter_clique.py` under Python 3.9+ with no nonstandard dependencies. The verifier uses exact rational elimination and determinant calculations, tests \(r=1,\ldots,10\) with four rational Laplace parameters, and confirms the expected characteristic polynomials, mean hitting times, partial fraction identities, and pole residues (155 checks). The proof of the infinite family and uniform Gumbel approximation is analytic, not computational. The exact finite-state generator and the public proof are scoped to a fixed positive hub, full initially negative periphery and rate-one node-update copying.

Self-review: passed. Independent audit: not yet performed.
