---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The residue intervals define a measure-one integer fundamental domain. Over [0,1/2) there are exactly two points in each fiber, t and t+1/2+m_j. With the unitary coefficient transform √2 times the Fourier series on that half interval, synthesis is multiplication by M_j(t)/√2. Its squared singular values are 1±|cos(πα(m_j+1/2))|. Localizing a normalized eigenvector on a positive-measure J_j and approximating with Fourier polynomials proves sharpness. For reduced odd a, a(2m+1) runs through every odd residue mod 2b, giving distance one from a multiple of 2b and the exact positive lower bound. For even a, b is odd and m=(b−1)/2 gives a singular fiber; right and left kernels localized there give an ℓ² synthesis kernel and incompleteness, including the indexed collision at even integers. For irrational α each fiber is invertible but irrational rotation makes the lower singular values arbitrarily small on positive-measure intervals. The adjoint therefore has zero kernel but is not bounded below, proving completeness and failure of the frame inequality, not merely failure of a synthesis bound. The half-angle ratio, orthonormal case and detuning asymptotic follow as stated. Replay at RESULT.md lines 28–88. Inspected CHECK.py and verification notes without running the finite tests.

## originality

FAIL

The full asserted spectral behavior is a direct specialization of established fiber formulas to the positive odd-height example of Cabrelli–Carbajal, which after scaling is already an unbounded integer fundamental domain. Changing to all signed odd heights is a genuine geometric change but leaves exactly the same extremal and singular-fiber tests for every offset, so it does not supply a distinct spectral result. This is coverage by implication, not a claim that the earlier example prints the three cases or their constants verbatim.

## value

FAIL

A complete nonframe arbitrarily close to an orthogonal spectrum is a meaningful illustration, but the known positive odd-height example and sharp fiber criterion already give this exact boundary and the same conditioning constants. Adding negative heights is not motivated by a different tested invariant, and the arithmetic evaluation is mechanical; the pedagogical example does not survive as a distinct scientific invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
