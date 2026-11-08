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

Run `python3 verify.py` using Python 3 standard library from the directory holding this file and `verify.py`.

The verifier directly enumerates every labeled mapping of chores to the genuine agents or the housekeeper. It rejects any agent load exceeding its budget and applies the literal exact-EF integer comparison \(\min(a_i,b_j)\le a_j\) for every source bundle \(i\), including the housekeeper, and each genuine agent \(j\). It does **not** derive EF from the proposed classification when testing these assignments.

It compares the direct count with the closed multinomial sum on 1206 instances, comprising 6,066,226 labeled assignments. It separately checks the sharp uniform-capacity threshold for 182 parameter settings and the heterogeneous threshold for 19,525 ordered positive capacity vectors. Expected examples: four agents with capacity five each and eleven chores have zero exact-EF allocations; with twelve chores they have 369600.

The finite enumeration is only a consistency check. The unbounded result follows from the three lemmas in RESULT.md. No random experiments, floating-point approximations or external datasets are needed. Priority comparisons are limited by the visibility of published sources; no independent audit has been performed.
