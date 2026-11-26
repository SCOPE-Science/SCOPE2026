---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The standalone standard-library Python program `verify.py` was extracted from the assembled finding package and executed. It reconstructs the directed classes on small marked rings, compares them with the residue and root-phase classification, and counts frozen configurations independently from binary occupancy subsets. For classes of size at most 120 it also checks exact-rational master-equation balances for a nontrivial potential and verifies the stationary current from the two partition functions. The exact example with \(L=12\), \(N=8\) and \(I=2\) contains \(105\) frozen states. The mathematical proof in `RESULT.md` uses connectivity, conservation, and finite-density exponential tilting with a multinomial bound, none of which is inferred from the finite test.

Independent audit has not been performed. No external formal proof certificate or third-party scientific validation is represented.
