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

# Reproducibility and limits

Run `python3 checker.py` in the unpacked directory. The verifier uses only the Python standard library. It independently obtains the first 96 coefficients of the generating function from marked-part products and from the eta quotient, checks the precise modular truncations of the proof, and tests 80 even parameter values for 24 indices each. It checks sample Frobenius vanishings and the universal finite witness for every tested exceptional parameter. It returns `DESIGNATED_EVEN_FINITE_OK 80 even k, 95 coefficients, two methods, witnesses, Frobenius` upon success.

The proof of the infinite assertions is in `RESULT.md`. No finite range is an exhaustive proof of the infinite coefficient assertions. The external mathematical input is the exact two-dissection in Lemma 3.11 of https://arxiv.org/html/2611.05623; the polynomial and modular calculations in the proof are independently inspectable. No independent validation or external audit has been performed.
