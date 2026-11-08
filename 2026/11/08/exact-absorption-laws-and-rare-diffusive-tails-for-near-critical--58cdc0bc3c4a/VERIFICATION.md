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

# Reproducibility and verification

Run `python3 verify_sticky.py` in a Python 3 interpreter. No installation, network access or external data are needed. The code independently constructs and updates the original absorbing many-player Markov chain without applying the proposed first-two-round reduction, and derives finite-state rational transforms and expectations by Gaussian elimination. It then separately calculates the proposed gambler’s ruin mixture. The observed output was:

```
EXACT_CHECKS_OK 2205 survival m<=10, t<=32; pgf and mean m<=8
```

The 2,205 assertions consist of every survival time \(0\le t\le32\) for all \(2\le m\le10\), \(0\le k\le m\), plus independent rational probability-generating-function checks at \(z=1/2\) and \(z=2/3\) and exact expected-duration checks for \(2\le m\le8\). They do not constitute an exhaustive check for unbounded \(m\) or a numerical verification of limits. General validity follows from the first-two-round conditioning proof, gambler's ruin recurrence, spectral diagonalization and uniform domination argument in `RESULT.md`.

For the continuous-density limit, substitute \(z=e^{-s/m^2}\) into the proved exact generating function, and verify \(m\operatorname{arcosh}(e^{s/m^2})\to\sqrt{2s}\). For sparse excess, use the exact killed-chain sine expansion including eigenvalues near \(-1\), and retain the \(N/a\) entrance factor. The source's two-step idea is credited; the quantified laws and all quoted assumptions are explicit. No independent audit or formal proof-assistant certification has been performed.
