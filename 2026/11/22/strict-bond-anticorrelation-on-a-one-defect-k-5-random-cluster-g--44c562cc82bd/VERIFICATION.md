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

# Verification of the finite polynomial certificate

`verify.py` uses only the Python 3 standard library. It enumerates all 1024 subsets of the ten-edge complete graph, counts five-vertex connected components exactly, and constructs integer-coefficient four-cell partition polynomials. For all eight \(S_2\times S_3\) pair orbits, it reconstructs the normalized Rayleigh polynomial, verifies divisibility by \(q^2(1-q)\) and multiplies back to confirm the identity. All 45 pairs are accounted for by the eight orbit sizes \(6+3+6+3+6+12+6+3=45\).

It compares the regenerated integer-coefficient tables byte-independently as JSON data with `CERTIFICATE.json` and checks positive coefficients in seven orbits. For the sole remaining orbit, the code subtracts \(25v^4(v-w)^2\) and \(v^5(84v^2-20vw+96w^2)\) from the constant-in-\(q\) slice, finding exactly 14 strictly positive monomials. It checks every positive-\(q\) slice has nonnegative coefficients and verifies the quadratic has negative discriminant. Together these algebraic conditions are a parameter-uniform proof, not a finite numerical test.

Supplementary: 540 exact-rational direct covariance computations for 12 triples of positive model parameters and all 45 unordered pairs agree with the certified factorization and have strict negative signs. The successful executable output is recorded below.

```
K5_RANDOM_CLUSTER_CERTIFICATE_PASSED edge_pair_orbits=8 edge_pairs=45 coefficient_counts=32,28,82,82,76,82,68,78 exact_covariance_comparisons=540
```

To reproduce: place `verify.py` and `CERTIFICATE.json` in the same directory, then execute `python verify.py`. No full graph classification, arbitrary heterogeneous activity assertion, independent external audit or historical-priority certification is claimed.
