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

# Verification and reproducibility

Run `python3 check_identification.py` with a Python 3 standard-library interpreter. The script checks 46,824 exact rational assertions, testing the quadratic identities, second-root inadmissibility, inverse parameters, Jacobian factor positivity, dose-response ordering, and constructive alternatives under two input levels.

The analytic proof, not the finite checker, establishes the theorem for every \(\theta>0\), \(0<q<1\), and \(0\le f<1\). It uses Poisson thinning, positivity of \(3(q-1/2)^2+1/4\), and continuity to construct a one-parameter fiber for two inputs. The displayed Jacobian is derived from differentiating \(a+j\theta q^j\); the program checks its explicit positive expression at rational examples.

The model is idealized and supplies no performance guarantee for finite assay replication, sampling error, heterogeneous extracts, dependent background contamination, or alternative inhibition laws. Independent scientific audit has not been performed.
