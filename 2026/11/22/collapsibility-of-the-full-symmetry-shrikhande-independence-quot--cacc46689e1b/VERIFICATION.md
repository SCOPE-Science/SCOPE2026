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

The standalone `verify.py` regenerates the graph and full affine automorphism group, proves the group is exhaustive by a cycle-neighborhood stabilizer bound, enumerates 200 nonempty independent faces and 2,680 barycentric flags, canonicalizes all flags under 192 automorphisms, and obtains exactly 43 quotient cells in dimensions zero through three. It checks oriented boundary-square identities, reads `certificate.json`, validates 21 successive free-face and downward-closure conditions, and confirms that only one zero-cell remains.

Run `python3 verify.py` from the directory containing `certificate.json`. The expected terminal output is stored in `verification_output.txt`. All values are exact finite combinatorial counts; the code needs only Python 3's standard library. This checks the particular graph and group in the theorem, not a general infinite family. Independent mathematical audit has not been performed.
