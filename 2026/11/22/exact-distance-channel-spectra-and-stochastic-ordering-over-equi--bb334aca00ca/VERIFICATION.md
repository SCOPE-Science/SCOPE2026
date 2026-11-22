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

Run `python3 check.py` with Python 3 and no third-party packages. It enumerates all labelled complete metric diagrams for every \(n\in\{1,\ldots,6\}\) and both equilateral old distances \(\delta\in\{2,3\}\), checks the forbidden triangles and the metric inequalities, compares each channel against its closed formula, and checks exact rational cross-products through \(n=200\). The saved result of the execution is `checks.txt`.

The independent finite enumeration does not prove all \(n\). That conclusion follows from the inclusion–exclusion and coefficient-extraction identities and the all-size analytic inequalities written in `RESULT.md`. No external or independent mathematical audit was performed.
