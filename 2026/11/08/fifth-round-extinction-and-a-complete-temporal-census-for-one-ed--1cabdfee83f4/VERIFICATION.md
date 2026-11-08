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

The theorem's finite reduction is exact for every graph order because all ordinary vertices of a given present color share identical neighborhoods. `quotient_checker.py` enumerates all 441 reduced states, compares the 15 coefficient matrices against a literal reference, checks that each of 41 periodic support states lifts with the identical labelled period, and verifies the sharp fifth-entry and orbit-count formulas on 196 additional graph-size pairs. The intact 49-support comparator verifies that its maximum transient is four.

`labelled_checker.cpp` implements the original synchronous vertex-by-vertex state updates without the quotient; it exhausts 1,185,921 labelled initial configurations over all 25 graph sizes with shore dimensions from two through six. The attached `quotient_output.txt` and `labelled_output.txt` record the observed passing checks.

Reproduce with `python3 quotient_checker.py`, then `c++ -O2 -std=c++17 labelled_checker.cpp -o labelled_checker` and `./labelled_checker`. Only the language standard libraries are used. The independent-labelled graph-size enumeration is not a substitute for the all-size exact quotient proof. Historical originality is assessed from accessible literature, not externally certified.
