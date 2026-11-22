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

Assuming a d-dimensional SIC exists, its d² projectors have Gram (d I+11^T)/(d+1), are a real Hermitian basis, and the trace-dual D_j=((d+1)P_j-I)/d is exact. Erasing r,s leaves a real two-dimensional Hermitian kernel. For normalized rank-one projectors, trace-zero restricts the difference to c(P_r-P_s); this rank-two operator has range W=span(u_r,u_s) and spectral values ±sqrt(d/(d+1)), forcing both ambiguous states into CP(W). In an eigenbasis, equality of the off-diagonal projector entry yields exactly one reflected partner (conjugate swap), except at equator where they coincide, so every fiber outside the exceptional line is singleton and off-equator is doubleton. Gap =delta/sqrt(d(d+1)) and chordal distance=|delta| follow algebraically. For unknown norm d>=5, a nonzero trace combination is already rank >=3 on Wperp; at d=4 rank2 on Wperp forces the independent rank-one projector terms to vanish on W (impossible unless zero), so equal norms. The qutrit D_r+D_s eigenvalues 4/3,0,-2/3 provide explicit unequal-norm pair. Independent Hesse SIC numerical Gram/collision corroborates d3 boundary but does not stand in for all-d proof.

## originality

PASS

Best-of-knowledge: the original SIC projector frame/dual is standard, but the exact two-outcome-erasure projective involution, singleton/doubleton fiber classification, gap-to-chordal constant and unknown-norm d>=4 cutoff were not implied by the highly relevant primary pure-state tomography construction theorem read in full HTML. Potential older equivalent phase-retrieval formulation remains a bounded priority risk.

## value

PASS

Pure-state informational completeness under deleted SIC measurement outcomes is a motivated exact identifiability problem. The theorem classifies all ambiguous states, their precise doubleton fibers and invisible distance factor; it also identifies an exact dimension-three versus dimension-four change when signal norm is unknown. These are natural structural facts beyond a bare linear kernel dimension count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
