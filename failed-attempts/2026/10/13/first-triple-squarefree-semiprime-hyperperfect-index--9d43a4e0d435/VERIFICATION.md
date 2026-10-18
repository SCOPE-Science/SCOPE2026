---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For squarefree semiprime pq the k-hyperperfect condition becomes pq=1+k(p+q), hence (p-k)(q-k)=k²+1 with positive factors. For p<q, let d=p-k, so 1<=d<=k; this bijectively parametrizes candidates with q=k+(k²+1)/d. An independent sieve enumerated p in (k,2k], tested primality of p and integer q=(kp+1)/(p-k) for all 1<=k<=132. Nonzero layers exactly 1,2,6,12,18,30,48,60,66,78,108,132. Double layers only 12 and18; k132 has precisely pairs (137,3617),(157,829),(173,557). Thus finite numerical theorem is correct.

## originality

FAIL

FAIL: McCranie (2000) Theorem 2 is the same exact semiprime parametrization and its paper reports a COMPLETE computation of all k-hyperperfect integers n<10^11, with the same three k132 pairs explicitly tabulated. Every solution with 1<=k<=132 satisfies p<=2k and q<=k²+k+1, hence pq<=2*132*(132²+132+1)=4,635,048 <10^11. The published full census therefore exhaustively covers ALL possible lower-index solutions; filtering its k-column yields exactly the submitted least-triple cutoff and double layers. This is covered by an exact database/table even absent identical theorem wording. The failing originality assessment is based on positive decisive coverage, not a failed search or access limitation.

## value

FAIL

FAIL: after crediting the classical factorization and the published COMPLETE table dominating the entire parameter range, the remaining task is a routine filtering/recounting of known finite entries. No separately justified new invariant, structural boundary proof, or mathematical implication beyond the pre-existing database remains. Computation/code correctness does not restore independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
