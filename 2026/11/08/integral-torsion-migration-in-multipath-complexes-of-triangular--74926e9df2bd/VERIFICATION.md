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

# Verification

The exact standalone scripts `verify_book.py` and `independent_book.py` are contained alongside this document. `verify_book.py` enumerates all arc subsets by valid path extensions, verifies the full simplicial Hasse incidence graph, and computes the integer cellular Morse boundary from signed gradient paths. It checks the number of critical cells and the rank-one Smith entry \(2\) for three, four and five pages, with zero boundary for six pages. The matrix-rank computation checks all integral \(2\)-minors of the occupied Morse boundary vanish, not only a modular rank.

`independent_book.py` uses independently defined arc combinations and independent directed-cycle testing, and calculates boundary ranks over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_5\). Both programs are standard-library-only. Their actual captured output is in `verification_output.txt`. The exhaustive checks certify exactly the four finite graphs stated, not all page counts. Independent external audit has not been performed.
