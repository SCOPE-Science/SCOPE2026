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

Independent code enumerated all permutations through length six, filtered by the defining 132 test, and constructed each shadow by positional deletion and rank standardization as a set. The empty output at n=1 is included. Codes are cliques in the disjoint-shadow graph. Exhaustive inclusion branches, with removal of each previously branched vertex, cover all cliques; a proper coloring bounds the number of further clique vertices and justifies pruning. The independent search returned M=(1,1,2,3,6,13) and checked the displayed 13-word code. At lengths 1–5 the supplied integral output covers hit every shadow and have sizes matching the code sizes. At length 6 all exact nonnegativity, primal capacity and dual covering checks pass with common denominator 308 and primal and dual numerators 4434. Weak duality gives P=(1,1,2,3,6,2217/154), so length 6 is the first gap in optimal values and the first strict floor gap, 13<14. This is not a claim that the earlier packing polytopes are integral. Replay: run python3 /workspace/branches/f34594ec-4a49-4274-b3f9-40cf067acff0/reproduce_independent.py /workspace/source/2026/11/22/the-first-fractional-single-deletion-packing-gap-for-132-avoidin--1f96402b4ab9/LP_CERTIFICATE.json. The uploaded Python was inspected, not run.

## originality

PASS

Best-of-knowledge pass for the exact finite optimum profile and the strict first rounding gap in this avoidance class. The channel, compatibility-graph reduction and sphere-size information are not credited as new. A distinct same-channel indexed result was compared by its statement, not dismissed by date.

## value

PASS

The standard fractional incidence bound is an independently motivated computational substitute for exact packing in a hereditary permutation class. The first strict slack after rounding demonstrates a real limitation of that substitute: it leaves open size 14 even though size 13 is the exact maximum. Exhaustion of all preceding lengths certifies that this is the smallest counterexample in the class rather than an arbitrary test instance. The complete profile also distinguishes two natural Catalan deletion channels despite equal source counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
