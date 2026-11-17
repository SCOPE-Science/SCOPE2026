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

# Reproducibility and limitations

The standalone `VERIFY.py` uses Python's standard library. Execute `python VERIFY.py` and compare the output to `VERIFY_OUTPUT.txt`. Its two independent stages are (i) recursive enumeration of all faces of an explicitly built flag complex, and (ii) bitset Gaussian elimination on simplicial boundaries over the field with two elements, for dimensions four through six. The link is tested via the expected two-clique and perfect-matching pattern. Full finite-chain and link computations support the proof's normalization and examples.

**Integral distinction:** Mod-two ranks do not establish torsion-freeness or the unrestricted theorem. The all-parameter integral claims rely instead on Green's integral homology theorem, the integral four-cycle basis of the link, and surjectivity of the relative-chain map from integral cross-polytope fundamental classes, as detailed in `RESULT.md`. No external audit or formal proof certificate is asserted.
