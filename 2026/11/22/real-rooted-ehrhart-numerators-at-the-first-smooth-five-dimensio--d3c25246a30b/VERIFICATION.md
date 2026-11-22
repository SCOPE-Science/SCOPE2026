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

# Reproducible symbolic verification

Place `verify.py` beside `certificate.json` and run `python3 verify.py` with Python 3 and SymPy installed. The program recomputes the quartic discriminant of the exact Ehrhart numerator as a symbolic polynomial, checks its full degree-nineteen shifted coefficient certificate, and checks the explicit negative evaluation test at \(u=-1/(c+1)\). It verifies the two exceptional cubic discriminants and the degree-one boundary. For each of nine integer twists, it directly counts 7 height-sliced lattice sets, recovers all six possible numerator coefficients, and independently reconstructs the Ehrhart counts from the numerator. It checks the exact linear Ehrhart-coefficient formula and the integer threshold evaluations.

A successful execution prints `PASS`. This verification was run successfully from the packaged mathematical files. It proves the exact symbolic identities because they hold in polynomial rings over the rationals; the finite lattice samples alone are not used to infer an all-parameter claim. The positivity/sign reasoning in `RESULT.md`, rather than a numerical root-finding experiment, completes the theorem.

No independent audit is claimed or implied.
