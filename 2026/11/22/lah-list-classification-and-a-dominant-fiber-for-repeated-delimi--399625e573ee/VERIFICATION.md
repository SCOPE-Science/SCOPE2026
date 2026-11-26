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

Subtracting outgoing or incoming edge counts from unigram counts recovers the last and first letters. Each singleton then has forced neighbors when present; since the observed trail comes from a word containing a, these forced chains recover the prefix, suffix, and unordered distinct nonempty returns at a. Conversely these lists along with r determine all edges, including r−1−k copies of aa. Combining the prefix and suffix into one ordered list with a distinguished separator gives exactly the sets of k+1 nonempty lists on s+1 atoms. Counting permutations and cuts then dividing by (k+1)! proves the Lah count. Ordering the distinct returns and indistinguishable empty gaps gives (r−1)!/(r−1−k)!. The largest stratum index is s and includes one profile, so missing it at r=s proves sharp saturation for s≥1. Dividing its fiber size by (r+s)!/r! gives the stated product and expansion; s=0 and r=1 obey the same formulas. At r=s+1 and s≥1 the k=s profile is not the unique largest fiber, because k=s−1 ties; this is allowed by the finding and does not affect fixed-s asymptotic dominance. Independent direct enumeration passed 14 cases, including saturation boundaries and coinciding sizes. For (r,s)=(4,3) the merged histogram was 1:24, 3:36, 6:13, with 210 words in 73 profiles.

## originality

PASS

Credit general individual-class enumeration and the known Lah numbers and saturated sequence to prior work. The distinct content is the full fixed-content quotient classification, not a new Euler-trail formula, a new combinatorial sequence, or an assertion that this saturated number is unknown. No equivalent classified source language was found in the inspected materials.

## value

PASS

This is a natural fixed-content reconstruction model where the observation forgets ordering only at one repeated letter. The complete quotient and fiber-size spectrum, including degenerate and saturation regimes, are useful beyond the size of any single class. A distinguished list identifies precisely the retained information and explains how almost all words can concentrate on one fixed profile even when the number of possible profiles has stabilized at a nontrivial value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
