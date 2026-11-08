---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For distinct nonempty scattered palindromic patterns, first/last enclosing occurrences give the exact bijective decomposition P(w)=sum_a[1+1_{a repeated}(1+P(I_a))]. Distinguishing equal from unequal endpoint symbols gives sharp bounds 4+M_{n-2}+M_{n-4} and 4+2M_{n-3}. With n=0..3 bases, the two Fibonacci recurrences and parity-restricted equality cases establish all-length maxima M_{2m}=2F_{m+3}-4 and M_{2m+1}=F_{m+5}-4 and exactly two odd/four even maximizing words (the two alternating orientations and, for even n, two vv^R with alternating v). Independently enumerated actual sets of distinct palindromic subsequences for every binary word n=0..10, reproducing all maxima and maximizer sets; finite checks are corroboration, not the all-length proof.

## originality

FAIL

FAIL: Palak Pandoh’s publicly posted slides dated 21 June 2021 state EXACTLY the same binary Fibonacci maxima and classify the same alternating/central-reversal words as all scattered 2-ary palindromic-rich maximizers, expressly credited to Mahalingam and Pandoh (slides in section “Scattered palindromes in a finite word”, around lines 260–300). Both theorem and maximizer classes were therefore publicly disclosed prior to this record; a later August 2021 arXiv preprint omitting the all-length q=2 statement does not restore originality. The record does not isolate a distinct new theorem, so its final scientific claim is rejected without revision.

## value

PASS

The exact all-length extremal counting and exhaustive equality classification would be a mathematically meaningful finite-word combinatorics result, especially the change of equality shape with parity. Its prior disclosure defeats originality, not the intrinsic mathematical substance of the underlying theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
