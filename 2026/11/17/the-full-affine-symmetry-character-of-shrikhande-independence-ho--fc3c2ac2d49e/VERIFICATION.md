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

# Reproducibility checks

Run `python3 verify.py` with `character_table.csv` in the same directory. This uses the Python 3 standard library only. It constructs the two Cayley-type graph presentations directly from their adjacency rules and enumerates every one of the \(2^{16}\) subsets.

The Shrikhande complex has \(200\) nonempty faces with size distribution \((16,72,96,16)\). Its greedy acyclic face matching consists of \(88\) pairs, leaving one zero-cell and \(23\) two-cells; a complete topological sort checks all \(496\) face-poset incidences. The mod-two augmented boundary ranks are \((1,15,57,16)\). The proof of the integral homotopy type uses the discrete-Morse matching, not an inference from modular ranks.

The twelve Cayley-generator-preserving linear matrices and sixteen translations produce \(192\) distinct graph automorphisms. The six-neighbor induced cycle and the distinct neighbor signatures of nine remaining vertices establish that this is the full graph automorphism group. All \(95{,}232\) signed boundary-equivariance identities are checked. On each automorphism two independent formulas compute the exact signed simplicial trace, and both agree with the row in `character_table.csv`. The full translation Fourier transform uses exact Gaussian integer arithmetic, avoiding numerical approximations; its character multiplicities and the dihedral action on the two-dimensional translation-fixed subspace are explicitly asserted in the verification code.

The executed check printed the exact output in `verification_output.txt` and ended with `FULL_SHRIKHANDE_CHARACTER_VERIFIED_192_PASS`. This is finite exhaustive verification for the stated finite graph, not certification of publication priority, higher graph families, integral representation lattices, or the homotopy types of the quotient spaces. Independent review has not been performed.
