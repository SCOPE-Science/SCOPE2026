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

# Reproduction and boundaries

Run `python3 verify.py` using a standard Python 3 installation. The script enumerates every categorical cylinder cell as an independent conjunction of zero or more coordinate-equality constraints, then enumerates candidate supports and directly checks whether the set of intersection traces has cardinality \(2^m\). It computes the proposed formula separately by integer inclusion–exclusion and compares results.

The executed test covered thirteen grids, with alphabet-size tuples \((2)\), \((3)\), \((4)\), \((5)\), \((2,2)\), \((2,3)\), \((2,4)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((2,2,2,2)\), \((2,2,2,3)\), and checked 22,061 supports. The expected final line is recorded in `verification_output.txt`.

These are finite exhaustive tests for the listed bounded supports. They are not an exhaustive computation over arbitrary dimension, cannot replace the private-coordinate proof, and do not verify the infinite Poisson asymptotic numerically. The latter follows from explicit factorial moments under the written hypotheses. Independent external validation has not been performed.
