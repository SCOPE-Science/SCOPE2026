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

# Verification record

Running `python3 verify.py` reproduced `VERIFY_OK partition_coefficient_checks=256 direct_sums_of_two_squares=256 atom_noncoincidence_checks=256 finite_sample_TV_identity=yes exact_arithmetic=yes`. The script independently expands the two-distinct-size signed generating series through the cutoff; computes character divisor sums and ordinary divisor sums by separate divisor loops; and verifies sums-of-two-squares membership by searching integer squares rather than invoking the two-square prime factor criterion. Every test uses exact integers and Python rational fractions, never floating-point comparisons. It checks the Merca identity, normalized formula, zero-vs-atom coincidence, and atom domination at every cutoff through 256.

At the cutoff \(N=256\), the number representable as two squares is \(B(256)=97\), and the exact total-variation distance is \(97/256\). These are finite checks, not infinite certification. The unrestricted statement is proved in `RESULT.md` using the published Merca identity, elementary prime-power parity, exact floor counts, and the classical Landau--Ramanujan theorem. No independent audit or validation has occurred.
