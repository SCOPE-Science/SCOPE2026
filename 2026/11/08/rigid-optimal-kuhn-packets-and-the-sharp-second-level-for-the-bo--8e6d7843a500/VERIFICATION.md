---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For Lambda=Z^3∪(Z^3+(1/2,1/2,1/2)), the only nonzero vectors of squared norm <2 are six signed coordinate axes and eight half-diagonals. Any frame with packet radius <1/√2 has every nonempty subset sum in this 14-vector shell. An axis forces the other vectors to be opposing half-diagonals, violating independence; therefore an eligible frame is three distinct vertices of the same sign-parity half-diagonal tetrahedron (8 unordered). Their Gram diagonal 3/4 and off-diagonal −1/4 gives each permutation simplex the centroid circumball with squared radius 5/16, verified by the average-squared-distance identity. Every nonoptimal frame hence has radius ≥1/√2. For the explicit frame (−e1,−e2,(e1+e2−e3)/2), independently checked the six given centers by exact Fraction arithmetic; each permutation tetrahedron fits radius 1/√2 and pair sum −e1−e2 requires at least that radius. No lattice-frame primitivity assumption is used.

## originality

PASS

An earlier published D3/D3* theorem already has the first-level radius √5/4 and exactly eight BCC minimizers, so those portions are credited and not new. Its full inspected theorem and proof do not establish the exact infimum among nonoptimizers or construct the six-ball witness attaining radius 1/√2. The sharp isolation gap is the surviving exact original result, subject to same-day ordering and unindexed literature risk.

## value

PASS

The exact second attainable packet-radius level is a natural stability/isolation invariant for discrete lattice-frame optimization, beyond simply listing the minimizing bases. The positive gap 1/√2−√5/4 and an explicit sharp next-level frame give a quantitative limit on near-optimal frames. Although the shell argument extends the first-level classification, the attained next level and its all-permutation ball certificate are mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
