---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Execute `python3 check_matrix.py` using an ordinary Python 3 interpreter. The program independently constructs point–line incidence matrices for the Desarguesian planes of orders \(2,3,4,5,8\), performs exact binary Gaussian elimination, and compares the resulting wave fixed-space dimensions for times \(1,2,3,4,6,12\) with the theorem. It checks that the temporal matrix returns to the identity at the asserted global period and not at any smaller positive iterate.

Execute `python3 check_orbits.py`. It computes updates vertex by vertex from an independently constructed incidence structure and checks \(54{,}204\) reproducible states for orders \(2,3,5\) against the claimed primitive-period sets and maximal period. Expected exact text output is included in `check_matrix_output.txt` and `check_orbits_output.txt`.

These checks were executed using the files provided and passed. The computations cover finitely many Desarguesian plane instances only and do not test every plane, every extension field, or every possible state. The full general result rests on the proof in RESULT.md, including the adjacency Jordan decomposition and temporal-block argument. No independent mathematical audit or certification has taken place.
