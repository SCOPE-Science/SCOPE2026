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

# Verification evidence and scope

The complete source code in `verify_bipartite_activity.py` constructs the microscopic two-occupied-vertex configuration graph, solves the finite stationary Poisson equation over rational numbers and compares the mean and Fano ratios against the theorem for every unordered shore partition at total sizes four through nine (18 cases). The same program checks the predicted strict optimizer order at total sizes four through eighty-nine. It prints exact rates and Fano fractions for nine specified examples. It passed in the delivered version.

`verify_bipartite_symbolic.py` independently forms the stationary three-class generator, solves its symbolic Poisson equation, differentiates the second cumulant relation and simplifies the difference from the claimed formula identically to zero. It passed with SymPy installed. The result's generality follows from the analytic argument and rational identity, not the finite range of empirical tests.

No external independent scientific audit, exhaustive literature priority certification or higher-cumulant check is claimed. Both scripts implement only checks described above.
