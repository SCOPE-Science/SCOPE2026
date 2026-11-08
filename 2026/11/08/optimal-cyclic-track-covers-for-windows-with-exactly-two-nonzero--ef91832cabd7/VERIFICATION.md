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

# Verification

Run `python3 verify_two_active_cycles.py` from a directory containing the attached standalone checker. It uses only Python's standard library, reconstructs the exact weight-two overlap graphs from allowed words, verifies the separation-class partition and edge counts, checks equal in- and out-degrees, computes integer directed Laplacian cofactors with the Bareiss algorithm, and checks the BEST-factor counts against the theorem's closed forms.

The checker completed and printed `VERIFIED component instances: 31`. Its test sets are \(q=2\), \(3\le n\le8\); \(q=3\), \(3\le n\le6\); \(q=4\), \(3\le n\le5\); and \(q=5\), \(3\le n\le4\). Direct fixed-first-edge Euler-tour enumeration is additionally performed for \((q,n)\in\{(2,3),(2,4),(3,3),(3,4),(3,5),(4,3)\}\). This avoids reliance on a numerical optimization status. The proof of the infinite theorem is the forced-path contraction, matrix-tree cofactor computation, and BEST theorem given in `RESULT.md`, not the finite test log.

Examples include component-cycle counts \(4\) and \(1\) for \(q=3,n=4\), and \(5184\) and \(24\) for \(q=4,n=4\). Known limitations: it does not test all alphabet sizes or lengths, and no independent mathematical audit has been performed.
