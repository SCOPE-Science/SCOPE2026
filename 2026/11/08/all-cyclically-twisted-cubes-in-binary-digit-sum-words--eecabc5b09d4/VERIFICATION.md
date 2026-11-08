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

# Verification procedure

Run `python3 check_twisted_cubes.py` in a directory containing this file and the checker. The program uses only Python's standard library and constructs the prefix both by iterative substitution and by independent binary digit summation.

It checks all triples \((N,m,s)\) with \(3\le N\le10\), \(1\le m\le120\), and \(0\le s<4096\), totaling 3,932,160 comparisons. It also validates the first position for each power-of-two root length whenever it fits inside the generated word. The program prints four PASS lines; any discrepancy raises an exception.

The infinite claims depend on three mathematical steps, not on the finite checks: (i) the shifted-difference characterization of the three blocks; (ii) the exclusion of odd root-length parts at least three by the five-consecutive-differences obstruction; (iii) the exact binary-valuation classification for dyadic root lengths. The proof is included in `RESULT.md`.

The computation does not establish historical priority, cover other twist permutations, or constitute independent external validation.
