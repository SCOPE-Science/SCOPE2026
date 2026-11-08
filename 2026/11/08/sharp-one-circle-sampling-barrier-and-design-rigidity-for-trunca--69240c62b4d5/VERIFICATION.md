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

# Reproducibility of the sampling theorem

The analytic proof is in `RESULT.md`. Numerical checks are additional, not substitutes for the min–max inequalities, the equality argument, or Stirling asymptotics.

Run `python check_ring_sampling.py` with Python 3 and the dependency declared in `requirements.txt`. The deterministic checker directly constructs weighted coherent-state sampling matrices, computes singular-value condition numbers, tests multiple dimensions and observation counts, compares alternative radii and angular/weight configurations, and exercises both uniform and nonuniform circle designs. The observed output is:

`FOCK_CIRCULAR_SAMPLING_CHECKS_PASS 1010`

The finite checks cover \(2\le n\le13\), including several values of \(m\), and separate large-dimensional asymptotic checks through \(n=10000\). They do not exhaust the continuous domain of angles, radii, or weights. The general proof covers all admissible integer dimensions and all positive real design parameters. No independent audit, computer-assisted infinite certification, or validated error bound for floating-point singular values is claimed.
