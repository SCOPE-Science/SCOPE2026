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

The included `check_psd.py` independently simulates the PSD rule at every intermediate white-component configuration for all \(33864\) initially white subsets of \(T_n\) for \(3\le n\le6\). It checks its outcome against an independently implemented union-find forest/two-component criterion; no discrepancies occurred. Its output is `check_psd.out`.

The included `check_forest_counts.py` weights all set partitions of \([n]\) using the Cayley formula for component tree counts, for \(3\le n\le8\). It independently enumerates all acyclic edge subsets for \(3\le n\le6\), compares complete forest profiles, and checks the exact sum over two-component forest sizes. Its output is `check_forest_counts.out`.

Reproduce from this directory with `python3 check_psd.py` and `python3 check_forest_counts.py`; no third-party packages or external data are used. The programs run on Python 3.8 or later. Every captured output line is embedded exactly in the accompanying `.out` artifact.

Both scripts are finite corroboration, not substitute infinite certificates. The proof for all orders is the permanent-white-cycle invariant, the spanning-tree obstruction, the leaf-to-external-component PSD forcing construction, and the labeled-tree partition enumeration. Exhaustiveness of the tested finite ranges is by direct iteration over every binary initial coloring and every set partition, respectively; no unexamined state in those ranges is inferred from sampling.
