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

# Reproduction instructions and limitations

Run `python3 verify.py` from the directory holding this file. The program uses only the standard library and verifies the full simplicial definition independently for \(m=3,4,5\), as well as all action traces for all corresponding group elements. Its expected standard output is `verification_output.txt`. It checks all faces, the union/intersection of the cover, every stated relative free-face pair in the one-pole links, complete mod-two boundary ranks and signed Lefschetz traces.

The **uniform** conclusion is proved in `RESULT.md` by free-face collapses and a contractible-cover suspension argument, with integral Mayer–Vietoris for the group action. Computed mod-two ranks and signed traces are corroboration only; they cannot certify arbitrary \(m\) or rule out all integral torsion in isolation. The proof supplies both statements. Independent audit and outside validation have not been performed.
