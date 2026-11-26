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

Repeated indices recover the source, distinct disjoint active swaps contribute C(r,2)−a uniquely by their four changed positions, all-distinct triples contribute 2(a−p) three-position changes, and a triple with exactly one equal boundary contributes a single endpoint-only change (h in total). The remaining outputs differ in one adjacent pair. If the original has an equal pair, an initial identity exchange pads every single swap. Otherwise only swapping an edge of an aba creates an equal pair for padding; both orders on an aba also yield one-effective-swap outputs. These exhaust the possibilities and give 1+C(r,2)+a+h−2p+s. For m=n−1 and all edges active, the deficit from C(n,2) is 2p−s, which counts starts of consecutive aba triples, i.e. abab. With any inactive edge, a+h=m−1−c_00, giving deficit (m(m−1)−r(r+1))/2+c_00+2p. It is positive with at least two inactive edges and zero with exactly one iff p=0. At n=2 all words tie, and a period-three word witnesses the bound for every n at q≥3. For type A, appending a nonreturning letter has q−2 choices; the one possible return is allowed only after a nonreturning triple, giving (q−2)(A_(n−1)+A_(n−2)) and the stated bases at n=2,3,4. For type B, split at the unique equal pair and fix the common letter. No aba can cross an equal boundary, so the two independent sides give the stated f_j f_(n−j) convolution. At q=3, A_3=12 and A_4=18 start 6F_n, while the two endpoint splits and n−3 interior splits give B_n=12(n−2) for n≥3. Independent replay: python3 /workspace/reviews/check_mathematics.py 4 directly generates all outputs on 22,978 symbol equality patterns of lengths 2–9 using at most five symbols, and recovers labelled counts by falling factorial weights for q=3,4,5. The structural proof covers all lengths and alphabet sizes in the claim.

## originality

PASS

The supported distinct result is the complete exact-operation optimizer classification and labelled census. The at-most-two ball and most of its local support calculation substantially overlap with a distinct same-day result. The exact sphere formula agrees with that ball whenever the source has an equal edge; the separate content in the structural lemma is accounting for attainable single-swap outputs when every source edge is active. Day-level dates do not establish chronology.

## value

PASS

Exact-operation ambiguity is a natural fixed error-budget observable, and the ball distribution alone loses precisely the overlap statistic that changes tie cases. The all-length classification and census show two genuinely different ways to attain the same sharp ambiguity, including repeated-symbol sources missed by distinct-triple ball maximizers. The Fibonacci-plus-linear count and its nonbinary generalization quantify the maximizing population, beyond merely subtracting an identity output or transferring the larger-ball bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
