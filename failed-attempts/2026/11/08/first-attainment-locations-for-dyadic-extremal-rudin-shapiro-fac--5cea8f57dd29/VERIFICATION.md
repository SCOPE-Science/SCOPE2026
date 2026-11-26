---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the one-sided zero-indexed word, padding the offset to k bits adds only the possible 11 across the join, so aligned blocks are signed P_k for even m and signed Q_k for odd m. The concatenation recurrences give the stated p,q,U,V by induction, also maintaining nonnegative prefixes via V_k≤p_k. The split at half the block gives the stated bounds for a+b and a−b. For k≥2 the P-then-Q bound is strictly below H_k. In the Q-then-P case the maximizing offsets require aligned signs at even k and opposite signs at odd k, with both nonzero contributions at equality. The first matching signed block pairs are m=1 and 11 for even k, m=3 and 5 for odd k, by direct signs of m and m+1. Their smallest offsets are (2L+1)/3 and (L+1)/3 respectively, coming from the least prefix maxima and lying strictly below L. This proves the global first starts suggested by the finite checks. An independent exact replay for 2≤k≤15 computed all signed adjacent-block types and their first block indices, enumerated every offset per type, and reproduced both extrema and first indices. This checks finite cases, not a replacement for the infinite proof. The prior-recurrence derivation below also confirms the formulas.

## originality

FAIL

The first-start formulas are mathematically correct but all four follow as a direct equality case of the already published fourfold sliding-window recurrence (Lü–Chen–Wen–Wu, Lemma 4(1)–(4)), together with their known extrema and two small anchor lengths. This is specific position-sensitive coverage, not an inference from the complexity spectrum alone or from mere computability. Separately, published prefix-extremum and shift identities already imply the even-positive branch. No source was found printing the identical four-formula display apart from the same Resultary record; the failure is mechanical corollary coverage, not a claim that the display appeared verbatim.

## value

FAIL

Shortest prefixes containing extremal factors are a natural observable, but the claimed closed forms are obtained by the direct equality case of the published per-position recurrence and two fixed tiny anchors. The self-contained block proof may be expository, but the finding does not contain a separate non-mechanical exact result to credit: it neither classifies a wider family of first locations nor delivers a different structural theorem as its claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
