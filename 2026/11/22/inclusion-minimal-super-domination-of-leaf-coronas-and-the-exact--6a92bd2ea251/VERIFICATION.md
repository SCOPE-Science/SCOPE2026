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

# Reproducibility checks

Run `python3 verify_corona_minimal.py` with a standard Python 3 installation; no third-party packages, external data, or network are necessary. `verification_output.txt` records the executed checks.

The checker constructs every corona directly from a base-graph edge list. It tests each omitted vertex against witnesses by intersecting literal neighbourhood masks with the omitted set. It then tests maximality by attempting each possible single-vertex addition to the omitted set. Independently, it evaluates the proved three-class combinatorial criterion and compares the results.

All labelled base graphs up to order four were checked (75 instances), as were seeded additional base graphs of orders five and six. Every vertex subset was checked for cyclic coronas of orders three through eight. At orders nine through thirteen the checker examined every three-state profile but did not examine subsets omitting both a core and its private leaf; those subsets are excluded by the elementary proof. Formula coefficients and positive spectrum support were also checked over 147 cycle orders.

These finite checks are not proofs of the universal statement. The noncomputational proof in `RESULT.md` establishes both the all-base classification and the unbounded all-order cycle formula. No third-party independent audit is claimed.
