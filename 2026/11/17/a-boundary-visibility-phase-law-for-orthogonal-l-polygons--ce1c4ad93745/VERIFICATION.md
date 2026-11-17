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

# Checks and limits

The exact proof partitions the six-edge boundary into three visibility groups, establishes \(ad>bc\) as the necessary and sufficient obstruction condition for opposite groups, and evaluates all four nontrivial edge-pair integrals. The analytic continuation comparison yields the derivative jump along the balance hypersurface. In the square-notch specialization, the difference of the two analytic continuations is \(128h^4/3+O(h^6)\), giving the visibility fourth-derivative jump \(-128\).

Run `python3 checker.py` from the same directory. It uses no third-party dependencies and a fixed pseudorandom seed. It samples both boundary endpoints on all six edges and tests the line's horizontal and vertical crossing times separately from the closed formula. The six tested parameter quadruples are \((1,1,1,1)\), \((0.1,0.9,0.3,0.2)\), \((1,2,3,4)\), \((4,2,3,0.1)\), \((0.7,0.4,0.8,0.3)\), and \((0.9,1.1,1.2,1.3)\). With 130,000 random boundary-pairs each, every empirical obstruction probability was within 1.7 estimated standard deviations of the exact formula. The finite-difference quotient of the two analytic extensions divided by \(h^4\) approached \(128/3\) as predicted. The diagnostic concluded `BOUNDARY_L_VISIBILITY_CUSP_CHECK_OK`.

These finite tests do not prove the exact integrals, differentiability or historical novelty; the proof establishes the first two, and historical priority remains provisional. No independent mathematical audit was performed.
