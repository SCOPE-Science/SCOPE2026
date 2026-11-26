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

The inverse-image argument applies to every finite reset word, with no length restriction. In the frame rotated by the number t of preceding inverse a steps, inverse b copies the membership of t mod n into t−1 mod n. From the terminal singleton {r}, the first additions must therefore be r−1, r−2, …, r−(n−1), even if later inverse b steps delete positions. The successive addition times have residues decreasing by one and thus are at least n−1 rotations apart. There must also be at least n−1 inverse b steps. Equality in both counts forces the initial addition at t=0, all gaps exactly n−1, and no redundant steps; conversely those steps reach Q. This includes n=2, where the equality word is b. Strict positivity makes equality in weighted cost equivalent to equality in both counts. The finite subset searches described in the frozen verification are corroborative, not the basis for the general conclusion.

## originality

FAIL

An earlier indexed theorem for the same labeled automata proves the strictly stronger statement that every reset word contains the claimed word as a scattered subsequence. This covers the whole finding, including weighted uniqueness, not just the unweighted optimum.

## value

FAIL

Uniform positive-weight optimality is natural, but the frozen result extracts two letter counts and the immediate equality case from a previously established mandatory reset subsequence. It adds no surviving mathematical extension or independent invariant beyond that indexed structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
