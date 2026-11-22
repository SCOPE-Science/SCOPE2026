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

The supplied C++17 program constructs the exact transition map on all \(3^{12}=531{,}441\) configurations, strips in-degree-zero states, records complete cycles, and propagates transient depths backwards. Its output gives \(1\) fixed state, \(40{,}740\) primitive three-periodic states, \(192\) primitive four-periodic states, and sharp entry time \(10\).

The second Python/NumPy implementation reconstructs graph incidence and the successor function using a distinct vectorized route. It checks \(F^{22}=F^{10}\) throughout the entire state space, \(F^{21}\ne F^9\) for at least one state, the fixed-power populations, every entry shell and eventual period, and the orbit partition under all 48 cube symmetries. It checks 319 geometric three-cycle classes and four geometric four-cycle classes of sizes 6, 6, 12 and 24.

Execution instructions, definitions, and exact integer orbit representatives are in `RESULT.md`; the NumPy dependency is declared in `requirements.txt`. None of these checks extends the result to an infinite graph family or constitutes an independent external mathematical audit. Historical equivalence outside the inspected sources has not been excluded.
