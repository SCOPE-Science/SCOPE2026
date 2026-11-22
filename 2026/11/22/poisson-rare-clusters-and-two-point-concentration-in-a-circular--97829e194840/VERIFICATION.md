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

# Verification details

Run `python3 verify.py` with the Python standard library. The finite checker exhausts all gap orderings of lengths five through eight, checks true circular nearest-neighbor edges independently using rational distances (through length seven), verifies each large-component indicator against actual connected components, and checks the rational probability identities for the valley-gap law. The recorded run passed 368786 exact or controlled assertions.

The analytic checks are separate: the factorial tail is derived by a telescoping identity; the Poisson approximation uses local dependence and the peak-free-block probability; the two-point concentration uses a second-moment inequality and the successive tail ratio. Exhaustive finite samples do not certify infinite limits. Full-text historical-priority checks remain incomplete for two potentially related papers, as recorded in REVIEW.md.
