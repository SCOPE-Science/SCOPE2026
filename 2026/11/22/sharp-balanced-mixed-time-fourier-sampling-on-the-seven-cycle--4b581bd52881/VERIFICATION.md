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

Run `python3 check.py` using the standalone Python standard library. It prints the seven disjoint affine orbit representatives with their sizes and exact cyclotomic determinant polynomials, then validates all 1225 row/column-triple configurations. The script replays the actual exact integer-ring operations \(\zeta_7^7=1\), maps real invariants to \(\mathbb Z[u]/(u^3+u^2-2u-1)\), and checks leading principal minors and rational sign inequalities. Its output ends with `PASS: 1,225 configurations; 7 affine orbits; 147 exact optimizers`.

The full proof additionally uses the standard two-projection principal-angle decomposition and elementary Sylvester criterion. No finite experiment alone is asserted as proof for any family beyond the seven-cycle. Exact output was obtained for the packaged code prior to review; independent validation was not performed.
