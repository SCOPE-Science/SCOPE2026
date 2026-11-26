---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The normalized nearest-neighbor energy has nonconstant eigenvalues 1 and 1+q with q=(1+sqrt(5))/2. Write u=(1+v+w)/sqrt(1+s), s=r²+b², where v,w are the first and second real harmonics of norms r,b. Normalized Taylor expansion gives deficit 2q b²-2<v²w>+3r⁴/4+o(b²+r⁴); the quartic terms in first harmonics are s²/2 and <v⁴>/6, with <v⁴>=3r⁴/2 and <v³>=0. The mixed terms are uniformly lower order on the stated error scale, e.g. r³b<=r(r⁴+b²)/2. If b/r² diverges, b² dominates both the other numerator terms and (r²+b²)². Otherwise d(u)^4 equals r⁴(1+o(1)); completing the square subtracts ||P₂(v²)||²/(2q)=r⁴/(4q). The normalized path w=P₂(v²)/(2q) achieves the lower limit, giving (7-sqrt(5))/8. I independently recomputed the witness from integer successive differences and rational enclosures of the logs (a range-reduced series for -log(1-t), rather than the frozen atanh series). The certified ratio lies between 0.594923412098787 and 0.594923412098788, below 119/200 and the exact local threshold. The local separation excludes an entire ball about 1 at any level at or below the witness. Continuity including zero coordinates and compactness on the remaining closed set imply attainment and uniform positive separation of the minimizing set.

## originality

PASS

Credit the exact local threshold to the earlier local analysis. The supported distinct contribution is the explicit normalized nearest-neighbor witness below that threshold and the resulting nonconstant attainment.

## value

PASS

The strict improvement is small numerically but qualitatively changes the variational problem: the global optimizer cannot be captured by perturbing around the constant. A short exact witness certifies a change from a local asymptotic comparison to nonconstant global attainment for a natural fixed energy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
