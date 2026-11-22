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
# Verification of the finite cut-complex classification

Run `python3 verify_cut5.py` with Python 3 using only its standard library, then compare complete output to `expected_output.txt`. The script requires no internet connection or packages. It constructs the graphs and all faces by definition, verifies the direct complement condition for every bit mask, forms every nonempty Hasse-cover incidence, checks that reversing the deterministic matching preserves acyclicity by Kahn's full topological sorting, and counts critical cells. It separately reduces all ordinary simplicial boundary maps over the field with two elements and checks the prescribed Betti numbers, including intermediate zeros. The largest case has 62,850 nonempty simplices, 30,818 matching pairs and 491,376 directed Hasse relations; all are visited. The exact final output is `ALL FIVE EXACT MATCHING AND DAG CHECKS PASSED`.

The proof of the **integral homotopy** statement uses the exhaustive acyclic matching and standard discrete Morse theory; the separate mod-two reductions alone would be insufficient. Verification proves only the finite cases of graph widths 8, 10, 12, 14, and 16. It does not establish any formula for larger widths. No independent audit has been performed.
