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

# Reproduction and boundaries

Execute `python3 verify.py` (Python 3, standard library only). The script builds every matrix in \(\mathrm{GL}_k(2)\), for \(0\le k\le4\), constructs every affine translation \(x\mapsto Mx+b\), evaluates compositions as actual functions on all \(2^k\) points, and counts fixed points. It separately generates all affine subspaces in dimensions up to four by closure, compares the numbers to Gaussian coefficients, and combines exact domain counts with local involution counts. It checks every joint domain-size/fixed-point stratum against the closed formula, not only totals. The outcome is `VERIFY_OK`.

Observed total self-inverse counts for ambient dimensions \(d=0,1,2,3,4\) are \(2,5,27,297,6113\), with corresponding fixed-point-free counts \(1,2,10,120,2656\). The complete affine involution spectra for internal dimensions zero through four are printed by the script. It also evaluates the finite-product constant \(\delta=0.06056210400129026\ldots\) and verifies the predicted asymptotic trend (global fixed-point-free proportion \(0.499775651268\ldots\) at ambient dimension twenty).

Finite enumeration and numerical convergence cannot prove the statements for unbounded dimensions; the structural counting and dominated-convergence proof in `RESULT.md` provide that argument. No external independent audit, Lean project, or third-party computational certification is asserted.
