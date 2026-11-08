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

# Reproducibility checks and limits

The `verify.py` file constructs each complete binary-state continuous-time Markov chain on stars with one to six leaves using exact rational transition rates and independent Gaussian elimination. For each size, it uses the pairs \((\alpha_{01},\alpha_{10})=(1/2,1/4),(1/3,2/3),(1,1),(2/5,3/7)\), checks all transient states against the closed formula and confirms both absorbing boundaries and the hub-versus-leaf inequalities. The actual replay printed:

`PASS 1092 exact rational checks on full Markov chains and hub-optimal comparisons`

Run `python verify.py` with Python 3.8 or newer after extracting this package. No external modules are required. These checks establish exact rational agreement only at the enumerated sizes and rates. The analytic recurrence and boundary proof in `RESULT.md` establishes the theorem for every positive pair of rates and each finite star, and the Riemann-sum argument gives its limit. Publication priority and independent external audit have not been established.
