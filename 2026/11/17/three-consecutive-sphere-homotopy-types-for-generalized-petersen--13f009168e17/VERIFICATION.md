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
Extract the three files under `verification/` into their relative paths alongside the documents. Run `python3 verification/verify_gp_m2.py` and `python3 verification/verify_gp_m2.py --reverse`; each prints one JSON line. Compare the output with `verification/forward.json` and `verification/reverse.json`, respectively. Each mode exhaustively constructs graph edges, enumerates all valid faces for all three indices, verifies incidence and gradient acyclicity, and recomputes integer Morse attaching data where an adjacent-dimensional critical pair occurs. No external libraries or network are needed.

The forward mode visits 34,704, 223,819, and 1,436,990 matching pairs. The reversed mode visits 34,705, 223,818, and 1,436,989 matching pairs. All computations use exact integer arithmetic. For the first graph the forward signed integral differential is a three-by-two unit-rank matrix; reversed modes have a single primitive attaching vector or row. These facts support integral homotopy types because the only nontrivial attaching maps in these CW models are in the first positive cell dimension and are detected by degrees. The software checks finite instances only; it does not prove a claim for other graph parameters, establish absolute novelty, or constitute independent audit.
