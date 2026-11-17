---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Positive-drift Dyck periodic points are in shift-equivariant bijection with words on M labelled opening symbols and one generic closing symbol, with height d determined by composition. Counting yields F_n(d)=binom(n,(n-d)/2)M^((n+d)/2); least period divides n and scales height under repetition, giving the stated Mobius sum over k|gcd(n,d). For odd n,d=1 the repetition correction is empty; for even n,d=2 only k=2 can subtract, and it appears iff n/2 is odd. A Chernoff upper bound for nonpositive heights and n(M+1)^(n/2) nonprimitive points, Stirling's central binomial formula, and the binomial CLT yield the displayed rare-shell prefactors and Gaussian limit. Independently enumerated primitive full-shift words for M=2,3, n<=8, agreeing with exact formulas; the finite check is not the proof.

## originality

FAIL

Prior full-shift Borel embedding for positive/negative Dyck multiplier classes is shift-equivariant, and the exact number of fixed-height periodic points is binomial composition counting. Applying the standard multivariate primitive-necklace / Möbius inversion theorem gives the exact claimed primitive-height formula with no new symbolic-dynamics lemma; the parity correction is just the gcd(n,2) term and the sharp n^(-1/2) constants are standard Stirling. Takahasi’s primary article explicitly credits exact period counts to Hamachi–Inoue and provides embeddings, so the claimed distinct refinement is mathematically a direct classical coding-and-necklace corollary, not an uncovered independent theorem.

## value

FAIL

Although the near-neutral height statistic is naturally motivated, every reported exact number and rare-shell asymptotic is obtained immediately by combining an existing shift-equivariant full-shift encoding, standard necklace Möbius inversion, Chernoff and Stirling. No additional nonstandard structure, classification boundary requiring new insight, or mathematically independent precision remains. Reject as textbook specialisation rather than treating reproducibility or a new presentation as value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
