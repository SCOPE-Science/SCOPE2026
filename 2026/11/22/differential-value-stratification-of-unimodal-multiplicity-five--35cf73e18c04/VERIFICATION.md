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

# Reproducible verification and boundaries

The accompanying `VERIFY.py` script (Python 3 standard library only) computes the image of the three formal derivatives multiplied by every coefficient monomial of valuation at most eight, truncates at coefficient degree twelve, and uses exact `fractions.Fraction` Gaussian elimination to identify differential leading values up to thirteen. Execute `python3 VERIFY.py`; a successful run terminates with `PASS`.

The executed test set comprised 35 cases: seven of type \(\langle5,6,7\rangle\), two of \(\langle5,6,8\rangle\), eight of \(\langle5,6,9\rangle\) including the exceptional coefficient \(13/12\), and eighteen of \(\langle5,7,8\rangle\). Every test returned the predicted values. All parameters in these tests lie in \(\mathbb Q\subseteq k\); this is not an exhaustive test of the algebraically closed field.

The proof does not extrapolate finite checks. Symbolic differential expansion produces the exact determinants \(60b-65\) and \(60c\) for the only potentially exceptional value. An exhaustive gap analysis and the conductors of the numerical semigroups establish the rest for every permitted parameter. The correctness proof and its analytic-equivalence prerequisites appear in `RESULT.md`.

The normalized value convention assigns \(\nu(h(t)dt)=1+\operatorname{ord}_t h(t)\). No statement is made about the torsion submodule of abstract Kähler differentials or about positive characteristics. The general standard-basis literature provides an alternative calculation framework, but the historical-example priority comparison is incomplete.
