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

For a cyclic independent word s of length L=n−1, let a_i=s_i OR s_{i−1} with indices mod L and repeat pair zero at i=L. During the rim sweep the closed count is 2a_i+a_{i+1}+s_i: at the first site the incoming neighbor is the repeated pair, at interior sites it is the already updated predecessor, and at the last the two updated neighbors have bits a_0 and a_1. If a_i=0 then s_i=0, if a_i=1 and s_i=0 the threshold tests a_{i+1}, and if s_i=1 then a_{i+1}=1. Thus the new rim is the shift by one. The degree-one leaf rule is b'_i=a'_i(1−b_i), giving s_{i+1} by cyclic independence. The first L leaf bits show injectivity. All-one rim states retain the rim and complement all leaves; the two families intersect only at the alternating words, two states for even L and none for odd L. The transfer matrix trace is Lucas, including the repetition test at e=1; divisor inversion on fixed words yields primitive orbit counts. Period two in the rotation occurs only at alternation, already counted among the 2^{n−1} leaf-flip orbits. This handles n=3 as well; a single one has exact period L for L≥3. An independent indegree-pruning check confirmed all stated finite recurrent counts at n=3–9, without extrapolating to general n.

## originality

PASS

The strongest retrieved overlap is the same-day two-sector classification for bare cycles under arbitrary permutation schedules. Its cyclic-order sector uses unrestricted binary words and it has no leaves. Neither it nor the synchronous sunlet results cover the encoded independent words coexisting with arbitrary leaf flips on the all-one rim in the claimed map.

## value

PASS

The natural decorated cycle gives a concrete mechanism for simultaneously supporting many two-cycles and long cycles in the same deterministic update. The explicit conjugacy and exact intersection resolve how two quite different recurring behaviours fit together. The value is not a new Lucas-word identity or a claim of global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
