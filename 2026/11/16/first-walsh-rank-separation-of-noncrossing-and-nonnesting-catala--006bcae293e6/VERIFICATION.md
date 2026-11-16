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
# Exact verification

Execute `python3 verify_catalan.py spectrum.csv`. This rebuilds all restricted-growth partitions for \(2\le n\le5\), reconstructs the nonnesting family a second way as interval-root antichains, and compares every coordinatewise signed sum to the independent integer Walsh–Hadamard butterfly transform. It checks equality of the full signed histograms through order four, verifies both order-five nullities, matches all certificate rows, and checks the full Parseval sum at each order. There are exactly 1024 frequencies at order five. No floating point computation or statistical sampling is used. The positive marker is `CATALAN_NN_NC_FOURIER_SPLIT_PASS`.

A separate mathematical argument, using the Fourier transform of an affine change of variables, establishes non-equivalence from the differing zero counts. All finite computations concern these exact small orders; no all-order result or independent mathematical audit is claimed.
