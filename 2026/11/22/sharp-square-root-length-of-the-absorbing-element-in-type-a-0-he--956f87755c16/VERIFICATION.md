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

A reduced word of length m used twice can increase inversion length by at most 2m, so m≥ceil(L/2). The disjoint four-cycles in the witness give the stated outer one-line entries at each four-degree extension; they add n inversions from outer n+4 to the old block, n from the old block to outer 1, and three among the four outer entries. The base lengths 1,2,3,5 cover all degrees. In the even-L classes the four-cycles square to the reversal transpositions and the central point, if present, is fixed. In the odd-L classes the central transposition or three-cycle gives w_n²=w₀sᵢ and a right descent at i. Choose a reduced word for w_n ending in sᵢ. The prefix of its second copy represents v=w_nsᵢ and w_nv=w₀ with length additivity, so every step of that prefix increases length and the last sᵢ is absorbed. This also proves the odd witness without requiring the more general subword comparison in the record. At even L, equality in the length bound means no omitted comparator, hence w²=w₀. Conversely ordinary roots have w₀w=w⁻¹, giving L−ℓ(w)=ℓ(w), and attain w₀ in the Demazure product. Ordinary group roots pair the 2k transpositions into four-cycles, two orientations per pair, and fix the optional singleton, giving (2k)!/k!. Independent checks from the one-line recursion and a separate reduction by rightmost descents passed through degree 52; a full scan of the minimal length layer through degree 8 agreed, including set equality with ordinary roots in the even-L cases. Replay with python3 /workspace/audit_checks.py 5.

## originality

PASS

The supported distinct contribution is attainment of the half-length lower bound for identical two-pass Demazure schedules in every degree, especially the parity-obstructed odd-L classes, together with identification of the even-L minimizing layer. Ordinary square-root cycle pairing and its count, the Bruhat subword property, and the length lower bound are standard; they are not credited separately as new. The checked power results constrain the first factor to Coxeter elements and do not give the unrestricted repeated-word optimum.

## value

PASS

The shortest identical two-pass adjacent-comparator schedule is a natural constrained way to reach the absorbing element. It is not clear from the length bound that the repeated-copy constraint allows a globally optimal length, in particular when parity bars an ordinary square. The witness achieves the unavoidable bound with exactly one omitted comparator in that parity class and explains the transition to the ordinary group-root layer in the other class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
