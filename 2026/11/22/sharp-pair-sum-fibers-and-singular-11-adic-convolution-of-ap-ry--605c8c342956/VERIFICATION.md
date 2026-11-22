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

# Reproduction and verification

Run `python3 CHECK.py` with Python 3's standard library only. The checker reads no external data and constructs its own digit transfer matrices. At preparation it passed 301 grouped assertions: all eleven Apéry digit values modulo eleven; the two-digit Lucas congruence for 121 indices; exact digit-pair correlations; signed-carry characteristic data; direct ordered-pair histograms for primes 5, 7, 11 and 13 through depth two; and every target's full spectrum, extrema, and energy through eleven-adic depth four (direct pair enumeration through depth three). It verifies the rational inequality used in the strict correlation-dimension conclusion and the normalization of stationary output-digit frequencies.

The all-depth statements rely on the established Lucas congruence, the proved exact carry identities, the finite irreducible Markov chain's ergodic theorem, and the positive transfer-matrix eigenvalue. None of these infinite conclusions is inferred from the finite checker output. The historical-equivalence comparison in `AUDIT.json` is a best-knowledge scholarly review, not an independent certification or a proof of worldwide novelty.
