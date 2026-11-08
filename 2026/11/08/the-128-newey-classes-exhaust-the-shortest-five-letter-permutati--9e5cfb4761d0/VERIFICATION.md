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

# Reproducible verification

Run `python3 tools/verify.py` with Python 3 and a C++17 compiler available. The script compiles both independent five-letter enumeration programs and the small-alphabet control program from source and runs them. The expected console messages end with `VERIFY_OK`.

The greedy-state program tracks the longest matched prefix of each of \(120\) permutations. The explicit-language program separately tracks every realized distinct-letter subsequence of lengths \(1\) through \(5\). Both search all first-appearance-normalized, adjacent-repeat-free words subject only to a proved length-dependent prefix-completeness cutoff. The mathematical cutoff is derived in `RESULT.md`; it is not a heuristic.

The programs produce exactly \(0\) complete canonical words at length \(18\) and exactly \(128\) at length \(19\), matching the full `data/canonical_optima.txt` list. A separate exhaustive search confirms the cutoffs \((1,3,7,12)\) for smaller alphabets. Python additionally retests each of the \(128\) words against all \(120\) permutations, checks first-appearance normalization and multiplicities, and verifies every class in the supplied reversal partition (\(16\) fixed, \(56\) paired). The three programs and their input data are self-contained and require no external services or downloaded datasets.

The result is a finite, exhaustively checked classification. Generalization to more letters is neither performed nor implied. Historical-priority comparisons and independent scientific review are distinct from computational verification; an independent audit has not been performed.
