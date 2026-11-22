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

# Computational verification and limits

Execute `python3 verify.py` with the SymPy dependency in `requirements.txt`. It computes both quartic discriminants in characteristic seven, checks irreducible factors and the exceptional square quartics, then performs a complete field-element census above every \(\mathbb P^1(\mathbb F_{49})^2\) point in two different quadratic presentations. It also checks that each model is pointless over \(\mathbb F_7\). The output is deterministic and all assertions must pass.

The polynomial identities and field point counts are exact finite calculations, not Monte Carlo tests. Geometric Kodaira-type reasoning uses the distinct-root and discriminant multiplicity facts proved in the accompanying result, as well as smoothness of each input surface from its cited source. Source authors' published smoothness arguments are not independently reconstructed here. No full Weil polynomial or integral Picard computation is claimed.
