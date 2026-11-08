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

# Reproduction and limits

Run `python3 verify_poset_c2.py` with a standard Python 3.9+ interpreter. The program uses only the standard library. It generates all posets from predecessor ideals of newly appended maxima, reduces them by exact canonical labeling over all degree-compatible permutations, and computes shared-palette directed vertex color refinement until stabilization. It verifies exact transitivity and irreflexivity, the exceptional pair descriptions, and the relation between color-refinement class counts and isomorphism classes.

Expected final output: `VERIFY_OK 16999 16997 2`.

The run-specific textual output is embedded in `census.txt` and was reproduced from the same source. The graph counts match the published poset enumeration A000112, but that comparison alone is not a mathematical proof of uniqueness of the logical classes. Exhaustiveness follows from maximal-element extension and exact canonicalization; the equivalence of directed color refinement and \(\mathrm C^2\) is an established general theorem. The checker certifies only order at most eight and the two explicit witnesses; the higher-order extension is proved in RESULT.md.
