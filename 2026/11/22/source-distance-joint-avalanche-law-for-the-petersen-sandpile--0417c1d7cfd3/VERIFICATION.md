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

# Reproducibility and limits

Run the two supplied Python 3 standard-library programs from the directory containing the CSV:

```
python verify_kneser.py
python verify_prism.py
```

Verified outputs:

```
PETERSEN_KNESER_EXACT_PASS recurrent=2000 joint_terms=44
PETERSEN_GENERALIZED_PETERSEN_EXACT_PASS recurrent=2000 joint_terms=44
```

The two programs independently construct the graph (disjoint two-subsets versus generalized Petersen outer/inner cycles), independently characterize recurrent configurations (burning addition versus forbidden-subconfiguration elimination), and independently stabilize additions (sequential versus parallel). Each compares the exact entire joint coefficient dictionary to `JOINT_COUNTS.csv`. They check per-case conservation; the first also checks the mean dissipation identity and both maxima. The 2,000 configurations follow independently from the reduced Laplacian determinant and the verified 3-to-the-ninth exhaustive state space.

These are finite integer proofs of a finite exact claim. They do not validate generalizations to larger graphs, infer universal asymptotic exponents, establish historical priority, or constitute an independent scientific audit.
