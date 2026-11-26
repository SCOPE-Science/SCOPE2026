---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the stated 12-state chain, each excursion's two absorption probabilities are the discounted reset-free first-passage sums divided by the common factor s. Renewal gives their ratio to the sum; success is positive for s>0. The tridiagonal cofactors give the two side determinants and odds prefactor 231/2, with s^(-1) from the distances five and six. Both determinant polynomials are positive on [0,1] by their decreasing derivatives and positive endpoint values. Exact reconstruction reproduced L, R, H, the transformed signs (--++-) and the bracket signs (-++-); solving the full eventual-probability equations with the reset term included also confirmed the formula at six rational s, including s=1. Replay: python3 /workspace/branches/independent-exact-4-5.py; the supplied verify.py was inspected, not run. Descartes' rule counts multiplicities after the interval-to-positive-axis substitution, so the two disjoint sign brackets exhaust the roots and both are simple. In increasing s, the extrema are a strict minimum and then a strict maximum (reversed order in reset probability 1-s); no absorption claim is made at s=0.

## originality

FAIL

Distinct catalogue record b7682f792857 contains the exact same rational witness and exact-two certificate as its sharpness example, and asserts a broader minimality result not contained here. The identical rate vector, start, reset convention, formula, derivative polynomial up to a nonzero scalar, brackets, and Descartes argument show substantive mathematical coverage, not just a similar search hit. Both records are dated 2026/11/22; the evidence does not establish which came first. No distinct claim survives in this frozen example, and this is not a finding that the example is false or a historical priority attribution.

## value

FAIL

A first exact witness would be well motivated by the open direction on multiple reset-rate extrema. This frozen version, however, supplies only the same narrowly specified witness and exact root-count certificate already present in the separate threshold record. There is no independent boundary, classification, or mechanism here beyond that overlap. Reproduction is useful as verification, not a distinct scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
