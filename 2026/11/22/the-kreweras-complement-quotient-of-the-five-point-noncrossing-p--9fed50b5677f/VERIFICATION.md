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

# Reproduction of the finite homotopy certificate

Place `verify.py` and `cancellation_certificate.json` in the same directory and run:

```
python3 verify.py
```

The program reconstructs the finite set of 40 proper noncrossing partitions on five labels and the tenfold complement action. It enumerates the original 40/150/125 simplices, the 315/1050/750 barycentrically subdivided simplices, and the quotient's 36/110/75 orbit simplices, retaining stabilizers and parallel edges. It builds the signed oriented attaching words, constructs the lexicographically canonical spanning tree of 35 edges, and verifies each of 74 single-generator two-cell cancellations against the included JSON certificate. The final CW model has one zero-cell, one one-cell and one two-cell, with attaching word five positive copies of the surviving generator.

Expected terminal lines:

```
KREWERAS_NC5_QUOTIENT_MOORE5_OK
vertices=36 edges=110 triangles=75; tree_edges=35; generator_eliminations=74
last generator= 105 last relator= [105, 105, 105, 105, 105]
```

All code requires only Python 3 standard-library modules and uses exact finite combinatorics. It checks explicit cell identifications and the complete homotopy-preserving elimination sequence. As a separate consistency check, modular boundary ranks of the orbit complex are \(35,75\) outside characteristic five and \(35,74\) in characteristic five. The latter is a homology check; the actual homotopy conclusion depends on the complete checked attaching-word cancellation. No assertion about any larger complex or unverified external computation is made.
