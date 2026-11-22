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

The general proof is the finite-average saturation and square-swap argument in `RESULT.md`. A uniform antipodal path contains each edge with probability \(2^{1-d}\). At the sharp objective, every such path is saturated. Comparing extensions of the two routes in a square from each opposite pair of corners forces its opposite edge weights equal; all edges of one coordinate class are linked by squares. This proves the full fractional face and the count of integral maxima for *every* stated parameter.

The standalone files `verify/exhaustive_small_cubes.py` and `verify/milp_four_cube.py` separately build the cube edges and shortest paths. The former exhausts all edge subsets of \(Q_2\) and \(Q_3\) with optimal objective, for every eligible capacity; the latter uses SciPy's mixed-integer solver and successive no-good cuts to enumerate all optima for \(Q_4\) at capacities two and three. The latter runs to an optimal solver termination with next-best objective strictly smaller. `verify/CHECKS.txt` contains the observed output; `verify/requirements.txt` specifies the nonstandard optional dependencies.

```text
Q2 t=2 optimum_size=4 exhaustive_optima=1 expected=1: PASS
Q3 t=2 optimum_size=8 exhaustive_optima=3 expected=3: PASS
Q3 t=3 optimum_size=12 exhaustive_optima=1 expected=1: PASS
Q4 t=2 optimum_size=16 all_optima=6 next_best=15: PASS
Q4 t=3 optimum_size=24 all_optima=4 next_best=23: PASS
```

The numerical verifiers establish only these small-dimensional instances. They neither prove the general theorem nor establish publication priority. The box constraints, capacity parameter, and graph are explicitly defined and are not interchangeable with unrelated weighted packing models.
