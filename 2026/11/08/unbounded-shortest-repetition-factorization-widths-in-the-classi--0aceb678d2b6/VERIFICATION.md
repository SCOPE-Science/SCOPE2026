---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Let d=2^k u, u odd. Mismatches at n=2^k q-1 with q=2 mod4 occur every 4*2^k, ruling out u>=5 because comparisons need length>=d; for u=3 additional q=3 mod4 mismatches rule out that case. For dyadic d=2^k, q=1 or 2 mod4 are forced mismatches with gaps<=3d and at n=d-1,2d-1, giving start a>=2d and factor length<=4d-1, so endpoint a+length<3a. Dyadic blocks p[2^j:2^(j+1)) are squares of period 2^(j-1), giving r-factor construction. Any factorization from initial index 2 to final 2^(r+1) has s>r log_3 2 hence s>=floor(r log_3 2)+1. Finite independent DP for r<=8 and exhaustive bounded mismatch checks match proof.

## originality

PASS

Best-of-knowledge PASS for the classical bounded-run period-doubling word: previously published shortest-width divergence for an exponential-run automatic word does not cover this word; same-word least periods do not guarantee repetitions.

## value

PASS

A natural shortest-factorization invariant in a canonical uniformly recurrent automatic word exhibits explicit logarithmically growing lower bounds despite bounded monochromatic runs, demonstrating genuine periodic structure rather than trivial long constant blocks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
