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

Run `python3 check.py` with standard Python 3 from the directory containing this file and `RESULT.md`. No network, third-party packages, precomputed tables, or external logs are required.

The checker performs an exhaustive comparison of all permissible first denominators for each integer \(2\le u\le500\), choosing for each first denominator the smallest strictly permissible second denominator, with ordering enforced. It also tests the exact polynomial comparison identities and residue class table used by the proof. In the reviewed execution it passed 125,249 rational first-denominator comparisons. The proof's infinite range is certified mathematically by the algebraic sign and concavity arguments; finite checks serve only as exact finite-boundary proof and corroboration.

The sole genuinely exhaustive finite region needed for the infinite proof is \(2\le u\le33\). The term-by-term code is present verbatim, not a log reference. The result does not assert any independent review, external formal certification, or experimental proof of infinity.
