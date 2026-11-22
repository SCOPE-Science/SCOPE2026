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

The finite check scripts `verification/verify_monochromatic.py` and `verification/verify_moments.py` require only the Python 3 standard library. Run them separately using `python3 verification/verify_monochromatic.py` and `python3 verification/verify_moments.py`; the expected console output is provided in `verification/verification_output.txt` and `verification/moments_output.txt`. Direct combinatorial mask enumeration was compared with the gap-polynomial identity. The moment checker independently enumerates weak compositions and expansions of the joint generating function. All finite assertions passed.

The unrestricted theorem rests on the explicit gap bijection, coefficient extraction, smoothing identity and Stirling asymptotics in `RESULT.md`, not on finite enumeration. No proof of novelty from failed searches, independently certified audit, or distributional limit theorem is asserted.
