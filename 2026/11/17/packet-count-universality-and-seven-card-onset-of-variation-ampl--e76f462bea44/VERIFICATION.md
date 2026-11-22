---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

For the quotient by constants, every signal decomposes into adjacent prefix-step differences, so the exact operator seminorm is the maximum variation of expected prefix images. Given a deterministic a-label assignment, the prefix ones occupy at most a contiguous block per packet in label-sorted order, giving ≤2a−1 jumps. Positive packet probabilities let one choose three quarter/half probes in every packet, and Hoeffding bounds force each ideal jump with probability 1−O(a exp(−np_*²/32)), proving matching limit and explicit lower bound. The two-packet prefix image is computed by exact binomial double sum, and independent rational arithmetic verified every 2≤n≤7, including sharp C_7=67/64 and C_6=29/32. Composition of inverse shuffles gives tensor-product packet labels, while the no-collision event for fixed n tends to one, yielding the uniform-rank averaging operator of zero adjacent-output variation. These are all-limit arguments, not finite-enumeration extrapolations.

## originality

PASS

Direct reading distinguishes permutation-distribution total variation in classical riffle literature from the bounded-variation seminorm on the *expected output signal*. The inverse model and biased packet convolution are credited as prior. No inspected source states the operator gain 2a−1 uniformly in positive packet bias, n=7 onset, or fixed-r product-law extension.

## value

PASS

A stochastic averaging operator can amplify adjacent path variation even though shuffle distributions mix. The exact packet-count dependent sharp gain, universal independence from fixed bias and first seven-card onset describe a well-motivated noncontractivity phenomenon in a familiar probability operator; the threshold is not an arbitrary toy table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
