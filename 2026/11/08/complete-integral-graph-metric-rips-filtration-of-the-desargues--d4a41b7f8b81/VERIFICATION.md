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

Run `python verify.py` with Python 3 (standard library only). The program enumerates the twenty incidence vertices, all shortest-path distances, every face of each threshold clique complex twice, the deterministic vertex-toggle matching and every Hasse incidence. It tests global matching acyclicity with topological sorting, not with sample cycles, and independently confirms the ten antipodal pairs at graph distance five. Expected stage counts and actual output are in `verification_output.txt`. All checks are finite and exhaustive for this explicitly defined graph. Forman’s discrete-Morse theorem supplies the homotopy implication from the verified certificate. This is reproducible computational evidence, not independent mathematical certification.
