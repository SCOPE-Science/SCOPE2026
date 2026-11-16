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

# Exact checks and reproducibility

Use `python3 check.py` from the same directory. It requires Python 3.10 or later and standard-library modules only. The final success marker is `NONCROSSING_WALSH_EXACT_PASS`. The checker exhausts all binary signs on eligible chords for pairs 1–4, agrees with separate direct enumeration through three pairs, constructs inductive zero witnesses for all eligible lengths through 131 and for 256, checks nontrivial vertex-switch orbits for pairs 2, 4 and 5, and exercises independent pseudorandom sign configurations up to 32 pairs. Catalan valuations and the divisibility statement are checked as exact integers.

These experiments are finite; the proof of the unbounded quantifiers is in RESULT.md. The two-adic content, reflection pairing, and vertex-switch stabilizer are mathematical arguments, not outputs inferred solely from testing. Independent auditing has not been performed.
