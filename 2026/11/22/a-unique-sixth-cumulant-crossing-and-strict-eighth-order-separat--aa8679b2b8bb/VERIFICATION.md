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

`CHECK.py` is a self-contained Python script requiring NumPy and SciPy. Run `python3 CHECK.py` alongside the other files. On the reviewed inputs, it printed `PASS 949 generator-hierarchy and analytic assertions`.

The script constructs two *separate* finite-dimensional infinitesimal-generator moment hierarchies through integrated-diffusivity order four, then converts the resulting Gaussian mixtures into second, fourth, sixth, and eighth displacement cumulants. It compares them at multiple positive mean, decorrelation, time, and contrast parameters, including the analytic crossing and both sides. It also checks the strict eighth-cumulant gap numerically and its short-time expansion.

No finite grid proves global sign or unique crossing; these are proven using strict algebraic monotonicity and the ordered positive four-time cumulant kernel in `RESULT.md`. The source result is mathematical and independently unvalidated; the test is not a formal proof certificate and cannot detect unindexed equivalent publications.
