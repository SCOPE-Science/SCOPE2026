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

Taking adjacent differences modulo 3 gives signs ±1; abab corresponds to an alternating triple, so comparison bits avoid consecutive ones. The six initial letter/sign choices give 6 F_n admissible words. At an interior substitution the neighbors must coincide; swapping the local sign pair (s,-s) to (-s,s) then creates an alternating triple with the next unchanged sign, or with the previous one at the last interior position. Such an unchanged sign exists for n>=4. Thus all moves are at endpoints. For n>=5 the two endpoint restrictions are independent: each has two choices on an equal-sign pair in the core and one choice on an unequal-sign pair. For k=n-4>=2 core comparison bits, the counts with endpoint types 00, exactly one 1, and 11 are F_k, 2 F_(k-1), F_(k-2), obtained by fixing endpoints and their forced zero neighbors; at k=2 the counts are 1,2,0, and at k=3 the 11 case is just 101. Each core contributes a connected K_1, K_2 or C_4, with six initial choices per bit string. At n=5 there is one comparison bit, and at n=4 the forbidden word removes one vertex from each endpoint square. The independence polynomials multiply; their degrees and leading coefficients give the asserted sizes and counts. Dividing by 6 F_n and taking Fibonacci ratios gives phi^(-6)+2 phi^(-5)+2 phi^(-4)=5-2 sqrt(5). The alphabet, boundary model and detection-only reading are essential.

## originality

PASS

The admissible language and its Fibonacci cardinality are prior. The supported distinct contribution is the exact Hamming-one component structure on that language and the resulting full independent-set and maximum-codebook enumeration. Neither the closest different-edit problems on this same language nor the inspected mixed-channel results cover those invariants.

## value

PASS

The constrained source language is established in coding theory. The graph's confinement to fibers of the whole interior is a structural restriction not visible from Fibonacci enumeration alone. It identifies the complete set of editing-confusability components, yields the exact optimum for one-substitution detection, and gives the total number of codebooks at every size and a nontrivial limiting occupied fraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
