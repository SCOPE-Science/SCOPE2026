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

# Verification of the mathematical statements

Run `python3 checks/verify.py` with a standard Python 3 installation. The script tests the **original** idempotency and two averaging identities on all ordered pairs of basis vectors. The three-dimensional boundary is fully exhausted over \(\mathbb F_2\) (\(2^9\) matrices) and \(\mathbb F_3\) (\(3^9\) matrices). It produces rank counts \((1,16,0,1)\) and \((1,45,0,1)\), respectively. These are boundary verification only; this dimension is not claimed as new.

For the five-dimensional case over \(\mathbb F_2\), it enumerates all \(2^{16}\) quotient matrices and both values of the center scalar, uses derived necessary equations to restrict possible central rows, then **rechecks the original defining identities** for every selected matrix. The rank profile is \((1,256,960,80,0,1)\), in agreement with the derived symplectic and isotropic rank formulas. Substitution checks for \(q\in\{2,3,5,9\}\) and \(1\le m\le4\) test integrality and rank support, not complete finite-field enumeration or operations over \(\mathbb F_9\). The successful program prints `HEISENBERG_AVERAGING_PROJECTIONS_VERIFIED`.

The arbitrary-dimension classification, orbit transitivity and smooth reduced components depend on the direct algebraic proof in `RESULT.md`, not finite experiments. No assertion about the equation scheme's nilpotents or external/independent mathematical validation is made.
