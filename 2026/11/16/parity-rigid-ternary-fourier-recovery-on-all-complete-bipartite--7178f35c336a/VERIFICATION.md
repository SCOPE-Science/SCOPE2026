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

The exact proof is contained in `RESULT.md`. The critical steps are (i) inclusion–exclusion of the two monochromatic-shore families, including the six overlap colourings; (ii) cyclotomic character orthogonality, which forces balanced total frequency; (iii) complete parity and two-adic analysis of two signed powers of two; and (iv) combinatorial assignment counts \(U_r\) and \(V_r\). These steps establish the theorem for all positive shore sizes, independently of testing.

Run `python3 check_bipartite.py` and `python3 check_group_transform.py` from this directory (Python 3.10 or later; standard library only). Both checkers were executed on their actual files. The first enumerates all proper colourings and directly sums cyclotomic characters for eight shore pairs; the second uses a different exact multidimensional three-point discrete Fourier transform on the full indicator for six shore pairs. Both report success, including 468 extra balanced zeros and convolution rank 1719 for \(K_{4,4}\).

The scripts test only small graphs, not general \(m,n\) or unsearched literature. No independent mathematical audit has been performed.
