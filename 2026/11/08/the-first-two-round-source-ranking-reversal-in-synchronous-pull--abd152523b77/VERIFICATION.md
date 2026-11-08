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

# Reproducibility of the finite-round source comparison

Execute `python3 verify_pull.py` from the directory containing the files. The checker uses only the Python standard library and `fractions.Fraction`; it has no random sampling, dependencies, or platform-specific inputs.

Its exact two-round formula is a separate calculation from the finite-state Markov kernel. It checks all twenty unequal bipartitions of total size at most ten for a strictly positive smaller-source two-round advantage and all five unequal bipartitions of total size eleven, with only \(K_{5,6}\) negative. It cross-checks the two formulations for smaller graphs and for the critical graph, and compares the four exact two- and three-round rational CDF values against independently specified constants.

Expected final line from the observed run: `VERIFY_OK 57 exact checks`.

This verifies finite arithmetic from a supplied derived recurrence, not the absence of other literature, not stochastic ordering at uncomputed times, and not any independently audited theorem.
