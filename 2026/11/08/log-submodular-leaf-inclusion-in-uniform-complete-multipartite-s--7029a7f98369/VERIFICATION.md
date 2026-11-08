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
# Mathematical verification

The all-size argument is analytic: the multipartite Laplacian eigenvalues produce the classical tree count, every forced leaf attaches once to the residual core, and the resulting product of nonnegative affine functions is log-submodular by the exact inequality \((a-1)^2\ge a(a-2)\) for integers \(a\ge2\). The proof treats the empty residual, the singleton residual and a disconnected residual explicitly. The bipartite equality cases come from whether a factor depends on both added vertices.

The supplementary standalone command is:

```text
python3 verify_leaf_inclusion.py
```

Observed output:

```text
PASS: 666620 exact checks; 127 multipartite shapes; 54 independent exhaustive tree enumerations
```

The independent enumerator checks every edge subset of the appropriate size on the selected small graphs; it does not use the derived tree-count formula to classify those edge subsets. Numerical evidence is not an infinite proof. No proof of full negative association or claims about weighted/arbitrary graphs are included. Historical priority is provisional where full prior text was unavailable.
