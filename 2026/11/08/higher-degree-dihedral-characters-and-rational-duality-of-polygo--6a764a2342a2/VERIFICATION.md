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

# Verification notes

Execute `python3 verify.py` with Python 3.9 or later. The program uses only the standard library and prints the exact deterministic results stored in `verification_output.txt`.

The checks calculate induced-component actions and signed Koszul-cell traces independently for all reflections, rotations and relevant degrees on cycles of length four through eleven. They directly verify differential equivariance on monomial supports through length eight, test graded Lefschetz sums and top-orientation characters, and check integrality/nonnegativity of every rational transfer average through length twenty-six.

These are finite corroborations of the general forest/cochain proof. A computation cannot prove a statement for unbounded cycle length, and no automated proof certification or independent mathematical audit is claimed.
