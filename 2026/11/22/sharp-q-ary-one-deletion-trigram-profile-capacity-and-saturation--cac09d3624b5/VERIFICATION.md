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

Translation by the original histogram preserves the number of outputs. At a deletion with two letters on either side exactly three old trigrams disappear and two new ones appear, giving the stated signed five-letter signature. Every signature has total −1 and nonempty support of at most five letters. Relabeling outside that support into it while fixing it leaves the signed result unchanged, even after arbitrary cancellations, so the census on each fixed support carries to every q. An independent exact replay in /workspace/branches/trigram_audit.py (run with Python 3) evaluated all k^5 neighborhoods for k=1,…,5 with integer sparse trigram coordinates: full-support counts were 1,8,90,192,120. Its direct boundary deletion test found four distinct signatures outside all ternary interior signatures, and the same collapse argument excludes realization over larger alphabets. The binomial support sum expands to M_q−4, and the four endpoint deletions add at most four; words shorter than five plainly satisfy the bound. The linearized order-five Euler circuit covers every neighborhood, and 0100 and 0012 fix the four exceptional boundary signatures independently of the middle. Padding before 0012 does not destroy any used five-factor or boundary signature. Independent Euler-circuit words and direct full-histogram differences attained 121,608,2069 for q=3,4,5 at witness lengths and at each witness length plus 11; the support and padding arguments, not these sample witnesses, prove all q and all stated lengths. The lower bound on first saturation is the number of deletion positions, giving the stated asymptotic but not the exact first length.

## originality

PASS

Credit the binary result and standard profile/de Bruijn machinery. The distinct supported finding is the q≥3 sharp polynomial for a fixed source and the saturation construction at all lengths at least q^5+12. No equivalent or dominating accessible statement was identified; inability to inspect some candidate full texts is a limitation, not negative evidence.

## value

PASS

The number of observation classes after an unknown deletion in a fixed string is intrinsic to the contiguous profile readout, not an unconstrained word count. The result determines exactly how support collisions and four endpoint events reduce the five-context bound, with explicit witnesses whose length is asymptotically minimal. This is a useful extremal benchmark for that model, independently of any coding-rate application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
