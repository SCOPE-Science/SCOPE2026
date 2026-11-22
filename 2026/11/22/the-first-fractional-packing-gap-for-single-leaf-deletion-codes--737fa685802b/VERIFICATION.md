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

# Reproducibility

With Python 3 and a C++17 compiler, execute `sh reproduce.sh` in a folder containing all files listed in the accompanying archive. `checker.py` reconstructs all trees using edge insertion, identifies each by its canonical set of nontrivial leaf splits, checks direct pruning against split restriction for every tree and deleted label, enumerates every receiver, verifies 1/3/15 complete small codebooks, and regenerates `incidence7.txt` and `witnesses.json`.

The incidence file starts with `945 735`, followed by 945 lines, each listing exactly seven receiver identifiers. Every receiver identifier occurs nine times. The exact-cover verifiers independently check that no 105-row subfamily partitions the receiver set. They return `NO FOUND after calls=2561709` and `UNSAT nodes=2561709`. They have no timeout, iteration limit, or floating-point stopping condition.

The upper-bound proof is that a 105-word code would necessarily cover every one of 105 possible outputs for each missing label. The present evidence proves impossibility of equality, but it does **not** prove the exact size of a largest seven-leaf code.
