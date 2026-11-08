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

# Reproducibility

Run `python3 verify.py` from an extracted set of the embedded files. It uses no nonstandard libraries.

The validation program directly builds every ordered zero-gap triple \((a,b,c)\) satisfying \(a+b+c=n-3\) for \(3\le n\le36\), then constructs the corresponding literal cyclic word and enumerates all palindromic windows. This verifies the symbolic case formula for 7,140 source words, including zero gaps, equal gaps, and periodic configurations. At every length \(14\le n\le36\) it compares the predicted sorted maximizing gap triples with an exhaustive search based on the gap formula; for \(14\le n\le24\), the maximizing values and triples are independently recomputed from actual sets of literal palindrome factors without using the proposed formula.

Observed output:

`VERIFY_OK words=7140 lengths=3..36 maximizers=14..36 independent_extrema=11`

The same source was executed as a standalone Python script and returned exit code zero. This finite experiment is not a proof of the general result. The infinite statement and sharp list of extremizers follow from the marker-type exhaustion and integer inequalities in `RESULT.md`. No formal proof-assistant artifact is asserted.
