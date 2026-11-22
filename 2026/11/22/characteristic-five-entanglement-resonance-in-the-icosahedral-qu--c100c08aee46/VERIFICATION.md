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

The supplied scripts use only Python 3's standard library. Run `python3 verify_modular.py` and `python3 verify_smith.py` from the directory containing the extracted files.

`verify_modular.py` constructs the icosahedral edges using a pole-and-pentagons model, enumerates every vertex subset with smaller-side size at most six, computes modular Gaussian-elimination ranks for every prime through \(216\) and for prime \(223\), compares all rank histograms to the stated formulas, and independently checks the twelve pentagon-plus-antipode cuts. Hadamard's bound ensures no new exceptional primes exceed \(216\).

`verify_smith.py` independently constructs the graph from exact golden-ratio coordinates, using no floating point, and computes the gcds of the complete sets of nontrivial square minors through size six by exact Bareiss determinants. It reproduces all Smith classes and verifies the binomial-count totals. Both programs completed successfully and emitted their final `PASS` lines.

The finite exhaustive computations certify the stated twelve-vertex arithmetic census; the mathematical justification for every local prime dimension also uses the general character-orthogonality cut spectrum and Smith-reduction proof in `RESULT.md`. No independent external verification, physical implementation or historical-priority certification has been performed.
