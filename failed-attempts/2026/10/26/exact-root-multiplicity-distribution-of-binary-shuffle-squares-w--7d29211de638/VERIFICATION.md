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

For fixed q, matching the copy with the first one and the copy with the last one gives q≤A≤2q and m−q≤C≤2(m−q). The unfilled before-one zeros of the second copy and after-one zeros of the first copy add to B, proving sufficiency. Requiring at least s+1 integers in the interval is equivalent to A,C≥2s and 2s+(A mod 2)+(C mod 2)≤B≤m−s. Subtracting 2s from every gap preserves outer parities and gives exactly the existence inequalities at m−3s, including empty ranges and m=0. Taking tail differences gives the census and extrema. Summing S(m) gives (1+x+x²)/(1−x)^3; taking the tail difference and summing in t gives the stated bivariate series. The limiting conditional tail follows from the quadratic leading term with t=floor(mu)+1; the conditional mean follows also by the incidence identity. A fresh exhaustive position-split check (/workspace/audit_replay_1.py) found identical root sets for all 252 words at m=0 through 6; at m=6 there were 27,45,18,1 words with respectively 0,1,2,3 roots. The all-length result rests on the proof, not the bounded replay.

## originality

FAIL

The substantive theorem has equivalent coverage in a distinct catalogue record: the same root interval, full inverse spectrum and three-gap bijection for all lengths. The catalogue path is dated after the frozen path, so this is a finding of exact duplication in the available record, not a finding that the assigned record lost historical priority or derived from the match. The generating function and conditional limit in the frozen record are automatic consequences of the matched theorem, not a distinct substantive result. The earlier papers and the OEIS entry cover only parts of the claim.

## value

FAIL

The ambiguity of sparse shuffle-square roots is a natural exact invariant and the gap bijection is mathematically useful. As a distinct contribution in the reviewed material it is already completely covered by the matched theorem. The remaining generating function, limiting law and incidence check are routine consequences or already covered by earlier forward counts; they do not supply a separate worthwhile unknown fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
