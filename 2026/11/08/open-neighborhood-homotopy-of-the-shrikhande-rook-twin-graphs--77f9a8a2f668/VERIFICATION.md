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

# Verification of the finite classification

Run `python3 verify_neighborhood_twins.py` with standard Python 3. Source and output are embedded alongside this file. Both graph definitions, every vertex pair's adjacency and common-neighbor count, all nonempty face masks, the complete discrete-Morse matching and its covering-incidence acyclicity, and the integer critical-two-cell attaching degrees are reconstructed. The exact degree distributions are \((-2:4,0:39,2:13)\) for the Shrikhande graph and \((-2:9,0:38,2:9)\) for the rook graph. Each has gcd \(2\), giving the claimed nonequivariant CW homotopy type.

All masks in the sixteen-vertex domain are examined. The checker also independently obtains rank \(104\) for the original simplicial second-boundary operator over \(\mathbb F_2\). Its exact integer Morse computation, rather than that finite-field rank, is the crucial integral certificate.

This verification does not establish homotopy types of other strongly regular graphs, automorphism-equivariant statements, or publication priority. No independent external audit has been performed.
