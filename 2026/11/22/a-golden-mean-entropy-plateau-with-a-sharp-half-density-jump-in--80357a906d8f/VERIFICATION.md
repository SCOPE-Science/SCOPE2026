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

For the exact one-sided shift closure and ties-up rule, the discrepancy increases by β on a 0 and decreases by 1 on a 1. At fixed starting discrepancy, appending an initial 0 leaves at most b_(n−1) choices; an initial 1 determines the second digit, and dropping any residual constraint on the third leaves at most b_(n−2). From b_0=1, b_1=2 this gives the Fibonacci bound. Over all starting discrepancies, every transition in an n-word depends on the sign at a threshold o−βz with 1≤o+z<n, so there are at most n²+n−1 regimes including ties and the n=1 case. Cylinders are open, so closure adds no previously absent finite words. For β<1, each 1 in (10)^N has negative discrepancy, and the discrepancy after the whole prefix tends to −∞. A sufficiently long such prefix lets any finite no-11 word obey the correct rule through its trailing zero continuation. The proof works for arbitrary real β in the relevant ranges, so golden-mean inclusion matches the entropy upper bound for all 0<p<1/2. Independently of the endpoint citation, at β=1 the generator consists of concatenated blocks 0^k1^(k+1)0, k≥0, with a possible terminal all-zero tail: from discrepancy 0, the k zeros build discrepancy k, the following ones are forced until discrepancy −1, and the forced 0 restores 0. Complete blocks of total length 2m are counted by compositions of m, giving 2^(m−1) words. Factors can trim at most two boundary blocks; each partial piece has only polynomially many possibilities at length ≤n (each block has at most two runs plus its final zero), as do factors entirely within one block or the zero tail. The resulting upper rate is (log 2)/2, matching the complete-block lower rate. Hence the left jump is real since φ>√2; no right-hand claim is made. The supplied finite checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the all-real sub-half plateau and the parameter-uniform language bound; the left discontinuity combines this with an already credited endpoint value. The exact-index match is the same record. Relevant distinct indexed rational and irrational results do not state a matching entropy theorem below 1/2 in the material read. Primary-source access limits remain, especially for the founding article.

## value

PASS

The rule has unbounded historical memory, so the language of all shifts cannot be counted by fixing one initial discrepancy. Showing that past history contributes only polynomial multiplicity while every golden-mean factor is realizable below half determines an exact invariant on an entire real parameter interval, including irrational parameters. Combined with the known half-density entropy, it shows an explicit and strict left discontinuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
