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

Execute `python3 verify_outer.py` with a standard Python 3 installation. It requires no third-party libraries.

The script implements the finite-field arithmetic for fields of orders \(2\), \(3\) and \(4\), constructs the derivation maps directly on the incidence-algebra basis, solves the innerness equations by vertex potentials, computes matrix ranks, and compares full/outer/fixed-nonzero-class polynomials. It checks the basis-pair Leibniz equations for explicit derivations. It exhaustively tests six combinations: a four-cycle over fields of orders \(2\), \(3\), and \(4\); a six-cycle over order \(2\); and a four-cycle with a pendant edge over orders \(2\) and \(3\).

For the four-cycle over \(\mathbb F_2\), the outer-class rank multiplicities in ranks \(0\) through \(4\) are \((0,8,24,56,40)\). For the same graph over \(\mathbb F_3\), each of the two nonzero quotient classes has multiplicities \((0,12,126,684,1365)\). For \(\mathbb F_4\), each of the three nonzero classes has \((0,16,336,3376,12656)\). Every test terminates with `VERIFY_OK`.

The finite tests are not a proof for all fields or all graph sizes. The universal proof depends on the derivation normal form, the forest-incidence rank lemma and additive-character orthogonality; it does not rely on a conjectural numerical pattern. Independent review has not been performed.
