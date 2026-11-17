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

# Reproducible verification

The theorem's finite computations concern exact rational graph eigenvalues and four strict sign changes of a real trigonometric root equation, followed by interval enclosures of two center parameters, the root-crossing speed, the cubic amplitude coefficient, and the leading cosine amplitude. Execute `python VERIFY.py` with `mpmath==1.3.0` installed. On the checked installation the program returned:

```
VERIFY_OK root_signs=4 rigorous_interval_comparisons=5 Walsh_eigenvalues=4
alpha_star [0.09529711354018..., 0.09529712250681...]
second_center [0.11199127315516..., 0.11199127883273...]
crossing_real [0.0459636114174..., 0.0459636480588...]
cubic_real [-0.0122364394409..., -0.0122364253416...]
physical_amplitude_coefficient [3.87622997172..., 3.87623374993...]
```

`VERIFY.py` uses arbitrary-precision interval arithmetic, not point-value sign tests. Endpoint intervals and exact graph eigenvalues are checked with hard assertions. The proof that no other root crosses earlier is analytic, using a global frequency bound and two monotonic branch equations; this has to be read in RESULT.md rather than inferred from finite tests. The standard local retarded Hopf theorem is invoked, not implemented numerically. No unrelated proof assistant or independent validation was used.
