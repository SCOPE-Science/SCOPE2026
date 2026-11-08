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

The claim concerns the matrix \(A_\kappa=\operatorname{diag}(\kappa,1,\ldots,1)\) and the projector onto \(\operatorname{range}((A_\kappa A_\kappa^\top)^q A_\kappa\Omega)\), with real iid Gaussian \(\Omega\). The proof establishes almost-sure full rank when \(1\le k<d\), reduces the squared Frobenius error to \(d-k+(\kappa^2-1)/(1+\kappa^{4q+2}\gamma)\), derives \(\gamma\) as a ratio of independent chi-square variables, and derives the three limiting cases of a beta integral.

The standalone `verifier.py` uses Python with `numpy` and `mpmath`. Invoke `python verifier.py` in the directory containing the file. The recorded run in `verification_output.txt` had 460 passing checks. For deterministic reproduction, the Gaussian-test seed is fixed; 440 direct QR/projector identities were checked at diverse dimensions, sketch widths, spike sizes and power counts. Additional assertions compare special cases, the beta integral and hypergeometric evaluation, and large-spike leading coefficients.

**Limits of computational evidence:** Finite QR samples do not certify distributional equality; quadrature and asymptotic spot checks do not prove infinite limiting claims. The source of the proof is the explicit projector and chi-square regression calculation in RESULT.md. The numerical experiment is not an independence or external certification procedure. Computations use floating-point arithmetic; the analysis assumes exact arithmetic and fixed parameters when the spike grows.
