---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The feature-series Fourier transform gives exactly the fixed-diagonal 2-by-2 blocks and cross moduli in RESULT.md:16–28. Positive definiteness for distinct nodes follows from the first 2n monomials. For the numerator recurrence, multiplying the preceding coefficient by (m+nk+j)/j and summing gives the displayed derivative term. The finite coefficient formula gives positive constant and leading coefficients and the recurrence bounds the degree increase by one. At each preceding simple negative root the new sign is the opposite of the old derivative's sign. The intervening intervals and the interval from the rightmost old root to 0 give d simple sign changes; if degree grows, the left tail gives the extra root. The constant case is immediate. The modulus squared increases strictly in cos(n delta), including for a constant numerator (the denominator is strictly decreasing) or a vanishing numerator at the half-step endpoint (the product is positive in the interior). Each fixed-trace block pair strictly widens, and direct sums of the pairwise doubly stochastic maps prove the full majorization. The extrema of the global largest and smallest eigenvalues are strict because every corresponding block extremum moves strictly. The fixed positive ring rescalings preserve these arguments. The uploaded finite checker and its recorded exact/approximate sample counts were inspected, not run or used in place of the proof.

## originality

FAIL

The decisive match is not just the determinant theorem in the distinct Resultary record dee70b752615. Its proof already gives the identical two-ring Fourier blocks and explicitly establishes strict per-block cross-modulus ordering for the same kernel and all integer powers p>=2 (Steps 1 and 3, especially equation (3)). The full spectral claim and strict extrema then follow mechanically from fixed-trace pairs; this works for normalized or unnormalized vectors. The remaining alpha=1 case is the same block calculation with the geometric series 1/(1-t). This is demonstrable catalogue coverage at the level of mathematical implication; it does not assert who obtained the argument first or infer priority from catalogue dates.

## value

FAIL

Exact spectral optimization of this natural design is useful in isolation. Here all the optimized quantities follow by the elementary fixed-trace two-entry argument from an already explicit same-kernel ordering of every Fourier cross modulus. Neither adding the geometric-series Hardy endpoint nor removing normalization leaves an independently valuable nonmechanical remainder. No repaired finding is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
