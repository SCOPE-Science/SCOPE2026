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

PASS: In the pure binary-successor language, atomic diagrams plus sets of extension r-types are equivalent to rank-r formulas by characteristic-formula induction, including arbitrarily long Boolean combinations. Source checker.py computes complete structural types on all single cycles n=1..32 for q=1..5, giving thresholds (2,4,7,11,19); the cyclic-gap EF invariant proves that all n,m>=2^q are indistinguishable, extending the finite q=5 table beyond 32. Rotation normalization is an automorphism. Independent direct EF game checks reproduced the rank<=3 small-order pattern; the full rank-five enumeration was inspected as code, not personally rerun as an independent complete computation. Thus the proof combines an exhaustive finite algorithm on a bounded domain and a genuine infinite-tail argument, without inferring the infinite statement from sampling.

## originality

PASS

PASS best-of-knowledge: exact 19-cycle rank-five threshold and all five successor-only classes are not implied by the inspected general EF/Gaifman results, rank-three permutation-classification, rank-q directed path cutoff or marked/two-variable cycle results. Earlier specialist cycle-type tables could still exist; failed search is not proof of novelty.

## value

PASS

PASS: The number 19 is an exact smallest stabilization cutoff for a canonical, natural finite-structure theory and a sharp improvement over the generic 32-vertex EF tail guarantee at rank five. Such exact logical spectra are usable as benchmarks for locality, model checking and Ehrenfeucht–Fraïssé bounds; it is more than a routine reformulation of EF equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
