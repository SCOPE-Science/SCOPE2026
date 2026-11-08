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

# Verification of the finite classifier and spectral proof

Run `python3 verify.py` from the directory containing these files using standard Python 3. The script deterministically tests every \(\pm1\) truth table with one through four inputs (respectively \(4,16,256,65536\) tables), performs integer Walsh–Hadamard transforms, checks the zero-mean and Fourier-degree filters, and counts precisely the essential variables. It also constructs the signed-multiplexer and signed-cross-product classes independently and checks set equality with the full enumeration.

The resulting exact essential-variable counts are \((2,2,24,24)\) for mean-zero Fourier degree at most two and \((0,2,0,24)\) for pure level two. Separately, the code exhausts all \(65536\) spin assignments on the sixteen-vertex \(Q_4\) using Gray-code single-spin updates and checks the five energy/degeneracy pairs in `RESULT.md`. Rational coupling samples confirm the proposed minimizing levels in dimensions four through twenty. The dimension-uniform result is proved analytically by Walsh decomposition, strict spectral convexity, and the four-coordinate influence bound; finite computations certify the local base cases and do not purport to establish infinite statements by sampling.

All inputs and dependencies are contained in this package. There is no assertion of an independent audit or of external verification.
