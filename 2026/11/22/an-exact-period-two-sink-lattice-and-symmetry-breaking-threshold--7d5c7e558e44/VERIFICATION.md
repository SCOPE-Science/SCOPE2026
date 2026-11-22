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

The analytic reduction in `RESULT.md` proves all positive-gain cases claimed within the stated domain. No finite search is used as a proof of exhaustiveness. Run `python3 check.py` to reproduce the algebraic reconstruction and second-iterate Floquet diagnostics at representative gains and translation cells. The checker requires the Python standard library only and should print `VERIFY_OK`.

The tests include direct \(F_a(P)=Q\), \(F_a(Q)=P\) residuals, exact symbolic-form trace and determinant identities, the strict negative characteristic-polynomial value at one on side branches, the critical root and a local square-root coefficient diagnostic. The numerical tests do not inspect every real orbit or establish historical priority.

At \(a=1+\pi\), the central cycle is neutral and the two side formulas coalesce; the strictly attracting region excludes this endpoint. The upper sink endpoint is also neutral. The 2022 related lattice article was only available as metadata/abstract for the literature comparison.
