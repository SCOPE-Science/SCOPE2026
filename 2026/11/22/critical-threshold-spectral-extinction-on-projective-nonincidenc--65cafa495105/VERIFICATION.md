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

For a periodic trajectory on a 2θ-regular graph, disjointness of E_{t-1} and E_{t+1} bounds contacts to the latter by θ per vertex in E_t; each new excitation needs at least θ preceding contacts. Thus the excited-set size is nonincreasing and periodic, forcing equality. Each excited vertex saturates its degree on the previous and next excited sets; their vertices each have exactly θ contacts back to E_t, with zero contacts from all other vertices. This proves the pointwise time identity on the full vertex set. For B the nonincidence matrix, two distinct points exclude the union of their two incidence pencils of size 2q+1, leaving q(q-1) shared neighbors. The Gram matrix gives eigenvalues q^4 and q, then the bipartite adjacency eigenvalues ±q² and ±sqrt(q), without a coordinate or Desarguesian hypothesis. The squared nonprincipal spectral ratio is 4/q³, a rational noninteger for even q≥2, whereas the square of a temporal root-of-unity sum is an algebraic integer. The surviving Fourier modes are ±1, giving two-step repetition excluded by the refractory rule unless all excited sets are empty. Periodicity then excludes refractory vertices too; finiteness gives eventual rest without asserting a uniform all-order time. Independently enumerated all 4782969 labelled Fano states using an OR subset transform for threshold-two neighbor pairs, ternary ranking of disjoint excited and refractory sets, and exact backward first-hitting layers from zero. This reproduced (1,16383,803001,2393358,1107890,364518,90258,7560), with no uncaptured states, and all eight words for the sharp witness 82105. Replay: python3 /workspace/branches/replay_3_5/scope_frozen_12345_fano.py, stdout in the matching .log. Inspected the archived sources and outputs without executing them. The finite computation certifies only the specified order-two census.

## originality

PASS

Qualified for the all-even-order plane specialization beyond integral spectra and the exact Fano nonincidence census. The temporal contact identity and Fourier obstruction are shared with distinct same-date records; the integral spectral criterion in 3ebebc11989a implies the square-order subfamily. No distinct checked result gives both the extension to nonsquare even orders and the census. Relative priority within the date and historical priority generally are not established.

## value

PASS

Projective nonincidence gives a natural regular test family at the exact threshold where strict contraction cannot decide extinction. Its irrational nonprincipal spectrum provides a concrete use of algebraic integrality in excluding every temporal period, in contrast to a same-degree oscillating network. The independently computed Fano distribution is a sharp benchmark for relaxation at criticality rather than an extrapolation to larger planes or a substitute for the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
