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

Both extreme recurrence coefficients of F^t are 1, giving bilateral surjectivity and a t-dimensional homogeneous space K_t with t consecutive free coordinates. Kernel trace surjectivity suffices for full image. It is also necessary for each fixed pattern: evaluating arbitrary configurations on the pinned sites exhausts the trace space, and a proper kernel trace gives a proper, varying coset as the target varies. At time b=2^m Frobenius makes K_b exactly the b-periodic sequences, so fullness is residue injectivity; fullness persists because F is onto. This includes a singleton at time one and m=0. Counting one site per occupied residue gives the binomial quotient; the log of the falling-factorial ratio is −k(k−1)/(2b)+O(k³/b²+k²/N) in the stated scaling, proving the phase-dependent limit. For the unrounded clock, z^s maps to evaluation on K_t, relations include (1+z)^t, and the t consecutive independent evaluations prove that the induced Laurent quotient is the full dual. Hence the first full-image time is one plus the maximum root order of a nonempty subset sum. For triples, odd subsets have order zero, and a pair has order 2^v₂(gap), by Frobenius and the simple root of the odd-power binomial, valid also after translating negative indices. Therefore the triple CDF at 1+2^(m−1) is exactly the injective-residue CDF with k=3. In the telescoping moments the tail numerator is 3·2^(−m)−2·4^(−m)−3/N+2/N² over Δ_N. Summing with increments 2^(m−1) and 3·4^(m−1), respectively, gives (5) and (6); the squared mean is O(R²) and the second moment has leading term 3N/2. The limiting CDFs at 3 and 5 are 3/8 and 21/32. These are statements about uniform unordered samples without replacement, the general rounded clock and the specifically three-site unrounded clock. The provided verifier was inspected, not executed; its finite checks are not needed for the proof.

## originality

PASS

There is material same-day overlap in the full-image residue criterion, random bucket sampling and unrounded-clock machinery. Credit those ingredients, not a new Frobenius or quotient mechanism. The surviving contribution in the frozen Finding is the general dyadic-window rounded law in the dilute phase regime, together with the arbitrary three-site unrounded law and its evaluated exact moments and tight limit. The checked results do not give that quantitative conclusion; this is not a finding of chronological priority over the same-day records.

## value

PASS

This is a concrete quantitative question that qualitative eventual onto-ness cannot answer: how widely dispersed pinned sites delay a full bilateral image. The phase-sensitive birthday scale for many pins and the three-pin contrast between a fixed median, logarithmically divergent expectation and order-N variance distinguish typical from mean behavior. The results are exact for the stated sampling models and do not claim unrounded times for general k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
