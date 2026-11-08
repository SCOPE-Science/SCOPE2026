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

The two self-contained Python programs provided here are complete proof checkers for the finite combinatorial certificates. Execute them with Python 3; they use only standard-library modules.

`verify_shrikhande_rook_ind2.py` checks both explicit graph definitions, all sixteen-bit face predicates, deterministic nonempty-face matchings and all Hasse-cover orientations, and exhaustively establishes a topological ordering. It computes signed integer Morse coefficients and verifies a \(+1\) coefficient from critical mask \(340\) to critical mask \(82\), giving a primitive boundary. The recorded terminal line is `INTEGRAL_MORSE_CERTIFICATE_PASS`.

`verify_homology_shrikhande_rook_ind2.py` constructs both graph face complexes by a different edge-generation implementation and performs independently implemented mod-two matrix reductions. Its terminal line is `INDEPENDENT_MOD2_HOMOLOGY_PASS`.

Neither a finite-field rank computation nor numerical Euler characteristic independently proves a homotopy statement. That conclusion follows from Forman's acyclic matching theorem plus the exact integer critical-cell attaching degrees. Independent mathematical auditing has not been performed.
