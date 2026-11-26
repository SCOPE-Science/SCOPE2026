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

In each ordinary binary length group, the valid suffixes are tiled uniquely by 1 and 00. Sorting them splits them as 00L_(L−2) followed by 1L_(L−1), with one new gap G_L=2^(L−2)+1+1_{L even}. Inter-group gaps alternate between sizes 2 and 1 (in addition to the initial gap 1). An internal split at suffix length j appears once per legal prefix, so its multiplicity summed over suffix lengths L=j,…,K−1 is F_(K−j+2)−1. The collision G_2=G_3=3 yields the stated length-two count by the Fibonacci recurrence, also zero at K=2 where neither split appears. Gap size 2 gives floor(K/2) one-zero runs and the other nonempty runs come from G_j−1. All listed run counts diverge for fixed j or length, and every finite run occurs in a sufficiently long dyadic prefix ending with a one. Of F_(K+2)−1 total gaps, ceil(K/2) are size one; subtracting them gives the correct normalization. Binet asymptotics yield the stated masses, which sum to one via the geometric series. The scope is dyadic only. The recorded checks are finite; the uploaded verifier was not executed.

## originality

FAIL

A distinct indexed full finding already gives the exact support-gap spectrum, dyadic Fibonacci histogram and limiting law on the same Baum–Sweet word with the same endpoints. The change of variable g↦g−1 and omission of gap 1 gives the frozen nonempty-run theorem. The later index date establishes catalogue coverage, not earlier priority over the frozen record.

## value

FAIL

Exact multiscale run counts in this natural automatic word are a motivated invariant, but the full count and frequency law are already available for the equivalent support gaps. Renaming the labels and removing the empty intervals provides no distinct valuable remainder; an arbitrary-cutoff law was not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
