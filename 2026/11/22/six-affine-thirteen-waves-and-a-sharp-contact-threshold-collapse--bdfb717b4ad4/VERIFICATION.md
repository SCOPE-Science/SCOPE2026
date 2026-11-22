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

# Reproduction and scientific limits

The file `verification/verify_package.py` is executable with Python 3 and a C++17 compiler. It compiles both integer-only classifiers from sources in `verification/`, reads the complete two threshold-specific adjacency specifications in `graph/`, and enumerates all \(3^{13}=1{,}594{,}323\) configurations for each threshold twice. The first classifier follows forward trajectories. The second constructs the functional graph and removes all noncyclic vertices by zero-indegree peeling. The replay compares every entry-time/period histogram cell and every individual-basin-size multiplicity between the independent implementations.

Recorded results at threshold two: primitive orbit counts \(\{1:1,3:2288,13:6\}\), maximal first-periodic-entry time \(14\), exactly \(624\) states at that depth, basin totals \(1{,}498{,}799\), \(88{,}114\), \(7410\) for periods \(1\), \(3\), \(13\) respectively, and six period-thirteen basin sizes of \(1235\). Recorded results at threshold three: only the zero fixed point, maximal extinction time \(4\), with \(101{,}062\) initial configurations at that time. Every recorded population sums to the entire state space.

The verifier independently applies the local transition to the color word `0000002221110`, tests that it translates by three positions, forms all affine images with quadratic-residue multipliers, checks that the \(78\) images are distinct, and proves directly by their transitions that they form exactly six primitive period-thirteen cycles.

The recorded standard output is `verification/verify_package.out`, and full graph-specific output tables are included for direct inspection. These are exact exhaustive finite computational checks, not a claim of external audit or a formal proof assistant certificate. Historical-priority searches cannot rule out inaccessible or unindexed calculations; neither the code nor its arithmetic proves novelty.
