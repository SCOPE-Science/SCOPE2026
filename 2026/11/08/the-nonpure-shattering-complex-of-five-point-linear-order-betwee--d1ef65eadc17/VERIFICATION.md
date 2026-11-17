---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 30 unordered-endpoint/middle queries on five labels have exactly 60 distinct response rows, since each of 120 linear orders identifies with its reversal. Independently enumerated every k-subset of query coordinates for k<=5 (including all 142506 five-subsets) and compared all 2^k traces; obtained face vector (1,30,405,2700,510,0). Downward closure excludes all larger supports. Independently tested immediate extensions, identifying 1530 maximal triples and 510 maximal quadruples, and the S5 action partitions those into 18 and 7 orbits. Direct pair counting gives C(30,2)-10 C(3,2)=405; witness gives VC>=4. These exhaustive finite calculations prove this specified finite-instance result, not a theorem for arbitrary n.

## originality

PASS

The exact finite Boolean-query face polynomial, nonpure maximal-face sizes and complete S5 orbit census survive comparison with structural betweenness axioms, adaptive betweenness dimensions and distinct permutation-order VC notions; originality is historical best-of-knowledge, not proof of absence.

## value

PASS

Ternary betweenness is a standard natural query concept class. The exact small-order shattering complex provides a sharp VC cutoff, a genuinely nonpure facet structure and 25 symmetry types; the polynomial is not a trivial renaming of general Sauer bounds. This is a motivated complete finite classification rather than an arbitrary slice or a claim of general-n theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
