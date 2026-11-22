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

Exact finite enumeration and two arithmetic checks were performed: all 759375 five-cell row configurations; 21960 accepted spectra; 191 isomorphism classes; 56 strongly connected classes. The two characteristic-polynomial checks are integer determinant interpolation at four explicit points (plus the guaranteed root at 2) and integer power-trace identities. All accepted matrices have connected undirected support. Canonical representatives and Burnside stabilizer sums agree. The checker was compiled and executed using the standalone `checker.cpp`, and its outputs match the provided `catalogue.tsv` and `summary.txt` byte-for-byte. A separate four-cell SymPy comparison reproduced the nine literature classes. These checks cover only the five-cell finite statement; no independent external mathematical audit has occurred.
