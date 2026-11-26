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

For the fixed-n Kingman process with unit rate per unordered pair, the falling factorial moments follow by avoiding r tagged leaves in each merger down to level k. Conditioning on a cherry at step j uses a size bias by (B_j)_2, followed by removal of its two singleton children and uniform-pair survival of the other singletons. For j at or below k, propagating each candidate pair from k to j gives the other mixed-moment term. Summation yields the stated Cov(C_n,B_k), including k=2 and k=n; independent holding times cancel the k(k-1) factor. The remaining sum of m(m-1) from 0 to n-2 is (n-1)(n-2)(n-3)/3, giving -2/9. The cases n=2,3 have one cherry almost surely. This is external, not total tree length; changing the pair rate to beta scales the length covariance by 1/beta. The supplied Python verifier was inspected, not executed. A separate exact Markov calculation over level, singleton count and accumulated cherries checked n=2–8 and all 59 levels at n=60; replay at /workspace/branches/ffce9c23-6d79-44d8-a076-d828d732c8d4/replay_small.py and outputs replay_small.out and replay_60.out. Those finite checks corroborate rather than establish the universal proof.

## originality

FAIL

Multiple distinct indexed statements give exactly the two principal findings, on the same fixed-size Kingman model and normalization. The covered claim includes both the level-resolved formula and the -2/9 length covariance, not just one special case or one numerical match. This is a determination of covered mathematical content, not a claim about priority or provenance; the matching entries bear later catalogue dates, which alone do not settle either. The named primary-paper access limitation is not the reason for the verdict.

## value

FAIL

A sample-size-invariant mixed topology/length moment and its level decomposition would be useful exact benchmarks, but the entire proposed invariant, including the reusable level profile, is already available in other checked findings. The frozen proof and deterministic boundaries do not isolate an additional distinct mathematical contribution worth repairing toward.

The dated certificate retains the supplied scientific assessment, sources and limitations.
