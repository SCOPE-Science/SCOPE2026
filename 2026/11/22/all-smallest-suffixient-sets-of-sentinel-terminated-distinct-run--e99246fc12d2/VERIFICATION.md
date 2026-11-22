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

The symbolic argument in `RESULT.md` proves the infinite family. To reproduce the finite checks, run `python verify.py`; no libraries beyond the Python standard library are required. The captured result appears in `verify_output.txt`.

The verifier constructs all right followers and all supermaximal right extensions directly from literal substrings. It compares the full sets, not merely their number. It separately checks occurrence-endpoint multiplicities, their pairwise disjointness and direct right-extension coverage. For four small instances it enumerates all candidate minimum-sized subsets to verify the exact count without using the product formula.

The finite verification covers 246 parameter instances and 12,358 right extensions. It does not certify parameters outside the enumerated ranges or the novelty of the statement. The proof's key hypotheses are the distinct cyclic letters, non-singleton runs, repetition count at least two and explicit unique terminal marker. Removing the marker changes the right-extension system and is not supported by this certificate.
