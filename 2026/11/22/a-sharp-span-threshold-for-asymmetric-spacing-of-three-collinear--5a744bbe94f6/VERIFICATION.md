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
# Verification and limits

The complete symbolic proof is in `RESULT.md`; no external formal certification is claimed. Running `python3 verification/wake_layout_check.py` from the package root completed 19,724 supplementary finite assertions. The program uses exact Python `Fraction` arithmetic for selected derivative sign expressions, seeded floating-point finite comparisons, and independently bisected optimum and critical span checks. It is standalone and requires Python 3, with no downloaded assets.

The exact signed derivatives of the two monotone terms, the strictly positive speeds, endpoint crossing and midpoint sign constitute the proof for the entire quantified domain. Sampling cannot prove a global optimum or establish nonexistence of other roots beyond the analytic argument. For \(\delta=1/5\), \(\kappa=1\), \(\ell=1/2\), the diagnostic critical span is about \(1.0617970425831\); for \(L=3\) the optimum is about \(1.5113339039885\), with a small normalized power gain of approximately \(1.0464271885\times10^{-5}\) against midpoint spacing. Numerical values are illustrations rather than exact algebraic certificates.

The theorem does not extend automatically to quadrature wake merging, nonuniform wind, wake turbulence, changing thrust curves or real turbine yield. The literature priority comparison includes inaccessible older papers and is qualified accordingly.
