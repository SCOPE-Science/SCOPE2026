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

# Reproduction and verification

The exact bivariate claim is finite and exhaustive for the 42-vertex point–line incidence graph of \(\operatorname{PG}(2,4)\), not an assertion based on sampling.

**Homogeneous construction.** `checks/pg4_homogeneous.cpp` builds \(\mathbb F_4\) from two-bit polynomials modulo \(t^2+t+1\), normalizes all 21 projective points and 21 nonzero covectors, checks that every line has five points, every point has five lines, and every pair of lines meets at one point, then enumerates every one of \(2^{21}\) point subsets. It explicitly rejects a subset unless the set of all lines disjoint from it covers the remaining points. Counts indexed by both selected shore cardinalities must exactly match the 17 entries in `data/bivariate_spectrum.tsv`. The executable asserts the hardcoded expected map and the grand total 25,237.

**Independent coordinate construction.** `checks/pg4_affine_numpy.py` uses a different geometry specification: 16 affine points and five at infinity, 20 finite lines and one at infinity. Incidence is constructed from slopes and vertical lines, then all \(2^{21}\) point masks are vectorized and independently binned. The expected 17-entry coefficient map and total 25,237 are asserted.

**Commands**, from the package root:

```bash
g++ -std=c++17 -O2 -Wall -Wextra checks/pg4_homogeneous.cpp -o pg4_check
./pg4_check
python3 checks/pg4_affine_numpy.py
```

Both commands completed successfully against the supplied source files. The model-to-count correspondence is justified separately by the two-way maximal-independent-set parametrization in RESULT.md. The programs do not prove any formula for larger projective-plane orders; no independent scholarly audit or external certification has been carried out.
