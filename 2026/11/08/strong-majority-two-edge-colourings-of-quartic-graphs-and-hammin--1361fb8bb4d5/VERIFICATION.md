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

Every red edge uv has red-degrees r(u)+r(v)=5; blue edges have sum3, because exactly three of six neighbouring edges are red. This forces the degree-type path 0–3–2–1–4 and 5 distance layers, each vertex with i predecessors and 4−i successors. Connectedness ensures all classes; converse colours consecutive layers alternately. Layer edge double-counting gives sizes (a,4a,6a,4a,a), hence 16a vertices and bipartiteness. Independent breadth-first layer tests found 16/8 centers in Q4 and switched Q4, respectively, with 24/22 four-cycles. This is full proof, finite examples only check sharpness.

## originality

PASS

Best-of-knowledge distinct general theorem: named two-colour edge assignments on every connected 4-regular graph correspond bijectively to completely regular radius-four distance codes with the precise Q4 array. Earlier strong-majority hypercube theorem gives Q4 as a special case only; NBC literature discusses colourings of a 4-regular graph, not arbitrary line graphs of quartic graphs.

## value

PASS

Natural exact structural classification translating a local edge-colour condition into completely regular code geometry for all connected quartic graphs, with sharp divisibility, bipartiteness, and different counts on smallest nonisomorphic witnesses. Independent of the already known Q4-only special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
