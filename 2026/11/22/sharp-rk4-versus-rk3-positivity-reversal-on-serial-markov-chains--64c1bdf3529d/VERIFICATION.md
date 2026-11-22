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

# Reproducibility and limits

Run `python3 verify.py`. The program uses Python 3 standard library exact rational matrix powers, exact complete-homogeneous-polynomial entry identities, and rational row-sum invariance. Its supplementary boundary checks use floating-point cubic bisection and rationalized test timesteps. Actual replay returned:

```
PASS 2441 exact matrix/entry checks and finite boundary/ratio checks
rho= 1.5960716379833215 delta= 2.785293563405282
sharp lower= 0.8703084536243505 sharp upper= 1.7450930754740892
```

The code exhausts neither all dimensions nor all real rate vectors. Strict monotonicity of the cubic pair obstruction, positivity of second divided differences, extremal inequalities, attainment and minimum dimension are demonstrated in `RESULT.md` analytically. This is a self-review; independent validation has not been performed.
