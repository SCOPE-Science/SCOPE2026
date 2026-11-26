---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reflexivity and symmetry transfer on at most 2k atoms. At n≥r+s+1, an r-tuple and its single-entry replacement have a common disjoint s-tuple neighbor, and single-entry replacements connect the injective ordered r-tuples (a spare atom permits a swap). The same proof on the other side connects the disjointness incidence graph; it also works when the two within-tuple equality types agree. One accepted disjoint pair thus forces all pairs between the two types in the finite equivalence restriction. A transitivity triple too large to embed in N_k has at most one lost support atom relative to the sum of the three support sizes, so at least one premise is disjoint. After applying saturation to that premise, carry the other premise into the test set. Given any desired representative of its end type in the test set, permute the second premise to end there; saturation joins any initial representative to the permuted middle, giving the full conclusion by finite transitivity and pair transport. For sharpness, six atoms at k=3 (2k in general) give complement pairs of support classes, plus singleton noninjective tuples. On one more atom two distinct overlapping supports can both be disjoint from the middle support, violating transitivity. Hence the seven-atom claim and both general bounds are true.

## originality

FAIL

A distinct indexed Resultary record 687b15057b20 gives and proves the exact 2k+1 test on any atom set of size at least 2k+1, with the same equal-or-disjoint support obstruction. This covers every frozen theorem component, is strictly stronger for k≥4, and is exact at k=3. The full stated theorem and the decisive proof were inspected. This is demonstrable coverage, not a determination of who proved the result first.

## value

FAIL

An exact finite equivalence-test cutoff is useful in principle, and the connected-disjointness argument is a readable alternative. But the frozen scientific finding gives the already-covered seven threshold with the same obstruction and gives a weaker general upper bound than the exact indexed one. It does not isolate a distinct algorithmic benefit, transferable new lemma, or other independently useful surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
