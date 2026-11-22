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

From the package directory, run `python verify.py` in a Python 3 environment. No third-party packages, network access or external data are needed. A successful execution prints `VERIFY_OK` together with the assertion count.

The checker reconstructs every scalar iterate using exact `fractions.Fraction` arithmetic on a broad rational grid, verifies the cubic filter and leading-mode invariance, and verifies separate diagonal matrix recurrences. It evaluates all candidate stationary extrema rather than identifying maxima only from a finite spectral grid. It checks the interior-to-cap minimax transition and the unique scalar crossing numerically over a dense parameter family, the golden-ratio endpoint-notch eligibility condition, and benchmark values. The reference run passed 110,612 assertions.

The proof in `RESULT.md` establishes the statements for all real admissible parameters; the finite executable tests do not claim exhaustive real-domain certification or independent mathematical audit. Roundoff error, noisy products, changing momentum, and optimality for more than three matrix multiplications are not verified.
