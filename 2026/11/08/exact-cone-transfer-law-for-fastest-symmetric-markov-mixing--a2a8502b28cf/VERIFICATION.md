---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

I checked the symmetric uniform-stationary SLEM objective ||Q−J_m||_2. For noncomplete H a missing off-diagonal Q_ij forces |(Q−J)ij|=1/m; the centered basis vectors yield rho(H)>=1/(m−1). An explicit hub-edge weight 1/m and outer block (m−1)Q/m has radial eigenvalue −1/m and other eigenvalues (m−1)/m times nontrivial Q eigenvalues, proving universal <=; complete H is handled by J. For vertex-transitive H, average any feasible cone matrix over Aut(H): all hub edges equal b<=1/m; the zero-sum outer block is (1−b)Q_b, yielding rho(P)>= (1−b)rho(Q_b)>= (m−1)rho(H)/m. Disconnected H retains rho(H)=1. The four-path lower bound rho(P4)=sqrt2/2 follows from reflection modes; I independently exactly recomputed the stated five-state witness characteristic polynomial x(40x²−2x−7)(200x²−10x−33)/8000, with SLEM (1+sqrt281)/40≈0.444076<3sqrt2/8. The proof, not graph samples, covers every finite graph.

## originality

PASS

Best-of-knowledge originality assessed after primary-source and published-record comparison, including same-object aliases and broader implications. Distinct surviving contribution is specified by the detailed checks. No claim of exhaustive priority certification.

## value

PASS

The exact cone transfer reduces the global symmetric fastest-mixing optimization on every vertex-transitive graph to its base optimum regardless of the number of edge orbits, and the nontransitive P4 witness shows a substantive boundary. This is a motivated structural reduction for a universal graph construction, extending the known wheel case beyond edge-transitive cycles; not a fixed small graph calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
