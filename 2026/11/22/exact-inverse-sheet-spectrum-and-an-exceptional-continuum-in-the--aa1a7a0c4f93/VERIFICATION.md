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

# Reproducibility and mathematical checks

`verify.py` is a Python standard-library script. Execute `python verify.py` from the containing directory. It prints `INVERSE_GEOMETRY_VERIFY_OK` when all checks succeed.

**Exact checks.** For each \(m=1,\ldots,12\), rational \(\delta\) with denominator \(23\) (including zero), and rational \(t\) with denominator \(19\) (including zero and negative values), the script counts integer \(\ell\) directly in \((-t,\delta+j-t]\) for every \(j\), and independently checks the predicted \(m(m-1)/2+m\mathbf1_{\{0<\{t\}\le\delta\}}\). This covers equality conventions but is finite diagnostic evidence only.

**Full-map reconstruction.** For selected nonexceptional targets and \(m=2,3,4,7,8,64\), the script reconstructs every candidate across all cubic sheets, then evaluates the original three-component map at every candidate and checks output error below \(10^{-8}\). At \(m=64\), the tested target triples have counted fibers \(110976\), \(111360\), and \(109856\); all were explicitly enumerated. It also tests that three distinct \(u\)-values with \(v=0\) yield exactly the same target for each chosen \(w\).

**Analytic proof scope.** These tests support reproducibility but do not certify the universal theorem on their own. Exhaustiveness over the continuum, every boundary case, and the infinite-fiber characterization are supplied by the explicit monotone inversion and integer interval proof in `RESULT.md`. No external audit, independent validation, cryptographic assessment, or formal proof assistant is represented.
