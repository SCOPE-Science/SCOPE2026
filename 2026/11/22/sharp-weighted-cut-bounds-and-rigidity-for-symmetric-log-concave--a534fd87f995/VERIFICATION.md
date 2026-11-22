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

# Verification record

## Analytic checks

The universal inequalities are proved in `RESULT.md` via the explicit cut derivative, the exact survival identity, a log-concavity midpoint inequality, and the independent uniform-scale-mixture identity. All normalization factors of \(2\), \(3/2\), and \(4/3\) are given with derivations. The equality cases follow from zero-defect constraints on the nonnegative integrands, not extrapolation from data.

## Reproduction

Run `python3 check.py` from the package directory using any modern Python 3 interpreter. It uses only `fractions.Fraction`, calculates exact rational interpolation values for \(101\) parameters, checks the endpoints, evaluates independent uniform-radius pair formulas for \(361\) radius pairs, and verifies one nontrivial two-atom mixing-radius defect. Expected count: `768` exact rational assertions (as reported by the script).

## Limits

The finite exact checks test algebraic special cases, not all inputs. The infinite-dimensional inequalities do not rely on a computer or an external certificate. No new claim is made about prior independent audits or peer review. Historical priority over all variants of Gini/MAD inequalities is not established by an incomplete bibliography search.
