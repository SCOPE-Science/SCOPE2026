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

# Verification

Run `python3 verify.py` using Python 3.10 or later. The script uses only the standard library, enumerates every proper four-colouring of cycles of lengths three through nine, and computes the complete Walsh transform independently of the prefix-count proof. It compares every exact coefficient against the theorem, checks the number of proper colourings against the chromatic-polynomial count, and checks the formula for every rank.

Executed successfully with marker `KLEIN_FOUR_CYCLE_FOURIER_PASS coefficients=349504`. Numerical ranges include 64 through 262144 characters at individual lengths. Since there are finitely many tested lengths, this is corroborating finite evidence; the theorem for arbitrary lengths follows from the written character-sum derivation and modular arithmetic lemma.

The preprint `arxiv:1204.1283` could not be inspected in full at the time of the historical comparison. No independent mathematical audit or validation has been performed.
