---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Direct coefficient integration yields T_g=DM_h with D diagonal 1/log n, and the finite Bohr lift of -g′ gives ||M_h||=C_g. Truncating N input coordinates proves s_(N+1)<=C_g/log(2N+2). Coprime prime-free fibers of a fixed finite polynomial near norm extremizer give positive-density orthogonal inputs and orthogonal images with lower norms (C_g-o(1))/log N. Min-max proves (log n)s_n→C_g; monotone inversion yields t log N_g(t)→C_g. The one-frequency exact sequence and infinite Schatten divergence agree with the coefficient law. Independent monomial and two-prime normalization checks passed. All asymptotic steps rely on proof, not finite experiments.

## originality

FAIL

FAIL: A published October 26 full RESULT.md gives the identical theorem on the identical unweighted Hardy Hilbert space for every nonconstant Dirichlet-polynomial symbol, with the same torus constant, exact monomial sequence, coprime-fiber proof and non-Schatten conclusion; November 2 full RESULT.md additionally states the same counting exponent. The assigned conclusion is a direct duplicate, not a distinct improvement.

## value

FAIL

FAIL as a new finding: The singular-value coefficient and exponential counting law are mathematically substantive but already established for exactly these objects and parameters. Recomputing the finite checker or reformulating the Bohr lift has no separate mathematical gap; the original package should be preserved as failed evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
