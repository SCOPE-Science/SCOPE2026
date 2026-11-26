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

After translating a root query to zero, its positive centers are edges. Within that fiber only queries of weights 0, 2 and 4 can be positive. A weight-four positive fiber has at most six edges; a weight-two positive fiber is a two-star. In a two-star, a weight-four or disjoint weight-two query has at most four positives; a pair containing exactly one hub splits it into two near-stars. A near-star query always has one branch of size at most three, which excludes depth three. Thus the edge class has rank at most four and the whole class at most five, also for small dimensions and duplicate concepts. All 32 supplied seven-bit witnesses and, separately, all possible masks over the 128 seven-bit centers were checked by independent code without executing the shipped verifier. Zero padding preserves the lower bound. The finite calculation proves the stated witness only; the edge-fiber argument gives the universal upper bound.

## originality

FAIL

Two distinct indexed records directly cover the frozen claim: aa804f0c6690 gives the exact VC dimension of the same class in every dimension, and 6e49ec510332 gives the exact Littlestone dimension in every dimension. The latter contains the same symbolic two-star and near-star upper-bound mechanism, including the uniform ceiling. This is established coverage, not an inference from a catalogue date or an unresolved web hit.

## value

FAIL

The dimension comparison is a worthwhile question, but this package combines already-established classifications using the already-indexed online obstruction and another small witness. It neither extends the range nor adds a distinct structural result or a substantially new proof of the ceiling. As a research contribution it does not advance the covered classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
