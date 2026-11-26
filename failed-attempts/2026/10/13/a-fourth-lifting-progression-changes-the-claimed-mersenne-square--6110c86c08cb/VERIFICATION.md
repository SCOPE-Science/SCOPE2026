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

FAIL

The bound itself is correct: independent modular computations give orders 6,20,21,110 modulo 9,25,49,121. Multiples preserve square divisibility, and a period of length 4620 contains 1034 classes from the first three orders and 1048 from all four, proving the lower bound 262/1155. The 14 extra classes are exactly 110k with gcd(k,6)=1 in that period. No density-existence assertion follows. The material defect is the characterization of Laniewski's result in the frozen Finding: the isolated abstract phrase 'on a set of exponents of density 47/210' is ambiguous, but the same v1 specifies lower density at least 47/210 in its introduction and precisely that liminf inequality in Corollary 6.20. The new bound rules out 47/210 as a possible exact density; it does not refute the preprint's stated density result.

## originality

FAIL

The decisive full text is Laniewski v1, Theorem 6.19 and Corollary 6.20. The general criterion there includes every multiple of 11·ord_11(2)=110. Using that theorem with one more small prime and counting its nonoverlapping residue classes is an immediate strengthening of the illustrative bound, not a distinct mechanism or a correction of the actual theorem. Coverage here means implication by the general theorem, not that 262/1155 was explicitly printed.

## value

FAIL

There would be value in refuting an exact-density theorem or deriving a substantive new lower-density mechanism. Here the source states a lower bound and already includes the extra progression in its all-primes criterion. The surviving arithmetic is a routine increment from one more small prime, with no sharpness or density-existence result; clarifying the abstract wording does not turn it into a new scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
