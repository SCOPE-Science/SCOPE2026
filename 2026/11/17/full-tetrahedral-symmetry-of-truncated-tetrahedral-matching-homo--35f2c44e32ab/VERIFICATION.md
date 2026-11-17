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

# Verification

Run `python3 verify.py` using Python 3 standard library only. The generated `output.txt` was recorded from executing that exact source. No external downloads or dependencies are necessary.

The verifier enumerates all 1010 matchings of the graph, including the empty matching, and independently reproduces their face counts by a vertex-deletion matching-polynomial recurrence, computes the exact \(\mathbb F_2\) augmented boundary ranks \((1,17,100,232,136,8)\), derives rational Betti constraints and proves the full character on all twenty-four group elements in two different ways: signed Lefschetz traces of the actual simplicial chain action and alternating counts of compatible orbits of matching edges. It also checks the five conjugacy-class sizes and traces, irreducible multiplicities, and fixed dimensions for \(S_4\), \(A_4\), the normal Klein-four group and a vertex-stabilizing \(S_3\).

The verifier output must end in `TRUNCATED_TETRAHEDRON_MATCHING_CHARACTER_PASS`. Its exact output is bundled as `output.txt`. The rank-over-characteristic-zero argument in `RESULT.md` uses the proven inequality between rational and mod-two Betti dimensions plus the Euler characteristic; there is no inference that modular ranks alone prove integral torsion-freeness. Finite-group rational averaging is applied after barycentric subdivision for ordinary quotient cohomology.

No independent audit was performed; the calculations do not prove publication priority or the integral homotopy type of any quotient.
