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

# Exact reproducibility checks

The included programs `verify_duads.py` and `verify_symplectic.py` each construct the complete thirty-vertex graph without external input or third-party Python packages. Run either as `python3 verify_duads.py` or `python3 verify_symplectic.py`.

The first program builds the incidence graph of the fifteen duads and fifteen synthemes of a six-element set. The second constructs the fifteen points and fifteen totally isotropic projective lines of a four-dimensional binary symplectic geometry. Both verify cubic degree and graph diameter four and independently enumerate all candidate subsets of size at most four.

The programs first apply the *porous* criterion using original graph distances (a necessary condition for nonporous domination). For every porous four-set they then recompute each source-to-target shortest path after excluding the other three selected sources, and accumulate exact rational weights. Both obtain no porous sets below four and exactly forty-five feasible four-sets; each agrees with the forty-five flag constructions and the nonporous weight histogram \(16\times9/8,8\times21/16,2\times3\). The first program also checks the single six-symbol relabeling orbit. Both verify no common two-vertex overlap between distinct optimal sets and the three-replacement graph's forty-five vertices, 450 edges, degree twenty and diameter two.

The analytical proof of the lower bound and optimizer rigidity is in `RESULT.md`. The calculation of the blocked-source distance histogram and the exact diameter-two graph check are finite exhaustive statements, with completely reproducible candidate ranges rather than partial enumeration or probabilistic sampling. These are verification scripts, not a formal proof system or an external human audit.
