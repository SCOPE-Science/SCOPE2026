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

The main proof certificate is the standalone Python 3 program `verify.py`, which uses no external packages. Execute `python3 verify.py`. Its expected exact output is embedded in `verification_output.txt`. It independently enumerates the simplices by all-mask filtering and by recursion; validates the projective plane incidence axioms; constructs all matching pairs; verifies the full directed incidence DAG; calculates signed integral Morse boundary coefficients; computes mod-two boundary ranks without using Morse theory; and enumerates the projective linear group and every signed Lefschetz trace.

Execute `python3 second_check.py` and compare with `second_output.txt`. This independent implementation starts from affine-chart projective representatives and obtains lines from cross products of pairs, rather than from an orthogonal coefficient-list model. It uses reverse-order pivots, separately computes the integral gradient recursion and verifies the same critical-cell dimensions and zero integer attaching matrix.

The exact first calculation produces 4330 augmented faces, 2145 augmented matching pairs, 40 augmented critical faces, 23140 face-cover relations and no directed cycles. Its reduced integral Morse boundary has size 1 by 39 and is zero. Its mod-two reduced Betti ranks in degrees 0 to 8 are 0,0,0,0,0,1,39,0,0. It checks 5616 projective linear automorphisms; the reduced Lefschetz sum is -5616, yielding zero invariant degree-six homology in characteristic zero. The separate calculation returns `SECOND_CHECK_PASS`.

No computation certifies an infinite family, an integral group-ring decomposition, an equivariant homotopy wedge or a quotient homotopy type. The independent audit field above records that external scientific validation has not been performed.
