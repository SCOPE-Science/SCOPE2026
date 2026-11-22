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

## Exact proof checks

The full argument is given in `RESULT.md`, Sections Proof 1–4. Exact calculations requiring care are: the Bloch generator from the stated Lindbladian, diagonalization of its \((y,z)\) block, regular Kummer solution of the history-averaged scalar equation, right-half-plane asymptotic coefficient and the single affine factor in the difference of the two decay powers. All are explicitly displayed with their hypotheses and boundaries.

## Reproducible computations

Run `python check.py` with Python, SymPy, NumPy, SciPy and mpmath. It carries out exact symbolic checks, integrates the real six-dimensional original history equation independently, checks 36 parameter/time combinations (108 real component comparisons) against the Kummer spectral solution, and verifies the rate-sign classification on 24 further parameter choices. At execution, it printed a PASS result and raised no errors.

The numerical integration uses the nonsingular initial Taylor expansion near time zero and checks solution convergence to the spectral formula within the documented tolerance. It is supplementary evidence only, not a proof for all positive parameters.

## Boundaries and remaining verification

The result requires \(\omega>\kappa>0\), \(q>0\), and nonzero initial projections onto both spectral sectors for an observable dominance switch. It includes \(\omega=\sqrt2\,\kappa\), which has no positive critical reset rate. It does not include \(q=0\) or \(\omega\le\kappa\). The infinite-time result follows analytically from Kummer asymptotics. No independent scientific audit or physical experimental replication has been performed.
