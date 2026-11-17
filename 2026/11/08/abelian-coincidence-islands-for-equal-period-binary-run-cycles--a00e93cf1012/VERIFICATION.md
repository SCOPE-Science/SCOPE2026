---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For length n=tL+r in a cyclic 0^e1^f period, the full attainable zero-count set is the integer interval [te+max(0,r-f),te+min(e,r)], since phase shifts by one change counts by at most one and both extrema occur. With a>c the overlap is [ta+max(0,r-b), tc+min(c,r)], giving the claimed C(n). Solving the exact piecewise-linear level-set inequality with h=t(a-c) yields length islands [t(a+d),(t+1)(b+c)] for t<=floor(min(b,c)/(a-c)); these are pairwise separated, the terminal length is (T+1)(b+c), and summing disjoint island cardinalities minus n=0 gives the claimed count. Equal profiles a=c use the separate periodic formula. The finite direct enumeration of cyclic phases corroborates but is not the universal proof.

## originality

PASS

Best-of-knowledge original complete all-positive-length Abelian-factor coincidence classification for unequal equal-period two-run cycles. Finite RLE algorithms compute a longest common Abelian factor but do not imply this explicit infinite periodic disjoint-interval spectrum or shared Parikh-class function. Related two-run Abelian complexity and higher-power spectra concern a single word, not pairwise overlap.

## value

PASS

Exact nonmonotone Abelian-coincidence islands and sharp last common length give a natural structural classification for a basic family of periodic words, beyond applying finite-string matching mechanically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
