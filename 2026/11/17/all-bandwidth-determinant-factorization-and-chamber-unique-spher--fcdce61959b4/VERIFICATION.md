---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Unitary discrete Fourier transforms on rings with 2j+1 samples create an upper triangular system ordered by absolute azimuth m. Diagonal m-block rows j>=|m| contain associated-Legendre radial values, and derivative polynomials of degrees 0,..,L-|m|-1 give ordinary Vandermonde determinants. Multiplying all signed-m blocks yields C_L times (1-x_j²)^{j(j+1)} and |x_j-x_i|^{2(2i+1)}, independent of ring offsets. Distinct interior heights make every factor nonzero. Taking log, its Hessian quadratic form is the sum of negative pole diagonal curvatures and negative pairwise squared-difference penalties; it is negative definite on each of the (L-1)! convex ordering chambers. Pole or collision boundaries force log determinant to -infinity, hence one interior nondegenerate maximizer per chamber. Independently verified C2=729/(1024*pi^4), C3=5189853515625/(1073741824*pi^9), L3 Hessian curvature, and compared analytical factorization with published nine-node L3 formula. These finite checks support but do not prove all L. No global best permutation, stability or condition number is claimed.

## originality

PASS

Earlier ring-sampling literature gives the architecture and associated-Legendre per-order systems; a published nine-node L3 case gives only one finite specialization. The all-L exact weighted Vandermonde with a factorial count of unique chamber maxima is not implied by those finite cases or conditioning heuristics; best-of-knowledge priority with residual risk from older weighted Fekete formulations.

## value

PASS

A structural all-bandwidth interpolation determinant and exactly (L-1)! unique D-optimal height placements are useful for designing minimal spherical harmonic sample grids, distinguishing volume design from condition number and making each constrained chamber optimization uniquely solvable. This is a natural infinite family, not simply re-evaluating the nine-node table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
