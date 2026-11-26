---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Burek §4 provides all six local equations. At v=0 and ∞ the principal part is −z²+4s⁴−q; at v=±1 and ±i it is 4z²−16s⁴−q in the given coordinates (swap the two factor functions for ±i). The weights of x,y,s,z are 1,1,1,2 and all corrections have weight greater than 4. By Euler's identity any common projective zero of q_x,q_y would be a multiple projective root of q, which has four distinct linear factors. Their length is 3·3 as a regular sequence of cubics; the z and s factors of the principal Jacobian have lengths 1 and 3. Semiquasihomogeneous invariance gives μ=27 for the exact germs without claiming analytic equivalence to the initial forms. The Milnor fiber of an isolated complex threefold hypersurface germ is a bouquet of 27 three-spheres, so χ=−26. Burek's 9 is for a surface fiber. Frozen verify.py and its recorded output cover the binary quartic and the weight check at v=0; the other five points were checked from the source, not from a replay of that script. No global smoothing follows.

## originality

FAIL

The number 27 is not quoted as an explicit total-space value in the inspected source; it is nevertheless mechanically implied by stronger local data explicitly given there. The source furnishes the isolated weighted principal form at every point, and the standard semiquasihomogeneous Milnor formula directly determines the invariant and hence the stated fiber topology. This is prior implication, not a finding that Burek printed the number 27.

## value

FAIL

The total-space versus surface distinction is mathematically relevant, but the frozen numerical result follows from the initiating paper by the standard weighted formula and bouquet theorem alone. No new local hypothesis, computation beyond this textbook deduction, or further consequence is required or established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
