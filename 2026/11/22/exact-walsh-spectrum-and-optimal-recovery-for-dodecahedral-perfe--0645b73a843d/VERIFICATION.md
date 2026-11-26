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

Independent construction of GP(10,2) gave 30 edges and 36 distinct 10-edge perfect matchings. In a connected graph, the vertex-star space restricts bijectively to tree-edge coordinates and has dimension 19; every switch changes all matching terms by a common sign. The replay enumerated the 2,048 normalized signings using its own tree and exact Walsh transform: absolute multiplicities (700,882,240,140,84,2) at (0,4,8,12,16,36). Since each class has 2^19 frequencies, rank and nullity are 706740224 and 367001600; gap 4 and maximum 36 give inverse norm 1/4 and condition number 9 on the range. Direct evaluation of all 30 singletons and 435 pairs reproduced the 12 matching incidences per edge, zero singleton cancellations and 60 pair cancellations. The empty signing has value 36. Inverse-transforming the nonzero indicator gives a cycle-space kernel with exactly 1,024 nonzeros and integer absolute sum 21,248 with denominator 2,048. Translation averaging preserves any projection's action as the identity on the range and maps into it, and cannot increase either endpoint norm; the unique translation-invariant projection is the Fourier range projection. Its row/column absolute sums attain 83/8. The supplied verifier uses int.bit_count (Python ≥3.10) despite the stated Python 3.9 minimum; the replay does not rely on the uploaded verifier.

## originality

PASS

The unsigned count 36 is not credited as new. Checked nearby works discuss cuts of the same graph or the same Walsh invariant on another graph. None establishes coverage of the signed dodecahedral census, first cancellations, or sharp endpoint norm. The nearest cited count-source full text remained inaccessible; this limits the comparison, not the verdict.

## value

PASS

The dodecahedral graph is a natural nonbipartite cubic model. For binary matching incidence, the result gives a complete cancellation profile at all frequency classes, the minimum size and number of cancelling edge tests, and sharp recovery and endpoint projection costs. In particular exact endpoint cost and nullity are not encoded by the unsigned matching count. This is a useful benchmark for graph-specific matching incidence computations without claiming a fullerene-family law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
