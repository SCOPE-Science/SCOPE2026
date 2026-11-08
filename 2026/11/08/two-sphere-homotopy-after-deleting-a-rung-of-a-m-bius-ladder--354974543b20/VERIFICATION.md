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

The self-contained `verify.py` was run with Python 3. It generates graph edges by their cyclic and antipodal definition, removes the singled-out rung, and checks each recorded open-neighborhood inclusion at the stage it is used. It checks that the \(n=4k+1\) link reduces to a connected \(6k\)-cycle; that the \(n=4k+2\) deletion and link reduce to the prescribed disjoint-edge graphs; and that the \(n=4k+1\) deletion admits folds to a graph containing an isolated vertex. It additionally enumerates simplicial faces and computes homology ranks over \(\mathbb F_2\) for \(n=5,6,9,10\).

Observed executable output (also embedded as `verification_output.txt`):

```
ALL_VERIFY_OK symbolic_fold_cases=70 valid_folds=2320 homology_cases=4 face_instances=10632
```

The exhaustive enumerations apply only to the tested finite cases. Infinite correctness is supplied by the explicit parameterized fold sequences and standard homotopy lemmas in `RESULT.md`, not inferred from those enumerations. The proof uses a published vertex-deletion lemma and path/cycle classification, neither of which is independently recertified by this program. No independent validation has been performed.
