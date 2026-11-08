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
# Verification

The proof in RESULT.md is an infinite argument for every integer \(k\ge2\), using an explicit trace-pairing criterion, a complete six-projector calculation over \(\mathbb F_2\), regular dyadic lifting, and a valuation-stratum count. The self-contained `check.py` separately evaluates the rank-one projector set, its ordered additive convolution, the pointwise formulas in the claimed regular sectors, all zero/nonzero target decisions, and sharp positive lower bounds for \(k=2,3,4,5\). Run it with `python3 check.py` using the package directory as the working directory. Expected marker: `DYADIC_PROJECTOR_CONVOLUTION_SUPPORT_PASS`.

The checker does not establish the all-depth statement and cannot establish historical priority. An earlier matrix-ring decomposition theorem covering the same dyadic obstruction remains a residual literature risk. Independent mathematical audit has not been performed.
