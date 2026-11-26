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

Reassessed the revised RESULT.md in /workspace/repairs/4. An adjacent swap composes an involution with a transposition, so it preserves involutivity iff the two factors commute, i.e. iff the two sites are fixed or paired to each other. Thus long pairs are invariant and each residual run supplies precisely the matching toggle graph of a path. Delete non-target edges before adding missing ones to attain the Hamming lower bound; complementary alternating matchings realize the stated diameter. To compare sizes the repair joins runs, not inserts separators: a bridge edge by itself supplies a strictly new matching, so equality with a full path requires a single run. Two or more long pairs leave at most n−4 vertices and have strictly fewer than F_(n−1) states, including n=4; the only single nonconsecutive pair whose deletion leaves a single run is {1,n}. The n=1,2 and empty residual cases are covered. Inclusion–exclusion on disjoint adjacent pairs gives C_n, and a swap index plus an arbitrary involution on the other n−2 sites specifies one edge. Independently enumerated every permutation through n=8, filtered involutions, built literal neighbor edges, and checked all components, diameters, pair distances, unique extrema and exact totals: python3 /workspace/evidence/4-permutations.py. Read supplied check_invol.py and VERIFICATION.md without executing them; the original script only checks the largest two size values, not uniqueness. The contextual limit also holds: R_m=1+(m−1)/R_(m−1) gives sqrt(m)≤R_m≤sqrt(m)+1, and the overlap scaling for r constrained local pairs in c<r runs is O(n^((c−r)/2)). Consequently the degree and short-pair factorial moments yield Poisson(2) and Poisson(1) respectively; the exact identities for zero counts then give the three limiting proportions/mean. This limit is not a claim of novelty in the repair.

## originality

PASS

Only the repaired geometry and exact graph enumeration pass. The frozen claim treated the degree limit as part of the original contribution, but the separate deletion-diversity record's joint motif theorem mechanically gives that limit, the isolated fraction, and (using the component-to-short-pair identity) the component ratio. The revision removes these from the Finding and credits them as contextual consequences with no same-day priority inference. The long-pair sectors, residual-run geometry, extrema and exact totals are not furnished by that motif theorem or by the other inspected comparators.

## value

PASS

The repaired theorem answers reachability, distance and extremal component size in a natural involution-restricted editing graph. It gives an explicit invariant identifying every component and sharp labelled extremizers, plus total graph sizes; value does not depend on claiming independent originality for the Poisson statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
