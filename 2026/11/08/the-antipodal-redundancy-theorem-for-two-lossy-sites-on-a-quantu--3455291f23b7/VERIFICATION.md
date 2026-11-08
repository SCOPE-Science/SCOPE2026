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

# Reproducibility and scientific verification

The claim concerns continuous-time single-excitation dynamics on the labeled \(n\)-cube for every integer \(n\ge2\), nonzero uniform hopping, arbitrary scalar onsite energy, and any two distinct strictly positive absorber rates. The limiting trapped fraction follows from the orthogonal projector onto the adjacency-invariant span of both trap states. The analytic proof (RESULT.md) proves all dimensions; finite computation is corroborative only.

From a directory containing both embedded Python programs and NumPy/SciPy, run:

```bash
python verify_two_traps.py
python verify_dissipation.py
```

The first program constructs spectral projectors from Krawtchouk kernels and independently constructs Krylov projectors from repeated applications of the graph adjacency matrix. It compares ranks, trace, idempotence, mixed-state capture, and all site-resolved capture values for \(n=2,3,4,5,6\) and every representative Hamming trap distance (640 site values).

The second program derives the adjacency spectral decomposition numerically without Krawtchouk formulas; it checks the nondecaying eigenvalue count of the actual non-Hermitian evolution with unequal rates \(0.7\) and \(2.1\), and compares its long-time survival norm with the bright-projector prediction at \(n=2,3,4\) across all trap separations (nine Hamiltonians). The test inputs and tolerances are specified in the code.

Observed output on the final embedded code:

```text
PASS n=2..6, all representative Hamming separations, 640 site checks; spectral vs independent Krylov.
PASS 9 unequal-loss Hamiltonians, exact nondecaying eigenspace counts and long-time survival projections.
```

Finite tests do not certify the infinite family, make historical priority conclusive, or address time-dependent, noisy, dephased or interacting models. Scientific audit by an independent party has not been performed.
