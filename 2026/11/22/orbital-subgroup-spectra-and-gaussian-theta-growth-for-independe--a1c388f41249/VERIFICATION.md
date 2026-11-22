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

# Reproducibility and proof boundaries

Run the included Python 3 program `verify_orbits.py` without third-party packages:

```
python3 verify_orbits.py
```

It enumerates all saturated unpointed submonoids, candidate stabilizers and their orbital-pair axioms for six small parameter sets, and compares the resulting **sets of pairs** to actual preimages of all subgroups of the corresponding cyclic products. The final output line is `MULTIGENERATOR_ORBITS_VERIFY_OK`. It also verifies the exact Gaussian rank counts for selected small primes and generator numbers.

Expected rank values: for \(p=2\), the \((R_r,T_r)\) pairs for \(r=1,2,3,4\) are \((3,1),(10,7),(38,42),(170,264)\); for \(p=3\), they are \((3,1),(11,8),(53,63),(369,632)\). The \(r=1\) values are included as source-theorem regression checks, not claimed as novel results.

The exhaustive finite checks are limited to enumerated parameter choices. The universal orbital classification, stable splitting, exact coefficients in arbitrary ranks, and infinite sharp theta limits follow from the symbolic argument in `RESULT.md`; no finite experiment alone establishes them. The proof relies on the published orbital-pair splitting theorem and elementary finite-group, Gaussian-subspace and stable-homotopy facts, whose applicability is stated there. No independent mathematical audit has been performed.
