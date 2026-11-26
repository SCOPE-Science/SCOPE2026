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

For each row, nonnegativity and gamma>=1 give R_i<=w_max A_i^gamma sum_{j!=i} A_j^gamma<=w_max[A_i(B-A_i)]^gamma<=C=w_max(B^2/4)^gamma. A maximum-affinity pair split evenly gives a 2x2 block with Perron root C. Conversely, if the root is C>0, a connected support block attains it; multiplying R_i<=C in that block by its positive left Perron vector forces every row to attain C. Each vertex in that block has area B/2, so there are exactly two, the whole budget is there, and its edge must be a maximum-affinity edge. This includes gamma=1, reducible W, and ties among heaviest edges. For the unit-weight K3, the equal three-site design has root 2(B^2/9)^gamma versus at most (B^2/4)^gamma on any two sites. Thus the strict witness is exactly gamma<log(2)/log(9/4) among positive exponents, without claiming a global transition below one. The frozen checker was inspected rather than executed; the inequality and equality analysis certify all admissible parameters directly.

## originality

PASS

The kernel family and area-to-graph spectral reduction already occur in the earlier corridor record. The square-root K3 comparison is also an instance of Motzkin–Straus and is not credited as independently new. The supported increment is the sharp arbitrary-weight, all-size gamma>=1 maximum and full two-site equality criterion, a p<=2/3 quasi-norm problem not covered by the usual p>=1 results consulted. The low-exponent comparison delimits that theorem, not a new general threshold result.

## value

PASS

The row-sum method is elementary, but the conclusion resolves a concrete allocation question rather than just bounding an eigenvalue: under the specified model all optimal designs spend the entire budget on a heaviest edge, and this remains true despite degeneracies or numerous alternative positive edges. The three-site contrast shows why the area elasticity matters. Its usefulness is as an exact consequence of the surrogate's assumptions, not a claim about ecological management under realistic constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
