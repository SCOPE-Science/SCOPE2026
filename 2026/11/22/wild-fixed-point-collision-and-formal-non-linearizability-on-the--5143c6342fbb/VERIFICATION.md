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

# Verification record

The exact SymPy checker `verify.py` is part of the artifact. Running `python3 verify.py` after installing the requirement in `requirements.txt` reports `QUINTIC_DEL_PEZZO_WILD_FIXED_SCHEME_VERIFIED` and checks:

1. The cross-ratio action has order five as rational functions.
2. Fixed-point elimination produces exactly the quadratic \(u^2-u-1\), with the necessary denominators invertible.
3. Its tangent representation has cyclotomic resultant \(\Phi_5\), and at characteristic five is the displayed nonidentity unipotent Jordan block.
4. The ten boundary divisors form two free five-cycles under relabelling.
5. The quadratic has one length-two root in characteristic five, and its rational root counts agree with sampled prime fields.

The proof of no boundary fixed points uses the SNC geometry of \(\overline M_{0,5}\); the checker verifies the finite permutation combinatorics, not the underlying geometric SNC premise. The failure of formal linearization follows from the fixed-scheme dimension contradiction, not from finite point sampling. Neither a resolution of the wild quotient nor independent external mathematical validation is claimed.
