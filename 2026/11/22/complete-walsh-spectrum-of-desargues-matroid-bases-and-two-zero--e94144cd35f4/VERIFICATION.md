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

# Exact reproducibility

Run `python3 verify.py` (Python 3.9+, standard library only). The code independently performs direct signed summation over 110 base masks, a full length-1024 integer Walsh–Hadamard transform, and exact evaluation of the Krawtchouk-minus-lines formula. It separately enumerates the 120 induced vertex relabellings of the ten point-coordinates, partitions all 1024 character frequencies into 34 full orbits, and checks every claimed sign, multiplicity and zero motif.

Expected output includes the exact signed spectral histogram, rank 952, nullity 72, inertia (476,476,72), sharp nonzero gap 2, condition 55, and the zero orbit sizes 12 and 60. No external datasets or numerical tolerances are needed. This exhaustive finite check does not imply any result for untested other geometries, any independent mathematical audit, or historical priority.
