---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Proved spider laws: all peripheral b_i jobs match private d_i or a_i; the center fails under job-side vertex order iff processed last and each arm job chooses a_i, giving 1/((m+1)2^m). Under uniformly random edge priorities it fails iff each arm internal edge a_i b_i is earliest of the three arm edges, giving 3^-m independently across arms. Thus the two-point stochastic order flips precisely for m>=4; the m=4 gap is 1/6480, with E[M_V]=399/80 and E[M_E]=404/81. For sharp n<=13 cutoff, independently enumerated all free trees with a second generator and both bipartition orientations and evaluated a separate exact Fraction first-edge/first-job recurrence: a single positive orientation at n=13, none for n<=12. Inspected pinned verify.py, including its independent induction-complete leaf-extension tree generator and canonical centers. This is exhaustive finite calculation, not a proof of an all-order tree classification.

## originality

PASS

The closest same-algorithm work proves domination after random graph averaging and explicitly allows deterministic graph counterexamples; it does not determine a sharp fixed-tree cutoff or one-sided bipartition orientation. Exact three-edge spider two-point laws and unique thirteen-vertex orientation add distinct finite structural information.

## value

PASS

A mathematically motivated expectation/stochastic-order comparison of two standard greedy algorithms is reversed by a uniquely minimal oriented tree, and the infinite spider family gives a clean analytic mechanism. The small n=13 gap is significant as a sharp counterexample to a natural universal pointwise domination conjecture, not claimed as a large numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
