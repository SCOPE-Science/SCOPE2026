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

# Verification procedure and limits

The proof has four independent steps: compulsory letter counts from two admissible targets; exact zero-rank criterion for single-one patterns; complete classification of interval covers for odd target length; and embedding of all admissible targets into every candidate using the three two-bit patterns contained in `010`. None of these steps assumes a finite computational cutoff.

To reproduce the checks, execute `python3 verify.py` beside this file. The verifier enumerates every host with the forced letter counts for each target length from \(1\) through \(12\), compares direct coverage of all no-`11` targets with coverage of just the single-one targets, and compares both sets with the explicit candidate classification. It examines \(36{,}940\) candidates over this finite range. It separately tests all constructed masters through target length \(20\). `verification_output.txt` contains the exact observed results and `VERIFY_OK` marker.

This does **not** exhaustively enumerate hosts of arbitrary length, prove the claim for all target lengths, or establish historical novelty. The universal proof is in `RESULT.md`. An independent mathematical audit has not been performed.
