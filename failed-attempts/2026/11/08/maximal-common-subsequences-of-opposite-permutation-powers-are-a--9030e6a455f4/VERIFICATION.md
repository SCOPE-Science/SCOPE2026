---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For P a permutation of q>=2 distinct letters and k>=1, greedy embedding in opposite linear block orders consumes 1+des+equal or 1+asc+equal blocks. Replacing an equality by xy,yx is budget preserving; the one-budget-saturated insertion argument uses boundary letters and telescoping to show every shorter common word extends. Thus maximal words are adjacent-distinct with exactly k-1 rises and falls, length 2k-1. The transfer recurrence is the classical Smirnov descent generating function, and palindromes are determined by q choices initially and q-1 for each of k-1 first-half steps. All q,k logical boundaries included. Direct independently constructed two-host subsequence enumeration produced (q,k,maximal,palindromes)=(2,3,2,2),(3,3,36,12),(4,2,28,12),(5,2,60,20); no finite check substitutes for the proof.

## originality

FAIL

The full October 18 2026 published reverse-periodic-permutation theorem establishes the SAME forall-q,k rigidity, SAME exact balanced rise/descent characterization and length, and a general all-q transfer-matrix coefficient plus ternary closed values. The present rational Smirnov GF is a different algebraic representation of the already determined identical enumerator; its elementary palindrome mirror count follows immediately from the earlier complete characterization. The original central claim is exactly covered; no separately motivated original invariant survives. Correctness does not cure prior coverage.

## value

FAIL

The exact maximality/longest rigidity and all-alphabet cardinality are already established for the same input words in the October 18 theorem. Reformulating the known transfer count through an existing Smirnov rational function, and its routine palindrome specialization, adds no independent worthwhile mathematical content in this submission; finite checks/reproducibility are not added value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
