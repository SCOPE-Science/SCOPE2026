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

# Verification record

The delivered package contains `verify_icosahedral_walk.py`, which uses standard-library integer and rational calculations. Executing it evaluates all even permutations, their orders, the exact 60-by-60 allowed-edge adjacency matrix, the degree and symmetry, the matrix polynomial \((A-44I)(A-4I)(A+I)(A+4I)=0\), and four exact traces. These yield the eigenvalue-multiplicity pairs \((44,1),(4,18),(-1,16),(-4,25)\), in accordance with the character-table proof. It additionally checks a rational balance identity and a sampled rational inequality, which is **not** used as a universal numerical proof.

The global optimization is proved analytically by convex norm-preserving symmetry averaging followed by a four-irrep minimax inequality. No external certification or independent audit has been performed. The code does not test all possible doubly stochastic matrices, nor is any such enumeration needed for the analytical reduction.
