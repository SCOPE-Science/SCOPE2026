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

# Direct verification

The standard-library-only `verify.py` constructs the complete coefficient-by-coefficient derivation equations in the natural basis, eliminates them over each prime field, and compares the resulting exact nullity with the degree-set formula. It independently constructs each predicted derivation in group-ring truncated-polynomial coordinates and checks the Leibniz equation on all ordered pairs of basis elements. Further direct commutators of the constructed matrices check the Lie bracket relations. The saved run is `verification_output.txt` and ends with `VERIFY_OK`.

The dimension computations cover every scalar \(a\in\mathbb F_p\setminus\{0,1\}\) for primes \(p=3,5,7,11\), including boundary controls. Generator checks cover additional selected scalars at \(p=17,19,31\), and bracket checks include four selected parameter pairs. The general theorem covers every prime \(p\ge5\), all non-dihedral nontrivial scalars, and all fields of characteristic \(p\) by the proof, **not** by extrapolating from these computations. No independent external mathematical audit has been performed.
