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

`verify_adpowers.py` uses Python's standard library to build the ten-by-ten matrix of the inner derivation on matrix units and calculate ranks after direct second and third compositions. It checks the complete count for the seven relevant coordinates over fields with \(q=2,3,4,5\), with characteristic-two extension arithmetic for \(\mathbb F_4\). The three higher entries are proven irrelevant, so each seven-coordinate frequency has a free multiplicity \(q^3\). The captured replay is in `verify_output.txt`; all four cases pass. General field validity follows from the symbolic proof, not the computational enumeration.

The validity of the five closed polynomials was additionally checked by expanding the nine mask groups and confirming their sum equals \(q^{10}\) separately in each characteristic branch. The third-power-zero components are reduced varieties; no scheme-multiplicity calculation or claim about the first adjoint-power rank is made.
