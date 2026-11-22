---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The exact proof is given in `RESULT.md`, Steps 1–3. The executable `verify.py` computes reachability by independent addition of the two generators up to \(ab\), extracts all maximal missing intervals, and compares their complete length histograms with the symbolic modular-rank formula. Tested domain: every coprime \(a,d\) with \(2\le a<50\), \(1\le d<a\), and every integer \(1\le q\le5\); 3,765 exact full-histogram comparisons passed.

Additional assertions verify the slope and intercept weighted sums, genus, modular-inverse total slope, the exact \(q\) maximal-length occurrences, and the displayed example. The proof establishes all \(a,d,q\) in scope regardless of finite test bounds. No external or independent audit has been performed.
