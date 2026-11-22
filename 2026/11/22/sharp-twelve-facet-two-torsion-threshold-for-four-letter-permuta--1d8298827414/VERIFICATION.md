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

# Verification of the finite certificate

Run `python3 verify_threshold.py` from the directory containing the packaged files (Python 3 standard library only). Compare the complete output with `certificate_output.txt`.

The executable constructs the signed top boundary directly from the twenty-four four-letter permutations and all twenty-four ordered triples, computes its nine-dimensional binary kernel, and exhausts its 511 nonzero vectors. For all 369 supports of size at most twelve, fraction arithmetic gives exact rational ranks; 52 supports of weight twelve and none of smaller weight are rationally independent. Enumerating all 48 symbol-relabeling/reversal operations gives orbit sizes 2, 6, 8, 12 and 24. For each orbit representative it checks the full twenty-four-triangle lower skeleton and exact integer unimodular row/column reduction, with eleven unit pivots followed by a single factor two.

An independent SymPy Smith-normal-form computation on the same five representative matrices gave identical factors. The homotopy upgrade additionally uses the published freeness of the fundamental group, the known sphere-wedge homotopy of the full injective-word complex, the Hurewicz/Whitehead theorems and changes of basis of sphere-wedge attaching maps. The script does not verify those external theorems; their hypotheses and role are explicitly given in `RESULT.md`. Nor does the computation address arbitrary alphabet sizes, odd-primary torsion, or independent external review.
