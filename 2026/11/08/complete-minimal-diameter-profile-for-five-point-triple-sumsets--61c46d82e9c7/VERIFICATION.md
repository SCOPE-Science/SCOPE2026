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

# Finite certificate and its limits

Run `python3 verify.py` using the Python standard library. The verifier enumerates all \(\binom{23}{4}=8855\) translated five-element sets of diameter at most \(23\), calculates each \(|3A|\) both via direct multisets of three indices and via bitset shifts, and checks the 22 sharp minima, the 22 explicit witnesses and the four maximal-cardinality extremizers. All arithmetic is integer-exact. The finite enumeration proves the minima: any shorter hypothetical realization would be one of the enumerated cases. The published theorem of Rajagopal supplies the *global* list of possible values of \(|3A|\), including the impossibility of \(14\); the verifier does not attempt to establish this infinite statement by finite testing.

The executable file and expected table are embedded in the same package. The recorded status reflects only self-review. Independent audit has not been performed.
