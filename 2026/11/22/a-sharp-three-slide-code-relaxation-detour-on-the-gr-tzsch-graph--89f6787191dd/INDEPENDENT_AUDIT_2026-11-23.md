# Independent mathematical audit

## correctness

PASS

Reconstructed the Mycielskian of C₅ with the five cycle, ten crossed clone, and five apex edges. LT requires open domination at every vertex and distinct open traces outside the set; IC instead uses nonempty distinct closed traces at every vertex. Enumeration by increasing size through five exhausts all 1024 candidates of size at most five. At the optimum a move exchanges exactly one removed and one inserted vertex, with an original edge required for slides. The independent Python reconstruction at /workspace/branches/31a8166b-9b0c-4ea7-b27e-3d0bef17ecd4/audit_mu_c5.py (recorded audit.log in the same directory) found minima five, sizes 110 and 191, inclusion of LT in IC, slide edge counts 190 and 555, connectivity, and all 5995 distance savings (4135,1440,360,60). Both frozen verifiers were inspected without execution. Their complementing exhaustive loops cover the ancillary jump metrics, full eccentricities, dihedral orbits and path checks: the mask verifier generates each single move directly and BFS gives the exact shortest distance; the tuple verifier builds all feasible exchange pairs, checks both histograms and enumerates maps i↦a±i. In the explicit witness the LT slides exchange u₀→v₄→v₃, v₀→u₄, u₄→w→u₀. The shorter path exchanges v₀→u₄→v₃; u₄ is open-undominated in its middle state. The tuple certificate checks legality and BFS establishes distances 5 and 2. Replays for the submitted jump, metric and orbit certificates are in VERIFICATION.md. This is an exact finite result on the specified graph, not a bound for other Mycielski graphs.

## originality

PASS

The strongest examined same-graph literature gives upper bounds on the optimum sizes, not the state families, their inclusion, or a cross-predicate metric comparison. The exact finite detour and histogram were not found in an independently matching record. No priority beyond the checked evidence is inferred.

## value

PASS

The Grötzsch graph is a canonical small Mycielski example, and the fixed-cardinality distance test isolates the cost of retaining the stronger feasibility requirement during moves. The comparison gives useful information unavailable from either optimum cardinality: some endpoint pairs cross a genuine three-slide barrier, with 60 extremal pairs and only one slide of potential saving if jumps are permitted. The exact census therefore measures a specific structural difference rather than recomputing a standalone domination number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
