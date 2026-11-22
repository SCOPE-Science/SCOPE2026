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

# Verification of the two-boundary survival-time operator

The file `verify.py` checks the four asserted integer-index identities for every ordered site pair and for every path length from 2 through 100. It prints `EXACT_IDENTITIES_PASSED 338349` when all entries agree. Because this is a finite check, it is supporting evidence only: the arbitrary-length conclusion follows from the Green-kernel argument, the boundary first-difference identities and uniqueness of the stable Lyapunov solution in `RESULT.md`.

When NumPy and SciPy are installed, the same standalone program independently solves the full complex Sylvester/Lyapunov equation on seven distinct path lengths and three pairs of positive hopping and end-loss rates. It prints `INDEPENDENT_LYAPUNOV_CASES 21`; the maximum entrywise and equation-residual tolerances are \(2\times10^{-9}\). This numerical check is intentionally separate from the symbolic verification and not claimed as a proof for infinitely many lengths.

Reproduce with `python3 verify.py`. Only Python's standard library is required for the exact integer checks; NumPy and SciPy are optional for the independent numerical comparison.

The physical model assumes one walker, equal positive loss rates at *both* endpoints, uniform real nearest-neighbor coherent hopping, no bulk loss, and Lindblad first absorption. The results concern the integrated survival operator and total mean time to either absorber, not the probability of which absorber clicks first, full first-passage distributions, or unequal-rate control. Independent external audit has not been performed.
