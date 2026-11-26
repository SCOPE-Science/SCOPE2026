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

The frozen opening says that x_0=3/5 enters the extinction branch above the border, but the formal clock counts equality and exact hits occur arbitrarily close to the border. At r_* all the polynomial even returns from 3/5 are positive. For N large, start at r_* and take the first parameter where the minimum of the first N polynomial returns becomes nonpositive. The minimum is then zero. It must be the Nth return, since an earlier zero would be followed by -Delta<0, contradicting minimality and continuity. Any fixed r>r_* has finite first passage, so these exact-hit parameters approach r_*. The actual map fixes 1/2. repairs/2/RESULT.md corrects the title and finding to a first-passage clock, preserves strict-crossing extinction, and proves that equality is a real exception. The repaired proof checks the sign branches and endpoint contact by f_r(r/4)-1/2=-Delta; the factored return gives the two roots, multiplier -r^2+2r+4, and the only eternally right fixed orbit above the border. At the critical trap the endpoint pair pushes forward to the single atom at 1/2, hence is not invariant. From 3/5 the odd state is right and strictly positive even returns shrink in the domain 0<u<=1/10; comparing -Delta+u^2(C-r^3u^2) with the pure squaring recurrences proves K=log_2 log(1/Delta)+O(1). Delta has a simple zero at r_*; each return uses two iterates. The frozen script was inspected, not executed; all-real claims follow from the analytic bounds.

## originality

PASS

The map, a generic ghost mechanism, and superattracting virtual-cycle collisions are not credited as newly discovered. The repaired result retains a distinct exact border and fixed-initial-condition parameter-detuning clock for this map, with the equality convention kept explicit. No inspected prior result establishes that combination or implies it; decisive portions of some primary sources were unavailable, so the judgment is bounded.

## value

PASS

The corrected statement quantifies a distinct change from a logarithmic to a double-logarithmic transient at a concrete border, with an exact factor of two, and separates approaches, threshold hits, and strict extinction-producing crossings. This matters even arbitrarily close to the border and cannot be inferred from stability or empirical convergence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
