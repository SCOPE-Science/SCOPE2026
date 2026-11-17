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

# Reproduction

Extract `verify_three_clusters.py` in the same directory and run:

```sh
python3 verify_three_clusters.py
```

The checker uses Python standard-library exact `Fraction` arithmetic and SymPy for contact-span ranks. It builds saturated-constraint graphs from candidate real potential assignments and retains exactly those with a connected graph. It compares global maximal Euclidean normal lengths, contact counts and center-rank predictions for \(m=2,3\) (the \(m=2\) cases are regression controls, not a novelty claim), including the transition equality at \(t=3/4\) for \(m=3\). Independently, it allows simultaneous intermediate points on both lower and upper sides in \(224\) integer profile optimizations, checking strict screening and the all-size formula for profile maxima. The run produced:

```
EXACT_COMPLETE_TIGHT_GRAPH_CHECK_PASS cases= 8 vertices= 10776
INDEPENDENT_TWO_SIDED_INTEGER_PROFILE_CHECK_PASS cases= 224
THREE_CLUSTER_INBALL_AND_CENTER_COLLAPSE_ALL_CHECKS_PASS
```

The code enumerates a finite set of rational parameters, not all real values. The analytical proof establishes the theorem's infinite domain. Other Euclidean embeddings and endpoint values are outside the claim. The verification is same-model reproducibility evidence and is not an independent mathematical audit.
