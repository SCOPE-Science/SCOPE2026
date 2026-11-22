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

# Finite verification and boundaries

All three reproducibility programs use precisely the Fano-plane incidence graph on seven points and seven lines, with \(21\) flags. They were executed using the source code included in this package and produced the accompanying output files.

- `verify_binary.cpp`: compile with `g++ -O2 -std=c++17 verify_binary.cpp -o verify_binary`, then execute `./verify_binary`. It enumerates every one of the \(2^{21}\) flag subsets; uses a binary-vector incidence model; confirms all \(17\) nonzero coefficients of the complete edge-domination polynomial, the three nonzero inclusion-minimal coefficients \((42,1246,24)\), the maximal-matching coefficients \((42,168,24)\), and the exchange distance profile.
- `verify_cyclic.py`: run `python3 verify_cyclic.py`. It independently builds the cyclic Fano plane, evaluates domination via covered graph vertices, and checks the identical exhaustive polynomials, multiplicities, and exchange geometry.
- `verify_coxeter.py`: run `python3 verify_coxeter.py`. It enumerates exactly all \(\binom{21}{5}\) candidate five-flags, retains the \(42\) optimal matchings, constructs the \(28\) exchange triangles, and verifies an explicit \(28\)-element adjacency-preserving Coxeter permutation in every ordered vertex pair.

Success markers in the output files are `VERIFY_BINARY_OK`, `VERIFY_CYCLIC_OK`, and `VERIFY_COXETER_OK`. The mathematical lower-bound and optimizer classification are also given as structural arguments in `RESULT.md`; finite enumeration is used only to establish exact finite counts and the fixed-graph exchange structure. No infinite-family claim, publication-priority certification, or independent external audit is asserted.
