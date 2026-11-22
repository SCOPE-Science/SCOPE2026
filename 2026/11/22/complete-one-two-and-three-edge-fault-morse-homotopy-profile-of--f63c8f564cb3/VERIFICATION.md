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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The complete calculation directly reconstructs all eight symmetry-orbit representatives, checks the 130 covered fault sets, enumerates every simplicial face, verifies the acyclicity of every face-poset gradient matching, checks the exact integral four-to-three cellular boundaries, and computes the reduced mod-two Betti numbers from the unreduced simplicial chain groups. The final success string is `PASS: all 130 fault sets covered by eight orbits; exact integral Morse certificates verified`.

The mathematical argument uses the proven absence of critical one- and two-cells and the Hurewicz isomorphism in degree three to turn the certified zero boundary into nullhomotopic four-cell attachments. The executable certificate verifies the finite claims; it does not by itself establish originality or claims outside at most three edge deletions. Independent validation has not been performed.
