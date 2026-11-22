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

# Verification record

The `structural_census.py` checker enumerates every one of the 65,536 binary incidence matrices and independently evaluates the proved pair/singleton recursion criterion for rank three. It lists all 29 side-preserving symmetry classes, with a seven-value edge histogram and orbit sizes. Its full output is in `structural_output.txt`.

The `independent_recursion.py` checker instead follows the **original definition** literally: at each of the finitely many parameter sets encountered at depth at most three it quantifies over every admissible new-shore Boolean pattern and every available witness. It checks all 65,536 matrices without importing the structural checker. Its actual full output is in `independent_recursion_output.txt`.

The `burnside_direct.py` checker constructs fixed matrices under pairs of row/column permutations as unions of orbits on the sixteen matrix cells and invokes the independent direct recursion, not canonical relabelling. The fixed-sum 16,704 and orbit total 29 agree with the independent canonical enumeration. Actual output is in `burnside_output.txt`.

All-order host order and edge minimum arguments appear in the proof, independent of computational exhaustive tests. The enumeration proves only the eight-vertex stratum and does not make a claim about every higher order, rank four, or historical publication priority. Independent external mathematical validation: not performed.
