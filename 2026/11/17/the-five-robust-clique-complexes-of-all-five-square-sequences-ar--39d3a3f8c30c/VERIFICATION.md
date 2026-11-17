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

# Verification instructions

Use Python 3.13 (or a compatible Python 3 implementation) and `networkx==3.6.1`, as declared in `requirements.txt`. From the unpacked directory run `python verify.py` and compare its output with `verifier_output.txt` (a harmless NetworkX hashing-version warning may appear on stderr).

The checker regenerates every graph from the two definition-level gluing operations, removes isomorphic duplicates using an exact isomorphism test, enumerates all admissible simplices and all Hasse cover relations, verifies 179 complete acyclic matchings, and checks every critical cell and Euler characteristic. The successful actual run reported 255,727 nonempty faces, 127,616 pairs and critical seven-cell multiplicity distribution `[(0,67),(1,27),(2,34),(3,16),(4,2),(5,33)]`.

The proof assumes exactly five square attachments in total (one starting square and four further squares), graph simplicity and the definition of \(\mathsf{Cliq}_5\) from the referenced paper. The finite check is exhaustive for this class; it is not evidence for unrestricted square sequence length. Independent audit has not been performed.
