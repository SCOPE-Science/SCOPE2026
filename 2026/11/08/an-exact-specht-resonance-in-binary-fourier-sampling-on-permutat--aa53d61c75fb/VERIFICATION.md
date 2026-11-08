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

The standalone `verify_permutation_fourier.py` requires Python 3 with standard-library modules only. Run `python3 verify_permutation_fourier.py` and expect the final marker `PERMUTATION_BINARY_FOURIER_RESONANCE_PASS`.

The program enumerates integer partitions and all one-box Young branching paths to compute the exact coefficient polynomial for each representation, independently of the dual Jacobi--Trudi proof. Every coefficient is checked for the shape \((3,2,2,1^{n-7})\) for every integer \(7\le n\le20\). It exhaustively enumerates the full representation spectra and associated ranks at \(n=4,5,7\), and constructs actual binary permutation Fourier matrices for \(n=2,3,4,5\) to check their ranks by exact modular arithmetic.

The finite calculations do not constitute a proof of the symbolic identity for all dimensions; that is supplied by the generating function for the specialized elementary symmetric functions and the three-by-three determinant in `RESULT.md`. Exact modular ranks are sound lower bounds over characteristic zero; they agree with independently exact character-sector ranks in these small cases. The \(n=7\) character-sector check is exhaustive because the partition generator produces all fifteen partitions and the degree-squared sum equals \(7!\).

There is no external independence claim.
