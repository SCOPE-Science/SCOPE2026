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

# Reproducible checks and limits

Run `python verify_transfer.py` with Python 3.10+ and SymPy. It constructs the explicit weighted transfer matrix using the original block permutation, checks the exact determinant and six successive unweighted traces, and prints the isolated spectral statistics. Compare with `transfer_output.txt`.

Compile `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct` and run `./verify_direct`. It enumerates all binary states on four, six, eight and ten column tori and applies the actual two-stage periodic update. Compare its full occupation histograms with `direct_output.txt`.

The determinant check is an exact symbolic computation over integer polynomials; direct enumeration is finite and is not presented as a proof for untested widths. The mathematical proof for arbitrary \(m\ge2\) is the bijection to closed walks plus the formal trace/determinant identity. The Gaussian limit further uses the unique primitive dominant transfer component, exact implicit derivatives and the usual analytic characteristic-function argument. The original 1987 book was not available for complete archival inspection, and independent validation remains not performed.
