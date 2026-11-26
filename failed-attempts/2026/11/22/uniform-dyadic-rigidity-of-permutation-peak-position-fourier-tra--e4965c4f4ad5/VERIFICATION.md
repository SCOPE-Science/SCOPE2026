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

Independently checked the argument for counting, not probability-normalized, Walsh multipliers. Realizing uniform permutation ranks by i.i.d. continuous labels makes the supporting variables for separate prescribed-peak runs disjoint. An adjacent marked pair is impossible; a maximal run of k marks spaced two apart gives just the alternating event on 2k+1 labels. Conditioning its maximum on one of the k even locations proves (2k+1)b_k=∑_{j=0}^{k−1}b_j b_{k−1−j}; since b_0=1 and the divisor is odd, all joint peak probabilities belong to Z_(2). In the product of 1−2I_i, the constant term is 1 and all nonempty terms are even in this localization. Then W/n! is a dyadic unit and W−n! is an integer of divisibility at least 2^{v+1}. A singleton peak is an event of probability 1/3 for the three labeled sites, hence W=n!/3 and the difference is −2n!/3, exactly of valuation v+1. For n=1,2 only the trivial multiplier remains. Walsh diagonalization with the stated counting convention gives the determinant and norm as claimed.

## originality

FAIL

A distinct indexed record with suffix 91622a387bdc gives the same all-character valuation for precisely this counting kernel, and its actual proof gives the same stronger-looking congruence and uses the same odd-denominator joint-peak lemma. The only added singleton check is the elementary three-site probability, so the submission does not establish a substantively distinct result. The shared date does not determine which record came first; this is a finding of equivalent scientific coverage and failure to establish distinctness, not a priority or external-publication claim.

## value

FAIL

Uniform dyadic nonvanishing on this natural peak kernel is a useful invariant in its own right, but the entire substantive invariant and the decisive proof mechanism are already represented by the equivalent catalogue record. Once separated from that content, the uniform-modulus sharpness adds only the three-site marginal; the determinant and norm are immediate diagonalization consequences. No distinct worthwhile remainder is established by the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
