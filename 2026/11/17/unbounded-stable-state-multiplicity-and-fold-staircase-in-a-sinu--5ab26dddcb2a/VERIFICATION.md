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

# Reproducible analytical and numerical checks

Install packages listed in `requirements.txt` in a conventional Python environment, then execute `python check_equilibria.py` in the same directory. The program first reconstructs the characteristic polynomial and its determinant relation symbolically using SymPy. It next locates roots on the full positive-sine lobes beyond the cubic transition for the published example parameters \((a,m,c,r)=(12,14,7,55)\) at two large finite feedback amplitudes, and evaluates all three Routh–Hurwitz inequalities. Finally it compares the unique lobe minimizer at a high index with the explicit two-term fold expansion.

On the reviewed environment the checker printed:

```
p=100000 positive_equilibria_outside_R=22 positive_sinks_outside_R=11 predicted_total_sinks~30.255
normalized sinks ratio 0.4739756318070145
p=1e+07 positive_equilibria_outside_R=130 positive_sinks_outside_R=65 predicted_total_sinks~138.210
normalized sinks ratio 0.6034065483696615
fold asymptotics checked 629.8845590459729 30567415.499462843
VERIFY_OK jacobian_characteristic=4 determinant_identity=1 finite_large_p_cases=2 lobe_sinks_checked= 130 fold_asymptotics=1
```

The root counts in this log include only lobes strictly above the cubic transition, not all compact-range roots. The predicted total is an asymptotic comparator rather than an exact finite-amplitude count. The checker samples finitely many values and does **not** certify all positive amplitudes, the infinite fold sequence, or the limiting sink law. Those conclusions are proved analytically in `RESULT.md`. Independent audit has not been performed.
