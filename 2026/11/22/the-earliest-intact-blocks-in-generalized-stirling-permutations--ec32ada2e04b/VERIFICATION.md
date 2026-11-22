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

# Reproducibility and checks

Run `python3 CHECK.py` (Python standard library only). A completed execution returned `PASS: 288 exact/numerical assertions; no simulation-based infinity claim`. The program constructs valid \(r\)-Stirling permutations by their unique gap-insertion histories and enumerates all selected-label intactness events in complete small word spaces for \(r=2,3,4\), with exact `Fraction` arithmetic. It independently evaluates the product inclusion probability from the proof. It also checks the analytic first-moment scaling at large finite \(n\) through log-Gamma ratios. All checked identities passed.

The central point-process assertion is an *infinite-size theorem* established analytically through joint inclusion probabilities, a controlled rare-window product approximation and a uniformly dominated Laplace-functional expansion; the finite checker is only a consistency test. No growing-multiplicity theorem, quantitative convergence rate, or independent audit is asserted.
