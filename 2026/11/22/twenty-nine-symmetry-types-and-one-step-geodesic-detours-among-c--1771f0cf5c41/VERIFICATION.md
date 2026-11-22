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

# Verification of the exact metric-basis classification

The two attached standalone programs use different graph constructions. The complete details of the mathematics, hypotheses and finite validity range appear in `RESULT.md`.

Run the first from the artifact directory with `c++ -O3 -std=c++17 cox_metric_a.cpp -o metric_a && ./metric_a`. It constructs 28 vertices and 42 edges of diameter four, checks that no resolving triple exists, enumerates exactly 7,728 minimum resolving quadruples, and constructs every possible one-for-one replacement. Breadth-first search from each of the 7,728 base configurations checks that every target is reached and certifies the full distance histogram: 155904, 2210880, 11718084, 15762852, 9408 unordered pairs at graph distances one through five. Its reported eccentricities have multiplicities 1680 (four) and 6048 (five); exactly 449820 unordered pairs require one more step than the Johnson lower bound. The graph has 155904 exchange edges.

Run the second with `python3 cox_metric_b.py`. It constructs the 28 triples that are not Fano-plane lines, with disjointness adjacency, checks an explicit isomorphism to the layered graph, enumerates the same 7,728 bases and 155,904 exchange edges, verifies 336 graph automorphisms and their 29 base orbits, and checks all exchange distances from orbit representatives with multiplicity. It terminates with `ALL_CHECKS_PASS` on success.

Both programs were executed successfully as supplied and their output compared. No random sampling was used for any asserted finite count. The complete automorphism-group size 336 is a known mathematical fact used as an explicitly cited premise; 336 concrete automorphisms are checked within the second program. The separate implementation does not constitute an independent scholarly audit. No assertion is made for larger graphs or other graph families.
