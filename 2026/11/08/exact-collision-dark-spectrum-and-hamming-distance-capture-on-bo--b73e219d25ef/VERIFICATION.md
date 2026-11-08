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

# Reproducibility checks and limits

The result concerns two identical noninteracting bosons moving on \(Q_d\) with uniform nonzero hopping and strictly positive on-site collision-loss rates. The proof in `RESULT.md` is all-dimensional. The accompanying finite checks replay only dimensions \(1\) through \(4\).

Run `python check_observability_exact.py` with Python 3. This uses the integer-coordinate bosonic hopping action and modular elimination of the entire detector observability matrix. The expected bright/dark dimensions in dimensions one through four are respectively \((3,0)\), \((8,2)\), \((20,16)\), and \((48,88)\). All four cases have been run successfully. Exact finite-field rank supports the specific finite instances; the proof establishes the unrestricted theorem.

Run `OPENBLAS_NUM_THREADS=1 python check_spectral_numeric.py` with Python 3, NumPy and SciPy. This independently builds the orthonormal two-boson Hamiltonian, computes collision-dark kernels across its eigenspaces, verifies projector idempotence and tests the Hamming-distance capture formula at tolerance \(10^{-8}\), for every distance in each dimension one through four. All finite tests have been run successfully. The calculation is floating-point and is not a substitute for the proof.

Neither checker evaluates an infinite system, nonzero interactions, a site with zero collision loss, nonuniform hopping or finite-time decay constants. No external independent audit or experimental validation has been performed.
