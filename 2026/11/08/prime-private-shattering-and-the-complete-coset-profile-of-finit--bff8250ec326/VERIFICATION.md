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

# Reproducibility and proof checks

The mathematical proof is in `RESULT.md` and uses no oracle or external computational certificate. Run `python3 VERIFY.py` with Python 3.10 or later. The program has only standard-library dependencies.

The verifier independently builds every congruence coset as a bitmask and enumerates Boolean traces for all support sizes through five when \(1\leq n\leq18\), evaluating \(43{,}794\) supports. It enumerates all three-element supports at moduli \(30,42,60,70,105\), with resulting counts \(240,504,2400,1680,5040\). Nine local prime-power/rank settings are exhaustively checked by direct residue tuples. For \(n=210\), it constructs all \(10{,}080\) CRT-designated maximum supports and checks their full traces; it also checks the formula's degree-three coefficient of \(170{,}520\).

Expected terminal marker: `ALL_COSET_SHATTERING_CHECKS_PASS`. These are finite validation tests. The universal proof's essential unbounded steps are the private-prime iff lemma, the CRT factorization, and the exact local \(p\)-adic count; the script does not replace them.
