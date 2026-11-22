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

# Reproducibility and mathematical verification

Run `python3 matching_fault_verifier.py` in the package directory. It performs complete direct induced-degree face enumeration for all 43 tested parameter stages, constructs the displayed relative boundary matrices, verifies that their composition vanishes, calculates ranks over primes 2, 3, and 5, and compares the actual second-homology inclusion image ranks across every stage. The recorded output is in `verification_output.txt`.

The general mathematical result is established instead by the integral relative-chain proof in `RESULT.md`. Mod-prime calculations cannot certify integer torsion-freeness, primitive lattice inclusions, or infinite parameter ranges. The chain presentation has fixed augmentation map and nested triangle-image lattices; the second-homology cycle classes have an explicit star-tree fundamental basis at every stage. The square boundaries have unit coefficients. These arguments establish the exact integral statements without relying on finite evidence.

The publication comparisons distinguish the prior complete classification of **each stage** from the newly determined maps **between** stages. Independent validation has not been performed.
