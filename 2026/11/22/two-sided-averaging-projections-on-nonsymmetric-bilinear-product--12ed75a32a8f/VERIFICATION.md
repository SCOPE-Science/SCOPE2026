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

# Reproducible mathematical checks

The theorem is proved symbolically in `RESULT.md`. The tests below provide additional finite consistency checks and are not infinite proofs.

Run `python3 verify_counts.py`. The program independently enumerates totally isotropic subspaces for \((q,n,a)=(5,1,2),(5,2,2),(7,1,2)\), checks the Goursat formula, enumerates idempotent \(2\)-by-\(2\) matrices over \(\mathbb F_5\), and verifies the rank polynomial. Expected marker: `RREF_ISOTROPIC_AND_CENTRAL_IDEMPOTENT_COUNTS_VERIFIED`.

Compile and run `g++ -O3 -std=c++17 exhaust.cpp -o exhaust && ./exhaust`. This program checks every \(3\)-by-\(3\) linear map on the \(n=1\) example over \(\mathbb F_5\) and \(\mathbb F_7\), evaluating the unmodified defining polynomial identities and computing ranks by elimination. Expected marker: `DIRECT_IDEMPOTENT_AVERAGING_EXHAUSTIVE_VERIFIED`.

The finite checks cannot verify the general structural reduction for all dimensions. The proof's critical mechanisms are socle invariance, nondegenerate self-adjointness, the split block matrix calculation, and Gaussian counting. The full retraction branch is established by earlier work and explicitly credited rather than claimed new. No independent audit is asserted.
