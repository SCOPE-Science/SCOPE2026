---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: The synchronous Rule 110 constraint for a T-periodic time-column triple (a,b,c) produces a finite directed de Bruijn transfer graph whose rooted spatial n-walks biject with configurations fixed by F_n^T. An independent implementation regenerated 4097 edges at T=6, recurrent SCCs with internal (size,edges) (1,1),(4,4),(9,9), and verified each nontrivial column in these cyclic components has temporal period 2 or 3, excluding primitive temporal six. At T=7 it independently regenerated 16385 edges and two cyclic SCCs (1,1),(63,84). The latter 63-vertex adjacency A yields primitive seven-cycle orbit count tr(A^n)/7 because F_n has one temporal fixed state and 7 is prime. Boolean recurrence on all 63 vertices reproduces exactly the 13 allowed lengths up to 30, while common vertex 193 has 9 and all 31..39 return lengths; concatenating the 9-return gives every n>=31, not a finite extrapolation. Integer trace sample checks n=9,11,14,17,18,20 agree with reported 9,11,2,17,9,60. Direct C++ verification for n<=20 is corroborative only.

## originality

PASS

PASS best of knowledge, with genuinely read exact-object comparators and explicitly bounded coverage risks. Only a complete G_7 recurrent classification plus an all-length return-walk argument yields the specified excluded lengths and closed walk count; prior selected glider families and height<=5 return results cannot logically force completeness.

## value

PASS

PASS: Rule 110 stationary period-seven gliders are a canonical, previously sampled aspect of a computationally universal automaton. This result settles the motivated all-ring existence and exact primitive population, not just isolated glider examples, and proves a sharp 30-site absence alongside universal six-period exclusion. The finite 63-state formula is reproducible and mathematically useful for spatially periodic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
