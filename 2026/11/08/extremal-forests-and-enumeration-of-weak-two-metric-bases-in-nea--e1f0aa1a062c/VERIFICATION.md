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
# Reproducibility and verification

Execute `python3 artifacts/verify.py` with the Python standard library. It extracts six coefficients from exact bivariate rational polynomials and reconstructs sample minimum bases for every \(8\le n\le16\) and \(n\le m\le2n-5\), testing all pairs of vertices directly.

For a separate small-case exhaustive check, compile `artifacts/verify_six.cpp` with `g++ -O3` and execute the resulting binary. It enumerates all eight-edge subsets of a \(6\times6\) incidence grid, filters positive row/column degrees and single-edge components, and directly checks the weak two-metric inequality for each remaining candidate. The observed count is \(8100\). This is outside the theorem's stated integer range and corroborates the mechanism only.

The proof of the unrestricted theorem is in `RESULT.md`, particularly its non-empty-class, isolated-edge and component-size inequalities. No external prover or independent audit is asserted.
