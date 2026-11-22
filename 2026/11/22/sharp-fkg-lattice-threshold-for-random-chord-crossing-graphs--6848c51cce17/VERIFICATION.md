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

# Reproducible checks and boundaries

Execute `python3 verify_chord_mtp2.py`. This standard-library-only program uses exact rational fractions. It independently enumerates multiset endpoint words and perfectly matched endpoints followed by all chord-label assignments. For every \(1\leq n\leq5\), the resulting complete labelled crossing-graph laws agree, including \(64\) positive graph states at four chords and \(1024\) at five. Its three-chord MTP2 comparisons cover every pair of Boolean states. It checks four-chord masses \(2/15, 2/45, 2/45, 4/315\), the strict ratio \(6/7\), pairwise covariances, and induced four-chord consistency from the five-chord law.

The exact finite enumeration directly establishes the obstruction and the three-chord base case. It does not, by itself, establish the classification for arbitrarily many chords; the self-contained proof of MTP2 marginal closure and coordinate-tilt cancellation in RESULT.md supplies that step. This verification makes no claim of independent mathematical certification or of completeness of the priority search.
