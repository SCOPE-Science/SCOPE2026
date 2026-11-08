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

The proof identifies all optimal magnetization sectors analytically. Counts are exact finite sums over completely specified state spaces rather than extrapolated samples.

Run `python3 verify.py` for: the graph's 24 vertices, eight triangle faces and 24 nontriangle edges; all \(6^8\) first-transition triangle selections; all \(4^8\) independent-set candidates; all \(2^6\) zero-field exterior sign assignments; exact comparison against the asserted polynomials.

For a logically separate full-spin check, compile `full_spectrum.cpp` with `c++ -O2 -std=c++17 full_spectrum.cpp -o full_spectrum` and run `./full_spectrum`. This enumerates all \(2^{24}=16,777,216\) spin assignments once, by Gray code, and compares each magnetization-sector minimum and multiplicity to explicit integer tables. This computation is a complete finite check, not an infinite-size theorem.

Graph geometry and incidence are described in `RESULT.md`, so no additional data file or external program is necessary. The known field-four independence polynomial is a cross-check from published graph homotopy work, not an independent originality assertion. Historical priority is provisional and independent scientific validation has not been performed.
