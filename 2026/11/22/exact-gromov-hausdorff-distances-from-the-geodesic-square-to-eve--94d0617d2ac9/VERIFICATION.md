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

I reconstructed both bounds in the integer metric obtained by multiplying all unit-circumference distances by 4m. Choose s with 4s=m±1; a step-s edge has distance 4s, and square vertices of the same parity have distance either 0 or 2m. Both discrepancies are at least m−1. Thus distortion strictly below m−1 would force an alternating parity assignment along the step-s cycle, which is odd (in fact gcd(s,m)=1). This applies to any correspondence by selecting one square image for each vertex without requiring the selection to be surjective. For the four-block graph, same-block distances are ≤4k≤m−1; adjacent-label discrepancies are at most m−2 using source distances in [4,2m−2]; opposite-label pairs are separated in either direction by at least k+1 steps, so their discrepancy is ≤2m−4(k+1)≤m−1. The block sizes are positive for both residues, including m=5 and m=7. Undoing the scale multiplies distortion by 2π/(4m); halving distortion gives π(m−1)/(4m).

## originality

PASS

The exact m=5 endpoint is already known, and consecutive blocks are not a new type of construction. The supported distinct contribution is the uniform odd family, in particular m≥7, and its parity lower bound for arbitrary correspondences. None of the closest inspected statements implies that family.

## value

PASS

This is a natural infinite slice of the exact-distance problem for regular circle samples. It supplies the entire missing odd portion of the square-source profile and a graph obstruction that controls arbitrary correspondences rather than only the explicit upper-bound map. Its value does not rest on the already known endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
