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

Run `python3 check_2factor6.py` with Python 3 and no third-party packages. `CERTIFICATE.json` lists the exact expected outcomes. The reproducible checker tests two independently constructed 70-member graph sets, all Fourier coefficients by direct character sums and transform, the modulo-four law, the 512-element annihilator support, an independent quotient-transform computation of the inverse kernel, both exact histograms, Parseval and all 32768 inverse convolution identities. It exits unsuccessfully if any assertion fails and prints `TWO_FACTOR_K6_EXACT_PASS` only after they all pass.

The source-date 2005-02-25 is the verified first online date of the motivating 2-factor paper. The integer certificate proves claims only for the specified fifteen-edge group, not an arbitrary larger graph. The primary literature search is bounded and one plausible 2005 paper was accessible only as an abstract. No independent audit is represented.
