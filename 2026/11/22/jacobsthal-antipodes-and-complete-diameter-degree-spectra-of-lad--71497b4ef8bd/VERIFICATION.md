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

# Reproducibility and scope

Run `python3 verify.py` with standard Python 3 in this directory. The program generates all \(2\times n\) domino tilings, maps each to its exact rung/top/bottom edge set, enumerates every unordered pair for \(2\le n\le12\), checks that the largest squared distance is \(2n\) and compares every vertex's degree with the \(2^{k-1}\)/parity formula. Independently, every word through \(n=19\) is passed through the transfer product and compared with the closed degree law. The exact count and histogram are derived from, and therefore limited by, these finite test domains; the manuscript proof covers every integer \(n\ge2\).

The program is self-contained and uses no downloaded data, files, packages, or floating-point rounding. Passing tests do not establish independent human validation, historical priority, or a proof for arbitrary orders without the argument in RESULT.md.
