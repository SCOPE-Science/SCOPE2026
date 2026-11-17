---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent exact rational path-integral checker source uses four affine shortest routes and same-arm competing arc; analytic cubic I_m=((2S+a)Q−R)/4+aS²/2+(7−2m)a²S/4+(2m²−7m+9)a³/12 follows. The balancing gap is strictly positive unless longer m−1 arms are equal. Differentiating the balanced polynomial leaves only an interior maximum and endpoint minima; m=3 equal lengths gives 5L/27, m>=4 collapse infimum (2m−3)L/[4(m−1)²]. Direct independent SymPy symbolic expansion confirms this entire cubic equals earlier published result after k=m−1, B=S, S₂=Q, S₃=R. Geometry and strict-positive boundary handled correctly.

## originality

FAIL

FAIL: decisive stronger prior coverage. Published complete earlier statement Sharp mean-distance collapse for parallel-arm metric graphs already proves identical m>=4 strict lower bound, unique minimizing degeneration, and explicitly states m=3 equilateral optimum. Its exact cubic pair-distance integral is algebraically identical to the submitted one under a renaming; novel symbol names and a different balancing presentation cannot produce an original result.

## value

FAIL

FAIL: The final theorem and rigidity are a complete recomputation/renaming of a known mathematical classification; there is no surviving separately motivated unknown exact invariant, sharpened boundary, or independently useful mathematical fact. Code and correct alternate derivation alone cannot establish novel mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
