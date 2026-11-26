---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The complete proof is in `RESULT.md`. For a symbolic replay, subtract the displayed rational expressions for h(r+1)-h(r) with p=r(r+1), and for j(r+1)-j(r) with that substitution and k=3(r+1)/2. The differences after subtraction of the claimed answers simplify identically to zero. For the finite exact replay, use r=1..12 and k=1..3r+6 with p=r(r+1) at q=10^6 and q=10^8. Use rational arithmetic in (1) for each a=0..min(p,k), retain all minimizers, and check the complete count set against the finding. All 612 tested optimizations matched; this check does not prove the all-parameter quantifier or give an eventual cutoff.
