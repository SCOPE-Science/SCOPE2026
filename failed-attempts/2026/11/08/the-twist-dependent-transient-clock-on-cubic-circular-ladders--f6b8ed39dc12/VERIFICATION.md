---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Pinned RESULT.md blob ad56d322a09f9cdb495ece783982dc2065cb1b65 gives prism operator a(S)I+N with N²=0; zeros only at primitive cube roots of unity. Local module K[y,e]/(y^h,e²) yields 2 J2 when h=1 and 4 Jh when h≥2 over the algebraic closure. Möbius multiplier x+x^-1+x^n has simple root at cube roots if n even (2 J_(2h)), and double root on length-2 local factor if n odd (4 J1). Fitting powers give exact cumulative shell counts. Independently rebuilt both adjacency matrices and rank-tested all kernel powers in stated range for 3≤n≤39, confirming the pattern. The proof handles arbitrary finite characteristic-two fields; tests on F2 do not alone prove that.

## originality

FAIL

Full submitted claim, including twist-induced Jordan fusion and all transient shell statistics, is published earlier on 2026-11-02 for F2. Finite field Q>2 is routine extension of the same integral/binary matrix Jordan module, insufficient to save originality.

## value

PASS

Exact transient-entry populations and twist-dependent Jordan blocks of two natural cubic graph families are meaningful dynamics invariants, but are already known; cannot accept as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
