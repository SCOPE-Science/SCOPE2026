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

The binomial series and transpose give the stated matrix and its symmetry. For u=(1-z)^{-1}-1/2 the boundary Jacobian is |u+1/2|^{-2}; it is canceled by the squared Cayley prefactor (the unweighted measures are not literally equal). Paley–Wiener then gives the normalized Laplace unitary. The atomic map sends u to tu/(1−t)+1/[2(1−t)] and the Laplace substitution gives t^{-1} exp(−x/(2t))g((1−t)x/t), hence the asserted reciprocal log-shifts and weights. For t≠1/2 the constant-coefficient symbol is 2r cos(ξL) and covers the full norm enclosure. On the normalized long translated cutoffs, each shift discrepancy has norm at most sqrt(2|L|/N); the multiplier error vanishes uniformly there, and the supports escape, giving the required singular Weyl sequence at every spectral point. Strict pointwise attenuation of both summands excludes norm attainment. At t=1/2 the doubled atom is the non-atomic multiplication model with essential range [0,4]. Strong continuity follows from dilations and dominated convergence of the locally uniformly bounded multipliers, for both terms. Testing the norm difference on unit approximate eigenvectors at the negative edge and using A_{1/2}≥0 gives the claimed lower bound. Inspected checks/finite_sections.py and frozen VERIFICATION.md; recorded finite numerical checks were not rerun and are not needed for these analytic conclusions.

## originality

FAIL

A distinct same-day Resultary theorem supplies exactly the full signed interval as a specialization of its Fourier-essential-spectrum inclusion with the sharp norm enclosure. It also contains the unit-atom midpoint multiplier and proves nonattainment in greater generality. Release order within the day is not established. The strong limit is not stated there, but the shared elementary model makes it routine, and the norm gap is immediate from the covered spectrum and midpoint positivity.

## value

FAIL

The exact signed spectrum of a positive-entry matrix is a meaningful question, but the submitted pair's classification and nonattainment are already supplied by the indexed general result. The separately worded strong/norm discontinuity follows by basic operator continuity in that same model and the covered spectral edge, rather than a substantive independent remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
