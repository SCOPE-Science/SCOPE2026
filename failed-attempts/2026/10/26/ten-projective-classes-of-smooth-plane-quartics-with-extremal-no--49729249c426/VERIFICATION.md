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

An independently written exact replay counted all subsets of sizes 0–6, finding 234 and none smaller, and obtained the stabilizer of the fixed set by enumerating its ordered projective frames (24 elements). Since the full projective group has order 5616 and preserves incidence, that proves a single orbit of all 234 such sets. Solving the complete evaluation system for each possible normalized nonzero sign pattern off the six-set gives exactly 567 normalized quartic candidates. Geometric smoothness was checked by independently coded ternary bitset row reduction on the degree-seven multiples of the three cubic partials. Euler in characteristic three makes the derivative ideal sufficient; no projective zero makes it a height-three regular sequence with Hilbert series (1+t+t²)^3 and zero degree-seven quotient; conversely a projective zero forces rank failure. The replay gives 222 smooth forms, with exact normalized candidate and smooth lists agreeing with the frozen files. Substitution by the stabilizer gives nine 24-element orbits and one six-element orbit, containing the displayed exceptional form. Hence the total is 51948 with sizes 5616 (nine) and 1404 (one) and stabilizer orders 1 and 4.

## originality

FAIL

A distinct published study of Weil polynomials for these very same quartics explicitly includes the full baseline projective census and its ten class representatives. The seemingly different exceptional equation in that study is in the same projective class by x↦x, y↦z, z↦y+z in the frozen representative, then scalar normalization. The distinct record's November 8 path follows the assigned October 26 path; exact published coverage is established, historical priority or dependence is not.

## value

FAIL

The census asks a natural finite-geometric realization question, but the exact baseline and representatives are already available together in the matched arithmetic classification. The frozen record adds no further mathematical distinction for these ten types; a redisplayed representative and an exact independent recomputation of the same census do not supply a surviving distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
