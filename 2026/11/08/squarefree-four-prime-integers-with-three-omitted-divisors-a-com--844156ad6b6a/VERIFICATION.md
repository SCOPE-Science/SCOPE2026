---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact-arithmetic verification

Run `python3 check.py` with the standard Python library; the resulting text is included in `check_output.txt`. The script deterministically evaluates the mathematically exhaustive 12 prime pairs times 455 omitted-divisor triples, certifies that every candidate largest prime is uniquely determined by the equation, and checks each retained case using integer divisibility and the exact sum-of-divisors formula.

The output reports 51 distinct integers and 60 unordered omitted-divisor triples; exactly eight integers have more than one triple (seven have two, one has three). Independently, the same program tests every integer through \(13000\) using direct factorization and its proper divisors; the exact sets of integers **and witness triples** agree.

The standalone proof in `RESULT.md` supplies a global bound on the first two odd primes and a single rational largest-prime candidate for every template. Thus the direct scan through \(13000\) is corroborating evidence only, not an unsupported inference from finite data to infinity. All outputs use exact integer arithmetic. Unindexed equivalent results and work outside the given squarefree support remain limitations. No independent external mathematical audit is claimed.
