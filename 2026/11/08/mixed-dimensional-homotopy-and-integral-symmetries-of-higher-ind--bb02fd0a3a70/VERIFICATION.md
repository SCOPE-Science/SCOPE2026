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

Run `python3 verify.py` from the directory containing the verifier. The code independently enumerates graph-induced connected components and admissible faces for exactly 47 parameter triples: \(2\le k\le4\), \(2\le s\le4\), \(1+ks\le11\), and all \(1\le r\le ks+1\). It computes reduced mod-two boundary ranks and checks all degree distributions, including the disconnected base case and contractible tail. It also verifies 188 signed Lefschetz traces (identity, one leaf swap, one block swap and simultaneous leaf swaps) against the exterior-power character formulas. The produced line is recorded in `verify_output.txt` and must match exactly.

These computations do **not** prove torsion-freeness, homotopy equivalence, or the integral module for infinitely many parameters. Those follow separately from the exact face decomposition, standard skeleton chain complexes, nullhomotopy by connectivity, Mayer--Vietoris, and the join sign calculation in RESULT.md. No external mathematical audit has been conducted.
