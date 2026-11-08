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

# Reproducibility and boundaries

Run `python verification/exhaustive.py` and `python verification/component_series.py` from the directory containing this document. Both rely only on the Python standard library and terminate with `VERIFY_OK` when every check succeeds.

The first script enumerates candidate operations and checks (P1)–(P5) on every triple, then canonicalizes all atom relabelings for two, three, and four atoms. Counts are 41/24, 278/66, and 2633/186 for labeled/isomorphism operations. It also independently evaluates the Burnside expression for five through ten atoms, obtaining 533, 1562, 4592, 13532, 39778, 116724.

A second program constructs unlabelled rooted-tree and cycle-component power series and computes via a distinct method the unlabelled functional-digraph spectrum through ten atoms. Its values agree with the Burnside counts. All arithmetic in this script is exact.

Checks of finitely many sizes are not an exhaustive proof for all lattice sizes. The general theorem relies on the explicit row classification, Burnside's lemma, the Pólya cycle index, and classical rooted-tree singularity analysis. No independent mathematical audit has been performed.
