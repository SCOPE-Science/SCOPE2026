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

# Verification of the stated Riccati pulse result

1. Algebraic derivation: derive each constant adverse pulse transfer by setting \(x=z'/z\), \(z''=-a^2z\). Multiply two symbolic matrices and verify their commutator is exactly diagonal with opposite entries. The threshold covector \((1,1)\) kills this diagonal term on the starting vector \((1,1)^{\mathsf T}\).
2. For any two schedules finite during the entire forcing interval, verify that \(z(0)=1\) and no zero of \(z\) implies the terminal transfer denominator is strictly positive, so the numerator sign classifies recovery/criticality/escape.
3. Append a third transfer and multiply the commutator; its terminal threshold difference equals the analytic product in RESULT.md. For the three chosen pulses check rational terminal values \(0,-1/4,-6/7\) and \(3/8,-4/7,-3/2\).
4. Run the bundled checker using `python3 check_riccati_pulses.py`. Its exact arithmetic checks 144 two-phase samples, 729 three-phase identities, and the witness. The output must be `RICCATI_PULSE_EXACT_OK two_phase=144 triple_identity=729 three_phase_witness=1`.
5. This computational test is supplemental only: universal claims depend on the full matrix calculation in the proof, not on finite enumeration. The finiteness hypothesis is essential for comparing signs; the theorem deliberately excludes comparisons when one trajectory has a pole during exposure.

Independent audit has not been performed.
