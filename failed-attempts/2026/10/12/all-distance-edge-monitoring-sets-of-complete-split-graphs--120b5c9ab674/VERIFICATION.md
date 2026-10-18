---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For K_m joined to an independent n-set, m=1 is a star so every nonempty set monitors all bridge edges. For m≥2 each clique vertex is universal, so only its incident edges can be forced in a shortest-path test. Independent vertices have m≥2 alternative predecessors at distance two, so also monitor only incident edges. Thus monitoring sets equal vertex covers; their independent complements are precisely subsets of I or one clique vertex, and the stated enumerators and boundary minima follow. Independently recomputed distances under each edge deletion for (m,n)=(1,2),(2,1),(2,2),(3,3) and enumerated every selected vertex subset; counts agree with coefficients. General m,n result is proof, not finite extrapolation.

## originality

FAIL

The same complete split graphs were analyzed in the 2025 Milivojević Danas–Kratica primary proceedings. Its Theorem 3 proof, Step 2, explicitly proves any edge whose two endpoints are omitted cannot be distance-monitored, by exactly the nonincident-edge/alternate-clique-path argument. Although presented to show a lower bound on minimum cardinality, that proof has no dependence on the overall size of the chosen set once the missing endpoints are fixed, so it already implies every monitoring set is a vertex cover. Foucaud et al. proves all vertex covers are monitoring sets. Their conjunction gives exactly the new claimed all-set characterization; the generating polynomial is immediate elementary count of independent complements. This is a decisive prior implication, not a claim that the old scalar minimum alone implies the new result.

## value

FAIL

Classifying feasible sensor placements and their size distribution is a worthwhile question in general, but for this family the old source already supplies the nonincident-edge obstruction, the foundational theorem supplies the converse, and the polynomial is the routine complement count of independent sets of a complete split graph. No non-implied structural classification, new cutoff, or substantive invariant remains after the prior proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
