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

# Reproducible checks and boundaries

Run `python3 verify.py` with Python 3.10+ in the directory containing `tree_certificate.json` and the scripts. The program requires no third-party packages and prints a final `ALL FINITE CHECKS PASSED` line. To rebuild the supplied tree independently of its serialization, run `python3 make_certificate.py` and then `python3 verify.py`.

The checker enumerates all proper named-colour assignments for each finite graph. It tests the explicit construction's \(2^{|S|}\) trace patterns for ten parameter/palette pairs. For \(K_{2,2,2}\) at four colours, a separate exhaustive recursive search evaluates every possible binary equality-query split of every reachable surviving concept subset, with exact bit-set intersections and memoization, and finds no complete depth-five tree. The five-colour adaptive tree is checked node-by-node with 64 valid terminal colourings. Palette sizes three through six give concept counts 6, 96, 780 and 4080.

The full arbitrary-parameter VC claim is established by a combinatorial colour-budget upper bound and a Hall-matching construction in `RESULT.md`. The finite checks verify instances and the complete finite octahedral rank table; they do not independently certify the all-parameter theorem. This package has no external proof-assistant certificate or independent mathematical audit.
