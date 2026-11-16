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

Run `python3 check_hamilton.py` from the directory containing this file. Only the Python standard library is required. The script independently enumerates unoriented Hamiltonian cycles, computes exact Walsh transforms by butterfly summation for three through eight vertices, and checks valuation congruences and nonvanishing for the qualifying sizes. It separately verifies random coefficients via signed Held–Karp dynamic programming and computes signed-cycle sums at twelve, fourteen, fifteen, and sixteen vertices. A direct full-cycle census of the four-vertex-clique signing at nine vertices yields signed counts `1440,8640,8640,1440`, matching the independent dynamic program; the single-edge signing at five vertices gives zero as well. It verifies the binary-digit order criterion through 160 vertices.

Expected terminal marker: `BINARY_HAMILTONIAN_2ADIC_CHECKS_PASS`. Finite verifications support the closed integer proof, but do not prove infinitely many parameter cases. No external or independent audit has been performed.
