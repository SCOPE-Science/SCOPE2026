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

# Reproducibility

Run `python3 verify.py` in the package directory. The script uses only the Python standard library, enumerates each labeled partial injection for \(1\le n\le6\), independently constructs the inverse submonoid closure under the generator and its inverse, and compares the number of resulting distinct sets and their nilpotent-generated subcollections with closed-form predictions. It also tests the exact partition formula and the first nine values. Successful execution concludes with `VERIFY_OK`.

Observed output from the packaged script:

```
FORMULA_VALUES_OK n=0..8
DIRECT_CLOSURES_OK n=1 total=2 monogenic=2 nilpotent=1
DIRECT_CLOSURES_OK n=2 total=7 monogenic=6 nilpotent=2
DIRECT_CLOSURES_OK n=3 total=34 monogenic=24 nilpotent=7
DIRECT_CLOSURES_OK n=4 total=209 monogenic=126 nilpotent=37
DIRECT_CLOSURES_OK n=5 total=1546 monogenic=838 nilpotent=251
DIRECT_CLOSURES_OK n=6 total=13327 monogenic=6841 nilpotent=2026
VERIFY_OK
```

The program does not verify the asymptotic estimates by symbolic or infinite certificates. Those are established by the explicit coefficient argument in `RESULT.md`. The complete exact count rests on the two-generator lemma and the cyclic subgroup enumeration; the program checks only finite instances of these conclusions. The public package contains no external dependencies or unpublished datasets.
