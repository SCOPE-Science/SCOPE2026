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

# Mathematical verification and limits

Run `python3 verify.py` with Python 3 (standard library only). The complete expected output is in `CHECK_OUTPUT.txt`. The script contains its own graph construction, finite-state transition, exact balanced-sign enumeration, an independent integer polynomial-annihilator plus power-trace test, a direct recurrence check on the constructed four-waves, and exact binomial congruence tests.

Verified executable facts include the following: \(KG(7,3)\) is connected, quartic and triangle-free with an explicit seven-cycle; its exact characteristic polynomial, certified by an annihilating polynomial and trace multiplicities, is \((\lambda-4)(\lambda+3)^6(\lambda-2)^{14}(\lambda+1)^{14}\). On each of \(Q_4\) and \(K_{4,4}\), there are 36 binary adjacency-nullvectors, producing 72 distinct periodic configurations and 18 primitive four-cycle orbits. All 243 ternary initial configurations on \(K_5\) become resting. The Lucas congruence was checked at \(a=0,1,\ldots,6\).

These finite checks do not establish the infinite family or the general classification. The proof in `RESULT.md`, especially the saturation identity, Fourier restriction, three-unit-root cancellation, signed-kernel correspondence and incidence-filtration integrality argument, supplies the general reasoning. Full enumeration of states on \(KG(7,3)\) is infeasible here and was neither attempted nor claimed. No external independent audit has been performed.
