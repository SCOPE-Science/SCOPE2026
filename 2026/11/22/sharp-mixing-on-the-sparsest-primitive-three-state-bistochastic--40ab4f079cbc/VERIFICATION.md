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

# Verification of the minimal-support mixing theorem

Run `python3 verify.py` with Python 3 and SymPy. Observed output:

`VERIFY_OK support_graphs=9 primitive_conjugates=6 exact_jordan_powers=7 spectral_test_parameters=25`

The script checks the symbolic characteristic polynomial, the exact nilpotent Jordan identity, all nine feasible support patterns with five nonzero cells, the six primitive support relabelings, and 25 rational spectral comparisons. These finite computations provide reproducible consistency evidence; the complete analytic proof covers every real parameter and all matrix powers. A full independent audit has not been performed.
