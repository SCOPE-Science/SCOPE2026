---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Five possible temporal 3-histories (empty, persistent conductor, three H/T/C rotations) per cell give 25 column symbols. The 625 ordered two-column states and local 8-offset count with repeated opposite-row incidences define an integer transfer T and R_n=tr(T^n), n>=3. Inspected verify_transfer.py constructs T by testing 15625 triples, obtains 4090 legal arcs, one 283-vertex recurrent component with 1816 arcs, and validates det(I−zT)=a^2 b c^2 d by exact symbolic integer matrix characteristic polynomial. A separate positive integer vector certificate bounds lambda between 6.44175 and 6.44176. The other recurrent eigenvalues are strictly dominated by the Perron eigenvalue since the component has a self-loop; hence R_n~lambda^n. Exactly 4^n configurations are temporally fixed, and C_n=(R_n−4^n)/3. Independent sparse transfer traces n=3..8 reproduced 238,1840,12064,70540,453478,2975344, and all six associated 3-orbit counts. The characteristic-polynomial calculation is a finite exactly specified matrix certificate, not an extrapolation from bounded n.

## originality

PASS

Gladkikh–Nigay 2018 supplies original four-state Wireworld rule and period-three clocks, but its main work is the seven-state Wireworld++ electronic implementation rather than a two-row torus primitive orbit zeta or entropy. Published two-row Greenberg–Hastings and three-row Brian's Brain zetas apply to different automata.

## value

PASS

An all-circumference exact spatial zeta and rigorously bounded entropy for a concrete small-width nonlinear 4-state cellular automaton is a motivated reproducible invariant of its local dynamics, not an arbitrary partial state census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
