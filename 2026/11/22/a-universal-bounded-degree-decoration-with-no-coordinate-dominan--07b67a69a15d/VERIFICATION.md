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

# Reproducibility and limits

The proof is in `RESULT.md`. The attached `checker.py` is a standalone exact-arithmetic supplementary check for finite decorated base graphs, invoked by `python3 checker.py`. It verifies the explicit eigenvectors and mass weights and calculates the nullity at \(0,\pm1\) on each checked finite base. In the recorded run, it printed `PASS 208 exact finite checks on decorated base graphs; infinite claim is proved independently.`

The proof of the infinite statement uses a pointwise elimination of the adjacency eigenvalue equations and exhausts each indicated eigenspace. There is no inference of an infinite theorem from a finite test. The check does not establish historical priority, a complete spectrum outside the indicated eigenvalues, or minimum possible degree. No independent mathematical audit has been performed.
