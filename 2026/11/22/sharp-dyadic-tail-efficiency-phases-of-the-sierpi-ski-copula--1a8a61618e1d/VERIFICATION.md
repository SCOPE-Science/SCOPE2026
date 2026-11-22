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
# Reproducibility and limits

The exact analytical proof is provided in `RESULT.md`. Run `python3 checker.py` with an ordinary Python 3 interpreter; no external packages or downloaded resources are required. The executable enumerates all first-\(m\)-bit odd-parity triple possibilities at every dyadic threshold for \(1\le m\le6\), compares each probability with the closed formula, verifies both cases of the attaining Bernoulli distributions, and checks exact sharp relative efficiency at sixteen dyadic scales. Its observed result is `PASS 1504 exact rational checks; all dyadic grid probabilities checked for m<=6`.

The generalization to arbitrary real thresholds and the explicit real-analytic logistic example are proved symbolically in `RESULT.md`; neither is inferred from finite enumerations. The latter uses an \(L^1\) upper bound and does not require numerical integration. All history/priority assessments are literature comparisons and are not independent mathematical validation.
