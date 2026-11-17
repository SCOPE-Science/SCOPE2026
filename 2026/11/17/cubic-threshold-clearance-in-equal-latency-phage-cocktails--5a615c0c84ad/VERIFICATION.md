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

# Verification details and limits

The analytical proof checks the simple center eigenvalue, its stable transverse spectrum, the compatible-history infected-population convolution, the coefficient \(K\) and the strict sum-of-squares cubic coefficient \(C\), the local stability implication and the sharp \(\sqrt t\) rate. The all-response-zero case is an exact equilibrium family, not an inferred numerical observation.

Run the standalone source `python verify_phage.py` with SymPy installed. Its exact symbolic checks establish the formal Taylor identities for the positive two-phage parameter witness. Finite Euler integration of the delay model with step \(0.01\), constant compatible history and observation times \(300\), \(600\), \(1200\) gives \(\sqrt t S(t)\approx0.465635904\), \(0.478209871\), \(0.486130745\) against the proved asymptotic value \(0.5\). The numerical run checks only finitely many times and does not replace the invariant-manifold proof.

The rate is for sufficiently close positive compatible histories, not a global result. No independent audit or validation has taken place.
