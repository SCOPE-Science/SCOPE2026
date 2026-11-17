---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

On the precisely specified 16-vertex 5-regular folded cube with XOR generators {1,2,4,8,15}, the synchronous three-colour threshold-one update is a finite total function on 3^16=43,046,721 states. Independent C++ complete functional-digraph enumeration reproduced 2,976,617 periodic states, cycle periods {1,3,4,7,10,13,16}, primitive-cycle counts (1,859552,970,11040,15360,9600,2400), 48 nonempty entry-period classes, maximum entry time 11 and exactly 11,520 maximally delayed states. Source clebsch_census.c/clebsch_walk.c independently implement indegree peeling vs forward memoization; the exact group proof uses all 16 translations and the 120 permutations of the five dependent generators, giving 1920 automorphisms. Inspected clebsch_symmetry.py verifies orbits on 9600 period-13 and 2400 period-16 canonical cycle representatives: five orbits of size 1920, and two orbits of 480 and 1920. The independent C++ census verifies class counts; source code and exact reported representative table support the equivariant component, not a separately repeated full orbit computation. Only the stated graph and update rule are covered.

## originality

PASS

Best-of-knowledge new full entry-time/period and automorphism-orbit census for 3-state excitation on the Clebsch folded cube; general excitation theorems do not calculate this discrete enumeration.

## value

PASS

The 16-vertex Clebsch/folded-cube graph is a canonical symmetric finite test object for excitable media; a complete 43-million-state census, sharp transient cutoff and full automorphism classification of the anomalously long 13- and 16-cycles give reusable nontrivial dynamical and equivariant invariants. An exact motivated finite classification is valuable without claiming a universal folded-cube theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
