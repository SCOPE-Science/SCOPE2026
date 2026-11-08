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

The theorem has two different evidentiary components. The general strict hierarchy is proved algebraically by \(\Delta^d f=\mathbf{1}+A^d f\) and the unique shortest walk, with radius locality ruling out every lower-depth formula. Finite tests are supplementary for this claim.

For the exact \(P_n\) counts, `refinement_checker.py` and `singleton_checker.py` enumerate all valuations and roots independently: one compares unordered distinct neighbor types; the other compares truth of each depth-bounded singleton-characteristic noncontingency test. On \(P_4\), `semantic_checker.py` enumerates *every* Boolean truth vector over the current partition and directly evaluates \(\Delta\), confirming the stable profile \(2,4,12,14,14\) without using either refinement implementation. `hierarchy_checker.py` evaluates the two explicit endpoint-defect models for \(d\) from one to one hundred, confirming the general proof's finite instances. The type table supplies a further finite certificate of the four-world classification.

Commands, from the directory containing these files:

```
python3 refinement_checker.py
python3 singleton_checker.py
python3 semantic_checker.py
python3 hierarchy_checker.py
```

The checkers use Python 3 and no nonstandard libraries. Exact script outputs include `REFINEMENT_OK`, `SINGLETON_OK`, `SEMANTIC_OK`, and `HIERARCHY_OK`. Enumeration does not prove an arbitrary-size stabilization formula; none is claimed.
