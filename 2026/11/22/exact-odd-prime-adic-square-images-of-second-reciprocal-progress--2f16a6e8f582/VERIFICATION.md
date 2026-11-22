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

# Mathematical verification and scope

The proof in `RESULT.md` verifies the infinite claim by a coefficientwise \(p\)-adic lower bound, a global contraction for the unique derivative root, and an exact isometric square coordinate. This argument works for all odd primes and all admissible progression parameters.

The standalone Python 3 file `check_reciprocal_e2.py` computes the reciprocal sums via their exact recurrence, recovers the critical value by finite-difference Hensel lifting, and compares complete modular fiber histograms with translated quadratic-residue histograms. Nine finite test cases examine 2087 input indices. The tests confirm the exact image counts, root multiplicities, critical leading residue, and index periods on those instances only. Their successful execution does not certify the infinite theorem, its novelty, or its external provenance.

No independent mathematical audit has been performed. The scientific priority comparison is qualified by inaccessible primary literature and possible indirect uses of general analytic normal-form methods.
