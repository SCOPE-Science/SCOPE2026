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

The proof reduces the all-depth discrepancy assertion to the exact finite identities \(P_{\tau^{16}(a)}=P_a\) for \(a\in\{0,1\}\), \(R(M^3-I)=V\), \(VM=V\), and the initial integer vectors. These are independently regenerated from the two explicitly defined Fibonacci words by `verify_matrix.py`; no stored numerical logs are required. The finite-state substitution induction in `RESULT.md` links the integer certificate to the infinite family.

The independent direct simulator `verify_direct.py` checks the four unique precursor branches for output words of lengths \(1\), \(2584\), and \(5702887\). The direct calculation does not establish the infinite result by itself, and the two scripts do not constitute an independent mathematical audit. All checks are deterministic and have no third-party dependencies.
