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
# Verification of the mathematical result

Run `python3 verify.py` using Python 3 and its standard library. The file is standalone. It enumerates all \(4^4=256\) four-index prime-forbidden mask configurations and compares the four support inequalities with exhaustive perfect-matchings; enumerates primitive pairs modulo \(5\), \(7\), and \(11\) to recover each root probability; and checks all \(1,327,104\) pairs of primitive local progression residue classes modulo \(35\), finding exactly \(27,648\) failures for two progressions. Hence the exact success proportion for that case is \(47/48\). It separately evaluates all-order local forbidden-index distributions by an exact probability dynamic program for \(k=1,\ldots,7\) and three different prime pairs, and checks independently matchable but not jointly matchable explicit examples.

The symbolic proof in `RESULT.md` supplies the unrestricted equivalence and analytic density: Hall’s marriage theorem, the root-position law, inclusion-exclusion, the Chinese remainder theorem, Möbius inversion, and the leading exponential bases. Finite exhaustive computations validate discrete instances only. Errors from finite enumeration are excluded by exact integer and rational arithmetic and full loop coverage; they do not remove historical-priority uncertainty or replace the unrestricted mathematical argument.

No independent mathematical audit or validation was performed.
