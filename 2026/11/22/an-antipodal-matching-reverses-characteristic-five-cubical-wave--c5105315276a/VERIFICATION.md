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

# Exact verification and limits

The provided `verify.py` constructs graph edges directly, rather than relying on the Walsh-mode multiplicity calculation used in the proof. It computes the full two-layer transition matrix modulo five, raises it to twelve selected powers, performs independent finite-field Gaussian elimination and compares the resulting nullities to the stated formulas. It also confirms each tested global matrix order directly by reducing the claimed order by every prime factor. The attached `verification_output.txt` captures a successful execution on dimensions two, three, four and five for both graph families.

Run `python3 verify.py` with Python 3.9 or newer and no additional packages. All matrix computations are exact modulo five. These checks cannot by themselves certify an infinite-dimensional theorem; the accompanying proof works for all dimensions and field extensions via the Boolean character decomposition and explicit two-by-two block algebra.

No external or independent mathematical audit has been performed. The originality assessment is limited to the identified accessible literature and searchable records.
