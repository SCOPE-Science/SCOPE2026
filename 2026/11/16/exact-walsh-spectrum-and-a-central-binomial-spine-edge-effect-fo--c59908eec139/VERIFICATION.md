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

# Finite exact checks and their limits

Run `python3 check_book.py` in the same directory as the six documentation files. The checker uses only the Python standard library and no external data. It enumerates all binary frequencies for sizes 1 through 8 and compares each actual spanning-tree transform with the closed form. It also checks rank, positive Fourier gap, maximum coefficient and the exact endpoint projection norm. An independent signed-Laplacian determinant computation checks 75 reproducible sample frequencies at each size 1 through 15, and the binomial correction identity is checked for sizes 1 through 100. The observed final line is `BOOK_WALSH_EXACT_TESTS_PASS`. Finite testing does not prove the unbounded theorem; proof is in RESULT.md. No external or independent mathematical validation has been performed.
