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

The stated coefficient recurrence was checked independently against direct all-element enumeration for \((b,h,q)=(2,1,2),(2,2,2),(2,2,3),(2,3,2),(3,2,2)\). The binary height-three case contains \(16{,}384\) labeled cover-supported matrices and 21 distinct Jordan partitions, matching exactly. Tests also check the corresponding literal matrix powers and the entire radical at binary height two.

Run `python verify.py` and `python verify_jordan.py` in the unpacked directory using standard Python. Compare stdout to `verification_output.txt` and `verification_jordan_output.txt`; they contain the actually captured successful checks. These finite checks are reproducibility probes, not an infinite proof or independent validation. The argument for all finite fields and heights is in `RESULT.md`; independent audit has not been performed.
