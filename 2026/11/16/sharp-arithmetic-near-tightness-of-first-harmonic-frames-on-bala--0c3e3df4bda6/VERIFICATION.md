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

Run the included standalone Python 3 standard-library program with `python verify.py`. It directly enumerates all uniform \(k\)-subset samples for \(3\le k\le7\), and all the corresponding shell samples. It forms exact rational covariance matrices on an explicit first-harmonic basis and checks that both invariant subspaces have exactly the eigenvalues asserted by the proof. This covers 30 shell cases, including the two single-node end shells and the even central noninjective shells. Separately, the program evaluates all parity-admissible offsets and exact rational condition numbers for \(3\le k\le1500\), checking the sharp lower bound and its equality family. A complete run emits `JOHNSON_SHELL_EXACT_PASS`.

The universal results are derived analytically using hypergeometric covariance, an integer lower bound, and a uniform asymptotic expansion. Computations on finitely many graph orders do not imply the universal formula, historical novelty, or independent mathematical audit.
