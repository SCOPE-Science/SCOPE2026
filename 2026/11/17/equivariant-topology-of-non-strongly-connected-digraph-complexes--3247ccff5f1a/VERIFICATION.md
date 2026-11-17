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
# Verification and limitations

Run `python3 verify.py` from the directory containing the extracted script. It uses only the Python standard library and requires no external input. Compare standard output with `verification_output.txt`.

Checks actually run: every cycle type in symmetric groups on two through five letters, ten nonidentity cycle types on six letters, every regular cyclic action on two through twelve vertices, and regular actions of the groups \(S_3\), \((C_2)^2\), and \((C_2)^3\). All orbit faces are tested against strong connectivity via transitive closure. Mod-two homology is computed with exact bitset Gaussian elimination, and signed simplicial Euler traces independently compare against classical multilinear free-Lie character values. Observed final marker: `DIRECTED_NONSTRONG_EQUIVARIANT_CHECKS_PASS`.

Finite experiments do not establish the all-n theorem or publication novelty. The universal proof rests on the equivariant poset map, fixed lower-fiber convex nerve, and equivariant Whitehead criterion as detailed in `RESULT.md`. The 1999 primary full text was not accessible; this limitation is not a scientific counterexample.
