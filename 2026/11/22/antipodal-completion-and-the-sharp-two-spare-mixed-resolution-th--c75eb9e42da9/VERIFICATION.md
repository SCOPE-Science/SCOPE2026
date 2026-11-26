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

The witnesses compare all 42 vertices and edges, with each edge response the smaller of its endpoint distances; hitting all 861 pair masks is equivalent to mixed resolution. Reviewed both frozen checkers without executing them. An independent replay (python3 /workspace/branches/fcf5a2af-46e4-4967-9339-4f9bce4c6787/check_icosahedral_mixed.py) enumerated all 4,096 subsets, reproducing the histogram (20,240,405,220,66,12,1) for sizes 6–12, equality of the size-six family with the 20 unions of three axes, minimal counts 20 and 120, and toggle component orders at budgets 6,7,8. Checking single deletions suffices for inclusion-minimality by monotonicity. At budget seven each of the 20 optima has six supersets of size seven and shares none with any other optimum, leaving 120 isolates; at budget eight a Johnson-graph exchange is realized by two adds then two deletes, and the independent traverse connects all 665 states. The same replay found precisely 160 ordinary orientated three-axis resolving triples; two landmarks cannot resolve since outside their axes at least eight vertices have only the four signatures in {1,2}². The induced-shape/complement clause was checked separately: pairs of axes induce a matching. Orient one axis at a pole and choose the neighbor of that pole on each remaining axis. These five representatives form a pentagon; between any two of those axes the matching preserves the chosen orientation exactly for consecutive members of the pentagon. Among triples containing the pole's axis, five have a positive matching-sign product (two triangles), and five have a negative product (a six-cycle). Their complementary triples in the pentagon have respectively two and one positive edges, so the product and shape switch. Thus there are ten of each. Here complementation means vertex-set complement (the three other axes), as defined in the proof, not applying the antipodal map to a set.

## originality

PASS

The ordinary three-axis resolving bases and their slide reconfiguration are credited to the same-graph comparison. The inspected results do not give mixed resolving on 42 elements, the antipodal completion equality, its full polynomial or the sharp mixed add/delete budget.

## value

PASS

The icosahedron is a canonical small test of the difference between ordinary and mixed landmark resolution. The all-minima antipodal rule, exact subset and minimality polynomials, and a sharp augmentation budget are linked by the geometry and monotone feasible family. In particular the many seven-landmark dead ends and their merger at budget eight do not follow from the scalar dimension, making the census useful for assessing stronger resolution and feasible-set mobility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
