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

In the extracted directory, run `python3 verify.py` and `python3 crosscheck.py` (Python 3, standard library only). Both scripts were executed against these exact embedded source bytes before packaging.

`verify.py` certifies the unbordered word candidate counts \(3,6,10,20\) at lengths four through seven, the exact partner sets of `0011`, the obstruction of shorter total lengths, the two oriented solutions, and the four-code symmetry orbit. `crosscheck.py` independently tests every sorted length triple of total at most \(16\), enumerating all binary words from length two through twelve, and confirms that only four labeled three-word codebooks of lengths \(5,5,6\) survive.

The analytic reduction in RESULT.md is necessary to relate the finite search to the unrestricted theorem. The computational checks do not establish an all-message-count or all-alphabet theorem. There has been no independent audit.

