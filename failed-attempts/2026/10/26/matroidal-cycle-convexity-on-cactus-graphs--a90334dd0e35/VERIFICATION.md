---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The cycle–vertex incidence graph is a forest by the cactus block structure. In a nonempty set of selected cycle rows there is a cycle meeting at most one vertex shared by other selected cycles: after deleting degree-one vertex nodes, a nontrivial component has a leaf on the cycle side, and isolated cycles also work. Its at least two private vertices prevent zero and unit sums. Thus the rows have rank c, the quotient has dimension n−c, and all represented vertices are nonzero. Cycle generation is contained in span closure by the relations. For the reverse direction, suppose a cycle-closed T has an outside vertex v in its span. The selected cycle rows witnessing this have mod-2 sum on V\T supported exactly at v. Retain only these rows and the outside vertices they meet in the incidence forest. Every retained row with edges has degree at least two by closedness, and every variable node but possibly v has even positive degree. An edge-containing forest must have at least two leaves in each nontrivial component; here there can be at most one. This contradiction proves the identity. For an independent set, the intersection of all deletion spans is zero, and spans of disjoint subsets meet only at zero; looplessness converts these to the Helly and Radon conditions. For a dependent set a witness in its own deletion span defeats both conditions. The edge-free one-vertex case has dimension one, and trees have free closure. In the diamond, {0,2} generates 1 then 3, but {2,3} is closed even accounting for the four-cycle. Independent binary elimination against iterated hull checks matched at all subsets of 100 generated cacti of orders 4–10.

## originality

FAIL

A distinct earlier-indexed Resultary finding states the same quotient representation, entire closure identity, looplessness and all three maxima on every cactus of order at least three, and uses the same incidence-forest argument. The orders one and two simply have zero cycle relations and free matroid closure; they do not give a new scientific remainder. This is exact substantive coverage, independently of any claim about origin or provenance.

## value

PASS

An explicit representation of an entire graph-convexity closure as a binary matroid, explaining three independence notions simultaneously and exhibiting a sharp neighboring obstruction, carries structural mathematical value. The finding fails because that full contribution is covered, not because it only gives an isolated numerical rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
