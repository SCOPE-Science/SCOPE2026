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

# Verification and reproducibility

The proof is self-contained apart from the standard cyclotomic degree formula and monic polynomial divisibility over the integers. Read the complete derivation in `RESULT.md`; computational tests are supplementary, not infinite-dimensional certificates.

Run `python verify.py`. The program uses only the Python standard library, evaluates every normalized ordered input pair for the five parameter cases, and checks the predicted support multiplicities and a separation between floating residuals and nonzero magnitudes. It does not establish exact vanishing on its own: that part is proved symbolically in `RESULT.md`.

Checked parameter cases: (p,q)=(2,3),(3,2),(3,4),(5,2),(5,4). Cases with the same prime dividing the phase alphabet and general composite alphabets are excluded. Independent mathematical review has not been performed.
