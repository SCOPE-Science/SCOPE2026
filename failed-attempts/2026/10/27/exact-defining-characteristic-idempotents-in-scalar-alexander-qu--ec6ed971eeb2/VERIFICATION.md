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

In the convolution ring R=F_q[(F_q,+)] the scalar maps T_c are algebra automorphisms and on basis elements u⋆v=T_a(u)T_(1−a)(v). Augmentation is multiplicative. The convolution augmentation ideal I is nilpotent by the truncated-polynomial presentation on an F_p-basis of the additive group. An augmentation-zero idempotent consequently lies in I^(2^r) for every r, hence vanishes. In augmentation one, Frobenius gives (1+w)^p=1 for w∈I, so the commuting principal units form an F_p-vector space with convolution as addition. The equation is the kernel of Id−T_a−T_(1−a) on that space. Its filtration by 1+I^r has the same F_p[F_q^×]-graded pieces as I, and both filtrations split because q−1 is prime to p; the kernel sizes on the two modules are equal. The basis [x]−[0] for x≠0 realizes the regular F_q[F_q^×]-module on I. Its eigenvalues for the kernel operator are 1−a^j−(1−a)^j, each with a one-dimensional character line before coincidences of eigenvalues. The dimension count and elementary abelian group assertion follow for all e, including p=2. The distinct Frobenius exponents p^r for 0≤r<e lie in 1..q−2 for q≥3 and give d_q(a)≥e. At q=7 the resonances are {1} for a=2 and {1,4} for a=4, giving 8 and 50. This arithmetic check is not an independent full census. The frozen finite verifier and verification notes were inspected, not executed; no formal verification is claimed.

## originality

FAIL

The distinct indexed result dd8ab47d1f33 proves the count when the base and defining-characteristic coefficient fields can have different sizes. Its equal-field specialization gives exactly the frozen count, augmentation assertions and ordinary-convolution group; the displayed principal-unit kernel proof also matches directly. The prime-dihedral portion independently has older exact indexed precedents. This is verified coverage, not a claim about who first obtained the equal-field result.

## value

FAIL

The idempotent number and convolution subgroup are natural invariants and legitimately distinguish some same-size quandles. As a distinct contribution, however, the frozen equal-field case is fully supplied by the broader indexed count and kernel result; the two numerical evaluations and Frobenius lower bound do not leave an independent substantive claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
