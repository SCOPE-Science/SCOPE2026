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

Run `python3 verify.py` with Python 3.9 or newer. No third-party packages, external data, random seeds, or network services are needed. The script solves the *full unordered vertex-pair* stationary covariance system with exact `fractions.Fraction` arithmetic, independently of the orbit-reduction used in the written proof. It evaluates every root lag from 0 to 12 by explicit powers of the neighbor transition kernel for both \(K_{4,4}\) versus \(K_{5,2}\) and \(K_{6,6}\) versus \(K_{11,2}\). It also checks simultaneous integer fibers for each \(k\) from 2 through 15 using the stated lcm construction and confirms further exact examples.

Executed result: `VERIFY_OK 560 exact-rational assertions` (successful process exit). The mathematical generalization to arbitrary \(k\) is established by the exact formulas in `RESULT.md`, not inferred from finite tests.

All calculations use the refresh probability \(\varepsilon=1/2\) and the synchronous independent-copying model. These checks do not test full higher-time joint distributions or independently establish historical priority. Independent scientific validation has not been performed.
