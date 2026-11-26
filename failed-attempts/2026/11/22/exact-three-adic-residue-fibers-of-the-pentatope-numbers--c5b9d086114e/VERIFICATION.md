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

The two nonsingular branches have divided differences equal to ±1 modulo 3, so each contributes one preimage at every level. With w=2t−1 the third branch is 3(w²−1)(9w²−1)/128. Its quadratic coefficient after subtracting 3/128 and factoring 3w² is 1 modulo 3; its Hensel square root b(w) satisfies b(t)−b(s)∈9(t−s)Z_3, making w↦wb(w) bijective on all quotients and on Z_3. This gives the square-root count including the factor of three in the lifts and k=1. The period 3^(k+1) works in each branch, but the shift 3^k fails in the n≡1 branch by its exact isometry. Counting nonzero square residues by even valuation and counting the zero roots give the histogram; the square set has measure (1/3)∑3^(−2j)=3/8, and scaling by three gives 1/8 for the enhancement set, not the full image. Replayed independently by separate branch histograms and the failing period shift for k=1,…,8 (`python3 /workspace/frozen_review_replay.py 3`); this supports but does not replace the all-level proof. The frozen script was read, not run.

## originality

FAIL

A distinct indexed result gives the same least period, full square-root fiber law, complete histogram, and enhancement set and measure for the identical fourth binomial column at 3, and also gives the Haar pushforward density and exact three-adic inverse-fiber counts. The evidence establishes equivalent coverage, not chronological priority between the two same-day records. No distinct surviving mathematical claim was identified.

## value

FAIL

The ramified three-adic fiber distribution of a natural integer-valued polynomial is a worthwhile exact invariant in itself, but this submission gives no additional invariant, sharper conclusion, or different useful mechanism beyond the matching indexed theorem, which already contains the same global square normal form and strictly more output information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
