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

# Verification of the stated classification

Run `python verify.py` with a standard Python 3 interpreter. The program requires no external packages and performs these checks: (i) the class-level dominating and exchange criteria for every occupancy profile of size at most five in all four threshold regimes with each shore size four or five; (ii) the corresponding profile formula at 64 additional parameter pairs; and (iii) direct labelled vertex-subset enumeration, with a separately implemented adjacency representation, for shore sizes (4,4), (4,5), (5,4), (5,5), and (4,6).

Observed output:

```
FOUR_THRESHOLD_REGIMES_EXHAUSTIVE_OK
UNRESTRICTED_FORMULA_SPOTCHECK_OK 64
LABELLED_VERTEX_CHECK_OK 4 4 804
LABELLED_VERTEX_CHECK_OK 4 5 1330
LABELLED_VERTEX_CHECK_OK 5 4 1330
LABELLED_VERTEX_CHECK_OK 5 5 2225
LABELLED_VERTEX_CHECK_OK 4 6 2046
VERIFY_OK
```

The proof establishes the unrestricted theorem by a five-class exact reduction and case analysis; the program is a transparent finite-case companion. Finite numerical tests alone do not prove a statement for arbitrary shore sizes. All claims of originality remain provisional pending external literature and mathematical review.
