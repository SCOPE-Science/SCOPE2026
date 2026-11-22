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

# Reproducible finite and structural verification

Run `python3 verify_arcs.py` with Python 3.10+ from the directory containing the package files. The program constructs rational projective points, lines and four-arcs without importing outside data; computes the 4,641 two-conic concepts; checks all 8,192 supports; and evaluates all 1,594,323 ternary partial assignments. It writes a deterministic `online_tree.json` and separately verifies that all 256 leaves of this depth-eight tree admit compatible concepts with no repeated query along a path. It also checks exactly 78 two-line nonbases and the mod-two top boundary rank 924.

Independently compile and run `c++ -std=c++17 -O2 verify_quadrics.cpp -o verify_quadrics && ./verify_quadrics`. This uses geometrically smooth homogeneous quadratic forms selected by nonzero Hessian determinant instead of the Python four-arc construction. Its separate support trace and ternary-state DP reproduce Littlestone dimension eight, the face polynomial, and the reduced Euler characteristic 714.

The decisive finite bounds are **exact**, not simulation: a partial-assignment state is a word in `*`, `0`, `1`; the two children assign one unqueried point absent/present. The recurrence maximizes one plus the minimum of both child depths, with branches having no compatible concept excluded. The terminal case is depth zero. Induction on unassigned point count proves correctness; exhaustive evaluation of all states proves no depth-nine tree exists. The supplied witness proves depth eight.

For the structural claim, any two unions of two distinct projective lines in this plane share at most five points. Thus the other seven-subsets form bases of a rank-seven sparse-paving matroid by basis exchange. Its independence complex is precisely the shattered-support complex. Classical shellability then implies integral homotopy equivalent to a wedge of six-spheres; the reduced Euler characteristic 714 fixes the multiplicity. The binary boundary calculation is a secondary check, not proof of integral torsion-freeness.

Scope limits: field exactly three; two distinct smooth conic components; query domain all thirteen rational points; no uniform larger-field conclusion. These self-review have not been independently expert-audited. The complete static-support census was known prior to this new adaptive/topological analysis.
