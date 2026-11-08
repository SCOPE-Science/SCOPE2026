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

# Finite verification report

Execute `python3 verify_grid_robust.py` using Python 3.10 or newer. No external packages or input files are needed.

The independent-four-set enumeration finds exactly 61 forbidden quartets; the two complexes contain respectively 1,415 and 2,679 nonempty faces. The checker pairs 697 and 1,329 face incidences by first-available row-major vertex toggling. It constructs all 6,160 and 13,744 codimension-one cover incidences and topologically sorts their fully oriented Hasse diagrams, visiting every node and thus proving acyclicity. Critical-cell dimensions are \(\{0:1,5:20\}\) and \(\{0:1,4:20\}\), respectively. Euler characteristics agree independently.

For the identity, row reversal, column reversal and their product, the checker recomputes every fixed face, signed vertex permutation and augmented Lefschetz number. Both top rational homology characters are \((20,0,-4,0)\). A separate square-triple fixed-set routine verifies the corresponding signed permutation module character and its four irreducible multiplicities.

The exact recorded output is in `verification_output.txt`. The output alone would not certify the theorem; the complete executable finite enumeration and the accompanying discrete Morse/Lefschetz arguments are the proof. The result is limited to this one finite grid. Independent mathematical audit has not been performed.
