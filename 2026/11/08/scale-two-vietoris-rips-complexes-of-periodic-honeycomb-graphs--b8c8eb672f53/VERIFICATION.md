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

# Reproduction and mathematical limits

From the artifact directory run `python3 verify.py`. The only dependency is the Python standard library. The executable reconstructs vertex/edge incidences from the modular definition, computes all shortest distances up to two, constructs all simplices through dimension three, checks all maximum cliques and exceptional triangles, verifies the two facial triangles and two neighboring faces per graph edge, and uses exact binary-elimination boundary ranks to calculate mod-two Betti numbers.

Exhaustive finite instances: \(L=5,6,7,8\). The outputs are captured byte-for-byte in `verification_output.txt`. Each instance verifies the face vector \((2L^2,9L^2,10L^2,2L^2)\), the facial count \(L^2\), and mod-two Betti ranks \(\beta_1=2\), \(\beta_2=L^2+1\), \(\beta_3=0\). The executable is not an exhaustive check for all \(L\), nor does finite-field computation prove torsion-freeness. The unrestricted integral result is established by the explicit collapse and CW attachment proof in `RESULT.md`.

The scientific assessment is same-model only; an independent audit has not been performed.
