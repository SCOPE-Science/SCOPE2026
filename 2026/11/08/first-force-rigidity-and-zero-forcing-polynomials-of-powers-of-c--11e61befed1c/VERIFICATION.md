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

# Computational verification

Execute `python verify.py` with standard Python 3. The code constructs each labelled cyclic power from its edge definition, runs the actual iterative zero-forcing rule on every initial subset of each tested graph, separately computes the cyclic transfer trace, and compares full coefficient distributions. The observed result was:

```text
VERIFY_OK profiles 35 all_subsets_checked 327512 literal_dynamics=PASS cyclic_transfer_polynomial=PASS minimum_multiplicity=PASS minimum_boundary_profiles=30
```

The exact profiles were \(k=1,2\) with \(n=2k+1,\ldots,16\) and \(k=3\) with \(n=7,\ldots,15\), plus 30 combinations \(k=1,\ldots,5\), \(n=2k+1,\ldots,2k+6\) checked at minimum-set size. The program is fully self-contained and uses no external packages or numerical approximations. Its test cases are finite; the unlimited quantifiers follow from the proof, not the run log. No independent audit was performed.
