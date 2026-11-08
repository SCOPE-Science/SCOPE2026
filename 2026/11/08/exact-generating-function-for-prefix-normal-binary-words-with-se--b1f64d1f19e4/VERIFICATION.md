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

# Verification of the exact generating function

Run `python3 verify_density7.py` with SymPy installed. The file is standalone and uses no downloaded input or earlier-run outputs.

The program first obtains primitive rays by exact nullspace enumeration on all rank-four active-inequality systems. It finds every supporting facet using rational linear algebra and builds a canonical recursive pulling triangulation of the nine-facet cone. Exact determinant and half-open parallelepiped calculations produce a rational generating function; the target identity is tested by symbolic cancellation, not by fitting a finite sequence. The code independently checks all words with seven ones at lengths 7–20 against the substring/prefix definition, verifies independent gap enumeration at lengths 7–27, and checks the leading asymptotic constant by exact arithmetic.

Verified execution output:

```
EXACT_CONE_G.F._OK; 13 rays, 9 facets, 15 pulling simplices
DIRECT_WORD_COUNTS_OK; lengths 7..20
INDEPENDENT_GAP_COUNTS_OK; lengths 7..27
LEADING_CONSTANT_OK; 289/2488320
COUNTS_7_TO_20: [1, 4, 13, 31, 71, 134, 249, 417, 688, 1062, 1628, 2367, 3430, 4781]
```

Exact nullspace enumeration, rational cone subdivision and formal generating-function algebra establish the infinite identity. The direct word and gap enumerations are additional finite consistency tests, not substitutes for that proof. No independent external review or certification has been performed.
