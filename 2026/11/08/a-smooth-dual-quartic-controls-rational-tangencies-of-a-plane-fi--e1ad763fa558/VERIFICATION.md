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
# Reproduction and verification

Run `python3 verify_tangent_spectrum.py` from the directory containing this file and the script. The program uses only the Python standard library and exits with `VERIFY_TANGENT_SPECTRUM_OK 41` when all assertions pass. Its tests enumerate projective rational points and lines over the prime fields with characteristics \(3,5,7,11,13,17,19,23,29\); for every parameter without a root of \(T^7+kT^3-1\), they independently calculate the cubic tangent-vector map and compare the fiber spectrum with the zero set of the quartic. For primes at most \(17\) they independently count tangent incidences point by point on each line. The script intentionally does not claim exhaustive tests over all prime powers.

The general theorem is proved algebraically in RESULT.md. For the crucial quartic smoothness step, the exact polynomial identity
\[
3bH_B=aH_A+3(3+4kb)H_C-4a(kb+1)(6kb+7)
\]
holds over \(\mathbb Z[a,b,k]\) in the chart \(C=1\), and the remaining steps are explicit field operations with cases for characteristics \(3\) and \(7\). The identity has also been symbolically expanded and checked independently during proof reconstruction. Finite computations do not replace the proof of smoothness or the Hasse–Weil consequence.

No independent audit has been performed, and the global geometric smoothness of the high-degree plane-filling curve is not asserted.
