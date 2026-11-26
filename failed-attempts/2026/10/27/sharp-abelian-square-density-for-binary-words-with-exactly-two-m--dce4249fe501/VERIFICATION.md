---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Equal halves require 0 or 2 ones. For two, the midpoint must lie between the ones and their separating zero run has (b+j−i)/2 zeros to the left of it; this gives precisely the parity and band conditions, including endpoints. Each pair names a distinct string, and fixing i−j gives the stated interval intersection count. The continuum section length is piecewise linear with slopes 0 or ±1; rounding each cross-section and comparing the spacing-two sum to its integral costs O(n) uniformly. Integrating the clipped triangles gives the stated area. When b≥s/3 the rectangle bound is at most s²/9; when a or c is less than b<s/3 the rectangle bound is strictly below b(s−2b)≤s²/8. With both outer lengths at least b, the area is bs−2b²−|a−c|²/2 for |a−c|≤b, and bs−3b²/2−b|a−c| otherwise; the latter is below s²/10 for b>0, and b=0 has zero area. The unique equality case, rounding, and compactness prove the coefficient and rigidity. For (3k,2k,3k), summing 3k+1−|d| at the allowed even differences gives 4k²+3k+1, then add the unary count. The frozen verification and script were inspected, not executed.

## originality

FAIL

A distinct indexed five-run result provides stronger mathematical coverage of the contribution presented for acceptance, including the sharp constant, the equality shape of the band bound, and the witness. Its five-run classification even yields the full mixed formula by a one-unit shift of both endpoint lengths. Its displayed date is later than the frozen record's date; this assessment of demonstrable coverage does not assign historical priority, chronology of discovery, or dependence.

## value

FAIL

The sharp extremal problem and its stability conclusion are scientifically motivated, but the only calculation not explicit in the stronger result is an elementary boundary translation and unary correction. The record does not determine exact restricted maxima or finite maximizers, and the residual elementary count after specialization does not supply a standalone valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
