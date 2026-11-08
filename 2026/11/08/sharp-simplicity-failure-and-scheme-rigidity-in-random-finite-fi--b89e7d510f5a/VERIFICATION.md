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
The theorem is proved in `RESULT.md` and draws on the established graph-automorphism scheme exact sequence. The included pure-Python `verify.py` is an ordinary direct checker for finite instances; it is not a formal proof or a mathematical independent audit. Run `python3 verify.py` from the directory containing that file. `verify.log` records the exact expected output.

The checker exhaustively enumerates \(\operatorname{GL}_n(\mathbb F_q)\) for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)\), in total 31,617 matrices. It performs modular Gaussian elimination, checks reachability of the nonzero-entry digraph, tests all vertex permutations for graph support symmetries, and enumerates monomial automorphisms over the prime field. Every certificate consisting of strong connectivity, a self-loop, and graph asymmetry gives trivial point automorphism group. The observed certificate failures obey the displayed union bound (where that bound can be larger than one). This independently tests relevant finite consequences but **cannot detect infinitesimal automorphism schemes**, prove an asymptotic coefficient, or establish the group-scheme statement over arbitrary test rings. Those follow from the proof and cited exact sequence.

The exact replay terminates in:

`VERIFY_OK perfect_matrices=31617 cases=7 certificate_no_false_positive=True`

No third-party Python dependencies are needed. All tests are reproducible with the two included files. No external mathematical audit or verification is claimed.
