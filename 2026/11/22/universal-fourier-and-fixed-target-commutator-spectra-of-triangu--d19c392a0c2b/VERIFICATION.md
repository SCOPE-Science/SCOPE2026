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

Run `python3 verify.py` using the Python standard library. The checker evaluates the alternating bilinear matrix directly over \(\mathbb Z/q^\ell\mathbb Z\) for \((q,\ell)=(2,1),(3,1),(2,2)\) at every Fourier frequency, plus selected frequencies at \((2,3),(3,2)\). Independently it evaluates the characteristic-two dual-number ring \(\mathbb F_2[\epsilon]/(\epsilon^2)\) at every frequency; this ring and \(\mathbb Z/4\mathbb Z\) share cardinalities and valuation lengths but have different additive and multiplicative laws. The checker also directly enumerates all \(2^{12}\) ordered pairs over the two-element field and verifies the complete fixed-target distribution by a separate direct Fourier inversion. Expected success markers are `TRIANGULAR_FOURIER_SPECTRUM_OK`, `DIRECT_BRACKET_FIBERS_OK`, and `DUAL_NUMBER_RING_OK 64`.

The program does **not** check arbitrary chain rings or prove the alternating Smith normal form or Fourier inversion; those are established algebraically in RESULT.md. The conclusions for unbounded \(q\) and \(\ell\) rest on that proof. Public finite-field computations supply a boundary comparison but do not establish publication priority for non-field chains.
