---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Deleting one selected detector (not a graph vertex) can empty a signature or erase a separator precisely when it is the sole selected member of the corresponding constraint. Thus resilience is exactly twofold covering of each of 20 closed neighborhoods and 190 indexed pairwise symmetric differences. In the cubic graph, summing the 20 covering inequalities gives 4|C|≥40. Independent exhaustive replay constructed GP(10,2) from its three edge families and enumerated 184756, 167960 and 125970 subsets at sizes 10, 11 and 12, respectively, finding 0, 0 and 15; the ascending decimal mask list agrees in full with RESULT.md lines 20–27. Every pair was checked, yielding 60 intersections of size 6 and 45 of size 8. The displayed mapping is a bijection onto the 15 two-subsets of a six-element set; checking all 105 pairs verifies intersection 8 iff disjoint, an exact KG(6,2) isomorphism. A move between size-12 codes would require intersection size 11, so both minimum reconfiguration graphs are 15 isolated vertices. Replay: python3 /workspace/branches/0263a8b2-acf5-438e-8b98-c34d62de1e25/audit_gp102.py; result in adjacent audit_gp102_output.txt. The two frozen implementations and their recorded outputs were inspected without executing the frozen programs. The bounded replay exhausts all sizes that can affect the optimum and census, with the lower sizes excluded analytically.

## originality

PASS

The standard erasure-to-twofold-cover equivalence is not the credited contribution. The exact optimum family, its intersection geometry and resulting minimum reconfiguration behavior survive the statement-level comparisons below. No distinct equivalent coverage was established in the inspected material; this is a bounded assessment, not a priority certification.

## value

PASS

The dodecahedron is a natural small cubic graph on which one can ask the complete robust detector-placement question, rather than sample arbitrary graph instances. Knowing all 15 minimum choices and the Kneser structure explains exactly how much choices can overlap and why none admits one-detector movement at optimal cardinality. This exact robust design and reconfiguration ground truth is useful independently of any general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
