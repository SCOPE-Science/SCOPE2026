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

A sum-zero launch evolves in the left nonbridge eigenspace of eigenvalue −1/(n−1), giving the exact bright-weight factor after right projection. Reflection of the degree-normalized four-dimensional block gives diagonal entries (a, ±1/n) and off-diagonal 1/√n. The even top root is 1; the odd top root θ is in (a,1), by nonzero coupling and Perron simplicity. The lower odd root η is O(1/n) by the product of the roots and θ≥a≥1/2. The identity (1−θ)(1−η)=2/[n(n−1)] gives the positive splitting. In each parity sector the squared residual weight at e₁ is at most q=n/(n−1)². The two errors in survival amplitudes are each at most 2q and each bridge amplitude at most 2√q; the half-differences give a probability error at most 4q+4q. Compact scaled-time convergence gives the first fixed-threshold crossing by bounding the whole earlier compact interval strictly below threshold and evaluating just above the crossing before π/2. The other consequences follow from the exact ceiling and the first sine-envelope peak. Independent full-matrix diagonalization reproduced the gap and 150 packet/time comparisons including bright, localized, dark and complex launches; replay: python /workspace/branches/independent_replay.py 5.

## originality

FAIL

The transfer statements are not identically worded in the primary paper, but the same Hamiltonian's published exact eigendata mechanically imply the entire proposed bound and its corollaries. From Appendix A's eigenvectors, the bridge/nonbridge aggregate ratio of a top parity eigenvector is √n(λ−a) (λ=1 or θ). Hence the residual squared weight is at most n/(n−1)², with no new spectral analysis. Directly using the two parity survival amplitudes and the triangle inequality yields the stated constant 8; inserting the Appendix A quadratic yields the gap, and the same profile and ceiling yield the preparation, scale and first-threshold results. This is implicit coverage by stronger exact solution data, not evidence of an identically published population theorem. Use the exact equations (A7–A8), not the inconsistent large-n display (A24) in the retrieved PDF; the exact roots give θ→1 and the quadratic splitting.

## value

FAIL

Preparation-sensitive transport on a bottleneck is a meaningful question, and stating the peak and arrival profile is a useful exposition of the exact solution. As a standalone mathematical contribution here, the asserted constant, packet criterion and arrival do not require a new estimate beyond elementary spectral projection of the prior exact eigenbasis for the very same graph. The theorem does not optimize the finite-size envelope or address a new graph or measurement regime. The straightforward correction of the source's displayed asymptotics by its own exact quadratic does not establish a separate valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
