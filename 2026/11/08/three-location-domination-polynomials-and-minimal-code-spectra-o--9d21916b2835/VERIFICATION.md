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

The standalone Python file `verify_complete_prism_location.py` checks the original closed-neighborhood definitions of ordinary, solid and self location domination, their full cardinality polynomials, and all inclusion-minimal cardinality distributions. The exhaustive parameter range is \(4\le n\le8\), examining \(87{,}296\) labelled vertex subsets. The output was:

```
PROFILE_OK n 4 subsets 256 LD 181 DLD 77 SLD 63
PROFILE_OK n 5 subsets 1024 LD 638 DLD 238 SLD 221
PROFILE_OK n 6 subsets 4096 LD 2175 DLD 723 SLD 703
PROFILE_OK n 7 subsets 16384 LD 7276 DLD 2180 SLD 2157
PROFILE_OK n 8 subsets 65536 LD 24041 DLD 6553 SLD 6527
VERIFY_OK profiles=5 all_subsets= 87296 literal_identifying_sets=PASS three_polynomials=PASS three_minimal_code_spectra=PASS structural_criteria=PASS
```

Run with `python3 verify_complete_prism_location.py` using Python 3 and no dependencies. These finite checks are not an infinite proof and do not provide independent mathematical validation. The unrestricted result is established by the classification and combinatorial argument in `RESULT.md`.
