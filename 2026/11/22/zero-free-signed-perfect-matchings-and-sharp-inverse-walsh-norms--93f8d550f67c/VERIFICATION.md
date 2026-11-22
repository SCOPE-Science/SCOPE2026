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

# Exact verification

The standalone `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` from the directory containing the file terminates with successful assertions and prints `PASS` for the two graph-model matching enumerations and the 2048 quotient signed-permanent comparisons.

Verified quantities: 30 edges, 60 matchings, each single edge in 20 matchings, all compatible edge pairs extended by even counts; magnitude multiplicities 1551, 406, 90, 1 at 4, 12, 20, 60; all signed multipliers equal 4 modulo 8; smallest magnitude 4; 1343 nonzero inverse-kernel entries; exact endpoint norm 68/15. Full-space multiplicities are derived from the 19-dimensional switching action.

The finite integer enumeration is exhaustive by the recursion, and the general all-signings conclusion is the modulo-eight proof from the enumerated incidence moments. The inverse rational transform is exact; no external symbolic or numerical certification is claimed. Independent audit has not been performed.
