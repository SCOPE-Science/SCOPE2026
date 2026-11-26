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

Even-start length-2n factors are substitution images; at an odd start the leading zero of an aligned image is moved to the end, because the next block also starts with zero. This proves surjectivity on necklaces represented by factors. An even rotation of images respects blocks, and an odd rotation can match two images only if both are all zero, hence both antecedents are all ones. For an independent check of the minimum, the one-count sets at the even and odd starts of length 2j+1 are j minus the length-j count set and j+1 minus the length-(j+1) count set, respectively, by p_(2i)=0, p_(2i+1)=1-p_i. For length three, 000 and 101 give spread at least two; for any larger odd length one of j and j+1 is a smaller odd number at least three, so induction gives spread at least two. Sliding windows attain the intermediate counts. Thus odd lengths greater than one have at least three classes, and the bijection finishes the minimum characterization. Bounded valuation-generation and literal-rotation counts corroborated the result (e.g. c(3)=c(6)=c(12)=3, c(5)=c(10)=c(40)=4).

## originality

FAIL

A distinct indexed record states and proves the same all-length substitution-class bijection. The minimum characterization, not stated there verbatim, is sustained by a direct implication of previously published abelian and cyclic complexity results. The comparison establishes coverage, not chronological priority relative to the frozen record.

## value

FAIL

A class-level bijection would be a useful exact invariant for computing ordinary necklace complexity at every even length. Here, however, that exact invariant is already supplied independently in the indexed corpus, while the new-looking exclusion from the minimum follows mechanically from the earlier spread recurrence. The frozen record leaves no demonstrated additional mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
