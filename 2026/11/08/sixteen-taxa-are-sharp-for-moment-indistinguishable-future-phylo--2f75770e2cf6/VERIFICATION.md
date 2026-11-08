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

`checker.py` uses Python 3 standard-library integer arithmetic. Execute `python3 checker.py` from the directory containing this document and the script. The program constructs canonical unordered rooted full-binary shapes, compares every exact mean/variance coefficient pair for leaf counts two through sixteen, and asserts the unique two-member collision at sixteen.

It then carries out a logically separate direct enumeration of all 65,536 surviving-subset configurations at extinction probability \(q=1/2\), confirming the probability-law gap and vanishing first two moments. A third computation uses a recursive raw-moment polynomial formulation to verify the exact third-moment gap \(-6q^{12}(1-q)^2\). All checks are deterministic and use exact integers; no sampling or floating-point tolerances are employed.

The all-probabilities agreement of the first two moments and existence at all larger leaf counts follow from the algebraic generating-function identity in `RESULT.md`. Numerical finite enumeration is not offered as a proof beyond sixteen leaves. Inputs are unlabeled, nonplane, rooted full-binary tree shapes with all edges of unit length, no added root stem, and independent equal extinction probability. Other probability or tree models are not verified. Historical priority and independent scientific assessment have not been established.
