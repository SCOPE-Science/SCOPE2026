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

# Verification scope

The mathematical argument is given in the associated result. A standalone check performs the following actual independent numerical comparisons: (i) adaptive evaluation of the disk chord-coordinate integral at six noncongruent placements; (ii) equality of the two- and one-dimensional integrals at centered positions; (iii) direct Monte Carlo intersection tests with independent area-uniform disk point pairs, using a fixed seed and 700,000 pairs in each case; (iv) an analytic comparison of the minor-axis extremum against 101 angular directions in each of three ellipses. The sample comparisons apply five standard-error uncertainty tolerances and do not establish infinite-dimensional or continuum claims.

The extracted checker produces these success markers:

```
DISK_SLIT_BEER_INDEX_AFFINE_CENTERING_OK
AFFINE_ELLIPSE_FREE_ORIENTATION_MINIMUM_OK
```

For the disk, the centered exact values at normalized half-lengths \(0.1\), \(0.3\), and \(0.6\) are approximately \(0.0806971266\), \(0.2335500450\), and \(0.4120254748\). At \(a=0.3\), the two tested shifts, \((c,h)=(0.3,0)\) and \((0,0.4)\), give \(0.2060127374\) and \(0.1895448349\). The proof itself, not numerical experiments, certifies strict global centering for every feasible displacement and the unique noncircular fixed-length orientation. Reproducibility command: `python check_slit.py` after installing `requirements.txt`.

# Limitations

Numerical quadrature has finite tolerance; sampling is finite; all analytic quantifiers, the coordinate Jacobian, strictness, affine normalization and endpoint limits must be verified from the proof rather than inferred from this numerical checker. Independent scientific evaluation remains unperformed.
