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

# Verification

Run `python3 CHECK.py` from the directory containing both supplied files. No third-party packages, outside datasets, downloaded papers or network services are required.

Observed complete checks: 1,280 balanced candidate words; 640 reverse-complement pairs; 248 self-consistent admissible pairs; 9,048 compatibility graph edges; exact maximum clique size 22 after 15,560 finite recursive calls; 44 distinct valid witness words. The algorithm uses exact integer bitsets and safe independent-set coloring upper bounds, not a timeout, floating-point threshold, or unproved solver declaration. Another independent integer-optimization calculation agreed, but is not part of the supplied proof.

The code checks each distinct witness's length and GC count, Watson–Crick closure, and every ordered pair's five proper prefix/suffix comparisons. The computational proof is finite-length only; no longer-length or biological performance claim is verified.
