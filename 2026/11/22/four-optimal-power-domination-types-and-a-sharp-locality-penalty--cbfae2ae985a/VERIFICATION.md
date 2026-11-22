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

# Reproducibility and checked boundaries

Execute `python3 verify_bitmask.py` and `python3 verify_incidence.py` with Python 3. Both use only the standard library, require no external data, and terminate after exhaustive finite enumeration. Both were executed from their final contents and completed with no assertion failures.

The first implementation constructs all twenty integer-labelled vertices, enumerates all \(\binom{20}{k}\) subsets for \(0\le k\le4\), partitions them under explicit graph automorphism generators, and constructs both full optimum-preserving replacement graphs. It performs breadth-first search from every configuration and checks complete distance histograms, center sets and the pairwise locality-penalty histogram.

The second implementation constructs the underlying incidence graph with named tuple vertices and Python sets, independently iterates the power-domination forcing rule, constructs the four disjoint proposed families using K5 patterns and twin choices, compares their union with independently enumerated successful four-sets, and generates both reconfiguration graphs by all-pairs set comparisons. It independently computes all shortest paths and the exact penalty classes.

The critical total is \(560\) minimum sets of size \(4\), with no successful smaller set. The two reconfiguration graphs have \(4680\) and \(1920\) edges and are both connected. Radii/diameters are \((4,4)\) and \((7,8)\), with \(80\) slide-center configurations, maximum locality penalty \(4\), and \(1320\) pairs attaining that penalty. Assertions in both programs match all these values, the distance distributions and all four placement-type counts.

The conclusion is a finite exact classification; the programs make no claim to verify any broader family of graphs or to establish historical novelty by computation. External independent mathematical audit has not been performed.
