---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The gradient and rotated-gradient modes are orthogonal by integration by parts and Stokes, with squared gradient norm ℓ(ℓ+1) times the scalar norm. The two-component frame and normalizations give Hermitian m-blocks with eigenvalues proportional to a±mb. For M≥2ℓ+1 the discrete Fourier phases are orthogonal; for fewer sites there are fewer component measurements than the complex dimension. I checked the Jacobi factorization independently: Q=P_ℓ^(m) up to sign is orthogonal to lower degrees for the (m,m) Jacobi weight. Dividing U⁺ by (1+h) gives mQ−(1−h)Q′. Integration by parts against the (m−1,m+1) weight converts a test polynomial r to (m+1)r+(1+h)r′ against the (m,m) weight, orthogonal for degree <ℓ−m; the leading coefficient is multiplied by ℓ. Reflection gives the other branch. The zonal derivative and simple Jacobi roots yield ℓ²−1 listed root occurrences counting coincidences, not necessarily distinct heights. At the equator each nonzero m has either nonzero value or derivative, but not both zero by uniqueness of the associated Legendre differential equation, leaving only the even-degree zonal obstruction. In degree two the three explicit associated Legendre modes give the listed five 5q/4 levels with two copies per branch (coincident branches add multiplicities), and the three rank-eight heights. The factor comparisons on 0<t<1/2 reduce the spectrum ratio to the two given branches with opposite strict monotonicity; the cubic is strictly decreasing there. Its root exceeds 257/1000, giving (1+t)²/(6t²)<4 there, while t>1/2 gives a lower bound of 9 via q₂₊/q₂₋. The exact formulas and root are corroborated by `python3 /workspace/independent_replay.py numeric`; the analytic minimization, not this numerical calculation, proves global optimality within the equal-weight regular single-ring class.

## originality

PASS

Classical Fourier, spin-one and Wigner/Jacobi identities already underlie the rank criterion, and no originality is assigned to those identities themselves. The distinct central result is the exact quadrupolar single-ring conditioning design for simultaneous poloidal and toroidal tangent modes: the full normalized two-helicity spectrum and global sharp cubic optimum. The closest accessible statements concern spin-one multi-ring acquisition, scalar first-jet measurements or scalar quadrupole designs. Their data and optimization targets differ, and no checked statement provides or dominates the exact minimax here. This is a best-of-knowledge judgment, not historical priority certification.

## value

PASS

For two-component tangent-field acquisition the dimension threshold gives the smallest number of stations worth considering, but does not identify the unusable latitudes or quantify stability. The exact all-degree loss-of-rank condition and the sharp degree-two normalized minimax quantify a real design tradeoff for a fixed natural acquisition geometry. No optimality is claimed among irregular stations, multiple latitudes, or unknown mixed degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
