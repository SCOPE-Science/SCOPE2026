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

The analytic proof is valid for every integer \(d\ge2\), every \(J_i>0\), and every real \(K\). The nonstandard equality classification follows from the Boolean constraint \(g^2=1\) on a degree-one Walsh polynomial, not from a finite enumeration.

The standalone `folded_cube_verifier.py` uses exact integer arithmetic and Python 3 standard libraries only. Run it with `python3 folded_cube_verifier.py`. In the recorded execution the script printed:

```
VERIFY_OK exhaustive_cases=26 spectral_cases=561 max_exhaustive_dimension=4
```

For the 26 cases, the program independently enumerated every binary spin configuration and compared **both** the exact minimum energy and the complete collection of minimizing spin configurations against the asserted theorem. Additional signed weighted cases across dimensions \(2\) through \(12\) compared the complete Walsh spectrum's minimum with the theorem. These finite checks are supplementary; no finite test is represented as proof of the infinite-family claim.

The original full-text folded-hypercube spectrum article and the general Ising/Hadamard article were inspected. The full text of one related weighted network-spectrum article remained inaccessible, so historical novelty has a residual literature-access risk. No independent audit has been conducted.
