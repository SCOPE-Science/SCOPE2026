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

Extract `checker.py` and `requirements.txt` from this item, install the latter into a trusted environment, and run `python checker.py`. The reference execution finished with **48 assertions passed** and printed Sturm endpoint variations \(V(0)=9\), \(V(1)=6\). The checker constructs the ODE solution, rational derivative identity, derivative polynomial, gcd, and exact Sturm root count from declared constants. A separate fixed-step RK4 integration of the original ODE is a supplementary finite check. The two-region strict concavity is a symbolic identity under positive parameters; one-region response is constant.

The output does not prove that a physical plant exhibits the effect, and no empirical calibration or independent scientific audit has been performed. Public preprint date for motivating literature: 2007-10-04, as stated by the publisher discussion archive; later journal date is not used as the first public date.
