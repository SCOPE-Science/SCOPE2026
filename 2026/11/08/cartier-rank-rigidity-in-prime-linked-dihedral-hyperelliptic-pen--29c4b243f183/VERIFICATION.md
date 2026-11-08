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

The proof is exact and valid for every prime \(p\ge11\) and every smooth geometric parameter. The included `verify.py` uses only the Python standard library and directly expands the polynomials in \(\mathbb F_p[a,T]\) for each prime from \(11\) to \(43\), verifies the reciprocal and leading-coefficient identities, and compares with independently expanded \((x^{p+1}+ax^{(p+1)/2}+1)^{(p-1)/2}\) at each admissible parameter over \(\mathbb F_p\). The program also checks matrix rank and stable-power rank, plus the zero-rank uniqueness test at all these parameter values.

To reproduce, execute `python3 verify.py` from the directory containing this file and `verify.py`; the script prints `VERIFY_PRIME_RIGIDITY_OK` followed by the exact rank census over the tested prime fields. This finite test is not a proof about all primes or algebraically closed parameters; the symbolic coefficient and anti-diagonal argument in the theorem supplies that proof. No independent mathematical audit has been performed.
