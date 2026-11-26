---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At the start of each round the adopter set is a prefix. Its only eligible nonadopter sees fraction 1/2 or 1 at the final leaf. Even a later vertex activated in that round sees the old state, so the prefix length increments by at most one. The choice of frontier is measurable before that round; its fresh coin has success probability 1/(s+2) given the entire past, independently of which vertex is selected. Extending the coin sequence past absorption gives K_t=min(m,Σ_{j=2}^{t+1}B_j). The untruncated generating function is (t+1)⁻¹∏_{l=1}^t(1+z/l), giving the stated shifted Stirling indices, with K_0=0 and no completion before m rounds. For fixed k its coefficient apart from (t+1)⁻¹ is the kth elementary symmetric function of {1/l}, asymptotic to (log t)^k/k!: the repeated-index terms in the kth power of the harmonic sum for k≥2 are O((log t)^(k−2)Σ l⁻²). Thus the highest allowed k=m−1 gives the claimed survival tail, including the exact m=1 survival 1/(t+1). The divergent sum of independent coin probabilities gives almost-sure completion; integration of the tail gives finite positive moments exactly for r<1. For the depth limit the untruncated sum has mean and variance log(t+1)+O(1), and bounded summands give Lindeberg. Inverting P(T_m≤t)=P(Σ B_j≥m) at t=floor(exp(m+x sqrt m)) gives standardized threshold −x+o(1) and limit Φ(x); tightness gives the stated law of large numbers. The frozen finite verifier was inspected, not executed, and no finite experiment is used to justify the limits.

## originality

PASS

The supported distinct claim is the exact discrete finite-round realization of a classical cycle/record law by the specified synchronous path. The closest exact inverse-age path result gives more than the fixed-depth tail: it gives a full continuous-time path law, from which the analogous log-depth Gaussian follows directly. So neither the tail exponent, the logarithmic-depth phenomenon in general, nor the Stirling law as a probability identity should be regarded as a free-standing novelty claim. The continuous formula is not the integer-round law, and the originating Monte Carlo model updates asynchronously. The originality decision rests on the exact synchronous path identification and its protocol-specific consequences.

## value

PASS

The endpoint-seeded path is a natural minimal geometry for propagation by a single advancing frontier, and the inherited inverse-age rule gives a reason to ask about delay at each depth. The exact law predicts finite-horizon success probabilities for arbitrary depth and number of synchronous rounds, including the hard one-step-per-round cutoff; neither a large-time tail nor the continuous path law gives those probabilities. This provides a precise benchmark for a parallel aging protocol and distinguishes eventual consensus from completion on useful finite horizons. The limit statements explain the discrete clock but are not treated as intrinsically new asymptotic mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
