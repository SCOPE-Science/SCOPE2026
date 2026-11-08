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

# Reproducible checks and limitations

From the directory containing the embedded files, install the listed NumPy dependency and run `python CHECK.py`. The completed local replay reported `CHECK_OK assertions=137685`. The script independently constructs all three normalized Fourier columns, checks column orthogonality, checks the complement relation between erased and retained spectra, enumerates every three-site erasure mask at cyclic orders 6 through 36, checks that exactly the cyclic consecutive triples reach the predicted loss and that all retained Gram matrices are positive definite, and separately checks the kernel bound through cyclic order 150. The mathematical proof, especially the two exceptional small-order comparisons and the strict Perron–Frobenius inequality for all larger orders, is required for the infinite claim. Numerical checks cannot certify all orders or priority in the literature. Independent audit: not performed.
