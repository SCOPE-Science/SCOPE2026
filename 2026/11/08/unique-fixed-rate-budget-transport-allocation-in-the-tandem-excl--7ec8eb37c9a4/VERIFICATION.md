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

# Reproduction and limits

The `check.py` artifact is standalone with Python, SymPy and SciPy. Run `python check.py` in the directory containing it. The script confirms the density inversion and fixed-budget current identity by symbolic cancellation; verifies the polynomial derivative and every coefficient of its transformed low-density Descartes polynomial; tests strict optimality against twelve off-optimum ratios at fourteen representative densities; verifies the leading low- and high-density constants; and enumerates canonical binary-ring configurations at four finite sizes as a separate current normalization test.

The analytical proof in `RESULT.md`, not these parameter tests, establishes uniqueness for all real densities \(0<\rho<1\). The finite-ring enumeration is only a local observable normalization check for a uniform canonical Gibbs measure at \(q=1\); it does not prove uniqueness or a thermodynamic limit. The source transfer-matrix current formula is a previously published scientific premise.

Self-review: passed. Independent audit: not yet performed.
