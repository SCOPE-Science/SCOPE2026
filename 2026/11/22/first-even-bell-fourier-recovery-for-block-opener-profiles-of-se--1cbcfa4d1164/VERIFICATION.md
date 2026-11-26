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

Restricted-growth words have a forced first opener. For a fixed opener set containing 1, every nonopener has one choice for each existing block and each opener has a single new-block choice. Counting convolution diagonalizes in the unnormalized Walsh convention; toggling coordinate 1 negates the multiplier without changing its magnitude. The independent restricted-growth enumeration with direct signed sums gives ranks 2,2,8,16,30,64,128,256, the stated two full zeros at orders 2 and 5 and none elsewhere. The only even Bell totals before order 8 are 2 and 52, both at singular orders. At order 8 the minimum magnitude is 8, at reduced masks 4,54,111,122, doubled to eight full masks; the maximum is the trivial multiplier 4140 by the triangle inequality. Thus the inverse norm is 1/8 and the 2-norm condition number 1035/2. At order 5 the unique translation-invariant range projection removes both null characters; its kernel is supported on the half cube x_1=0, with value 15/16 at zero and fifteen other entries of magnitude 1/16. The equal absolute row and column sums give 15/8 on both endpoints. Translation averaging preserves the range and identity action on it and cannot increase the norm, so 15/8 is also a lower bound for arbitrary projections.

## originality

PASS

The supported distinct claim is the sharp finite spectral recovery and stability of the joint strong-record-position profile, including the first failure of Bell parity as an invertibility obstruction. The restricted-growth bijection and fixed-opener count are covered by classical word decompositions, and endpoint projection optimality here is a standard translation symmetry consequence once the missing characters are known. Neither is credited separately. The inspected joint-spectrum comparisons concern other embeddings, whereas the primary strong-record sources give coarser statistics rather than these Walsh multipliers or their sharp zero/gap data.

## value

PASS

A partition's ordered block minima give a natural coordinate profile, and Bell parity gives a concrete obstruction to test: odd total mass rules out Walsh zeros, whereas even mass leaves the issue open. The first even invertible order is a meaningful boundary. Its exact inverse norm measures stability, and the first higher singular order supplies explicit lost modes and a sharp cost of projecting onto the recoverable data. These spectral facts concern the chosen joint profile, not just recomputation of the known Bell totals or record counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
