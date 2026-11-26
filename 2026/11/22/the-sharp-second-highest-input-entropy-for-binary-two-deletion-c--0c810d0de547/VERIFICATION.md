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

Reviewed RESULT.md:5–158, VERIFICATION.md, both scripts, and the nonstandard imported lemmas in Ma–Zhang arXiv:2611.01064v1 (Lemma 2.1, Lemma 3.1 Eq. (7), §3.2 Eq. (10)). Uniform inputs and equally likely pairs give posterior weights proportional to embeddings, with Z=4 binom(n+2,2) by filling the two unused positions independently. Thus minimizing Φ=sum e log2 e maximizes the entropy. The verified run formula and strict adjacent-increment bound charge at least c_n per nonsingleton run, with equality only at length two. For one such run of length r, the two weights sum to n+r+2; strict convexity minimizes at balanced integer weights, and the minimum is strictly increasing in their sum. Thus r=2 and |s_0−s_1|<=1 characterize equality. For q>=2, the weight sum is n+U+q+1>=n+3q+1. The Jensen bound G_n(q) lies more than 1 above G_n(1), since on t>=1, n>=4 its derivative exceeds (3/4)n−2>=1. The integer balancing loss at q=1 is less than 1 by the bound using f''(x)=1/(x ln 2); hence no q>=2 case ties. At n=2,3 there is no q>=2 case. The alternating maximum is strict by the cited Theorem 2.2, so subtracting its Φ gives the positive stated Δ_n; division by Z yields the entropy gap. One balanced position for even n and two for odd n, each with both starting bits, give the word counts. The expansion Δ_n=(6 log2 3−9)n+3 log2 n+O(1) and Z=2(n+1)(n+2) give the stated limit. At n=1 there is no strict second level. Independent replay: python3 /workspace/branches/replay_frozen_review.py 4 counted each two-position insertion witness and compared exact products, checking the run formula for all 2,044 words at n=2..10 as well as both top levels and complete tie classes. This is finite corroboration, not the all-length argument.

## originality

PASS

The first entropy maximum, the run-functional machinery, and finite runner-up examples are prior. The supported distinction is the strict all-length second level, full balanced-double-run equality class, and its explicit gap and asymptotic, proved by a uniform separation of every multi-defect run pattern. The closest primary theorem and data were read and compared at statement level.

## value

PASS

Given the known alternating maximum, the exact entropy loss to the best nonalternating observation is a natural stability invariant. Knowing the complete centrally balanced one-defect equality class and a positive limiting n-scaled gap says more than either a strict maximum or a finite runner-up table. The conclusion is for uniform binary two-deletion channels, not general synchronization errors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
